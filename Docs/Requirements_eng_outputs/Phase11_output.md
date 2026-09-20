# SOVEREIGN AGENTIC AI WORKBENCH

# ARCHITECTURE DECISION & TECHNOLOGY SELECTION

**Phase:** 11  
**Predecessors:** Phase 8 — PRD; Phase 9 — SRS; Phase 10 — System Architecture  
**Successor:** Phase 12 — Component Architecture  
**Primary product:** Sovereign Enterprise AI Workbench / Agentic Knowledge-Work Execution Environment

---

# 1. Executive Decision

## Phase 11 status

# **TECHNOLOGY BASELINE ESTABLISHED WITH TARGETED VALIDATION REQUIRED**

The research establishes a defensible technology direction, but **the project must not yet claim that every component is production-selected**.

The most important decisions are:

| Architecture role | Current decision |
|---|---|
| Backend/API | **FastAPI — Preferred** |
| Primary model-serving engine | **vLLM — Preferred, validation required** |
| Secondary/local compatibility inference | **llama.cpp — Strong Candidate / compatibility path** |
| Primary compact multimodal model family | **Qwen3.5 — Preferred candidate, validation required** |
| Retrieval embedding family | **Qwen3-Embedding — Preferred candidate, validation required** |
| Reranking | **Qwen3-Reranker — Preferred candidate, validation required** |
| Document intelligence | **Docling — Preferred, validation required** |
| Specialized OCR/layout | **PaddleOCR / PP-StructureV3 — Strong Candidate, validation required** |
| Agent runtime | **LangGraph — Preferred, validation required** |
| Durable workflow engine | **Do not introduce for MVP unless spike proves necessity** |
| Search/vector layer | **Hybrid retrieval architecture; Qdrant — Strong Candidate, validation required** |
| Primary transactional state | **SQLite — Preferred MVP candidate; concurrency validation required** |
| Sandbox | **Firecracker — Preferred for high-assurance code boundary; gVisor — Strong Candidate for lower-overhead path** |
| Observability protocol | **OpenTelemetry — Preferred** |
| Frontend | **React/TypeScript — Preferred** |
| Network enforcement | **Host-level firewall/network namespace mechanism — technology selection remains validation-bound** |
| Provenance | **Application-owned provenance model; storage technology not delegated to a vendor** |
| Audit | **Application-owned immutable/correlation-aware audit model** |
| Artifact generation | **Programmatic deterministic generation + independent validation** |
| Deployment | **Single Linux workstation/server; controlled processes/isolated execution domains** |

No model, sandbox, retrieval engine, or inference engine is marked **fully selected** where hardware, security, or workflow validation remains outstanding.

This follows the Phase 11 rule that a technology must not be marked fully selected when critical validation remains.

---

# 2. Source of Truth

The technology-selection hierarchy is:

1. Final PRD
2. Final SRS
3. Phase 10 System Architecture
4. Existing research
5. Primary technical documentation
6. Research papers / benchmarks
7. Standards and government documentation
8. Reproducible technical evaluations
9. Independent engineering analysis
10. Vendor documentation
11. Community discussion

This is explicitly required by the Phase 11 methodology.

Vendor claims are therefore treated as **evidence about capability**, not as independent proof of suitability.

---

# 3. Technology Selection Principles

## 3.1 Architecture before technology

The question is not:

> Which technology is best?

It is:

> Which technology best satisfies the specific architecture contract under the project's sovereignty, security, hardware, reliability and verification constraints?

## 3.2 Hard constraints precede scoring

A candidate that violates a hard constraint is rejected regardless of its benchmark score.

Hard constraints include:

- offline operation;
- no mandatory cloud dependency;
- no mandatory external API;
- compatible licensing;
- required modality;
- architecture compatibility;
- required security boundary;
- feasible deployment model;
- ability to satisfy the relevant trust boundary.

The Phase 11 specification explicitly separates hard constraints from weighted criteria.

## 3.3 End-to-end performance dominates component performance

A model with excellent benchmark scores can still be rejected if:

- its inference engine consumes excessive VRAM;
- model switching destroys latency;
- retrieval quality is poor;
- tool calling is unreliable;
- verification becomes too expensive;
- the combined stack cannot operate on the target workstation.

## 3.4 Security failures dominate numerical optimization

A 10% performance advantage cannot compensate for:

- sandbox escape;
- unauthorized retrieval;
- credential exposure;
- policy bypass;
- prohibited egress;
- cross-user leakage;
- agent self-authorization.

The supplied security thresholds explicitly make these zero-tolerance properties.

---

# 4. Architecture-to-Technology Mapping

The Phase 10 architecture establishes the following technology roles:

```text
                    SOVEREIGN AI WORKBENCH
                              |
             +----------------+----------------+
             |                                 |
        CONTROL PLANE                      DATA PLANE
             |                                 |
       Task / Policy /                  Knowledge / Evidence
       Authorization                    Documents / Models
             |                                 |
             +---------------+-----------------+
                             |
                        Agent Runtime
                             |
                       AI Capabilities
                             |
                     Inference Runtime
                             |
                       Tool Boundary
                       /            \
                    Tools         Sandbox
                                    |
                              Code Execution
                                    |
                               Verification
                              /            \
                         Artifact       Provenance
                              \            /
                                  Audit
```

The technology baseline must preserve this architecture rather than collapse it into a model-centric application.

---

# 5. Candidate Evaluation Method

Every candidate is evaluated in this order:

```text
Architecture Role
       ↓
Capability Contract
       ↓
Hard Constraints
       ↓
Candidate Generation
       ↓
Early Elimination
       ↓
Evidence Review
       ↓
Component Evaluation
       ↓
Combination Evaluation
       ↓
Security Evaluation
       ↓
Hardware Evaluation
       ↓
Workflow Evaluation
       ↓
Decision
       ↓
Reversal Conditions
```

The project therefore deliberately avoids selecting an entire stack in one pass.

---

# 6. Decision Status Definitions

### SELECTED

Empirically validated and suitable for the relevant MVP role.

### PREFERRED — VALIDATION REQUIRED

Best current candidate, but one or more critical validation activities remain.

### STRONG CANDIDATE

Good fit but not currently the leading choice.

### REQUIRES VALIDATION

Evidence is insufficient to rank the candidate responsibly.

### DEFERRED

Not required for MVP.

### REJECTED

Fails a requirement or is inferior after meaningful comparison.

### OPEN QUESTION

Insufficient evidence to decide.

---

# 7. LLM SELECTION

## 7.1 Capability contract

The primary LLM must support:

- task understanding;
- enterprise technical language;
- evidence-grounded synthesis;
- structured output;
- planning;
- bounded tool use;
- correction;
- abstention;
- long-context processing;
- code assistance where required;
- local operation;
- resource-aware inference.

The LLM is **not** the system authority.

---

## 7.2 Candidate classes

The serious MVP candidates are:

1. Qwen3.5 dense models
2. Llama 4 Scout
3. Mistral Small family
4. Qwen3 family as fallback/compatibility candidate

### Early elimination

Very large models are not automatically disqualified by model quality, but models whose practical deployment requires hardware materially beyond the single-node MVP envelope are not acceptable as the primary MVP model.

For example, Llama 4 Scout has 17B active parameters but approximately 109B total parameters and its official deployment material describes single-H100-class deployment for its BF16 form, with int4 quantization enabling the single-H100 case. 

That makes it a useful research candidate but **not evidence for mid-range-GPU feasibility**.

Mistral Small 3.2 is also technically credible, but its official model card reports approximately 55 GB GPU memory for BF16/FP16 operation and recommends multi-GPU vLLM serving in the documented configuration. 

This creates an immediate MVP hardware concern.

---

## 7.3 Qwen3.5

Qwen3.5 is currently the strongest model-family candidate because it provides a useful combination of:

- open weights;
- Apache 2.0 licensing for the 9B model;
- native vision-language capability;
- text reasoning;
- tool use;
- long context;
- multiple model sizes;
- local serving support.

The official Qwen3.5-9B model card reports 9B parameters, native vision capability, 262,144-token native context, and compatibility with vLLM, SGLang, KTransformers and Transformers. 

Its published benchmark results include:

- MMMU: 78.4
- MMMU-Pro: 70.1
- MathVision: 78.9
- OmniDocBench 1.5: 87.7
- OCRBench: 89.2
- AI2D: 90.2
- TIR-Bench: 45.6/31.9

These are **vendor/model-card results**, not project validation.

### Decision

**Qwen3.5-9B — PREFERRED, VALIDATION REQUIRED**

### Why

It is unusually well aligned with the project's desire for:

- compact local multimodal capability;
- tool use;
- technical reasoning;
- one model family spanning text and vision;
- Apache 2.0 licensing;
- multiple serving options.

### Critical reservation

The architecture must not become dependent on Qwen3.5 specifically.

The capability abstraction remains mandatory.

---

# 8. VLM SELECTION

## Decision

The project should initially test **Qwen3.5-9B and Qwen3.5-4B** as the primary VLM candidates.

Qwen3.5-4B is particularly attractive for preprocessing or low-cost multimodal tasks because the model card identifies it as a 4B vision-language model with 262K native context and local serving support. 

### Proposed division

```text
                    MULTIMODAL TASK
                          |
              +-----------+-----------+
              |                       |
        Lightweight task          Complex task
              |                       |
        Qwen3.5-4B             Qwen3.5-9B
              |                       |
              +-----------+-----------+
                          |
                      Verification
```

### Critical rule

Neither model becomes authoritative for P&ID interpretation.

The architecture established earlier remains:

```text
Image
 ↓
Visual observations
 ↓
OCR / layout
 ↓
Entity extraction
 ↓
Spatial relations
 ↓
Connectivity/topology
 ↓
Engineering representation
 ↓
Domain interpretation
 ↓
Verification
 ↓
Human engineering authority
```

---

# 9. EMBEDDING MODEL

## Candidate set

1. Qwen3-Embedding-0.6B
2. Qwen3-Embedding-4B
3. Qwen3-Embedding-8B
4. BGE-M3
5. Jina multilingual embedding alternatives

## Qwen3-Embedding

The Qwen3 embedding family provides 0.6B, 4B and 8B variants, supports 100+ languages and supports flexible embedding dimensions. 

The model card reports:

| Model | Parameters | Context | Max dimension |
|---|---:|---:|---:|
| Qwen3-Embedding-0.6B | 0.6B | 32K | 1024 |
| Qwen3-Embedding-4B | 4B | 32K | 2560 |
| Qwen3-Embedding-8B | 8B | 32K | 4096 |

The 0.6B model is especially interesting because it materially reduces resource pressure.

### Decision

**Qwen3-Embedding-0.6B — PREFERRED, VALIDATION REQUIRED**

### Rationale

The architecture requires retrieval quality but does not require the embedding model itself to perform sophisticated reasoning.

Therefore:

> Use the smallest embedding model that passes the project retrieval benchmark.

The 4B and 8B versions remain escalation candidates if domain evaluation demonstrates a material retrieval advantage.

---

# 10. RERANKER

## Candidate

**Qwen3-Reranker-0.6B**

The Qwen3 family also provides 0.6B, 4B and 8B rerankers, with the model card reporting strong retrieval benchmark performance across multilingual and code retrieval evaluations. 

### Decision

**Qwen3-Reranker-0.6B — PREFERRED, VALIDATION REQUIRED**

### Architecture role

```text
Query
 ↓
Authorization filter
 ↓
Lexical retrieval
+
Dense retrieval
 ↓
Candidate fusion
 ↓
Reranker
 ↓
Authority/revision/temporal filtering
 ↓
Evidence sufficiency
```

The reranker is not allowed to override:

- authorization;
- authority;
- revision;
- temporal validity.

Semantic relevance is subordinate to evidence governance.

---

# 11. INFERENCE ENGINE

## Candidate classes

1. vLLM
2. SGLang
3. llama.cpp
4. Transformers serving

## Selection criteria

Hard:

- local operation;
- target hardware support;
- required model compatibility;
- offline operation;
- no mandatory cloud service;
- structured output;
- tool calling;
- multimodal support where required.

Soft:

- latency;
- throughput;
- batching;
- memory efficiency;
- model switching;
- observability;
- operational simplicity.

---

## 11.1 vLLM

vLLM currently provides:

- local/offline inference;
- OpenAI-compatible APIs;
- structured outputs;
- tool calling;
- continuous batching;
- prefix caching;
- multiple quantization formats;
- multimodal model support;
- embedding and scoring APIs;
- broad hardware support.

Its current documentation also explicitly describes offline inference and local model execution. 

The latest release evidence reviewed for this phase identifies **v0.28.0**, released August 26, 2026, with continued Qwen3.5 support, multimodal support, quantization support, KV-cache improvements and serving features. 

### Decision

# **vLLM — PREFERRED, VALIDATION REQUIRED**

### Reason

It currently provides the strongest architectural fit for a common serving abstraction across:

- LLM;
- VLM;
- embedding;
- reranking/scoring;
- structured output;
- tool calling.

### Critical limitation

