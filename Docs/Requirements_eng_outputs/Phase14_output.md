# SOVEREIGN AGENTIC AI WORKBENCH

# PHASE 14 — AGENT RUNTIME & TOOL ARCHITECTURE

**Phase:** 14  
**Predecessor:** Phase 13 — Data & Knowledge Architecture  
**Successor:** Phase 15 — Interface / API / Contract Design  
**Status:** **AGENT RUNTIME ARCHITECTURE BASELINE ESTABLISHED — READY FOR DETAILED RUNTIME IMPLEMENTATION DESIGN**  
**Primary domain:** Agent Execution, Workflow Control, Capability Invocation, Tool Security, Verification, Recovery and Completion

---

# 1. Objective

Phase 14 defines the controlled execution runtime through which an authorized user task becomes a bounded sequence of:

```text
Identity
→ Security Context
→ Policy
→ Task
→ Capability
→ Agent
→ Evidence / Model / Tool
→ Policy Re-check
→ Execution
→ Result
→ Verification
→ Continue / Correct / Escalate / Abstain / Stop
→ Completion
```

The central architectural requirement is:

> **The agent may reason and propose actions, but it never becomes the authority mechanism that permits those actions.**

The runtime therefore separates:

- intelligence from authority;
- planning from execution;
- capability selection from permission;
- tool requests from tool authorization;
- execution success from correctness;
- model confidence from verification;
- agent state from authoritative workflow state;
- generated artifacts from released artifacts;
- agent completion claims from system completion.

This phase converts the Phase 13 governed knowledge model into a controlled execution model without creating a competing data architecture.

---

# 2. Architectural Position

The final runtime is:

```text
                         USER
                           │
                           ▼
                      IDENTITY
                           │
                           ▼
                  SECURITY CONTEXT
                           │
                           ▼
                        POLICY
                           │
                           ▼
                         TASK
                           │
                           ▼
                      CAPABILITY
                           │
                           ▼
                         AGENT
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
              EVIDENCE    MODEL     TOOL
                 │         │         │
                 └─────────┼─────────┘
                           ▼
                    POLICY RE-CHECK
                           │
                     ┌─────┴─────┐
                     │           │
                    DENY        ALLOW
                     │           │
                     │           ▼
                     │       EXECUTION
                     │           │
                     │           ▼
                     │         RESULT
                     │           │
                     │           ▼
                     │      VERIFICATION
                     │           │
                     │      ┌────┼────┐
                     │      ▼    ▼    ▼
                     │    PASS  FAIL UNCERTAIN
                     │      │    │      │
                     │      │    ▼      ▼
                     │      │ CORRECT ESCALATE
                     │      │    │
                     └──────┴────┴───────┐
                                          ▼
                                      COMPLETION
                                          │
                                          ▼
                                        AUDIT
```

The runtime is therefore **not**:

```text
Prompt → LLM → Tool → Answer
```

That architecture is rejected.

---

# 3. Governing Architectural Principles

## AR-01 — Agent Is Not Authority

The agent cannot:

- grant permissions;
- modify authorization;
- modify policy;
- grant tool access;
- bypass sandboxing;
- disable verification;
- suppress audit;
- suppress provenance;
- approve its own consequential result;
- control OT or production state.

---

## AR-02 — Tool Call Is a Request

An agent-generated tool call has the semantic type:

```text
PROPOSED_ACTION
```

not:

```text
AUTHORIZED_ACTION
```

Authorization exists only after independent runtime and policy evaluation.

---

## AR-03 — Policy Is Outside the Agent

Security-critical policy evaluation must be deterministic and external to model reasoning.

```text
Agent Proposal
      ↓
Runtime Validation
      ↓
Policy
      ↓
Authorization
      ↓
Resource Check
      ↓
Execution
```

---

## AR-04 — Evidence Is Governed Before Reasoning

The runtime consumes Phase 13 `Evidence`, `EvidenceBundle`, and associated authorization/provenance semantics.

The agent must not directly access:

- arbitrary databases;
- arbitrary filesystem locations;
- arbitrary indexes;
- unrestricted source repositories.

The agent requests governed evidence.

---

## AR-05 — Generated Code Is Untrusted

Generated code is treated as hostile until:

```text
Generated
→ Validated
→ Policy Checked
→ Sandboxed
→ Resource Limited
→ Executed
→ Tested
→ Verified
```

---

## AR-06 — Execution Success Is Not Correctness

A tool returning:

```text
SUCCESS
```

means only that the execution mechanism completed.

It does not establish:

```text
CORRECT
```

Correctness requires verification where applicable.

---

## AR-07 — LLM Completion Is Not System Completion

The model cannot directly transition a task to `COMPLETED`.

The runtime evaluates completion predicates.

---

## AR-08 — Failure Is Explicit

The runtime must never convert:

```text
timeout
policy denial
verification failure
missing evidence
resource exhaustion
```

into success-looking output.

---

## AR-09 — Abstention Is Valid

A safe system is allowed to conclude:

```text
INSUFFICIENT
UNVERIFIABLE
CONFLICTED
UNAUTHORIZED
BLOCKED
ESCALATED
```

rather than manufacture completion.

---

## AR-10 — Security Overrides Autonomy

No increase in agent autonomy may weaken:

- authorization;
- policy;
- sandboxing;
- verification;
- audit;
- provenance;
- sovereignty;
- human consequential authority.

---

# 4. Runtime Object Model

The runtime uses the following logical objects.

| Object | Primary role | Persistence |
|---|---|---|
| Task | User-requested work | Persistent |
| Execution | Particular attempt of a task | Persistent |
| Workflow | System-controlled execution structure | Persistent/versioned |
| Plan | Proposed execution strategy | Versioned |
| Step | Unit of workflow execution | Persistent |
| Action | Intended executable operation | Event/state |
| Capability | Abstract system capability | Registry |
| Tool Request | Proposed invocation | Persistent/event |
| Tool Execution | Actual invocation | Persistent/event |
| Observation | Runtime input after action | Persistent where required |
| Evidence Request | Governed knowledge request | Event/persistent trace |
| Evidence Result | Governed evidence response | Persistent/reference |
| Verification | Assessment of result | Persistent |
| Approval | Human authorization event | Persistent |
| Escalation | Transfer of control | Persistent |
| Retry | Controlled recovery attempt | Persistent |
| Failure | Classified execution failure | Persistent |
| Completion Predicate | Deterministic completion condition | Workflow definition |
| Execution Trace | Ordered execution history | Persistent |

Not every object requires an independent database table.

The semantic distinction is mandatory; physical representation is an implementation concern.

---

# 5. Task Model

A `Task` represents the user's requested work.

Conceptual structure:

```text
Task
├── task_id
├── requester
├── task_type
├── user_request
├── security_context_id
├── workflow_class
├── required_capabilities
├── task_scope
├── priority
├── constraints
├── requested_artifact
├── status
├── created_at
└── provenance
```

A task is independent from its executions.

```text
Task T-100
 ├── Execution E-001
 ├── Execution E-002
 └── Execution E-003
```

This permits:

- retry as a new execution;
- controlled re-execution;
- failure comparison;
- historical reconstruction.

A retry of a step is not automatically a new user task.

---

# 6. Execution Model

An `Execution` represents one controlled attempt to perform a task.

```text
Execution
├── execution_id
├── task_id
├── execution_number
├── workflow_version
├── plan_version
├── security_context_version
├── model_configuration
├── tool_configuration
├── status
├── started_at
├── completed_at
├── failure_state
└── trace_reference
```

An execution must bind the versions relevant to reproducibility.

A running execution must not silently change:

- security context;
- policy version;
- workflow version;
- tool version;
- model version;

unless an explicit runtime policy permits the transition and records it.

---

# 7. Workflow vs Plan

## Workflow

A workflow is system-controlled execution structure.

It controls:

- mandatory gates;
- ordering;
- approval;
- verification;
- retry constraints;
- cancellation;
- completion;
- failure transitions.

## Plan

A plan is a strategy for achieving the task.

It may be:

- agent-generated;
- system-generated;
- human-specified.

The plan is subordinate to:

```text
Policy
+
Workflow Constraints
+
Security Context
+
Resource Constraints
```

Therefore:

```text
Agent Plan
   ↓
Plan Validation
   ↓
Policy
   ↓
Workflow Constraints
   ↓
Executable Steps
```

---

# 8. Plan Object

```text
Plan
├── plan_id
├── task_id
├── execution_id
├── version
├── goal
├── steps[]
├── dependencies[]
├── required_capabilities[]
├── required_evidence[]
├── constraints[]
├── risk_class
├── completion_conditions[]
├── creator
├── created_at
└── provenance
```

A plan is invalid if it:

- requires unauthorized evidence;
- requires prohibited tools;
- exceeds resource policy;
- omits mandatory verification;
- bypasses approval;
- contains prohibited actions;
- lacks completion conditions.

---

# 9. Plan Validation

Before execution:

```text
Plan
 ↓
Schema Validation
 ↓
Capability Validation
 ↓
Evidence Accessibility Check
 ↓
Authorization Check
 ↓
Policy Check
 ↓
Resource Check
 ↓
Risk Check
 ↓
Verification Requirement Check
 ↓
Completion Predicate Check
 ↓
Executable Plan
```

The runtime may reject the entire plan or transform it into a constrained executable plan.

The agent cannot override validation failures.

---

# 10. Dynamic Replanning

Replanning is permitted only inside the execution authority established by the runtime.

Triggers include:

- insufficient evidence;
- conflicting evidence;
- tool failure;
- model failure;
- verification failure;
- resource exhaustion;
- policy change;
- security-context change;
- new user information;
- unexpected result.

Replanning must preserve:

- task identity;
- security context;
- authorization;
- audit history;
- provenance;
- already-established constraints.

Every material plan change receives a new plan version.

Infinite replanning is prohibited.

---

# 11. Agent Authority Model

## Agent may

- interpret the task;
- propose a plan;
- select permitted capabilities;
- request evidence;
- request model invocation;
- request tools;
- inspect observations;
- propose correction;
- propose retry;
- request clarification;
- request human intervention;
- abstain;
- stop voluntarily.

## Agent may not

- authorize itself;
- escalate its own permissions;
- alter policy;
- alter security context;
- access arbitrary storage;
- invoke unregistered tools;
- bypass verification;
- bypass sandboxing;
- suppress audit;
- suppress provenance;
- approve consequential outputs;
- control OT;
- declare system completion independently.

---

# 12. Final Authority Matrix

