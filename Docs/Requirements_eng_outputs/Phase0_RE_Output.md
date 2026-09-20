
# Phase 0 — Research Closure & Evidence Consolidation

# 1. Executive Decision

## Phase-0 Gate: **B. READY WITH TARGETED VALIDATION**

### Decision

**The research is sufficient to begin product-definition and requirements-engineering work.**

However, several high-risk parameters must remain explicitly marked **Requires Validation** rather than being silently frozen into the PRD.

This is **not** a “NOT READY” situation.

The research establishes enough to define:

* the problem;
* target users and organizations;
* core workflows;
* product purpose;
* major capabilities;
* MVP boundaries;
* security principles;
* sovereignty requirements;
* data requirements;
* agent behavior requirements;
* verification requirements;
* artifact requirements;
* observability requirements;
* broad hardware constraints;
* competitive expectations.

The remaining uncertainty is primarily about **exact thresholds, deployment-specific policies, technology selection, customer-specific workflows, and acceptance benchmarks**.

That is precisely the type of uncertainty that should be resolved during requirements engineering and targeted validation—not by reopening the entire research program.

The Phase-0 prompt explicitly permits this outcome: unresolved questions do not block product definition unless they prevent defining what the product must do. 

---

# 2. Research Coverage

The research pipeline was intentionally sequential rather than independent. The workflow defines:

**R1 User → R2 Market → R3 Competitor → R4 Technical → R5 Failure → R6 Innovation → R7 Data → R8 Regulatory/Security.**

Each later stream inherits the relevant accumulated evidence from earlier streams. 

| Stream             | Investigated                                                                      | Major contribution                                    | Evidence state |
| ------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- |
| **R1 User**        | users, workflows, pain points, current workarounds, expectations                  | establishes actual enterprise knowledge-work problems | Strong         |
| **R2 Market**      | market, adoption, industrial constraints, AI adoption                             | establishes commercial/environmental context          | Strong–Medium  |
| **R3 Competitor**  | direct/indirect alternatives, capabilities, gaps                                  | establishes expected capability baseline              | Strong–Medium  |
| **R4 Technical**   | local inference, RAG, VLM, document AI, agents, sandbox, artifacts, observability | establishes feasible technical mechanisms             | Strong–Medium  |
| **R5 Failure**     | failure modes, attack paths, operational failures                                 | establishes containment/verification requirements     | Strong         |
| **R6 Innovation**  | routing, verification, provenance, adaptive execution                             | identifies differentiation mechanisms                 | Medium–Strong  |
| **R7 Data**        | data classes, P&IDs, provenance, temporal data, retrieval, evaluation data        | establishes evidence/data requirements                | Strong         |
| **R8 Security**    | sovereignty, privacy, CII/OT, supply chain, AI security, audit                    | establishes security/regulatory boundary              | Strong         |
| **R10 Evaluation** | not yet completed as an independent stream                                        | major future requirement dependency                   | **Gap**        |
| **R11 Abuse**      | not yet completed as an independent stream                                        | important security/agent-abuse dependency             | **Gap**        |

The research-stream definition itself identifies R10 Evaluation Science and R11 Abuse/Adversarial Research as distinct future streams. 

### Important distinction

R10/R11 are **not blockers for defining the product**.

They become important for defining the **exact acceptance criteria and security qualification criteria**.

---

# 3. Research-Process Assessment

The research methodology itself is sufficiently mature for transition.

The project requires:

* primary/credible sources;
* source reading rather than snippet reliance;
* evidence ledgers;
* explicit uncertainty;
* negative findings;
* alternative comparison;
* real-world constraints;
* traceability;
* confidence classification. 

The prerequisite schema additionally establishes the evidence hierarchy:

1. official technical documentation;
2. research papers;
3. standards/government documentation;
4. technical reports;
5. reproducible engineering evaluations;
6. independent technical analysis;
7. vendor material;
8. community discussion.

Vendor claims are not independent validation, and search snippets are not evidence. 

That distinction is important because some R3/R4/R6 conclusions remain **candidate decisions**, not facts.

---

# 4. Established Findings

Only findings with sufficient support are included here.

## EF-01 — The core problem is confidential enterprise knowledge work

**Classification:** FACT / OBSERVATION
**Streams:** R1, R2
**Confidence:** High

Organizations possess sensitive engineering, business, operational, financial and software information that cannot always be safely processed through public AI services.

The product definition explicitly identifies P&IDs, engineering drawings, inspection reports, calculations, approval notes, presentations, correspondence, financial information, source code, SOPs and historical organizational knowledge as target material. 

### Product implication

The product is not fundamentally a “local chatbot.”

It is a **confidential enterprise knowledge-work execution environment**.

---

## EF-02 — Sovereignty is a core product requirement

**Classification:** FACT / INFERENCE
**Streams:** R1, R4, R5, R8
**Confidence:** High

Confidential information must remain inside the controlled environment, and core operation cannot depend on external AI APIs.

The project constraints explicitly require local processing, multiple open-weight models, sandboxed code execution, observable/controllable agents, multimodal processing and realistic enterprise hardware. 

### Product implication

“Local inference” is insufficient.

The product must provide **technically demonstrable sovereignty**.

---

## EF-03 — The system must support multimodal technical knowledge

**Classification:** INFERENCE supported by multiple evidence streams
**Streams:** R1, R4, R7
**Confidence:** High

Text-only RAG cannot adequately represent:

* P&IDs;
* engineering drawings;
* tables;
* scanned documents;
* figures;
* layouts;
* visual relationships.

R7 resolves the P&ID representation as:

> image = observation
> OCR/layout = extracted evidence
> engineering graph = structural representation
> domain rules = semantic interpretation
> human engineer = consequential authority. 

### Product implication

Multimodality is not a decorative capability. It is a core requirement.

---

## EF-04 — Enterprise knowledge must preserve source authority and revision

**Classification:** INFERENCE
**Streams:** R1, R5, R7
**Confidence:** High

Semantic relevance alone cannot establish that a document is current or authoritative.

The knowledge layer therefore requires document identity, revision, effective dates, authority, ownership and source-system metadata. 

