import io
import asyncio

import httpx
import pytest
from fastapi.testclient import TestClient
from PIL import Image
from pypdf import PdfWriter

import backend_mvp


client = TestClient(backend_mvp.app)
PERMITTED = '{"user_identity":"test","role":"engineer","data_permissions":["standard"],"tool_permissions":["extract_pid_entities"]}'
DENIED = '{"user_identity":"test","role":"engineer","data_permissions":["standard"],"tool_permissions":[]}'


def pdf_bytes(text="P-101A is connected to 6-CS-101"):
    output = io.BytesIO()
    writer = PdfWriter()
    writer.add_blank_page(width=300, height=300)
    writer.write(output)
    # A blank page is intentional: extraction behavior is tested separately from
    # the parser's ability to accept a valid PDF container.
    return output.getvalue()


def png_bytes():
    output = io.BytesIO()
    Image.new("RGB", (40, 20), "white").save(output, format="PNG")
    return output.getvalue()


def test_valid_pdf_upload_returns_structured_result():
    response = client.post(
        "/api/v1/workflows/w2/analyze",
        files={"file": ("drawing.pdf", pdf_bytes(), "application/pdf")},
        data={"security_context": PERMITTED},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["workflow"] == "W2"
    assert body["result"]["pages_processed"] == 1
    assert body["trace"][-1].startswith("VERIFY:")


def test_valid_image_requires_explicit_vision_configuration(monkeypatch):
    monkeypatch.setattr(backend_mvp, "W2_VISION_ENABLED", False)
    response = client.post(
        "/api/v1/workflows/w2/analyze",
        files={"file": ("drawing.png", png_bytes(), "image/png")},
        data={"security_context": PERMITTED},
    )
    assert response.status_code == 503
    assert "vision-capable model" in response.json()["detail"]


@pytest.mark.parametrize(
    "filename, content_type, content, status",
    [
        ("empty.pdf", "application/pdf", b"", 400),
        ("drawing.exe", "application/octet-stream", b"MZ", 415),
        ("drawing.pdf", "application/pdf", b"not a pdf", 400),
        ("drawing.png", "image/png", b"not an image", 400),
    ],
)
def test_upload_validation(filename, content_type, content, status):
    response = client.post(
        "/api/v1/workflows/w2/analyze",
        files={"file": (filename, content, content_type)},
        data={"security_context": PERMITTED},
    )
    assert response.status_code == status


def test_missing_w2_permission_is_rejected_before_processing():
    response = client.post(
        "/api/v1/workflows/w2/analyze",
        files={"file": ("drawing.pdf", pdf_bytes(), "application/pdf")},
        data={"security_context": DENIED},
    )
    assert response.status_code == 403


def test_oversized_upload_is_rejected(monkeypatch):
    monkeypatch.setattr(backend_mvp, "W2_MAX_UPLOAD_BYTES", 10)
    response = client.post(
        "/api/v1/workflows/w2/analyze",
        files={"file": ("drawing.pdf", b"%PDF-1.7 more than ten", "application/pdf")},
        data={"security_context": PERMITTED},
    )
    assert response.status_code == 413


def test_w5_remains_blocked():
    response = client.post(
        "/api/v1/task/execute",
        json={"user_request": "run code", "workflow_class": "W5", "security_context": {"role": "engineer"}},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "BLOCKED"


class FakeClient:
    def __init__(self, result):
        self.result = result

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return None

    async def post(self, *_args, **_kwargs):
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def test_vision_provider_timeout_is_actionable(monkeypatch):
    monkeypatch.setattr(backend_mvp, "W2_VISION_ENABLED", True)
    monkeypatch.setattr(backend_mvp, "MODEL_VISION", "vision-test")
    monkeypatch.setattr(backend_mvp, "API_KEY", "test-key")
    monkeypatch.setattr(backend_mvp.httpx, "AsyncClient", lambda **_kwargs: FakeClient(httpx.TimeoutException("timeout")))
    with pytest.raises(backend_mvp.HTTPException) as error:
        asyncio.run(backend_mvp._vision_result("drawing.png", ".png", png_bytes(), []))
    assert error.value.status_code == 504


def test_vision_schema_mismatch_is_rejected(monkeypatch):
    monkeypatch.setattr(backend_mvp, "W2_VISION_ENABLED", True)
    monkeypatch.setattr(backend_mvp, "MODEL_VISION", "vision-test")
    monkeypatch.setattr(backend_mvp, "API_KEY", "test-key")
    response = FakeResponse({"choices": [{"message": {"content": "not json"}}]})
    monkeypatch.setattr(backend_mvp.httpx, "AsyncClient", lambda **_kwargs: FakeClient(response))
    with pytest.raises(backend_mvp.HTTPException) as error:
        asyncio.run(backend_mvp._vision_result("drawing.png", ".png", png_bytes(), []))
    assert error.value.status_code == 502