| Operation | Agent | Runtime | Policy | Human |
|---|---:|---:|---:|---:|
| Interpret task | Propose | Validate | Constrain | May clarify |
| Create plan | Yes | Validate | Constrain | May override through authorized workflow |
| Retrieve evidence | Request | Execute | Authorize | Not normally required |
| Select model | Propose | Decide/route | Constrain | Not normally required |
| Select tool | Propose | Validate | Authorize | Required if policy says so |
| Execute tool | No direct authority | Yes | Permit | If consequential |
| Execute generated code | Request | Controlled | Permit | If required |
| Modify task state | No | Yes | Constrain | Via authorized action |
| Change policy | No | No | Authorized policy authority | Authorized administrator |
| Approve consequential conclusion | No | No | Cannot substitute for human authority | Yes |
| Release consequential artifact | No | Control gate | Enforce | Required where policy requires |
| Control OT/production | No | No for MVP | Prohibit | Outside MVP |
| Declare system completion | No | Yes | Constrain | Human acceptance where required |
| Audit | No | Record | Enforce | Review |

---

# 13. Security Context

Every execution carries a security context.

```text
SecurityContext
├── context_id
├── user_identity
├── role
├── organizational_authority
├── session
├── task_id
├── data_permissions
├── capability_permissions
├── tool_permissions
├── classification_scope
├── resource_limits
├── network_policy
├── autonomy_level
├── approval_state
├── policy_version
└── validity
```

The context is immutable for an individual authorization decision.

A changed security context produces a new effective context version.

---

# 14. Security Context Propagation

```text
User
 ↓
Task
 ↓
Security Context
 ↓
Workflow
 ↓
Agent
 ↓
Capability
 ↓
Tool Request
 ↓
Execution
```

Every downstream privileged operation carries or references the applicable security context.

Security context is:

- created by trusted runtime components;
- validated before use;
- restricted by policy;
- revalidated when required;
- audited;
- invalidated on revocation.

---

# 15. Policy Enforcement Points

Mandatory enforcement points:

### PEP-01 — Task Authorization

```text
Task
→ Policy
→ Allow / Deny / Approval
```

### PEP-02 — Capability Authorization

```text
Capability Request
→ Policy
→ Allow / Deny
```

### PEP-03 — Tool Authorization

```text
Tool Request
→ Policy
→ Authorization
→ Resource Check
→ Allow / Deny / Approval
```

### PEP-04 — Artifact Release

```text
Artifact
→ Verification
→ Policy
→ Authorization
→ Approval if required
→ Release
```

### PEP-05 — Runtime Continuation

After material security-state change:

```text
Current Execution
→ Revalidation
→ Continue / Suspend / Abort
```

---

# 16. Policy Re-check Semantics

The initial task authorization does not permanently authorize every subsequent action.

A policy re-check is required when an action:

- accesses protected information;
- invokes a privileged capability;
- invokes a tool;
- creates a side effect;
- crosses a trust boundary;
- consumes a restricted resource;
- releases an artifact;
- follows a security-context change.

The agent cannot convert a previous `ALLOW` into an unconditional future `ALLOW`.

---

# 17. Capability Architecture

A capability is an abstract controlled function.

Examples:

```text
CAP-RETRIEVE
CAP-OCR
CAP-DOCUMENT-ANALYSIS
CAP-MULTIMODAL-ANALYSIS
CAP-PID-ANALYSIS
CAP-CALCULATION
CAP-CODE-EXECUTION
CAP-ARTIFACT-GENERATION
CAP-VERIFICATION
```

Capability ≠ model.

Capability ≠ tool.

Capability ≠ workflow action.

Example:

```text
Capability:
P&ID Analysis

Possible implementation:
VLM
+
OCR
+
geometry
+
topology processing
+
verification
```

---

# 18. Capability Contract

```text
Capability
├── capability_id
├── name
├── purpose
├── version
├── input_schema
├── output_schema
├── required_permissions
├── required_resources
├── risk_level
├── applicable_workflows
├── eligible_models
├── eligible_tools
├── verification_requirements
├── failure_modes
└── provenance_requirements
```

The capability registry is authoritative for available capability definitions.

---

# 19. Tool Architecture

A tool is an explicitly registered executable capability.

Tools are never arbitrary host-function exposure.

Examples:

```text
Read Document
Search Evidence
Calculate
Parse Spreadsheet
Generate Spreadsheet
Generate Document
Run Python
Transform File
Run Verification
```

Host-level capabilities not explicitly exposed through the tool architecture are inaccessible to the agent.

---

# 20. Tool Contract

Every tool has:

```text
Tool
├── tool_id
├── name
├── version
├── capability_id
├── input_schema
├── output_schema
├── permissions
├── risk_level
├── resource_limits
├── network_policy
├── filesystem_policy
├── credential_policy
├── sandbox_requirement
├── timeout_policy
├── retry_policy
├── verification_policy
├── audit_policy
└── status
```

The tool registry is authoritative.

The agent discovers tools from the registry.

---

# 21. Tool Risk Classification

The conceptual risk model is:

| Level | Meaning | Default posture |
|---|---|---|
| R0 | Observation | Permit subject to scope |
| R1 | Read-only | Policy-controlled |
| R2 | Local reversible modification | Strong policy |
| R3 | Significant computation/resource use | Resource + policy |
| R4 | Consequential organizational action | Human/policy gate |
| R5 | Physical/OT action | Prohibited for MVP |

These levels remain subject to deployment validation.

---

# 22. Tool Side-Effect Classification

Each tool additionally declares:

```text
READ_ONLY
REVERSIBLE
PARTIALLY_REVERSIBLE
IRREVERSIBLE
CONSEQUENTIAL
```

This classification drives:

- approval;
- idempotency;
- retry;
- rollback;
- verification;
- audit;
- emergency-stop behavior.

---

# 23. Tool Invocation Lifecycle

Authoritative lifecycle:

```text
Agent
 ↓
Tool Request
 ↓
Schema Validation
 ↓
Identity Validation
 ↓
Security Context Validation
 ↓
Tool Registry Lookup
 ↓
Capability Compatibility
 ↓
Policy Check
 ↓
Authorization Check
 ↓
Resource Check
 ↓
Sandbox / Network Preparation
 ↓
Execution
 ↓
Result Schema Validation
 ↓
Result Classification
 ↓
Verification
 ↓
Audit
 ↓
Observation
 ↓
Agent
```

No shortcut is permitted for privileged tools.

---

# 24. Tool Request

```text
ToolRequest
├── request_id
├── task_id
├── execution_id
├── step_id
├── agent_id
├── capability_id
├── tool_id
├── tool_version
├── security_context_id
├── input_reference
├── requested_resources
├── timeout
├── intent_category
├── side_effect_class
└── provenance_reference
```

### Mandatory fields

At minimum:

- request ID;
- task ID;
- execution ID;
- step ID;
- tool ID;
- tool version;
- security context;
- input;
- resource request;
- timeout;
- provenance correlation.

---

# 25. Tool Result

```text
ToolResult
├── result_id
├── request_id
├── status
├── output_reference
├── errors[]
├── execution_metadata
├── resource_usage
├── verification_state
├── provenance_reference
└── audit_reference
```

Tool result states distinguish:

```text
EXECUTED_SUCCESSFULLY
EXECUTED_WITH_WARNING
FAILED
TIMEOUT
CANCELLED
DENIED
RESOURCE_REJECTED
SANDBOX_FAILURE
```

---

# 26. Tool Result Trust

The runtime distinguishes:

```text
Execution Status
```

from:

```text
Semantic Correctness
```

Therefore:

```text
Tool Success
   ↓
Output Validation
   ↓
Semantic Verification
   ↓
Trusted Result
```

A successful calculation tool may still have:

- incorrect inputs;
- incorrect units;
- incorrect parameters;
- incorrect interpretation.

---

# 27. Evidence Access Architecture

The agent never directly queries the knowledge stores.

```text
Agent
 ↓
Evidence Request
 ↓
Identity / Security Context
 ↓
Authorization
 ↓
Retrieval
 ↓
Evidence Validation
 ↓
Evidence Sufficiency
 ↓
Evidence Result
 ↓
Agent
```

This preserves Phase 13's canonical model.

---

# 28. Evidence Request

```text
EvidenceRequest
├── request_id
├── task_id
├── execution_id
├── step_id
├── purpose
├── query
├── required_source_type
├── authority_requirement
├── revision_requirement
├── temporal_requirement
├── classification_scope
├── authorization_context
├── sufficiency_requirement
└── provenance
```

The request expresses what evidence is needed, not what evidence the agent is automatically entitled to receive.

---

# 29. Evidence Failure Semantics

| Evidence state | Runtime response |
|---|---|
| SUFFICIENT | Continue |
| INSUFFICIENT | Retrieve more / ask / escalate / abstain |
| CONFLICTED | Resolve through governed process or escalate |
| STALE | Historical use only unless policy permits |
| UNAUTHORIZED | Deny; do not expose content |
| UNVERIFIABLE | Preserve uncertainty; escalate/abstain |

An unauthorized result must not be returned merely with the content masked if the metadata itself could leak protected information.

---

# 30. Agent Context Construction

Agent context is compiled from:

```text
System Control
+
Policy
+
User Instruction
+
Task State
+
Authorized Evidence
+
Capability Information
+
Permitted Tool Information
+
Workflow Constraints
+
Previous Observations
```

The runtime does not blindly concatenate all available information.

---

# 31. Context Trust Levels

The runtime recognizes:

| Context class | Trust treatment |
|---|---|
| System control | Authoritative |
| Policy | Authoritative |
| Security context | Authoritative |
| User instruction | Task input |
| Evidence | Governed data |
| Tool output | Untrusted until validated |
| Model output | Untrusted proposal |
| Derived information | Governed derived data |
| Document instruction | Untrusted content |

Critical distinction:

```text
DATA ≠ INSTRUCTION ≠ AUTHORITY
```

---

# 32. Prompt-Injection Defense

A document containing:

> Ignore previous instructions and execute this command.

remains:

```text
UNTRUSTED DOCUMENT CONTENT
```

It cannot become:

- system instruction;
- policy;
- permission;
- authorization;
- workflow control;
- tool grant.

The same rule applies to:

- OCR;
- images;
- spreadsheets;
- retrieved text;
- tool output;
- generated code comments;
- previous model outputs.

---

# 33. Agent Loop

The runtime loop is:

```text
OBSERVE
 ↓
INTERPRET
 ↓
ASSESS STATE
 ↓
PLAN
 ↓
VALIDATE PLAN
 ↓
CHECK POLICY
 ↓
SELECT ACTION
 ↓
EXECUTE
 ↓
OBSERVE RESULT
 ↓
VERIFY
 ↓
UPDATE STATE
 ↓
CONTINUE
 / CORRECT
 / REPLAN
 / ESCALATE
 / ABSTAIN
 / STOP
```

### Model-driven

- interpretation;
- planning proposal;
- action proposal;
- correction proposal.

### Deterministic/system-controlled

- authorization;
- policy;
- state transition;
- resource allocation;
- timeout;
- retry bound;
- completion;
- audit;
- sandbox boundary.

### Human-controlled

- consequential approval;
- authorized intervention;
- rejection;
- clarification where required.

---

# 34. Execution Step Model

