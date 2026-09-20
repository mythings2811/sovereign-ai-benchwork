# SOVEREIGN AGENTIC AI WORKBENCH

# PHASE 17 — PROTOTYPE / TECHNICAL SPIKES

**Document Status:** EXECUTION BASELINE — EMPIRICAL VALIDATION PENDING  
**Predecessors:** Phase 9 SRS → Phase 10 System Architecture → Phase 11 Technology Baseline → Phase 12 Component Architecture → Phase 13 Data & Knowledge Architecture → Phase 14 Agent Runtime & Tool Architecture → Phase 15 Security & Sovereignty Architecture → Phase 16 Reference Deployment Architecture  
**Successor:** Phase 18 — MVP Implementation  
**Primary Validation Target:** W3 → W1 → W2 → W4, with W5 conditional

---

# 1. Executive Decision

## Current Phase 17 status

**PHASE 17 VALIDATION PROGRAM ESTABLISHED — EXECUTION REQUIRED**

No empirical evidence has yet been admitted as Phase 17 validation evidence in this document.

Therefore:

> **MVP implementation must not yet be declared empirically validated.**

The purpose of Phase 17 is to determine whether the architecture established in Phases 9–16 survives contact with:

- representative enterprise data;
- local AI execution;
- real retrieval;
- multimodal processing;
- P&ID structural interpretation;
- bounded agent execution;
- verification;
- sandbox isolation;
- zero-egress enforcement;
- constrained hardware;
- artifact generation;
- component interaction;
- adversarial failure.

The Phase 17 principle is:

> **Representative Data → Real Architecture Boundary → Real Execution → Measurement → Failure Injection → Verification → Evidence → Architectural Decision**

rather than prototype → demo → approval.

---

# 2. Primary Objective

The primary question is:

> **Can the proposed Sovereign Agentic AI Workbench perform confidential enterprise knowledge workflows locally, reliably and securely, within the reference deployment envelope, while preserving evidence, authorization, verification, provenance and sovereignty?**

Phase 17 must answer this empirically.

It must not answer the weaker question:

> “Can the individual technologies produce an impressive demonstration?”

---

# 3. Phase Boundary

## Phase 17 MUST

1. identify high-risk assumptions;
2. rank them by consequence;
3. formulate falsifiable hypotheses;
4. construct representative datasets;
5. construct ground truth where feasible;
6. build minimum viable prototypes;
7. execute reproducible experiments;
8. measure quality and resource consumption;
9. inject failures;
10. perform security testing;
11. perform sovereignty testing;
12. test architectural seams;
13. record failed approaches;
14. determine architecture-changing evidence;
15. update confidence;
16. establish implementation constraints for Phase 18.

These requirements follow the Phase 17 master brief.

## Phase 17 MUST NOT

- build the complete MVP;
- build production UI;
- create full enterprise administration;
- optimize every component;
- benchmark components without workflow relevance;
- use one successful demonstration as validation;
- hide failed experiments;
- rely exclusively on synthetic data for critical claims;
- replace empirical testing with theoretical reasoning.

---

# 4. Architectural Baseline Under Test

Phase 17 does not redesign the approved architecture.

The baseline under test is:

```text
USER
  ↓
IDENTITY
  ↓
SECURITY CONTEXT
  ↓
POLICY
  ↓
TASK
  ↓
AGENT / WORKFLOW
  ↓
EVIDENCE
  ↓
LOCAL AI CAPABILITY
  ↓
CONTROLLED TOOL
  ↓
ISOLATED EXECUTION
  ↓
VERIFICATION
  ↓
RESULT / ARTIFACT
  ↓
PROVENANCE
  ↓
AUDIT
```

The agent remains subordinate to external authorization and policy.

Phase 12 explicitly establishes that model output, agent plans, retrieved documents, tool requests, code execution and artifact existence are not themselves authority.

---

# 5. Highest-Risk Architectural Assumptions

