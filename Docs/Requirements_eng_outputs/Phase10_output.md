# SOVEREIGN AGENTIC AI WORKBENCH

# SYSTEM ARCHITECTURE

**Phase:** 10  
**Predecessor:** Phase 9 — System Requirements Specification  
**Successor:** Phase 11 — Architecture Decision & Technology Selection  
**Architecture Status:** **ARCHITECTURE READY WITH TARGETED VALIDATION**  
**Product Category:** Sovereign Enterprise AI Workbench / Agentic Knowledge-Work Execution Environment

---

# 1. Document Control

| Field | Decision |
|---|---|
| Product | Sovereign Agentic AI Workbench |
| Architecture phase | Phase 10 |
| Architectural objective | Define how the SRS is structurally satisfied |
| MVP workflows | W3, W1, W2, W4 |
| Conditional workflow | W5 |
| Primary user | Technical engineer / engineering knowledge worker |
| Deployment constraint | Single workstation/server |
| Resource constraint | Mid-range GPU target; exact envelope requires validation |
| Sovereignty principle | No unauthorized external processing or egress |
| Architecture method | Alternatives → elimination → baseline |
| Technology selection | Deferred to Phase 11 |
| Status | Architecture Ready With Targeted Validation |

The Phase-9 SRS establishes the system as an execution environment rather than a chatbot or generic RAG system, with sovereignty, external authority, evidence governance, bounded agency, verification, provenance and resource constraints as architectural drivers.

---

# 2. Architecture Objective

The architecture shall answer:

> **How should the Sovereign Agentic AI Workbench be structurally organized so that its requirements can actually be implemented, secured, verified, operated and demonstrated?**

The architecture must establish:

- architectural boundaries;
- major domains;
- responsibilities;
- interfaces;
- data and control flows;
- trust zones;
- authority boundaries;
- state ownership;
- failure domains;
- resource boundaries;
- verification boundaries;
- deployment structure.

It shall not prematurely select:

- LLMs;
- VLMs;
- inference engines;
- agent frameworks;
- databases;
- OCR engines;
- sandbox technologies;
- orchestration platforms.

Those are Phase-11 decisions.

---

# 3. Architecture Scope

The architecture covers the system required for:

1. task intake;
2. task understanding;
3. evidence determination;
4. authorization;
5. governed knowledge access;
6. document and multimodal processing;
7. P&ID/drawing analysis;
8. local AI capability execution;
9. bounded agentic execution;
10. controlled tools;
11. restricted code execution;
12. verification;
13. artifact generation;
14. provenance;
15. audit;
16. observability;
17. sovereignty enforcement;
18. resource management;
19. configuration;
20. operations and recovery.

The architecture does **not** include autonomous OT/ICS control, unrestricted enterprise automation, unrestricted external communication or unrestricted autonomous organizational decisions.

---

# 4. Source Requirements

Architectural authority is ordered:

1. Final PRD
2. Final SRS
3. Product decisions
4. Research conclusions
5. Existing architectural findings
6. Validated technical evidence

The Phase-9 SRS explicitly identifies twelve architecture-driving requirements:

- sovereignty;
- multiple local AI capabilities;
- evidence-first knowledge;
- bounded agent execution;
- controlled tools;
- untrusted code isolation;
- verification;
- provenance;
- multimodal/P&ID processing;
- single-system resource constraints;
- auditability;
- offline lifecycle.

The SRS also explicitly leaves technology and deployment choices open.

---

# 5. Architectural Principles

## AP-01 — Sovereignty First

Confidential processing is local by default. External communication is denied unless explicitly permitted by deployment policy outside the sovereign core.

## AP-02 — Security by Architecture

Security-critical controls shall exist outside model compliance.

## AP-03 — Model Agnosticism

No architectural function shall fundamentally depend upon one model.

## AP-04 — Capability Abstraction

Models implement capabilities; they do not define the system's architecture.

## AP-05 — Evidence First

Evidence is a first-class architectural object rather than an incidental retrieval result.

## AP-06 — Bounded Agency

Agent reasoning proposes and executes within authority granted externally.

## AP-07 — Least Privilege

Permissions are scoped by identity, task, data, capability, tool and action.

## AP-08 — Verification Before Acceptance

Generation and completion are separate from verification.

## AP-09 — Provenance by Design

Important outputs retain source-to-output lineage.

## AP-10 — Failure Containment

A component failure must not automatically become a system-wide failure.

## AP-11 — Observability

Material system behavior must be reconstructable.

## AP-12 — Resource Awareness

GPU, CPU, RAM, storage and concurrency are architectural resources.

## AP-13 — Extensibility

New compatible capabilities can be introduced without redesigning the product.

## AP-14 — Human Consequential Authority

The architecture cannot silently convert AI output into organizational authority.

---

# 6. Architectural Drivers

The architecture drivers are ranked as follows:

| Rank | Driver | Architectural importance |
|---:|---|---|
| 1 | Sovereignty | Dominant |
| 2 | Security/isolation | Dominant |
| 3 | External authority and least privilege | Dominant |
| 4 | Evidence integrity and authorization | Dominant |
| 5 | Verification | Dominant |
| 6 | Bounded agent execution | High |
| 7 | Multimodal/P&ID processing | High |
| 8 | Local multi-model capability | High |
| 9 | Single-system resource constraint | High |
| 10 | Provenance | High |
| 11 | Auditability | High |
| 12 | Reliability/failure containment | High |
| 13 | Extensibility | Medium |
| 14 | Future horizontal scalability | Lower for MVP |

This ranking intentionally differs from conventional enterprise-AI architecture priorities. Horizontal scalability and framework ecosystem are subordinate to sovereignty, authority, evidence and verification.

---

# 7. System Context

```text
                         HUMAN USERS
                              |
                              v
                    +-------------------+
                    |   WORKBENCH UI    |
                    +---------+---------+
                              |
                              v
              +-------------------------------+
              |     CONTROL / AUTHORITY       |
              | Task | Policy | Identity      |
              | State | Approval | Resources  |
              +---------------+---------------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
 +----------------+  +----------------+  +----------------+
 | KNOWLEDGE /    |  | LOCAL AI       |  | AGENT         |
 | EVIDENCE       |  | CAPABILITIES   |  | EXECUTION     |
 +-------+--------+  +----------------+  +-------+--------+
         |                                      |
         +------------------+-------------------+
                            |
                            v
                 +----------------------+
                 | CONTROLLED EXECUTION |
                 | Tools / Code / Data  |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |    VERIFICATION      |
                 +----------+-----------+
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          +-------------+       +-------------+
          | ARTIFACTS   |       | PROVENANCE  |
          +-------------+       +-------------+
                 |                     |
                 +----------+----------+
                            v
                       +---------+
                       |  AUDIT  |
                       +---------+

             X  UNAUTHORIZED EXTERNAL NETWORK  X
```

---

# 8. System Boundary

The sovereign system boundary contains:

- user/task control;
- policy;
- authorization;
- agent runtime;
- AI capabilities;
- knowledge/evidence;
- document processing;
- tools;
- code execution;
- verification;
- artifacts;
- provenance;
- audit;
- resource management;
- configuration.

The following are outside the sovereign software boundary:

- human consequential authority;
- physical site security;
- external organizational identity infrastructure where integrated;
- physical network infrastructure;
- underlying host hardware.

However, the architecture must impose enforceable requirements on these external dependencies.

---

# 9. External Entities

| Entity | Relationship |
|---|---|
| Human user | Creates and reviews tasks |
| Domain expert | Performs technical validation |
| Approver | Provides formal approval |
| Administrator | Controls configuration |
| Security administrator | Controls security policy/evidence |
| Operator | Controls deployment/recovery |
| Identity provider | Optional identity assertion |
| Enterprise knowledge source | Provides controlled information |
| File/data source | Provides task data |
| External network | Untrusted/unavailable by default |
| Physical infrastructure | Hosts the sovereign deployment |

---

# 10. Architectural Domains

