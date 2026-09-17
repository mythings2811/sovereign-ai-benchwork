from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class Workflow(str, Enum):
    W1 = "W1"
    W2 = "W2"
    W3 = "W3"
    W4 = "W4"
    W5 = "W5"


class ExecutionStatus(str, Enum):
    RECEIVED = "RECEIVED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_WARNINGS = "COMPLETED_WITH_WARNINGS"
    ABSTAINED = "ABSTAINED"
    BLOCKED = "BLOCKED"
    UNAVAILABLE = "UNAVAILABLE"
    FAILED = "FAILED"


class KnowledgeState(str, Enum):
    CANDIDATE = "CANDIDATE"
    VALIDATED = "VALIDATED"
    APPROVED = "APPROVED"
    SUPERSEDED = "SUPERSEDED"
    CONFLICTED = "CONFLICTED"
    UNVERIFIABLE = "UNVERIFIABLE"
    REJECTED = "REJECTED"


class SecurityContext(BaseModel):
    user_identity: str = "evaluation_user"
    role: str = "engineer"
    permissions: set[str] = Field(default_factory=lambda: {"read_evidence", "execute_w3", "execute_w1", "execute_w2", "execute_w4"})
    data_scopes: set[str] = Field(default_factory=lambda: {"standard"})


class TaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=8000)
    workflow: Workflow
    security: SecurityContext = Field(default_factory=SecurityContext)
    inputs: dict[str, Any] = Field(default_factory=dict)


class Evidence(BaseModel):
    evidence_id: str = Field(default_factory=lambda: f"EV-{uuid4().hex[:10]}")
    source: str
    content: str
    state: KnowledgeState = KnowledgeState.VALIDATED
    authority: str = "standard"
    revision: str = "unknown"
    effective_from: str | None = None
    effective_to: str | None = None
    classification: str = "standard"
    owner: str | None = None
    page: int | None = None
    region: str | None = None


class ProvenanceLink(BaseModel):
    output_id: str
    evidence_ids: list[str] = Field(default_factory=list)
    derived_by: str
    verification_state: str = "GENERATED"


class TraceEvent(BaseModel):
    sequence: int
    phase: str
    message: str
    data: dict[str, Any] = Field(default_factory=dict)


class Entity(BaseModel):
    entity_type: str
    tag: str
    description: str
    page: int | None = None
    region: str | None = None
    evidence_text: str
    confidence: float = Field(ge=0, le=1)
    uncertainty: list[str] = Field(default_factory=list)


class Relationship(BaseModel):
    source: str
    target: str
    relationship: str
    evidence_text: str
    confidence: float = Field(ge=0, le=1)
    page: int | None = None


class WorkflowResult(BaseModel):
    execution_id: str = Field(default_factory=lambda: str(uuid4()))
    workflow: Workflow
    status: ExecutionStatus
    result: dict[str, Any] | None = None
    warnings: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    provenance: list[ProvenanceLink] = Field(default_factory=list)
    trace: list[TraceEvent] = Field(default_factory=list)
    requires_human_review: bool = False
    external_transfer: bool = False


class Source(BaseModel):
    source_id: str = Field(default_factory=lambda: f"SRC-{uuid4().hex[:10]}")
    name: str
    owner: str | None = None
    classification: str = "standard"


class Document(BaseModel):
    document_id: str = Field(default_factory=lambda: f"DOC-{uuid4().hex[:10]}")
    source_id: str
    logical_name: str
    document_type: str
    classification: str = "standard"
    allowed_scopes: set[str] = Field(default_factory=lambda: {"standard"})


class DocumentRevision(BaseModel):
    revision_id: str = Field(default_factory=lambda: f"REV-{uuid4().hex[:10]}")
    document_id: str
    revision: str
    content: str
    state: KnowledgeState = KnowledgeState.CANDIDATE
    effective_from: str | None = None
    effective_to: str | None = None


class Claim(BaseModel):
    claim_id: str = Field(default_factory=lambda: f"CLM-{uuid4().hex[:10]}")
    statement: str
    evidence_ids: list[str] = Field(default_factory=list)
    state: KnowledgeState = KnowledgeState.CANDIDATE
    verification_state: str = "GENERATED"


class Artifact(BaseModel):
    artifact_id: str = Field(default_factory=lambda: f"ART-{uuid4().hex[:10]}")
    artifact_type: str
    content: str
    claim_ids: list[str] = Field(default_factory=list)
    state: str = "GENERATED"
    approval_required: bool = True


class ApprovalDecision(BaseModel):
    artifact_id: str
    reviewer: str
    decision: str
    reason: str


class VerificationRecord(BaseModel):
    verification_id: str = Field(default_factory=lambda: f"VER-{uuid4().hex[:10]}")
    subject_id: str
    checks: list[str] = Field(default_factory=list)
    status: str
    verifier: str = "deterministic-reference-checks"
    notes: list[str] = Field(default_factory=list)


class CapabilityDescriptor(BaseModel):
    capability_id: str
    modality: str
    version: str
    enabled: bool = False
    local_only: bool = True
    supports: list[str] = Field(default_factory=list)
    status: str = "UNAVAILABLE"


class ToolDescriptor(BaseModel):
    tool_id: str
    version: str
    permissions: list[str] = Field(default_factory=list)
    side_effects: list[str] = Field(default_factory=list)
    enabled: bool = False


class ComponentDescriptor(BaseModel):
    component_id: str
    responsibility: str
    trust_zone: str
    criticality: str
    state: str = "DEFINED"
    deployable: bool = False


class ExperimentRecord(BaseModel):
    experiment_id: str
    assumption: str
    hypothesis: str
    workflow: Workflow | None = None
    dataset_fingerprint: str | None = None
    ground_truth_status: str = "GROUND_TRUTH_UNAVAILABLE"
    metrics: dict[str, float] = Field(default_factory=dict)
    status: str = "PENDING"
    decision: str = "PENDING"
    notes: list[str] = Field(default_factory=list)
