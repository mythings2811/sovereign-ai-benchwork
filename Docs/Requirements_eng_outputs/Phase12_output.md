# 1. Document Control

| Field | Decision |
|---|---|
| Product | Sovereign Agentic AI Workbench |
| Phase | 12 |
| Document | Component Architecture Specification |
| Predecessors | PRD → SRS → System Architecture → Phase 11 Technology Baseline |
| Primary purpose | Define implementable component boundaries |
| Deployment target | Single self-hosted workstation/server for MVP |
| Architecture style | Modular single-node with protected execution boundaries |
| Core control principle | External authority controls AI-generated actions |
| Core data principle | Evidence is a first-class object |
| Core security principle | Untrusted content never acquires control-plane authority |
| Technology baseline | Phase 11 |
| Numerical thresholds | Requires Validation where not already established |
| Status | **COMPONENT ARCHITECTURE BASELINE ESTABLISHED — IMPLEMENTATION-READY WITH TARGETED VALIDATION** |

---

# 2. Architectural Position

The approved progression is:

```text
PRD
"What must the product accomplish?"
        ↓
SRS
"What must the system provide?"
        ↓
SYSTEM ARCHITECTURE
"How is the system structurally organized?"
        ↓
PHASE 11
"Which technologies satisfy the architecture?"
        ↓
PHASE 12
"What implementable components own the responsibilities?"
        ↓
PHASE 13
"How are those components internally designed?"
        ↓
IMPLEMENTATION
```

The SRS defines the system as an execution environment rather than a chatbot or simple RAG system. Its core lifecycle is:

```text
USER TASK
    ↓
TASK UNDERSTANDING
    ↓
EVIDENCE / CAPABILITY REQUIREMENT
    ↓
AUTHORIZED KNOWLEDGE + LOCAL PROCESSING
    ↓
REASON / PLAN
    ↓
BOUNDED EXECUTION
    ↓
VERIFY
    ↓
RESULT / ARTIFACT
    ↓
PROVENANCE + AUDIT
```

The system must also preserve:

```text
GENERATED
    ↓
CHECKED
    ↓
VERIFIED
    ↓
HUMAN-APPROVED WHERE REQUIRED
```

These states cannot be collapsed.

---

# 3. Component Architecture Principles

## 3.1 Single-node does not mean monolithic

The MVP is deployed as one logical system on one workstation/server, but its internal responsibilities remain explicitly separated.

The preferred structure is therefore:

```text
                 ┌─────────────────────────────┐
                 │       USER INTERFACE        │
                 └──────────────┬──────────────┘
                                │
                 ┌──────────────▼──────────────┐
                 │     APPLICATION API         │
                 └──────────────┬──────────────┘
                                │
        ┌───────────────────────▼──────────────────────┐
        │             CONTROL PLANE                    │
        │                                               │
        │ Identity | Policy | Task | Workflow | State  │
        └───────────────────────┬──────────────────────┘
                                │
                 ┌──────────────▼──────────────┐
                 │       AGENT RUNTIME         │
                 └───────┬─────────┬───────────┘
                         │         │
             ┌───────────▼───┐ ┌──▼────────────────┐
             │ MODEL ROUTER  │ │ CAPABILITY REG.  │
             └───────┬───────┘ └───────────────────┘
                     │
             ┌───────▼───────────┐
             │ INFERENCE GATEWAY │
             └───────┬───────────┘
                     │
          ┌──────────┴──────────┐
          │                     │
     Text Models            Vision Models
          │                     │
          └──────────┬──────────┘
                     │
       ┌─────────────▼────────────────┐
       │       KNOWLEDGE PLANE        │
       │                              │
       │ Ingestion → Processing →     │
       │ Retrieval → Evidence         │
       └─────────────┬────────────────┘
                     │
        ┌────────────▼─────────────┐
        │      EXECUTION PLANE     │
        │                          │
        │ Tools → Sandbox → Files  │
        └────────────┬─────────────┘
                     │
             ┌───────▼────────┐
             │ VERIFICATION   │
             └───────┬────────┘
                     │
        ┌────────────▼─────────────┐
        │ ARTIFACT + PROVENANCE    │
        └────────────┬─────────────┘
                     │
        ┌────────────▼─────────────┐
        │ AUDIT + OBSERVABILITY    │
        └──────────────────────────┘

        Independent host/network security boundary
```

## 3.2 Architectural rule

A component receives authority only from the component that owns that authority.

In particular:

```text
MODEL OUTPUT
    ≠
AUTHORIZATION

AGENT PLAN
    ≠
PERMISSION

RETRIEVED DOCUMENT
    ≠
SYSTEM INSTRUCTION

TOOL REQUEST
    ≠
TOOL AUTHORIZATION

CODE EXECUTION SUCCESS
    ≠
CORRECTNESS

ARTIFACT EXISTENCE
    ≠
VERIFICATION
```

These distinctions are direct consequences of the SRS security, agent, verification, and evidence requirements. 
---

# 4. Master Component Registry

The 30 candidate subsystems from the Phase 12 prompt are consolidated into **24 architectural components**. Some are modules rather than deployable services because creating 30 independently deployed services on the MVP's single node would add failure and operational complexity without creating useful boundaries.

| ID | Component | Category | Primary responsibility | State | Trust zone | Criticality | Deployable | MVP |
|---|---|---|---|---|---|---|---|---|
| CMP-001 | Identity & Authorization | Security / Control | Establish identity and authorization context | Auth state | Trusted control | Critical | No | Yes |
| CMP-002 | Policy Engine | Security / Control | Evaluate policy decisions | Policy/config | Trusted control | Critical | No | Yes |
| CMP-003 | Task Manager | Control | Own task identity/lifecycle | Task state | Trusted control | Critical | No | Yes |
| CMP-004 | Workflow Engine | Control / Execution | Deterministic workflow control | Workflow state | Trusted control | Critical | No | Yes |
| CMP-005 | Execution State Manager | Control | Durable execution state | Execution state | Trusted control | Critical | No | Yes |
| CMP-006 | Capability Registry | AI Capability | Describe models/tools/capabilities | Registry state | Trusted control | High | No | Yes |
| CMP-007 | Model Router | AI Capability / Control | Select permitted capability | Routing state | Trusted control | High | No | Yes |
| CMP-008 | AI Inference Gateway | AI Capability | Abstract model execution | Runtime/cache | AI execution | Critical | Yes | Yes |
| CMP-009 | Agent Runtime | Execution | Plan and perform bounded reasoning | Agent state | Restricted execution | Critical | No | Yes |
| CMP-010 | Knowledge Ingestion Manager | Knowledge | Govern source ingestion | Ingestion state | Knowledge | High | No | Yes |
| CMP-011 | Document Intelligence Engine | Knowledge | Parse/structure documents | Processing state | Restricted data | High | Yes/module | Yes |
| CMP-012 | OCR Capability | AI Capability / Knowledge | Extract text/layout from images | Processing state | Restricted data | High | No | Yes |
| CMP-013 | Multimodal Processing Engine | AI Capability / Knowledge | Visual understanding | Processing state | Restricted data | Critical | No | Yes |
| CMP-014 | Engineering Drawing Processor | Knowledge | Produce drawing/P&ID representation | Derived state | Restricted data | Critical | No | Yes |
| CMP-015 | Retrieval Engine | Knowledge | Authorization-aware search | Index/query state | Knowledge | Critical | Yes/module | Yes |
| CMP-016 | Evidence Manager | Evidence | Own evidence lifecycle | Evidence state | Evidence | Critical | No | Yes |
| CMP-017 | Tool Registry | Execution / Security | Define governed tools | Registry state | Trusted control | Critical | No | Yes |
| CMP-018 | Tool Runtime | Execution / Security | Execute authorized tools | Execution state | Restricted execution | Critical | Yes/module | Yes |
| CMP-019 | Code Sandbox | Execution / Security | Isolate untrusted code | Ephemeral state | High-risk boundary | Critical | Yes | Conditional |
| CMP-020 | Verification Engine | Verification | Determine acceptable completion | Verification state | Verification | Critical | No | Yes |
| CMP-021 | Artifact Generator | Artifact | Generate enterprise deliverables | Artifact state | Restricted output | High | No | Yes |
| CMP-022 | Provenance Manager | Evidence / Assurance | Maintain source→claim→artifact lineage | Provenance state | Trusted assurance | Critical | No | Yes |
| CMP-023 | Audit & Observability | Assurance | Record audit and operational telemetry | Audit/telemetry | Trusted assurance | Critical | Module/service | Yes |
| CMP-024 | Resource & Platform Manager | Infrastructure | Manage compute, storage, deployment, updates | Platform state | Infrastructure | Critical | Yes | Yes |

