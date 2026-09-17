from .contracts import CapabilityDescriptor, ComponentDescriptor, ToolDescriptor


class Registry:
    def __init__(self) -> None:
        self.components = self._components()
        self.capabilities = {
            "text-reasoning": CapabilityDescriptor(capability_id="text-reasoning", modality="text", version="reference-0", supports=["W3", "W4"], status="UNAVAILABLE"),
            "vision": CapabilityDescriptor(capability_id="vision", modality="vision", version="reference-0", supports=["W1", "W2"], status="UNAVAILABLE"),
            "ocr": CapabilityDescriptor(capability_id="ocr", modality="ocr", version="reference-0", supports=["W1", "W2"], status="UNAVAILABLE"),
            "embedding": CapabilityDescriptor(capability_id="embedding", modality="embedding", version="reference-0", supports=["retrieval"], status="UNAVAILABLE"),
        }
        self.tools = {
            "search_knowledge": ToolDescriptor(tool_id="search_knowledge", version="reference-0", permissions=["read_evidence"]),
            "generate_artifact": ToolDescriptor(tool_id="generate_artifact", version="reference-0", permissions=["execute_w4"]),
            "execute_code": ToolDescriptor(tool_id="execute_code", version="reference-0", permissions=["execute_w5"], side_effects=["filesystem", "process", "network"]),
        }

    @staticmethod
    def _components() -> dict[str, ComponentDescriptor]:
        entries = [
            ("identity-policy", "Identity and external authorization", "trusted-control", "critical", False),
            ("task-workflow", "Task lifecycle and bounded workflow state", "trusted-control", "critical", False),
            ("capability-registry", "Capability and model metadata", "trusted-control", "high", False),
            ("knowledge-ingestion", "Source, document, revision, and evidence lifecycle", "restricted-data", "critical", False),
            ("document-intelligence", "Document structure and extraction", "restricted-data", "high", True),
            ("retrieval-evidence", "Authorization-aware retrieval and evidence bundles", "evidence", "critical", False),
            ("agent-runtime", "Bounded planning and action requests", "restricted-execution", "critical", False),
            ("tool-runtime", "Explicitly authorized tools", "restricted-execution", "critical", True),
            ("code-sandbox", "Isolated code boundary", "high-risk-boundary", "critical", True),
            ("verification", "Completion and correctness checks", "verification", "critical", False),
            ("artifact-provenance", "Artifacts and source-to-output lineage", "trusted-assurance", "critical", False),
            ("audit-observability", "Audit and operational evidence", "trusted-assurance", "critical", True),
            ("resource-platform", "Resource, deployment, and update management", "infrastructure", "critical", True),
        ]
        return {key: ComponentDescriptor(component_id=key, responsibility=responsibility, trust_zone=zone, criticality=criticality, deployable=deployable) for key, responsibility, zone, criticality, deployable in entries}

    def capability(self, capability_id: str) -> CapabilityDescriptor:
        return self.capabilities[capability_id]

    def tool(self, tool_id: str) -> ToolDescriptor:
        return self.tools[tool_id]