The 27 SRS domains are consolidated into the following architectural domains.

## A. Interaction Domain

Owns:

- task submission;
- file submission;
- result presentation;
- evidence inspection;
- approval;
- failure communication.

It does not own authorization or task completion truth.

## B. Control and Authority Domain

Owns:

- task identity;
- lifecycle state;
- policy;
- authorization;
- approvals;
- workflow transitions;
- completion predicates;
- capability permissions.

This is the **authoritative control plane**.

## C. Intelligence Domain

Owns:

- capability registry;
- model selection;
- local model execution;
- multimodal capability invocation;
- model lifecycle.

It cannot grant itself authority.

## D. Knowledge and Evidence Domain

Owns:

- source representation;
- document representations;
- metadata;
- evidence;
- authority;
- revision;
- temporal validity;
- authorization-aware retrieval;
- evidence sufficiency;
- provenance relationships.

## E. Agent Execution Domain

Owns:

- planning;
- decomposition;
- step selection;
- bounded execution;
- correction;
- escalation;
- stopping.

It proposes actions but cannot independently authorize them.

## F. Controlled Execution Domain

Owns:

- governed tools;
- code execution;
- sandbox boundaries;
- execution receipts;
- tool results.

## G. Verification Domain

Owns:

- deterministic checks;
- evidence checks;
- semantic checks;
- numerical checks;
- policy checks;
- human-review gates.

## H. Output Integrity Domain

Owns:

- artifact specification;
- artifact generation;
- artifact validation;
- provenance attachment;
- release state.

## I. Assurance Domain

Owns:

- provenance;
- audit;
- observability;
- security evidence;
- sovereignty evidence.

## J. Infrastructure Control Domain

Owns:

- resource management;
- storage;
- configuration;
- deployment;
- lifecycle;
- recovery;
- network enforcement.

---

# 11. Architectural Layers

The architecture adopts **logical layers**, but avoids unnecessary physical service decomposition.

```text
L1  Interaction
 |
L2  Control / Authority
 |
L3  Agent / Workflow
 |
L4  Intelligence / Capability
 |
L5  Knowledge / Evidence
 |
L6  Controlled Execution
 |
L7  Verification
 |
L8  Artifact / Output
 |
L9  Provenance / Audit
 |
L10 Security / Infrastructure
```

These are **logical boundaries**, not mandatory processes or containers.

The key architectural rule is:

> Logical modularity is mandatory; physical distribution is conditional.

This distinction is important for the single-node MVP.

---

# 12. Control Plane / Data Plane

## 12.1 Control Plane

The control plane owns:

- identity;
- task state;
- policy;
- authorization;
- workflow state;
- capability registry;
- tool registry;
- resource admission;
- verification state;
- approval;
- release;
- audit-event creation.

## 12.2 Data Plane

The data plane carries:

- documents;
- images;
- OCR;
- extracted text;
- evidence;
- embeddings;
- structured representations;
- model inputs/outputs;
- tool results;
- code;
- sandbox data;
- artifacts.

## Decision

**Strong separation is architecturally necessary.**

The reason is not performance. It is authority containment.

Untrusted content and model outputs belong to the data/intelligence side. Authority belongs to the control side.

Therefore:

```text
DATA / MODEL OUTPUT
        |
        v
CONTROLLED INTERPRETATION
        |
        v
POLICY + AUTHORIZATION
        |
        v
AUTHORITATIVE ACTION
```

rather than:

```text
MODEL
 |
 +--> permission
 +--> tool
 +--> policy
```

---

# 13. Trust Zones

| Zone | Trust | Primary contents | Key rule |
|---|---|---|---|
| Z1 | Human-controlled | User interaction | Authentication/authorization |
| Z2 | High-control | Policy/task/authority | AI cannot modify |
| Z3 | Controlled AI | Models/capabilities | Model output is untrusted |
| Z4 | Confidential data | Sources/evidence | Authorization required |
| Z5 | Restricted execution | Tools | Explicit contracts |
| Z6 | Untrusted execution | Generated code | Independent isolation |
| Z7 | Infrastructure | Host/resources | Protected from application |
| Z8 | External | Network | Denied by default |

The strongest boundary is between **Z2 control** and **Z3/Z4/Z5/Z6 untrusted or conditionally trusted processing**.

---

# 14. Security Boundaries

The architecture preserves these boundaries:

```text
User -> Control
Control -> Data
Data -> AI
AI -> Agent
Agent -> Control
Agent -> Tool
Agent -> Code
Code -> Sandbox
Sandbox -> Host
System -> Network
Supply Chain -> System
```

No boundary is trusted merely because both endpoints are local.

---

# 15. System Control Flow

```text
RECEIVE
  |
VALIDATE
  |
CLASSIFY
  |
IDENTIFY REQUIREMENTS
  |
IDENTIFY EVIDENCE
  |
IDENTIFY CAPABILITIES
  |
CREATE PLAN
  |
AUTHORIZATION
  |
RESOURCE ADMISSION
  |
EXECUTE
  |
INSPECT
  |
VERIFY
  |
+--------+---------+---------+
|        |         |         |
PASS   CORRECT   ESCALATE  ABSTAIN
|        |         |         |
v        +---->----+         |
COMPLETE                    STOP
```

The authoritative state machine exists outside model context.

---

# 16. System Data Flow

## Evidence flow

```text
SOURCE
  |
INGEST
  |
VALIDATE
  |
PROCESS
  |
STRUCTURE
  |
EVIDENCE
  |
AUTHORIZE
  |
RETRIEVE
  |
ASSEMBLE CONTEXT
  |
REASON
  |
CLAIM
  |
VERIFY
  |
ARTIFACT
```

## Model flow

```text
Task Requirement
       |
Capability Requirement
       |
Capability Registry
       |
Candidate Capability
       |
Resource Admission
       |
Local Inference
       |
Output
       |
Verification
```

## Tool flow

```text
Agent Proposal
      |
Tool Contract
      |
Authorization
      |
Policy
      |
Resource Admission
      |
Execution
      |
Result
      |
Verification
      |
Audit
```

---

# 17. Task Orchestration Architecture

The **Task Control Domain** owns the authoritative lifecycle.

| State | Owner |
|---|---|
| RECEIVED | Task Control |
| VALIDATING | Task Control |
| UNDERSTANDING | Task + Intelligence |
| REQUIREMENTS_IDENTIFIED | Task Control |
| EVIDENCE_REQUIRED | Task Control |
| RETRIEVING | Knowledge |
| EVIDENCE_ASSESSED | Evidence |
| PLANNING | Agent |
| AUTHORIZED | Policy/Authority |
| EXECUTING | Execution |
| VERIFYING | Verification |
| CORRECTING | Agent + Control |
| COMPLETED | Task Control |
| ABSTAINED | Task Control |
| FAILED | Task Control |
| SECURITY_VIOLATION | Security/Control |

The agent can recommend transitions. It cannot unilaterally commit authoritative state transitions.

---

# 18. Agent Runtime Architecture

The agent is architecturally a **bounded planner/executor**, not the system controller.

It may:

- decompose tasks;
- propose plans;
- request evidence;
- request capabilities;
- request tools;
- inspect intermediate results;
- request correction;
- request escalation;
- request verification;
- stop.

It may not:

- alter policy;
- grant permissions;
- bypass authorization;
- modify its own sandbox;
- declare formal approval;
- bypass verification;
- disable audit;
- establish sovereignty;
- authorize consequential actions.

### Agent authority

```text
Agent
  |
  | proposal/request
  v
Control Plane
  |
  +--> Authorization
  +--> Policy
  +--> Resource Admission
  +--> Verification
  |
  v
Execution
```

---

# 19. Agent State Architecture

Important state shall persist outside model context.

Authoritative state includes:

- task state;
- workflow state;
- plan identity;
- step identity;
- execution state;
- evidence state;
- authorization state;
- tool state;
- verification state;
- artifact state;
- failure state;
- approval state.

Model context is treated as **working memory**, not authoritative state.

---