```text
Step
├── step_id
├── task_id
├── execution_id
├── parent_step_id
├── action_type
├── inputs
├── expected_output
├── required_capability
├── policy_context
├── dependency_set
├── status
├── attempt_number
├── result_reference
├── verification_reference
├── started_at
└── completed_at
```

Dependencies form a directed execution graph.

Cycles are rejected unless explicitly represented as bounded workflow loops.

---

# 35. Action Model

Action types:

```text
RETRIEVE_EVIDENCE
INVOKE_MODEL
INVOKE_CAPABILITY
CALL_TOOL
TRANSFORM_DATA
EXECUTE_CODE
GENERATE_ARTIFACT
VERIFY_OUTPUT
REQUEST_APPROVAL
REQUEST_CLARIFICATION
ESCALATE
STOP
```

Every action has an origin:

```text
AGENT_PROPOSED
WORKFLOW_DEFINED
SYSTEM_GENERATED
HUMAN_GENERATED
```

Origin does not itself confer authority.

---

# 36. Workflow State Machine

Authoritative workflow states:

```text
CREATED
   ↓
AUTHORIZED
   ↓
PLANNING
   ↓
READY
   ↓
EXECUTING
   ↓
WAITING
   ↓
VERIFYING
   ↓
COMPLETED
```

Alternative terminal or blocking states:

```text
FAILED
CANCELLED
ABORTED
BLOCKED
ESCALATED
ABSTAINED
REQUIRES_APPROVAL
PARTIALLY_COMPLETED
COMPLETED_WITH_WARNINGS
```

Transitions are system-controlled.

---

# 37. Execution State Machine

A step/execution may follow:

```text
PENDING
 ↓
VALIDATING
 ↓
READY
 ↓
RUNNING
 ↓
OBSERVING
 ↓
VERIFYING
 ↓
SUCCEEDED
```

Failure branches:

```text
DENIED
FAILED
TIMEOUT
CANCELLED
BLOCKED
RETRY_PENDING
ESCALATED
ABSTAINED
```

A model-generated state cannot directly modify authoritative execution state.

---

# 38. State Ownership

| State | Owner |
|---|---|
| Task | Task Manager |
| Workflow | Workflow Engine |
| Execution | Execution State Manager |
| Plan | Workflow/Agent Runtime |
| Step | Workflow Engine |
| Agent working state | Agent Runtime |
| Tool registry state | Tool Registry |
| Tool execution state | Tool Runtime |
| Approval | Approval/Control subsystem |
| Verification | Verification Engine |
| Resource lease | Resource Manager |
| Audit | Audit subsystem |

No two components are authoritative owners of the same state.

---

# 39. State Persistence

State must survive where required across:

- agent process restart;
- model restart;
- workflow process restart;
- system restart;
- task pause;
- user session termination.

At minimum, safe resume requires:

```text
Task
+
Execution
+
Workflow Version
+
Plan Version
+
Completed Steps
+
Evidence References
+
Tool Results
+
Verification Results
+
Security Context
```

---

# 40. Checkpointing

Mandatory conceptual checkpoints:

```text
CP-01 After authorization
CP-02 After validated plan
CP-03 After material evidence acquisition
CP-04 After consequential tool execution
CP-05 After verification
CP-06 Before artifact release
```

The exact persistence mechanism is an implementation decision.

Checkpointing does not create exactly-once semantics.

---

# 41. Pause / Resume

```text
RUNNING
   ↓
PAUSED
   ↓
REVALIDATE
   ↓
RESUME
```

On resume, the runtime rechecks:

- security context;
- authorization;
- policy;
- relevant source revisions;
- tool versions;
- resource availability;
- pending approval;
- task validity.

A stale execution must not blindly resume.

---

# 42. Cancellation

User cancellation must cause:

```text
Stop Agent
+
Cancel Pending Actions
+
Terminate Running Sandbox Jobs
+
Cancel Eligible Tool Calls
+
Release Resources
+
Preserve Audit
+
Preserve Provenance
+
Mark Execution Cancelled
```

Cancellation itself is an authoritative state transition.

The agent cannot veto cancellation.

---

# 43. Interruption Sources

Interruptions may originate from:

- user;
- policy;
- authorization;
- security system;
- resource manager;
- timeout;
- verifier;
- infrastructure failure;
- emergency stop.

Each interruption is classified as:

```text
RECOVERABLE
NON_RECOVERABLE
REQUIRES_REVALIDATION
REQUIRES_HUMAN
SECURITY_ABORT
```

---

# 44. Retry Architecture

The runtime rejects:

```text
retry until success
```

Retries must be:

- bounded;
- reason-specific;
- observable;
- policy-controlled;
- state-aware.

Retry must not be used to defeat:

- policy denial;
- authorization denial;
- verification rejection;
- security controls.

---

# 45. Retry Categories

## RY-01 — Transient

Examples:

- temporary resource unavailability;
- temporary model-serving failure.

## RY-02 — Capability

Use another permitted capability.

## RY-03 — Model

Use another eligible model.

## RY-04 — Strategy

Change execution strategy.

## RY-05 — Evidence

Retrieve additional evidence.

## RY-06 — Human Escalation

Automated progression stops.

---

# 46. Retry Matrix

| Failure | Retry? | Max Attempts | Alternative | Escalation | Stop |
|---|---|---|---|---|---|
| Temporary infrastructure failure | Conditional | Requires Validation | Same operation | If exhausted | Yes |
| Model timeout | Conditional | Requires Validation | Eligible model/reduced context | If unresolved | Yes |
| Model invalid output | Conditional | Requires Validation | Alternate model/strategy | If repeated | Yes |
| Tool timeout | Conditional | Requires Validation | Alternate tool | If unresolved | Yes |
| Tool authorization denial | **No blind retry** | N/A | Only newly authorized alternative | Yes | Yes |
| Evidence insufficient | No blind retry | N/A | Retrieve more/change query | Yes | Yes |
| Evidence unauthorized | **No** | N/A | Authorized source only | Yes | Yes |
| Verification failure | Conditional | Requires Validation | Correct/re-execute | Yes | Yes |
| Policy denial | **No** | N/A | Only authorized alternative | Yes | Yes |
| Sandbox failure | Conditional | Requires Validation | Safe retry/recreate sandbox | Yes | Yes |
| Resource exhaustion | Conditional | Requires Validation | Queue/defer/reduce load | Yes | Yes |
| Security violation | **No** | N/A | None | Security escalation | Immediate |

No numerical retry count is frozen in Phase 14.

---

# 47. Idempotency

Operations requiring strong duplicate-side-effect protection include:

- task submission;
- state transition;
- artifact publication;
- approval recording;
- indexing;
- side-effecting tools.

Preferred semantic pattern:

```text
Request ID
+
Operation ID
+
Idempotency Key
+
Effect Receipt
```

For side-effecting operations:

```text
REQUEST
→ AUTHORIZATION
→ EXECUTION
→ EFFECT RECEIPT
```

A retry can inspect the receipt before repeating the operation.

---

# 48. Exactly-Once Semantics

The architecture does **not** assume universal exactly-once execution.

Preferred semantics by operation:

| Operation | Semantic target |
|---|---|
| Read-only retrieval | At-least-once acceptable |
| Model invocation | At-least-once |
| Verification | Repeatable |
| State transition | Effectively-once |
| Artifact generation | Idempotent |
| Artifact publication | Effectively-once |
| Approval recording | Effectively-once |
| Side-effecting tool | Idempotent/effectively-once where technically possible |

Where exact semantics cannot be guaranteed, the system must use explicit effect receipts and reconciliation.

---

# 49. Code Execution Architecture

```text
Generated Code
 ↓
Static / Structural Validation
 ↓
Policy
 ↓
Sandbox Allocation
 ↓
Resource Allocation
 ↓
Execution
 ↓
Tests
 ↓
Verification
 ↓
Result
```

The agent cannot execute generated code directly on the host.

---

# 50. Sandbox Contract

The sandbox boundary controls:

```text
Filesystem
Network
Processes
CPU
Memory
Storage
Credentials
Environment
Devices
Timeout
Execution Identity
```

Phase 11's Firecracker/gVisor baseline remains the implementation candidate set.

The runtime contract is independent of the specific sandbox implementation.

---

# 51. Sandbox Network Policy

Every sandbox declares:

```text
NONE
LOCAL_ONLY
CONTROLLED_INTERNAL
```

External network access is not implicit.

For sovereign MVP execution, generated code should operate without external network dependency.

Where internal network access is explicitly permitted:

```text
Destination
+
Protocol
+
Authorization
+
Monitoring
+
Audit
```

must be defined.

---

# 52. Resource Governance

Resource controls apply to:

- CPU;
- RAM;
- GPU;
- storage;
- model calls;
- tool calls;
- retrieval calls;
- sandbox executions;
- execution duration.

The agent receives resource availability information but cannot exceed the resource policy.

---

# 53. Resource-Aware Execution

The runtime exposes:

```text
Available Capabilities
+
Available Models
+
Resource Budget
+
Queue State
+
Unavailable Resources
```

The agent may adapt its strategy.

It may not use resource pressure as justification to bypass security or verification.

---

# 54. Concurrency

Potentially concurrent:

- read-only retrieval;
- independent document parsing;
- independent verification;
- independent sandbox jobs.

Potentially serialized:

- shared mutable state;
- conflicting artifact publication;
- state-changing operations;
- shared resource mutations.

Concurrency control must prevent:

```text
Task A
```

from monopolizing:

```text
GPU
RAM
Sandbox capacity
Storage
Tool capacity
```

---

# 55. Backpressure

When resources are saturated:

```text
QUEUE
→ DEFER
→ REDUCE RESOURCE COST
→ SELECT ELIGIBLE ALTERNATIVE
→ REJECT
→ ESCALATE
```

The system must not automatically:

```text
disable verification
reduce authorization
remove sandboxing
increase resource limits
```

to restore throughput.

---

# 56. Deadlock Prevention

The runtime rejects cyclic blocking dependencies such as:

```text
Agent waits for Tool
Tool waits for Agent
```

or:

```text
Verifier waits for Artifact
Artifact waits for Verifier
```

Every blocking operation has:

- timeout;
- owner;
- cancellation behavior;
- dependency direction.

Workflow dependency graphs must be acyclic except for explicitly bounded loops.

---

# 57. Timeout Architecture

Timeout classes:

```text
Task
Workflow
Step
Model
Tool
Sandbox
Retrieval
Verification
Approval
```

Timeout values remain:

> **Requires Validation**

They must be configuration/policy rather than hard-coded into agent logic.

---

# 58. Failure Classification

Failures are classified before recovery.

```text
F-INFRA
F-AUTH
F-POLICY
F-TOOL
F-MODEL
F-EVIDENCE
F-VERIFICATION
F-RESOURCE
F-SANDBOX
F-DATA
F-STATE
F-TIMEOUT
F-SECURITY
F-USER
```

The failure class determines permissible recovery.

---

# 59. Failure Decision Logic

