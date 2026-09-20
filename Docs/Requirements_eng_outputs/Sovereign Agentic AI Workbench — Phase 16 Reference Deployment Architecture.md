# SOVEREIGN AGENTIC AI WORKBENCH

# PHASE 16 — REFERENCE DEPLOYMENT ARCHITECTURE

**Status:** REFERENCE DEPLOYMENT READY WITH CONDITIONS  
**Architecture mode:** Single sovereign Linux workstation/server  
**Primary deployment objective:** Execute complete verified MVP workflows within an explicitly bounded security, resource, reliability and sovereignty envelope.

---

# 1. Executive Deployment Decision

## 1.1 Decision

The MVP shall use a:

> **Single Linux-based enterprise workstation/server with one high-memory GPU, large host RAM, local NVMe storage, host-enforced network controls, colocated application/data services, and separately isolated execution boundaries for untrusted document processing and generated code.**

The deployment deliberately does **not** introduce Kubernetes, service mesh, distributed storage, multiple inference servers, or a multi-node cluster for the MVP.

This follows the Phase 16 principle that the simplest deployment satisfying security, performance, isolation, reliability and operational requirements is preferred.

### Reference hardware envelope

| Resource | Reference target | Status |
|---|---:|---|
| CPU | 16–32 modern x86-64 cores/threads-class | Candidate |
| System RAM | **128 GB ECC preferred** | Candidate |
| GPU | **1 × 48 GB VRAM-class accelerator** | Candidate |
| GPU count | 1 | Architectural decision |
| VRAM | 48 GB class | Requires Validation |
| OS storage | 1 TB NVMe SSD | Candidate |
| Application/data storage | 4 TB NVMe SSD | Candidate |
| Backup | Separate offline storage | Required |
| Network | 1 × enterprise interface + controlled management/update path | Candidate |
| OS | Hardened Linux | Candidate |
| Deployment | Single physical host | **Preferred MVP** |

These figures define the **reference qualification target**, not demonstrated performance claims.

The Phase 16 methodology explicitly prohibits declaring hardware feasible from theoretical specifications; feasibility must be established through complete workflow execution, resource measurement, concurrency testing and failure testing.

---

# 2. Current State

The architecture entering Phase 16 is already substantially constrained:

- modular single-node architecture;
- external authority over AI actions;
- control/data-plane separation;
- evidence-first knowledge architecture;
- bounded agent runtime;
- multiple local AI capabilities;
- controlled tools;
- isolated generated-code execution;
- independent verification;
- provenance and audit;
- zero-egress requirement;
- offline lifecycle;
- W3, W1, W2 and W4 as MVP workflows;
- W5 conditional.

The technology baseline identifies vLLM as the preferred inference layer, Qwen3.5 as the leading compact multimodal family, Docling plus specialized OCR/layout processing, LangGraph for bounded agent execution, Qdrant as a retrieval candidate, SQLite for MVP transactional state, Firecracker as the high-assurance sandbox candidate, OpenTelemetry for observability, and host-level network enforcement as mandatory.

The deployment problem is therefore no longer conceptual architecture.

It is:

> **Can these components coexist on one physical machine without resource contention, security boundary failure, unacceptable latency, operational fragility or sovereignty failure?**

---

# 3. Deployment Gap

The major remaining uncertainty is empirical.

Known:

- logical architecture;
- component responsibilities;
- technology candidates;
- security boundaries;
- workflow definitions;
- required measurements.

Not yet established:

- exact GPU requirement;
- exact VRAM operating envelope;
- simultaneous model residency;
- model switching cost;
- maximum supported concurrency;
- sustained thermal behavior;
- complete workflow latency;
- storage growth rate;
- recovery performance;
- actual zero-egress behavior;
- sandbox isolation under adversarial testing.

Therefore:

> **Phase 16 establishes the reference deployment architecture but does not falsely convert candidate hardware into a validated production configuration.**

This distinction is required by the phase specification.

---

# 4. Deployment Alternatives

## Alternative A — High-end multi-GPU server

**Rejected for MVP.**

Advantages:

- large VRAM;
- simultaneous model residency;
- high throughput;
- greater concurrency.

Problems:

- excessive capital and power;
- larger operational footprint;
- unnecessary complexity;
- moves the product toward infrastructure-heavy deployment;
- weakens the MVP's ability to demonstrate useful sovereign AI on relatively compact infrastructure.

Use later only if workflow evidence requires it.

---

## Alternative B — Low-memory consumer workstation

**Rejected as primary reference deployment.**

Typical weakness:

- insufficient VRAM margin;
- excessive model swapping;
- weak concurrency;
- poor P&ID/document-processing headroom;
- increased CPU/RAM offloading;
- reduced operational predictability.

It may become a minimum-cost qualification target if experiments demonstrate acceptable performance.

---

## Alternative C — Single 48 GB-class professional workstation/server

**Preferred.**

Advantages:

- sufficient VRAM candidate for compact local model portfolio;
- single-GPU scheduling;
- simpler sovereignty boundary;
- simpler administration;
- lower failure-domain count;
- easier deployment qualification;
- compatible with single-node architecture;
- enough host RAM for document processing, indexes, evidence and sandbox workloads.

Primary risk:

> Whether 48 GB VRAM provides adequate margin when inference, VLM workloads, KV cache, context length and model switching are exercised under realistic workflows.

Therefore this is the **reference qualification target**, not yet a validated guarantee.

---

## Alternative D — Two independent hosts

**Deferred.**

Potential future roles:

- high availability;
- separated AI and application workloads;
- larger model capacity;
- departmental deployments.

Not justified for MVP unless single-host validation fails.

---