# 20. Model / Capability Architecture

The architecture introduces a capability abstraction:

```text
                 CAPABILITY REGISTRY
                        |
          +-------------+-------------+
          |             |             |
       Candidate      Candidate     Candidate
        Model A        Model B       Model C
          |             |             |
          +-------------+-------------+
                        |
                 Selection / Admission
                        |
                     Execution
```

Capabilities may include:

- language reasoning;
- vision-language reasoning;
- OCR;
- layout extraction;
- document understanding;
- embeddings;
- reranking;
- structured extraction;
- code generation;
- code analysis;
- numerical reasoning.

The system records capability and implementation identity without making the implementation the architectural identity.

---

# 21. Model Routing Architecture

Routing is a **constraint-solving/admission function**, not simply a model-ranking function.

Inputs:

- task;
- workflow;
- required capability;
- modality;
- evidence requirements;
- quality requirement;
- verification requirement;
- model availability;
- model version;
- resource cost;
- context requirement;
- latency;
- security policy.

Conceptually:

```text
TASK
 |
CAPABILITY REQUIREMENT
 |
CANDIDATE SET
 |
POLICY FILTER
 |
RESOURCE FILTER
 |
QUALITY / VERIFICATION REQUIREMENT
 |
ROUTING DECISION
 |
LOCAL EXECUTION
 |
VERIFY
 |
+---- PASS
|
+---- ESCALATE
```

This supports adaptive escalation while preventing the router from treating the largest model as automatically optimal.

---

# 22. Knowledge Architecture

The knowledge architecture is deliberately **not a vector database architecture**.

```text
ENTERPRISE SOURCES
        |
        v
SOURCE VAULT
        |
        v
DOCUMENT REPRESENTATIONS
        |
        +--> TEXT
        +--> LAYOUT
        +--> TABLES
        +--> IMAGES
        +--> STRUCTURES
        +--> P&ID REPRESENTATIONS
        |
        v
EVIDENCE OBJECTS
        |
        +--> AUTHORITY
        +--> REVISION
        +--> TEMPORALITY
        +--> AUTHORIZATION
        +--> PROVENANCE
        |
        v
RETRIEVAL PROJECTIONS
        |
        +--> LEXICAL
        +--> SEMANTIC
        +--> VISUAL
        +--> STRUCTURAL
        |
        v
EVIDENCE ASSEMBLY
```

Indexes are projections of governed evidence rather than the authoritative knowledge layer.

---

# 23. Evidence Architecture

Evidence is a first-class object.

Minimum conceptual identity:

```text
Evidence
 ├─ source_id
 ├─ source_revision
 ├─ source_location
 ├─ authority
 ├─ authorization
 ├─ temporal_validity
 ├─ extraction_context
 ├─ provenance
 ├─ verification_state
 └─ conflict_state
```

Evidence states:

- SUFFICIENT
- INSUFFICIENT
- CONFLICTED
- STALE
- UNAUTHORIZED
- UNVERIFIABLE

### Critical architectural decision

Authorization must occur **before evidence becomes available to reasoning**, wherever practical.

The architecture therefore rejects:

```text
retrieve everything
       |
       v
filter later
```

as the default pattern.

Preferred:

```text
Identity
 +
Task
 +
Authorization
 +
Query
       |
       v
Authorized Retrieval
       |
       v
Evidence
```

This directly addresses the SRS requirement that semantic relevance cannot substitute for authorization.

---

# 24. Document Intelligence Architecture

```text
INPUT
 |
FILE VALIDATION
 |
FORMAT DETECTION
 |
PARSING
 |
+--------+---------+
|        |         |
OCR    LAYOUT    NATIVE STRUCTURE
|        |         |
+--------+---------+
 |
TABLE / IMAGE / STRUCTURE EXTRACTION
 |
SEMANTIC EXTRACTION
 |
STRUCTURED REPRESENTATION
 |
EVIDENCE
```

Native digital documents and scans share the evidence layer but may follow different processing paths.

Every transformation preserves source linkage.

---

# 25. Multimodal Architecture

Multimodal processing is decomposed into capabilities:

```text
DOCUMENT / IMAGE / DRAWING
          |
   +------+------+
   |             |
 Visual       Text/OCR
   |             |
   +------+------+
          |
        Layout
          |
   Multimodal Representation
          |
       Reasoning
          |
      Verification
```

The architecture deliberately avoids a universal "vision model does everything" dependency.

---

# 26. P&ID / Engineering Drawing Architecture

The P&ID path is:

```text
DRAWING
  |
IMAGE PROCESSING
  |
OCR / TEXT
  |
SYMBOL / ENTITY DETECTION
  |
SPATIAL RELATIONSHIPS
  |
CONNECTIVITY / TOPOLOGY
  |
ENGINEERING REPRESENTATION
  |
DOMAIN INTERPRETATION
  |
ANALYSIS
  |
VERIFICATION
  |
HUMAN ENGINEERING AUTHORITY
```

The architecture maintains separate representations for:

1. visual observation;
2. extracted entities;
3. spatial relationships;
4. structural connectivity;
5. engineering interpretation;
6. consequential conclusions.

A visual model is therefore not the authoritative P&ID representation.

---

# 27. Tool Architecture

Every tool has a governed contract:

```text
Tool Registry
     |
Tool Identity
     |
Capability
     |
Input Contract
     |
Permission Requirements
     |
Policy
     |
Authorization
     |
Resource Boundary
     |
Execution
     |
Output Contract
     |
Verification
     |
Audit
```

Tool outputs are data, not authority.

---

# 28. Code Execution / Sandbox Architecture

Generated code follows:

```text
AGENT
 |
GENERATED CODE
 |
STATIC / POLICY CHECK
 |
AUTHORIZATION
 |
SANDBOX ADMISSION
 |
ISOLATED EXECUTION
 |
RESOURCE LIMIT
 |
RESULT
 |
TEST / VALIDATION
 |
VERIFICATION
```

Required independent boundaries:

- filesystem;
- network;
- credentials;
- processes;
- system calls;
- CPU;
- memory;
- storage;
- execution time.

No particular sandbox technology is selected.

The important architectural decision is:

> **The sandbox is an independent trust boundary, not merely a runtime option.**

---

# 29. Verification Architecture

Verification is a dedicated architectural domain.

```text
                  CANDIDATE OUTPUT
                        |
        +---------------+---------------+
        |       |        |       |       |
   Deterministic Evidence Semantic Numerical Policy
        |       |        |       |       |
        +---------------+---------------+
                        |
                  VERIFICATION RESULT
                        |
          +------+------+------+------+
          |             |             |
         PASS        CORRECT       ESCALATE
                                      |
                                   ABSTAIN
```

Human verification enters where the workflow requires consequential judgment.

Verification influences task state; it is not merely metadata attached after completion.

---

# 30. Artifact Architecture

```text
VERIFIED INFORMATION
        |
ARTIFACT SPECIFICATION
        |
TEMPLATE / FORMAT
        |
GENERATION
        |
STRUCTURAL CHECK
        |
CONTENT CHECK
        |
EVIDENCE CHECK
        |
ARTIFACT VERIFICATION
        |
+-------+---------+
|                 |
RELEASE        CORRECT
```

Artifact states remain:

```text
GENERATED → CHECKED → VERIFIED → HUMAN-APPROVED
```

Generation never implies approval.

---

# 31. Provenance Architecture

The architectural provenance chain is:

```text
SOURCE
 |
PROCESSING
 |
EVIDENCE
 |
DERIVED INFORMATION
 |
CLAIM
 |
ANALYSIS / DECISION
 |
ARTIFACT
```

Associated identities include, where applicable:

- user;
- task;
- source;
- revision;
- processing operation;
- capability;
- model/version;
- tool;
- execution;
- verification;
- approval.

The provenance architecture is logically independent of the physical storage technology.

---

# 32. Audit Architecture

Audit records capture significant events including:

- task creation;
- identity;
- data access;
- retrieval;
- model invocation;
- model selection;
- agent action;
- authorization;
- tool invocation;
- code execution;
- verification;
- correction;
- retry;
- escalation;
- failure;
- artifact generation;
- approval;
- security event;
- sovereignty event.

### Audit vs provenance

**Audit** answers:

> What happened?

**Provenance** answers:

> Where did this output come from?

**Observability** answers:

> Is the system operating correctly?

These concerns share correlation identifiers but are not collapsed into one mechanism.

---

# 33. Observability Architecture

Operational observability covers:

- task lifecycle;
- execution state;
- model latency;
- model resource consumption;
- GPU utilization;
- CPU/RAM;
- storage;
- tool latency;
- verification;
- failure;
- queueing;
- network events;
- sandbox events.

Sensitive payloads are minimized or access-controlled.

Hidden chain-of-thought is not an observability dependency.

---

# 34. Security Architecture

Security is layered:

```text
IDENTITY
   |
AUTHORIZATION
   |
TASK SCOPE
   |
DATA SCOPE
   |
CAPABILITY SCOPE
   |
TOOL SCOPE
   |
CODE SCOPE
   |
NETWORK SCOPE
   |
VERIFICATION
   |
AUDIT
```

The architecture follows:

- defense in depth;
- least privilege;
- external authority;
- deny-by-default for sensitive operations;
- independent enforcement.

---

# 35. Prompt-Injection Defense Architecture

The core invariant is:

> **Untrusted content cannot become control-plane authority.**

Attack path:

```text
Malicious Document
       |
OCR / Parsing
       |
Retrieved Content
       |
Model Context
       |
Agent Interpretation
       |
Tool Request
       |
CONTROL PLANE
       |
AUTHORIZATION / POLICY
       |
ALLOW OR DENY
```

A malicious instruction contained inside a document therefore remains **data**.

It cannot directly modify:

- policy;
- permissions;
- identity;
- task authority;
- tool authority;
- security state.

The same principle applies to:

- PDFs;
- DOCX;
- spreadsheets;
- images;
- OCR;
- source code;
- retrieved documents;
- tool output.

---

# 36. Network / Sovereignty Architecture

The sovereign architecture uses a deny-by-default external boundary.

```text
                EXTERNAL NETWORK
                       X
                       |
             +---------+---------+
             | EGRESS ENFORCEMENT|
             +---------+---------+
                       |
             SOVEREIGN BOUNDARY
                       |
       +---------------+---------------+
       |               |               |
      DATA             AI            TOOLS
       |               |               |
       +---------------+---------------+
                       |
                VERIFICATION
                       |
                   ARTIFACT
```

All core functions operate locally:

- AI;
- retrieval;
- document processing;
- verification;
- artifact generation;
- agent execution.

Zero-egress is not inferred from application behavior. It requires independent enforcement and observation.

The SRS explicitly requires external network behavior to be independently observable and network controls not to depend solely on application-level compliance.

---

# 37. Supply-Chain Architecture

The supply chain is treated as an input boundary:

```text
OFFLINE ACQUISITION
       |
INTEGRITY VALIDATION
       |
PROVENANCE
       |
SECURITY REVIEW
       |
APPROVAL
       |
CONTROLLED IMPORT
       |
VERSION REGISTRATION
       |
DEPLOYMENT
       |
AUDIT
```

Covered assets include:

- models;
- model weights;
- OCR models;
- libraries;
- packages;
- drivers;
- system dependencies;
- containers where used;
- configuration;
- templates;
- update bundles.

Rollback must be possible where operationally required.

---

# 38. Resource Architecture

A centralized logical **Resource Management Domain** is necessary.

It manages:

- GPU memory;
- GPU compute;
- CPU;
- RAM;
- storage;
- model residency;
- cache;
- sandbox capacity;
- concurrency.

Conceptually:

```text
             RESOURCE CONTROL
                    |
       +------------+------------+
       |            |            |
      AI         Processing    Sandbox
       |            |            |
      GPU       CPU/RAM       CPU/RAM
```

This does not imply a distributed scheduler.

For MVP, resource management should be lightweight and local.

---

# 39. Caching Architecture

Caching is allowed only where cache identity can preserve:

- task scope;
- authorization;
- source revision;
- temporal validity;
- provenance;
- invalidation state.

Potential caches:

- model weights;
- model state;
- OCR;
- document processing;
- embeddings;
- retrieval;
- intermediate representations;
- tool results;
- verification.

A cached result that has become stale or unauthorized must be unusable for the relevant task.

---

# 40. Storage Architecture

Logical storage domains:

```text
SOURCE DATA
PROCESSED DATA
EVIDENCE
METADATA
INDEXES
EMBEDDINGS
TASK STATE
AGENT STATE
EXECUTION STATE
TEMPORARY DATA
ARTIFACTS
PROVENANCE
AUDIT
CONFIGURATION
MODELS
MODEL METADATA
```

The architecture does **not** require each category to have separate physical storage.

For MVP, logically separate stores may be physically co-located where security, lifecycle and failure requirements permit.

---

# 41. Failure Domains

| Failure domain | Containment | User-visible outcome |
|---|---|---|
| UI | UI boundary | Session interruption |
| Task control | Control boundary | Workflow unavailable/paused |
| Model | Capability boundary | Capability unavailable/escalation |
| Retrieval | Knowledge boundary | Insufficient evidence |
| Document processing | Processing boundary | Processing failure |
| Agent | Agent boundary | Workflow failure/escalation |
| Tool | Tool boundary | Tool failure |
| Sandbox | Execution boundary | Security/execution failure |
| Verification | Verification boundary | Unverified result |
| Storage | Persistence boundary | Recovery/error |
| Network control | Sovereignty boundary | Security failure |
| Resource exhaustion | Resource boundary | Degrade/pause/fail |
| Supply chain | Lifecycle boundary | Import blocked |

Security failures do not enter normal retry loops.

---

# 42. Resilience Architecture

Failure handling follows:

```text
FAILURE
   |
CLASSIFY
   |
+--+--------+---------+----------+
|           |         |          |
RETRY     CORRECT   ESCALATE   SECURITY
|           |         |          |
bounded     |         |       CONTAIN
            +---------+----------+
                      |
                    FINAL STATE
```

Fallback is not automatically safe.

For example:

- model failure may permit capability substitution;
- authorization failure does not;
- security violation does not;
- verification failure may require correction;
- stale evidence may require re-retrieval;
- resource exhaustion may require scheduling rather than retry.

---

# 43. Configuration Architecture

Configuration is divided into:

1. system;
2. model;
3. capability;
4. tool;
5. policy;
6. user;
7. knowledge source;
8. verification;
9. artifact;
10. resource;
11. security.

Security-critical controls are outside agent authority.

Configuration changes have:

- identity;
- timestamp;
- version;
- previous state;
- new state;
- authorization;
- audit event.

---

# 44. Administration Architecture

Administrative authority is separate from agent authority.

```text
ADMINISTRATOR
      |
      v
ADMIN CONTROL
      |
 +----+----+----+----+
 |    |    |    |    |
Policy Models Tools Data
```

Administrative operations include:

- users;
- roles;
- models;
- capabilities;
- tools;
- knowledge sources;
- policies;
- audit;
- security;
- updates;
- backups;
- recovery.

---

# 45. Deployment Architecture

Three architectural deployment alternatives were considered:

### A. Single-process application

All logical domains share one process.

### B. Single-node modular multi-process system

Logical domains are separated into controlled processes but remain on one workstation/server.

### C. Distributed local services

Multiple services may run across multiple local nodes.

The analysis is performed later in Section 51.

---

# 46. Interface Architecture

Major interfaces:

| Interface | Information crossing | Authority rule |
|---|---|---|
| UI ↔ Control | Task/input/state | User authenticated |
| Control ↔ Agent | Task/plan/permissions | Control authoritative |
| Agent ↔ AI | Prompt/context/request | AI output untrusted |
| Agent ↔ Knowledge | Evidence request/result | Authorization enforced |
| Agent ↔ Tool | Tool request/result | Policy-gated |
| Tool ↔ Sandbox | Execution request/result | Restricted |
| Processing ↔ Evidence | Extracted representation | Provenance required |
| Evidence ↔ Retrieval | Query/evidence | Authorization-aware |
| Execution ↔ Verification | Candidate/result | Verification authoritative |
| Verification ↔ Artifact | Verified information | Release gated |
| System ↔ Provenance | Events/relationships | Correlated |
| System ↔ Audit | Significant events | Controlled access |

Interfaces require:

- schemas;
- version identity;
- authorization context;
- correlation identity;
- failure semantics;
- observability.

---

# 47. Concurrency Architecture

MVP concurrency is bounded.

The architecture supports multiple:

- users;
- tasks;
- document-processing operations;
- model requests;
- sandbox executions.

But concurrency is subordinate to resource qualification.

Logical queueing is required where resource contention exists.

The system must prevent:

- uncontrolled GPU overcommitment;
- RAM exhaustion;
- sandbox starvation;
- verification starvation;
- indefinite agent queues.

No numerical concurrency target is asserted until benchmarking.

---

# 48. Resource Scheduling Architecture

A centralized resource-admission function is preferred.

```text
REQUEST
  |
RESOURCE ESTIMATE
  |
POLICY CHECK
  |
CAPACITY CHECK
  |
+------+------+
|             |
ADMIT        QUEUE
|             |
EXECUTE      WAIT
|
RELEASE
```

Resource scheduling shall account for:

- model residency;
- context size;
- document size;
- modality;
- verification depth;
- sandbox resources;
- concurrent tasks.

---

# 49. Data Consistency / Revision Architecture

The evidence architecture must preserve:

- document identity;
- revision identity;
- effective time;
- ingestion time;
- authority;
- supersession;
- conflict.

Retrieval cannot collapse:

```text
CURRENT REVISION
        ≠
SUPERSEDED REVISION
```

unless the task explicitly requests historical information.

A revision-aware evidence selection function therefore precedes reasoning.

---

# 50. Human Authority Architecture

Human authority is an architectural boundary.

Human approval may be required for:

- consequential engineering interpretation;
- safety;
- formal approval;
- security exceptions;
- policy exceptions;
- consequential artifacts;
- physical actions.

Approval is represented as an explicit state transition:

```text
AI OUTPUT
   |
VERIFICATION
   |
APPROVAL REQUIRED
   |
HUMAN REVIEW
   |
+------+------+
|             |
APPROVE      REJECT
```

No approval may be inferred from:

- user inactivity;
- model confidence;
- successful generation;
- agent completion;
- lack of error.

---

# 51. Architectural Alternatives

This section is the central adversarial evaluation.

Four genuinely different architectural alternatives were considered.

---

## Alternative A — Integrated Monolithic Workbench

### Structure

One principal application process owns:

- task control;
- agent;
- retrieval;
- AI calls;
- document processing;
- tools;
- verification;
- artifact generation;
- audit.

Sandboxed code executes separately.

### Strengths

- minimal operational complexity;
- low inter-process latency;
- straightforward MVP deployment;
- simple state management;
- low memory overhead.

### Weaknesses

- weak isolation between logical security domains;
- difficult containment of compromised components;
- model/runtime failure can affect control;
- prompt-injection containment depends heavily on internal discipline;
- security boundaries become predominantly logical;
- difficult independent enforcement;
- audit and control components share a large failure domain.

### SRS evaluation

| Criterion | Assessment |
|---|---|
| PRD compliance | Strong |
| SRS compliance | Partial |
| Sovereignty | Strong if host-enforced |
| Security | Weak/Moderate |
| Isolation | Weak |
| Agent control | Moderate |
| Evidence integrity | Strong |
| Verification | Strong |
| Resource efficiency | Strong |
| Failure containment | Weak |
| Auditability | Strong |
| MVP feasibility | Strong |
| Future scalability | Moderate |

### Verdict

**REJECTED AS PRIMARY ARCHITECTURE**

It optimizes implementation simplicity at precisely the boundaries where the SRS requires structural separation.

---

## Alternative B — Fully Distributed Local Microservices

### Structure

Nearly every domain becomes an independent service:

- identity;
- task;
- policy;
- agent;
- model gateway;
- model workers;
- retrieval;
- evidence;
- document processing;
- OCR;
- tools;
- sandbox;
- verification;
- artifact;
- provenance;
- audit;
- resource scheduler.

### Strengths

- excellent logical isolation;
- independent failure domains;
- strong extensibility;
- clear interfaces;
- future multi-node scaling;
- independent deployment.

### Weaknesses

- excessive MVP complexity;
- substantial IPC/network overhead;
- duplicated serialization;
- more state synchronization;
- more resource overhead;
- more operational failure modes;
- harder single-node diagnosis;
- unnecessary distributed-systems complexity.

### SRS evaluation

| Criterion | Assessment |
|---|---|
| PRD compliance | Strong |
| SRS compliance | Strong |
| Sovereignty | Strong |
| Security | Strong |
| Isolation | Strong |
| Agent control | Strong |
| Evidence integrity | Strong |
| Verification | Strong |
| Resource efficiency | Moderate/Weak |
| Failure containment | Strong |
| Auditability | Strong |
| MVP feasibility | Weak/Moderate |
| Future scalability | Strong |
| Operational complexity | Poor |

### Verdict

**REJECTED FOR MVP**

The SRS requires security boundaries, not maximum service count. Full distribution adds complexity without proportionate MVP value.

---

## Alternative C — Modular Single-Node Architecture with Protected Execution Boundaries

### Structure

A single workstation/server hosts logically modular domains.

Critical control and security boundaries are separated into processes or equivalent independently enforceable execution domains where justified.

```text
                 USER
                   |
             INTERACTION
                   |
          CONTROL / AUTHORITY
          /    |       |     \
       TASK POLICY   STATE  APPROVAL
          |
     +----+-----------------------------+
     |                                  |
     v                                  v
 AGENT / WORKFLOW                 KNOWLEDGE/EVIDENCE
     |                                  |
     v                                  v
 CAPABILITY LAYER                 DOCUMENT / MULTIMODAL
     |                                  |
     +---------------+------------------+
                     |
              CONTROLLED TOOLS
                     |
             +-------+-------+
             |               |
          TOOL EXEC       CODE SANDBOX
             |               |
             +-------+-------+
                     |
                 VERIFICATION
                     |
             +-------+-------+
             |               |
         ARTIFACT        PROVENANCE
             |               |
             +-------+-------+
                     |
                   AUDIT

       Independent sovereignty/network boundary
       Independent resource control
```

### Strengths

- preserves logical architecture;
- strong control/data separation;
- independent code boundary;
- local deployment;
- low operational overhead;
- appropriate failure containment;
- efficient resource utilization;
- model agnosticism;
- future migration path to distributed deployment;
- compatible with single workstation/server.

### Weaknesses

- more complex than a monolith;
- requires disciplined interfaces;
- process isolation may consume resources;
- some high-assurance boundaries still require technical validation;
- future distributed scale is not the immediate optimization target.

### SRS evaluation

| Criterion | Assessment |
|---|---|
| PRD compliance | Strong |
| SRS compliance | Strong |
| Sovereignty | Strong |
| Security | Strong |
| Isolation | Strong |
| Agent control | Strong |
| Evidence integrity | Strong |
| Verification | Strong |
| Performance | Strong candidate |
| Resource efficiency | Strong candidate |
| Reliability | Strong |
| Failure containment | Strong |
| Observability | Strong |
| Extensibility | Strong |
| MVP feasibility | Strong |
| Operational complexity | Moderate |
| Future scalability | Strong enough |
| Maintainability | Strong |

### Verdict

**PREFERRED**

This is the best balance between the SRS's security requirements and the MVP's single-node/resource constraints.

---

## Alternative D — Event-Sourced Durable Execution Architecture

### Structure

The system is fundamentally organized around durable events:

```text
Task Event
   |
Planner
   |
Action Event
   |
Execution Event
   |
Verification Event
   |
Artifact Event
   |
Approval Event
```

State is derived from an event history.

### Strengths

- excellent auditability;
- strong replay;
- durable workflows;
- explicit state transitions;
- useful for long-running agent execution;
- strong provenance potential;
- recovery-friendly.

### Weaknesses

- substantial implementation complexity;
- event/schema evolution burden;
- replay complexity;
- sensitive-data duplication;
- potentially large storage footprint;
- difficult to guarantee that replay is semantically identical for AI components;
- does not itself solve sandbox, authorization, sovereignty or resource isolation.

### Verdict

**REJECTED AS THE PRIMARY SYSTEM ORGANIZING PRINCIPLE**

However, selected event-sourced concepts are adopted within the preferred architecture for:

- significant state transitions;
- audit;
- execution identity;
- recovery;
- provenance.

The system should therefore be **event-aware**, not necessarily a pure event-sourced system.

---

# 52. Architecture Decision Records

## ADR-01 — Modular single-node over monolith

**Context:** Security boundaries and resource constraints conflict with both a monolith and a distributed system.

**Options:** A, B, C, D.

**Decision:** **C — Modular Single-Node Architecture**

**Rationale:** It provides structural security boundaries without imposing distributed-system complexity on MVP.

**Status:** **Preferred**

**Validation:** Process/resource overhead and isolation effectiveness.

---

## ADR-02 — Logical control/data separation

**Decision:** Separate control plane and data plane conceptually and enforce critical authority boundaries independently.

**Rationale:** Untrusted content and model outputs must not become authority.

**Status:** **Preferred**

---

## ADR-03 — Central authoritative task state

**Decision:** Task/control state is owned by the control domain, not by the agent or model context.

**Rationale:** Completion and authorization require deterministic system authority.

**Status:** **Preferred**

---

## ADR-04 — Evidence as governed architectural object

**Decision:** Evidence receives identity, authorization, revision, authority, temporal and provenance semantics.

**Rationale:** Retrieval cannot be reduced to similarity search.

**Status:** **Preferred**

---

## ADR-05 — Independent execution boundary for generated code

**Decision:** Generated code executes outside the trusted control domain.

**Rationale:** Generated code is untrusted.

**Status:** **Mandatory architectural decision**

---

## ADR-06 — Dedicated verification domain

**Decision:** Verification is an explicit architectural stage that controls completion.

**Rationale:** Verification is part of the system completion contract.

**Status:** **Preferred**

---

## ADR-07 — Capability abstraction

**Decision:** Models implement abstract capabilities through governed contracts.

**Rationale:** Prevents model lock-in and supports adaptive local model selection.

**Status:** **Preferred**

---

## ADR-08 — Central logical resource management

**Decision:** A resource-management domain controls admission, residency and contention.

**Rationale:** The single-node GPU constraint makes resource contention a system-level problem.

**Status:** **Preferred; hardware validation required**

---

## ADR-09 — Event-aware audit rather than pure event sourcing

**Decision:** Use durable correlated execution events without making the entire system purely event-sourced.

**Rationale:** Captures audit/recovery value while avoiding unnecessary state/replay complexity.

**Status:** **Preferred**

---

## ADR-10 — Independent sovereignty boundary

**Decision:** Network enforcement must remain outside application/model obedience.

**Rationale:** Application-level zero-egress claims are insufficient.

**Status:** **Mandatory architectural decision**

---

# 53. Quality Attribute Scenarios

## Sovereignty

**Stimulus:** Confidential workflow executes.

**Expected response:** No unauthorized external communication or processing occurs.

**Validation:** Network enforcement + packet capture + adversarial tests.

---

## Security

**Stimulus:** Malicious document attempts to issue instructions.

**Expected response:** Content remains untrusted data and cannot alter authority.

**Validation:** Prompt-injection attack suite.

---

## Reliability

**Stimulus:** Primary model fails during execution.

**Expected response:** Workflow enters explicit capability-failure state or safely escalates.

**Validation:** Fault injection.

---

## Resource

**Stimulus:** Concurrent workloads compete for GPU memory.

**Expected response:** Resource admission prevents uncontrolled exhaustion.

**Validation:** Load/soak testing.

---

## Evidence integrity

**Stimulus:** Current and superseded documents both match a query.

**Expected response:** Authority/revision policy determines admissible evidence.

**Validation:** Revision corpus evaluation.

---

## Verification

**Stimulus:** Candidate artifact contains an incorrect claim.

**Expected response:** Applicable verification detects/rejects/escalates it.

**Validation:** Workflow evaluation.

---

## Recoverability

**Stimulus:** A long-running workflow encounters a recoverable service failure.

**Expected response:** Useful task state remains recoverable.

**Validation:** Fault injection.

---

## Observability

**Stimulus:** An operator investigates a failed workflow.

**Expected response:** Operator can reconstruct material actions, state, evidence, capability, failures and verification without hidden chain-of-thought.

**Validation:** Audit replay.

---

## Safety

**Stimulus:** Agent attempts consequential action.

**Expected response:** External authorization/human authority gate prevents unauthorized execution.

**Validation:** Security assessment.

---

# 54. Architecture Traceability Matrix

| SRS driver | Architectural owner | Mechanism | Validation |
|---|---|---|---|
| Sovereignty | Sovereignty domain | External egress enforcement | Network test |
| Multiple AI capabilities | Intelligence | Capability abstraction | Capability substitution test |
| Evidence governance | Knowledge/Evidence | Governed evidence objects | Retrieval evaluation |
| Bounded agent | Control + Agent | External authority | Security test |
| Controlled tools | Execution | Tool contracts + policy gate | Security test |
| Untrusted code | Sandbox | Independent execution boundary | Adversarial test |
| Verification | Verification | Dedicated verification flow | Workflow evaluation |
| Provenance | Provenance | Source-to-output lineage | Trace reconstruction |
| Multimodal | Document/Multimodal | Specialized processing paths | Multimodal evaluation |
| P&ID | Engineering domain | Structural representation | Engineering evaluation |
| Single-node constraint | Resource domain | Admission/residency control | Hardware benchmark |
| Auditability | Audit | Correlated execution events | Audit replay |
| Offline lifecycle | Supply-chain domain | Controlled import/update | Operational validation |

The architecture therefore gives every major SRS driver an architectural owner.

---

# 55. Architectural Risk Register

| Risk | Cause | Impact | Severity | Mitigation | Validation |
|---|---|---|---|---|---|
| GPU pressure | Multiple models/capabilities | Workflow failure | High | Admission/residency control | Benchmark |
| Model switching overhead | Dynamic routing | Latency | High | Routing/resource policy | Benchmark |
| Agent unreliability | Planning errors | Unsafe/incomplete workflows | Critical | Bounded execution + verification | Workflow benchmark |
| Retrieval error | Semantic/revision conflict | Wrong answer | Critical | Evidence governance | Corpus evaluation |
| Evidence conflict | Multiple authorities | Incorrect conclusion | High | Explicit conflict state | Evaluation |
| Multimodal complexity | Heterogeneous processing | Wrong interpretation | High | Specialized pipeline | Benchmark |
| Sandbox escape | Host exposure | Security compromise | Critical | Independent isolation | Adversarial testing |
| Prompt injection | Untrusted documents | Unauthorized action | Critical | Data/control separation | Attack suite |
| Network leakage | Hidden dependency | Sovereignty failure | Critical | External enforcement | Packet tests |
| Storage growth | Evidence/provenance/audit | Resource exhaustion | High | Lifecycle controls | Soak test |
| Cache invalidation | Revision changes | Stale evidence | High | Versioned cache keys | Revision tests |
| Verification bottleneck | Deep verification | Latency | Medium/High | Risk-tiered verification | Benchmark |
| Artifact failure | Generation errors | User rejection | High | Structural/content verification | Artifact tests |
| Operational complexity | Too many boundaries | Deployment burden | Medium | Co-location | Pilot |
| Single-node failure | Shared hardware | System outage | High | Recovery/backup | Fault injection |
| Supply-chain compromise | Offline import | System compromise | Critical | Integrity/provenance gates | Supply-chain test |

