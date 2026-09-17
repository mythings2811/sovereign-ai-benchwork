from __future__ import annotations

import json
import os

from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from .contracts import SecurityContext, TaskRequest, Workflow
from .deployment import DeploymentManifest, FAILURE_POLICIES
from .evaluation import ExperimentRegistry
from .engine import OfflineWorkbench

app = FastAPI(title="Sovereign Workbench Offline Reference Model", version="0.1.0")
engine = OfflineWorkbench(os.getenv("WORKBENCH_AUDIT_PATH", "runtime/audit.jsonl"))
experiments = ExperimentRegistry()


@app.get("/api/v1/health")
def health() -> dict[str, object]:
    return {"status": "online", "mode": "offline-reference", "model_runtime": "disabled", "external_transfer": False, "workflows": [workflow.value for workflow in Workflow], "pending_validation": experiments.REQUIRED_SPIKES}


@app.get("/api/v1/architecture")
def architecture() -> dict[str, object]:
    return {
        "deployment": DeploymentManifest().model_dump(mode="json"),
        "components": [component.model_dump(mode="json") for component in engine.registry.components.values()],
        "capabilities": [capability.model_dump(mode="json") for capability in engine.registry.capabilities.values()],
        "tools": [tool.model_dump(mode="json") for tool in engine.registry.tools.values()],
        "failure_policies": [policy.model_dump(mode="json") for policy in FAILURE_POLICIES],
    }


@app.get("/api/v1/experiments/pending")
def pending_experiments() -> dict[str, object]:
    return {"status": "VALIDATION_PENDING", "required_spikes": experiments.REQUIRED_SPIKES, "pending": experiments.pending_spikes()}


@app.post("/api/v1/tasks/execute")
def execute(request: TaskRequest):
    return engine.execute(request).model_dump(mode="json")


@app.post("/api/v1/workflows/w2/analyze")
async def analyze_w2(file: UploadFile = File(...), security_context: str = Form(default="")):
    try:
        security = SecurityContext.model_validate_json(security_context) if security_context else SecurityContext()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="security_context must be valid JSON") from exc
    content = await file.read()
    request = TaskRequest(task=f"Analyze uploaded file {file.filename or 'document'}", workflow=Workflow.W2, security=security)
    try:
        result = engine.analyze_file(file.filename or "document", content, file.content_type or "", request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return result.model_dump(mode="json")