---

# 5. Why 24 Components Instead of 30 Services

The Phase 12 prompt explicitly states that every candidate subsystem must be classified as a component, module, subsystem, service, library, runtime, infrastructure component, or shared capability rather than automatically becoming a deployable service.

The resulting rule is:

### Separate architectural ownership where:

- authority differs;
- security boundary differs;
- state ownership differs;
- failure isolation matters;
- replacement is independently useful;
- scaling/resource behavior differs;
- independent testing materially improves assurance.

### Keep as modules where:

- they share the same trust boundary;
- independent deployment creates little value;
- their lifecycle is tightly coupled;
- independent failure isolation is unnecessary;
- the MVP would otherwise become operationally fragmented.

Therefore:

```text
OCR
Multimodal
P&ID
Retrieval
Evidence
```

are architectural responsibilities but do not automatically become five network services.

Likewise:

```text
Task
Workflow
Execution State
Policy
Authorization
```

remain distinct ownership domains while living inside the application control plane.

This is deliberate **modular architecture, not microservice architecture**.

---

# 6. Control Plane

## CMP-001 — Identity & Authorization

### Responsibility

This component is responsible for establishing:

- authenticated principal;
- roles;
- permissions;
- session identity;
- task identity context;
- resource access rights;
- document access rights;
- tool authorization;
- approval authority.

### Not responsible for

It does **not**:

- execute tools;
- execute models;
- decide whether evidence is semantically correct;
- determine engineering correctness;
- allow the agent to modify permissions.

### Authority

It answers:

```text
WHO IS ACTING?
WHAT AUTHORITY DOES THAT PRINCIPAL POSSESS?
WHAT RESOURCES MAY THAT PRINCIPAL ACCESS?
```

It does not answer:

```text
WHAT SHOULD THE AGENT DO?
```

### Key interface

```text
authorize(
    principal,
    task_context,
    resource,
    requested_action
)
        ↓
ALLOW | DENY | REQUIRE_APPROVAL
```

### State owner

Authoritative owner of authorization context.

### Security

This is a trusted control-plane component. Compromise is critical because authorization bypass can expose enterprise data.

---

# 7. CMP-002 — Policy Engine

### Responsibility

Evaluates organizational/system policy independently of model output.

Policies cover:

- data access;
- model use;
- tool use;
- code execution;
- network access;
- artifact release;
- autonomy;
- approval requirements;
- data handling.

### Not responsible for

It does not:

- authenticate users;
- execute tools;
- generate model responses;
- decide semantic correctness.

### Decision contract

```text
POLICY_REQUEST
    ↓
VALIDATE
    ↓
EVALUATE
    ↓
ALLOW
DENY
REQUIRE_APPROVAL
ESCALATE
ABSTAIN
```

Policies must be executable system controls, not prompt instructions. The SRS explicitly requires authorization to be independently enforceable and security-critical configuration to be protected from the agent.

---

# 8. CMP-003 — Task Manager

Owns:

- task identity;
- task creation;
- task metadata;
- task inputs;
- task permissions;
- task lifecycle;
- cancellation;
- completion state.

### Lifecycle

```text
CREATED
 ↓
VALIDATING
 ↓
CLASSIFIED
 ↓
PLANNED
 ↓
EXECUTING
 ↓
VERIFYING
 ↓
COMPLETED
```

Exceptional states:

```text
BLOCKED
FAILED
ESCALATED
ABSTAINED
CANCELLED
TIMEOUT
RESOURCE_EXHAUSTED
SECURITY_VIOLATION
```

### Critical invariant

Task completion is system-owned.

The LLM cannot transition a task directly to `COMPLETED`.

This directly implements the SRS requirement that completion be determined independently of model-generated claims.

---

# 9. CMP-004 — Workflow Engine

The workflow engine owns deterministic control.

### Deterministic responsibilities

- approval gates;
- verification gates;
- retry limits;
- timeout;
- cancellation;
- state transitions;
- artifact release;
- completion predicates;
- escalation;
- audit event generation.

### Agent responsibility

The agent proposes:

```text
WHAT SHOULD HAPPEN NEXT?
```

The workflow engine determines:

```text
IS THAT STEP PERMITTED?
IS THAT STATE TRANSITION VALID?
HAS THE REQUIRED CONDITION BEEN MET?
```

This separation prevents the agent runtime from becoming the system authority.

---

# 10. CMP-005 — Execution State Manager

Owns durable state for:

- task;
- workflow;
- plan;
- step;
- tool call;
- model invocation;
- evidence request;
- verification;
- artifact;
- approval;
- failure;
- retry.

### Required operations

```text
create
read
update
checkpoint
pause
resume
cancel
recover
replay-where-safe
```

### Important distinction

Checkpointing does not imply exactly-once execution.

Side-effecting operations therefore require:

```text
idempotency key
+
execution receipt
+
state transition
```

to avoid duplicate external/local side effects.

---

# 11. AI Capability Plane

## CMP-006 — Model / Capability Registry

The registry owns metadata describing:

```text
MODEL
    ↓
MODEL VERSION
    ↓
MODEL CONFIGURATION
    ↓
CAPABILITY
    ↓
RESOURCE PROFILE
    ↓
POLICY COMPATIBILITY
```

It stores:

- model identity;
- version;
- checksum;
- license metadata;
- modality;
- context limits;
- structured-output support;
- tool-calling support;
- hardware profile;
- quantization variant;
- capability class;
- availability;
- lifecycle state.

### Model lifecycle

```text
REGISTERED
 ↓
VALIDATED
 ↓
AVAILABLE
 ↓
LOADED
 ↓
SERVING
 ↓
UNLOADED
 ↓
DEPRECATED
 ↓
REMOVED
```

---

# 12. CMP-007 — Model Router

### Inputs

```text
TASK
+
REQUIRED CAPABILITY
+
RISK
+
EVIDENCE REQUIREMENT
+
POLICY
+
RESOURCE CONSTRAINT
+
AVAILABLE MODELS
```

### Output

```text
SELECTED CAPABILITY
SELECTED MODEL
MODEL CONFIGURATION
RESOURCE RESERVATION
ROUTING DECISION
FALLBACK POLICY
```

### Routing must not bypass

- authorization;
- policy;
- resource management;
- sovereignty;
- capability availability.

### Routing strategy

The architecture supports:

```text
cheap/small model
      ↓
quality check
      ↓
escalate if necessary
      ↓
larger/specialized model
      ↓
verification
```

The router is therefore not simply a "best model classifier"; it is a **policy- and resource-aware capability selector**.

---

# 13. CMP-008 — AI Inference Gateway

This is the stable interface between the application and model-serving infrastructure.