# 5. Selected Reference Deployment

## 5.1 Physical topology

```text
                    ENTERPRISE USERS
                           |
                    Controlled Access
                           |
                    Enterprise Network
                           |
                    [Network Firewall]
                           |
                    [Sovereign Host NIC]
                           |
        +------------------+------------------+
        |             SOVEREIGN HOST         |
        |                                    |
        |  HOST SECURITY / FIREWALL          |
        |             |                      |
        |  +-----------v------------------+   |
        |  |      CONTROL PLANE           |   |
        |  | Identity / Policy            |   |
        |  | Task / Workflow / State      |   |
        |  | Capability / Resource Ctrl   |   |
        |  +-----------+------------------+   |
        |              |                      |
        |  +-----------v------------------+   |
        |  |       DATA / AI PLANE        |   |
        |  | Retrieval / Evidence         |   |
        |  | Document / OCR / P&ID        |   |
        |  | Inference / Verification     |   |
        |  +-----------+------------------+   |
        |              |                      |
        |  +-----------v------------------+   |
        |  |   RESTRICTED EXECUTION       |   |
        |  | Tools / Parser Workers       |   |
        |  | Firecracker / gVisor         |   |
        |  +-----------+------------------+   |
        |              |                      |
        |  +-----------v------------------+   |
        |  | TRUST / ASSURANCE STORAGE    |   |
        |  | Audit / Provenance / Config   |   |
        |  +------------------------------+   |
        |                                    |
        |       CPU / RAM / GPU / NVMe       |
        +----------------+-------------------+
                         |
                 Explicitly allowed
                 enterprise paths
                         |
                  Enterprise Systems

                 X INTERNET EGRESS X
                 X PUBLIC DNS X
                 X CLOUD AI X
```

The physical deployment therefore preserves the architecture's strongest boundary:

> **trusted control plane → restricted processing → independently isolated execution**

---

# 6. Operating Environment

## 6.1 Host OS

**Target:** hardened Linux distribution.

Required characteristics:

- supported long-term kernel;
- security updates available through controlled offline mechanism;
- NVIDIA/accelerator driver support where applicable;
- namespaces/cgroups;
- firewall support;
- systemd or equivalent service supervision;
- encrypted storage capability;
- secure boot capability where deployment policy requires;
- audit subsystem;
- container/microVM support;
- local-only administrative capability.

Exact distribution remains a deployment qualification decision.

## 6.2 Host hardening

The host shall implement:

- least-privilege service accounts;
- disabled unnecessary services;
- restricted administrative access;
- encrypted persistent storage where required;
- protected model directories;
- protected audit/provenance directories;
- firewall default-deny policy;
- restricted DNS;
- controlled USB/removable-media policy;
- controlled update mechanism;
- host-level monitoring.

---

# 7. Process Boundary Architecture

The 24 architectural components do **not** become 24 processes.

The deployment uses five primary runtime classes.

| Runtime | Components | Boundary |
|---|---|---|
| Control runtime | Identity, policy, task, workflow, state, registry, routing | Trusted process |
| AI runtime | Inference gateway + model serving | Restricted process |
| Knowledge runtime | ingestion, parsing, retrieval, evidence | Restricted process group |
| Execution runtime | tools + processing workers | Restricted process group |
| High-assurance runtime | generated code / hostile execution | Firecracker or qualified equivalent |

This follows the component architecture's deliberate distinction between architectural ownership and physical deployment units. The project explicitly rejected unnecessary microservice fragmentation.

---

# 8. Control Plane Deployment

The trusted application process owns:

- identity;
- authorization;
- policy;
- task state;
- workflow state;
- execution state;
- capability registry;
- model routing;
- resource admission;
- approval;
- completion predicates;
- release state;
- audit event creation.

The agent runtime resides logically within this application but remains subordinate to control-plane authority.

### Critical rule

```text
Agent Proposal
      |
      v
Control Plane
      |
      +--> Authorization
      +--> Policy
      +--> Resource Admission
      +--> Verification Gate
      +--> Approval Gate
      |
      v
Execution
```

The model cannot bypass this sequence.

---

# 9. Data Plane Deployment

The data plane contains:

- document representations;
- OCR outputs;
- visual representations;
- P&ID structures;
- evidence;
- retrieval indexes;
- model inputs/outputs;
- tool results;
- artifacts;
- temporary processing data.

The data plane is **not authoritative over policy**.

This preserves the Phase 10 rule that model/data output cannot acquire control-plane authority.

---

# 10. AI Compute Architecture

## 10.1 GPU strategy

The reference system uses:

> **One GPU with approximately 48 GB VRAM as the initial qualification target.**

The GPU is treated as a scheduled shared resource rather than an unrestricted pool.

### Priority order

1. Active user-facing inference
2. Verification-critical inference
3. P&ID/VLM processing
4. Retrieval embeddings/reranking
5. Background ingestion
6. Non-critical batch processing

Background jobs must yield to interactive/critical workflows.

---

# 11. Model Residency Strategy

The system shall **not** attempt to keep every model permanently resident.

Initial strategy:

```text
Resident / preferred
--------------------
Primary LLM/VLM
        |
        v
One compact embedding/reranker capability
where memory permits

Dynamic
-------
Alternative LLM
Specialist VLM
OCR acceleration
Large embedding/reranker variants
Experimental models
```

The model router therefore considers:

- VRAM currently occupied;
- model load time;
- current workflow;
- expected next capability;
- context length;
- verification requirement;
- task priority;
- resource reservation.

### Model switching rule

A model switch is worthwhile only when:

> expected quality/verification benefit > switching cost + resource pressure.

This prevents the router from creating pathological model churn.

---