vLLM's breadth does not prove that the selected model portfolio can coexist within the target workstation.

That requires the hardware spike.

---

# 12. llama.cpp

llama.cpp remains strategically valuable because it provides:

- broad local inference;
- GGUF support;
- CPU/GPU heterogeneous execution;
- low-level deployment flexibility;
- a useful compatibility/fallback path.

### Decision

**llama.cpp — STRONG CANDIDATE**

It should not be the primary serving layer initially unless the hardware benchmark demonstrates that its lower-level control provides a material advantage for the target deployment.

---

# 13. SGLang

SGLang remains a serious alternative.

However, the architecture does not currently have sufficient evidence that its additional serving capabilities justify introducing another primary serving substrate.

### Decision

**SGLang — STRONG CANDIDATE / REQUIRES VALIDATION**

It becomes preferred only if benchmark evidence demonstrates a meaningful advantage on:

- Qwen3.5;
- target GPU;
- tool-calling workloads;
- multimodal workloads;
- model switching;
- latency/resource contention.

---

# 14. INFERENCE ENGINE DECISION

```text
vLLM
  |
  +-- Primary candidate
  |
  +-- LLM
  +-- VLM
  +-- Embedding
  +-- Reranking
  +-- Structured output
  +-- Tool calling

llama.cpp
  |
  +-- Compatibility / fallback candidate

SGLang
  |
  +-- Performance challenger
```

### Current decision

**vLLM — PREFERRED**

but **not frozen until the actual model portfolio passes hardware and workflow testing.**

---

# 15. DOCUMENT INTELLIGENCE

## Candidate classes

1. Docling
2. PaddleOCR / PP-StructureV3
3. PyMuPDF + custom extraction
4. Unstructured
5. specialised format-specific parsers

---

# 16. Docling

Docling provides a unified document representation and supports formats including PDF, DOCX, PPTX, XLSX and images. Its current documentation also supports local conversion and offline model artifacts. 

Its architecture is particularly compatible with the project because it preserves more than raw text:

- layout;
- tables;
- document structure;
- page information;
- images;
- structured representations.

### Decision

# **Docling — PREFERRED, VALIDATION REQUIRED**

### Why

It maps closely to the project's evidence-first document architecture.

The project does not merely need:

> PDF → text

It needs:

> source → structured representation → evidence → provenance.

Docling is therefore a better architectural fit than a simple text extractor.

---

# 17. PaddleOCR / PP-StructureV3

PP-StructureV3 provides:

- layout detection;
- OCR;
- table recognition;
- formula recognition;
- chart parsing;
- reading-order recovery;
- local inference;
- CPU/GPU execution;
- configurable lightweight and high-accuracy models.

The official documentation explicitly describes its modular pipeline and local Paddle inference. 

### Decision

**PaddleOCR / PP-StructureV3 — STRONG CANDIDATE**

### Recommended role

Do not replace Docling wholesale.

Instead:

```text
                 DOCUMENT
                    |
                 Docling
                    |
          +---------+---------+
          |                   |
       Native             Scanned
       structure              |
          |               PaddleOCR
          |                   |
          +---------+---------+
                    |
               Evidence Layer
```

This reduces unnecessary coupling between parsing and OCR.

---

# 18. DOCUMENT ARCHITECTURE DECISION

### Preferred

**Docling + specialized OCR/layout capability**

### Rejected

A single universal document parser that is expected to solve:

- native PDFs;
- scanned PDFs;
- tables;
- engineering drawings;
- P&IDs;
- OCR;
- semantic interpretation.

The architecture explicitly requires capability decomposition.

---

# 19. RETRIEVAL / SEARCH

## Required capability

The search layer must support:

- lexical retrieval;
- semantic retrieval;
- metadata filtering;
- authorization filtering;
- revision filtering;
- temporal filtering;
- hybrid retrieval;
- reranking;
- deletion;
- update;
- provenance;
- offline deployment.

The Phase 11 specification explicitly requires evaluating the complete retrieval workflow rather than generic vector search.

---

# 20. Qdrant

Qdrant currently supports:

- payload filtering;
- hybrid queries;
- dense and sparse representations;
- multi-stage retrieval;
- reranking;
- local/self-hosted deployment.

Its documentation specifically describes hybrid dense+sparse retrieval and payload filtering. 

### Security reservation

The Qdrant production checklist states that self-hosted instances require deliberate authentication/network hardening and should not simply be exposed by default. 

That is compatible with the project's architecture, provided Qdrant is **inside the sovereign boundary** and never becomes the authorization authority.

### Decision

**Qdrant — STRONG CANDIDATE, VALIDATION REQUIRED**

---

# 21. Search Architecture Decision

The project should not define itself as:

> Qdrant-based knowledge system.

It should define itself as:

> Governed evidence architecture with search projections.

Preferred:

```text
                SOURCE
                  |
             EVIDENCE VAULT
                  |
        +---------+---------+
        |         |         |
     Lexical   Dense     Structural
        |         |         |
        +---------+---------+
                  |
              Fusion
                  |
              Reranker
                  |
        Authority/Revision
        Authorization
        Temporal Filtering
                  |
          Evidence Sufficiency
```

Qdrant is therefore an implementation candidate for one layer of this architecture, not the architectural identity.

---

# 22. AGENT RUNTIME

## Candidates

1. LangGraph
2. custom state-machine runtime
3. Semantic Kernel Process Framework
4. Temporal

---

# 23. Custom Runtime

A custom state machine has maximum control.

Advantages:

- no framework authority;
- exact state semantics;
- minimal dependency;
- direct security integration.

Disadvantages:

- substantial engineering effort;
- durability;
- interrupt/resume;
- observability;
- debugging;
- workflow evolution;
- retry semantics.

### Decision

**Strong architectural fallback, not preferred implementation initially.**

---

# 24. LangGraph

LangGraph currently provides:

- stateful agent execution;
- persistence/checkpointing;
- human-in-the-loop interrupts;
- durable execution;
- recovery;
- state inspection;
- conditional workflows.

Its documentation explicitly describes persisted graph state, human interrupts and checkpoint-based recovery. 

### Important security observation

LangGraph cannot become the authority plane.

The project architecture requires:

```text
LangGraph
   |
   | proposal / workflow execution
   v
Authoritative Control Domain
   |
   +-- authorization
   +-- policy
   +-- resource admission
   +-- verification
   +-- approval
```

### Decision

# **LangGraph — PREFERRED, VALIDATION REQUIRED**

The framework is useful because the project's workflow semantics are already graph/state-machine-like.

---

# 25. Temporal