### Responsibilities

- model invocation;
- model loading/unloading;
- structured generation;
- tool-call generation;
- streaming;
- cancellation;
- context submission;
- resource reservation;
- inference telemetry;
- capability version recording.

### Interface abstraction

```text
InferenceRequest
{
    task_id
    invocation_id
    capability_id
    model_id
    model_version
    input
    context_refs
    output_schema
    resource_budget
    security_context
}
```

```text
InferenceResult
{
    invocation_id
    output
    model_identity
    capability_identity
    usage
    termination_reason
    verification_state
}
```

The rest of the application must not directly depend on vLLM, llama.cpp, or an individual model implementation.

---

# 14. CMP-009 — Agent Runtime

The agent runtime is an **execution subsystem**, not an authority subsystem.

### Agent loop

```text
OBSERVE
   ↓
UNDERSTAND
   ↓
PLAN
   ↓
REQUEST POLICY CHECK
   ↓
SELECT ACTION
   ↓
EXECUTE
   ↓
OBSERVE RESULT
   ↓
VERIFY
   ↓
CONTINUE
CORRECT
ESCALATE
STOP
ABSTAIN
```

### Agent may

- decompose;
- plan;
- request evidence;
- request tools;
- inspect results;
- request model escalation;
- retry permitted transient failures;
- correct semantic failures;
- escalate;
- stop;
- abstain.

### Agent may not

- change policy;
- change permissions;
- grant itself access;
- authorize consequential actions;
- bypass verification;
- bypass sandbox;
- bypass network controls.

---

# 15. Knowledge Plane

## CMP-010 — Knowledge Ingestion Manager

Pipeline:

```text
SOURCE
 ↓
AUTHORIZATION CHECK
 ↓
INGEST
 ↓
VALIDATE
 ↓
CLASSIFY
 ↓
PROCESS
 ↓
REGISTER
```

Owns ingestion lifecycle, source identity, authorization context, revision metadata, and ingestion status.

It does not decide whether extracted content is authoritative engineering truth.

---

# 16. CMP-011 — Document Intelligence Engine

Handles:

- PDF;
- DOCX;
- XLSX;
- CSV;
- scans;
- images;
- technical reports;
- tables;
- drawings.

### Output

Not merely text.

It produces a structured representation containing:

```text
document
pages
regions
blocks
tables
relationships
coordinates
metadata
revision
processing provenance
```

This is required because the SRS explicitly requires preservation of source location, structure, revision, extraction context, and provenance.

---

# 17. CMP-012 — OCR Capability

OCR is treated as a specialized capability.

### Input

```text
image/page/region
```

### Output

```text
OCR_TEXT
BOUNDING_BOX
PAGE
LANGUAGE
CONFIDENCE
LAYOUT_METADATA
```

### Critical trust rule

```text
OCR OUTPUT
    ≠
TRUSTED FACT
```

OCR output becomes evidence only after the evidence pipeline records its origin and processing state.

---

# 18. CMP-013 — Multimodal Processing Engine

Separates:

1. visual extraction;
2. interpretation;
3. spatial reasoning;
4. cross-modal reasoning;
5. consequential conclusion.

Pipeline:

```text
IMAGE / DOCUMENT
       ↓
VISUAL PROCESSING
       ↓
DETECTED ELEMENTS
       ↓
SPATIAL RELATIONSHIPS
       ↓
STRUCTURED REPRESENTATION
       ↓
EVIDENCE
       ↓
REASONING
```

The architecture must not treat "vision-capable LLM" as equivalent to a complete multimodal subsystem.

---

# 19. CMP-014 — Engineering Drawing / P&ID Processor

This is one of the most important domain-specific components.

### Processing chain

```text
DRAWING
   ↓
VISUAL OBSERVATIONS
   ↓
OCR / TEXT
   ↓
SYMBOL DETECTION
   ↓
TAG DETECTION
   ↓
LINE DETECTION
   ↓
RELATIONSHIP DETECTION
   ↓
CONNECTIVITY
   ↓
STRUCTURED ENGINEERING REPRESENTATION
   ↓
VERIFICATION
   ↓
ENGINEERING INTERPRETATION
```

### Representation must distinguish

```text
OBSERVED
DETECTED
INFERRED
VERIFIED
ENGINEERING INTERPRETATION
```

A VLM is therefore a component in this pipeline, not the final P&ID truth source.

The SRS explicitly requires visual recognition, structural representation, interpretation, and consequential engineering authority to remain separate.

---

# 20. CMP-015 — Retrieval Engine

Retrieval supports:

- keyword search;
- semantic search;
- metadata filtering;
- hybrid search;
- authorization filtering;
- revision filtering;
- temporal filtering;
- authority filtering;
- provenance filtering.

### Retrieval contract

```text
QUERY
+
SECURITY CONTEXT
+
TASK CONTEXT
+
TEMPORAL CONSTRAINT
+
REVISION CONSTRAINT
+
AUTHORITY CONSTRAINT
        ↓
AUTHORIZED EVIDENCE REFERENCES
```

It must not return anonymous text chunks.

It returns evidence references with sufficient metadata for downstream evidence assessment.

---

# 21. CMP-016 — Evidence Manager

Evidence is a first-class system object.

### Canonical evidence object

```text
Evidence
├── evidence_id
├── source_id
├── source_type
├── source_location
├── document_version
├── page
├── region
├── coordinates
├── authorization
├── authority
├── temporal_validity
├── extraction_context
├── content_reference
├── processing_state
├── verification_state
├── conflict_state
└── provenance
```

### Evidence states

```text
SUFFICIENT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
UNVERIFIABLE
```

### State behavior

| State | System action |
|---|---|
| SUFFICIENT | Permit applicable reasoning |
| INSUFFICIENT | Retrieve, ask, escalate, abstain or stop |
| CONFLICTED | Surface conflict; do not silently choose |
| STALE | Reject as current authority unless historical use is explicit |
| UNAUTHORIZED | Deny |
| UNVERIFIABLE | Do not represent as established fact |

The SRS requires exactly this distinction and prohibits fabricating evidence to satisfy workflow completion.

---

# 22. Execution Plane

## CMP-017 — Tool Registry

Every tool has:

```text
tool_id
version
description
capability
input_schema
output_schema
permissions
risk_level
resource_requirements
allowed_principals
allowed_tasks
sandbox_requirement
network_requirement
audit_requirement
side_effect_class
```

No arbitrary host capability becomes a tool.

---

# 23. CMP-018 — Tool Runtime

Execution contract:

```text
AGENT REQUEST
      ↓
POLICY CHECK
      ↓
AUTHORIZATION
      ↓
INPUT VALIDATION
      ↓
RESOURCE CHECK
      ↓
EXECUTION
      ↓
OUTPUT VALIDATION
      ↓
AUDIT
      ↓
AGENT OBSERVATION
```

### Critical rule

The tool runtime, not the agent, owns actual invocation authority.

Tool failures become explicit execution failures and cannot silently become successful agent steps.

---

# 24. CMP-019 — Code Sandbox

Conditional MVP component for W5.

### Security boundary

```text
GENERATED CODE
      ↓
STATIC / POLICY VALIDATION
      ↓
RESOURCE ALLOCATION
      ↓
SANDBOX
      ↓
EXECUTION
      ↓
TESTING
      ↓
RESULT VALIDATION
      ↓
VERIFIED RESULT / REJECTION
```

Restrict independently:

- CPU;
- memory;
- disk;
- filesystem;
- process control;
- network;
- credentials;
- environment variables;
- system calls;
- devices;
- execution duration.

Phase 11 baseline prefers Firecracker for the high-assurance boundary, with gVisor retained as a strong candidate. This does **not** mean the sandbox itself establishes sovereignty; host/network controls remain independent.