### Product implication

The product must distinguish:

```text
relevant
current
authoritative
authorized
validated
```

rather than treating retrieval similarity as truth.

---

## EF-05 — Knowledge derived by AI cannot automatically become authoritative knowledge

**Classification:** INFERENCE
**Streams:** R5, R7
**Confidence:** High

R7 establishes the state progression:

```text
RAW
→ PARSED
→ CANDIDATE
→ VALIDATED
→ APPROVED
```

with additional states such as SUPERSEDED, CONFLICTED and UNVERIFIABLE. 

### Product implication

The product needs explicit knowledge/evidence states and validation boundaries.

---

## EF-06 — Retrieval must be evidence-governed

**Classification:** INFERENCE
**Streams:** R5, R6, R7
**Confidence:** High

R7 establishes an evidence sufficiency gate based on predicates such as:

* entity resolved;
* property resolved;
* current revision;
* authoritative source;
* value;
* unit;
* no unresolved conflict.

Possible outcomes include:

```text
SUFFICIENT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
UNVERIFIABLE
```



### Product implication

The agent must be able to **abstain, retrieve more evidence, escalate, or ask the user**.

---

## EF-07 — Agent authority must remain outside the LLM

**Classification:** INFERENCE
**Streams:** R5, R6, R8
**Confidence:** High

The research establishes that enterprise documents can contain adversarial instructions and that agents can be manipulated through their data plane.

The resulting control principle is:

```text
User
 ↓
Policy
 ↓
Security Context
 ↓
Allowed Capability
 ↓
Agent
 ↓
Tool Request
 ↓
Policy Re-check
 ↓
Execution
```

not:

```text
Agent → decide its own permissions
```

R8 explicitly establishes this distinction. 

### Product implication

Authorization is an independent system responsibility.

---

## EF-08 — Air-gapping does not eliminate AI security risk

**Classification:** FACT / INFERENCE
**Streams:** R5, R8
**Confidence:** High

Air-gapping reduces external communication/exfiltration paths, but does not prevent:

* prompt injection;
* malicious documents;
* tool manipulation;
* privilege escalation;
* malicious generated code;
* local supply-chain compromise;
* sandbox escape.

R8 explicitly distinguishes the control plane from the data plane for this reason. 

### Product implication

Security must be built around **containment and least privilege**, not simply network disconnection.

---

## EF-09 — Generated code requires isolated execution

**Classification:** INFERENCE
**Streams:** R4, R5, R8
**Confidence:** High

Generated code is inherently an untrusted execution surface.

The research rejects plain Docker as the sole hostile-code boundary and identifies stronger isolation plus independent network controls as necessary. 

### Product implication

Code execution must have:

* isolation;
* resource limits;
* restricted filesystem;
* restricted credentials;
* network isolation;
* output validation;
* execution records.

---

## EF-10 — Verification must be layered

**Classification:** INFERENCE
**Streams:** R5, R6
**Confidence:** High

No single verifier is sufficient.

The research establishes the need for combinations of:

```text
deterministic validation
+
semantic/model validation
+
human approval where consequence warrants it
```

### Product implication

“Generated successfully” cannot equal “correct.”

---

## EF-11 — Provenance is required at evidence/claim level

**Classification:** INFERENCE
**Streams:** R6, R7
**Confidence:** High

R7 establishes source → processing → evidence → derived fact → claim → decision → artifact provenance. 

### Product implication

The user should be able to trace important output back to source evidence.

---

## EF-12 — Data heterogeneity matters more than raw document count

**Classification:** INFERENCE
**Stream:** R7
**Confidence:** High

A small heterogeneous corpus can be more demanding than a large homogeneous corpus.

R7 therefore recommends representative evaluation rather than arbitrary document volume. 

### Product implication

Acceptance testing must be based on **representative workflows and difficult cases**, not only dataset size.

---

## EF-13 — Customer-local data is required for production qualification

**Classification:** INFERENCE
**Stream:** R7
**Confidence:** High

Public/synthetic data can support development, regression and initial model selection, but cannot represent a specific customer's:

* terminology;
* revisions;
* authority hierarchy;
* ACLs;
* P&ID conventions;
* workflow;
* organizational history.

R7 explicitly identifies customer-owned data as mandatory for production qualification. 

### Product implication

Customer onboarding must include an evaluation/adaptation phase.

---

## EF-14 — Sovereignty includes the software/model supply chain

**Classification:** FACT / INFERENCE
**Stream:** R8
**Confidence:** High

A disconnected runtime can still consume compromised or unapproved:

* models;
* containers;
* packages;
* drivers;
* OCR models;
* inference engines;
* dependencies.

R8 therefore identifies signed release manifests, SBOM/AIBOM, VEX and offline verification as important controls. 

### Product implication

Release management becomes part of the sovereignty product.

---

## EF-15 — CII/OT deployments require a separate risk boundary

**Classification:** FACT / INFERENCE
**Stream:** R8
**Confidence:** High

The evidence does not support treating the Workbench as an unrestricted autonomous controller of OT/ICS environments.

R8 explicitly recommends analysis of OT/engineering information while avoiding free-form autonomous manipulation of PLC/DCS/SIS/process-control state. 

### Product implication

OT integration must be explicitly bounded.

---

# 5. Relevant but Non-Decisive Findings

These are important, but should **not yet become hard product decisions**.