---

# 56. Architectural Assumption Register

| Assumption | Dependency | Impact if false | Validation | Status |
|---|---|---|---|---|
| Local models meet MVP quality | Intelligence architecture | Product infeasible | End-to-end benchmark | Open |
| Single-node hardware is adequate | Resource architecture | Deployment invalid | Full-workflow benchmark | Open |
| Modular process overhead is acceptable | Deployment architecture | Simplification required | Prototype | Open |
| Evidence metadata is available | Knowledge architecture | Authorization/revision weakened | Customer corpus | Open |
| P&ID structure can be extracted sufficiently | Engineering architecture | W2 scope affected | Engineering evaluation | Open |
| Verification can operate within resource envelope | Verification architecture | Latency/resource conflict | Benchmark | Open |
| Sandbox mechanism can meet isolation requirement | Execution architecture | W5 affected | Security validation | Open |
| External network enforcement is deployable | Sovereignty architecture | Sovereignty claim fails | Deployment test | Open |
| Customer accepts operational controls | Deployment | Adoption affected | Customer validation | Open |

---

# 57. Architectural Open Questions

1. Exact process boundaries for MVP.
2. Model co-loading versus model switching.
3. Exact resource-admission strategy.
4. Exact evidence persistence structure.
5. Exact retrieval projection architecture.
6. Exact provenance representation.
7. Exact sandbox mechanism.
8. Exact network enforcement mechanism.
9. Exact authorization integration.
10. Exact deployment profile.
11. Exact audit retention.
12. Exact concurrency target.
13. Exact P&ID representation.
14. Exact verification implementation.
15. Exact artifact-generation boundary.
16. Exact model registry lifecycle.
17. Whether W5 enters the first production profile.

These are intentionally carried to Phase 11 or targeted technical validation.

---

# 58. MVP Architecture

The MVP baseline is:

```text
                         USER
                           |
                           v
                 +-------------------+
                 | INTERACTION       |
                 +---------+---------+
                           |
                 +---------v---------+
                 | CONTROL /         |
                 | AUTHORITY         |
                 |-------------------|
                 | Task State        |
                 | Policy            |
                 | Authorization     |
                 | Approval          |
                 | Resource Control  |
                 +---------+---------+
                           |
            +--------------+--------------+
            |              |              |
            v              v              v
       +---------+    +---------+    +---------+
       | AGENT   |    | EVIDENCE|    | AI      |
       | RUNTIME |    | DOMAIN  |    | CAP.    |
       +----+----+    +----+----+    +----+----+
            |              |              |
            |       +------+-------+      |
            |       | Document/    |      |
            |       | Multimodal   |      |
            |       +------+-------+      |
            |              |              |
            +--------------+--------------+
                           |
                 +---------v---------+
                 | CONTROLLED TOOLS  |
                 +---------+---------+
                           |
                 +---------v---------+
                 | CODE EXECUTION /  |
                 | SANDBOX           |
                 +---------+---------+
                           |
                 +---------v---------+
                 | VERIFICATION      |
                 +---------+---------+
                           |
              +------------+------------+
              |                         |
              v                         v
        +-----------+             +-----------+
        | ARTIFACT  |             | PROVENANCE|
        +-----------+             +-----------+
              |                         |
              +------------+------------+
                           v
                       +-------+
                       | AUDIT |
                       +-------+

     Independent network / sovereignty enforcement
     Independent host/resource boundaries
```

### Mandatory MVP domains

- interaction;
- control/authority;
- agent;
- AI capability;
- knowledge/evidence;
- document/multimodal;
- controlled tools;
- sandbox;
- verification;
- artifacts;
- provenance;
- audit;
- resource management;
- security/network;
- configuration/operations.

### Optional/conditional

- W5 code-analysis workflow;
- broader enterprise integrations;
- additional artifact formats;
- advanced multimodal capabilities.

---

# 59. MVP vs Future Architecture

## MVP

Optimize for:

- one workstation/server;
- controlled process boundaries;
- local inference;
- governed evidence;
- bounded agent;
- isolated code;
- verification;
- provenance;
- audit;
- zero-egress;
- resource admission.

## Phase 2

Potential additions:

- additional model workers;
- richer enterprise integrations;
- more artifact formats;
- stronger deployment profiles;
- more sophisticated distributed execution.

## Future enterprise scale

Potentially:

```text
Multiple Control / Execution Nodes
          |
Shared or Federated Knowledge
          |
Dedicated Model Capacity
          |
Multiple Sandbox Workers
          |
Centralized Enterprise Governance
```

The logical architecture remains stable while physical deployment expands.

---

# 60. Architectural Simplification Review

The following were deliberately rejected as MVP complexity:

### Separate physical service for every logical domain

**Rejected.** Logical separation is sufficient where independent isolation is not required.

### Full event-sourced system

**Rejected.** Event durability is retained selectively.

### Distributed model cluster

**Rejected.** Conflicts with MVP hardware constraint.

### Separate physical database for every data class

**Rejected.** Logical storage separation is sufficient initially.

### Universal knowledge graph

**Rejected.** Only workflow-required structured representations are justified.

### Universal multimodal pipeline

**Rejected.** Capability-specific processing is more resource-conscious.

### Permanent model co-loading

**Not assumed.** Hardware validation determines residency strategy.

### Maximum concurrency

**Rejected.** Resource safety takes priority.

The result is:

> **minimum architecture that fully satisfies the SRS, not maximum architectural sophistication.**

---

# 61. Security Architecture Review

| Question | Result |
|---|---|
| Can sensitive actions be associated with identity? | Yes, architecturally |
| Can sensitive actions be authorized? | Yes |
| Can agent bypass authorization? | Designed to prevent |
| Can tools bypass policy? | Designed to prevent |
| Can generated code escape? | Boundary exists; implementation validation required |
| Can unauthorized data reach model? | Authorization-aware evidence architecture |
| Can stale evidence silently become current? | Revision-aware architecture prevents by design |
| Can malicious documents change policy? | Control/data separation prevents |
| Can data leave sovereign boundary? | External enforcement boundary required |
| Can supply-chain inputs bypass control? | Import/integrity boundary defined |
| Can security events be reconstructed? | Yes |
| Can human authority be bypassed? | Approval/authority boundary defined |

**Security architecture status:** structurally ready; empirical assurance required.

---

# 62. Sovereignty Architecture Review

The sovereignty chain is:

```text
CONFIDENTIAL DATA
       |
LOCAL PROCESSING
       |
LOCAL AI
       |
LOCAL TOOLS
       |
LOCAL VERIFICATION
       |
LOCAL ARTIFACT
```

There is no architectural dependency on:

- external AI APIs;
- cloud inference;
- external vector search;
- external telemetry;
- external model download;
- external license validation;
- external analytics.

Potential deployment dependencies requiring explicit validation include:

- identity infrastructure;
- update acquisition;
- package import;
- DNS;
- host management;
- monitoring;
- backup.

The sovereignty architecture therefore treats:

> **runtime sovereignty**

and

> **lifecycle sovereignty**

as separate properties.

---

# 63. Architectural Verification Plan

| Property | Validation |
|---|---|
| Zero egress | Packet capture + enforcement test |
| Tool isolation | Security assessment |
| Sandbox containment | Adversarial execution |
| Evidence authorization | Access-control test corpus |
| Revision correctness | Revision/conflict evaluation |
| Agent reliability | End-to-end workflow benchmark |
| Artifact quality | Automated + human evaluation |
| Resource feasibility | Full-workflow hardware benchmark |
| Recovery | Fault injection |
| Provenance | Trace reconstruction |
| Auditability | Audit replay |
| Prompt injection | Adversarial corpus |
| Model substitution | Capability compatibility test |
| Verification effectiveness | False-acceptance/false-rejection evaluation |
| P&ID usefulness | Engineering evaluation |
| Cache correctness | Revision/invalidation test |
| Supply chain | Offline import/integrity test |