---

# 25. CMP-020 — Verification Engine

Verification is a first-class execution subsystem.

### Verification types

```text
DETERMINISTIC
    schema
    file integrity
    required fields
    structural validity

EVIDENCE
    source existence
    authority
    revision
    authorization
    temporal validity
    sufficiency

SEMANTIC
    consistency
    contradiction
    completeness
    relationship correctness

NUMERICAL
    calculations
    invariants
    tolerances
    independent calculation

POLICY
    authorization
    security
    workflow rules

HUMAN
    engineering
    safety
    formal approval
```

### Output

```text
ACCEPT
REJECT
CORRECT
ESCALATE
ABSTAIN
```

Verification must be selected based on task risk and output type.

Model confidence, citation presence, artifact existence, and successful code execution cannot by themselves establish correctness.

---

# 26. CMP-021 — Artifact Generator

Supports:

- technical reports;
- approval-note drafts;
- structured documents;
- spreadsheets;
- code artifacts;
- analysis outputs.

### Artifact lifecycle

```text
DRAFT
 ↓
GENERATED
 ↓
CHECKED
 ↓
VERIFIED
 ↓
HUMAN APPROVAL WHERE REQUIRED
 ↓
RELEASED
```

Artifact metadata:

```text
artifact_id
artifact_type
version
task_id
evidence_refs
claim_refs
generation_metadata
verification_state
approval_state
provenance
```

Artifact generation does not equal approval.

---

# 27. CMP-022 — Provenance Manager

The canonical provenance graph is:

```text
SOURCE
 ↓
PROCESSING
 ↓
EVIDENCE
 ↓
DERIVED INFORMATION
 ↓
CLAIM
 ↓
ANALYSIS
 ↓
ARTIFACT
```

Each material transformation creates a provenance edge.

### Provenance ownership

| Edge | Created by |
|---|---|
| Source → Processing | Ingestion |
| Processing → Evidence | Document/evidence pipeline |
| Evidence → Derived Information | Reasoning/analysis |
| Derived Information → Claim | Analysis |
| Claim → Analysis | Workflow/agent |
| Analysis → Artifact | Artifact generator |
| Verification → Output | Verification engine |

The provenance manager owns the graph and its integrity; it does not invent provenance retrospectively.

The SRS requires important transformations, evidence, derived information, claims, models, tools, verification states, and artifacts to remain traceable.

---

# 28. CMP-023 — Audit & Observability

Audit and observability are related but distinct.

## Audit

Records:

- user actions;
- task creation;
- authorization;
- policy decisions;
- model selection;
- model invocation;
- evidence retrieval;
- tool calls;
- code execution;
- verification;
- artifact generation;
- approval;
- failure;
- escalation;
- abstention;
- network/security events;
- configuration changes.

## Observability

Provides:

- logs;
- metrics;
- traces;
- task timeline;
- latency;
- GPU utilization;
- memory;
- queue state;
- resource utilization;
- tool performance;
- model utilization;
- retry behavior.

### Correlation chain

```text
principal_id
     ↓
task_id
     ↓
workflow_id
     ↓
agent_execution_id
     ↓
invocation_id
     ↓
tool_execution_id
     ↓
verification_id
     ↓
artifact_id
```

Sensitive content should not be logged merely because it exists.

The SRS explicitly requires useful operational observability without requiring hidden chain-of-thought exposure.

---

# 29. CMP-024 — Resource & Platform Manager

Owns:

- GPU;
- VRAM;
- CPU;
- RAM;
- storage;
- model loading;
- model unloading;
- concurrency;
- queues;
- cache;
- temporary workspace;
- sandbox resources;
- deployment state;
- update lifecycle.

### Resource flow

```text
TASK
 ↓
RESOURCE REQUEST
 ↓
ADMISSION CONTROL
 ↓
QUEUE / RESERVATION
 ↓
EXECUTION
 ↓
RELEASE
```

### Resource states

```text
AVAILABLE
RESERVED
IN_USE
DEGRADED
EXHAUSTED
RECOVERING
```

Resource exhaustion must become a resource failure, not be misclassified as model failure.

---

# 30. Component Interaction Model

## 30.1 Primary control flow

```text
UI
 ↓
API
 ↓
Identity
 ↓
Task Manager
 ↓
Policy
 ↓
Workflow
 ↓
Agent Runtime
 ↓
Model Router
 ↓
Inference Gateway
 ↓
Evidence / Knowledge
 ↓
Agent
 ↓
Tool Runtime
 ↓
Verification
 ↓
Artifact
 ↓
Provenance
 ↓
Audit
```

The agent never directly controls the entire chain.

---

# 31. Interface Registry

| Interface | Source | Destination | Operation | Data | Auth | Sync/Async |
|---|---|---|---|---|---|---|
| INT-001 | UI | API | Submit Task | TaskRequest | User | Sync |
| INT-002 | API | Identity | Authenticate | PrincipalContext | User | Sync |
| INT-003 | API | Task Manager | Create Task | TaskRequest | Principal | Sync |
| INT-004 | Task Manager | Policy | Evaluate Task | PolicyRequest | System | Sync |
| INT-005 | Workflow | Agent | Start Execution | ExecutionContext | System | Async |
| INT-006 | Agent | Router | Select Capability | RoutingRequest | System | Sync |
| INT-007 | Router | Registry | Query Capability | CapabilityQuery | System | Sync |
| INT-008 | Router | Inference | Invoke | InferenceRequest | System | Sync/Stream |
| INT-009 | Agent | Retrieval | Search Evidence | EvidenceQuery | Task auth | Sync |
| INT-010 | Retrieval | Evidence | Register/resolve | EvidenceRefs | System | Sync |
| INT-011 | Agent | Tool Runtime | Execute Tool | ToolRequest | Agent/task | Sync/Async |
| INT-012 | Tool Runtime | Policy | Authorize Tool | AuthorizationRequest | System | Sync |
| INT-013 | Tool Runtime | Sandbox | Execute Code | SandboxRequest | System | Async |
| INT-014 | Workflow | Verification | Verify | VerificationRequest | System | Sync |
| INT-015 | Verification | Artifact | Release status | VerificationResult | System | Sync |
| INT-016 | Artifact | Provenance | Register Artifact | ArtifactProvenance | System | Sync |
| INT-017 | All critical components | Audit | Record Event | AuditEvent | System | Async |
| INT-018 | All runtime components | Observability | Telemetry | Trace/Metric/Log | System | Async |
| INT-019 | Resource Manager | Inference | Resource allocation | ResourceLease | System | Sync |
| INT-020 | Resource Manager | Sandbox | Resource allocation | ResourceLease | System | Sync |

---

# 32. API Contract Rules

Every internal operation follows:

```text
REQUEST
 ↓
SCHEMA VALIDATION
 ↓
AUTHENTICATION CONTEXT
 ↓
AUTHORIZATION
 ↓
POLICY
 ↓
PROCESSING
 ↓
STATE UPDATE
 ↓
AUDIT
 ↓
RESPONSE
```

Every operation that can create side effects must support an idempotency strategy where applicable.

### Failure contract

```text
SUCCESS
VALIDATION_FAILURE
AUTHORIZATION_FAILURE
POLICY_DENIAL
RESOURCE_FAILURE
TIMEOUT
DEPENDENCY_FAILURE
SECURITY_FAILURE
SEMANTIC_FAILURE
UNVERIFIABLE
```

`500 ERROR` is not a sufficient architectural failure model.

---

# 33. State Ownership Matrix