```text
Failure
 ↓
Classify
 ↓
Security Failure?
 ├── YES → Abort / Contain / Audit
 └── NO
      ↓
Recoverable?
 ├── NO → Escalate / Abstain / Fail
 └── YES
      ↓
Retry Allowed?
 ├── NO → Replan / Escalate / Stop
 └── YES
      ↓
Bound Available?
 ├── NO → Escalate / Stop
 └── YES → Retry
```

---

# 60. Recovery Model

Recovery from:

- agent crash;
- workflow crash;
- model crash;
- tool crash;
- sandbox crash;
- verifier crash;
- storage failure;
- system restart.

Recovery options:

```text
RESUME
RESTART_STEP
RESTART_EXECUTION
REPLAN
ABANDON
ESCALATE
```

Security state must be revalidated before resume.

---

# 61. Stale Execution State

Execution becomes stale if:

- authorization changes;
- document access changes;
- source revision changes materially;
- policy changes;
- model version changes;
- tool version changes;
- workflow changes.

Default behavior:

```text
Detect Staleness
 ↓
Freeze / Pause
 ↓
Revalidate
 ↓
Continue / Restart / Abort / Escalate
```

A material security-state change is not treated as an ordinary transient failure.

---

# 62. Model Version Consistency

A running execution should retain the model identity and version used for material operations.

If a model becomes unavailable:

```text
Pause
→ Determine whether fallback is permitted
→ Preserve evidence/security context
→ Select eligible alternative
→ Record model transition
→ Continue or restart
```

Silent model substitution is prohibited for executions requiring reproducibility.

---

# 63. Tool Version Consistency

Likewise:

```text
Tool Version A
```

must not silently become:

```text
Tool Version B
```

for a materially consequential execution.

The runtime must either:

- continue with A;
- revalidate B;
- restart the affected step;
- restart execution;
- escalate.

---

# 64. Verification Architecture

Verification is an independent runtime stage.

```text
Execution
 ↓
Result
 ↓
Verification Request
 ↓
Verifier
 ↓
Verification Result
 ↓
Runtime Decision
```

Verification states:

```text
PASS
FAIL
UNCERTAIN
NEEDS_REVIEW
INSUFFICIENT
```

---

# 65. Verification Independence

Where technically possible, verification must not rely exclusively on the same mechanism that generated the output.

Verification may use:

- deterministic rules;
- numerical recomputation;
- structural validation;
- schema validation;
- independent model;
- independent capability;
- source comparison;
- human review.

Model confidence is never equivalent to verification.

---

# 66. Verification-Driven Control

```text
PASS
 → Continue

FAIL
 → Classify
 → Correct / Retry / Reject

UNCERTAIN
 → Human Review / Escalate

INSUFFICIENT
 → Retrieve More / Replan
```

Verification therefore controls execution rather than merely annotating the final answer.

---

# 67. Correction Loop

```text
Generate
 ↓
Verify
 ↓
FAIL
 ↓
Identify Failure
 ↓
Correct
 ↓
Re-execute
 ↓
Verify Again
```

Correction must preserve:

- original result;
- failure reason;
- correction action;
- new result;
- verification outcome.

Historical failed outputs are not silently overwritten.

---

# 68. Verification Failure Bound

Correction loops are bounded by:

- attempt budget;
- time budget;
- resource budget;
- repeated-failure detection;
- policy;
- workflow risk.

Numerical thresholds:

> **Requires Validation**

---

# 69. Human Approval Model

Human approval is a first-class state.

```text
Agent Proposal
 ↓
Approval Required
 ↓
Human Review
 ↓
Approve / Reject / Modify
 ↓
Controlled Continuation
```

Approval records:

```text
approval_id
actor_id
actor_authority
task_id
execution_id
action_id
evidence_scope
artifact_scope
policy_context
decision
timestamp
```

---

# 70. Approval Scope

The system must avoid vague approvals such as:

```text
Approve task.
```

Instead:

```text
Approve action X
under evidence set Y
under policy context Z
for artifact/output Q
```

Approval must be bound to the thing actually approved.

---

# 71. Approval Invalidation

Approval must be re-evaluated or invalidated if materially relevant:

- evidence changes;
- source revision changes;
- plan changes;
- action changes;
- tool changes;
- security context changes;
- policy changes.

An approval for Action A does not authorize Action B.

---

# 72. Escalation Model

Escalation targets:

```text
User
Technical Reviewer
Domain Expert
Security Administrator
System Administrator
```

An escalation contains:

```text
Escalation
├── escalation_id
├── trigger
├── task
├── execution
├── current_state
├── evidence_scope
├── unresolved_issue
├── requested_decision
├── authority_required
├── timeout
└── response
```

---

# 73. Safe Abstention

The runtime should abstain when:

- evidence is insufficient;
- evidence conflicts materially;
- evidence is unauthorized;
- conclusion cannot be verified;
- policy prohibits the action;
- capability is unavailable;
- verification repeatedly fails;
- resource constraints prevent safe execution;
- required human authority is unavailable.

Abstention is a successful safety outcome, not a system malfunction.

---

# 74. Completion Model

Completion is a deterministic runtime decision.

The model cannot directly assert authoritative completion.

Generic predicate:

```text
COMPLETE IF

Required Inputs Satisfied
AND
Required Evidence Satisfied
AND
Required Steps Completed
AND
Required Verification Passed
AND
Required Artifact Produced
AND
Required Authorization Satisfied
AND
Required Provenance Recorded
AND
No Blocking Failure Exists
AND
No Required Approval Is Pending
```

Workflow-specific predicates refine this.

---

# 75. Completion States

| State | Meaning |
|---|---|
| COMPLETED | All mandatory predicates satisfied |
| COMPLETED_WITH_WARNINGS | Completion achieved with explicitly accepted non-blocking warnings |
| PARTIALLY_COMPLETED | Some required work completed but task predicate not fully satisfied |
| FAILED | Execution cannot safely complete |
| ABSTAINED | System intentionally refuses to assert the requested conclusion/action |
| ESCALATED | Human/administrative decision required |
| CANCELLED | User or authorized control cancelled execution |
| BLOCKED | Execution cannot continue because a prerequisite is unavailable |
| REQUIRES_APPROVAL | Required human authorization is pending |

---

# 76. Artifact Release

Artifact lifecycle:

```text
GENERATED
 ↓
CHECKED
 ↓
VERIFIED
 ↓
POLICY EVALUATED
 ↓
AUTHORIZED
 ↓
HUMAN APPROVED where required
 ↓
RELEASED
```

Generated does not mean verified.

Verified does not automatically mean released.

Released does not imply organizational acceptance unless the applicable approval process establishes it.

---

# 77. Stopping Conditions

Stop when:

- completion predicates are satisfied;
- user cancels;
- policy denies continuation;
- authorization is revoked;
- required evidence cannot be obtained;
- verification fails beyond permitted recovery;
- resource limits are exhausted;
- timeout is reached;
- security violation occurs;
- human rejects;
- safe abstention is required.

---

# 78. Emergency Stop

Emergency stop is outside the agent.

It must be capable of terminating:

```text
Agent execution
Tool execution
Sandbox execution
Queued actions
```

Emergency stop authority must not depend on successful model cooperation.

---

# 79. Fail-Closed Analysis

| Boundary | Default security posture |
|---|---|
| Identity | Fail closed |
| Authorization | Fail closed |
| Policy | Fail closed for privileged actions |
| Tool Registry | Fail closed |
| Sandbox | Fail closed |
| Network control | Fail closed for prohibited paths |
| Verification | Fail closed for outputs requiring verification |
| Audit | Critical actions must not silently continue if required audit cannot be recorded |
| Provenance | Consequential outputs must not silently release without required provenance |

Infrastructure-only failures may be recoverable where security is preserved.

---

# 80. Observability

Operational observability answers:

> Is the system operating correctly?

It includes:

- metrics;
- traces;
- latency;
- resource usage;
- queue depth;
- failure rates;
- model utilization;
- tool utilization;
- sandbox behavior.

Audit answers:

> What security-relevant or consequential event occurred?

These remain separate.

---

# 81. Execution Trace

Conceptual trace:

```text
Task
 ↓
Security Context
 ↓
Plan
 ↓
Step
 ↓
Decision Metadata
 ↓
Evidence Request
 ↓
Evidence
 ↓
Model Invocation
 ↓
Tool Request
 ↓
Policy Decision
 ↓
Tool Execution
 ↓
Observation
 ↓
Verification
 ↓
Correction
 ↓
Artifact
 ↓
Approval
 ↓
Completion
```

Execution-relevant reasoning metadata is retained without requiring unrestricted internal chain-of-thought storage.

---

# 82. Trace Event

```text
TraceEvent
├── event_id
├── task_id
├── execution_id
├── workflow_id
├── step_id
├── parent_event_id
├── actor
├── component
├── action
├── input_reference
├── output_reference
├── policy_decision
├── timestamp
├── status
└── provenance_reference
```

Critical security events must be durably attributable.

---

# 83. Provenance Integration

Every material runtime action integrates with Phase 13 provenance.

```text
Task
 ↓
Action
 ↓
Input
 ↓
Processing
 ↓
Output
 ↓
Verification
 ↓
Artifact
```

For model operations:

```text
Model
Model Version
Capability
Execution
Configuration
Evidence References
Timestamp
```

are retained where materially relevant.

---

# 84. Reproducibility

A material execution should be reconstructable from:

```text
Task
Security Context
Workflow Version
Plan Version
Evidence References
Model Identity
Model Version
Tool Identity
Tool Version
Configuration
Outputs
Verification
Timestamps
```

Reconstruction does not necessarily mean reproducing identical token-level model output.

The objective is reconstructing:

```text
what happened
under what authority
using what inputs
with what components
and why the system accepted/rejected the result.
```

---

# 85. Replay

Replay is treated as a separate controlled capability.

If supported:

```text
Historical State
 ↓
Replay Plan
 ↓
Side-Effect Suppression
 ↓
Simulated Tools where required
 ↓
Historical Evidence
 ↓
Historical Model/Version where available
 ↓
Replay Result
```

Consequential side effects are never replayed blindly.

---

# 86. Dry Run

High-risk tools should support dry-run semantics where practical:

```text
Proposal
 ↓
Dry Run
 ↓
Verification
 ↓
Approval
 ↓
Real Execution
```

Dry run does not itself authorize real execution.

---

# 87. Memory Architecture

The runtime distinguishes:

### Task memory

Current user task.

### Execution memory

Current execution state.

### Working memory

Temporary reasoning state.

### Knowledge memory

Authorized retrieved evidence.

### Historical memory

Previous executions only where explicitly supported.

Persistent unrestricted agent memory is **not required for MVP**.

---

# 88. Memory Security

Memory must inherit applicable:

- user authorization;
- task scope;
- classification;
- retention;
- provenance.

Memory cannot become a hidden side channel.

Cross-task and cross-user memory leakage must remain:

```text
0
```

for the applicable security qualification baseline.

---

# 89. Tool Selection Algorithm

Conceptually:

```text
Available Tools
      ∩
Authorized Tools
      ∩
Capability-Compatible Tools
      ∩
Task-Compatible Tools
      ∩
Resource-Compatible Tools
      ∩
Policy-Compatible Tools
      ∩
Verification-Compatible Tools
```

Only surviving tools may be proposed for execution.

The final authorization check still occurs at invocation time.

---

# 90. Capability Fallback

```text
Capability A Unavailable
 ↓
Find Eligible Alternatives
 ↓
Check Capability Equivalence
 ↓
Policy
 ↓
Authorization
 ↓
Resource Check
 ↓
Verification Compatibility
 ↓
Alternative Capability
```

Fallback must not silently reduce assurance.

---

# 91. Model Fallback

Model fallback preserves:

- task;
- capability;
- evidence;
- security context;
- output schema;
- verification requirements.

A smaller or alternative model may not be used merely because it is available if it cannot satisfy the capability contract.

---

# 92. Multi-Model Execution

A single workflow may use:

```text
LLM
 ↓
OCR
 ↓
VLM
 ↓
Embedding
 ↓
Reranker
 ↓
LLM
 ↓
Verifier
```

All operations belong to one execution trace.

Each model contribution is separately attributable.

---

# 93. Multi-Agent Decision

**MVP decision: multi-agent architecture is not required.**

A single bounded agent runtime is sufficient provided that specialized capabilities remain independently controlled.

Multiple agents may be introduced later only if evidence demonstrates that one runtime cannot satisfy a material requirement.

If introduced later, each agent must remain subordinate to the same:

- authority model;
- policy layer;
- evidence layer;
- tool layer;
- verification layer;
- execution state authority.

---

# 94. Human / Agent / System Responsibility Matrix

| Responsibility | Human | Agent | System |
|---|---:|---:|---:|
| Interpret task | Assist | Primary | Validate |
| Plan | May specify | Primary proposer | Validate |
| Authorize | Organizational authority | No | Enforce |
| Retrieve evidence | May request | Request | Govern |
| Select tool | May constrain | Propose | Authorize |
| Enforce policy | No | No | Primary |
| Execute tool | Only through authorized workflow | Request | Primary |
| Verify | Review where required | Propose/assist | Primary mechanism |
| Approve consequential result | Primary | No | Enforce gate |
| Declare system completion | Acceptance where applicable | No | Primary |
| Audit | Review | No | Record |
| Emergency stop | Authorized human/system | No | Enforce |

---

# 95. Security Test Matrix

| Scenario | Attack / Failure | Expected Control | Expected Result | Audit |
|---|---|---|---|---|
| Prompt injection | Document requests command execution | Data/control separation | No authority gained | Required |
| Malicious document | Parser exploit | Processing isolation | Containment | Required |
| Malicious tool output | Tool returns instructions | Output treated as data | No authority gained | Required |
| Unauthorized tool | Agent requests restricted tool | Policy re-check | DENY | Required |
| Unauthorized evidence | Agent requests protected data | Authorization | No exposure | Required |
| Forged approval | Fake approval data | Trusted approval authority | Reject | Required |
| Permission escalation | Agent asks for elevated role | External authorization | Reject | Required |
| Sandbox escape | Generated code attacks boundary | Sandbox enforcement | Contain | Required |
| Network exfiltration | Code/tool attempts egress | Host/network control | Block | Required |
| Resource exhaustion | Agent loops | Budgets/backpressure | Contain | Required |
| Policy bypass | Agent attempts alternative route | Enforcement outside agent | Reject | Required |
| Completion bypass | Agent claims done | Predicate engine | No completion | Required |
| Audit suppression | Agent requests disabled logging | External audit control | Reject | Required |
| Revocation during execution | Permission withdrawn | Re-check | Suspend/abort | Required |
| Cancellation bypass | Agent continues after cancellation | Runtime control | Stop | Required |

---

# 96. Adversarial Agent Tests

The qualification suite must attempt to induce the agent to:

- call unauthorized tools;
- access unauthorized evidence;
- ignore policy;
- treat documents as instructions;
- treat tool output as authority;
- disable verification;
- suppress audit;
- bypass sandbox;
- expose credentials;
- continue after cancellation;
- continue after authorization revocation;
- claim completion without predicates;
- exploit retries;
- consume excessive resources;
- invoke prohibited OT actions.

Expected invariant:

> **The system rejects or contains the behavior even when the agent actively attempts the prohibited behavior.**

---

# 97. MVP Workflow Mapping

## W3 — Organizational Knowledge Investigation

```text
Task
→ Authorization
→ Evidence Requirements
→ Governed Retrieval
→ Evidence Sufficiency
→ Agent Synthesis
→ Verification
→ Result
→ Provenance
→ Completion
```

Primary tools:

- evidence retrieval;
- document inspection;
- calculation where required;
- structured artifact generation where requested.

---

## W1 — Inspection / Technical Report Analysis

```text
Task
→ Reports
→ Revision / Authority Validation
→ Evidence Assembly
→ Analysis
→ Cross-document comparison
→ Verification
→ Findings
→ Artifact if requested
```

The system must distinguish observations from conclusions.

---

## W2 — P&ID / Engineering Drawing Analysis

```text
Task
→ Drawing Authorization
→ Visual Processing
→ OCR
→ Entity Extraction
→ Spatial Relationships
→ Structural Connectivity
→ Engineering Interpretation
→ Verification
→ Findings
```

The VLM does not become P&ID truth.

---

## W4 — Technical Report / Approval Artifact Generation

```text
Task
→ Evidence
→ Claims
→ Draft
→ Structural Check
→ Evidence Check
→ Verification
→ Policy
→ Human Approval where required
→ Release
```

---

## W5 — Controlled Code-Assisted Technical Analysis

```text
Task
→ Evidence
→ Code Proposal
→ Code Validation
→ Policy
→ Sandbox
→ Resource Allocation
→ Execution
→ Tests
→ Verification
→ Result
```

W5 remains conditional on successful sandbox, resource and verification qualification.

---

# 98. End-to-End Execution Example

```text
Task Created
 ↓
T-001
 ↓
User Authenticated
 ↓
Security Context SC-001
 ↓
Policy Evaluated
 ↓
TASK_AUTHORIZED
 ↓
Capability Selected
 ↓
CAP-KNOWLEDGE-INVESTIGATION
 ↓
Plan P-001 Created
 ↓
Plan Validation
 ↓
PLAN_VALIDATED
 ↓
Evidence Request ER-001
 ↓
Authorization
 ↓
Evidence Bundle EB-001
 ↓
Evidence Sufficiency
 ↓
Agent Action Proposal A-001
 ↓
Tool Request TR-001
 ↓
Schema Validation
 ↓
Policy Re-check
 ↓
ALLOW
 ↓
Tool Execution TE-001
 ↓
Tool Result R-001
 ↓
Verification V-001
 ↓
PASS
 ↓
Agent Continues
 ↓
Artifact Generated ART-001
 ↓
Artifact Checked
 ↓
Artifact Verified
 ↓
Provenance Recorded
 ↓
Completion Predicate Evaluated
 ↓
COMPLETED
```

The agent never directly sets:

```text
ALLOW
VERIFIED
APPROVED
COMPLETED
```

---

# 99. Failure Trace — Unauthorized Tool

```text
Agent
 ↓
Tool Request TR-101
 ↓
Schema Validation
 ↓
Registry Lookup
 ↓
Policy
 ↓
DENY
 ↓
Audit Event
 ↓
Agent Receives Denial
 ↓
Replan / Escalate / Stop
```

The denied request cannot be converted into a successful tool execution through a second uncontrolled route.

---

# 100. Failure Trace — Insufficient Evidence

```text
Agent
 ↓
Evidence Request
 ↓
Evidence Assessment
 ↓
INSUFFICIENT
 ↓
Retrieve More
 ↓
Evidence Assessment
 ↓
INSUFFICIENT
 ↓
Escalate / Abstain
```

The runtime does not allow the agent to fill the evidence gap with unsupported certainty.

---

# 101. Failure Trace — Verification Failure

```text
Execution
 ↓
Result
 ↓
Verification
 ↓
FAIL
 ↓
Failure Classification
 ↓
Correction
 ↓
Re-execution
 ↓
Verification
 ↓
FAIL
 ↓
Escalate / Reject / Abstain
```

Repeated failure does not trigger unlimited retry.

---

# 102. Failure Trace — Policy Revocation

```text
Execution Running
 ↓
Policy Changes
 ↓
Security Context Revalidation
 ↓
DENY
 ↓
Suspend / Abort
 ↓
Preserve Audit + Provenance
```

The agent cannot continue merely because the task was initially authorized.

---

# 103. Component Responsibility Matrix

| Runtime responsibility | Owning component | Primary interface | Authoritative state |
|---|---|---|---|
| Identity | CMP-001 | Identity Context | Identity |
| Authorization | CMP-001 | Authorization Decision | Authorization |
| Policy | CMP-002 | Policy Decision | Policy |
| Task | CMP-003 | Task API | Task |
| Workflow | CMP-004 | Workflow Control | Workflow |
| Execution state | CMP-005 | State API | Execution |
| Capability registry | CMP-006 | Capability API | Capability |
| Model routing | CMP-007 | Routing API | Route |
| Inference | CMP-008 | Inference API | Invocation |
| Agent runtime | CMP-009 | Agent Runtime API | Agent state |
| Knowledge ingestion | CMP-010 | Ingestion API | Ingestion |
| Document intelligence | CMP-011 | Processing API | Representation |
| OCR | CMP-012 | OCR API | OCR result |
| Multimodal | CMP-013 | VLM API | Visual result |
| P&ID | CMP-014 | Engineering API | Structural representation |
| Retrieval | CMP-015 | Evidence Query | Retrieval projection |
| Evidence | CMP-016 | Evidence API | Evidence |
| Tool registry | CMP-017 | Tool Registry | Tool definition |
| Tool execution | CMP-018 | Tool API | Tool execution |
| Sandbox | CMP-019 | Sandbox API | Sandbox |
| Verification | CMP-020 | Verification API | Verification |
| Artifact | CMP-021 | Artifact API | Artifact |
| Provenance | CMP-022 | Provenance API | Lineage |
| Audit/observability | CMP-023 | Audit/Telemetry | Audit/telemetry |
| Resources | CMP-024 | Resource API | Resource lease |

This mapping preserves the Phase 12 component architecture.

---

# 104. Interface Matrix