# 12. GPU Scheduling

The GPU resource manager shall maintain:

```text
GPU
 |
 +-- VRAM reservation
 |
 +-- active model
 |
 +-- KV/cache reservation
 |
 +-- inference workload
 |
 +-- queued workloads
 |
 +-- emergency headroom
```

The scheduler shall prevent a new workload from being admitted merely because the GPU appears available at the moment of request.

Admission must account for:

- current VRAM;
- expected peak VRAM;
- model loading;
- KV cache;
- multimodal image processing;
- concurrent processes;
- safety headroom.

---

# 13. Host CPU and RAM Allocation

Initial allocation policy:

| Workload | CPU | RAM | GPU | Priority |
|---|---|---|---|---|
| Control plane | Reserved | Reserved | No | Critical |
| Agent runtime | Reserved | Moderate | Indirect | High |
| Retrieval | Moderate | Moderate | Optional | High |
| Document processing | High burst | High | Optional | High |
| OCR | Moderate/high | Moderate | Optional | High |
| P&ID processing | High burst | High | High | High |
| Model serving | Moderate | Moderate | High | Critical |
| Verification | Moderate/high | Moderate | Optional | Critical |
| Sandbox | Capped | Capped | No by default | Medium |
| Audit/provenance | Low | Low/moderate | No | Critical |
| UI/API | Low | Low | No | High |

Exact numerical allocations remain benchmark outputs.

---

# 14. Resource Admission

Every expensive operation requires a resource request.

```text
Task
 |
 v
Resource Request
 |
 +-- CPU
 +-- RAM
 +-- GPU
 +-- VRAM
 +-- Storage
 +-- I/O
 +-- Sandbox
 |
 v
Admission Controller
 |
 +--> ACCEPT
 +--> QUEUE
 +--> DEGRADE
 +--> ESCALATE
 +--> REJECT
```

The agent cannot allocate unlimited resources.

### Backpressure

When resources are exhausted:

1. reject non-critical background work;
2. queue lower-priority work;
3. preserve active critical workflow;
4. prevent memory thrashing;
5. expose resource exhaustion explicitly.

Resource exhaustion must never become a security bypass.

---

# 15. Concurrency Model

The MVP shall support experimentally determined bounded concurrency.

Initial qualification modes:

### C1 — Single user / single task

**Mandatory.**

### C2 — Single user / multiple tasks

**Required validation.**

### C3 — Multiple users / concurrent tasks

**Required validation.**

### C4 — Concurrent document processing

**Required validation.**

### C5 — Concurrent sandbox execution

**Conditional.**

The system shall not advertise arbitrary concurrency.

The supported capacity is the highest tested operating point satisfying:

- workflow quality;
- security;
- verified completion;
- resource limits;
- acceptable latency;
- stability.

Phase 16 explicitly requires concurrency to be experimentally established.

---

# 16. Storage Architecture

## 16.1 Storage tiers

| Tier | Purpose | Persistence |
|---|---|---|
| OS volume | OS/runtime | Persistent |
| Model volume | Model weights/configuration | Persistent |
| Source vault | Original enterprise documents | Persistent |
| Evidence store | Governed evidence | Persistent |
| Index store | Search projections | Rebuildable |
| Execution store | Task/workflow state | Persistent |
| Artifact store | Generated outputs | Persistent |
| Provenance store | Lineage | Persistent |
| Audit store | Security/operational audit | Persistent |
| Cache | Derived temporary acceleration | Controlled |
| Processing workspace | Document/OCR intermediate data | Temporary |
| Sandbox workspace | Code execution | Ephemeral |
| Backup | Recovery copies | Separate/offline |

---

# 17. Storage Isolation

The following must never be treated as one unrestricted filesystem:

```text
CONTROL DATA
KNOWLEDGE DATA
MODEL DATA
TEMPORARY DATA
SANDBOX DATA
AUDIT DATA
BACKUP DATA
```

The application shall use separate paths, ownership and permissions.

Generated code receives only an ephemeral workspace.

Sandbox execution does not receive:

- host root filesystem;
- credentials;
- arbitrary persistent storage;
- control-plane database;
- audit database;
- model registry;
- network credentials.

---

# 18. Cache Architecture

Caching is security-sensitive.

Each cache entry must be bound, where applicable, to:

```text
task_scope
authorization_scope
source_revision
temporal_context
policy_version
representation_version
model_version
```

Required cache classes:

- model cache;
- KV/context cache;
- embedding cache;
- retrieval cache;
- OCR cache;
- document-processing cache;
- visual representation cache;
- artifact-generation cache.

### Cache invariant

> A cache entry cannot remain usable after the authorization or validity conditions governing its source have expired.

This directly follows the project's evidence-first and authorization-aware data architecture.

---

# 19. Network Topology

The reference host has three logical network classes.

## N1 — User/Enterprise interface

Permitted only to explicitly approved enterprise endpoints.

## N2 — Management interface

Restricted to administrators/operators.

## N3 — Update/import interface

Normally disconnected.

Used only during controlled update/import procedures.

### Internet

```text
DEFAULT: DENY
```

There is no general-purpose Internet route.

---

# 20. Zero-Egress Enforcement

Zero-egress shall be enforced in layers:

```text
Application policy
       ↓
Process restrictions
       ↓
Network namespace / socket controls
       ↓
Host firewall
       ↓
Enterprise firewall
       ↓
Physical/deployment boundary
```

The host must not depend solely on application behavior.

### Required prohibited paths

- public Internet;
- public DNS;
- public package repositories;
- cloud AI APIs;
- telemetry SaaS;
- model download endpoints;
- arbitrary proxy access;
- unrestricted outbound HTTP/HTTPS;
- unrestricted outbound DNS.

