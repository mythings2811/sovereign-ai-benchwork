**Objective:** Stress-test the R4 architecture under failure conditions and convert the observed breakpoints into concrete controls, residual risks, rejected approaches, and engineering questions for R6.

R5 is explicitly the stream that stress-tests R4 rather than restarting technology discovery. Its required focus is *what fails, why, under what conditions, how severe it is, whether it can be detected, how it can be mitigated, and what residual risk remains*.  

The project constraints remain binding: local-only confidential processing, multiple replaceable open-weight models, controlled/observable agent actions, sandboxed code, single-server/mid-range-GPU feasibility, and technically demonstrable sovereignty. 

---

# R5 — FAILURE RESEARCH

## 1. R5 Executive Finding

The R4 architecture survives the failure review, but **not in its naïve form**.

The dominant danger is not a component returning an explicit error. The more serious class is:

> **a component returns something structurally valid, plausible, and therefore accepted by the next component even though it is wrong.**

This occurs in document parsing, retrieval freshness, tool outputs, model synthesis, agent recovery, and human approval. Recent reliability benchmarks independently show that apparently grounded or syntactically valid agent outputs can still be operationally wrong when evidence is stale, unauthorized, incomplete, from the wrong session, or semantically corrupted. ([arXiv][1])

Therefore the central R5 result is:

**Failure containment must be layered.** The system cannot rely on the model, agent framework, retriever, sandbox, or validator individually.

---

# 2. R5-01 — Local inference can fail at the engine level, not merely at request level

### Research Stream

R5 — Failure Research

### Research Topic

Local LLM/VLM inference reliability

### Research Question

Can a single bad or unusually demanding request destabilize the inference service under the MVP's constrained-GPU architecture?

### Source

vLLM production metrics and current issue history; R4's vLLM primary-candidate decision.

### Source Type

Official documentation + implementation/incident evidence.

### Key Finding

**FACT:** vLLM exposes metrics for KV-cache utilization, preemptions, queue depth, request latency, multimodal-cache behavior and request success, confirming that resource pressure is an operational condition that should be monitored rather than inferred indirectly. ([vLLM][2])

**OBSERVATION:** Current vLLM issue reports show failure cases in which CUDA out-of-memory or multimodal engine errors can terminate the engine rather than only reject the offending request. Some reported failures produced `EngineDeadError`, HTTP 500 responses and health failures for subsequent requests.

### Evidence

The current vLLM issue record contains examples of:

* forward-pass CUDA OOM killing the `EngineCore`;
* multimodal Qwen3-VL buffer errors becoming fatal engine failures;
* memory-pressure failures depending on request ordering and workload history rather than a fixed model-size threshold.

These are issue-level observations, not universal rates.

### Project Relevance

The MVP intentionally places multiple AI capabilities on a constrained machine. A process-level failure can therefore affect the entire workbench rather than one task.

### Implication

**Decision Status: Retain vLLM as a candidate, but reject “single inference process = reliable service” as an architecture.**

The Model Gateway needs:

```text
Request
  ↓
Admission control
  ↓
Resource budget
  ↓
Inference worker
  ↓
Health supervision
  ↓
Failure classification
  ├── reject request
  ├── retry/reduce workload
  ├── route elsewhere
  └── restart worker
```

A malformed or oversized request should not become a workstation-wide outage.

### Limitations / Failure

Inference-engine behavior is version-, model-, CUDA-, driver-, and workload-dependent. A benchmark on one GPU cannot establish fleet-wide reliability.

### Confidence

**High** for the failure class; **Medium** for the frequency in the final deployment.

### Open Question

What request-level budget—prompt tokens, images, image resolution, generated tokens, concurrency and KV-cache occupancy—keeps the engine inside a demonstrably safe operating envelope?

---

# 3. R5-02 — VRAM contention is a systemic failure, not just a capacity problem

### Research Stream

R5 — Failure Research

### Research Topic

GPU resource contention

### Research Question

What happens when LLM, VLM, OCR, embedding, reranking and other workloads share the same constrained GPU?

### Key Finding

**FACT:** GPU memory consumption is affected not only by model weights but also by KV cache, multimodal processing, batching and intermediate activations. vLLM exposes separate metrics for KV-cache usage, preemption, waiting requests and multimodal cache activity. ([vLLM][2])

### Failure Mechanism

A single request can trigger:

```text
large document
      ↓
large image / many images
      ↓
vision activations
      +
long-context KV cache
      +
other resident model state
      ↓
VRAM peak
      ↓
latency spike / OOM / engine crash
```

The failure can be **history-dependent**: an identical request may succeed on a fresh process and fail later after memory peaks or cache residency changes.

### Project Relevance

R4 assumes local multimodal processing on a single server. The architecture therefore cannot treat GPU capacity as a static “model fits / model doesn't fit” property.

### Implication

**Decision Status: Mandatory control.**

The model router must become a **resource-aware scheduler**, with explicit budgets for:

* resident model memory,
* KV-cache allocation,
* multimodal activation budget,
* concurrent sequences,
* maximum image count/resolution,
* maximum context length,
* model loading/swap operations.

### Mitigation

Use bounded admission:

```text
Task requirements
       ↓
Estimated resource footprint
       ↓
GPU budget check
       ├── fit → execute
       ├── marginal → queue
       ├── overflow → smaller model/path
       └── impossible → safe rejection
```