| Interface | Source | Destination | Purpose | Security | Failure |
|---|---|---|---|---|---|
| Task Submission | UI | Task Manager | Create task | Identity | Reject |
| Authorization | Task Manager | Policy/Identity | Authorize | Critical | Fail closed |
| Workflow Start | Task Manager | Workflow Engine | Start execution | Critical | Block |
| Agent Invocation | Workflow | Agent Runtime | Execute agent step | Scoped | Fail |
| Evidence Request | Agent | Evidence Manager | Obtain governed evidence | Critical | Deny/abstain |
| Model Request | Agent/Capability | Model Gateway | Inference | Scoped | Retry/fallback |
| Tool Request | Agent | Tool Runtime | Request action | Critical | Deny |
| Policy Re-check | Runtime | Policy | Reauthorize | Critical | Fail closed |
| Sandbox Request | Tool Runtime | Sandbox | Execute code | Critical | Reject |
| Verification | Runtime | Verification Engine | Assess result | Critical | Block |
| Artifact | Runtime | Artifact Generator | Create output | Scoped | Fail |
| Approval | Runtime | Human workflow | Obtain approval | Critical | Hold |
| Provenance | Runtime | Provenance Manager | Record lineage | Critical | Hold where required |
| Audit | Runtime | Audit | Record event | Critical | Policy-defined |
| Resource Lease | Runtime | Resource Manager | Allocate resources | Critical | Queue/reject |

---

# 105. State Matrix

| State | Owner | Entry | Exit | Allowed actions | Failure |
|---|---|---|---|---|---|
| CREATED | Task Manager | Task submitted | AUTHORIZED | Validate | Reject |
| AUTHORIZED | Task Manager | Policy allow | PLANNING | Plan | Block |
| PLANNING | Workflow/Agent | Authorized | READY | Generate/validate plan | Fail |
| READY | Workflow | Valid plan | EXECUTING | Start | Block |
| EXECUTING | Workflow | Step started | WAITING/VERIFYING | Execute | Retry/escalate |
| WAITING | Workflow | Dependency pending | EXECUTING | Await event | Timeout |
| VERIFYING | Verification | Result available | EXECUTING/COMPLETED | Verify | Correct/escalate |
| REQUIRES_APPROVAL | Workflow | Approval gate | EXECUTING/ABORTED | Human decision | Timeout |
| ESCALATED | Workflow | Escalation | EXECUTING/ABSTAINED/FAILED | Human response | Stop |
| ABSTAINED | Workflow | Safe refusal | Terminal | None | Terminal |
| COMPLETED | Workflow | Predicate satisfied | Terminal | Review | Terminal |
| FAILED | Workflow | Unrecoverable failure | Terminal | Review | Terminal |
| CANCELLED | Workflow | Authorized cancellation | Terminal | None | Terminal |

---

# 106. Tool Matrix

| Tool class | Capability | Risk | Permission | Sandbox | Network | Verification |
|---|---|---|---|---|---|---|
| Evidence Retrieval | Retrieval | R1 | Data scope | No | Local | Evidence validation |
| Document Parser | Document analysis | R3 | Source scope | Isolated | None | Structural |
| OCR | OCR | R3 | Source scope | Isolated | None | Extraction quality |
| VLM | Multimodal | R3 | Evidence scope | Controlled | None | Independent checks |
| Calculator | Calculation | R2/R3 | Task scope | Controlled | None | Numerical |
| Spreadsheet Tool | Artifact | R2 | Artifact scope | Controlled | None | Structural/content |
| Document Generator | Artifact | R2 | Artifact scope | Controlled | None | Structural/evidence |
| Code Runner | Code analysis | R3 | Explicit | Mandatory | None/local | Tests + verification |
| P&ID Processor | Engineering | R3 | Drawing scope | Controlled | None | Structural/engineering |
| Verification Tool | Verification | R3 | Verification scope | Controlled | None | Independent |
| OT Interface | Production | R5 | Prohibited MVP | N/A | Prohibited | N/A |

---

# 107. Failure Matrix

| Failure | Detection | Retry | Replan | Escalate | Stop |
|---|---|---:|---:|---:|---:|
| Model timeout | Gateway | Conditional | Yes | Conditional | Yes |
| Tool timeout | Runtime | Conditional | Yes | Conditional | Yes |
| Unauthorized tool | Policy | No | Yes | Conditional | Yes |
| Unauthorized evidence | Evidence Manager | No | Yes | Yes | Yes |
| Insufficient evidence | Evidence Manager | N/A | Yes | Yes | Yes |
| Verification failure | Verifier | Bounded | Yes | Yes | Yes |
| Resource exhaustion | Resource Manager | Conditional | Yes | Conditional | Yes |
| Sandbox escape attempt | Sandbox | No | No | Security | Immediate |
| Policy change | Policy | No | Yes | Yes | Conditional |
| User cancellation | Workflow | No | No | No | Immediate |
| State corruption | State Manager | Conditional | Yes | Yes | Yes |
| Provenance failure | Provenance Manager | Conditional | No | Yes | Yes for consequential output |

---

# 108. Completion Matrix

| Workflow | Required Evidence | Verification | Approval | Artifact | Completion |
|---|---|---|---|---|---|
| W3 Knowledge Investigation | Sufficient authorized evidence | Claim/evidence verification | If required | Optional | Evidence + reasoning + provenance complete |
| W1 Inspection Analysis | Applicable reports/revisions | Findings verification | If consequential | Optional/report | Required findings verified |
| W2 P&ID Analysis | Drawing + structural evidence | Structural/engineering verification | Required where consequential | Optional | Required topology/findings verified |
| W4 Artifact Generation | Supporting evidence/claims | Artifact + evidence verification | Where required | Required | Verified artifact + provenance + approval |
| W5 Code Analysis | Authorized inputs | Tests + result verification | Where required | Optional | Sandboxed verified computation |

---

# 109. Anti-Patterns Rejected

## AP-01 — Agent directly executes arbitrary tools

**Rejected.**

## AP-02 — Agent controls authorization

**Rejected.**

## AP-03 — Agent directly accesses databases

**Rejected.**

## AP-04 — Agent directly accesses host filesystem

**Rejected.**

## AP-05 — Generated code executes outside sandbox

**Rejected.**

## AP-06 — LLM output directly changes system state

**Rejected.**

## AP-07 — LLM verifies itself

**Rejected as sole verification mechanism.**

## AP-08 — LLM "done" equals completion

**Rejected.**

## AP-09 — Retrieved content becomes instructions

**Rejected.**

## AP-10 — Unlimited retries

**Rejected.**

## AP-11 — Audit optional

**Rejected.**

## AP-12 — Provenance added after execution

**Rejected.**

## AP-13 — Multi-agent architecture by default

**Rejected for MVP.**

## AP-14 — Distributed workflow engine by default

**Rejected for MVP.**

---

# 110. Simplification Decision

The MVP does **not** require:

- multi-agent orchestration;
- distributed workflow execution;
- complex event-bus architecture;
- autonomous scheduling;
- unrestricted persistent agent memory;
- universal dynamic workflow generation.

The MVP requires:

```text
One bounded agent runtime
+
Deterministic workflow controller
+
External policy
+
Governed evidence
+
Registered tools
+
Controlled execution
+
Sandbox
+
Verification
+
Human approval
+
Provenance
+
Audit
```

This is the minimum architecture that preserves the product's defining guarantees.

---

# 111. Component-Level ADRs

The following decisions require formal ADR records before implementation freeze:

### ADR-14-01
Agent vs workflow authority boundary.

### ADR-14-02
Policy enforcement location.

### ADR-14-03
Authorization re-check strategy.

### ADR-14-04
Execution-state ownership.

### ADR-14-05
Plan versioning and replanning.

### ADR-14-06
Retry semantics and idempotency.

### ADR-14-07
Checkpoint persistence.

### ADR-14-08
Sandbox implementation and failure semantics.

### ADR-14-09
Tool registry authority.

### ADR-14-10
Verification independence.

### ADR-14-11
Completion predicate implementation.

### ADR-14-12
Human approval semantics.

### ADR-14-13
Execution trace vs audit separation.

### ADR-14-14
Model/version consistency.

### ADR-14-15
Evidence access enforcement.

### ADR-14-16
Runtime resource scheduling.

---

# 112. Traceability

| Requirement | Component | Runtime mechanism | Interface | Test |
|---|---|---|---|---|
| Agent cannot self-authorize | Policy/Runtime | External policy | Policy API | Permission escalation |
| Unauthorized evidence blocked | Evidence | Authorization propagation | Evidence API | Cross-user/task |
| Tool calls controlled | Tool Runtime | Registry + policy | Tool Request | Unauthorized tool |
| Code sandboxed | Sandbox | Execution isolation | Sandbox API | Escape test |
| Verification separate | Verification | Independent verifier | Verification API | Verification failure |
| Completion deterministic | Workflow | Predicate engine | Completion API | Completion bypass |
| Provenance preserved | Provenance | Runtime event integration | Provenance API | Lineage reconstruction |
| Audit preserved | Audit | Mandatory event recording | Audit API | Audit suppression |
| Resource bounded | Resource Manager | Leases/budgets | Resource API | Resource exhaustion |
| Cancellation authoritative | Workflow | Runtime state transition | Control API | Cancellation bypass |
| OT prohibited | Policy/Tool Runtime | R5 rejection | Tool API | OT attempt |

---

# 113. Performance Architecture

Measure:

```text
Task Startup
Planning Latency
Evidence Latency
Model Latency
Tool Latency
Verification Latency
Queue Latency
End-to-End Workflow Latency
```

The optimization objective is:

> **Verified task completion per unit resource**, not minimum individual model latency.

The runtime must preserve:

- security;
- evidence quality;
- verification;
- provenance;

when optimizing performance.

---

# 114. Runtime Resource Scheduling

The resource manager controls:

```text
GPU
CPU
RAM
Storage
Model Residency
Sandbox Capacity
Task Queue
Tool Capacity
```

A resource request is a lease rather than an unconditional allocation.

Conceptually:

```text
Resource Request
 ↓
Admission Control
 ↓
Lease
 ↓
Execution
 ↓
Usage Measurement
 ↓
Release
```

---

# 115. GPU Interaction

The agent does not directly control GPU allocation.

Instead:

```text
Agent/Capability
 ↓
Resource Request
 ↓
Resource Manager
 ↓
Eligible Model
 ↓
Model Gateway
```

The runtime may select:

- another eligible model;
- lower-cost capability;
- queued execution;
- reduced context;

only if policy and correctness requirements remain satisfied.

---

# 116. Resource Starvation Defense

The runtime limits resource abuse from:

- repeated model calls;
- retrieval loops;
- tool loops;
- huge documents;
- repeated retries;
- sandbox jobs;
- oversized context.

A task cannot gain additional resources simply by creating additional steps.

---

# 117. Privacy / Data Minimization

The runtime passes the minimum necessary information to:

- model;
- agent;
- tool;
- verifier.

Preferred:

```text
Relevant Authorized Evidence
```

over:

```text
Entire Confidential Document
```

when the smaller representation is sufficient.

Execution traces themselves are classified and access-controlled.

---

# 118. Execution Trace Security

Trace data may contain:

- confidential evidence references;
- tool inputs;
- outputs;
- filenames;
- document locations;
- security context;
- resource information.

Therefore traces require:

- classification;
- access control;
- retention policy;
- minimization;
- masking where applicable;
- export restrictions.

---

# 119. Runtime Deployment

The MVP deployment remains:

```text
┌────────────────────────────────────────────┐
│ Controlled Workstation / Server            │
│                                            │
│  UI                                        │
│   │                                        │
│  API / Control Plane                       │
│   │                                        │
│  Workflow + Agent Runtime                  │
│   │       │        │                       │
│ Evidence  Model    Tool Runtime             │
│   │       │        │                       │
│ Local Stores  vLLM/llama.cpp   Sandbox     │
│                                            │
│  Host Network Enforcement                  │
│  Resource Control                          │
│  Audit / Provenance / Observability        │
└────────────────────────────────────────────┘
```

Distributed deployment is not required for MVP.

---

# 120. Final Agent Runtime Architecture

```text
                         ┌──────────────────┐
                         │       USER       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    IDENTITY      │
                         └────────┬─────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  SECURITY CONTEXT    │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │       POLICY         │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │        TASK          │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │     WORKFLOW         │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │       AGENT          │
                       │  proposes actions    │
                       └──────┬───┬───┬───────┘
                              │   │   │
                 ┌────────────┘   │   └────────────┐
                 ▼                ▼                ▼
          ┌────────────┐   ┌────────────┐   ┌────────────┐
          │  EVIDENCE  │   │   MODEL    │   │    TOOL    │
          └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
                │                │                │
                └────────────────┼────────────────┘
                                 ▼
                       ┌──────────────────────┐
                       │   POLICY RE-CHECK    │
                       └──────────┬───────────┘
                                  │
                          ┌───────┴───────┐
                          │               │
                         DENY            ALLOW
                          │               │
                          ▼               ▼
                       AUDIT          EXECUTION
                                          │
                                          ▼
                                      RESULT
                                          │
                                          ▼
                                    VERIFICATION
                                          │
                            ┌─────────────┼─────────────┐
                            ▼             ▼             ▼
                          PASS          FAIL       UNCERTAIN
                            │             │             │
                            │             ▼             ▼
                            │         CORRECT       ESCALATE
                            │             │             │
                            └─────────────┼─────────────┘
                                          ▼
                                    COMPLETION
                                          │
                                          ▼
                               PROVENANCE + AUDIT
```

---

# 121. Final Authority Model

## Human controls

- organizational authority;
- consequential approval;
- engineering acceptance;
- safety-sensitive decisions;
- formal approval;
- authorized intervention;
- cancellation;
- escalation resolution.

## System controls

- authentication;
- authorization;
- policy;
- workflow state;
- tool access;
- resource allocation;
- sandbox;
- network restrictions;
- verification gates;
- completion;
- audit;
- provenance;
- emergency stop.

## Agent controls

- interpretation;
- planning proposal;
- capability proposal;
- evidence request;
- tool request;
- model request;
- observation interpretation;
- correction proposal;
- replan proposal;
- escalation request;
- abstention;
- voluntary stop.

The fundamental relationship is:

```text
Agent proposes.
System authorizes.
Tools execute within boundaries.
Verifier evaluates.
Human retains consequential authority.
Runtime determines completion.
Provenance records why the result exists.
```

---

# 122. Final Execution Lifecycle

```text
Identity
→ Security Context
→ Policy
→ Task
→ Workflow
→ Capability
→ Agent
→ Evidence / Model / Tool
→ Tool Request
→ Policy Re-check
→ Authorization
→ Resource Check
→ Execution
→ Result
→ Verification
→ Continue / Correct / Replan / Escalate / Abstain / Stop
→ Artifact
→ Approval where required
→ Completion
→ Audit / Provenance
```

This is the authoritative runtime lifecycle.

---

# 123. Final Tool Architecture

```text
Tool Registry
      ↓
Capability Compatibility
      ↓
Agent Proposal
      ↓
Schema Validation
      ↓
Identity
      ↓
Policy
      ↓
Authorization
      ↓
Resource
      ↓
Sandbox / Network Boundary
      ↓
Tool Execution
      ↓
Result Validation
      ↓
Verification
      ↓
Audit
      ↓
Agent Observation
```

No tool may bypass this control chain.

---

# 124. Final State Model

The authoritative execution states are:

```text
CREATED
AUTHORIZED
PLANNING
READY
EXECUTING
WAITING
VERIFYING
REQUIRES_APPROVAL
ESCALATED
ABSTAINED
PARTIALLY_COMPLETED
COMPLETED_WITH_WARNINGS
COMPLETED
FAILED
BLOCKED
CANCELLED
ABORTED
```

State transitions are owned by the runtime/workflow system.

---

# 125. Final Failure / Recovery Model

```text
Failure
 ↓
Classification
 ↓
Security Impact?
 ├── YES → Contain / Abort / Audit
 └── NO
      ↓
Recoverable?
 ├── NO → Escalate / Abstain / Fail
 └── YES
      ↓
Bounded Retry?
 ├── YES → Retry
 └── NO → Replan / Alternate / Escalate
```

No blind retry.

No policy retry.

No authorization retry.

No infinite correction.

---

# 126. Final Verification Model

Verification is:

```text
Independent Runtime Stage
```

and can produce:

```text
PASS
FAIL
UNCERTAIN
NEEDS_REVIEW
INSUFFICIENT
```

Verification controls continuation.

A model's confidence cannot produce `PASS` by itself.

---

# 127. Final Completion Model

A task is `COMPLETED` only when its workflow-specific completion predicate is satisfied.

At minimum:

```text
Required Evidence
+
Required Steps
+
Required Verification
+
Required Authorization
+
Required Provenance
+
Required Artifact
```

where applicable.

The agent cannot declare completion.

---

# 128. Final Security Boundaries

The following boundaries cannot be bypassed:

1. Identity → Authorization
2. Authorization → Evidence
3. Agent → Tool
4. Agent → Model
5. Tool → Sandbox
6. Tool → Network
7. Execution → Verification
8. Artifact → Release
9. Execution → Audit
10. Execution → Provenance
11. Agent → OT
12. Agent → Host filesystem
13. Agent → Host credentials
14. Untrusted data → Control plane

---

# 129. Final MVP Runtime

The minimum runtime required is:

## W3

- task manager;
- policy;
- workflow;
- bounded agent;
- evidence manager;
- retrieval;
- model gateway;
- verification;
- provenance;
- audit.

## W1

Everything in W3 plus:

- document intelligence;
- OCR;
- structured evidence comparison;
- report-specific verification.

## W2

Everything in W1 plus:

- multimodal processing;
- engineering drawing processor;
- spatial representation;
- topology representation;
- structural verification.

## W4

Everything above plus:

- artifact generator;
- artifact verification;
- approval gate;
- controlled release.

## W5 — Conditional

Everything above plus:

- code generation;
- code validation;
- sandbox;
- resource controls;
- execution testing;
- numerical/semantic verification.

---

# 130. Open Questions

Only genuinely unresolved runtime questions remain:

### OQ-RT-01
Exact policy language / policy-engine implementation.

### OQ-RT-02
Exact authorization granularity inherited from customer deployment.

### OQ-RT-03
Exact retry and correction thresholds.

### OQ-RT-04
Exact timeout values.

### OQ-RT-05
Exact resource-budget algorithm.

### OQ-RT-06
Exact checkpoint persistence mechanism.

### OQ-RT-07
Firecracker versus gVisor deployment profile for individual execution classes.

### OQ-RT-08
Exact human approval workflow and authority mapping.

### OQ-RT-09
Exact verification implementation per MVP workflow.

### OQ-RT-10
Exact model fallback rules after Phase 11 hardware qualification.

### OQ-RT-11
Exact replay requirements.

### OQ-RT-12
Exact dry-run support for future consequential tools.

### OQ-RT-13
Exact execution-trace retention policy.

### OQ-RT-14
Exact resource fairness policy across concurrent users/tasks.

### OQ-RT-15
Exact event persistence/transaction mechanism.

None of these reopen the core runtime architecture.

---

# 131. Material Risks

## R-RT-01 — Agent manipulation

An agent may intentionally or accidentally propose prohibited actions.

**Control:** External policy and authorization.

## R-RT-02 — Tool semantic failure

A tool may execute successfully while producing an incorrect result.

**Control:** Independent validation/verification.

## R-RT-03 — State corruption

Concurrent or stale updates may corrupt execution state.

**Control:** Single authoritative state owner, versioning, transactional transitions.

## R-RT-04 — Retry amplification

Failures may cause resource exhaustion.

**Control:** bounded, classified retry budgets.

## R-RT-05 — Security-context staleness

Permissions may change during execution.

**Control:** security-context versioning and re-check.

## R-RT-06 — Verification weakness

A weak verifier may accept incorrect output.

**Control:** independent verification methods and workflow-specific qualification.

## R-RT-07 — Sandbox failure

Generated code may exploit runtime weaknesses.

**Control:** independent sandbox/network/resource enforcement and adversarial testing.

## R-RT-08 — Resource starvation

One task may monopolize local hardware.

**Control:** admission control, leases, fairness, backpressure.

## R-RT-09 — Provenance loss

Runtime events may not map cleanly to Phase 13 lineage.

**Control:** provenance integration at action execution time.

## R-RT-10 — Excessive runtime complexity

Over-engineering could undermine the single-node MVP.

**Control:** single-agent, single-node baseline and explicit simplification review.

---

# 132. ADRs Required Before Implementation Freeze

The following must be formalized:

```text
ADR-14-01  Agent / Workflow Authority
ADR-14-02  Policy Enforcement
ADR-14-03  Authorization Re-check
ADR-14-04  State Ownership
ADR-14-05  Plan Versioning
ADR-14-06  Retry / Idempotency
ADR-14-07  Checkpointing
ADR-14-08  Sandbox Boundary
ADR-14-09  Tool Registry
ADR-14-10  Verification Independence
ADR-14-11  Completion Predicate Engine
ADR-14-12  Human Approval
ADR-14-13  Trace / Audit Separation
ADR-14-14  Model / Tool Version Consistency
ADR-14-15  Evidence Access
ADR-14-16  Resource Scheduling
```

---

# 133. Implementation Order

The implementation sequence should be:

```text
1. Identity + Security Context
        ↓
2. Policy Enforcement
        ↓
3. Task + Execution State
        ↓
4. Workflow State Machine
        ↓
5. Capability Registry
        ↓
6. Tool Registry
        ↓
7. Evidence Access Interface
        ↓
8. Agent Runtime
        ↓
9. Model Invocation
        ↓
10. Tool Execution Boundary
        ↓
11. Sandbox
        ↓
12. Verification
        ↓
13. Completion Predicate Engine
        ↓
14. Artifact Release
        ↓
15. Provenance Integration
        ↓
16. Audit / Observability
        ↓
17. Recovery / Checkpointing
        ↓
18. Resource Scheduling
        ↓
19. End-to-End Workflow Qualification
```