The Phase 15 architecture already establishes zero-egress as a structural control rather than an assumption based on an "offline" label.

---

# 21. DNS Architecture

Preferred MVP configuration:

```text
Application
    X
Public DNS

Application
    |
    v
Enterprise-controlled DNS
or
No DNS resolution
```

For a genuinely air-gapped deployment, external DNS is unnecessary and should be unavailable.

A failed DNS lookup must not cause fallback to public resolvers.

---

# 22. Model Deployment Security

Model serving shall have:

- read-only model access where practical;
- no credential access;
- no arbitrary process spawning;
- no unrestricted filesystem access;
- no unrestricted network access;
- version-pinned model configuration;
- recorded model identity;
- controlled model loading;
- controlled model replacement.

The inference runtime does not receive tool authority merely because it is local.

---

# 23. Document Processing Deployment

Potentially malicious documents are processed through:

```text
Upload
  ↓
Quarantine
  ↓
Validation
  ↓
Isolated Parser
  ↓
OCR / Vision
  ↓
Normalization
  ↓
Evidence Registration
  ↓
Knowledge Store
```

Document processors must not directly modify:

- policy;
- authorization;
- task state;
- security configuration;
- audit history.

The deployment must contain parser failures and resource exhaustion.

This is mandatory because the Phase 16 specification explicitly treats uploaded content as potentially hostile and requires isolated processing.

---

# 24. Sandbox Deployment

## Preferred boundary

**Firecracker-class microVM isolation.**

## Alternative

**gVisor-class sandbox**, subject to security qualification.

The sandbox receives:

- generated code;
- explicitly permitted input data;
- ephemeral workspace;
- bounded CPU/RAM/storage;
- explicitly defined network policy.

It does not receive:

- host credentials;
- arbitrary host filesystem;
- control database;
- audit database;
- model registry;
- administrative sockets.

### Lifecycle

```text
Generate
 ↓
Static validation
 ↓
Policy check
 ↓
Sandbox admission
 ↓
MicroVM creation
 ↓
Execute
 ↓
Observe
 ↓
Verify
 ↓
Collect result
 ↓
Destroy
```

---

# 25. Tool Runtime Deployment

Tools execute outside the model process.

```text
Agent
 ↓
Tool Request
 ↓
Authorization
 ↓
Policy
 ↓
Resource Admission
 ↓
Tool Runtime
 ↓
Execution Receipt
 ↓
Verification
```

Tools receive only the minimum data and permissions required for the operation.

---

# 26. Verification Deployment

Verification remains logically separate from generation.

Verification may combine:

- deterministic validation;
- schema validation;
- numerical validation;
- evidence validation;
- consistency checks;
- policy checks;
- artifact integrity checks;
- domain-specific validation;
- human review.

The deployment must preserve:

```text
GENERATED
   ↓
CHECKED
   ↓
VERIFIED
   ↓
HUMAN-APPROVED
```

A process returning exit code zero does not establish correctness.

---

# 27. Startup Architecture

Startup sequence:

```text
1. Host boot
2. Host security controls
3. Storage integrity
4. Network policy
5. Audit subsystem
6. Provenance subsystem
7. Configuration validation
8. Identity subsystem
9. Policy engine
10. Resource manager
11. Model/capability registry
12. Inference runtime
13. Knowledge/retrieval
14. Agent/workflow runtime
15. Tool runtime
16. Sandbox service
17. Verification
18. API
19. UI
```

The API/UI must not become operational before:

- security controls are active;
- policy is loaded;
- authorization is available;
- audit is operational;
- network controls are active.

This startup ordering is explicitly required by Phase 16.

---

# 28. Shutdown Architecture

Normal shutdown:

```text
Stop accepting new tasks
        ↓
Drain safe operations
        ↓
Checkpoint active executions
        ↓
Terminate sandbox workloads
        ↓
Terminate tool workloads
        ↓
Flush audit
        ↓
Persist provenance
        ↓
Persist state
        ↓
Clear temporary data
        ↓
Stop AI runtime
        ↓
Stop application
```

Forced shutdown must prioritize:

1. security;
2. state integrity;
3. audit integrity;
4. sandbox termination;
5. recovery information.

---

# 29. Failure Domains

| Failure | Containment | Recovery |
|---|---|---|
| GPU failure | AI workloads stop | Restart/fallback |
| Model crash | AI runtime | Reload model |
| Retrieval failure | Knowledge domain | Retry/rebuild index |
| Parser crash | Isolated worker | Restart worker |
| Sandbox crash | MicroVM boundary | Destroy/recreate |
| RAM exhaustion | Admission/backpressure | Recover/retry |
| VRAM exhaustion | Scheduler | Queue/evict/retry |
| Storage failure | Protected storage boundary | Restore/replace |
| Policy failure | Fail closed | Administrative recovery |
| Audit failure | Block critical execution | Restore audit |
| Network failure | Restrict affected integrations | Recover connectivity |
| Power failure | Persistent checkpoint | Resume/restart |
| Update failure | Quarantine/rollback | Restore prior version |

Phase 16 requires each failure domain to be evaluated for impact, containment, recovery, data loss, task loss, audit impact and security impact.

---

# 30. Recovery Architecture

A paused execution may resume only after re-evaluating:

```text
Identity
Authorization
Policy
Evidence validity
Document revision
Model/version availability
Tool availability
Resource availability
```

A checkpoint is **not** an authorization token.

A stale checkpoint cannot silently regain authority.

Side-effecting operations require:

```text
Idempotency Key
+
Execution Receipt
+
Authoritative State Transition
```

---

# 31. Backup and Restore