| ID | Assumption | Consequence if false | Initial confidence | Validation |
|---|---|---|---|---|
| A-01 | Local models can perform required knowledge work | MVP value collapses | Medium | SP-01 |
| A-02 | Qwen3.5-class local models fit reference hardware | Model baseline changes | Medium | SP-01/SP-09 |
| A-03 | Multimodal pipeline preserves useful document structure | W1/W2 degrade | Medium | SP-02 |
| A-04 | P&ID processing can produce sufficiently reliable structure | W2 architecture changes | Low/Medium | SP-03 |
| A-05 | Retrieval can enforce authority/revision/authorization | Confidentiality/correctness failure | Medium | SP-04 |
| A-06 | Bounded agent execution is reliable | Core execution model fails | Medium | SP-05 |
| A-07 | Verification catches important errors | False confidence reaches users | Medium | SP-06 |
| A-08 | Sandbox prevents unauthorized code effects | Security boundary invalid | Medium | SP-07 |
| A-09 | Zero-egress is enforceable and observable | Sovereignty claim invalid | Medium | SP-08 |
| A-10 | Reference hardware supports complete workflows | Deployment baseline changes | Low/Medium | SP-09 |
| A-11 | Artifact pipeline produces usable outputs | W4 fails | Medium | SP-10 |
| A-12 | Architectural seams work together | Isolated benchmarks become irrelevant | Low/Medium | INT-01–05 |

---

# 6. Spike Portfolio

The mandatory portfolio is:

1. **SP-01 — Local Model Quality**
2. **SP-02 — Multimodal Document Processing**
3. **SP-03 — P&ID Structural Interpretation**
4. **SP-04 — Evidence-Aware Retrieval**
5. **SP-05 — Agent Reliability**
6. **SP-06 — Verification Effectiveness**
7. **SP-07 — Sandbox Security**
8. **SP-08 — Zero-Egress Operation**
9. **SP-09 — End-to-End Hardware Feasibility**
10. **SP-10 — Artifact Generation**

This exact portfolio is required by the Phase 17 specification.

---

# 7. Shared Validation Environment

A single common validation environment shall be used wherever practical.

## Required controls

```text
Hardware
   +
OS
   +
Software Versions
   +
Model Versions
   +
Configuration
   +
Dataset Version
   +
Experiment ID
   +
Telemetry
   +
Execution Trace
   +
Provenance
   +
Results
```

The environment shall record:

- hardware identity;
- GPU identity;
- driver/runtime versions;
- OS version;
- application revision;
- model identifiers;
- model hashes where applicable;
- inference configuration;
- prompt/configuration version;
- dataset fingerprint;
- experiment ID;
- execution ID;
- workflow ID;
- telemetry;
- logs;
- provenance;
- failure records.

This is required for reproducibility.

---

# 8. Dataset Architecture

The validation corpus shall represent actual intended workloads.

## Required corpus classes

### Documents

- native PDFs;
- scanned PDFs;
- DOCX;
- spreadsheets;
- CSV;
- technical reports;
- inspection reports;
- manuals;
- SOPs;
- approval notes;
- correspondence;
- photographs;
- engineering drawings;
- P&IDs.

### Governance variants

- current revision;
- historical revision;
- superseded revision;
- conflicting revision;
- different authority levels;
- authorized documents;
- unauthorized documents;
- incomplete documents.

### Adversarial variants

- prompt injection;
- malicious document structures;
- malformed files;
- misleading evidence;
- conflicting evidence;
- stale evidence;
- unauthorized information;
- adversarial code.

The Phase 17 specification explicitly requires both benign and adversarial data.

---

# 9. Ground-Truth Strategy

Ground truth shall be constructed wherever objectively possible.

## Ground truth may contain

- expected facts;
- source documents;
- exact evidence regions;
- expected entities;
- expected relationships;
- expected P&ID topology;
- expected calculations;
- expected claims;
- expected artifact structure;
- expected refusal;
- expected abstention;
- expected security response.

Ground truth status shall be recorded as:

```text
GROUND_TRUTH_AVAILABLE
GROUND_TRUTH_PARTIAL
GROUND_TRUTH_UNAVAILABLE
```

Subjective engineering judgment shall not be falsely converted into objective ground truth.

---

# 10. Experiment Registry

Every experiment receives a unique identifier.