| Finding                           | Confidence        | Why relevant                            | Decision affected         | Required validation            |
| --------------------------------- | ----------------- | --------------------------------------- | ------------------------- | ------------------------------ |
| Hierarchical model routing        | Medium-High       | may improve quality/resource efficiency | model orchestration       | workload benchmark             |
| Small specialist model portfolio  | Medium            | could fit mid-range GPU better          | model strategy            | actual GPU benchmark           |
| vLLM as primary serving candidate | Medium-High       | technically strong candidate            | serving layer             | deployment benchmark           |
| llama.cpp as compatibility path   | Medium            | useful for constrained models           | serving layer             | model-specific test            |
| OpenSearch hybrid retrieval       | Medium-High       | strong enterprise retrieval candidate   | knowledge layer           | corpus benchmark               |
| Docling document representation   | High              | structurally useful                     | document processing       | customer corpus test           |
| Qwen3-VL family                   | Medium            | strong multimodal candidate             | VLM selection             | engineering-document benchmark |
| LangGraph                         | Medium-High       | useful durable workflow mechanism       | agent runtime             | workflow complexity test       |
| gVisor                            | Medium-High       | plausible MVP sandbox                   | code execution            | escape/performance test        |
| Firecracker                       | Medium-High       | stronger isolation option               | high-assurance deployment | operational complexity test    |
| provenance graph                  | High conceptually | supports auditability                   | evidence layer            | usability/performance test     |
| proof-carrying action envelope    | Medium-High       | useful consequential-action evidence    | execution layer           | schema/prototype test          |
| dynamic constrained workflows     | Medium            | potentially strong differentiator       | orchestration             | reproducibility test           |
| physical/unidirectional isolation | Medium            | high-assurance sovereignty              | defence deployment        | customer/security assessment   |

The prerequisite framework specifically warns against freezing technologies simply because they appear impressive; technologies may remain **Requires Validation**. 

---

# 6. Rejected Approaches

## RA-01 — Generic cloud AI assistant as core architecture

**Rejected**

Violates the sovereignty constraint.

---

## RA-02 — “Local chatbot + vector database”

**Rejected as the product definition**

Insufficient for:

* multimodal technical documents;
* authority/version reasoning;
* controlled actions;
* verification;
* artifacts;
* auditability;
* agent execution.

---

## RA-03 — Image-only P&ID reasoning

**Rejected**

R7 evidence supports combining visual observation with structured engineering relationships. 

---

## RA-04 — OCR-only engineering understanding

**Rejected**

OCR loses important topology/layout/visual information.

---

## RA-05 — Universal fixed-size chunking

**Rejected**

The correct retrieval unit varies by content type. 

---

## RA-06 — LLM extraction → authoritative truth

**Rejected**

Derived knowledge must remain traceable and pass validation states.

---

## RA-07 — One scalar confidence score

**Rejected**

Confidence cannot simultaneously represent:

* authority;
* freshness;
* authorization;
* extraction quality;
* semantic correctness;
* provenance;
* consistency.

R7 explicitly establishes a multidimensional quality vector. 

---

## RA-08 — One giant model for everything

**Rejected**

The evidence favors a multi-model architecture, while exact model selection remains validation-dependent. 

---

## RA-09 — Dozens of tiny specialists

**Rejected**

Creates orchestration complexity without established evidence that the additional complexity is justified.

---

## RA-10 — Autonomous agent with unrestricted tools

**Rejected**

Violates least-privilege and security requirements.

---

## RA-11 — Model decides its own authorization

**Rejected**

Authorization must be external to model reasoning.

---

## RA-12 — Retry-until-success

**Rejected**

R5 established that blind retries can create loops and conceal semantic failure.

---

## RA-13 — Citation = correctness

**Rejected**

A cited document can still be stale, unauthorized, incorrectly interpreted or internally contradictory.

---

## RA-14 — Checkpointing = exactly-once execution

**Rejected**

Durable state does not automatically guarantee exactly-once external side effects.

---

## RA-15 — Docker alone as hostile-code sandbox

**Rejected**

Insufficient isolation for the required security model.

---

## RA-16 — “Observed no traffic” = zero-egress proof

**Rejected**

Observation must be combined with enforced network controls and adversarial testing.

---

## RA-17 — Complete enterprise digital twin in MVP

**Rejected**

Excessive scope and unnecessary for validating the initial product hypothesis.

---

## RA-18 — Giant universal enterprise ontology

**Rejected**

Too broad and not necessary to deliver initial workflows.

---

## RA-19 — Public datasets as production qualification

**Rejected**

Customer-local data is required for final qualification.

---

# 7. Technology / Approach Decision Register

This is intentionally **not** a final architecture decision register.

| Technology / approach                | Status                             | Why                                                  |
| ------------------------------------ | ---------------------------------- | ---------------------------------------------------- |
| Multi-model architecture             | **Preferred**                      | matches heterogeneous workload/resource requirements |
| Hierarchical routing                 | **Strong Candidate**               | task → capability → step → verification escalation   |
| Adaptive resource-aware routing      | **Strong Candidate**               | hardware state materially affects inference          |
| vLLM                                 | **Strong Candidate**               | strong local serving option                          |
| llama.cpp                            | **Candidate / Strong Candidate**   | useful compatibility path                            |
| SGLang                               | **Requires Validation**            | promising but insufficient project-specific evidence |
| Hybrid retrieval                     | **Preferred**                      | lexical + semantic + metadata/structure              |
| OpenSearch                           | **Strong Candidate**               | enterprise search + filtering                        |
| Vespa                                | **Requires Validation**            | powerful but potentially greater complexity          |
| Docling                              | **Strong Candidate**               | structured document representation                   |
| PaddleOCR                            | **Candidate**                      | specialized OCR path                                 |
| Qwen3-VL                             | **Strong Candidate**               | multimodal technical-document candidate              |
| LangGraph                            | **Strong Candidate**               | durable stateful workflow candidate                  |
| Semantic Kernel Process Framework    | **Requires Validation**            | maturity/fit uncertainty                             |
| gVisor                               | **Strong Candidate**               | MVP sandbox candidate                                |
| Firecracker                          | **Strong Candidate**               | higher-assurance isolation candidate                 |
| Plain Docker sandbox                 | **Rejected as sole boundary**      | inadequate assurance                                 |
| Programmatic Office generation       | **Preferred**                      | deterministic artifact construction                  |
| LLM-only artifact generation         | **Rejected**                       | insufficient structural assurance                    |
| Provenance graph                     | **Strong Candidate**               | evidence/claim traceability                          |
| Evidence sufficiency gate            | **Preferred**                      | prevents unsupported reasoning                       |
| Proof-carrying action envelope       | **Strong Candidate**               | action accountability                                |
| Full cryptographic neural proof      | **Requires Validation / Research** | excessive MVP complexity                             |
| Dynamic constrained workflow grammar | **Strong Candidate**               | adaptive execution without unrestricted autonomy     |
| Full autonomous OT control           | **Rejected for MVP**               | unacceptable consequence/risk                        |