### Residual Risk

Exact resource prediction remains imperfect because runtime memory may depend on implementation details and input characteristics.

### Confidence

**High**

### Open Question

Can resource usage be predicted accurately enough before execution to prevent catastrophic peaks, particularly for multimodal inputs?

---

# 4. R5-03 — Multimodal inference has feature-interaction failures

### Research Stream

R5 — Failure Research

### Research Topic

Local VLM reliability

### Research Question

Do multimodal models fail through ordinary accuracy errors only, or can preprocessing/caching/scheduler interactions destabilize serving?

### Key Finding

**OBSERVATION:** Current vLLM issue history shows modality-specific failures involving Qwen3-VL, including multimodal buffer mismatches, device mismatches and OOM conditions under combinations of chunked prefill, prefix caching, vision inputs and concurrent workloads.

### Evidence

One reported Qwen3-VL issue produced repeated fatal `EngineCore` failures under multimodal requests; another involved a CPU/CUDA device mismatch in video processing. Such bugs were later associated with regressions/fixes rather than intrinsic model incapability.

### Project Relevance

R4 proposed a hybrid parser/OCR/VLM architecture with Qwen3-VL as a strong candidate. The failure risk is therefore in the **interaction between model + runtime + preprocessing + cache + scheduler**, not just in model quality.

### Implication

**Do not treat “VLM benchmark passed” as production readiness.**

The evaluation matrix must include:

```text
model
×
vLLM/SGLang version
×
image resolution
×
image count
×
context length
×
prefix caching
×
chunked prefill
×
concurrency
```

### Mitigation

Version-pin the complete serving stack:

```text
GPU driver
CUDA
PyTorch
inference engine
model revision/hash
multimodal processor
```

Then run long-duration soak tests.

### Confidence

**High** for existence of feature-interaction failures; **Medium** for recurrence in any specific release.

### Open Question

Which runtime/model combinations remain stable under a multi-hour mixed text+vision workload representative of the workbench?

---

# 5. R5-04 — Document parsing errors propagate silently downstream

### Research Stream

R5 — Failure Research

### Research Topic

OCR/document parsing failure

### Research Question

Can structured-document parsing produce plausible but semantically wrong representations that survive into agent reasoning?

### Key Finding

**FACT:** Recent professional-document benchmarks show that current document systems still fail on table alignment, charts, footnotes, exclusions, reading order, scans, amendments and visual grounding. GDP.pdf found that even strong multimodal systems performed poorly on realistic professional PDF tasks, with failures concentrated in precisely these areas. ([arXiv][3])

ParseBench likewise evaluates semantic rather than merely textual correctness because a parser can generate readable output while assigning information to the wrong visual region. Its evaluation shows no single tested method is consistently strong across tables, charts, content faithfulness, formatting and visual grounding.

### Failure Mechanism

The most dangerous sequence is:

```text
Wrong parsing
 ↓
Structurally valid JSON/Markdown
 ↓
Retriever accepts it
 ↓
LLM treats it as evidence
 ↓
Agent reasons correctly over wrong evidence
 ↓
Artifact looks professional
```

The system may report no software error.

### Project Relevance

The workbench explicitly handles scanned reports, engineering documents, spreadsheets, diagrams and drawings.

### Implication

**Decision Status: Mandatory independent parsing validation.**

Parsing quality must be evaluated on:

* text completeness;
* reading order;
* table structure;
* numerical fidelity;
* superscripts/subscripts;
* amendment/superseded content;
* bounding boxes;
* image/figure associations;
* page/document provenance.

### Mitigation

Maintain an evidence object such as:

```text
EvidenceItem
 ├── document_id
 ├── revision
 ├── page
 ├── bounding_box
 ├── extracted_value
 ├── extraction_method
 ├── confidence
 └── source_hash
```

### Residual Risk

No generic parser can guarantee semantic correctness for all enterprise documents.

### Confidence

**High**

### Open Question

What subset of parser outputs must be independently verified before the data is permitted into an evidence-grounded agent workflow?

---

# 6. R5-05 — Engineering drawings are harder than ordinary multimodal documents

### Research Stream

R5 — Failure Research

### Research Topic

Engineering drawing/P&ID reasoning

### Research Question

Can a VLM reliably infer engineering relationships from drawings without an explicit structural representation?

### Key Finding

**FACT:** Recent P&ID research reports that raw image interaction can be substantially less reliable than graph-grounded representations. A 2026 ChatP&ID study reports improved accuracy when smart-P&ID information is converted into structured graphs rather than given directly as images. ([arXiv][4])

This direction is consistent with the earlier R1 engineering-dependency evidence and R4 conclusion that visual reasoning alone should not become the canonical truth source.

### Failure Mechanisms

P&IDs combine:

```text
symbols
+ tags
+ geometry
+ line connectivity
+ spatial relationships
+ labels
+ legends
+ revision metadata
```

A model can correctly recognize every visible symbol while still infering the wrong connection.

### Project Relevance

This is one of the project's highest-value and highest-consequence workloads.

### Implication

**Decision Status: Narrow the R4 VLM decision.**

Qwen3-VL or another VLM may be used as an **evidence extractor/reasoner**, but engineering relationships should increasingly move toward structured representations:

```text
Drawing
 ↓
OCR + layout
 ↓
entity extraction
 ↓
symbol/tag localization
 ↓
connection/relationship extraction
 ↓
engineering graph
 ↓
reasoning
```

### Mitigation

Require location-linked and relationship-linked evidence for engineering assertions.

For consequential answers:

```text
Claim
 ↓
supporting visual region
 +
supporting extracted entity
 +
relationship evidence
 ↓
engineering conclusion
```

### Residual Risk

Automatic graph extraction itself can be wrong.

### Confidence

**High** for the architectural failure class; **Medium** for generalization of particular P&ID benchmark numbers.

### Open Question

What minimum graph fidelity is required before a P&ID-derived claim is allowed to support an approval or engineering artifact?

---

# 7. R5-06 — Retrieval can be grounded and still wrong

### Research Stream

R5 — Failure Research

### Research Topic

Enterprise RAG reliability

### Research Question

Does citation/grounding guarantee correctness when enterprise evidence is stale, unauthorized, incomplete or contextually wrong?

### Key Finding

**FACT:** LayerRAG-Bench explicitly demonstrates that an agentic RAG response can appear grounded while failing at the evidence, authorization or session layer. Across 38,880 records, stale indexes, denied permissions, missing tool output and wrong-session context were not repaired by schema normalization. ([arXiv][1])

### Failure Modes

| Failure            | Why superficial grounding fails                                  |
| ------------------ | ---------------------------------------------------------------- |
| Stale document     | Citation exists, but content is obsolete                         |
| Wrong revision     | Correct source family, wrong version                             |
| Wrong authority    | Relevant departmental document overrides a higher-authority rule |
| Permission failure | Semantically correct evidence belongs to another user            |
| Wrong session      | Evidence belongs to another task/context                         |
| Missing evidence   | Model fills the gap from parametric knowledge                    |

### Project Relevance

R1 already established authority/version/ACL requirements; R4 chose hybrid retrieval. R5 demonstrates that **hybrid retrieval alone is insufficient**.

### Implication

**Decision Status: Retain hybrid retrieval; add evidence-governance layer.**

Retrieval should output:

```text
retrieved evidence
+
authorization status
+
authority level
+
revision/time validity
+
session/task provenance
+
completeness state
```

### Critical Rule

A denied, stale or ambiguous result should be allowed to produce:

> **NO SAFE ANSWER**

rather than forcing an answer.

### Confidence

**High**

### Open Question

How should the system resolve conflicting revisions and departmental authority when enterprise metadata itself is unreliable?

---

# 8. R5-07 — Reranking can prefer obsolete but semantically rich evidence

### Research Stream

R5 — Failure Research

### Research Topic

Retrieval recency failure

### Research Question

Can a technically strong reranker still select obsolete enterprise information?

### Key Finding

**FACT:** FRESCO reports a consistent failure mode across evaluated rerankers in evolving-information settings: semantically rich older evidence can outrank factually current evidence. Their obsolete-ratio measurements remained high across the evaluated reranker set. ([arXiv][5])

### Failure Mechanism

```text
old document ─┐
              ├─ high semantic relevance
new document ─┘
        ↓
reranker chooses richer old text
        ↓
LLM receives plausible obsolete evidence
```

### Project Relevance

Engineering revisions, SOP versions, safety procedures and technical instructions frequently change.

### Implication

**Decision Status: Preferred retrieval design must be temporal/authority-aware, not relevance-only.**

Ranking should consider:

```text
semantic relevance
+
lexical relevance
+
authorization
+
authority
+
revision validity
+
effective date
```

### Residual Risk

Metadata may itself be incorrect or missing.

### Confidence

**Medium-High**

### Open Question

What should the system do when document authority and revision metadata conflict with the actual content?

---

# 9. R5-08 — Prompt injection can originate inside trusted enterprise files

### Research Stream

R5 — Failure Research

### Research Topic

Indirect prompt injection through documents

### Research Question

Does keeping the system entirely local prevent prompt-injection-driven agent compromise?

### Key Finding

**FACT:** NIST identifies direct and indirect prompt injection as a GenAI security risk and notes that malicious instructions can be embedded in retrieved data; it also notes demonstrated risks involving proprietary-data theft and remote code execution in connected systems. ([NIST Publications][6])

**FACT:** OWASP's 2026 Agentic Top 10 explicitly treats goal hijacking, tool misuse, identity/privilege abuse, memory poisoning, code execution and cascading failures as distinct agentic risks. ([OWASP Gen AI Security Project][7])

### Failure Mechanism

A malicious instruction can be embedded in:

* PDF text;
* OCR text;
* image content;
* source code comments;
* spreadsheet cells;
* tool descriptions;
* retrieved knowledge;
* persistent memory.

For the model, all of these ultimately enter the context window.

### Important Consequence

**Air-gapping blocks a class of exfiltration paths; it does not eliminate instruction-confusion attacks.**

### Implication

The architecture needs an explicit distinction:

```text
CONTROL PLANE
system policy
permissions
tool authorization
workflow rules

DATA PLANE
documents
OCR
retrieved text
tool results
user content
```

Data-plane content must never acquire control-plane privileges merely because a model interprets it as an instruction.