| Experiment | Assumption | Hypothesis | Workflow | Dataset | Metric | Success criterion | Result | Decision |
|---|---|---|---|---|---|---|---|---|
| EXP-01 | Local model | Local model can execute required reasoning | W3 | Validation corpus | Quality/reliability/resource | TBD by qualification | PENDING | PENDING |
| EXP-02 | Multimodal | Pipeline preserves usable structure | W1 | Mixed documents | Extraction/interpretation | TBD | PENDING | PENDING |
| EXP-03 | P&ID | Structural representation is usable | W2 | P&ID corpus | Entity/relation/topology | TBD | PENDING | PENDING |
| EXP-04 | Retrieval | Correct evidence is selected | W3 | Revision corpus | Auth/revision/recall | TBD | PENDING | PENDING |
| EXP-05 | Agent | Bounded execution completes reliably | W3/W1/W4 | Workflow corpus | Verified completion | TBD | PENDING | PENDING |
| EXP-06 | Verification | Important errors are detected | W1/W2/W4 | Seeded-error corpus | Unsafe acceptance | TBD | PENDING | PENDING |
| EXP-07 | Sandbox | Untrusted code remains contained | W5 | Adversarial code | Escape/data exposure | Zero unauthorized access | PENDING | PENDING |
| EXP-08 | Sovereignty | Prohibited egress is prevented | All | Adversarial network tests | Egress | Zero prohibited egress | PENDING | PENDING |
| EXP-09 | Hardware | Complete workflows fit deployment | All | Representative corpus | E2E/resource | Qualification envelope | PENDING | PENDING |
| EXP-10 | Artifacts | Outputs are structurally/usefully valid | W4 | Artifact corpus | Structural/content/evidence | TBD | PENDING | PENDING |

---

# 11. SP-01 — Local Model Quality

## Question

Can the proposed local model capability support the required enterprise workload?

## Evaluate

### Reasoning

- technical QA;
- multi-document reasoning;
- evidence synthesis;
- contradiction handling;
- uncertainty handling;
- structured extraction.

### Tool use

- structured requests;
- parameter validity;
- bounded action selection;
- recovery after tool failure.

### Long context

- large documents;
- multiple documents;
- evidence-heavy context;
- conflicting revisions.

### Infrastructure

- model load time;
- VRAM;
- RAM;
- latency;
- stability;
- resource contention.

The official Phase 17 specification requires task quality to be evaluated together with evidence grounding, reliability, hardware feasibility and security—not benchmark scores alone.

## Candidates

Initial validation set:

- Qwen3.5-4B;
- Qwen3.5-9B;
- fallback model candidates from Phase 11.

The Phase 11 baseline currently identifies Qwen3.5-9B as preferred but explicitly validation-bound.

## Failure conditions

- unsupported claims;
- failure to obey structured contracts;
- inadequate reasoning;
- unacceptable latency;
- excessive resource consumption;
- instability;
- inability to operate within reference deployment.

---

# 12. SP-02 — Multimodal Document Processing

## Pipeline

```text
DOCUMENT
 ↓
PAGE
 ↓
REGION
 ↓
OCR / TEXT
 ↓
LAYOUT
 ↓
VISUAL INFORMATION
 ↓
STRUCTURED REPRESENTATION
 ↓
EVIDENCE
```

## Test

- native PDF;
- scanned PDF;
- mixed layout;
- tables;
- diagrams;
- poor scans;
- rotated pages;
- difficult text;
- images.

## Metrics

Keep separate:

1. extraction correctness;
2. OCR quality;
3. table extraction;
4. region localization;
5. layout preservation;
6. visual interpretation;
7. evidence localization;
8. processing latency;
9. failure rate.

Do not collapse extraction, interpretation and consequential correctness into one score.

---

# 13. SP-03 — P&ID Structural Interpretation

This is a **critical architectural spike**.

## Target

```text
P&ID IMAGE
 ↓
VISUAL OBSERVATION
 ↓
OCR / LAYOUT
 ↓
ENTITY EXTRACTION
 ↓
RELATION EXTRACTION
 ↓
STRUCTURAL GRAPH
 ↓
EVIDENCE
 ↓
ENGINEERING INTERPRETATION
```

## Measure

- equipment precision/recall/F1;
- instrument precision/recall/F1;
- valve precision/recall/F1;
- line recognition;
- tag accuracy;
- relation precision/recall/F1;
- topology correctness;
- spatial localization;
- revision correctness;
- provenance coverage.

The Phase 17 brief explicitly rejects evaluating P&ID capability merely by whether a model can describe an image.

## Decision

Determine empirically whether the architecture should:

- rely more heavily on multimodal reasoning;
- use an explicit intermediate representation;
- combine both;
- abstain when structural confidence is insufficient.

No architecture change shall be made before evidence.

---

# 14. SP-04 — Evidence-Aware Retrieval

## Critical question

Can the system select the **correct evidence**, rather than merely semantically similar text?

## Test matrix