The distinction between technology **status** and final architectural selection is deliberate and follows the project requirement that technologies remain “Requires Validation” when evidence is insufficient. 

---

# 8. Known Constraint Register

## Product Constraints

| Constraint                                               | Type                 |
| -------------------------------------------------------- | -------------------- |
| Confidential enterprise knowledge work                   | **Hard**             |
| Target industrial/government/defence-linked environments | **Hard direction**   |
| P&IDs and engineering drawings                           | **Hard capability**  |
| Technical/scanned documents                              | **Hard capability**  |
| Internal knowledge and correspondence                    | **Hard capability**  |
| Artifact generation                                      | **Hard capability**  |
| Agentic multi-step execution                             | **Hard**             |
| Consumer/mobile-first product                            | **Out of scope MVP** |
| Giant model training                                     | **Out of scope MVP** |
| Massive distributed GPU infrastructure                   | **Out of scope MVP** |

---

## Sovereignty Constraints

| Constraint                              | Type     |
| --------------------------------------- | -------- |
| Data stays in controlled infrastructure | **Hard** |
| No external AI API dependency           | **Hard** |
| Local inference                         | **Hard** |
| Local document processing               | **Hard** |
| Controlled network connectivity         | **Hard** |
| Demonstrable zero-egress posture        | **Hard** |
| Offline model/artifact management       | **Hard** |
| Sovereignty evidence                    | **Hard** |

The project's prerequisite schema explicitly establishes these sovereignty constraints. 

---

## Hardware Constraints

| Constraint                              | Type                    |
| --------------------------------------- | ----------------------- |
| Single workstation/server demonstration | **Hard MVP boundary**   |
| Mid-range GPU preference                | **Soft**                |
| GPU memory must be measured             | **Requires Validation** |
| CPU/RAM requirements                    | **Requires Validation** |
| Storage requirements                    | **Requires Validation** |
| Concurrent workload limits              | **Requires Validation** |
| Model residency strategy                | **Requires Validation** |
| KV-cache limits                         | **Requires Validation** |

---

## Security Constraints

| Constraint                              | Type                                             |
| --------------------------------------- | ------------------------------------------------ |
| Agent permissions controlled externally | **Hard**                                         |
| Tool permissions controlled             | **Hard**                                         |
| Code sandboxing                         | **Hard**                                         |
| Prompt-injection containment            | **Hard**                                         |
| Malicious document handling             | **Hard**                                         |
| Data-exfiltration prevention            | **Hard**                                         |
| Auditability                            | **Hard**                                         |
| Provenance                              | **Hard for consequential outputs**               |
| Secrets isolation                       | **Hard**                                         |
| Supply-chain control                    | **Hard for regulated/high-security deployments** |

---

# 9. Failure Mode Register

| ID    | Failure                | Cause                        | Impact                 | Detection               | Mitigation                        | Requirement implication      |
| ----- | ---------------------- | ---------------------------- | ---------------------- | ----------------------- | --------------------------------- | ---------------------------- |
| FM-01 | hallucinated answer    | model error                  | wrong decision         | evidence/verifier       | grounded generation + abstention  | answer must expose evidence  |
| FM-02 | stale retrieval        | old revision ranked highly   | obsolete decision      | temporal checks         | revision/authority filtering      | temporal retrieval           |
| FM-03 | unauthorized retrieval | ACL failure                  | confidentiality breach | authorization check     | permission-aware retrieval        | ACL enforcement              |
| FM-04 | wrong P&ID topology    | VLM interpretation           | engineering error      | graph consistency       | structured representation         | topology validation          |
| FM-05 | OCR corruption         | scan/layout quality          | wrong extracted value  | extraction QA           | OCR + visual validation           | source-region provenance     |
| FM-06 | incomplete evidence    | insufficient retrieval       | unsupported answer     | sufficiency gate        | retrieve/refuse/escalate          | evidence gate                |
| FM-07 | prompt injection       | malicious enterprise content | agent manipulation     | adversarial tests       | control/data separation           | untrusted content handling   |
| FM-08 | tool misuse            | excessive agency             | unauthorized action    | policy trace            | external authorization            | tool policy                  |
| FM-09 | semantic tool error    | valid but wrong output       | downstream corruption  | result verification     | typed outputs                     | tool validation              |
| FM-10 | infinite retry         | retry policy                 | resource exhaustion    | retry counters          | failure classification            | bounded recovery             |
| FM-11 | false completion       | LLM says “done”              | incomplete workflow    | state predicates        | predicate-based completion        | explicit completion criteria |
| FM-12 | sandbox escape         | runtime vulnerability        | host compromise        | escape testing          | stronger isolation                | sandbox boundary             |
| FM-13 | egress attempt         | malicious code/tool          | data leakage           | network telemetry       | host/network enforcement          | zero-egress test             |
| FM-14 | dependency compromise  | supply chain                 | system compromise      | artifact verification   | signed bundles/SBOM               | release qualification        |
| FM-15 | GPU OOM                | resource contention          | service failure        | telemetry               | admission/resource control        | resource envelopes           |
| FM-16 | artifact corruption    | generation library/model     | unusable output        | structural validation   | deterministic artifact generation | artifact QA                  |
| FM-17 | verifier failure       | weak verifier                | false acceptance       | cross-verification      | layered verification              | verifier independence        |
| FM-18 | provenance loss        | context compression          | untraceable answer     | provenance check        | evidence IDs/source map           | provenance preservation      |
| FM-19 | partial completion     | workflow interruption        | incomplete task        | execution state         | durable state + recovery          | partial-state handling       |
| FM-20 | configuration drift    | updates                      | invalid qualification  | environment fingerprint | version registry                  | requalification              |

The Phase-0 prompt specifically requires failure analysis across model, routing, planning, tools, retrieval, OCR, multimodality, parsing, code, sandbox, verification, artifacts, hardware, networking, security and silent/partial failure. 

---

# 10. Security & Sovereignty Requirements

## Established requirements

