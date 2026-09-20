## Objective

Complete **R4 — Technical Research** for the Sovereign Agentic AI Workbench, using the accumulated R1–R3 outputs plus the supplied R4 prerequisite documents, and convert the open architecture questions into evidence-backed technical findings and candidate decisions. The required research chain is R1+R2+R3 → R4, and R4 is explicitly intended to produce candidate technologies, architectures, mechanisms and feasibility evidence. 

The project constraints remain binding: confidential data stays inside controlled infrastructure; core functionality cannot depend on external AI APIs; multiple open-weight models must be supported; agent actions must be controlled and observable; code must be sandboxed; the MVP must be feasible on a single workstation/server with a mid-range GPU; and sovereignty must be technically demonstrable. 

The R4 keyword package focuses on **local knowledge retrieval, document intelligence, multimodal AI, artifact generation, local model execution, model serving, model routing and constrained-GPU feasibility**.  

---

# R4 — TECHNICAL RESEARCH

## R4-01 — Local LLM serving: vLLM vs llama.cpp

**Research Stream:** R4 — Technical Research
**Research Topic:** Local model serving architecture
**Research Question:** Which inference substrate is appropriate for the MVP's mid-range GPU, multi-model, multi-user and air-gapped requirements?

**Sources**

vLLM official documentation:
[https://docs.vllm.ai/](https://docs.vllm.ai/)

llama.cpp official server documentation:
[https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

Red Hat technical comparison:
[https://developers.redhat.com/articles/2026/06/15/llamacpp-vs-vllm-choosing-right-local-llm-inference-engine](https://developers.redhat.com/articles/2026/06/15/llamacpp-vs-vllm-choosing-right-local-llm-inference-engine)

**Source Type:** Official technical documentation + independent technical analysis.

### Key Finding

**FACT:** Both vLLM and llama.cpp can serve local open-weight models through OpenAI-compatible APIs, but they optimize for different operating conditions.

vLLM is designed around production GPU serving, continuous batching, KV-cache management, structured outputs and tool calling. Its current documentation explicitly supports quantization, multimodal preprocessing, structured output, tool calling, embeddings, reasoning parsers and OpenAI-compatible serving. It also has an offline documentation mode intended for air-gapped environments.

llama.cpp is substantially lighter and more hardware-portable. Its server supports CPU/GPU inference, quantized models, CPU/GPU hybrid execution, multimodality, continuous batching, parallel sequences, tool use, constrained JSON and monitoring. Its GGUF format is particularly suitable for portable offline model distribution.

### Project Relevance

The workbench needs a serving layer, not a model runtime embedded directly into application code.

### Implication

**Decision Status: Strong Candidate — vLLM as the primary server-side inference substrate; llama.cpp as a secondary compatibility/edge backend.**

The architecture should expose a stable **internal model-serving contract** rather than bind the application directly to one inference engine.

This matters because R1–R3 established that the product must support multiple model classes and future model replacement. 

### Limitations / Failure

vLLM's strength comes with greater deployment complexity and stronger GPU assumptions. llama.cpp is easier to deploy but should not automatically be assumed to provide the same multi-user throughput or scheduler behavior.

A weak architecture would therefore be:

```text
Workbench → llama.cpp only
```

A stronger architecture is:

```text
                ┌───────────────┐
                │ Model Gateway │
                └───────┬───────┘
                        │
              ┌─────────┴─────────┐
              │                   │
          vLLM backend       llama.cpp backend
```

### Confidence

**High**

### Open Question

What exact model-serving split produces the best quality/latency/VRAM trade-off on the target GPU class?

---

# R4-02 — Quantization is mandatory for the MVP hardware target

**Research Topic:** Quantized local inference
**Research Question:** Can useful model capability fit within a mid-range GPU without unacceptable quality degradation?

### Key Finding

**FACT:** Quantization materially reduces model memory requirements and is directly supported by modern local inference engines.

vLLM supports AWQ, GPTQ, INT4, INT8, FP8 and several other quantization paths.

llama.cpp provides first-class quantized GGUF execution and CPU/GPU hybrid offloading.

The reproduced independent L4 benchmark found large differences between FP16 and AWQ configurations, including substantially reduced VRAM use and higher throughput for quantized models. However, that benchmark explicitly uses synthetic workloads and limited model/GPU coverage, so its absolute numbers should not be treated as product guarantees.

### Project Relevance

The MVP explicitly targets a mid-range GPU. Therefore full-precision large-model deployment cannot be the default strategy.

### Implication

**Decision Status: Preferred architectural principle — quantization-first model catalogue.**

The workbench should store model metadata such as:

```text
Model
├── capability_profile
├── parameter_count
├── quantization
├── VRAM_estimate
├── context_limit
├── latency_profile
├── tool_call_support
├── vision_support
└── quality_scores
```

Model selection must therefore be based on **capability × hardware feasibility**, not parameter count alone.

### Failure

Quantization can change reasoning behaviour, and memory fit is not determined solely by model weights. Context length and KV-cache consumption also matter.

### Confidence

**High**

### Open Question

Which quantization format offers the best quality/VRAM compromise for each selected model family?

---

# R4-03 — SGLang is strategically important, but should not be the first mandatory runtime

**Research Topic:** Alternative inference engine
**Research Question:** Does SGLang provide material advantages for repeated agentic/model-routing workloads?

### Key Finding

**FACT:** SGLang is explicitly designed for high-throughput LLM/VLM serving, structured generation, prefix reuse, continuous batching and agentic workloads. Its architecture includes RadixAttention, structured outputs, speculative decoding and multi-modal support.

SGLang also has a model gateway with routing, health checks, retries, circuit breakers, queueing and observability.

### Implication

**Decision Status: Requires Validation**

SGLang is a strong candidate for the later optimization stage, particularly if evaluation shows that agent loops and repeated prompts dominate workloads.

It should **not** replace the initial vLLM decision merely because it benchmarks well under a specific configuration.

### Confidence

**Medium-High**

### Open Question

Does SGLang outperform vLLM on the project's *actual* mixed workload:

```text
RAG + VLM + tool calling + reasoning + concurrent users
```

rather than isolated benchmark workloads?

---

# R4-04 — Enterprise retrieval should be hybrid, metadata-aware and permission-aware

**Research Topic:** RAG architecture
**Research Question:** What retrieval architecture is required for confidential enterprise knowledge and engineering documentation?

### Key Finding

**FACT:** Hybrid retrieval combines lexical retrieval with semantic/vector retrieval. Current OpenSearch documentation supports BM25 + neural retrieval with score normalization/RRF and supports filtering during hybrid retrieval.

Vespa's current RAG architecture similarly recommends combining lexical and vector retrieval and supports structured filtering, permissions, ranking phases and expensive reranking only on a restricted candidate set.

This directly matches the R1 finding that engineering retrieval cannot rely purely on semantic similarity because identifiers, revision metadata, tags and exact terms matter. 

### Project Relevance

P&IDs, equipment tags, instrument IDs, standards references and document revisions contain information that embeddings alone can miss.

### Implication

**Decision Status: Preferred architecture**

The retrieval pipeline should be approximately:

```text
Query
 ↓
Task / intent interpretation
 ↓
Metadata + permission filters
 ↓
 ┌──────────────┬───────────────┐
 │ BM25 / lexical│ Vector search │
 └───────┬───────┴───────┬───────┘
         └───────┬───────┘
                 ↓
            Candidate set
                 ↓
             Reranker
                 ↓
        Evidence selection
                 ↓
      Citation-preserving context
                 ↓
                LLM
```

The key architectural point is that **authorization filtering must happen before evidence is exposed to the model**, not after generation. This was already established in R1 via the IBM permission-aware enterprise implementation. 

### Recommended technology direction

**Strong Candidates:**

* OpenSearch
* Vespa

**Do not make yet:** separate vector DB + separate keyword engine unless there is a demonstrated requirement.

A unified retrieval engine reduces index duplication and synchronization complexity. Vespa explicitly describes this advantage.

### Confidence

**High**

### Open Question

Which engine has the lower operational burden for the MVP while still supporting ACL filtering, hybrid ranking and future multimodal retrieval?

---

# R4-05 — Document parsing must produce a structured intermediate representation

**Research Topic:** Document intelligence pipeline
**Research Question:** How should raw enterprise documents be transformed before retrieval and reasoning?

### Key Finding

**FACT:** Modern document-processing systems increasingly preserve layout, tables, structure and multimodal information instead of reducing documents to plain text.

Docling supports PDF, DOCX, PPTX, XLSX, images and other formats, including layout analysis, reading order, table structure, formulas and OCR. It explicitly supports local execution and offline environments. Its models can be prefetched to local storage, and remote services require explicit opt-in.

PaddleOCR 3.0 provides OCR, hierarchical document parsing, structured extraction and local/offline deployment options.

### Project Relevance

This directly addresses:

* scanned inspection reports
* technical PDFs
* tables
* engineering documents
* office files
* images
* diagrams

The R4 prerequisite explicitly requires the transformation:

**Raw information → processing → structured representation → retrieval → evidence → reasoning → action.** 

### Implication

**Decision Status: Preferred design principle**

Do not build:

```text
PDF → OCR → giant text blob → embedding
```

Build:

```text
Raw file
   ↓
Parser
   ↓
Structured document representation
   ├── text
   ├── headings
   ├── tables
   ├── images
   ├── coordinates
   ├── page references
   ├── document metadata
   ├── revision metadata
   └── provenance
```

This intermediate representation becomes the canonical source for downstream retrieval.

### Recommended technology

**Strong Candidate: Docling**

**Secondary Candidate: PaddleOCR**

Docling is particularly attractive as the orchestration-level document representation, while PaddleOCR can serve as a specialized OCR/layout component where benchmarks justify it.

### Confidence

**High**

### Open Question

Can Docling's representation preserve enough engineering-specific graphical semantics for P&IDs, or is a dedicated diagram-extraction path required?

---

# R4-06 — Generic OCR is insufficient for engineering drawings

**Research Topic:** Multimodal technical-document understanding
**Research Question:** What architecture is required for P&IDs, diagrams and visually rich engineering documents?

### Key Finding

**FACT:** Modern VLMs such as Qwen3-VL combine text and visual processing, include OCR capabilities, document parsing, spatial understanding and multimodal reasoning, and can be run locally through vLLM or SGLang.

Qwen3-VL documentation explicitly supports:

* document parsing
* OCR
* layout position information
* spatial reasoning
* long-document understanding
* local/offline inference
* VLM inference through vLLM/SGLang.

However:

**INFERENCE:** A VLM alone should not become the canonical parser for every enterprise document.

### Why

A technical drawing contains multiple information types:

```text
visual geometry
+ symbols
+ text
+ spatial relationships
+ tags
+ lines/connections
+ legends
+ document metadata
```

A pure OCR pipeline loses geometry.

A pure VLM pipeline may produce plausible descriptions without deterministic evidence mapping.

### Implication

**Decision Status: Preferred hybrid multimodal pipeline**

```text
                Engineering PDF / image
                         ↓
                 Layout/document parser
                         ↓
            ┌────────────┴────────────┐
            │                         │
       OCR/text path            Visual path
            │                         │
            └────────────┬────────────┘
                         ↓
              Spatial/semantic model
                         ↓
           Structured drawing evidence
```

The VLM should be an **evidence extractor/reasoner**, not the only source of truth.

### Confidence

**High**

### Open Question

What representations are sufficient for a P&ID reasoning system: image + OCR coordinates, graph extraction, symbolic tags, vector geometry, or a combination?

---

# R4-07 — Qwen3-VL is a strong multimodal candidate, not yet a universal model decision

**Research Topic:** Local VLM model selection
**Research Question:** Which local multimodal model family deserves evaluation for the MVP?

### Key Finding

Qwen3-VL is unusually aligned with the project's requirements because its documented capabilities include visual reasoning, OCR, document parsing, spatial understanding, long-context processing and visual-agent functionality. It has dense and MoE variants and multiple model sizes.

### Implication

**Decision Status: Strong Candidate**

The first evaluation matrix should include at least:

```text
Qwen3-VL
├── small model
├── medium model
└── larger model
```

and measure:

* document OCR accuracy
* table extraction
* layout preservation
* diagram reasoning
* P&ID tag extraction
* spatial relation accuracy
* hallucination rate
* latency
* VRAM
* context utilization

The current evidence does **not** justify declaring one Qwen3-VL size “best” before project-specific benchmarking.

### Confidence

**Medium-High**

### Open Question

What is the smallest VLM that remains reliable on the project's real technical drawings?

---

# R4-08 — Agent execution needs durable state and explicit interruption points

**Research Topic:** Agent runtime
**Research Question:** What runtime primitives are required for controlled multi-step execution?

### Key Finding

**FACT:** LangGraph supports persistent checkpoints, human-in-the-loop interrupts, fault recovery, replay and durable execution. It can resume execution after failure and pause before sensitive steps for approval.

It also explicitly warns that interrupted nodes may restart from the beginning, meaning side effects before interrupts must be idempotent.

### Project Relevance

The product journey already requires:

```text
plan
→ execute
→ inspect
→ retry/correct
→ approve
→ continue
```

### Implication

**Decision Status: Strong Candidate — graph/state-machine agent runtime**

The agent should have explicit states:

```text
RECEIVED
  ↓
PLANNING
  ↓
EVIDENCE_COLLECTION
  ↓
EXECUTION
  ↓
VALIDATION
  ├── FAIL → RETRY / CORRECT
  └── PASS
         ↓
   APPROVAL_REQUIRED?
      ↓         ↓
     YES        NO
      ↓         ↓
   PAUSED     CONTINUE
      ↓
   APPROVED
      ↓
   ARTIFACT
      ↓
   FINAL_VERIFY
```

This is much safer than a free-running agent loop.

### Alternative

Semantic Kernel is also relevant because its Process Framework supports stateful processes, events, human approval and OpenTelemetry, but Microsoft currently labels the Process Framework experimental.

### Decision

**LangGraph: Strong Candidate**

**Semantic Kernel Process Framework: Requires Validation**

### Confidence

**High for architectural mechanism.**

---

# R4-09 — Tool access should be explicit and narrow

**Research Topic:** Agent tool architecture
**Research Question:** How should local tools be exposed to agents without turning the agent into an unrestricted operating-system process?

### Key Finding

Semantic Kernel's current documentation highlights a critical design principle: tools/functions should be semantically described and only the necessary tools should be exposed to the model. It also recommends keeping sensitive data local and passing references/state identifiers rather than unnecessarily sending large confidential content through model calls.

### Implication

The workbench should use:

```text
Agent
 ↓
Tool policy layer
 ↓
Allowed tool set
 ↓
Tool invocation
 ↓
Execution sandbox
 ↓
Result validation
```

Rather than:

```text
Agent → shell
```

Tools should be typed and constrained:

```text
read_file(...)
search_knowledge(...)
create_xlsx(...)
run_python_sandbox(...)
render_docx(...)
inspect_pdf(...)
```

and not:

```text
execute_any_command(...)
```

### Decision Status

**Preferred design principle**

### Confidence

**High**

---

# R4-10 — gVisor is suitable for the first sandbox; Firecracker is the stronger isolation option

**Research Topic:** AI-generated code execution
**Research Question:** What runtime should execute untrusted model-generated code?

### Key Finding

gVisor is an application-kernel isolation layer that intercepts system calls and uses namespaces/seccomp as defense in depth. It provides a stronger isolation boundary than conventional containers without requiring a full guest VM in every configuration.

Firecracker provides hardware-virtualization-based microVM isolation using KVM, seccomp, cgroups, namespaces and its Jailer. Its security documentation explicitly treats guest workloads as potentially malicious and recommends host-level egress filtering.

### Implication

**Decision Status:**

* **gVisor: Strong Candidate for MVP**
* **Firecracker: Strong Candidate for higher-assurance deployments**
* **Plain Docker container: Rejected as the sole isolation boundary for untrusted code**

The MVP can use:

```text
Agent
 ↓
Code generation
 ↓
Policy check
 ↓
gVisor sandbox
 ↓
read-only approved inputs
 ↓
execution
 ↓
resource/time limits
 ↓
output validation
```

For higher-risk/classified deployments:

```text
Agent
 ↓
Firecracker microVM
 ↓
isolated filesystem/network
 ↓
execution
```

### Critical security point

Firecracker itself does **not** filter network traffic; the host/network layer must enforce egress policy.

Therefore “sandboxed” does not automatically mean “sovereign.”

### Confidence

**High**

### Open Question

Does the MVP require VM-grade isolation immediately, or is gVisor sufficient for the expected code/tool threat model?

---

# R4-11 — Artifact generation should be deterministic wherever possible

**Research Topic:** Word/PowerPoint/Excel generation
**Research Question:** How should the system create reliable business deliverables?

### Key Finding

**FACT:** Programmatic libraries already support local generation of Office artifacts.

`python-docx` supports creation and modification of Word documents.

`python-pptx` supports creation/modification of PowerPoint files including text, tables, images, shapes and charts.

OpenPyXL supports programmatic Excel workbook manipulation and data validation; the supplied evidence package also identifies Python-based schema-driven Office generation as a viable approach.

### Implication

Do not ask an LLM to directly “write a PowerPoint file.”

Use:

```text
LLM
 ↓
Structured artifact specification
 ↓
Deterministic renderer
 ↓
DOCX / PPTX / XLSX
 ↓
Validation
 ↓
Final artifact
```

For example:

```json
{
  "report_title": "...",
  "sections": [],
  "tables": [],
  "citations": [],
  "approval_status": "draft"
}
```

The renderer owns document structure.

### Decision Status

**Preferred**

### Confidence

**High**

### Open Question

How much of the artifact should be schema-driven versus template-driven for each enterprise?

---

# R4-12 — Artifact validation must be a separate subsystem

**Research Topic:** Output verification
**Research Question:** How do we detect generated artifacts that are syntactically valid but semantically wrong?

### Key Finding

R1 already demonstrated that AI-generated documents may contain omissions, formatting artifacts and cross-section inconsistencies. 

Therefore:

**FACT/INFERENCE:** Successful file creation is not successful task completion.

### Implication

The verification layer should run:

```text
Structural validation
+
Source/evidence validation
+
Logical consistency checks
+
Numerical validation
+
Template compliance
+
Artifact integrity
```

Examples:

**Excel**

* formulas compile
* references valid
* expected sheets exist
* data types correct

**DOCX**

* sections present
* required citations present
* tables populated
* metadata correct

**PPTX**

* expected slide count
* title hierarchy
* no empty placeholders
* charts contain required data

### Decision Status

**Preferred architecture**

### Confidence

**High**

---

# R4-13 — Air-gap is an artifact-management and supply-chain problem, not merely a networking problem

**Research Topic:** Offline deployment
**Research Question:** What technically constitutes a reliable air-gapped deployment?

### Key Finding

Official documentation from multiple vendors demonstrates the same architectural pattern:

```text
Connected staging environment
        ↓
download artifacts
        ↓
verify artifacts
        ↓
transfer through approved channel
        ↓
internal registry / model store
        ↓
isolated environment
        ↓
runtime with no external dependency
```

NVIDIA documents pre-staging model assets and images for disconnected environments. GitLab similarly documents offline transfer of container images, model weights and executor images.

Docling also explicitly supports prefetching models to local storage for offline execution.

### Implication

The workbench needs an **offline supply-chain subsystem**:

```text
Model Registry
Artifact Registry
Container Registry
Dependency Manifest
SHA256 hashes
SBOM
Version manifest
Update package
Offline installer
```

The MVP should not depend on runtime downloads from:

* Hugging Face
* package registries
* model hubs
* SaaS APIs

### Decision Status

**Mandatory architecture requirement**

### Confidence

**High**

---

# R4-14 — Zero-egress must be measured, not asserted

**Research Topic:** Sovereignty verification
**Research Question:** How can the system technically prove that confidential data does not leave the environment?

### Key Finding

The project requirement says sovereignty must be technically demonstrable. 

Configuration statements such as “the application is local” are insufficient evidence.

### Implication

The system should generate a **Sovereignty Evidence Record** for every execution:

```text
Task ID
User
Input files
Models invoked
Model hashes
Tools invoked
Retrieved documents
Network policy
Outbound connections observed
Artifact hashes
Execution timestamps
Approval events
Verification results
```

Network enforcement should happen outside the application process as well.

Example:

```text
               INTERNAL NETWORK
────────────────────────────────────────────
UI
 │
Orchestrator
 │
Model gateway
 │
RAG
 │
Tools
 │
Sandbox
 │
Artifact engine
 │
Audit store
────────────────────────────────────────────
          │
       DENY EGRESS
          │
      INTERNET
```

### Decision Status

**Mandatory**

### Confidence

**High**

### Open Question

Which combination of host firewall, namespace/network policy, packet capture and application-level telemetry provides sufficient evidence for the target customer's assurance requirements?

---

# R4-15 — Recommended retrieval technology: Vespa vs OpenSearch

| Criterion                          | Vespa             | OpenSearch      |
| ---------------------------------- | ----------------- | --------------- |
| Hybrid retrieval                   | Strong            | Strong          |
| BM25                               | Strong            | Strong          |
| Vector search                      | Strong            | Strong          |
| Structured filtering               | Strong            | Strong          |
| Advanced multi-stage ranking       | **Very strong**   | Strong          |
| Custom ranking                     | **Very strong**   | Strong          |
| Enterprise familiarity             | Medium            | **High**        |
| Operational footprint              | Higher complexity | Moderate        |
| Permission filtering               | Supported         | Supported       |
| RAG suitability                    | **Very strong**   | **Very strong** |
| MVP simplicity                     | Medium            | **Better**      |
| Long-term retrieval sophistication | **Excellent**     | Excellent       |

Vespa's phased ranking architecture is especially relevant because it separates cheap candidate retrieval from expensive reranking and can run ONNX models during ranking.

OpenSearch provides a more familiar enterprise-search ecosystem and current hybrid search workflows.

### Decision

**OpenSearch: Strong Candidate for MVP**

**Vespa: Strong Candidate for advanced retrieval phase**

Do **not** deploy both initially.

The decision should be settled through a retrieval benchmark using the actual project corpus.

---

# R4-16 — Proposed technical architecture emerging from R4

The evidence now supports a modular architecture rather than a monolithic “AI application.”

```text
┌─────────────────────────────────────────────────────────────┐
│                    USER WORKBENCH UI                       │
│ Chat / Files / Tasks / Artifacts / Approvals / Audit      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                       Task Orchestrator
                               │
                ┌──────────────┴──────────────┐
                │                             │
          Policy Engine                 Task Classifier
                │                             │
                └──────────────┬──────────────┘
                               │
                        Model Router
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
          LLM backend       VLM backend       Utility models
          vLLM              vLLM/SGLang        OCR / embed / rerank
              │                │                 │
              └────────────────┴─────────────────┘
                               │
                     Agent Execution Graph
                               │
          ┌────────────────────┼─────────────────────┐
          │                    │                     │
     Knowledge Tool       File/Document Tool     Code Tool
          │                    │                     │
          │              ┌─────┴─────────┐          │
          │              │ Docling/OCR   │          │
          │              │ VLM pipeline │          │
          │              └─────┬─────────┘          │
          │                    │                    │
          └──────────────┬─────┴────────────────────┘
                         │
                  Structured Evidence
                         │
                Hybrid Retrieval Layer
                         │
                    OpenSearch*
                         │
                     Reranking
                         │
                         ↓
                  Evidence-grounded LLM
                         │
                  Verification Engine
                         │
               ┌─────────┴──────────┐
               │                    │
          Artifact Engine       Approval Gate
         DOCX/PPTX/XLSX              │
               │                    │
               └─────────┬──────────┘
                         │
                    Final Artifact
                         │
                     Audit Store
                         │
                Sovereignty Evidence
```

`*` OpenSearch is the current MVP candidate, not a final irreversible selection.

---

# R4 Established Findings

## EF-01 — The workbench requires a model gateway

The application must not directly depend on individual model servers.

**Decision:** Model Gateway abstraction — **Preferred**

---

## EF-02 — Quantization is part of architecture

It is not an optional optimization because the hardware constraint makes it necessary.

**Decision:** Quantization-aware model catalogue — **Preferred**

---

## EF-03 — Hybrid retrieval is the baseline

Semantic-only retrieval is inadequate for technical enterprise content.

**Decision:** lexical + semantic + metadata/ACL filtering + reranking — **Preferred**

---

## EF-04 — Documents require a structured intermediate representation

Plain text is insufficient for complex technical documents.

**Decision:** structured document representation — **Preferred**

---

## EF-05 — Multimodal reasoning must be separated from deterministic document extraction

VLMs should augment document pipelines, not replace them wholesale.

**Decision:** parser/OCR/layout + VLM — **Preferred**

---

## EF-06 — Agent execution requires durable state

A production agent needs checkpoints, retries, interruption and resume.

**Decision:** graph/state-machine runtime — **Strong Candidate**

---

## EF-07 — Code execution requires an actual isolation boundary

Plain Docker is insufficient as the sole trust boundary for untrusted generated code.

**Decision:** gVisor MVP; Firecracker for higher-assurance profiles — **Strong Candidates**

---

## EF-08 — Artifact generation should be deterministic

LLMs should generate structured content specifications rather than own binary document creation directly.

**Decision:** schema → deterministic renderer → validation — **Preferred**

---

## EF-09 — Air-gap requires offline supply-chain management

Models, containers, packages and dependencies must be staged and verified before entering the isolated environment.

**Decision:** offline artifact registry + verified bundles — **Mandatory**

---

## EF-10 — Sovereignty requires runtime evidence

“No internet access” must be demonstrable.

**Decision:** network enforcement + execution telemetry + sovereignty evidence record — **Mandatory**

---

# Relevant Findings

The R4 evidence substantially strengthens five core architectural conclusions from R1–R3:

| Requirement          | R4 technical conclusion                        |
| -------------------- | ---------------------------------------------- |
| Local AI             | vLLM primary + llama.cpp compatibility path    |
| Multiple models      | Internal model gateway + capability profiles   |
| Automatic routing    | Policy/task/capability-aware routing           |
| Enterprise knowledge | Hybrid retrieval with ACL/metadata filtering   |
| Scanned documents    | Docling + OCR + VLM                            |
| P&IDs / drawings     | multimodal + spatial/structured representation |
| Agent execution      | durable graph/state machine                    |
| Tool execution       | narrow typed tools                             |
| Generated code       | gVisor/Firecracker sandbox                     |
| DOCX/PPTX/XLSX       | programmatic deterministic rendering           |
| Verification         | independent validation layer                   |
| Air-gap              | pre-staged offline artifact ecosystem          |
| Auditability         | event log + execution trace                    |
| Sovereignty          | network enforcement + evidence generation      |

These requirements are directly consistent with the R4 prerequisite structure and the prior R1 findings around engineering documents, cross-document dependencies, permission-aware retrieval and human approval.  

---

# Rejected / Inadequate Approaches

### RA-01 — Single-model architecture

**Rejected.**

The system's workloads differ materially between reasoning, coding, OCR, VLM and retrieval.

---

### RA-02 — Vector-only RAG

**Rejected.**

Fails technical identifiers, exact terms, metadata, authorization and structured relationships.

---

### RA-03 — LLM directly generates Office binaries

**Rejected.**

Deterministic programmatic rendering is more controllable and verifiable.

---

### RA-04 — Unrestricted shell access for agents

**Rejected.**

Creates an unacceptable trust boundary for model-generated actions.

---

### RA-05 — “Docker is the sandbox”

**Rejected.**

Container isolation alone should not be assumed sufficient for hostile/untrusted generated code.

---

### RA-06 — Runtime downloads in air-gapped environments

**Rejected.**

Violates the operational sovereignty model and creates hidden external dependencies.

---

### RA-07 — Build the entire platform around a single inference engine

**Rejected.**

The project's explicit requirement for multiple replaceable models makes this unnecessarily coupled.

---

# Failure / Risk Findings

## FR-01 — VRAM contention

The same GPU may be required by:

```text
LLM
VLM
embeddings
reranker
OCR
```

This can create unpredictable latency and out-of-memory failures.

**Mitigation:** model scheduler + resource reservations + load/unload policies.

---

## FR-02 — Long-context memory explosion

Long prompts increase KV-cache usage even when model weights fit.

**Mitigation:** chunking, retrieval compression, context budgets, KV-cache-aware routing.

---

## FR-03 — VLM hallucination

The model can describe a visually plausible but incorrect engineering relationship.

**Mitigation:** coordinate-linked evidence, deterministic extraction, confidence thresholds, human approval.

---

## FR-04 — Retrieval permission failure

An unauthorized but semantically relevant document can contaminate the answer.

**Mitigation:** ACL enforcement before model context assembly.

---

## FR-05 — Agent replay side effects

Durable agents can unintentionally repeat side effects when a node is resumed.

LangGraph explicitly documents this behaviour around interrupts.

**Mitigation:** idempotent operations, dedicated action nodes and transactional tool wrappers.

---

## FR-06 — Sandbox egress

A sandbox can still communicate outward unless network policy explicitly denies it.

Firecracker documentation explicitly places network filtering responsibility on the host.

**Mitigation:** default-deny network namespace / host firewall / packet-level verification.

---

## FR-07 — Offline dependency drift

A model may be offline-capable while a parser, package or container initialization path still expects network access.

**Mitigation:** complete offline dependency manifests and preflight validation.

---

# Open Questions

1. What exact GPU defines “mid-range” for the MVP?
2. What is the acceptable concurrent user count?
3. Which model size/quantization combination provides sufficient reasoning quality?
4. Should the first MVP support one model at a time or multiple resident models?
5. OpenSearch vs Vespa for the production retrieval layer?
6. What embedding model performs best on engineering terminology?
7. Which reranker works reliably within the GPU budget?
8. What exact document representation is required for P&IDs?
9. What is the minimum VLM size that passes the project's drawing benchmark?
10. gVisor vs Firecracker for the target threat model?
11. What exact approval taxonomy maps to tool/action risk?
12. Which artifacts require template-driven generation?
13. How should enterprise ACLs map into the local retrieval index?
14. What offline update mechanism will be acceptable to customers?
15. What exact test methodology proves zero-egress operation?

---

# Architecture / Engineering Questions Passed Forward

R4 should now pass a much sharper set of questions into **R5 Failure Research**:

### Inference

* benchmark vLLM vs llama.cpp vs SGLang
* benchmark quantization schemes
* measure cold start/model swapping
* measure mixed LLM/VLM workloads
* model-router failure behaviour

### Retrieval

* evaluate BM25 vs dense vs hybrid
* evaluate OpenSearch vs Vespa
* test ACL pre-filtering
* measure reranker cost
* test stale/conflicting document handling

### Documents

* compare Docling vs PaddleOCR vs RAGFlow components
* test multi-column PDFs
* test scanned engineering reports
* test tables
* test diagrams
* test P&ID extraction

### Multimodal

* benchmark Qwen3-VL model sizes
* test spatial reasoning
* quantify OCR errors
* quantify visual hallucination

### Agents

* test checkpoint recovery
* test failed tool execution
* test repeated side effects
* test approval interruption
* test long-running tasks

### Sandboxing

* attack gVisor sandbox
* compare Firecracker isolation
* test filesystem escape
* test network escape
* test resource exhaustion

### Artifacts

* verify DOCX/PPTX/XLSX structural integrity
* verify formulas and references
* compare template-driven and schema-driven generation

### Sovereignty

* measure every possible network path
* test DNS
* test telemetry
* test package managers
* test model initialization
* test OCR/runtime downloads
* generate machine-readable sovereignty evidence

---

# Technical Decision Register — End of R4

| Component                       | Current Status                                       |
| ------------------------------- | ---------------------------------------------------- |
| Model Gateway                   | **Preferred architecture**                           |
| vLLM                            | **Strong Candidate / likely primary**                |
| llama.cpp                       | **Strong Candidate / compatibility backend**         |
| SGLang                          | **Requires Validation**                              |
| Quantization                    | **Preferred / mandatory strategy**                   |
| Hybrid retrieval                | **Preferred**                                        |
| OpenSearch                      | **Strong Candidate for MVP**                         |
| Vespa                           | **Strong Candidate for advanced retrieval**          |
| Docling                         | **Strong Candidate / likely primary document layer** |
| PaddleOCR                       | **Strong Candidate / specialized OCR**               |
| Qwen3-VL                        | **Strong Candidate**                                 |
| LangGraph                       | **Strong Candidate**                                 |
| Semantic Kernel Process         | **Requires Validation**                              |
| gVisor                          | **Strong Candidate for MVP sandbox**                 |
| Firecracker                     | **Strong Candidate for high-assurance isolation**    |
| Docker-only sandbox             | **Rejected**                                         |
| Programmatic Office generation  | **Preferred**                                        |
| Independent artifact validation | **Mandatory**                                        |
| Offline model/artifact registry | **Mandatory**                                        |
| Zero-egress verification        | **Mandatory**                                        |

## R4 conclusion

The research does **not** justify prematurely freezing the entire stack.

It does justify freezing the **architectural contracts**:

```text
UI
 ↓
Policy
 ↓
Task Router
 ↓
Model Gateway
 ↓
Agent Runtime
 ↓
Capability Tools
 ↓
Evidence / Retrieval Layer
 ↓
Verification Layer
 ↓
Artifact Layer
 ↓
Audit / Sovereignty Layer
```

That is the correct level of commitment at the end of R4.

The specific engines—especially **vLLM vs SGLang, OpenSearch vs Vespa, Docling vs specialized OCR components, Qwen3-VL size, and gVisor vs Firecracker**—should now be experimentally stress-tested rather than decided by documentation alone.

The supplied methodology explicitly requires R4 to investigate mechanism, deployment, offline capability, hardware, performance, security, failure behaviour, licensing, maturity, production evidence and project relevance before technology selection. 

The next research stream is therefore **R5 — Failure Research**, and it should use these R4 candidates as the attack surface rather than restarting technology discovery. 