| State | Authoritative owner |
|---|---|
| User identity | CMP-001 |
| Authorization | CMP-001 |
| Policy configuration | CMP-002 |
| Task | CMP-003 |
| Workflow | CMP-004 |
| Execution state | CMP-005 |
| Model/capability metadata | CMP-006 |
| Routing decision | CMP-007 |
| Inference runtime state | CMP-008 |
| Agent state | CMP-009 |
| Ingestion state | CMP-010 |
| Document processing state | CMP-011 |
| OCR processing | CMP-012 |
| Multimodal representation | CMP-013 |
| P&ID representation | CMP-014 |
| Search/index state | CMP-015 |
| Evidence | CMP-016 |
| Tool definitions | CMP-017 |
| Tool execution | CMP-018 |
| Sandbox execution | CMP-019 |
| Verification result | CMP-020 |
| Artifact | CMP-021 |
| Provenance | CMP-022 |
| Audit record | CMP-023 |
| Resource/platform state | CMP-024 |

No second component may silently become an authoritative owner of another component's state.

---

# 34. Dependency Direction

The allowed dependency hierarchy is:

```text
UI
 ↓
API
 ↓
CONTROL PLANE
 ├── Identity
 ├── Policy
 ├── Task
 ├── Workflow
 └── Execution State
       ↓
AGENT
       ↓
ROUTING
       ↓
CAPABILITY / KNOWLEDGE / TOOLS
       ↓
VERIFICATION
       ↓
ARTIFACT
       ↓
PROVENANCE
       ↓
AUDIT
```

Cross-cutting infrastructure:

```text
RESOURCE MANAGEMENT
STORAGE
OBSERVABILITY
NETWORK SECURITY
```

supports components but does not become their decision authority.

---

# 35. Prohibited Dependency Directions

The following are architectural violations:

```text
Model → Policy
Model → Authorization
Agent → Permission Store
Agent → Network Control
Agent → Security Configuration
Document → Policy
Document → Tool Authorization
Tool → Arbitrary Host
Sandbox → Unrestricted Host
Artifact Generator → Approval Authority
LLM → Task Completion State
```

These violations are more important than whether the implementation is technically "modular."

---

# 36. Trust-Zone Model

```text
ZONE A — USER
    UI
      ↓
ZONE B — TRUSTED CONTROL PLANE
    API
    Identity
    Policy
    Task
    Workflow
    State
      ↓
ZONE C — RESTRICTED AI EXECUTION
    Agent
    Model Router
    Inference
      ↓
ZONE D — RESTRICTED KNOWLEDGE
    Documents
    OCR
    Retrieval
    Evidence
      ↓
ZONE E — CONTROLLED TOOLS
    Tool Runtime
      ↓
ZONE F — HIGH-RISK SANDBOX
    Generated Code
      ↓
ZONE G — ASSURANCE
    Verification
    Provenance
    Audit
```

Independent infrastructure controls surround all zones:

```text
HOST SECURITY
NETWORK ENFORCEMENT
STORAGE CONTROLS
SUPPLY-CHAIN CONTROLS
```

---

# 37. Prompt-Injection Boundary

The permitted path is:

```text
UNTRUSTED DOCUMENT
       ↓
DOCUMENT PROCESSING
       ↓
EXTRACTED CONTENT
       ↓
EVIDENCE
       ↓
REASONING CONTEXT
```

The prohibited path is:

```text
DOCUMENT
   ↓
SYSTEM INSTRUCTION
   ↓
POLICY
   ↓
AUTHORIZATION
   ↓
TOOL PERMISSION
```

The same principle applies to:

- OCR output;
- retrieved documents;
- spreadsheet cells;
- code comments;
- engineering notes;
- tool output.

The SRS explicitly identifies these inputs as potentially untrusted and requires that they never acquire control-plane authority.

---

# 38. Security Responsibility Matrix

| Responsibility | Owner | Enforcement point | Detection | Audit |
|---|---|---|---|---|
| Authentication | CMP-001 | Identity boundary | Auth events | Yes |
| Authorization | CMP-001 | Authorization gate | Denials/bypass tests | Yes |
| Policy | CMP-002 | Policy gate | Policy decisions | Yes |
| Task permissions | CMP-001/003 | Task gate | Unauthorized request | Yes |
| Data access | CMP-001/015/016 | Retrieval/data boundary | Access tests | Yes |
| Model access | CMP-002/006/007 | Capability gate | Unauthorized invocation | Yes |
| Tool access | CMP-002/018 | Tool gate | Invocation tests | Yes |
| Code access | CMP-002/019 | Sandbox boundary | Escape tests | Yes |
| Filesystem | CMP-019/platform | Sandbox/host | Isolation tests | Yes |
| Network | Platform/network controls | Host/network boundary | Packet observation | Yes |
| Credentials | Platform/security | Secret boundary | Exposure tests | Yes |
| Artifact release | CMP-020/021 | Verification/release gate | Release tests | Yes |
| Provenance | CMP-022 | Provenance store | Integrity checks | Yes |
| Audit | CMP-023 | Audit pipeline | Audit health checks | Yes |
| Configuration | CMP-024/CMP-002 | Configuration boundary | Change monitoring | Yes |

---

# 39. Agent Authority Matrix

| Action | Agent can request? | Direct execution? | Policy required? | Human approval? |
|---|---:|---:|---:|---:|
| Search knowledge | Yes | No | Yes | No |
| Read authorized document | Yes | No | Yes | No |
| Generate report draft | Yes | No | Yes | Usually no |
| Execute approved code | Yes | No | Yes | Conditional |
| Modify local working artifact | Yes | No | Yes | Conditional |
| Access credentials | No direct access | No | Mandatory | N/A |
| Change permissions | No | No | Mandatory | Admin only |
| Change security policy | No | No | Mandatory | Admin only |
| Approve engineering decision | No | No | Mandatory | **Yes** |
| Approve formal artifact | No | No | Mandatory | **Yes** |
| Modify OT system | No | **No** | Mandatory | Authorized organizational control only |
| Establish own authority | **No** | **No** | Mandatory | No |

This implements the SRS requirement that the agent remain subordinate to externally defined authority.

---

# 40. Data Flow Classification

| Flow | Classification | Trust | Main control |
|---|---|---|---|
| User → API | Sensitive | User-controlled | Authentication |
| Document → Processor | Confidential/untrusted | Untrusted | Input isolation |
| OCR → Evidence | Derived/unverified | Untrusted-derived | Provenance |
| Retrieval → Agent | Confidential/evidence | Controlled | Authorization |
| Model → Agent | Derived/untrusted | Untrusted | Schema/policy |
| Agent → Tool | Control request | Untrusted requester | Policy |
| Tool → Agent | Derived/untrusted | Restricted | Output validation |
| Agent → Sandbox | Untrusted code | High-risk | Sandbox |
| Sandbox → Host | Prohibited except controlled interface | Untrusted | Isolation |
| Evidence → Artifact | Derived | Controlled | Provenance |
| Verification → Release | Control | Trusted | Verification gate |
| System → Network | Confidential | Controlled | Host enforcement |
| Audit → Storage | Sensitive | Trusted | Integrity/access control |

---

# 41. Storage Architecture

Storage is split by responsibility rather than forcing everything into one database.

| Storage class | Owner | Primary use |
|---|---|---|
| Object/document storage | CMP-010/011 | Source documents |
| Evidence metadata store | CMP-016 | Evidence state/metadata |
| Search/index store | CMP-015 | Retrieval |
| Vector index | CMP-015 | Semantic retrieval |
| Task/state store | CMP-003/005 | Execution state |
| Artifact store | CMP-021 | Generated outputs |
| Provenance store | CMP-022 | Lineage graph |
| Audit store | CMP-023 | Immutable/controlled audit |
| Telemetry store | CMP-023/024 | Metrics/traces/logs |
| Configuration store | CMP-002/024 | Versioned configuration |
| Model registry | CMP-006 | Model metadata |
| Temporary execution storage | CMP-018/019 | Ephemeral work |