### SR-01

The Workbench shall operate without requiring external AI APIs for core functionality.

### SR-02

Confidential data shall remain within the defined deployment boundary.

### SR-03

External network communication shall be denied by default in sovereign deployments.

### SR-04

Network isolation shall be enforced outside application logic.

### SR-05

The system shall provide evidence of network behavior rather than merely asserting network isolation.

### SR-06

Agent authorization shall be enforced outside model reasoning.

### SR-07

Tools shall have explicit capability, permission and side-effect definitions.

### SR-08

Untrusted enterprise content shall not be able to modify control-plane authorization.

### SR-09

Generated code shall execute in an isolated environment.

### SR-10

Generated code shall not receive unrestricted host filesystem, credential or enterprise-network access.

### SR-11

Security-relevant actions shall be auditable.

### SR-12

Important claims and generated artifacts shall retain provenance.

### SR-13

Models and software dependencies shall have identifiable versions and integrity information.

### SR-14

Security-sensitive releases shall be independently qualified before deployment.

### SR-15

OT/ICS access shall be explicitly bounded.

### SR-16

High-consequence actions shall require appropriate human approval.

These requirements follow directly from the accumulated R5/R8 evidence rather than from technology preference. R8 explicitly establishes external policy enforcement, control/data-plane separation and independent network enforcement. 

---

# 11. Data & Knowledge Requirements

The research establishes that the data layer needs to support at least six classes:

1. **Source artifacts**
2. **Document structure**
3. **Enterprise metadata**
4. **Structured domain data**
5. **Derived knowledge**
6. **Execution/evaluation data**

R7 explicitly distinguishes source artifacts from derived knowledge and requires the source artifact to remain the evidentiary root. 

## Required data capabilities

### DR-01 — Document ingestion

Support at minimum:

* PDF
* DOCX
* XLSX
* PPTX
* scanned documents
* images
* engineering drawings
* P&IDs
* code
* email-like textual content where required.

### DR-02 — Structural preservation

Preserve:

* headings;
* sections;
* tables;
* figures;
* page references;
* coordinates;
* reading order;
* relationships.

### DR-03 — Metadata

Support:

* owner;
* authority;
* classification;
* ACL;
* revision;
* effective date;
* source system.

### DR-04 — Temporal knowledge

Support:

* revision identity;
* effective time;
* supersession;
* validity;
* historical knowledge.

### DR-05 — Provenance

Every important derived claim must be traceable to source evidence.

### DR-06 — Multimodal retrieval

Retrieval must be able to use more than textual similarity when the task requires it.

### DR-07 — Evidence states

The system must distinguish:

```text
RAW
PARSED
CANDIDATE
VALIDATED
APPROVED
SUPERSEDED
CONFLICTED
UNVERIFIABLE
REJECTED
```

### DR-08 — Evidence sufficiency

The system must be able to determine that retrieved evidence is insufficient.

### DR-09 — Structure-aware retrieval units

The retrieval unit must depend on document type rather than one global chunk size.

### DR-10 — Customer-local evaluation

Production qualification must support customer-owned corpus evaluation.

---

# 12. Competitive Requirements

## 12.1 Must Match

The market establishes that users will reasonably expect:

* conversational interaction;
* enterprise search;
* document understanding;
* citations/evidence;
* multi-step task execution;
* file handling;
* artifact generation;
* permission-aware access;
* model/tool extensibility;
* observability;
* useful UX.

The market research framework itself emphasizes identifying current solutions, missing capabilities, manual-review boundaries, integrations and user expectations. 

---

## 12.2 Must Exceed

The Workbench should differentiate through:

1. **Sovereignty**
2. **Evidence-governed reasoning**
3. **Multimodal engineering knowledge**
4. **Controlled agent execution**
5. **Verification-aware workflows**
6. **Proof/provenance**
7. **Hardware-aware model routing**
8. **Offline enterprise operation**
9. **Security evidence**
10. **Customer-local knowledge adaptation**

These are stronger differentiators than simply offering “local LLM chat.”

---

## 12.3 Cannot Match Directly

The Workbench should not attempt to compete head-on with hyperscale cloud platforms in:

* unlimited compute;
* global cloud infrastructure;
* giant foundation-model training;
* consumer-scale distribution;
* massive generic SaaS ecosystems.

Those conflict with the project's sovereignty and MVP constraints.

---

# 13. Contradiction Register

## CR-01 — Large model quality vs mid-range GPU

### Conflict

Large models improve capability but increase:

* VRAM;
* latency;
* concurrency constraints;
* operational complexity.

### Stronger position

**Multi-model/adaptive approach currently stronger.**

### Decision

Product requirement can be defined:

> System must deliver required workloads within constrained hardware.

Exact model portfolio remains **Requires Validation**.

---

## CR-02 — Maximum autonomy vs security

### Conflict

Users want automation.

Security requires limited authority.

### Stronger position

**Risk-tiered autonomy.**

### Decision

The product can support autonomous reasoning while consequential actions remain governed.

---

## CR-03 — Dynamic workflows vs reproducibility

### Conflict

Dynamic planning can improve adaptability.

Dynamic execution can make behavior harder to reproduce/debug.

### Stronger position

**Constrained dynamic workflow grammar**, not unrestricted autonomous workflow generation.

### Decision

Strong Candidate; implementation remains open.

---

## CR-04 — Comprehensive enterprise ontology vs MVP simplicity

### Conflict

A richer ontology may improve reasoning.

A universal ontology creates substantial implementation and maintenance cost.

### Stronger position

**Minimum domain structures + standards-aligned extensions.**

### Decision

No complete enterprise digital twin in MVP.

---

## CR-05 — Privacy deletion vs immutable audit

### Conflict

Security/audit systems benefit from durable records.

Privacy regimes can require controlled deletion/minimization.

### Current position

**Unresolved.**

### Decision

Requirements can state that auditability and privacy must both be supported, but exact retention/deletion semantics require customer/legal validation.

---

## CR-06 — Fully offline operation vs update/security maintenance

### Conflict

Air-gap reduces exposure.

Security requires vulnerability updates.

### Current position

