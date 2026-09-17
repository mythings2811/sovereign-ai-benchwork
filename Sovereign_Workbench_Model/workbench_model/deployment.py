from pydantic import BaseModel, Field


class DeploymentManifest(BaseModel):
    deployment_id: str = "reference-single-node"
    mode: str = "offline-reference"
    host: str = "single controlled workstation/server"
    external_network_default: str = "DENY"
    model_runtime: str = "DISABLED"
    code_execution: str = "DISABLED"
    audit_path: str = "runtime/audit.jsonl"
    required_validation: list[str] = Field(default_factory=lambda: [
        "zero-egress enforcement and observation",
        "sandbox escape resistance",
        "hardware/resource envelope",
        "multimodal quality",
        "customer-corpus qualification",
        "offline update integrity",
    ])


class FailurePolicy(BaseModel):
    failure: str
    immediate_action: str
    user_state: str
    security_impact: str


FAILURE_POLICIES = [
    FailurePolicy(failure="policy failure", immediate_action="deny operation", user_state="BLOCKED", security_impact="fail closed"),
    FailurePolicy(failure="audit failure", immediate_action="stop consequential execution", user_state="FAILED", security_impact="preserve safety over availability"),
    FailurePolicy(failure="resource exhaustion", immediate_action="stop or bound workload", user_state="FAILED", security_impact="no false completion"),
    FailurePolicy(failure="model unavailable", immediate_action="abstain or use deterministic path", user_state="UNAVAILABLE", security_impact="no fabricated output"),
    FailurePolicy(failure="network violation", immediate_action="block and record", user_state="BLOCKED", security_impact="fail closed"),
]