### Mitigation

Use:

* typed evidence objects;
* tool authorization outside the model;
* least privilege;
* explicit action policies;
* untrusted-content labeling;
* approval gates for consequential actions;
* adversarial document testing.

### Confidence

**High**

### Open Question

How much prompt injection can be prevented versus only contained through capability restriction and least agency?

---

# 10. R5-09 — Tool failure is often semantic, not explicit

### Research Stream

R5 — Failure Research

### Research Topic

Agent tool-use reliability

### Research Question

What happens when a tool returns a syntactically valid but semantically wrong result?

### Key Finding

**FACT:** ToolMaze shows that agents degrade substantially under tool perturbations, with the sharpest weakness under implicit semantic failures; its study reports an average implicit-versus-explicit recovery gap of about 37 percentage points. ([arXiv][8])

ToolBench-X similarly reports substantial reliability degradation under recoverable tool hazards and finds hazard diagnosis to be a stronger bottleneck than simply increasing inference budget. ([arXiv][9])

### Typical Failure

```text
tool call succeeds
 ↓
HTTP 200
 ↓
JSON schema valid
 ↓
value is wrong / stale / partial
 ↓
agent trusts it
```

### Project Relevance

The workbench depends heavily on local tools for files, spreadsheets, retrieval, code and artifacts.

### Implication

**Decision Status: Mandatory tool-result contracts.**

Every tool should expose:

```text
status
schema version
provenance
completeness
freshness
confidence / validity
error class
```

A semantic validator should run where possible.

### Confidence

**High**

### Open Question

Which tool classes require deterministic outcome monitors rather than relying on the agent to inspect their results?

---

# 11. R5-10 — Blind retry creates loops and compounds errors

### Research Stream

R5 — Failure Research

### Research Topic

Agent retry/replanning failure

### Research Question

Does retry automatically improve reliability?

### Key Finding

**FACT:** ToolMaze and ToolBench-X both show that retrying is not equivalent to recovery. Agents frequently repeat failed actions or fail to diagnose the underlying fault, particularly when the error is implicit rather than explicit. ([arXiv][8])

### Failure Pattern

```text
tool fails
 ↓
agent retries same tool
 ↓
same failure
 ↓
agent changes argument
 ↓
same semantic failure
 ↓
loop
 ↓
resource/time consumption
```

### Severity

Medium for ordinary tasks, potentially **High** for:

* repeated file mutation;
* repeated external/internal action;
* expensive computation;
* repeated approval requests;
* recursive agent calls.

### Implication

R4's retry loop must become:

```text
Failure
 ↓
Classify failure
 ├── transient
 ├── permanent
 ├── semantic
 ├── authorization
 └── unknown
 ↓
select recovery policy
```

Retry should **not** be the default response to every error.

### Confidence

**High**

### Open Question

How accurately can a lightweight local failure classifier distinguish transient infrastructure faults from semantic tool corruption?

---

# 12. R5-11 — Durable execution does not provide exactly-once side effects

### Research Stream

R5 — Failure Research

### Research Topic

Agent state/replay failure

### Research Question

Does checkpointing prevent duplicate actions when an agent is interrupted or restarted?

### Key Finding

**FACT:** LangGraph explicitly documents that interrupted nodes may execute again after resumption, and therefore side effects need to be idempotent or isolated appropriately. ([Docs by LangChain][10])

Replay also re-executes later nodes, including LLM/API calls, so replay is not equivalent to reading a frozen output. ([Docs by LangChain][11])

### Failure

```text
agent
 ↓
write file
 ↓
interrupt
 ↓
resume
 ↓
node runs again
 ↓
duplicate / overwrite / side effect
```

### Project Relevance

The workbench explicitly requires retries, approvals, correction and resumable execution.

### Implication

**Decision Status: Strong Candidate runtime retained; exactly-once execution rejected as an implicit assumption.**

Side effects must use:

* idempotency keys;
* transactional wrappers;
* effect receipts;
* separate action nodes;
* durable action state.

Example:

```text
Action ID = SHA(task + tool + parameters + version)

execute
 ↓
record effect
 ↓
checkpoint
```

On replay:

```text
Action ID already committed?
   yes → return existing result
   no  → execute
```

### Confidence

**High**

### Open Question

Which tool operations can realistically support transactional/idempotent semantics, especially filesystem and Office-artifact operations?

---

# 13. R5-12 — False completion is more dangerous than explicit failure

### Research Stream

R5 — Failure Research

### Research Topic

Agent task-completion failure

### Research Question

Can the agent conclude that a task is complete despite incomplete or incorrect work?

### Key Finding

**OBSERVATION:** Tool-use and enterprise-RAG benchmarks show that aggregate task success masks materially different failure behaviors, while agents can over-trust tool outputs and incomplete evidence. ([arXiv][9])

NIST also identifies confabulation and information-integrity failures in consequential settings, including fabricated supporting logic/citations. ([NIST Publications][6])

### Failure Pattern

```text
required steps = 8
completed = 5
 ↓
model writes polished answer
 ↓
“task completed”
```

No exception occurs.

### Implication

Completion must be **state-derived, not language-derived**.

The runtime should maintain:

```text
required outputs
required evidence
required tool actions
validation status
approval status
artifact status
```