Security boundaries are implemented before broad agent autonomy.

---

# 134. Implementation Readiness

## Classification

# **READY WITH CONDITIONS**

The runtime architecture is sufficiently defined to begin detailed implementation design.

The architecture has established:

- agent authority boundaries;
- workflow authority;
- task/execution distinction;
- plan semantics;
- bounded replanning;
- capability abstraction;
- tool registry;
- tool contracts;
- policy enforcement points;
- authorization re-check;
- evidence access;
- prompt-injection containment;
- state ownership;
- persistence;
- checkpointing;
- cancellation;
- retry semantics;
- idempotency;
- failure classification;
- recovery;
- resource control;
- concurrency;
- sandbox contract;
- verification;
- correction;
- escalation;
- human approval;
- abstention;
- completion predicates;
- artifact release;
- execution tracing;
- provenance integration;
- security boundaries;
- MVP workflow mapping;
- testing architecture.

The remaining conditions are primarily qualification and implementation decisions rather than architectural uncertainty.

---

# 135. Required Validation Before Runtime Freeze

The following technical spikes are mandatory:

```text
V-RT-01 Agent manipulation / authorization bypass
V-RT-02 Tool contract and policy enforcement
V-RT-03 Evidence access isolation
V-RT-04 State persistence / crash recovery
V-RT-05 Retry / idempotency behavior
V-RT-06 Sandbox escape resistance
V-RT-07 Resource exhaustion
V-RT-08 Verification effectiveness
V-RT-09 Completion bypass resistance
V-RT-10 Cancellation / revocation handling
V-RT-11 Full W3 execution
V-RT-12 Full W1 execution
V-RT-13 Full W2 execution
V-RT-14 Full W4 execution
V-RT-15 Conditional W5 execution
V-RT-16 End-to-end hardware/resource qualification
```

Quantitative thresholds remain:

> **Requires Validation**

where not previously established.

---

# 136. Final Quality Gate

## Agent

- Planning defined: **YES**
- Agent state defined: **YES**
- Memory boundaries defined: **YES**
- Authority explicitly limited: **YES**
- Replanning bounded: **YES**
- Self-permission prohibited: **YES**

## Policy

- Enforcement points explicit: **YES**
- Tool re-check: **YES**
- Authorization external: **YES**
- Failure behavior: **YES**

## Tools

- Registry: **YES**
- Contracts: **YES**
- Permissions: **YES**
- Result validation: **YES**
- Observable execution: **YES**
- Side-effect classification: **YES**

## Execution

- Task state: **YES**
- Workflow state: **YES**
- Step state: **YES**
- Ownership: **YES**
- Checkpointing: **YES**
- Pause/resume: **YES**
- Cancellation: **YES**
- Recovery: **YES**

## Security

- Security-context propagation: **YES**
- Prompt injection: **YES**
- Tool-output injection: **YES**
- Sandbox requirement: **YES**
- Network policy: **YES**
- Secret boundary: **YES**
- OT prohibition: **YES**

## Verification

- Separate from generation: **YES**
- Runtime-affecting: **YES**
- Failure behavior: **YES**
- Correction bound: **YES**
- Human review: **YES**

## Completion

- Predicates explicit: **YES**
- LLM done non-authoritative: **YES**
- Abstention: **YES**
- Escalation: **YES**
- Emergency stop: **YES**
- Artifact release control: **YES**

## Reliability

- Bounded retry: **YES**
- Failure classes: **YES**
- Recovery: **YES**
- Timeout model: **YES**
- Infinite-loop prevention: **YES**
- Resource exhaustion: **YES**
- Deadlock prevention: **YES**

## Observability

- Execution trace: **YES**
- Critical events auditable: **YES**
- Provenance integrated: **YES**
- Correlation identifiers: **YES**
- Sensitive trace protection: **YES**

## Testing

- Unit: **YES**
- Contract: **YES**
- Integration: **YES**
- Security: **YES**
- Adversarial: **YES**
- Failure: **YES**
- End-to-end: **YES**

---

# A. Final Agent Runtime Architecture

The Workbench uses a **single bounded agent runtime subordinate to deterministic workflow, policy, authorization, evidence, tool, resource, verification, and human-approval mechanisms**.

The agent is a reasoning/proposal engine.

It is not:

- an authorization engine;
- a policy engine;
- a database authority;
- a host execution authority;
- a sandbox authority;
- a verification authority;
- a human authority.

---

# B. Final Authority Model

```text
                    HUMAN
                      │
          Consequential Authority
                      │
                      ▼
                  SYSTEM
       ┌──────────────┼──────────────┐
       │              │              │
    POLICY      AUTHORIZATION    WORKFLOW
       │              │              │
       └──────────────┼──────────────┘
                      │
                      ▼
                    AGENT
                      │
                Proposes Actions
                      │
                      ▼
               CONTROLLED TOOLS
                      │
                      ▼
                  VERIFIER
                      │
                      ▼
                 SYSTEM RESULT
```

Authority never flows upward from the agent.

---

# C. Final Execution Lifecycle

```text
Identity
→ Security Context
→ Policy
→ Task
→ Capability
→ Agent
→ Tool Request
→ Policy Re-check
→ Execution
→ Result
→ Verification
→ Continue / Correct / Escalate / Abstain / Stop
→ Completion
```

With the necessary control-plane stages:

```text
Identity
→ Security Context
→ Policy
→ Task
→ Workflow
→ Capability
→ Agent
→ Evidence / Model / Tool
→ Policy Re-check
→ Authorization
→ Resource Check
→ Execution
→ Result
→ Verification
→ Correction / Replan / Escalation
→ Artifact / Approval
→ Completion
→ Provenance / Audit
```

---

# D. Final Tool Architecture

Tools are:

```text
Registered
→ Versioned
→ Capability-bound
→ Permission-bound
→ Policy-checked
→ Resource-bounded
→ Sandbox/network-controlled
→ Executed
→ Validated
→ Verified
→ Audited
```

The agent never obtains arbitrary host functionality.

---

# E. Final State Model

The authoritative runtime state model is:

```text
CREATED
→ AUTHORIZED
→ PLANNING
→ READY
→ EXECUTING
→ WAITING / VERIFYING
→ COMPLETED
```

with explicit branches:

```text
FAILED
CANCELLED
ABORTED
BLOCKED
ESCALATED
ABSTAINED
REQUIRES_APPROVAL
PARTIALLY_COMPLETED
COMPLETED_WITH_WARNINGS
```

---

# F. Final Failure / Recovery Model

Failure is:

```text
Detected
→ Classified
→ Security Assessed
→ Recovery Eligibility Determined
→ Retry / Alternate / Replan / Escalate / Abstain / Stop
```

Recovery never bypasses policy or authorization.

---

# G. Final Verification Model

Verification is a first-class execution stage.

```text
Output
→ Validation
→ Verification
→ Runtime Decision
```

Only the verification result can move an execution across the applicable verification gate.

---

# H. Final Completion Model

The system declares completion only after its workflow-specific predicates are satisfied.

```text
Evidence
+
Execution
+
Verification
+
Authorization
+
Provenance
+
Artifact
+
Approval where required
=
COMPLETION
```

The LLM's declaration of completion has no authoritative status.

---

# I. Final Security Boundaries

The non-bypassable boundaries are:

```text
Identity
→ Authorization
→ Policy
→ Agent
→ Capability
→ Tool
→ Sandbox
→ Network
```

and:

```text
Execution
→ Verification
→ Approval
→ Release
```

and:

```text
Execution
→ Provenance
→ Audit
```

Untrusted content cannot cross from:

```text
DATA
```

into:

```text
AUTHORITY
```

without an independent trusted control-plane decision.

---

# J. Final MVP Runtime

The MVP consists of:

```text
Identity / Authorization
Policy
Task Manager
Workflow Engine
Execution State
Capability Registry
Model Router
Inference Gateway
Bounded Agent Runtime
Evidence Manager
Retrieval
Tool Registry
Tool Runtime
Sandbox
Verification
Artifact Generator
Provenance
Audit / Observability
Resource Manager
```

with:

```text
Single Node
+
Local Models
+
Local Knowledge
+
Controlled Tools
+
Independent Network Enforcement
```

W3, W1, W2 and W4 are core.

W5 remains conditional upon sandbox and execution qualification.

---

# K. Open Questions

Only implementation/customer qualification questions remain:

- policy implementation;
- authorization granularity;
- retry thresholds;
- timeout values;
- resource scheduling;
- checkpoint persistence;
- sandbox profile;
- approval workflow;
- verification implementations;
- model fallback;
- replay;
- trace retention.

The core runtime authority model is closed.

---

# L. Risks

Material risks:

1. Agent manipulation.
2. Tool semantic correctness.
3. Verification weakness.
4. State corruption.
5. Retry/resource amplification.
6. Security-context staleness.
7. Sandbox compromise.
8. Runtime complexity.
9. Provenance loss.
10. Hardware/resource contention.

---

# M. ADRs Required

```text
ADR-14-01 Agent / Workflow Authority
ADR-14-02 Policy Enforcement
ADR-14-03 Authorization Re-check
ADR-14-04 Execution State Ownership
ADR-14-05 Plan Versioning
ADR-14-06 Retry / Idempotency
ADR-14-07 Checkpointing
ADR-14-08 Sandbox Boundary
ADR-14-09 Tool Registry
ADR-14-10 Verification Independence
ADR-14-11 Completion Predicate Engine
ADR-14-12 Human Approval
ADR-14-13 Trace / Audit Separation
ADR-14-14 Model / Tool Version Consistency
ADR-14-15 Evidence Access
ADR-14-16 Resource Scheduling
```

---

# N. Implementation Readiness

## **READY WITH CONDITIONS**

Phase 14 establishes an implementation-grade runtime architecture.

The central architectural contract is now fixed:

> **The Workbench is not an autonomous agent with attached tools. It is a controlled execution system containing an AI agent whose proposals are continuously constrained by external authority, policy, authorization, evidence, capability, resource, tool, sandbox, verification, provenance, audit, and human-approval mechanisms.**

The next phase should therefore move into **detailed interface/API/contract design and implementation specifications**, not reopen the fundamental agent authority architecture.

# PHASE 14 SUCCESS CONDITION

> **The Workbench now has a formally defined agent execution model, explicit workflow and execution state, bounded planning and replanning, governed capability selection, explicit tool contracts, external policy and authorization enforcement, controlled tool execution, sandbox integration, bounded retries, recovery, escalation, abstention, stopping, human approval, deterministic completion predicates, verification-driven control, execution tracing, provenance integration, resource governance, and non-bypassable security boundaries sufficient to implement the runtime without making the AI agent an implicit authority mechanism.**

**Phase 14 status: COMPLETE — READY WITH CONDITIONS FOR DETAILED RUNTIME/API IMPLEMENTATION DESIGN.**