Temporal provides substantially stronger durable workflow infrastructure, including self-hosted operation, event history and durable timers. 

However, for the MVP it introduces:

- another control/persistence system;
- additional operational infrastructure;
- additional deployment complexity;
- potentially unnecessary distributed workflow machinery.

### Decision

**Temporal — DEFERRED FOR MVP**

It should be reconsidered if:

- workflows become very long-lived;
- human approvals routinely persist for days/months;
- multi-node execution becomes necessary;
- recovery requirements exceed the capabilities of the local runtime.

---

# 26. AGENT DECISION

# **LangGraph + external authoritative control**

Not:

> LangGraph controls the system.

Instead:

> LangGraph executes bounded workflow logic inside an externally governed control architecture.

This preserves the Phase 10 authority boundary.

---

# 27. SANDBOX

This is one of the most security-critical Phase 11 decisions.

## Candidates

1. Firecracker
2. gVisor
3. hardened containers
4. Docker/container runtime alone
5. native process isolation

---

# 28. Docker-only

### Rejection

**REJECTED**

Reason:

The project explicitly treats generated code as untrusted and requires an independent execution boundary.

A conventional container alone does not provide sufficient architectural assurance for the project's stated security target.

---

# 29. gVisor

gVisor provides an application-kernel isolation model and intercepts application system calls rather than simply exposing the host kernel directly. Its documentation describes defense-in-depth using the Sentry, restricted host system calls, namespaces, seccomp and cgroups. 

Advantages:

- strong isolation relative to ordinary containers;
- OCI compatibility;
- lower fixed resource overhead than a conventional VM;
- existing container ecosystem integration.

Limitations:

- compatibility constraints;
- performance overhead;
- still requires external network policy;
- still requires host resource controls.

### Decision

**gVisor — STRONG CANDIDATE**

---

# 30. Firecracker

Firecracker provides microVM isolation based on KVM with:

- minimal device model;
- process isolation;
- seccomp;
- namespaces;
- cgroups;
- Jailer;
- resource controls;
- network namespaces;
- VM boundary.

Its official documentation explicitly states that the guest is treated as potentially malicious and recommends Jailer, cgroups and host-level network filtering. 

This is highly compatible with the project's threat model.

### Critical limitation

Firecracker itself does **not** perform network traffic filtering; host-level filtering remains necessary. 

### Decision

# **Firecracker — PREFERRED FOR HIGH-ASSURANCE CODE EXECUTION, VALIDATION REQUIRED**

---

# 31. Sandbox Decision

The current architecture should support:

```text
              CODE
                |
          Policy Analysis
                |
          Sandbox Admission
                |
        +-------+-------+
        |               |
     gVisor         Firecracker
        |               |
   Lower overhead   Higher isolation
        |               |
        +-------+-------+
                |
           Verification
```

### MVP recommendation

Run the technical spike against both.

If the security target can be met with gVisor and its performance advantage is material:

> gVisor may become the MVP default.

If the assurance requirement dominates:

> Firecracker becomes the default.

No final security decision should be made from documentation alone.

The supplied security threshold requires **zero successful sandbox escapes**, zero prohibited network access and zero credential access.

---

# 32. STORAGE

The architecture intentionally separates responsibilities.

## 32.1 SQLite

SQLite is attractive for MVP task/control metadata because it is:

- embedded;
- serverless;
- transactional;
- single-file;
- zero-configuration;
- self-contained;
- highly tested.

Its official documentation describes ACID transactions, zero configuration and a self-contained serverless architecture. 

### Decision

**SQLite — PREFERRED FOR MVP CONTROL/LOCAL METADATA**

Use for:

- task state;
- workflow state;
- configuration metadata;
- execution records;
- local indexes where appropriate;
- checkpoint metadata.

### Limitation

SQLite should not automatically become the storage system for:

- huge document corpora;
- large vector indexes;
- massive audit archives;
- model weights.

---

# 33. Object/File Storage

The MVP should use a local filesystem/object abstraction for:

- original documents;
- processed document representations;
- artifacts;
- model files;
- sandbox images;
- update bundles.

The abstraction should permit later migration to a dedicated object store.

---

# 34. Provenance Storage

Do not select a generic provenance database merely because one exists.

The architecture requires a project-owned provenance model.

Minimum conceptual graph:

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

Storage technology is subordinate to this model.

### Decision

**Application-owned provenance schema — SELECTED ARCHITECTURAL PRINCIPLE**

Physical storage:

**Requires Validation**

---

# 35. AUDIT

Audit and provenance remain separate.

Audit answers:

> What happened?

Provenance answers:

> Where did this output come from?

Observability answers:

> Is the system operating correctly?

The Phase 10 architecture explicitly separates these concerns.

### Decision

**Application-owned audit event model — PREFERRED**

Do not outsource security truth to a generic log platform.

---

# 36. OBSERVABILITY

## Candidate

**OpenTelemetry**

OpenTelemetry provides a vendor-neutral collection model for:

- traces;
- metrics;
- logs.

Its Collector can run locally and can receive/process/export telemetry through configurable pipelines. 

### Decision

# **OpenTelemetry — PREFERRED**

Use it for operational telemetry.

Do not use it as the sole authoritative security audit.

---

# 37. BACKEND

## Candidates

- FastAPI
- Django
- Go HTTP stack
- custom Python service stack

FastAPI is based on Python type hints and provides OpenAPI/JSON Schema integration. 

### Why FastAPI fits

The system has substantial Python-native requirements:

- AI models;
- document processing;
- retrieval;
- orchestration;
- evaluation;
- GPU tooling.

FastAPI minimizes impedance between the AI/application layer and the API layer.

### Decision

# **FastAPI — PREFERRED**

This is a lower-risk decision than the model/runtime decisions and can be frozen earlier.

---

# 38. FRONTEND

## Decision

**React + TypeScript — PREFERRED**

The UI must expose:

- task state;
- execution trace;
- evidence;
- verification;
- provenance;
- artifacts;
- approval state;
- sovereignty state;
- failures.

The frontend is therefore not merely a chat interface.

---

# 39. MODEL PORTFOLIO DECISION

The architecture should initially avoid permanent co-loading of every model.

Proposed conceptual portfolio:

```text
             TASK
               |
          ROUTER / POLICY
               |
      +--------+--------+
      |        |        |
     4B       9B     ESCALATION
      |        |        |
    cheap    primary   stronger
   multimodal reasoning candidate
      |
      +----------------+
               |
          Verification
```

### Candidate baseline

- Qwen3.5-4B
- Qwen3.5-9B
- Qwen3-Embedding-0.6B
- Qwen3-Reranker-0.6B
- OCR/layout specialists