Completion becomes:

```text
Completion = all mandatory predicates satisfied
```

rather than:

```text
Completion = LLM says "done"
```

### Confidence

**High**

### Open Question

How should mandatory completion predicates be generated for open-ended enterprise tasks without making the workflow excessively rigid?

---

# 14. R5-13 — Verification itself can fail

### Research Stream

R5 — Failure Research

### Research Topic

Verification-layer failure

### Research Question

Can an apparently successful validator approve a wrong output?

### Key Finding

**FACT:** Professional document benchmarks demonstrate that high-level answer correctness or structural validity can coexist with incorrect evidence selection, omitted footnotes and incorrect spatial associations. ([arXiv][3])

### Failure Mechanisms

A validator may:

* check syntax but not semantics;
* check a citation exists but not whether it supports the claim;
* verify formulas compile but not whether the formula is appropriate;
* validate slide count but not factual content;
* compare generated text to the wrong version of the source.

### Implication

R4's “verification layer” must itself be **multi-layered**:

```text
Schema
 ↓
Structural
 ↓
Evidence
 ↓
Semantic
 ↓
Numerical
 ↓
Policy
 ↓
Human approval
```

For high-consequence tasks, no single LLM judge should be considered authoritative.

### Confidence

**High**

### Open Question

Which validation properties can be made deterministic enough to eliminate LLM-as-judge dependence?

---

# 15. R5-14 — Sandboxing reduces blast radius but does not solve malicious execution by itself

### Research Stream

R5 — Failure Research

### Research Topic

Generated-code sandbox failure

### Research Question

Can gVisor or Firecracker alone make AI-generated code safe?

### Key Finding

**FACT:** gVisor is explicitly designed to reduce exposure of the host kernel by implementing a userspace kernel and intercepting system calls. Its own security documentation nevertheless emphasizes that sandboxing is not a substitute for secure system architecture. ([gVisor][12])

**FACT:** SandboxEscapeBench demonstrates that LLM agents can exploit vulnerable or misconfigured container environments. ([arXiv][13])

### Failure Classes

```text
misconfiguration
privilege exposure
host mounts
kernel/runtime vulnerability
credential exposure
network exposure
resource exhaustion
```

### Implication

R4's direction survives, but the hierarchy must be sharpened:

**Plain Docker**
→ unsuitable as sole boundary for hostile generated code.

**gVisor**
→ strong isolation candidate, but requires configuration validation and kernel/runtime maintenance.

**Firecracker**
→ stronger boundary for higher-assurance untrusted workloads, but not automatically secure.

### Critical Additional Finding

gVisor's own security material states that a sandbox is not a substitute for a secure architecture and that other host/API paths can remain exploitable. ([gVisor][12])

### Confidence

**High**

### Open Question

What threat class does the MVP actually need to defend against: accidental bad code, prompt-injected code, malicious user code, or deliberately hostile escape attempts?

---

# 16. R5-15 — Sandbox egress defeats the sovereignty model

### Research Stream

R5 — Failure Research

### Research Topic

Code-sandbox network escape

### Research Question

Can sandboxed code still leak confidential data?

### Key Finding

**FACT:** Sandbox isolation and network isolation are separate controls. gVisor's architecture protects the host from sandboxed processes but does not by itself mean the workload has no network route. ([gVisor][12])

### Failure

```text
safe filesystem boundary
+
unsafe network route
=
confidential-data exfiltration still possible
```

### Project Relevance

This directly affects the strongest product claim: sovereignty.

### Implication

The architecture must enforce:

```text
sandbox isolation
+
credential minimization
+
network default deny
+
host firewall
+
independent network observation
```

The application must not merely tell the sandbox “do not access the internet.”

### Confidence

**High**

### Open Question

What is the strongest independently auditable network-control design feasible on the single-server MVP?

---

# 17. R5-16 — Offline deployments can fail through dependency or supply-chain drift

### Research Stream

R5 — Failure Research

### Research Topic

Air-gapped operational failure

### Research Question

Can a nominally offline installation unexpectedly depend on components outside the isolated environment?

### Key Finding

**OBSERVATION:** R4's offline-supply-chain requirement is validated by the current agentic-security landscape: OWASP explicitly identifies agentic supply-chain vulnerabilities, while the GenAI security literature treats component integration and dependency integrity as risk areas. ([OWASP Gen AI Security Project][7])

### Failure Sources

* missing model file;
* runtime model download;
* OCR model download;
* package installation;
* container pull;
* license activation;
* telemetry endpoint;
* DNS lookup;
* update service;
* dependency version mismatch;
* CUDA/PyTorch/NCCL incompatibility.

### Severity

**High** when the failure is hidden and appears only on customer deployment.

### Implication

R4's offline registry requirement becomes **mandatory release engineering**.

A deployment package should have a dependency closure:

```text
OS
GPU driver
CUDA
Python/runtime
models
model processors
OCR assets
containers
packages
schemas
templates
certificates
licenses
configuration
```

All items should be versioned and integrity-checked.

### Confidence

**High**

### Open Question

Can the release process automatically prove that an offline package has complete dependency closure before it enters the isolated site?

---

# 18. R5-17 — Sovereignty claims can be false even when no obvious network call occurs

### Research Stream

R5 — Failure Research

### Research Topic