Phase 11's SQLite baseline is therefore appropriate for local control/metadata state where its concurrency characteristics are acceptable; Qdrant remains the retrieval-index candidate; application-owned provenance and audit remain authoritative rather than delegated conceptually to a database product.

---

# 42. End-to-End Workflow A — Organizational Knowledge Investigation

```text
USER
 ↓
UI
 ↓
API
 ↓
IDENTITY
 ↓
TASK MANAGER
 ↓
POLICY
 ↓
WORKFLOW
 ↓
AGENT
 ↓
MODEL ROUTER
 ↓
RETRIEVAL
 ↓
AUTHORIZATION FILTER
 ↓
EVIDENCE MANAGER
 ↓
EVIDENCE SUFFICIENCY
 ↓
AGENT REASONING
 ↓
VERIFICATION
 ↓
RESULT
 ↓
PROVENANCE
 ↓
AUDIT
```

### Failure examples

```text
No authorization
    → DENIED

No sufficient evidence
    → RETRIEVE / ASK / ESCALATE / ABSTAIN

Conflicting evidence
    → CONFLICTED

Stale source
    → STALE

Verification failure
    → CORRECT / ESCALATE / ABSTAIN
```

---

# 43. End-to-End Workflow B — Inspection Report Analysis

```text
USER
 ↓
TASK
 ↓
DOCUMENT INGESTION
 ↓
DOCUMENT INTELLIGENCE
 ↓
OCR / MULTIMODAL
 ↓
STRUCTURED REPRESENTATION
 ↓
EVIDENCE REGISTRATION
 ↓
RETRIEVAL
 ↓
AGENT ANALYSIS
 ↓
VERIFICATION
 ↓
FINDINGS
 ↓
PROVENANCE
 ↓
ARTIFACT
```

The workflow does not treat OCR output as automatically authoritative.

---

# 44. End-to-End Workflow C — P&ID Analysis

```text
P&ID
 ↓
INGEST
 ↓
PAGE / REGION EXTRACTION
 ↓
OCR
 ↓
VISION
 ↓
ENTITY DETECTION
 ↓
TAG DETECTION
 ↓
LINE DETECTION
 ↓
RELATIONSHIP DETECTION
 ↓
CONNECTIVITY
 ↓
STRUCTURED REPRESENTATION
 ↓
TOPOLOGY VERIFICATION
 ↓
ENGINEERING INTERPRETATION
 ↓
HUMAN REVIEW WHERE CONSEQUENTIAL
```

This is a deliberate multi-component architecture.

It prevents:

```text
P&ID image
   ↓
VLM
   ↓
"engineering truth"
```

from becoming the system's architecture.

---

# 45. End-to-End Workflow D — Artifact Generation

```text
TASK
 ↓
EVIDENCE
 ↓
CLAIMS
 ↓
ANALYSIS
 ↓
ARTIFACT GENERATOR
 ↓
STRUCTURAL CHECK
 ↓
CONTENT CHECK
 ↓
EVIDENCE / PROVENANCE CHECK
 ↓
VERIFICATION
 ↓
HUMAN APPROVAL IF REQUIRED
 ↓
RELEASE
```

---

# 46. End-to-End Workflow E — Controlled Code Analysis

```text
TASK
 ↓
AGENT
 ↓
CODE GENERATION
 ↓
STATIC / POLICY CHECK
 ↓
RESOURCE ADMISSION
 ↓
SANDBOX
 ↓
EXECUTION
 ↓
TEST
 ↓
RESULT VALIDATION
 ↓
VERIFICATION
 ↓
RESULT / REJECTION
```

Successful execution is only evidence that the program ran.

It is not evidence that the program was correct.

---

# 47. Failure Ownership Matrix

| Failure | Detection | Recovery owner | Retry? | Escalate? | User visible? | Audit |
|---|---|---|---|---|---|---|
| Model unavailable | Inference Gateway | Router | Yes if alternate | Maybe | Yes | Yes |
| GPU OOM | Resource Manager | Resource Manager | Controlled | Maybe | Yes | Yes |
| OCR failure | OCR | Document Processor | Limited | Maybe | Yes | Yes |
| Parsing failure | Document Engine | Ingestion | Limited | Yes | Yes | Yes |
| Corrupt document | Document Engine | Ingestion | No | Maybe | Yes | Yes |
| Retrieval unavailable | Retrieval | Knowledge layer | Controlled | Yes | Yes | Yes |
| Insufficient evidence | Evidence | Agent/Workflow | Additional retrieval | Yes | Yes | Yes |
| Conflicting evidence | Evidence | Agent/Reviewer | No blind retry | Yes | Yes | Yes |
| Stale evidence | Evidence | Retrieval/Workflow | New revision search | Yes | Yes | Yes |
| Unauthorized evidence | Authorization | Policy | No | Maybe | Yes | Yes |
| Tool failure | Tool Runtime | Agent/Workflow | Classified | Maybe | Yes | Yes |
| Sandbox failure | Sandbox | Resource/Execution | Controlled | Yes | Yes | Yes |
| Code failure | Sandbox | Agent | Correction only | Maybe | Yes | Yes |
| Verification failure | Verification | Workflow | Correction | Yes | Yes | Yes |
| Agent loop failure | Agent/Workflow | Workflow | Bounded | Yes | Yes | Yes |
| Timeout | Workflow | Workflow | Policy dependent | Maybe | Yes | Yes |
| Cancellation | Task Manager | Workflow | No | No | Yes | Yes |
| Storage failure | Platform | Platform | Controlled | Yes | Yes | Yes |
| Audit failure | Audit | Platform | **Fail according to assurance policy** | Yes | Yes | Yes |
| Provenance failure | Provenance | Workflow | No silent completion | Yes | Yes | Yes |
| Policy denial | Policy | Workflow | No blind retry | Maybe | Yes | Yes |
| Authorization failure | Identity/Auth | Workflow | No | Maybe | Yes | Yes |

---

# 48. Partial Failure Strategy

## Principle

Not every component failure should collapse the entire system.

### Example: OCR unavailable

Possible paths:

```text
OCR unavailable
    ↓
Can native text extraction establish sufficient evidence?
    ├── YES → Continue with reduced capability
    └── NO
          ↓
       Escalate / Ask / Abstain
```

### Example: primary model unavailable

```text
Primary model unavailable
       ↓
Router
       ↓
Compatible alternative?
   ├── YES → Use alternative
   └── NO → Degrade / Escalate / Stop
```

### Example: verification unavailable

```text
Verification unavailable
       ↓
Consequential output?
   ├── YES → BLOCK
   └── NO → Apply policy-specific degraded state
```

Verification failure cannot be converted into success.

---

# 49. Security Compromise Matrix

| Component | Compromise impact | Data access | Tools | Network | Privilege | Containment |
|---|---|---|---|---|---|---|
| Identity | Critical | Broad metadata | Indirect | No | High | Control-plane isolation |
| Policy | Critical | Policy/config | Indirect | No | High | Protected configuration |
| Task | High | Task metadata | No direct | No | Limited | Control plane |
| Workflow | Critical | Execution metadata | Requests | No direct | High | State authority boundary |
| Agent | High | Task/evidence context | Requests | No direct | Restricted | Capability boundary |
| Inference | High | Prompt/context | No direct | Blocked | Low | Runtime/network isolation |
| Document processor | High | Documents | No | Blocked | Low | Data-processing boundary |
| Retrieval | High | Indexed knowledge | No | Blocked | Low | Authorization filter |
| Tool Runtime | Critical | Tool-scoped data | Controlled | Policy-bound | Tool-specific | Execution boundary |
| Sandbox | High | Assigned files | Sandbox only | Blocked | Restricted | MicroVM/gVisor boundary |
| Verification | High | Outputs/evidence | No | No | Low | Assurance boundary |
| Artifact | High | Derived content | No | Blocked | Low | Output boundary |
| Provenance | Critical | Lineage | No | No | High integrity | Protected store |
| Audit | Critical | Audit metadata | No | Controlled | Integrity-critical | Protected storage |
| Resource Manager | Critical | Runtime metadata | Indirect | Infrastructure | High | Platform boundary |