Back up:

### Mandatory

- configuration;
- policy;
- task state;
- execution state;
- evidence metadata;
- provenance;
- audit;
- artifact metadata.

### Conditional

- enterprise source documents;
- indexes;
- generated artifacts;
- model weights.

The backup policy must respect customer retention and classification requirements.

Backups shall be:

- integrity-protected;
- access-controlled;
- encrypted where required;
- sovereign;
- independently restorable;
- periodically restoration-tested.

---

# 32. Observability Deployment

Observability is divided into three classes.

## Operational telemetry

- CPU;
- RAM;
- GPU;
- VRAM;
- storage;
- I/O;
- latency;
- queues;
- failures.

## Security/audit

- authorization decisions;
- policy decisions;
- denied actions;
- security violations;
- network attempts;
- sandbox events;
- administrative actions.

## Provenance

- source;
- transformation;
- model;
- tool;
- evidence;
- claim;
- artifact.

These stores must not be collapsed merely because they are all "logs."

Telemetry itself must remain sovereign. Phase 16 explicitly requires operational telemetry to remain distinct from security/audit and provenance data.

---

# 33. Deployment Lifecycle

```text
PROVISION
   ↓
INSTALL
   ↓
CONFIGURE
   ↓
VERIFY
   ↓
INITIALIZE
   ↓
LOAD MODELS
   ↓
LOAD KNOWLEDGE
   ↓
VALIDATE
   ↓
OPERATE
   ↓
MONITOR
   ↓
UPDATE
   ↓
BACKUP
   ↓
RECOVER
   ↓
DECOMMISSION
```

Every transition requires:

- responsible actor;
- security conditions;
- validation;
- audit;
- rollback;
- failure behavior.

This lifecycle is directly mandated by Phase 16.

---

# 34. Offline Installation

The installation bundle shall contain:

- OS baseline;
- drivers;
- application binaries;
- Python/runtime dependencies;
- model artifacts;
- model metadata;
- configuration;
- policy;
- security configuration;
- certificates where required;
- trust roots;
- update metadata;
- integrity information.

No installation step may silently download dependencies.

---

# 35. Offline Update Architecture

```text
CONTROLLED BUILD ENVIRONMENT
          ↓
SBOM / provenance
          ↓
SIGNED PACKAGE
          ↓
CONTROLLED TRANSFER
          ↓
IMPORT QUARANTINE
          ↓
HASH / SIGNATURE CHECK
          ↓
MALWARE / SECURITY CHECK
          ↓
COMPATIBILITY CHECK
          ↓
ADMIN APPROVAL
          ↓
INSTALL
          ↓
HEALTH CHECK
          ↓
ACTIVATE
          ↓
VERIFY
          ↓
ROLLBACK IF REQUIRED
```

Update activation must not rely on model-generated approval.

---

# 36. Configuration Management

Configuration categories:

- system;
- security;
- model;
- knowledge;
- resource;
- network;
- tools;
- sandbox;
- update.

Each configuration version must have:

- identity;
- version;
- owner;
- validation state;
- approval state;
- timestamp;
- provenance;
- rollback path.

Security configuration is inaccessible to the agent.

---

# 37. Reference Resource Matrix

The following is the **deployment allocation model**, not measured consumption.

| Deployment Component | CPU | RAM | GPU | VRAM | Storage | Process | Isolation | Network | Criticality |
|---|---|---|---|---|---|---|---|---|---|
| Control plane | Reserved | Reserved | — | — | State SSD | App | Trusted | Enterprise | Critical |
| Agent runtime | Reserved | Moderate | Indirect | — | State | App | Trusted/restricted | Controlled | Critical |
| Inference | Moderate/high | Moderate | Primary | Primary | Models | Separate | Restricted | Internal only | Critical |
| Retrieval | Moderate | Moderate/high | Optional | Optional | Index | Separate/module | Restricted | Internal | Critical |
| Document processing | Burst | High | Optional | Optional | Temp | Worker | Isolated | None | High |
| OCR | Burst | Moderate | Optional | Optional | Temp | Worker | Isolated | None | High |
| P&ID processing | High | High | Primary | Primary | Temp/evidence | Worker | Restricted | None | Critical |
| Tool runtime | Burst | Capped | — | — | Temp | Worker | Restricted | Explicit | Critical |
| Sandbox | Capped | Capped | Default none | — | Ephemeral | MicroVM | Strong | Deny | Critical |
| Verification | Moderate/high | Moderate | Optional | Optional | Temp | App/worker | Restricted | None | Critical |
| Audit | Low | Moderate | — | — | Audit SSD | App/service | Trusted | Controlled | Critical |
| Provenance | Low/moderate | Moderate | — | — | Provenance SSD | App/service | Trusted | Controlled | Critical |
| UI/API | Low | Low | — | — | App | App | Trusted | Enterprise | High |

All numerical resource reservations require empirical qualification.

---

# 38. Workflow Resource Matrix

| Workflow | CPU Peak | RAM Peak | GPU Peak | VRAM Peak | Storage Peak | Duration | Concurrency | Main Risk | Verified Completion |
|---|---:|---:|---:|---:|---:|---|---|---|---|
| W3 Knowledge Investigation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Retrieval/model latency | Requires Validation |
| W1 Inspection Report | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | OCR/document processing | Requires Validation |
| W2 P&ID Analysis | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | VLM/topology processing | Requires Validation |
| W4 Artifact Generation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Verification/artifact quality | Requires Validation |
| W5 Code Analysis | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Requires Validation | Sandbox/resource pressure | Requires Validation |

No numerical value is fabricated.

Phase 16 explicitly requires unknown measurements to remain marked **Requires Validation**.