### Decision

**Portfolio architecture — PREFERRED**

Exact model residency:

**REQUIRES HARDWARE VALIDATION**

---

# 40. MODEL ROUTING

Routing must optimize:

```text
Quality
+
Resource cost
+
Latency
+
Modality
+
Verification requirement
+
Risk
+
Availability
```

It must not optimize only:

> highest benchmark score.

The routing system should therefore be a **constraint solver/admission function**.

---

# 41. QUANTIZATION

Quantization is mandatory as an evaluation dimension because the MVP has a constrained GPU envelope.

vLLM currently supports multiple quantization formats including AWQ, GPTQ, INT8, FP8, GGUF and others, with hardware compatibility varying by method. 

### Decision

**Quantization-first model catalogue — SELECTED PRINCIPLE**

Exact quantization:

**REQUIRES VALIDATION**

The project should benchmark:

- quality degradation;
- VRAM;
- latency;
- model loading;
- context behavior;
- tool calling;
- multimodal quality.

---

# 42. TECHNOLOGY COMBINATION STRATEGY

The following combinations are currently the strongest candidates:

### Combination A — Primary AI

```text
Qwen3.5
   ↓
vLLM
   ↓
Capability Gateway
```

### Combination B — Retrieval

```text
Qwen3-Embedding-0.6B
          ↓
Lexical + Dense Search
          ↓
Qwen3-Reranker-0.6B
          ↓
Evidence Gate
```

### Combination C — Documents

```text
Docling
   +
PaddleOCR
   ↓
Structured Evidence
```

### Combination D — Agent

```text
LangGraph
   ↓
External Control/Authorization
   ↓
Typed Tools
   ↓
Verification
```

### Combination E — Code

```text
Agent
 ↓
Static Policy Checks
 ↓
Firecracker / gVisor
 ↓
Resource Limits
 ↓
Verification
```

---

# 43. END-TO-END STACK

The current preferred stack is:

```text
                    USER
                     |
              React / TypeScript
                     |
                  FastAPI
                     |
          +----------+----------+
          |                     |
    CONTROL PLANE          DATA PLANE
          |                     |
   Task / Policy          Evidence / Docs
   Authorization              |
   Resource Control       Docling / OCR
          |                     |
          +----------+----------+
                     |
                LangGraph
                     |
             Capability Router
                     |
                  vLLM
                     |
        +------------+-------------+
        |            |             |
    Qwen3.5-4B  Qwen3.5-9B   Specialists
        |            |             |
        +------------+-------------+
                     |
             Retrieval / Evidence
                     |
          Qwen3 Embedding 0.6B
                     |
            Hybrid Search
                     |
          Qwen3 Reranker 0.6B
                     |
             Evidence Gate
                     |
              Typed Tools
                     |
            +--------+--------+
            |                 |
          Tools          Firecracker
                           / gVisor
                              |
                         Verification
                              |
                     Artifact Generation
                              |
                +-------------+-------------+
                |                           |
           Provenance                    Audit
                |                           |
                +-------------+-------------+
                              |
                       OpenTelemetry
                              |
                  Independent Network
                       Enforcement
```

This is a **technology mapping of the Phase 10 architecture**, not permission for any component to bypass the control plane.

---

# 44. FINAL TECHNOLOGY DECISION MATRIX

| Architecture Role | Candidate | Current Decision | Primary Reason | Critical Validation |
|---|---|---|---|---|
| LLM | Qwen3.5-9B | Preferred | strong compact multimodal + reasoning/tool use | workflow + hardware |
| VLM | Qwen3.5-4B | Preferred | low-resource multimodal candidate | W1/W2 benchmark |
| LLM challenger | Llama 4 Scout | Strong Candidate | native multimodal | hardware/license/workflow |
| LLM challenger | Mistral Small | Strong Candidate | instruction/tool use | hardware |
| Inference | vLLM | Preferred | broad model/API/tool/quantization support | target GPU |
| Inference fallback | llama.cpp | Strong Candidate | local flexibility | compatibility/performance |
| Inference challenger | SGLang | Strong Candidate | performance challenger | target workload |
| Embedding | Qwen3-Embedding-0.6B | Preferred | small + multilingual + retrieval | retrieval corpus |
| Reranker | Qwen3-Reranker-0.6B | Preferred | retrieval quality/resource balance | retrieval corpus |
| Document parsing | Docling | Preferred | structured local document representation | corpus |
| OCR/layout | PaddleOCR | Strong Candidate | modular OCR/layout/table pipeline | scans |
| Search | Qdrant | Strong Candidate | filtering + hybrid retrieval | governed retrieval |
| Agent runtime | LangGraph | Preferred | stateful execution/HITL/persistence | reliability/security |
| Durable workflow | Temporal | Deferred | too much MVP infrastructure initially | revisit later |
| Sandbox | Firecracker | Preferred | stronger isolation model | adversarial test |
| Sandbox | gVisor | Strong Candidate | lower overhead | adversarial test |
| DB/control state | SQLite | Preferred | embedded transactional MVP store | concurrency/recovery |
| Observability | OpenTelemetry | Preferred | vendor-neutral local telemetry | operational test |
| Backend | FastAPI | Preferred | Python/AI ecosystem integration | integration |
| Frontend | React + TypeScript | Preferred | task/evidence UI flexibility | UX/security |
| Provenance | Custom domain model | Preferred | architecture-specific lineage | trace reconstruction |
| Audit | Custom event model | Preferred | authoritative audit semantics | tamper/replay testing |
| Network | Host enforcement | Mandatory | independent sovereignty | zero-egress test |

---

# 45. HARDWARE DECISION

No exact hardware configuration is selected yet.

This is intentional.

The architecture requires:

> single workstation/server + mid-range GPU

but the actual resource envelope remains an empirical question.

The critical experiment is not:

> Can Qwen3.5-9B run?

It is:

> Can the complete W3/W1/W2/W4 workflow run reliably under realistic resource contention?

---

# 46. HARDWARE TEST MATRIX

The benchmark shall measure:

| Variable | Test |
|---|---|
| GPU VRAM | peak/resident/free |
| RAM | peak |
| CPU | average/peak |
| model loading | cold start |
| model switching | warm/cold |
| context | short/medium/long |
| images | low/high resolution |
| documents | small/large |
| concurrency | 1 → N |
| verification | shallow/deep |
| sandbox | concurrent |
| retrieval | corpus growth |
| storage | ingestion/index/audit growth |
| thermal stability | sustained workload |

The Phase 11 specification explicitly requires these hardware measurements on actual intended hardware where possible.