| Condition | Expected behavior |
|---|---|
| Correct current document | Retrieve |
| Older revision | Reject/deprioritize when inapplicable |
| Higher-authority conflict | Preserve/identify authority distinction |
| Unauthorized document | Never expose |
| Similar but irrelevant document | Avoid |
| Multiple-source answer | Preserve lineage |
| Insufficient evidence | Abstain/escalate |
| Conflicting evidence | Represent conflict |
| Stale evidence | Mark/reject according to policy |

## Metrics

- retrieval recall;
- retrieval precision;
- authority correctness;
- revision correctness;
- temporal correctness;
- authorization correctness;
- evidence sufficiency;
- grounding precision;
- unsupported claim rate;
- attribution coverage.

The decisive experiment is whether authoritative evidence can beat highly similar but obsolete/lower-authority material.

---

# 15. SP-05 — Agent Reliability

## Execution loop

```text
OBSERVE
 ↓
PLAN
 ↓
POLICY
 ↓
ACTION
 ↓
TOOL
 ↓
RESULT
 ↓
VERIFY
 ↓
CONTINUE / CORRECT / ESCALATE / STOP
```

## Failure injection

- wrong tool;
- invalid parameters;
- missing evidence;
- conflicting evidence;
- tool failure;
- model failure;
- verification failure;
- repeated failure;
- policy denial;
- stale state;
- timeout;
- resource exhaustion.

## Primary metric

> **Verified Workflow Completion Rate**

Supporting metrics:

- workflow success;
- step success;
- tool-call correctness;
- unnecessary calls;
- retry count;
- loop frequency;
- escalation correctness;
- abstention correctness;
- completion-predicate correctness;
- recovery success.

The architecture must be evaluated on the complete execution trajectory rather than whether the final response merely looks good.

---

# 16. SP-06 — Verification Effectiveness

## Method

Seed known errors into:

- extracted facts;
- calculations;
- retrieved evidence;
- claims;
- reports;
- generated code;
- structured data.

## Metrics

- true errors detected;
- false positives;
- false negatives;
- consequential errors missed;
- verification coverage;
- verifier agreement;
- verifier independence;
- escalation correctness;
- correction success;
- unsafe acceptance rate.

## Architectural question

Determine which verification mechanisms are necessary:

```text
Deterministic
Evidence-based
Numerical
Semantic
Policy-based
Human-assisted
```

Self-checking by the same model shall not automatically qualify as independent verification.

---

# 17. SP-07 — Sandbox Security

## Adversarial tests

Attempt:

- filesystem escape;
- parent-process access;
- privilege escalation;
- credential access;
- network access;
- environment inspection;
- process spawning;
- resource exhaustion;
- persistence;
- malicious dependency installation;
- device access;
- IPC abuse.

## Acceptance principle

> **Generated code must not obtain capabilities outside its explicit execution contract.**

Measure:

- prevented;
- detected;
- contained;
- host impact;
- data exposure;
- audit visibility;
- resource isolation.

This directly tests the security boundary rather than merely demonstrating that code can execute.

---

# 18. SP-08 — Zero-Egress Operation

This experiment is mandatory.

## Test every outbound path

- application;
- agent;
- model runtime;
- OCR;
- document processor;
- tools;
- sandbox;
- subprocesses;
- package managers;
- update mechanisms;
- telemetry;
- crash handling.

## Protocols

Attempt:

- HTTP;
- HTTPS;
- DNS;
- arbitrary TCP;
- package download;
- model download;
- telemetry;
- external API access.

## Record

For every attempted connection:

```text
Source Process
Destination
Protocol
Timestamp
Result
Blocking Layer
Log Record
Alert
```

## Acceptance

> **Prohibited communication = prevented + observable + attributable**

Application configuration alone is insufficient evidence.

---

# 19. SP-09 — End-to-End Hardware Feasibility

This is the principal infrastructure experiment.

## Reference deployment under test

Current Phase 16 target:

```text
Single Linux Host
        │
        ├── CPU: 16–32-core/thread class
        ├── RAM: 128 GB ECC preferred
        ├── GPU: 48 GB VRAM-class
        ├── OS Storage: ~1 TB NVMe class
        ├── Application/Data: ~4 TB NVMe class
        └── Separate Offline Backup
```

These are **qualification targets**, not yet empirically validated procurement specifications.

## Benchmark

Do not use tokens/sec as the principal KPI.

Measure:

```text
Task Intake
 + Retrieval
 + Evidence
 + Reasoning
 + OCR
 + Vision
 + P&ID Processing
 + Tool Execution
 + Verification
 + Artifact Generation
 + Provenance
 + Audit
```