---

# 39. Workflow Performance Model

The primary performance measure is:

> **Verified useful work completed per unit time and resource.**

Not:

- tokens/sec;
- GPU utilization alone;
- isolated inference latency;
- model benchmark score.

For each workflow:

```text
Task submission
      ↓
Task setup
      ↓
Retrieval
      ↓
Document/OCR processing
      ↓
Model inference
      ↓
Agent execution
      ↓
Verification
      ↓
Artifact
      ↓
Provenance
      ↓
Audit
      ↓
Verified completion
```

The complete workflow must be measured.

Phase 16 explicitly rejects isolated token throughput as the primary performance measure.

---

# 40. Capacity Model

The initial deployment shall expose explicit limits for:

- maximum concurrent tasks;
- maximum documents per task;
- maximum document size;
- maximum pages;
- maximum image resolution;
- maximum active model workloads;
- maximum sandbox concurrency;
- maximum temporary storage;
- maximum evidence corpus size;
- maximum audit growth;
- maximum provenance growth.

These are **qualification parameters**, not arbitrary product promises.

---

# 41. Reference Deployment Acceptance Criteria

The deployment is accepted only if all applicable conditions pass.

### Installation

- reproducible installation;
- no uncontrolled downloads;
- integrity verified.

### Startup

- security controls active before workload exposure;
- audit operational;
- network policy active.

### Hardware

- reference hardware completes committed workflows.

### Performance

- complete workflows meet approved performance targets.

### Resource

- no unacceptable CPU/RAM/VRAM/storage exhaustion.

### Security

- trust boundaries are technically enforced.

### Sovereignty

- prohibited external communication is prevented **and demonstrated**.

### Reliability

- verified workflow completion and recovery satisfy approved thresholds.

### Storage

- capacity and lifecycle are adequate.

### Updates

- offline signed update works;
- rollback works.

### Recovery

- defined failure scenarios recover safely.

### Operations

- administrators can operate the system without violating confidentiality or sovereignty.

These acceptance categories are explicitly required by Phase 16.

---

# 42. End-to-End Qualification Protocol

## T01 — Clean installation

Verify:

- installation reproducibility;
- package integrity;
- dependency closure;
- no external access.

## T02 — Startup/shutdown

Verify security-first startup and controlled shutdown.

## T03 — Model loading

Measure:

- load time;
- peak VRAM;
- RAM;
- model switching;
- failure recovery.

## T04 — Knowledge ingestion

Measure:

- parsing;
- OCR;
- temporary storage;
- evidence construction.

## T05 — Retrieval

Test:

- authorization;
- revision;
- temporal filtering;
- relevance;
- evidence sufficiency.

## T06–T10 — W3/W1/W2/W4/W5

Run complete workflows.

## T11 — Concurrent workflows

Determine operating envelope.

## T12 — Resource exhaustion

Intentionally exhaust:

- VRAM;
- RAM;
- storage;
- CPU;
- sandbox capacity.

Verify safe rejection/backpressure.

## T13 — Component failure

Inject failures.

## T14 — Recovery

Verify checkpoint/recovery semantics.

## T15 — Malicious document

Test parser containment.

## T16 — Prompt injection

Test untrusted document instructions.

## T17 — Sandbox escape

Test filesystem, process, privilege and network escape.

## T18 — Unauthorized tool access

Verify denial.

## T19 — Unauthorized evidence access

Verify zero exposure.

## T20 — Zero-egress

Perform packet-level verification.

## T21 — Update

Install signed offline update.

## T22 — Rollback

Return to known-good state.

## T23 — Backup/restore

Restore task/evidence/audit/provenance state.

## T24 — Long-duration stability

Run sustained workloads.

The complete 24-test sequence follows the Phase 16 qualification specification.

---

# 43. Zero-Egress Verification

The test shall use both positive and negative controls.

### Positive controls

Verify explicitly permitted enterprise connections work.

### Negative controls

Attempt:

- HTTPS to public endpoint;
- HTTP to public endpoint;
- DNS lookup;
- direct IP connection;
- IPv6 egress;
- proxy use;
- alternate DNS;
- package-manager connection;
- model download;
- telemetry endpoint;
- sandbox outbound connection.

Expected result:

```text
BLOCKED
+
OBSERVED
+
AUDITED
```

A "no traffic observed during normal use" result is insufficient.

---

# 44. Deployment Security Matrix

| Boundary | Threat | Enforcement | Failure behavior |
|---|---|---|---|
| Host → Application | Host compromise | OS hardening | Stop |
| Application → Model | Prompt/tool abuse | Capability interface | Deny |
| Application → Knowledge | Unauthorized retrieval | Authorization-aware query | Deny |
| Document → Parser | Malicious document | Isolation | Quarantine/terminate |
| Agent → Tool | Privilege escalation | External policy | Deny |
| Agent → Sandbox | Code escape | MicroVM boundary | Terminate |
| Sandbox → Host | Escape | Kernel/VM boundary | Security failure |
| Application → Network | Egress | Host firewall | Block/audit |
| Update → System | Supply-chain compromise | Signatures/quarantine | Reject |
| Admin → Audit | Tampering | Protected audit storage | Alert/deny |

---

# 45. Deployment Dependency Order

```text
Host
 ↓
Security controls
 ↓
Storage
 ↓
Audit / provenance
 ↓
Identity
 ↓
Policy
 ↓
Resource manager
 ↓
Model registry
 ↓
Inference
 ↓
Knowledge
 ↓
Agent/workflow
 ↓
Tools
 ↓
Sandbox
 ↓
Verification
 ↓
API
 ↓
UI
```

Circular dependencies must not be introduced.