---

# 47. SECURITY DECISION FRAMEWORK

The supplied security thresholds create three tiers.

## Tier 1 — Absolute invariants

Must be:

> **0 violations**

Including:

- authorization bypass;
- privilege escalation;
- self-authorization;
- cross-user leakage;
- cross-task leakage;
- unauthorized evidence;
- prompt injection acquiring authority;
- credential exposure;
- sandbox escape;
- prohibited egress;
- audit/provenance tampering;
- unauthorized OT/ICS action.



## Tier 2 — Security effectiveness

Baseline:

- High/Critical attack detection ≥95%;
- Critical containment =100%;
- High containment ≥95%;
- required security-event auditability ≥99%;
- unauthorized-action enforcement =100%;
- emergency stop =100%;
- authorization preservation after recovery =100%.



## Tier 3 — Operational robustness

Test:

- resource exhaustion;
- concurrency;
- degraded operation;
- restart;
- recovery;
- observability;
- runaway agents.

---

# 48. ZERO-EGRESS DECISION

Zero-egress remains a **system property**, not a feature of a particular library.

Testing must cover:

- application;
- agent;
- inference runtime;
- model process;
- OCR/parser;
- document processing;
- tools;
- sandbox;
- subprocesses;
- updates;
- telemetry;
- DNS;
- IPv4;
- IPv6;
- HTTP;
- HTTPS;
- TCP;
- UDP.

The supplied threshold is:

> **0 successful prohibited communications and 0 prohibited confidential-data transmissions.**



### Decision

**Independent host/network enforcement — MANDATORY**

Exact implementation:

**REQUIRES VALIDATION**

---

# 49. PROMPT-INJECTION DECISION

The invariant remains:

> **Data ≠ Instructions**

The security qualification requires:

- 100% preservation of the data/instruction boundary;
- 0 unauthorized tool execution;
- 0 unauthorized retrieval;
- 0 policy changes caused by untrusted content;
- 0 credential disclosure;
- 0 prohibited artifact releases;
- 0 autonomous consequential actions.



This means prompt-injection defense cannot be delegated to:

- Qwen;
- LangGraph;
- vLLM;
- the retriever;
- the UI.

It must be an architectural property enforced by the control plane.

---

# 50. GENERATED-CODE DECISION

The security contract requires:

- 0 sandbox escapes;
- 0 host filesystem modification;
- 0 credential access;
- 0 prohibited network access;
- 0 persistence outside sandbox;
- 0 privilege escalation;
- 100% resource limits;
- 100% verification of consequential numerical outputs.



Therefore:

# **Generated code remains untrusted until verified.**

---

# 51. TECHNICAL SPIKE PLAN

## Spike 1 — LLM

**Question:**  
Can Qwen3.5-9B satisfy W3/W4 while remaining inside the hardware envelope?

**Compare:**

- Qwen3.5-9B
- Qwen3.5-4B
- Llama 4 Scout
- Mistral Small challenger

**Measure:**

- grounded task success;
- hallucination;
- abstention;
- structured output;
- tool calling;
- latency;
- VRAM;
- RAM.

---

## Spike 2 — VLM/P&ID

**Question:**  
Can Qwen3.5 multimodal capability produce sufficiently useful P&ID representations?

Measure:

- entity precision/recall;
- tag accuracy;
- symbol identification;
- topology;
- connectivity;
- spatial relationships;
- provenance;
- engineering review acceptance.

---

## Spike 3 — Retrieval

Compare:

- Qwen3-Embedding-0.6B;
- Qwen3-Embedding-4B;
- BGE/Jina challenger.

Evaluate the complete:

```text
query
→ authorized retrieval
→ hybrid fusion
→ reranking
→ authority/revision filtering
→ sufficiency
→ grounded answer
```

---

## Spike 4 — Inference

Compare:

- vLLM;
- SGLang;
- llama.cpp.

Use the same:

- model;
- prompts;
- hardware;
- quantization;
- context;
- concurrency.

---

## Spike 5 — Agent reliability

Compare:

- LangGraph;
- constrained custom state machine.

Measure:

- completion;
- retries;
- recovery;
- tool arguments;
- authorization violations;
- verification compliance;
- false completion;
- infinite loops.

---

## Spike 6 — Sandbox

Compare:

- Firecracker;
- gVisor.

Attack:

- filesystem;
- credentials;
- process;
- privilege;
- network;
- resource exhaustion;
- persistence;
- escape.

---

## Spike 7 — Full hardware

Run:

```text
LLM
+
VLM
+
OCR
+
Embedding
+
Reranker
+
Agent
+
Sandbox
+
Verification
```

under realistic contention.

---

## Spike 8 — Artifact

Generate representative:

- technical report;
- approval note;
- structured engineering output.

Validate:

- structure;
- content;
- evidence;
- provenance;
- verification;
- human usefulness.

---

## Spike 9 — Sovereignty

Demonstrate:

- no DNS leakage;
- no IPv4/IPv6 leakage;
- no HTTP/HTTPS leakage;
- no tool-mediated egress;
- no sandbox egress;
- no update telemetry;
- no license check;
- no model download.

---

## Spike 10 — Provenance

Perform:

```text
Source
 ↓
Processing
 ↓
Evidence
 ↓
Claim
 ↓
Analysis
 ↓
Artifact
```

and reconstruct the complete lineage.

---

# 52. REQUIRED BENCHMARK MATRIX

| Workflow | Component | Candidate | Dataset | Hardware | Metric | Result | Decision |
|---|---|---|---|---|---|---|---|
| W3 | LLM | Qwen3.5-9B | enterprise corpus | target GPU | grounded task success | TBD | Requires Validation |
| W3 | Retrieval | Qwen3-Embedding-0.6B | retrieval corpus | target CPU/GPU | Recall/authority/sufficiency | TBD | Requires Validation |
| W1 | OCR | PaddleOCR | scanned reports | target CPU/GPU | OCR/structure accuracy | TBD | Requires Validation |
| W1 | Parser | Docling | technical PDFs | target CPU/GPU | structure fidelity | TBD | Requires Validation |
| W2 | VLM | Qwen3.5-4B/9B | P&ID corpus | target GPU | topology/entity accuracy | TBD | Requires Validation |
| W4 | LLM + artifact | Qwen3.5 | report corpus | target GPU | artifact correctness | TBD | Requires Validation |
| W5 | Sandbox | Firecracker/gVisor | hostile code | target host | escape rate | TBD | Requires Validation |

The absence of results here is deliberate. The Phase 11 specification prohibits invented hardware measurements.

---

# 53. NEGATIVE FINDINGS