## Workflows

### W3

Organizational Knowledge Investigation

### W1

Inspection / Technical Report Analysis

### W2

P&ID / Engineering Drawing Analysis

### W4

Technical Report / Approval Artifact Generation

### W5

Controlled Code-Assisted Analysis, conditional

## Conditions

- cold start;
- warm start;
- sustained;
- peak;
- concurrent;
- resource pressure;
- failure/recovery.

## Measure

- end-to-end latency;
- verified completion latency;
- CPU;
- RAM;
- GPU utilization;
- VRAM;
- storage;
- I/O;
- model loading;
- retrieval;
- OCR;
- multimodal processing;
- agent execution;
- tool execution;
- sandbox;
- verification;
- artifact generation;
- concurrency;
- failure;
- recovery.

The Phase 17 brief explicitly requires complete workflow measurement rather than isolated inference/OCR/retrieval benchmarks.

---

# 20. SP-10 — Artifact Generation

Evaluate:

- technical reports;
- findings summaries;
- approval-note drafts;
- structured documents;
- tables;
- spreadsheets where applicable;
- evidence references;
- provenance.

## Quality dimensions

```text
Structural Correctness
        +
Content Correctness
        +
Evidence Correctness
        +
Provenance
        +
Human Usability
```

Critical state distinction:

```text
GENERATED
   ≠
VERIFIED
   ≠
APPROVED
```

The Phase 17 brief explicitly requires this separation.

---

# 21. Cross-Spike Integration

Individual component success is insufficient.

The following integrated experiments are mandatory.

## INT-01 — W3 Investigation

```text
User Task
 ↓
Retrieval
 ↓
Evidence
 ↓
Local Model
 ↓
Agent
 ↓
Verification
 ↓
Result
 ↓
Provenance
```

## INT-02 — W1 Technical Analysis

```text
Document
 ↓
OCR / Processing
 ↓
Evidence
 ↓
Multimodal Analysis
 ↓
Agent
 ↓
Verification
 ↓
Result
```

## INT-03 — W2 P&ID

```text
P&ID
 ↓
Visual Processing
 ↓
OCR
 ↓
Structural Representation
 ↓
Evidence
 ↓
Reasoning
 ↓
Verification
 ↓
Result
```

## INT-04 — W4 Artifact

```text
Evidence
 ↓
Reasoning
 ↓
Draft
 ↓
Verification
 ↓
Provenance
 ↓
Artifact
```

## INT-05 — W5 Code Analysis

```text
Task
 ↓
Evidence
 ↓
Code Generation
 ↓
Policy
 ↓
Sandbox
 ↓
Execution
 ↓
Numerical Verification
 ↓
Artifact
```

These integrated paths are explicitly required by the Phase 17 master specification.

---

# 22. Integrated Security Experiment

Run a normal workflow while simultaneously injecting:

- malicious document;
- prompt injection;
- unauthorized retrieval request;
- unauthorized tool request;
- prohibited network attempt;
- malicious generated code;
- resource exhaustion.

The critical question is:

> Does the security architecture continue to enforce authority and isolation without silently corrupting workflow integrity?

---

# 23. Failure Propagation Testing

Test the complete chain against bad subsystem outputs.

| Failure | Required observation |
|---|---|
| Bad OCR | Downstream uncertainty is visible |
| Wrong retrieval | Unsupported claim is detected |
| Wrong P&ID extraction | Structural uncertainty is surfaced |
| Tool failure | Retry is controlled |
| Verification failure | Workflow stops/escalates |
| Sandbox failure | Task recovers safely |
| Model failure | Routing/fallback operates correctly |
| Policy failure | Execution fails closed |

The Phase 17 specification specifically requires these cross-spike failure-propagation tests.

---

# 24. False-Confidence Testing

Explicitly test whether the system produces an answer that looks highly confident while being wrong.

Inject:

- unsupported claims;
- incorrect citations;
- wrong revision;
- wrong P&ID relationship;
- incorrect calculation;
- incorrect artifact;
- incorrect interpretation of tool output.

Evaluate:

> **Confidence vs correctness**

not confidence by itself.

---

# 25. Abstention Validation

Construct cases where the correct behavior is:

- insufficient evidence;
- conflicting evidence;
- unauthorized evidence;
- stale evidence;
- uncertain interpretation;
- unsafe code;
- failed verification;
- unavailable capability.

Classify:

```text
Incorrect Answer
Over-Abstention
Correct Abstention
Correct Escalation
```

Safe abstention is a positive result, not a failure.

---

# 26. Risk-Based Spike Priority

| Spike | Risk | Architectural Impact | Uncertainty | Cost of Failure | Priority | Status |
|---|---|---|---|---|---|---|
| SP-09 Hardware | Critical | Critical | High | Critical | P0 | Pending |
| SP-08 Zero-egress | Critical | Critical | Medium/High | Critical | P0 | Pending |
| SP-07 Sandbox | Critical | Critical | Medium | Critical | P0 | Pending |
| SP-04 Retrieval | Critical | Critical | Medium | Critical | P0 | Pending |
| SP-03 P&ID | Critical | High | High | High | P0 | Pending |
| SP-05 Agent | High | Critical | Medium/High | High | P1 | Pending |
| SP-06 Verification | High | Critical | Medium | Critical | P1 | Pending |
| SP-01 Models | High | High | Medium | High | P1 | Pending |
| SP-02 Multimodal | High | High | Medium | High | P1 | Pending |
| SP-10 Artifacts | Medium/High | High | Medium | High | P1 | Pending |

Priority uses qualitative categories rather than invented numerical risk scores, consistent with the Phase 17 requirement.

---

# 27. Execution Order

The recommended execution order is:

```text
PHASE 17 ENVIRONMENT
        ↓
DATASET + GROUND TRUTH
        ↓
SP-09 HARDWARE BASELINE
        ↓
SP-01 LOCAL MODELS
        ↓
SP-02 DOCUMENT PROCESSING
        ↓
SP-04 RETRIEVAL
        ↓
SP-03 P&ID
        ↓
SP-05 AGENT
        ↓
SP-06 VERIFICATION
        ↓
SP-07 SANDBOX
        ↓
SP-08 ZERO-EGRESS
        ↓
SP-10 ARTIFACTS
        ↓
W3 THIN VERTICAL SLICE
        ↓
W1
        ↓
W2
        ↓
W4
        ↓
W5 IF JUSTIFIED
        ↓
ADVERSARIAL INTEGRATION
        ↓
ARCHITECTURE DECISIONS
        ↓
PHASE 18
```

Hardware should be established early because an invalid resource envelope can invalidate otherwise successful component experiments.

---

# 28. Thin Vertical Slice

The final Phase 17 prototype shall not consist of independent demos.

It shall demonstrate:

```text
User Task
 ↓
Identity
 ↓
Policy
 ↓
Agent
 ↓
Retrieval / Evidence
 ↓
Local Model
 ↓
Tool
 ↓
Verification
 ↓
Artifact
 ↓
Provenance / Audit
```

W3 is the preferred first integration path because it exercises the greatest number of architectural seams with comparatively manageable multimodal complexity. The Phase 17 specification explicitly calls for this architecture-level vertical slice.

---

# 29. Prototype Security Requirements

Every prototype must retain:

- data isolation;
- authorization;
- policy boundaries;
- tool boundaries;
- sandboxing;
- network controls;
- provenance;
- audit;
- version tracking.

A prototype shortcut that bypasses the security mechanism under test invalidates the corresponding security result.

If unavoidable:

> **SECURITY VALIDATION INCOMPLETE**

This is an explicit Phase 17 requirement.

---

# 30. Reproducibility Package

Each major experiment shall preserve:

- source code;
- configuration;
- model identifiers;
- model hashes where applicable;
- dependencies;
- hardware;
- dataset ID;
- experiment configuration;
- results;
- logs;
- provenance;
- useful artifacts/screenshots;
- failure records.

The experiment must be rerunnable.

---

# 31. Experiment Decision States

Each assumption shall conclude as exactly one of:

### VALIDATED

Evidence supports the architecture under defined conditions.

### VALIDATED WITH CONDITIONS

Architecture works only within explicit constraints.

### PARTIALLY VALIDATED

Important capability works but material uncertainty remains.

### INVALIDATED

Evidence contradicts the assumption.

### REQUIRES FURTHER VALIDATION

Experiment was inconclusive.

### REJECTED

The approach should not proceed.

These states are mandated by the Phase 17 decision framework.

---

# 32. Stop Conditions

Stop pursuing an approach when evidence demonstrates:

- repeated failure against critical requirements;
- unacceptable security risk;
- hardware infeasibility;
- unacceptable workflow reliability;
- insufficient evidence quality;
- unsustainable complexity;
- sovereignty violation;
- licensing incompatibility;
- operational infeasibility.