In particular:

> Audit must not depend on successful task completion.

> Policy must not depend on model availability.

> Authorization must not depend on retrieval.

> Security controls must not depend on the application behaving correctly.

---

# 46. Deployment Anti-Patterns Rejected

### Hardware chosen by VRAM alone

**Wrong:** VRAM does not measure workflow feasibility.

**Correction:** benchmark complete workflows.

### GPU chosen by tokens/sec

**Wrong:** ignores retrieval, OCR, verification, switching and artifacts.

**Correction:** measure verified useful work.

### Everything in one unrestricted process

**Wrong:** creates a common failure/security domain.

**Correction:** separate control, AI, processing and high-risk execution boundaries.

### Everything as microservices

**Wrong:** increases deployment and operational complexity without necessarily increasing security.

**Correction:** use logical modularity with selective process isolation.

### Air-gapped by assertion

**Wrong:** physical disconnection does not demonstrate all deployment paths.

**Correction:** enforce and test zero-egress.

### Shared caches

**Wrong:** creates cross-user/task leakage.

**Correction:** bind caches to authorization and validity context.

### Unlimited concurrency

**Wrong:** creates unpredictable GPU/RAM contention.

**Correction:** experimentally establish capacity.

### Immediate hardware upgrade

**Wrong:** may hide scheduling or architectural inefficiency.

**Correction:**

```text
Measure
 ↓
Identify bottleneck
 ↓
Remove unnecessary work
 ↓
Schedule
 ↓
Cache
 ↓
Route
 ↓
Optimize inference
 ↓
Only then upgrade hardware
```

This optimization order is explicitly prescribed by Phase 16.

---

# 47. Simplification Review

The reference deployment deliberately eliminates:

- Kubernetes;
- service mesh;
- distributed message bus;
- distributed database;
- separate retrieval server;
- separate provenance server;
- separate audit cluster;
- multiple inference nodes;
- external observability SaaS;
- cloud model APIs.

These are not rejected universally.

They are rejected **for the MVP because their demonstrated benefit does not yet justify their operational and security cost**.

The resulting deployment has:

```text
ONE HOST
 |
 +-- Control Application
 |
 +-- AI Runtime
 |
 +-- Knowledge/Processing Workers
 |
 +-- Retrieval/Stores
 |
 +-- Verification
 |
 +-- Audit/Provenance
 |
 +-- Isolated Sandbox
 |
 +-- Host Security / Network Enforcement
```

This is the minimum practical deployment shape currently justified by the architecture.

---

# 48. Hardware Feasibility Status

| Requirement | Reference target | Status |
|---|---|---|
| Single host | 1 host | **Established architectural decision** |
| Linux | Hardened Linux | Candidate |
| CPU | 16–32 core/thread class | Requires Validation |
| RAM | 128 GB ECC preferred | Requires Validation |
| GPU | 48 GB VRAM class | Requires Validation |
| GPU count | 1 | Preferred |
| Local model execution | Required | Architecture established |
| Model portfolio coexistence | Multiple local capabilities | Requires Validation |
| W3 | Required | Requires Validation |
| W1 | Required | Requires Validation |
| W2 | Required | Requires Validation |
| W4 | Required | Requires Validation |
| W5 | Conditional | Requires Validation |
| Concurrent operation | Bounded | Requires Validation |
| Sustained operation | Required | Requires Validation |
| Zero-egress | Host/network enforcement | Requires Deployment Test |
| Sandbox | Firecracker preferred | Requires Security Test |
| Recovery | Required | Requires Validation |

---

# 49. Deployment Risks

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| DEP-01 | 48 GB VRAM insufficient | High | Full workflow benchmark |
| DEP-02 | Model switching dominates latency | High | Residency/scheduling optimization |
| DEP-03 | P&ID workload overwhelms GPU | High | Dedicated workload profiling |
| DEP-04 | Document processing saturates CPU/RAM | High | Worker quotas/backpressure |
| DEP-05 | Sandbox overhead excessive | Medium | Benchmark Firecracker/gVisor |
| DEP-06 | Storage growth underestimated | High | Capacity model |
| DEP-07 | Audit/provenance growth excessive | Medium | Retention/capacity policy |
| DEP-08 | Concurrent users cause contention | High | Admission control |
| DEP-09 | Host network path bypass | Critical | Independent egress testing |
| DEP-10 | Update process compromises sovereignty | Critical | Offline signed lifecycle |
| DEP-11 | Recovery resumes stale authorization | Critical | Mandatory reauthorization |
| DEP-12 | Thermal throttling | Medium | Sustained-load testing |

---

# 50. Open Questions

### DEP-OQ-01
Does the selected 48 GB-class GPU provide adequate VRAM headroom for the validated model portfolio?

### DEP-OQ-02
Should the primary model remain resident continuously?

### DEP-OQ-03
What is the measured cost of switching between LLM/VLM configurations?

### DEP-OQ-04
What maximum context sizes are operationally useful rather than merely technically supported?

### DEP-OQ-05
What is the maximum supported concurrent workflow count?

### DEP-OQ-06
Is 128 GB RAM sufficient for the largest representative document corpus and processing workload?

### DEP-OQ-07
Does P&ID processing require persistent GPU residency?

### DEP-OQ-08
Does OCR materially benefit from GPU acceleration on the reference deployment?

### DEP-OQ-09
Does Firecracker overhead justify its stronger boundary compared with gVisor?

### DEP-OQ-10
What storage growth rate results from evidence, provenance and audit retention?

### DEP-OQ-11
What customer-specific network topology is required for enterprise integration?

### DEP-OQ-12
What deployment hardening baseline is required for the first target customer?

---