**Controlled offline update mechanism.**

### Decision

Offline operation must not imply static software forever.

---

## CR-07 — Generic product vs sector-specific compliance

### Conflict

One platform is commercially desirable.

Different sectors have different security requirements.

### Stronger position

**Common product core + deployment/security profiles.**

### Decision

Product requirement can define profile support without prematurely implementing every sector regulation.

---

# 14. Assumption Register

| Assumption                                      | Why it exists                 | Risk if wrong                  | Validation                      |
| ----------------------------------------------- | ----------------------------- | ------------------------------ | ------------------------------- |
| Users will trust a local AI workbench           | sovereignty/value proposition | adoption failure               | customer interviews/pilot       |
| Customers will provide evaluation data          | production qualification      | cannot validate                | pilot agreements                |
| Mid-range GPU can support useful workloads      | MVP constraint                | architecture infeasible        | hardware benchmark              |
| Small multimodal models are adequate            | resource strategy             | poor quality                   | engineering corpus test         |
| Hybrid retrieval is sufficient when governed    | R5/R7 evidence                | retrieval failures             | retrieval benchmark             |
| Customers permit required security telemetry    | sovereignty proof             | cannot demonstrate claim       | deployment/security review      |
| Programmatic artifacts meet enterprise quality  | artifact strategy             | unusable outputs               | document acceptance tests       |
| Users accept human approval for high-risk tasks | safety model                  | workflow friction              | workflow study                  |
| Customers accept offline update bundles         | operational model             | maintenance problem            | security/procurement validation |
| gVisor is sufficient for MVP                    | sandbox candidate             | security/performance failure   | adversarial benchmark           |
| Customer terminology can be adapted locally     | data strategy                 | poor grounding                 | pilot ingestion                 |
| Agent workflows can be made reliable enough     | core product hypothesis       | product becomes assistant only | end-to-end benchmark            |
| Provenance improves trust/usefulness            | product differentiation       | low perceived value            | UX pilot                        |
| Security evidence will influence procurement    | enterprise positioning        | differentiation weak           | customer interviews             |

### Highest-risk assumptions

1. **Mid-range GPU feasibility**
2. **Agent reliability**
3. **Customer acceptance**
4. **Customer data availability**
5. **Artifact quality**
6. **Security deployment acceptance**

These deserve priority because they can invalidate major product decisions.

---

# 15. Research → Requirement → Decision Matrix

This is the most important Phase-0 bridge.

| Finding                                                  | Project implication                  | Requirement candidate                                        | Type                    | Decision                           |
| -------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------ | ----------------------- | ---------------------------------- |
| Confidential enterprise data cannot safely use public AI | local execution required             | Core operation shall run without external AI APIs            | Business / Security     | **Established**                    |
| Engineering workloads are multimodal                     | text-only system insufficient        | Support visual/document/structured technical information     | Functional              | **Established**                    |
| Documents have revisions/authority                       | similarity insufficient              | Retrieval shall account for authority and revision           | Data / Functional       | **Established**                    |
| AI-derived knowledge can be wrong                        | extraction cannot equal truth        | Derived knowledge shall have validation state                | Data                    | **Established**                    |
| Retrieval can be insufficient                            | answerability must be tested         | System shall detect insufficient evidence                    | Functional              | **Preferred**                      |
| Prompt injection can originate internally                | air-gap insufficient                 | Untrusted content shall not control authorization            | Security                | **Established**                    |
| Agents can misuse tools                                  | unrestricted agency unsafe           | Tool access shall be policy-controlled                       | Security                | **Established**                    |
| Generated code is untrusted                              | execution risk                       | Code shall execute in isolated environment                   | Security                | **Established**                    |
| Outputs can be plausible but wrong                       | generation ≠ correctness             | Important outputs shall undergo verification                 | Functional/NFR          | **Established**                    |
| Provenance is necessary                                  | users need traceability              | Important claims/artifacts shall retain evidence provenance  | Functional              | **Strong Candidate → requirement** |
| Customer data differs materially                         | generic corpus insufficient          | Customer-local qualification corpus shall be supported       | Data/Evaluation         | **Established**                    |
| Hardware state affects inference                         | static routing insufficient          | System shall operate within measured resource envelopes      | Performance             | **Established**                    |
| CII/OT has higher consequence                            | unrestricted OT agent unsafe         | OT interaction shall be bounded by deployment policy         | Security                | **Established**                    |
| Supply chain affects sovereignty                         | local runtime alone insufficient     | Software/model provenance shall be verifiable                | Security/Deployment     | **Established**                    |
| Market expects assistant UX                              | security alone is insufficient       | Conversational task-oriented interaction required            | User                    | **Established**                    |
| Competitive platforms provide governed execution         | simple chatbot not competitive       | Multi-step governed task execution required                  | Product                 | **Established**                    |
| Dynamic routing may improve efficiency                   | potentially important differentiator | System should support adaptive routing                       | Functional              | **Strong Candidate**               |
| Proof-carrying execution may improve assurance           | consequential actions need evidence  | Action execution should generate verifiable execution record | Security                | **Strong Candidate**               |
| Exact model stack uncertain                              | premature selection dangerous        | Model portfolio shall be replaceable                         | Architecture constraint | **Established principle**          |

The Phase-0 prompt explicitly requires this bridge and warns against converting every research finding into a requirement. 

---

# 16. Evidence Gap Register

## Critical

### EG-01 — Actual customer workflow validation

**Why:** R1 establishes plausible workflows, but product definition needs confirmation of priority and frequency for the first target customer.

**Affected decision:** MVP workflow priority.

**Validation:** customer interviews + workflow observation + representative corpus.

**Exit criterion:** 3–5 target workflows confirmed by representative users with measurable outcomes.

---

### EG-02 — Mid-range GPU end-to-end benchmark

**Why:** This is a hard MVP constraint.

**Affected decision:** model portfolio, concurrency, latency, architecture.

**Validation:** actual workstation/server benchmark using representative multimodal workloads.

**Exit criterion:** agreed latency/throughput/VRAM thresholds achieved for priority workflows.

---

### EG-03 — End-to-end agent reliability

