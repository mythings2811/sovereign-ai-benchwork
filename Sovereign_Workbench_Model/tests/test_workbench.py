import io

from fastapi.testclient import TestClient
from PIL import Image
from pypdf import PdfWriter

from workbench_model.api import app
from workbench_model.contracts import ApprovalDecision, Artifact, Claim, Document, Evidence, ExperimentRecord, SecurityContext, Source, TaskRequest, Workflow
from workbench_model.engine import OfflineWorkbench
from workbench_model.evaluation import ExperimentRegistry
from workbench_model.knowledge import KnowledgeManager
from workbench_model.verification import VerificationEngine


client = TestClient(app)


def pdf_bytes():
    output = io.BytesIO()
    writer = PdfWriter()
    writer.add_blank_page(width=300, height=300)
    writer.write(output)
    return output.getvalue()


def png_bytes():
    output = io.BytesIO()
    Image.new("RGB", (20, 20), "white").save(output, format="PNG")
    return output.getvalue()


def test_health_declares_model_runtime_disabled():
    body = client.get("/api/v1/health").json()
    assert body["model_runtime"] == "disabled"
    assert body["external_transfer"] is False


def test_w3_returns_evidence_and_provenance_without_model():
    engine = OfflineWorkbench("runtime/test-audit.jsonl")
    result = engine.execute(TaskRequest(task="What is required for P-101A diagnostics?", workflow=Workflow.W3))
    assert result.status == "COMPLETED"
    assert result.evidence
    assert result.provenance[0].verification_state == "VERIFIED"
    assert result.external_transfer is False


def test_w3_abstains_when_evidence_is_missing():
    result = OfflineWorkbench("runtime/test-audit.jsonl").execute(TaskRequest(task="What is the turbine inspection policy?", workflow=Workflow.W3))
    assert result.status == "ABSTAINED"
    assert result.requires_human_review is True


def test_w2_text_extracts_entities_but_requires_review():
    result = OfflineWorkbench("runtime/test-audit.jsonl").execute(TaskRequest(task="analyze", workflow=Workflow.W2, inputs={"text": "P-101A connects to 6-CS-101 and FIT-200."}))
    assert result.status == "COMPLETED_WITH_WARNINGS"
    assert {entity["tag"] for entity in result.result["entities"]} == {"P-101A", "6-CS-101", "FIT-200"}
    assert result.requires_human_review is True


def test_w2_valid_pdf_returns_needs_ocr_warning():
    response = client.post("/api/v1/workflows/w2/analyze", files={"file": ("drawing.pdf", pdf_bytes(), "application/pdf")})
    assert response.status_code == 200
    body = response.json()
    assert any("OCR" in warning for warning in body["warnings"])


def test_w2_image_is_explicitly_unavailable_without_vision_runtime():
    response = client.post("/api/v1/workflows/w2/analyze", files={"file": ("drawing.png", png_bytes(), "image/png")})
    assert response.status_code == 200
    assert response.json()["status"] == "UNAVAILABLE"


def test_w5_is_blocked_by_policy():
    result = OfflineWorkbench("runtime/test-audit.jsonl").execute(TaskRequest(task="run code", workflow=Workflow.W5))
    assert result.status == "BLOCKED"


def test_w4_never_marks_artifact_approved():
    result = OfflineWorkbench("runtime/test-audit.jsonl").execute(TaskRequest(task="draft report", workflow=Workflow.W4, inputs={"source": "Observed corrosion on P-101A."}))
    assert result.result["approval_state"] == "HUMAN_REVIEW_REQUIRED"


def test_architecture_endpoint_exposes_components_and_disabled_capabilities():
    body = client.get("/api/v1/architecture").json()
    assert len(body["components"]) >= 12
    assert body["deployment"]["external_network_default"] == "DENY"
    assert all(capability["enabled"] is False for capability in body["capabilities"])


def test_phase17_spikes_remain_pending_until_empirical_evidence_exists():
    body = client.get("/api/v1/experiments/pending").json()
    assert body["status"] == "VALIDATION_PENDING"
    assert body["pending"] == [f"SP-{index:02d}" for index in range(1, 11)]


def test_knowledge_lifecycle_requires_source_and_excludes_revoked_evidence():
    manager = KnowledgeManager()
    source = manager.register_source(Source(name="test source"))
    document = manager.register_document(Document(source_id=source.source_id, logical_name="manual", document_type="pdf"))
    evidence = manager.add_evidence(Evidence(source="manual", content="isolation procedure", classification="standard"), document.document_id)
    assert manager.retrieve("isolation procedure", {"standard"})
    manager.revoke(evidence.evidence_id)
    assert manager.retrieve("isolation procedure", {"standard"}) == []


def test_verification_and_approval_remain_separate():
    verifier = VerificationEngine()
    claim = Claim(statement="Observed fact", evidence_ids=["EV-1"])
    assert verifier.verify_claim(claim).status == "PASSED"
    artifact = Artifact(artifact_type="report", content="draft")
    assert verifier.verify_artifact(artifact).status == "PASSED"
    assert artifact.state == "GENERATED"
    verifier.approve_artifact(artifact, ApprovalDecision(artifact_id=artifact.artifact_id, reviewer="engineer", decision="APPROVED", reason="Reviewed"))
    assert artifact.state == "APPROVED"


def test_experiment_registry_persists_recorded_results(tmp_path):
    registry = ExperimentRegistry(tmp_path / "experiments.jsonl")
    registry.register(ExperimentRecord(experiment_id="SP-01", assumption="local model", hypothesis="works"))
    record = registry.record_result("SP-01", {"latency": 1.0}, "COMPLETED", "REQUIRES_VALIDATION")
    assert record.decision == "REQUIRES_VALIDATION"
    assert "SP-01" not in registry.pending_spikes()