# 51. Required Technical Spikes

Only the following spikes materially reduce deployment uncertainty.

## DEP-S01 — Full GPU qualification

Test:

- LLM;
- VLM;
- embedding;
- reranker;
- model switching;
- context length;
- KV cache;
- concurrency.

## DEP-S02 — Full W3 benchmark

Measure complete knowledge-investigation workflow.

## DEP-S03 — Full W1 benchmark

Measure document/OCR/report workflow.

## DEP-S04 — Full W2 benchmark

Measure P&ID/drawing workflow.

## DEP-S05 — Full W4 benchmark

Measure evidence → reasoning → artifact → verification.

## DEP-S06 — Resource contention

Run mixed workloads simultaneously.

## DEP-S07 — Sandbox qualification

Compare Firecracker and gVisor under security and performance tests.

## DEP-S08 — Zero-egress qualification

Perform packet-level adversarial testing.

## DEP-S09 — Recovery qualification

Test GPU, storage, process, power and network failures.

## DEP-S10 — Sustained deployment qualification

Run long-duration mixed workflows and measure thermal/resource degradation.

---

# 52. Deployment Decision Register

| Decision | Status |
|---|---|
| Single-node MVP | **Frozen** |
| Single Linux host | **Preferred** |
| One-GPU reference topology | **Preferred** |
| 48 GB VRAM-class reference target | **Candidate / Requires Validation** |
| 128 GB RAM target | **Candidate / Requires Validation** |
| Modular process boundaries | **Frozen** |
| Control/data separation | **Frozen** |
| Separate high-risk sandbox | **Frozen** |
| Firecracker | **Preferred / Requires Validation** |
| gVisor | Strong alternative |
| Host firewall | **Mandatory** |
| Zero-egress | **Mandatory** |
| Offline model lifecycle | **Mandatory** |
| Local audit/provenance | **Frozen** |
| Bounded concurrency | **Frozen** |
| Exact concurrency limit | **Requires Validation** |
| Exact hardware SKU | **Deferred** |
| Multi-node deployment | **Deferred** |
| Kubernetes | **Rejected for MVP** |
| Distributed inference | **Deferred** |
| Cloud AI dependency | **Rejected** |

---

# 53. Final Readiness Assessment

## Established

The following are architecturally established:

- single-node reference deployment;
- control/data-plane placement;
- selective process isolation;
- GPU scheduling model;
- resource admission;
- storage domains;
- cache isolation principle;
- network topology;
- zero-egress enforcement architecture;
- sandbox placement;
- malicious-document isolation;
- startup/shutdown order;
- failure-domain model;
- recovery model;
- offline update path;
- observability placement;
- workflow-level benchmark methodology.

## Requires Validation

The following cannot responsibly be declared established yet:

- exact GPU SKU;
- exact VRAM sufficiency;
- exact RAM requirement;
- exact CPU requirement;
- model residency;
- model-switching cost;
- concurrent workflow capacity;
- W3/W1/W2/W4 performance;
- W5 feasibility;
- sustained thermal behavior;
- sandbox performance/security;
- complete zero-egress qualification;
- recovery performance.

## Deployment blockers

There is currently **no conceptual deployment blocker**.

However, the reference deployment cannot be commercially declared qualified until:

1. complete MVP workflows run successfully;
2. hardware/resource envelopes are measured;
3. security boundaries pass adversarial testing;
4. zero-egress is demonstrated;
5. recovery is demonstrated;
6. sustained operation passes;
7. supported capacity is explicitly bounded.

---

# 54. Final Decision

# REFERENCE DEPLOYMENT READY WITH CONDITIONS

The architecture is sufficiently concrete to begin implementation and technical spikes.

It is **not yet evidence-backed enough to claim production hardware feasibility**.

The correct next step is therefore not another architecture phase.

It is empirical deployment qualification:

```text
REFERENCE HARDWARE
       ↓
RUNTIME INSTALLATION
       ↓
COMPONENT INTEGRATION
       ↓
RESOURCE MEASUREMENT
       ↓
W3 / W1 / W2 / W4
       ↓
W5 WHERE APPLICABLE
       ↓
CONCURRENCY
       ↓
SECURITY
       ↓
ZERO-EGRESS
       ↓
RECOVERY
       ↓
SUSTAINED LOAD
       ↓
CAPACITY ENVELOPE
       ↓
SUPPORTED DEPLOYMENT
```

The governing acceptance principle remains:

> **The deployment is accepted only when the complete verified workflow operates inside the defined security, sovereignty, resource, reliability and quality boundaries.**

This is the central Phase 16 decision.

---

# 55. Phase 17 Handoff

Phase 16 hands forward a concrete deployment target and qualification envelope.

Phase 17 should therefore focus on:

1. **Technical Spike Implementation**
2. **Reference Hardware Benchmarking**
3. **Model Portfolio Qualification**
4. **Inference Runtime Qualification**
5. **Document/OCR/P&ID Qualification**
6. **Retrieval Qualification**
7. **Agent Runtime Qualification**
8. **Sandbox Security Qualification**
9. **End-to-End Workflow Benchmarking**
10. **Zero-Egress Qualification**
11. **Failure/Recovery Qualification**
12. **Deployment Hardening**
13. **Measured Capacity Envelope**
14. **Evidence-backed Reference Configuration**

Phase 17 should **not reopen the product definition or redesign the approved architecture** unless measured evidence demonstrates a documented reversal condition.

# Phase 16 Gate

**REFERENCE DEPLOYMENT READY WITH CONDITIONS**

**Primary unresolved dependency:** empirical validation of the complete reference deployment under realistic workload, resource contention, security attack, sovereignty and recovery conditions.