**Why:** Individual component evidence does not establish complete workflow reliability.

**Affected decision:** degree of agent autonomy.

**Validation:** frozen workflow benchmark with repeated trials.

**Exit criterion:** predefined task-completion, verification and abstention thresholds.

---

### EG-04 — Security deployment acceptance

**Why:** Technical zero-egress mechanisms may not be accepted in every customer environment.

**Affected decision:** sovereignty evidence architecture.

**Validation:** security-team review with target organization.

**Exit criterion:** customer accepts evidence mechanism and deployment boundary.

---

# High

### EG-05 — Customer-local data availability

Exit criterion: representative corpus available under approved data handling.

### EG-06 — Artifact quality

Exit criterion: generated DOCX/PPTX/XLSX pass structural and human acceptance criteria.

### EG-07 — Prompt-injection resistance

Exit criterion: defined adversarial suite passes required containment thresholds.

### EG-08 — Sandbox security/performance

Exit criterion: escape tests pass while meeting usable execution latency.

### EG-09 — Exact compliance profile

Exit criterion: target customer profile mapped to applicable regulatory/contractual requirements.

### EG-10 — Model portfolio

Exit criterion: benchmark selects models against quality/resource/security criteria.

---

# Medium

* exact provenance implementation;
* dynamic workflow strategy;
* capability graph complexity;
* high-assurance physical isolation;
* exact retrieval engine;
* exact policy language.

---

# Low

* full enterprise ontology;
* complete digital twin;
* broad ecosystem integrations;
* advanced cryptographic proof of neural inference.

---

# 17. Product-Definition Readiness Assessment

| Category                   | Status              | Reason                                                                |
| -------------------------- | ------------------- | --------------------------------------------------------------------- |
| **Problem**                | **READY**           | clear confidential knowledge-work problem                             |
| **Users**                  | **READY**           | target organizations/user classes established                         |
| **Workflows**              | **PARTIALLY READY** | major workflows known; priority needs customer validation             |
| **Scope**                  | **READY**           | MVP and exclusions sufficiently defined                               |
| **Capabilities**           | **READY**           | core capabilities can be specified                                    |
| **Security**               | **READY**           | major security requirements established                               |
| **Data**                   | **READY**           | document, metadata, provenance and retrieval requirements established |
| **Agent Behavior**         | **READY**           | controlled, evidence-gated, risk-tiered behavior can be specified     |
| **Multimodality**          | **READY**           | engineering documents clearly require it                              |
| **Artifacts**              | **PARTIALLY READY** | artifact classes known; exact quality thresholds need validation      |
| **Verification**           | **READY**           | layered verification principle established                            |
| **Auditability**           | **READY**           | provenance/execution/security evidence requirements established       |
| **Hardware**               | **PARTIALLY READY** | constraint known; exact performance envelope unknown                  |
| **Competitive Position**   | **READY**           | must-match and differentiating capabilities identifiable              |
| **Exact Technology Stack** | **NOT READY**       | deliberately deferred                                                 |
| **Final Architecture**     | **NOT READY**       | correctly deferred to later phase                                     |

This is the correct state.

A requirements phase should **not** wait until every implementation technology is known.

The project documentation explicitly separates requirements from architecture and technology selection. 

---

# 18. What Phase 0 Has Now Established About the Product

We can now state the product definition at requirement level without prematurely designing the implementation.

## Product must:

### 1. Understand confidential enterprise tasks

The system must accept natural-language tasks involving enterprise documents, data and knowledge.

### 2. Determine what evidence is required

It must identify relevant sources and determine whether available evidence is sufficient.

### 3. Work across heterogeneous enterprise information

It must handle text, scanned documents, tables, images, engineering drawings and structured information.

### 4. Respect enterprise authority

It must distinguish current/authoritative information from stale, conflicting or superseded information.

### 5. Execute multi-step workflows

It must be able to perform more than question-answering.

### 6. Select appropriate capabilities

Different tasks and workflow steps may require different computational/model capabilities.

### 7. Use controlled tools

The agent must interact with tools through explicit authorization boundaries.

### 8. Verify important work

The system must check outputs rather than assuming generation equals correctness.

### 9. Generate useful enterprise artifacts

It must produce usable documents/spreadsheets/presentations/code where workflows require them.

### 10. Explain and trace important results

Important outputs must retain evidence/provenance.

### 11. Fail safely

When evidence, resources, authorization or verification are insufficient, the system must abstain, escalate, retry within bounds, request approval or stop.

### 12. Operate locally

The core product must remain usable in controlled/offline environments.

### 13. Demonstrate sovereignty

The product must provide evidence supporting its sovereignty/security posture.

### 14. Adapt to customer knowledge

The system must be qualified against customer-local data.

This is enough to start formal requirements engineering.

---

# 19. Phase-0 Final Gate

# **B — READY WITH TARGETED VALIDATION**

This is the strongest defensible decision.

### Why not A?

Because several high-impact variables are still unmeasured:

* actual target-customer workflow priorities;
* actual hardware performance;
* end-to-end agent reliability;
* exact artifact quality;
* customer acceptance of sovereignty evidence;
* deployment-specific regulatory controls.

Freezing these as facts would violate the project's own evidence rules.

### Why not C?

Because none of these gaps prevents us from defining the **behavior the product must provide**.

For example:

We do not yet know whether the final model is Qwen3-VL, another VLM, or a combination.

But we already know:

> **The product must process visual/technical documents and provide sufficiently reliable, traceable interpretations under the deployment's hardware and security constraints.**

That is a valid product requirement.

Technology comes later.

---

# 20. Required Targeted Validation Before Freezing Affected PRD Sections

## Validation V1 — Priority Workflow Validation

Select the initial **3–5 workflows** from the R1 research and validate with actual representative users.

Measure:

* frequency;
* time spent;
* current workflow;
* error cost;
* required approval;
* acceptable automation level;
* desired output;
* success criterion.

---

## Validation V2 — Representative Corpus

Build the first frozen evaluation corpus:

```text
documents
+
scans
+
P&IDs
+
spreadsheets
+
revisions
+
conflicts
+
cross-document cases
```