No test result is claimed by this architecture document.

---

# 64. Technology-Selection Boundary

## Architecture Decisions — established

1. Modular single-node architecture.
2. Logical control/data-plane separation.
3. External authority over agent authority.
4. Capability abstraction.
5. Governed evidence architecture.
6. Authorization-aware retrieval.
7. Independent code execution boundary.
8. Dedicated verification domain.
9. Provenance as an architectural concern.
10. Audit as a separate assurance concern.
11. Independent sovereignty/network boundary.
12. Central logical resource-management domain.
13. Revision-aware knowledge architecture.
14. Risk-aware bounded agent execution.
15. Logical modularity with physical co-location where safe.
16. Human approval as an explicit architectural state.
17. Event-aware execution/audit rather than mandatory pure event sourcing.

## Technology Decisions — deliberately unselected

- LLMs;
- VLMs;
- embedding models;
- rerankers;
- OCR engines;
- inference engine;
- agent framework;
- workflow engine;
- retrieval engine;
- vector/index technology;
- database;
- object store;
- provenance implementation;
- sandbox mechanism;
- container runtime;
- process-isolation mechanism;
- network enforcement mechanism;
- operating system;
- GPU;
- orchestration technology;
- observability stack.

The Phase-10 document therefore establishes **architecture contracts**, not vendor choices.

---

# 65. Architecture Readiness Assessment

| Criterion | Result |
|---|---|
| Architectural boundaries stable | **YES** |
| Responsibilities clear | **YES** |
| Interfaces defined | **YES** |
| Trust zones defined | **YES** |
| Control/data flow understood | **YES** |
| Major alternatives evaluated | **YES** |
| Alternatives eliminated against SRS | **YES** |
| Security architecture established | **YES** |
| Sovereignty architecture established | **YES** |
| Resource architecture established | **YES, validation required** |
| Failure domains established | **YES** |
| MVP architecture defined | **YES** |
| Technology choices still separated | **YES** |
| Hardware feasibility proven | **NO — validation required** |
| Sandbox assurance proven | **NO — validation required** |
| Agent reliability proven | **NO — validation required** |
| P&ID quality proven | **NO — validation required** |

### Overall status

# **ARCHITECTURE READY WITH TARGETED VALIDATION**

The architecture is sufficiently defined to constrain Phase 11 technology selection.

---

# 66. Architecture Acceptance Checklist

### A1 — Can every major SRS requirement map to an architectural domain?

**YES.**

### A2 — Can every sensitive data flow be identified?

**YES.**

### A3 — Can every authority boundary be identified?

**YES.**

### A4 — Can the agent be prevented from bypassing policy?

**Architecturally YES; implementation validation required.**

### A5 — Can untrusted code be contained?

**Architectural boundary YES; sandbox technology validation required.**

### A6 — Can indirect prompt injection be contained?

**Architecturally YES through control/data separation; adversarial validation required.**

### A7 — Can evidence authorization be enforced?

**YES through authorization-aware retrieval architecture.**

### A8 — Can evidence provenance be preserved?

**YES through first-class evidence/provenance architecture.**

### A9 — Can generated results be verified before completion?

**YES through dedicated verification and authoritative task state.**

### A10 — Can the system operate without external AI APIs?

**YES by architecture.**

### A11 — Can zero-egress behavior be demonstrated?

**YES through independent network enforcement/observation; deployment validation required.**

### A12 — Can multiple local AI capabilities coexist?

**YES through capability abstraction and resource admission.**

### A13 — Can models be replaced without redesigning the entire system?

**YES, subject to capability-contract compatibility.**

### A14 — Can the architecture operate within the intended hardware envelope?

**Architecturally designed for it; not yet empirically proven.**

### A15 — Can failures be isolated?

**YES at the architectural-domain level.**

### A16 — Can execution be audited?

**YES.**

### A17 — Can important outputs be traced?

**YES through provenance.**

### A18 — Can human consequential authority be preserved?

**YES.**

### A19 — Can MVP avoid unnecessary distributed-system complexity?

**YES.**

### A20 — Is technology selection now sufficiently constrained?

**YES.**

---

# FINAL ARCHITECTURAL DECISIONS

## Decision 1 — Architecture Status

# **ARCHITECTURE READY WITH TARGETED VALIDATION**

The architecture has sufficient definition for Phase 11 technology selection.

---

## Decision 2 — Major Architectural Decisions

The following are established:

1. **Modular single-node architecture** is preferred for MVP.
2. **Control plane and data plane are logically separated.**
3. **Authority resides outside the AI/agent.**
4. **Agent state is subordinate to authoritative system state.**
5. **Evidence is a governed first-class architectural object.**
6. **Retrieval is authorization-, authority-, revision- and temporal-aware.**
7. **AI capabilities are abstracted from specific models.**
8. **Generated code has an independent execution boundary.**
9. **Verification is a dedicated architectural domain.**
10. **Artifacts progress through generated → checked → verified → approved states.**
11. **Provenance is maintained from source to artifact.**
12. **Audit and operational observability are distinct concerns.**
13. **Sovereignty is independently enforced and observable.**
14. **Resource management is a first-class system function.**
15. **Logical modularity does not imply distributed deployment.**
16. **Human consequential authority remains outside AI authority.**

---

## Decision 3 — Deferred Decisions

Phase 11 shall determine:

- model portfolio;
- model sizes;
- quantization;
- inference engine;
- model-serving topology;
- agent/workflow technology;
- retrieval/index technology;
- document-processing technology;
- OCR;
- storage;
- provenance implementation;
- sandbox;
- network enforcement mechanism;
- operating system;
- deployment packaging;
- observability tooling.

Technology selection must now be performed **against this architecture**, rather than directly against the product idea.

---

## Decision 4 — Validation Required

Before architecture can be considered empirically qualified:

1. single-node hardware benchmark;
2. model residency/switching benchmark;
3. multimodal benchmark;
4. P&ID benchmark;
5. evidence/retrieval benchmark;
6. end-to-end agent reliability benchmark;
7. verification effectiveness benchmark;
8. sandbox adversarial validation;
9. zero-egress test;
10. prompt-injection test;
11. artifact-quality evaluation;
12. fault-injection/recovery testing;
13. cache/revision correctness testing;
14. offline supply-chain validation.

These are **architecture validation activities**, not reasons to reopen the product definition.

---

## Decision 5 — Next Phase

# **PHASE 11 — ARCHITECTURE DECISION & TECHNOLOGY SELECTION**

Phase 11 should select technologies by evaluating them against:

```text
APPROVED PRD
      ↓
APPROVED SRS
      ↓
PHASE 10 ARCHITECTURE
      ↓
TECHNOLOGY CANDIDATES
      ↓
BENCHMARK / SECURITY / RESOURCE EVIDENCE
      ↓
TRADE-OFF ANALYSIS
      ↓
TECHNOLOGY DECISIONS
      ↓
IMPLEMENTATION BASELINE
```

The governing question for Phase 11 is no longer:

> "What technology would be good for an AI application?"

It is:

> **"Which concrete technologies can satisfy the established architecture under the sovereignty, security, evidence, verification, multimodal, reliability and single-node resource constraints?"**

# PHASE 10 FINAL GATE

## **GATE A — ARCHITECTURE BASELINE ESTABLISHED**

The architecture has survived adversarial comparison.

The important result is not that one architecture was drawn and justified. It is that:

- the **monolithic alternative was rejected** for insufficient structural isolation;
- the **fully distributed alternative was rejected** for unnecessary MVP complexity and resource cost;
- the **pure event-sourced alternative was rejected** as the primary organizing principle while retaining its useful durability concepts;
- the **modular single-node architecture survived** because it provides the required security and authority boundaries without violating the MVP deployment/resource constraint.

This establishes a defensible architectural basis for Phase 11 technology selection.