Zero-egress proof failure

### Research Question

Does application logging prove that confidential information remained inside the environment?

### Key Finding

**INFERENCE:** No. Application telemetry alone observes only the paths instrumented by the application.

A hidden dependency could exist in:

* DNS;
* package managers;
* model initialization;
* telemetry libraries;
* OS services;
* container runtime;
* GPU/runtime components;
* error-reporting code;
* another process on the host.

This directly follows R4's conclusion that sovereignty must be measured rather than asserted, and is consistent with the supplied security proof model.  

### Implication

The proof must have independent layers:

```text
Application evidence
        +
Host enforcement
        +
Network observation
        +
DNS observation
        +
Controlled adversarial test
```

And the system should distinguish:

> **“No outbound traffic observed under test conditions”**

from the stronger claim:

> **“Outbound communication is technically impossible under the enforced network policy.”**

The second requires a stronger architecture.

### Confidence

**High**

### Open Question

What level of assurance will the target customer require before accepting “sovereign / zero-egress” as a technical claim?

---

# 19. R5-18 — Lower-layer dependency failures can masquerade as AI failures

### Research Stream

R5 — Failure Research

### Research Topic

Cross-layer infrastructure failure

### Research Question

Can a failure attributed to the AI runtime actually originate below it?

### Key Finding

**OBSERVATION:** Current serving incidents illustrate failures caused by interactions between inference engines, CUDA, NCCL, hardware architecture and multimodal execution rather than by the model itself.

The practical implication is that:

```text
Model
Inference engine
PyTorch
CUDA
NCCL
GPU driver
Kernel
Hardware
```

form one operational dependency chain.

### Project Relevance

On a single-server system, there may be no redundant cluster to absorb a lower-layer failure.

### Implication

The workbench must record the full execution environment for each incident:

```text
model hash
engine version
container digest
CUDA
PyTorch
NCCL
driver
kernel
GPU identity
request profile
```

Otherwise diagnosis becomes guesswork.

### Confidence

**High**

### Open Question

What minimum environment fingerprint is required for deterministic incident reproduction and customer support?

---

# 20. Cross-Cutting Failure Matrix

| Failure class                    | Severity    |              Detectability | Required control                             | Residual risk               |
| -------------------------------- | ----------- | -------------------------: | -------------------------------------------- | --------------------------- |
| Engine OOM                       | High        |                       High | admission/resource guard + supervisor        | rare unpredicted peak       |
| GPU contention                   | High        |                       High | scheduler + quotas                           | prediction error            |
| VLM runtime regression           | High        |                     Medium | version pinning + soak tests                 | future regression           |
| OCR/table corruption             | High        |                        Low | structured validation + evidence provenance  | undetected semantic error   |
| P&ID relationship error          | Very High   |                        Low | graph/coordinate evidence + human review     | domain ambiguity            |
| Stale retrieval                  | High        |                     Medium | revision/time-aware ranking                  | bad metadata                |
| ACL leakage                      | Critical    | High if enforced correctly | pre-retrieval authorization                  | policy/configuration defect |
| Prompt injection                 | Critical    |                        Low | least agency + typed tools + isolation       | novel injection             |
| Tool misuse                      | High        |                     Medium | policy + typed schemas                       | semantic misuse             |
| Tool output corruption           | High        |                        Low | outcome contracts/monitors                   | unknown semantic anomaly    |
| Retry loop                       | Medium–High |                       High | bounded recovery state machine               | misclassification           |
| Duplicate side effect            | High        |                       High | idempotency/effect receipts                  | non-idempotent legacy tool  |
| False completion                 | High        |                        Low | explicit completion predicates               | incompletely specified task |
| Verification failure             | High        |                        Low | layered deterministic + human validation     | validator blind spots       |
| Sandbox escape                   | Critical    |                     Medium | gVisor/Firecracker + hardening               | zero-day/configuration      |
| Sandbox egress                   | Critical    |                       High | default-deny + host firewall + observation   | host compromise             |
| Offline dependency drift         | High        |                     Medium | signed bundles + dependency closure          | update-process defect       |
| Zero-egress proof gap            | Critical    |                     Medium | independent enforcement/measurement          | unobserved path             |
| Lower-layer infrastructure fault | High        |                     Medium | environment fingerprint + health supervision | difficult RCA               |

---

# R5 Established Findings

## EF-01 — The most dangerous failures are semantically plausible

Explicit exceptions are easier to handle than:

* wrong-but-valid OCR;
* stale-but-authoritative-looking documents;
* wrong-session evidence;
* corrupted tool outputs;
* plausible VLM interpretations;
* polished but incomplete artifacts.

This is the strongest cross-study result emerging from the failure research. ([arXiv][1])

## EF-02 — Grounding is necessary but not sufficient

A citation, retrieved document or valid tool response does not establish correctness. Freshness, authority, permission, session integrity and semantic validity must also be checked. ([arXiv][1])

## EF-03 — Agent reliability is not equivalent to model intelligence

ToolMaze, ToolBench-X and ToolFailBench all point toward distinct failure modes involving tool choice, result interpretation and recovery. Larger models do not automatically eliminate these system-level failures. ([arXiv][8])

## EF-04 — Durable execution requires idempotent effects