Do not continue optimizing an approach that is fundamentally unsuitable.

---

# 33. Reversal Conditions

The following evidence can reopen Phase 11–16 decisions:

| Decision | Reversal trigger |
|---|---|
| Model family | Quality/resource failure |
| Inference engine | Instability or unacceptable switching/resource behavior |
| Retrieval architecture | Authorization/evidence failure |
| P&ID architecture | Structural accuracy inadequate |
| Agent runtime | Unsafe/reliable completion inadequate |
| Verification architecture | Consequential errors escape |
| Sandbox | Isolation failure |
| Zero-egress design | Prohibited egress cannot be prevented/attributed |
| Reference hardware | Complete workflow cannot fit supported envelope |
| Artifact architecture | Verification/provenance insufficient |

Architecture decisions remain evidence-reversible rather than protected by project momentum.

---

# 34. Architecture Change Matrix

| Finding | Requirement | Component | Architecture impact | Technology impact | Deployment impact | Security impact | Decision |
|---|---|---|---|---|---|---|---|
| PENDING | — | — | — | — | — | — | PENDING |

This matrix becomes the formal bridge from experiments back to architecture.

---

# 35. Risk Retirement Matrix

| Risk | Initial confidence | Spike | Evidence | Remaining risk | New confidence | Retired |
|---|---|---|---|---|---|---|
| 48 GB hardware sufficiency | Medium/Low | SP-09 | Pending | Unknown | Pending | No |
| P&ID topology | Low/Medium | SP-03 | Pending | Unknown | Pending | No |
| Agent reliability | Medium | SP-05 | Pending | Unknown | Pending | No |
| Retrieval authorization | Medium | SP-04 | Pending | Unknown | Pending | No |
| Sandbox isolation | Medium | SP-07 | Pending | Unknown | Pending | No |
| Zero-egress | Medium | SP-08 | Pending | Unknown | Pending | No |
| Verification effectiveness | Medium | SP-06 | Pending | Unknown | Pending | No |

The purpose of Phase 17 is risk retirement. A spike that does not materially reduce risk has not succeeded.

---

# 36. Technology Rejection Discipline

A technology shall be rejected when empirical evidence demonstrates that it:

- violates sovereignty;
- violates a hard security constraint;
- cannot operate within the supported resource envelope;
- cannot satisfy the capability contract;
- creates unacceptable integration complexity;
- produces unacceptable workflow reliability;
- prevents required verification;
- creates unacceptable operational risk.

The Phase 11 baseline already establishes that technology decisions must be based on architecture requirements, evidence, security, hardware and workflow evaluation—not popularity.

---

# 37. Human Evaluation

Automated evaluation shall not be the only evaluation mechanism for high-consequence workflows.

Human evaluation should assess:

- usefulness;
- evidence sufficiency;
- correctness;
- clarity;
- artifact usability;
- appropriate uncertainty;
- appropriate abstention;
- engineering review burden.

Human evaluators must distinguish:

```text
Factually Correct
Evidence-Supported
Professionally Useful
Decision-Ready
```

These are not synonymous.

---

# 38. Consequential Error Analysis

Errors shall be classified by consequence:

1. Minor
2. Operationally significant
3. Engineering significant
4. Safety significant
5. Security significant
6. Confidentiality significant
7. Financial/legal significant

Aggregate accuracy shall not hide high-consequence failures.

The Phase 17 specification explicitly requires prioritizing consequential errors rather than aggregate accuracy.

---

# 39. Acceptance Logic

A Phase 17 result cannot be accepted solely because:

- a model answered correctly once;
- a document parsed successfully once;
- an agent completed one workflow;
- a sandbox executed code;
- no egress occurred during a normal run;
- an artifact opened successfully.

Acceptance requires reproducible evidence across representative and adversarial conditions.

---

# 40. Phase 17 Completion Gate

Phase 17 can be considered complete only when:

- highest-risk assumptions are identified;
- risks are ranked;
- every critical assumption has a falsifiable hypothesis;
- representative datasets exist;
- ground truth exists where feasible;
- experiments are reproducible;
- local model quality is measured;
- multimodal processing is measured;
- P&ID interpretation is measured;
- evidence-aware retrieval is measured;
- agent reliability is measured;
- verification is measured;
- sandbox security is adversarially tested;
- zero-egress is empirically tested;
- complete workflow hardware feasibility is measured;
- artifacts are evaluated;
- cross-component integration is tested;
- failure injection is performed;
- security boundaries remain active;
- sovereignty boundaries remain active;
- failures are recorded;
- architecture-changing evidence is identified;
- risks are retired/reduced/explicitly accepted;
- technology decisions are confirmed/rejected/reopened;
- reference hardware is validated or revised;
- implementation constraints are explicit;
- end-to-end acceptance tests exist;
- remaining uncertainties are classified.

These are the formal Phase 17 completion conditions.

---

# 41. Phase 18 Input Package

Phase 17 shall produce the following controlled inputs for implementation:

## 1. Validated Architecture Baseline

What survived experimentation.

## 2. Validated Technology Baseline

What technologies remain acceptable under tested conditions.

## 3. Reference Deployment Baseline

Validated CPU/RAM/GPU/storage/concurrency envelope.

## 4. Security Baseline

Validated boundaries and mandatory controls.

## 5. Validated Workflow Baseline

W3/W1/W2/W4 and W5 status.

## 6. Evaluation Baseline

Datasets, ground truth and metrics.

## 7. Performance Baseline

Measured workflow/resource behavior.

## 8. Known Limitations

Explicit unsupported cases.

## 9. Rejected Approaches

Technologies and architectures invalidated by evidence.

## 10. Open Questions

Remaining uncertainty.

## 11. Implementation Constraints

Concrete constraints derived from experiments.

## 12. Acceptance Tests

Tests required during MVP implementation.

## 13. Regression Tests

Tests that must remain green as implementation evolves.

The Phase 17 specification defines these as the controlled Phase 18 input package.

---

# 42. Current Evidence State

| Area | Current state |
|---|---|
| Product definition | Established |
| SRS | Established |
| System architecture | Established |
| Component architecture | Established |
| Data/knowledge architecture | Established |
| Agent runtime architecture | Established |
| Security architecture | Established with qualification conditions |
| Reference deployment | Candidate / validation required |
| Model baseline | Preferred candidates / validation required |
| Retrieval | Preferred architecture / validation required |
| P&ID pipeline | High-risk assumption |
| Agent reliability | Unvalidated |
| Verification effectiveness | Unvalidated |
| Sandbox | Unvalidated |
| Zero-egress | Unvalidated empirically |
| Hardware feasibility | Unvalidated |
| Artifact quality | Unvalidated |
| End-to-end integration | Unvalidated |

The distinction is intentional: the project already has architectural decisions, but Phase 17 is the point where those decisions must acquire empirical evidence.

---

# 43. Final Phase 17 Readiness Decision

## **NOT READY FOR MVP IMPLEMENTATION**

This is **not** a statement that the architecture is invalid.

It means:

> The architecture has reached the prototype/validation boundary, but the mandatory empirical evidence required to declare it ready for MVP implementation has not yet been produced.

The Phase 17 framework requires the final readiness decision to be based on evidence rather than project momentum.

The correct next action is therefore not more architecture writing.

It is execution of the highest-information experiments, beginning with:

```text
SP-09 — End-to-End Hardware Feasibility
        ↓
SP-01 — Local Model Quality
        ↓
SP-04 — Evidence-Aware Retrieval
        ↓
SP-03 — P&ID Structural Interpretation
        ↓
SP-05 — Agent Reliability
        ↓
SP-06 — Verification
        ↓
SP-07 — Sandbox
        ↓
SP-08 — Zero-Egress
        ↓
SP-10 — Artifacts
        ↓
W3 Thin Vertical Slice
```

---

# 44. Phase 17 Architectural Principle

The governing rule is:

> **Do not build the whole system to discover whether the architecture works. Build the smallest experiments capable of disproving the architecture before committing to it.**

And:

> **A technical spike succeeds when it reduces a consequential uncertainty—not when it produces an impressive demo.**

Therefore Phase 17 is successful only when it transforms:

```text
ARCHITECTURAL ASSUMPTIONS
        ↓
EXPERIMENTS
        ↓
EMPIRICAL EVIDENCE
        ↓
RISK RETIREMENT
        ↓
ARCHITECTURE CONFIRMATION / MODIFICATION / REJECTION
        ↓
IMPLEMENTATION CONSTRAINTS
        ↓
PHASE 18
```

rather than:

```text
ARCHITECTURE
 ↓
DEMO
 ↓
CONFIRMATION
```

# End of Phase 17 Specification