---

# 50. Performance Contracts

No unsupported numerical thresholds are introduced.

Each component must expose measurable:

- latency;
- throughput;
- concurrency;
- CPU consumption;
- RAM;
- GPU;
- VRAM;
- storage;
- startup time;
- queue time;
- resource limits.

The principal system-level measure remains:

> **Time and resources required to produce an acceptable verified outcome.**

This follows the SRS requirement to evaluate performance at workflow level rather than reducing the system to tokens/second.

---

# 51. Resource Scheduling Model

The MVP resource scheduler should use:

```text
TASK
 ↓
RISK / PRIORITY
 ↓
CAPABILITY REQUIREMENT
 ↓
RESOURCE ESTIMATE
 ↓
ADMISSION CONTROL
 ↓
RESERVATION
 ↓
EXECUTION
 ↓
OBSERVATION
 ↓
RELEASE
```

A task should be rejected/deferred before execution if its estimated resource envelope cannot be admitted safely.

This is preferable to allowing the model to start execution and discovering GPU exhaustion halfway through the workflow.

---

# 52. Model Loading Strategy

The component architecture supports:

```text
MODEL REGISTERED
       ↓
COMPATIBILITY CHECK
       ↓
RESOURCE CHECK
       ↓
LOAD
       ↓
SERVE
       ↓
UNLOAD / KEEP-WARM
```

The exact policy for simultaneous resident models remains a hardware-validation item.

The architecture therefore supports both:

```text
multiple resident models
```

and:

```text
controlled model swapping
```

without changing the rest of the system.

---

# 53. Configuration Architecture

Configuration is divided into:

```text
SYSTEM CONFIGURATION
    ↓
MODEL CONFIGURATION
    ↓
ROUTING CONFIGURATION
    ↓
TOOL CONFIGURATION
    ↓
SECURITY CONFIGURATION
    ↓
RETRIEVAL CONFIGURATION
    ↓
RESOURCE CONFIGURATION
    ↓
WORKFLOW CONFIGURATION
```

Separate from:

```text
RUNTIME STATE
```

and:

```text
USER DATA
```

Security-critical configuration is immutable from the agent's perspective.

Every configuration change receives:

```text
config_version
actor
timestamp
change
reason
previous_version
new_version
```

and an audit record.

---

# 54. Deployment Architecture

## MVP deployment

```text
┌─────────────────────────────────────────────────────┐
│ SINGLE CONTROLLED WORKSTATION / SERVER             │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │ Application Process                           │  │
│  │                                               │  │
│  │ API / Control / Agent / Knowledge / Verify   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌────────────────────┐  ┌───────────────────────┐ │
│  │ Model Serving      │  │ Search / Metadata     │ │
│  │ vLLM                │  │ Local stores          │ │
│  └────────────────────┘  └───────────────────────┘ │
│                                                     │
│  ┌────────────────────┐                             │
│  │ Sandbox            │                             │
│  │ Firecracker/gVisor │                             │
│  └────────────────────┘                             │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │ Host Network / Security Enforcement           │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

The architecture intentionally avoids requiring a distributed cluster for MVP.

---

# 55. Deployable vs Non-Deployable Boundaries

## Deployable/runtime boundaries

- CMP-008 — AI Inference Gateway/model serving;
- CMP-011 — Document processing runtime where resource isolation is useful;
- CMP-018 — Tool execution runtime;
- CMP-019 — Code sandbox;
- CMP-024 — Platform/resource management.

## Application modules

- Identity;
- Policy;
- Task;
- Workflow;
- Execution state;
- Capability registry;
- Router;
- Agent;
- OCR;
- Multimodal;
- P&ID;
- Retrieval orchestration;
- Evidence;
- Verification;
- Artifact;
- Provenance.

This arrangement provides independent **security and resource boundaries** where they matter without manufacturing unnecessary network boundaries.

---

# 56. Phase 11 Technology Mapping

The component architecture consumes, rather than reopens, the Phase 11 baseline.

| Component | Phase 11 technology baseline |
|---|---|
| Application API | FastAPI |
| Frontend | React + TypeScript |
| Model serving | vLLM preferred |
| Compatibility inference | llama.cpp |
| Main local models | Qwen3.5 family candidates |
| Embedding | Qwen3-Embedding |
| Reranking | Qwen3-Reranker |
| Document processing | Docling |
| OCR | PaddleOCR / PP-Structure |
| Agent runtime | LangGraph |
| Retrieval | Qdrant candidate |
| Control metadata | SQLite candidate |
| Sandbox | Firecracker preferred |
| Secondary isolation | gVisor candidate |
| Observability | OpenTelemetry |
| Network sovereignty | Host-enforced controls |
| Provenance | Application-owned |
| Audit | Application-owned |

No Phase 11 technology is silently replaced by Phase 12.

Where Phase 11 marked validation as required, Phase 12 preserves that status.

---

# 57. Interface Independence From Technology

The architecture must expose stable contracts such as:

```text
ModelCapability
InferenceRequest
InferenceResult

EvidenceQuery
EvidenceObject
EvidenceAssessment

ToolDefinition
ToolRequest
ToolResult

VerificationRequest
VerificationResult

ArtifactRequest
ArtifactResult

PolicyRequest
PolicyDecision

ResourceRequest
ResourceLease

AuditEvent
ProvenanceEdge
```

This allows:

```text
Qwen → another model
vLLM → another serving runtime
Qdrant → another search implementation
Firecracker → another isolation implementation
LangGraph → another workflow/agent runtime
```

without redesigning the control plane.

Replacement requires contract compatibility, not application-wide rewrites.

---

# 58. Testing Architecture

Every component must have four test levels.

## Level 1 — Unit

Tests internal logic.

## Level 2 — Contract

Tests interface schemas and state transitions.

## Level 3 — Security

Tests:

- authorization bypass;
- privilege escalation;
- prompt injection;
- unauthorized retrieval;
- tool abuse;
- sandbox escape;
- network bypass;
- credential exposure.

## Level 4 — Workflow

Tests:

```text
USER TASK
 → EVIDENCE
 → REASON
 → EXECUTE
 → VERIFY
 → ARTIFACT