Checkpointing solves state persistence; it does not automatically solve duplicate side effects. ([Docs by LangChain][10])

## EF-05 — Multimodal document processing remains a significant reliability bottleneck

Professional-document benchmarks continue to expose serious failures in tables, charts, spatial reasoning, footnotes, amendments, scans and visual grounding. ([arXiv][3])

## EF-06 — P&ID reasoning requires more structure than generic VLM prompting

Engineering diagrams contain topology and relationships that should not be left entirely to unconstrained visual-language inference. ([arXiv][4])

## EF-07 — Sandbox and sovereignty are independent security properties

A sandbox can protect the host while still permitting confidential information to leave through an available network path. gVisor itself frames sandboxing as only one part of secure architecture. ([gVisor][12])

## EF-08 — Failure containment is more important than assuming component reliability

The architecture should be designed so that an individual model, parser, tool, agent node or validator can fail without silently promoting the failure downstream.

---

# Relevant Findings

R5 materially changes the implementation interpretation of the R4 architecture:

| R4 decision              | R5 result                                                                     |
| ------------------------ | ----------------------------------------------------------------------------- |
| Model Gateway            | **Strengthened**                                                              |
| vLLM                     | **Retain as candidate; require resource/admission controls and soak testing** |
| llama.cpp                | **Retain as compatibility/low-resource option**                               |
| SGLang                   | **Still requires validation**                                                 |
| Quantization             | **Retain; evaluate quality + peak memory, not weight size only**              |
| Hybrid retrieval         | **Retain, add authority/freshness/session controls**                          |
| OpenSearch/Vespa         | **Selection must include stale/conflict/ACL fault testing**                   |
| Docling/OCR              | **Retain, but introduce semantic parsing validation**                         |
| Qwen3-VL                 | **Strong candidate, not trusted as canonical engineering truth**              |
| LangGraph                | **Retain as runtime candidate; idempotency is mandatory**                     |
| Typed tools              | **Strengthened to typed tools + outcome contracts**                           |
| gVisor                   | **Strong candidate, threat-model dependent**                                  |
| Firecracker              | **Higher-assurance candidate strengthened**                                   |
| Docker-only              | **Further rejected**                                                          |
| Deterministic artifacts  | **Strongly validated by failure research**                                    |
| Artifact validation      | **Must validate semantics, not only structure**                               |
| Offline registry         | **Mandatory and security-critical**                                           |
| Zero-egress verification | **Must use independent enforcement + measurement**                            |

---

# Rejected / Inadequate Approaches

### RA-01 — “Retry until it works”

**Rejected.**

Implicit failures can cause agents to repeat incorrect actions and enter futile recovery loops. ([arXiv][8])

### RA-02 — “Citation means grounded means correct”

**Rejected.**

Stale, wrong-session and unauthorized evidence can remain apparently grounded. ([arXiv][1])

### RA-03 — “VLM can be the sole source of truth for drawings”

**Rejected.**

Visual models can identify content without reliably recovering engineering relationships.

### RA-04 — “Checkpointing provides exactly-once effects”

**Rejected.**

Replay/resume semantics require idempotent side effects. ([Docs by LangChain][10])

### RA-05 — “A valid tool response is a trustworthy tool result”

**Rejected.**

Semantic corruption can preserve schema validity. ([arXiv][9])

### RA-06 — “Sandboxed means sovereign”

**Rejected.**

Network egress is independent of process isolation. ([gVisor][12])

### RA-07 — “No observed network traffic proves zero egress”

**Rejected.**

Observation is not the same as enforcement.

### RA-08 — “A syntactically valid artifact is a successful artifact”

**Rejected.**

Document semantics, evidence, formulas and source correctness require additional validation. ([arXiv][3])

---

# Failure / Risk Findings

The highest-risk failure chain is:

```text
Untrusted document
      ↓
Prompt injection / parsing corruption
      ↓
Wrong retrieval or wrong evidence
      ↓
LLM forms plausible plan
      ↓
Agent selects valid tool
      ↓
Tool returns valid-looking but wrong result
      ↓
Agent fails to diagnose anomaly
      ↓
Artifact generated
      ↓
Superficial validator passes
      ↓
Human trusts polished result
```

This is substantially more dangerous than a simple model hallucination because **every individual interface can appear healthy**.

The second critical chain is:

```text
Constrained GPU
 ↓
VLM + LLM + cache contention
 ↓
latency / OOM
 ↓
engine failure
 ↓
agent retry
 ↓
queue amplification
 ↓
system-wide degradation
```

The third is:

```text
Agent
 ↓
sandbox
 ↓
network path
 ↓
credential/data access
 ↓
exfiltration
```

R5 therefore establishes a general principle:

> **The system must fail closed at trust-boundary crossings and fail soft at infrastructure boundaries.**

---

# Open Questions