The exact numbers should be determined by workflow coverage, not arbitrary volume.

---

## Validation V3 — Hardware Envelope

Measure:

```text
VRAM
RAM
CPU
storage
TTFT
TPOT
throughput
concurrency
KV-cache pressure
VLM image resolution
model residency
failure/OOM behavior
```

This determines the actual MVP computational envelope.

---

## Validation V4 — End-to-End Agent Benchmark

Measure:

```text
task completion
step correctness
tool-call correctness
evidence sufficiency
verification success
abstention correctness
partial completion
recovery
latency
resource consumption
```

This is more important than benchmarking an isolated LLM.

---

## Validation V5 — Security Adversarial Suite

Test:

```text
prompt injection
malicious documents
tool poisoning
unauthorized retrieval
privilege escalation
malicious generated code
sandbox escape
network egress
DNS
IPv6
proxy paths
credential access
resource exhaustion
```

---

## Validation V6 — Artifact Acceptance

Define objective criteria for:

* DOCX;
* PPTX;
* XLSX;
* code;
* reports.

Measure both structural validity and human usefulness.

---

## Validation V7 — Customer Security Review

Take the proposed sovereignty evidence model to a representative security/IT stakeholder.

Determine:

* accepted isolation model;
* accepted telemetry;
* acceptable audit evidence;
* update mechanism;
* deployment boundary;
* approval process.

---

# 21. Inputs to Phase 1

Phase 1 should **not start from a blank page**.

It should receive this decision base.

## Input A — Problem Definition

> Confidential enterprise knowledge work requires AI assistance, but sensitive information cannot safely rely on public cloud AI services.

## Input B — Product Direction

> Sovereign Agentic AI Workbench for controlled local enterprise knowledge-work execution.

## Input C — Core User Outcome

> Enable users to perform complex confidential knowledge workflows faster while retaining organizational control, evidence, verification and auditability.

## Input D — Core Capability Set

```text
Task understanding
Evidence retrieval
Multimodal document understanding
Enterprise knowledge grounding
Agentic workflow execution
Controlled tool use
Code execution
Verification
Artifact generation
Provenance
Auditability
Sovereignty evidence
```

## Input E — Non-Negotiable Constraints

```text
Local operation
No external AI API dependency
Controlled data boundary
Controlled agent permissions
Sandboxed code
Multimodal capability
Observable execution
Enterprise hardware feasibility
```

## Input F — Major Product Risks

```text
wrong-but-plausible output
stale knowledge
unauthorized retrieval
prompt injection
tool misuse
sandbox compromise
resource exhaustion
false completion
artifact failure
insufficient evidence
sovereignty failure
customer deployment friction
```

## Input G — Technology Status

Technology choices remain appropriately separated into:

```text
Preferred
Strong Candidate
Candidate
Requires Validation
Rejected
```

rather than being prematurely frozen.

---

# 22. Phase-1 Starting Requirement Hierarchy

Phase 1 should now transform the decision base into:

```text
Business Requirements
        ↓
User Requirements
        ↓
Workflow Requirements
        ↓
Functional Requirements
        ↓
Non-Functional Requirements
        ↓
Security Requirements
        ↓
Data Requirements
        ↓
Evaluation Requirements
        ↓
Deployment Requirements
        ↓
Acceptance Criteria
```

This follows the software-planning material, which separates requirements engineering into elicitation, functional requirements, non-functional requirements, prioritization and formal SRS/acceptance criteria. 

The development workflow adds the important constraint that requirements must be **testable, measurable and traceable to business objectives**. 

---

# 23. Open Questions Carried Forward

These are not failures of Phase 0.

They are explicitly carried forward.

### Product

1. Which 3–5 workflows constitute MVP?
2. Who is the primary MVP user?
3. What is the first target organization profile?

### Performance

4. What latency is acceptable?
5. What concurrency is required?
6. What exact GPU constitutes the MVP reference system?

### AI

7. Which model portfolio meets the benchmark?
8. What minimum multimodal accuracy is acceptable?
9. What level of autonomous reasoning is acceptable?

### Knowledge

10. What exact enterprise metadata is available from target customers?
11. What authority hierarchy exists?
12. What customer-local adaptation is necessary?

### Security

13. What security profile is the first deployment?
14. What evidence qualifies as sufficient sovereignty proof?
15. What sandbox assurance level is required?

### Compliance

16. Which regulatory/sector controls apply to the first customer?
17. What retention/deletion policy is required?
18. What audit evidence must be exportable?

### Evaluation

19. What constitutes task success?
20. What constitutes unacceptable failure?
21. Which failures require mandatory human review?

### Architecture

22. Which model-serving technology?
23. Which agent runtime?
24. Which retrieval technology?
25. Which sandbox?
26. Which policy mechanism?
27. Which provenance implementation?

These should **not** be resolved by opinion.

They should be resolved by the appropriate Phase-1 requirements or targeted validation activities.

---

# 24. Phase-0 Closure Statement

The research phase has now crossed the important threshold:

```text
RESEARCH
   ↓
EVIDENCE
   ↓
ESTABLISHED FINDINGS
   ↓
PROJECT IMPLICATIONS
   ↓
REQUIREMENT CANDIDATES
   ↓
DECISIONS
   ↓
OPEN QUESTIONS
   ↓
TARGETED VALIDATION
```

The project documentation defines exactly this transition as the purpose of the research pipeline. 

The accumulated research is therefore **decision-ready enough to stop researching broadly**.

The next phase should not be another technology investigation.

It should be:

# **Phase 1 — Research-to-Requirement Synthesis**

with the specific job of turning this decision base into a **formal requirement hierarchy and traceability system**.

The most important discipline going forward is:

> **Do not write “the system should use X.” Write “the system must achieve Y under constraint Z,” and only then determine whether X is the appropriate implementation.**

That preserves the distinction between **product requirements, architecture decisions, technology choices and validation evidence**, which is the main thing Phase 0 was supposed to protect. 

**Phase 0 status: CLOSED — READY WITH TARGETED VALIDATION.**

**Next Action:** Phase 1 — **Research-to-Requirement Synthesis**.