| Technology/Approach | Decision | Reason |
|---|---|---|
| Docker-only hostile-code boundary | Rejected | insufficient assurance for stated threat model |
| One giant LLM | Rejected | resource concentration + poor capability specialization |
| Generic vector DB as knowledge architecture | Rejected | evidence governance exceeds vector storage |
| Fully distributed MVP | Rejected | conflicts with single-node constraint |
| Full event-sourced architecture | Rejected | unnecessary MVP complexity |
| Temporal as mandatory MVP orchestrator | Deferred | infrastructure burden not yet justified |
| VLM as sole P&ID authority | Rejected | visual recognition ≠ engineering truth |
| LLM-declared completion | Rejected | completion requires system predicates |
| Application-only zero-egress | Rejected | cannot independently prove sovereignty |
| Retrieval-then-authorization | Rejected as default | unauthorized data may already reach reasoning |
| Permanent model co-loading | Rejected as assumption | hardware must determine residency |
| Blind retry | Rejected | unsafe and can create loops/duplicate effects |

---

# 54. TECHNOLOGY-TO-REQUIREMENT TRACEABILITY

| Technology | Requirement | Mechanism | Limitation |
|---|---|---|---|
| vLLM | local multi-model capability | common local serving interface | target hardware unvalidated |
| Qwen3.5 | multimodal + reasoning | native text/image model | P&ID qualification unvalidated |
| Qwen3-Embedding | retrieval | semantic embeddings | domain retrieval unvalidated |
| Qwen3-Reranker | precision | second-stage ranking | resource cost unvalidated |
| Docling | document structure | unified representation | difficult engineering docs require testing |
| PaddleOCR | scan/OCR | local OCR/layout pipeline | domain OCR unvalidated |
| Qdrant | retrieval projections | vector/sparse/hybrid search | authorization must remain external |
| LangGraph | bounded workflow | stateful execution/checkpoints | authority must remain external |
| Firecracker | code isolation | microVM boundary | startup/performance must be tested |
| gVisor | code isolation | application-kernel sandbox | assurance/performance trade-off |
| SQLite | task state | local ACID store | concurrency envelope must be tested |
| OpenTelemetry | observability | local traces/metrics/logs | not authoritative audit |
| FastAPI | backend | typed API/OpenAPI | security architecture remains application responsibility |

---

# 55. SUPPLY-CHAIN REGISTER — INITIAL

| Component | Source | Version | License | Offline | Integrity |
|---|---|---|---|---|---|
| vLLM | official project release | 0.28.0 validation baseline | project license | Yes, with pre-staging | hash/SBOM required |
| Qwen3.5-9B | official model repository | current pinned checkpoint | Apache 2.0 | Yes after staging | model hash |
| Qwen3.5-4B | official model repository | current pinned checkpoint | Apache 2.0 | Yes after staging | model hash |
| Qwen3 Embedding | official model repository | pinned checkpoint | Apache 2.0 | Yes after staging | model hash |
| Qwen3 Reranker | official model repository | pinned checkpoint | Apache 2.0 | Yes after staging | model hash |
| Docling | official project | pinned release | verify release license | Yes after staging | package/SBOM |
| PaddleOCR | official project | pinned release | verify dependency tree | Yes after staging | package/model hashes |
| Qdrant | official project | pinned release | verify release license | Yes | package hash |
| LangGraph | official project | pinned release | verify dependencies | Yes | package/SBOM |
| Firecracker | official project | pinned release | Apache 2.0 | Yes | binary/source hash |
| OpenTelemetry | official project | pinned release | Apache 2.0 | Yes | package/SBOM |
| SQLite | official project | pinned release | public domain | Yes | source/binary hash |

**Important:** exact production versions are not frozen merely because a current release exists. The final baseline must include the exact tested artifact, dependencies and checksum.

---

# 56. LICENSE REVIEW

Licensing is a release gate.

The following require explicit legal review before commercial freezing:

- model license;
- software license;
- transitive dependency licenses;
- redistribution requirements;
- modification requirements;
- attribution;
- acceptable-use restrictions;
- model-specific restrictions.

The Phase 11 methodology explicitly rejects the assumption:

> open source = commercially unrestricted.

---

# 57. MAJOR TRADE-OFFS

## Model quality vs VRAM

Qwen3.5-9B is currently more attractive than simply using a much larger model, but actual quality/resource trade-off remains empirical.

## Multimodal unification vs specialization

A unified Qwen3.5 model reduces integration complexity.

Specialists may outperform it for:

- OCR;
- layout;
- P&ID extraction;
- reranking.

The architecture therefore retains specialization.

## vLLM breadth vs stack simplicity

vLLM's broad capability surface is valuable, but a smaller runtime may outperform it for specific low-resource workloads.

## Firecracker security vs execution overhead

Firecracker offers a stronger isolation model but must be benchmarked against gVisor.

## SQLite simplicity vs concurrency

SQLite is highly attractive for the single-node MVP but must be tested against realistic concurrent task workloads.

## LangGraph flexibility vs authority

LangGraph can simplify workflow implementation, but authority must remain outside it.

---

# 58. REVERSAL CONDITIONS

## vLLM

Reverse if:

- target model support becomes unstable;
- memory overhead prevents MVP deployment;
- model switching becomes unacceptable;
- security-critical runtime behavior cannot be adequately controlled.

## Qwen3.5

Reverse if:

- W3 quality is insufficient;
- W2/P&ID quality is inadequate;
- hallucination/abstention behavior fails thresholds;
- licensing becomes unacceptable;
- target hardware cannot support required latency.

## Qwen3 Embedding

Reverse if:

- retrieval Recall@K materially fails target;
- technical terminology retrieval is inadequate;
- a smaller or alternative embedding is demonstrably superior.

## Docling

Reverse if:

- structural fidelity on customer corpus is insufficient;
- difficult scans require excessive supplementary processing;
- provenance cannot be preserved adequately.

## LangGraph

Reverse if:

- framework authority cannot be reliably subordinated;
- reliability falls below target;
- checkpoint semantics conflict with authoritative task state;
- dependency/operational complexity becomes excessive.

## Firecracker

Reverse if:

- startup/resource cost materially damages W5;
- compatibility is insufficient;
- deployment complexity is disproportionate.

## Qdrant

Reverse if:

- authorization/revision filtering is insufficient;
- storage/resource requirements exceed MVP envelope;
- governed hybrid retrieval performs better with another engine.

---

# 59. FINAL TECHNOLOGY BASELINE

## Selected / Architecturally Established

These can be treated as architectural implementation direction:

1. capability abstraction;
2. multi-model architecture;
3. local inference;
4. governed retrieval;
5. structured document representation;
6. external authorization;
7. dedicated verification;
8. independent sandbox;
9. independent network enforcement;
10. application-owned provenance;
11. application-owned audit semantics;
12. local observability;
13. single-node deployment.

---

# 60. Preferred — Validation Required

### AI

- **Qwen3.5-9B**
- **Qwen3.5-4B**
- **Qwen3-Embedding-0.6B**
- **Qwen3-Reranker-0.6B**

### Inference

- **vLLM**

### Documents

- **Docling**

### OCR/layout

- **PaddleOCR / PP-StructureV3**

### Agent

- **LangGraph**

### Sandbox

- **Firecracker**

### Storage

- **SQLite for control/local metadata**

### Observability

- **OpenTelemetry**

### Backend

- **FastAPI**

### Frontend

- **React + TypeScript**

---

# 61. Strong Candidates

- llama.cpp;
- SGLang;
- Llama 4 Scout;
- Mistral Small challenger;
- Qwen3-Embedding-4B;
- Qwen3-Reranker-4B;
- gVisor;
- Qdrant;
- custom workflow runtime.

---

# 62. Deferred

- Temporal;
- distributed inference;
- multi-node model serving;
- Kubernetes;
- enterprise-scale object storage;
- multi-cluster orchestration;
- larger model fleets;
- universal multimodal pipeline;
- broad enterprise integration platform.

---

# 63. Rejected

- Docker-only hostile-code isolation;
- one giant model;
- vector database as the knowledge architecture;
- unrestricted agent framework authority;
- application-only sovereignty;
- VLM-only engineering truth;
- blind retries;
- model-declared completion;
- full distributed MVP;
- pure event-sourced MVP architecture.

---

# 64. Remaining Open Questions

1. Exact target GPU.
2. Exact system RAM.
3. Exact CPU.
4. W3 reliability threshold.
5. W1 document-quality threshold.
6. W2 P&ID qualification threshold.
7. W4 artifact acceptance threshold.
8. W5 inclusion decision.
9. Firecracker vs gVisor.
10. vLLM vs SGLang performance on target hardware.
11. Qwen3.5-4B vs 9B residency strategy.
12. Model switching vs co-loading.
13. Exact Qdrant/storage architecture.
14. Audit retention.
15. Exact authorization integration.
16. Exact network enforcement implementation.
17. Customer-specific model/data licensing.
18. First customer evaluation corpus.

These are genuine unresolved engineering decisions, not hidden assumptions.

---

# 65. Phase 11 Acceptance Checklist

| Criterion | Result |
|---|---|
| Architecture role defined before candidate | **YES** |
| Hard constraints defined before scoring | **YES** |
| Candidates generated after criteria | **YES** |
| Early elimination performed | **YES** |
| Vendor claims separated from independent evidence | **YES** |
| Negative findings recorded | **YES** |
| Security criteria applied | **YES** |
| Hardware criteria applied | **YES** |
| Integration criteria applied | **YES** |
| Workflow benchmarking defined | **YES** |
| Exact benchmark results available | **NO — validation required** |
| Exact target hardware available | **NO — open** |
| Critical sandbox validation completed | **NO** |
| Critical zero-egress validation completed | **NO** |
| P&ID validation completed | **NO** |
| Agent reliability validated | **NO** |
| Technology stack direction established | **YES** |
| Reversal conditions established | **YES** |
| Remaining uncertainties explicit | **YES** |
| Technology baseline reproducible today | **PARTIAL** |
| Phase 12 can begin | **YES, with validation work continuing in parallel** |

---

# 66. Final Phase 11 Decision

# **GATE B — TECHNOLOGY BASELINE ESTABLISHED WITH TARGETED VALIDATION**

The project has crossed the important threshold from:

> architecture concepts

to:

> concrete implementation candidates.

However, it has **not** crossed the threshold from:

> candidate technology baseline

to:

> empirically qualified production stack.

That distinction is intentional.

The strongest current implementation direction is:

```text
React / TypeScript
        |
     FastAPI
        |
Authoritative Control Plane
        |
     LangGraph
        |
Capability Router
        |
      vLLM
        |
+-------+-------+
|               |
Qwen3.5-4B   Qwen3.5-9B
|               |
+-------+-------+
        |
Governed Evidence
        |
+-------+-------+
|               |
Docling      PaddleOCR
|               |
+-------+-------+
        |
Qwen3 Embedding
        |
Hybrid Retrieval
        |
Qwen3 Reranker
        |
Evidence Sufficiency
        |
Typed Tools
        |
Firecracker / gVisor
        |
Verification
        |
Artifact
        |
Provenance + Audit
        |
OpenTelemetry

Independent host/network enforcement
```

The decisive point is that **the technology stack remains subordinate to the architecture**.

---

# 67. What Phase 11 Has Actually Proven

### Proven by documentation/evidence

- viable local serving technologies exist;
- vLLM currently has broad model, multimodal, structured-output and tool-calling support;
- Qwen3.5 provides a credible compact multimodal model family;
- Qwen3 embedding/reranking provides credible small retrieval components;
- Docling provides a structured local document-processing layer;
- PaddleOCR provides specialized OCR/layout processing;
- LangGraph provides stateful workflow primitives;
- Firecracker and gVisor provide meaningful isolation mechanisms;
- SQLite provides a viable embedded transactional store;
- OpenTelemetry provides local observability infrastructure.

### Not proven yet

- complete W3/W1/W2/W4 performance;
- target-GPU feasibility;
- model residency strategy;
- P&ID engineering usefulness;
- end-to-end agent reliability;
- sandbox qualification;
- zero-egress qualification;
- customer-corpus retrieval quality;
- artifact acceptance.

Those remain technical validation activities.

---

# 68. Phase 12 Handoff

Phase 12 should now take the **preferred technology baseline**, not the abstract architecture, and define:

1. concrete components;
2. process boundaries;
3. deployment units;
4. internal APIs;
5. schemas;
6. capability contracts;
7. model gateway;
8. retrieval interfaces;
9. evidence objects;
10. provenance schema;
11. audit schema;
12. agent state schema;
13. tool contracts;
14. sandbox interface;
15. verification interfaces;
16. artifact interfaces;
17. resource-management interfaces;
18. network-control integration;
19. configuration model;
20. dependency graph.

The Phase 11 specification explicitly identifies Phase 12 as the point where selected technology becomes component architecture.

**Phase 12 should not silently reopen the technology decisions. It may reverse a Phase 11 decision only when a component-level incompatibility or new validation evidence triggers the documented reversal condition.**