1. What exact GPU and VRAM envelope defines the safe MVP operating region?
2. What maximum image count, image resolution and context length can be admitted safely?
3. What inference-service failure should trigger request rejection versus worker restart versus model fallback?
4. Which document fields require deterministic validation before entering the knowledge index?
5. What is the minimum P&ID graph fidelity required for engineering reasoning?
6. How should stale and conflicting documents be resolved when metadata is incomplete?
7. What semantic outcome contracts are practical for each local tool?
8. How should failure diagnosis be separated from agent recovery?
9. Which filesystem/spreadsheet operations can be made idempotent?
10. What completion predicates can be derived automatically for open-ended tasks?
11. Which artifact checks can be deterministic rather than model-judged?
12. What exact threat model determines gVisor versus Firecracker?
13. What credentials, if any, can safely enter a code-execution sandbox?
14. What independent network evidence is sufficient for the target customer's assurance level?
15. What dependency-closure test proves an installation is truly offline?
16. What cross-layer environment fingerprint is necessary for reproducible incident analysis?

---

# Architecture / Engineering Questions Passed to R6

R5 narrows the innovation problem considerably. R6 should not search for novelty for its own sake; it should search for solutions to these specific failure bottlenecks, consistent with the sequential research design. 

### A. Failure-aware inference

Can resource-aware model routing predict **peak** GPU usage rather than only model weight size?

Can a small local model act as a **resource/admission controller** before a large VLM/LLM is invoked?

Can model serving be made failure-isolated enough that one request cannot kill the service?

### B. Self-validating retrieval

Can retrieval systems jointly score:

```text
relevance
+
authority
+
freshness
+
permission
+
evidence completeness
```

rather than treating retrieval as one ranking problem?

Can the system identify **evidence insufficiency** before generation?

### C. Structured multimodal reasoning

Can P&IDs and similar engineering drawings be represented as:

```text
OCR
+
coordinates
+
entities
+
graph
+
image evidence
```

and allow the LLM to reason over the combined representation?

### D. Failure-aware agents

Can an agent maintain an explicit:

```text
hypothesis of failure
+
evidence
+
recovery options
+
expected outcome
```

instead of blindly retrying?

Can outcome monitors detect semantically invalid tool results before they reach the planner?

### E. Verifiable execution

Can agent actions be represented as a **typed execution plan** with preconditions, postconditions and effect receipts?

Can replay semantics approach exactly-once behavior through durable effect identities?

### F. Verifiable artifacts

Can the artifact layer produce machine-checkable provenance:

```text
artifact claim
 ↓
source evidence
 ↓
document/page/location
 ↓
validation result
```

for every consequential claim?

### G. Sovereignty proof

Can the system generate a cryptographically bound execution record combining:

```text
task
+
model hashes
+
tool calls
+
source hashes
+
artifact hashes
+
network policy
+
observed traffic
+
approval events
```

while independently proving network isolation?

### H. Sandbox assurance

Can workload risk be classified dynamically so that:

```text
trusted local transformation → lighter isolation
untrusted generated code     → gVisor
high-assurance execution     → Firecracker
```

without weakening the security boundary through policy errors?

---

# R5 Final Assessment

The R4 architecture should **not be discarded**. The failure research instead shows that its contracts need stronger semantics.

The architecture emerging after R5 is:

```text
UI
 ↓
Policy / Identity
 ↓
Task Admission
 ↓
Resource-Aware Model Router
 ↓
Model Gateway
 ↓
Durable Agent Runtime
 ↓
Typed Tools + Outcome Contracts
 ↓
Document / Retrieval / Multimodal Evidence
 ↓
Independent Verification
 ↓
Deterministic Artifact Engine
 ↓
Approval / Release Gate
 ↓
Audit + Sovereignty Evidence
```

The most important architectural shift is this:

> **Do not design the system around components that are assumed to be correct. Design it around components whose failures can be detected, contained, attributed and prevented from silently propagating.**

That is the principal failure-research result to carry into R6.

[1]: https://arxiv.org/abs/2607.27353?utm_source=chatgpt.com "LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation"
[2]: https://docs.vllm.ai/en/latest/usage/metrics/?utm_source=chatgpt.com "Production Metrics - vLLM"
[3]: https://arxiv.org/abs/2607.11192?utm_source=chatgpt.com "GDP.pdf: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents"
[4]: https://arxiv.org/abs/2603.22528?utm_source=chatgpt.com "GraphRAG for Engineering Diagrams: ChatP&ID Enables LLM Interaction with P&IDs"
[5]: https://arxiv.org/abs/2604.14227?utm_source=chatgpt.com "FRESCO: Benchmarking and Optimizing Re-rankers for Evolving Semantic Conflict in Retrieval-Augmented Generation"
[6]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf?utm_source=chatgpt.com "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile"
[7]: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/?utm_source=chatgpt.com "OWASP Top 10 for Agentic Applications for 2026 - OWASP Gen AI Security Project"
[8]: https://arxiv.org/abs/2606.05806?utm_source=chatgpt.com "When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents"
[9]: https://arxiv.org/abs/2606.25819?utm_source=chatgpt.com "Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability"
[10]: https://docs.langchain.com/oss/python/langgraph/interrupts?utm_source=chatgpt.com "Interrupts - Docs by LangChain"
[11]: https://docs.langchain.com/oss/python/langgraph/use-time-travel?utm_source=chatgpt.com "Use time-travel - Docs by LangChain"
[12]: https://gvisor.dev/docs/architecture_guide/security/?utm_source=chatgpt.com "Security Model - gVisor"
[13]: https://arxiv.org/abs/2603.02277?utm_source=chatgpt.com "Quantifying Frontier LLM Capabilities for Container Sandbox Escape"