```

The system should not declare the architecture validated merely because every individual component passes unit tests.

---

# 59. Architecture Acceptance Tests

## A. Authority

- [ ] Agent cannot change permissions.
- [ ] Agent cannot modify security policy.
- [ ] Agent cannot authorize itself.
- [ ] Model output cannot directly change control-plane state.
- [ ] Consequential actions require human authority.

## B. Evidence

- [ ] Evidence retains source identity.
- [ ] Revision is preserved.
- [ ] Authorization is preserved.
- [ ] Conflicts are represented.
- [ ] Stale evidence is detectable.
- [ ] Insufficient evidence blocks unsupported completion.

## C. Execution

- [ ] Every tool has an explicit contract.
- [ ] Tool execution is policy-gated.
- [ ] Code execution is sandboxed.
- [ ] Retry behavior is bounded.
- [ ] Completion is system-defined.

## D. Verification

- [ ] Verification is independent of generation.
- [ ] Verification failure changes completion state.
- [ ] Human approval remains separate.
- [ ] Successful execution does not equal correctness.

## E. Sovereignty

- [ ] Core inference operates locally.
- [ ] No external AI API is required.
- [ ] Network egress is host-enforced.
- [ ] Network behavior is observable.
- [ ] Sandbox cannot bypass network policy.
- [ ] Offline installation/update path exists.

## F. Operations

- [ ] Resource exhaustion is observable.
- [ ] GPU utilization is observable.
- [ ] Task state survives recoverable failures.
- [ ] Audit records material actions.
- [ ] Provenance can reconstruct important outputs.

---

# 60. Critical Architectural Invariants

These become implementation-level invariants.

### INV-001 — External authority

```text
AI output never creates authority.
```

### INV-002 — Evidence integrity

```text
No material claim without traceable evidence
unless explicitly classified as inference/uncertainty.
```

### INV-003 — Authorization independence

```text
Model compliance is never the authorization mechanism.
```

### INV-004 — Completion independence

```text
LLM "done" ≠ system completion.
```

### INV-005 — Verification independence

```text
Generation ≠ verification.
```

### INV-006 — Sandbox independence

```text
Code execution ≠ host execution.
```

### INV-007 — Sovereignty independence

```text
Application intent ≠ network enforcement.
```

### INV-008 — Audit integrity

```text
Critical execution cannot silently disappear from audit.
```

### INV-009 — Provenance continuity

```text
Material transformation must preserve lineage.
```

### INV-010 — Failure honesty

```text
Failure ≠ success-looking output.
```

### INV-011 — No untrusted control-plane escalation

```text
Document/model/OCR/tool/code output
cannot become policy or authority.
```

### INV-012 — Human consequential authority

```text
AI can prepare and analyze;
authorized humans retain consequential decision authority.
```

---

# 61. Architectural Failure Modes

The following designs are explicitly rejected.

## Rejected 1 — Agent as central authority

```text
User
 ↓
Agent
 ↓
Everything
```

**Reason:** collapses authorization, policy, execution, and reasoning boundaries.

## Rejected 2 — LLM-owned workflow state

```text
LLM says completed
        ↓
COMPLETED
```

**Reason:** violates deterministic completion.

## Rejected 3 — Vector database as knowledge authority

```text
Vector DB
   ↓
Truth
```

**Reason:** retrieval relevance does not establish authority, revision, authorization, or correctness.

## Rejected 4 — VLM as P&ID truth

```text
Image
 ↓
VLM
 ↓
Engineering truth
```

**Reason:** visual recognition, topology, interpretation, and engineering authority are distinct.

## Rejected 5 — Docker-only code boundary

**Reason:** insufficient architectural assurance for the intended high-risk code execution boundary.

## Rejected 6 — Application-only sovereignty

```text
Application says:
"No network."
```

**Reason:** sovereignty requires independent enforcement and observation.

## Rejected 7 — Everything as microservice

**Reason:** increases operational complexity and distributed failure modes on a single-node MVP without improving the critical security boundaries.

---

# 62. Implementation Package Produced by Phase 12

Phase 12 establishes the following implementation contracts:

```text
01. Component registry
02. Component ownership model
03. Trust-zone model
04. Control/data-plane model
05. Interface registry
06. API contract model
07. State ownership model
08. State transition model
09. Dependency direction
10. Security responsibility matrix
11. Agent authority matrix
12. Data classification matrix
13. Storage ownership model
14. Workflow interaction model
15. Failure ownership model
16. Partial-failure model
17. Resource management model
18. Deployment boundaries
19. Testing boundaries
20. Architectural invariants
```

The next engineering work is therefore no longer "what components should exist?"

It is:

```text
COMPONENT
    ↓
INTERNAL DESIGN
    ↓
SCHEMA
    ↓
API CONTRACT
    ↓
STATE MACHINE
    ↓
IMPLEMENTATION
    ↓
COMPONENT TEST
    ↓
INTEGRATION TEST
    ↓
WORKFLOW TEST
```

---

# 63. Remaining Validation Items

Phase 12 does **not** pretend that architecture-level decisions prove runtime feasibility.

The following remain empirical:

| ID | Validation |
|---|---|
| V12-01 | Target hardware supports intended model portfolio |
| V12-02 | Concurrent model/resource behavior |
| V12-03 | vLLM + selected model configurations |
| V12-04 | Multimodal/P&ID workload quality |
| V12-05 | Retrieval quality on representative enterprise corpus |
| V12-06 | Agent workflow reliability |
| V12-07 | Sandbox isolation and performance |
| V12-08 | Artifact generation quality |
| V12-09 | End-to-end workflow latency |
| V12-10 | Zero-egress enforcement |
| V12-11 | Audit completeness |
| V12-12 | Provenance reconstruction |
| V12-13 | Recovery after process/resource failure |
| V12-14 | Customer-specific authorization model |
| V12-15 | Offline update/install lifecycle |

These are **validation tasks**, not reasons to reopen the architecture without evidence.

---

# 64. Phase 12 Gate Assessment

## Gate

**COMPONENT ARCHITECTURE BASELINE ESTABLISHED — IMPLEMENTATION-READY WITH TARGETED VALIDATION**

### Established

- component responsibilities;
- component ownership;
- control-plane/data-plane separation;
- security boundaries;
- agent authority boundary;
- evidence ownership;
- verification ownership;
- provenance ownership;
- audit ownership;
- resource ownership;
- state ownership;
- dependency direction;
- interface contracts;
- failure ownership;
- deployment boundaries;
- MVP component scope.

### Strong architectural conclusion

The correct MVP is **not** a collection of independent AI services.

It is a **modular single-node execution environment with a trusted control plane, restricted AI/data execution planes, independent high-risk execution boundaries, and first-class evidence/verification/provenance/assurance subsystems**.

That conclusion is consistent with the project's established requirement to favor modular, replaceable components while maintaining strict authority and sovereignty boundaries.

### Not yet established

- exact class/function design;
- exact database schemas;
- exact message/event schemas;
- final hardware envelope;
- production concurrency limits;
- final sandbox choice between preferred and candidate implementation;
- customer-specific identity/authorization integration;
- final deployment packaging;
- production benchmark thresholds.

Those belong to component design and validation rather than being fabricated here.

---

# 65. Phase 13 Handoff

Phase 13 should now begin from the **24-component baseline**, not restart architecture discovery.

Its primary objective should be:

> **Convert each Phase 12 component into an internally implementable design consisting of domain model, data schemas, state machines, API contracts, algorithms, error handling, security controls, test specifications, and implementation boundaries.**

The highest-priority components for Phase 13 are:

```text
1. CMP-001 Identity & Authorization
2. CMP-002 Policy Engine
3. CMP-003 Task Manager
4. CMP-004 Workflow Engine
5. CMP-005 Execution State Manager
6. CMP-009 Agent Runtime
7. CMP-016 Evidence Manager
8. CMP-018 Tool Runtime
9. CMP-020 Verification Engine
10. CMP-022 Provenance Manager
11. CMP-024 Resource & Platform Manager
```

These components form the **system's authority and correctness backbone**.

The model, OCR, retrieval, and multimodal components are important, but they should plug into this backbone rather than becoming the backbone.

# Final Phase 12 Decision

**Proceed to Phase 13 — Component Design.**

The architecture is sufficiently decomposed to begin implementation-level design without reopening the product, SRS, system architecture, or Phase 11 technology baseline. Any Phase 11 reversal should occur only if a Phase 12/implementation validation demonstrates an actual incompatibility, security failure, or unacceptable resource envelope.