# Sovereign Workbench Model

This is a deterministic, offline reference implementation of the Sovereign Agentic AI Workbench contract. It is a new project and does not modify the existing `Prototype` application.

## Important execution boundary

No LLM, VLM, model server, provider API, API key, external network call, or generated-code executor is used. The health endpoint reports `model_runtime: disabled` and `external_transfer: false`.

The implementation provides deterministic substitutes so the control-plane and workflow contracts can be developed before hardware is available:

- W3: local synthetic evidence retrieval with authority/revision checks, provenance, and abstention.
- W1: supplied report-text observation extraction with explicit human-review status. OCR/model processing is unavailable.
- W2: PDF signature/parsing, image validation, deterministic tag extraction from text, and explicit vision-unavailable status.
- W4: Markdown draft generation that can never become approved automatically.
- W5: blocked until a separately validated sandbox exists.

## Structure

- `workbench_model/contracts.py`: typed task, evidence, provenance, trace, entity, and result contracts.
- `workbench_model/policy.py`: external authorization decisions.
- `workbench_model/engine.py`: deterministic offline workflow engine and audit JSONL writer.
- `workbench_model/api.py`: FastAPI health, task, and W2 upload endpoints.
- `workbench_model/knowledge.py`: source/document/revision/evidence lifecycle with authorization-aware retrieval and revocation.
- `workbench_model/registry.py`: component, capability, and tool registry based on the Phase 12 architecture.
- `workbench_model/verification.py`: independent claim/artifact verification and human approval transition.
- `workbench_model/evaluation.py`: Phase 17 experiment registry with the ten required technical spikes.
- `workbench_model/deployment.py`: reference deployment manifest and fail-closed failure policies.
- `tests/`: no-model tests for workflow behavior and security boundaries.

Inspectable API surfaces:

- `GET /api/v1/health`: offline mode, external-transfer state, workflows, and pending validation.
- `GET /api/v1/architecture`: deployment, components, capabilities, tools, and failure policies.
- `GET /api/v1/experiments/pending`: required Phase 17 spikes and their validation status.
- `POST /api/v1/tasks/execute`: governed W1/W2/W3/W4 task execution; W5 remains blocked.
- `POST /api/v1/workflows/w2/analyze`: validated PDF/image intake with explicit OCR/vision limitations.

## Run locally

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
$env:WORKBENCH_HOST="127.0.0.1"
$env:WORKBENCH_PORT="8010"
python -m uvicorn workbench_model.api:app --host 127.0.0.1 --port 8010
```

OpenAPI is available at `http://127.0.0.1:8010/docs`.

## Test without running a model

```powershell
python -m pytest -q
```

Tests use local synthetic inputs and parser libraries only. The current suite has 13 tests and does not require hardware, model weights, API credentials, or paid services.

## Deliberate limitations

Quantitative quality, hardware feasibility, OCR quality, vision quality, sandbox assurance, zero-egress enforcement outside the process, customer-owned corpus qualification, and production retention policies remain validation items from the supplied requirements. They are represented as explicit unavailable, warning, abstained, or human-review states rather than invented success.
