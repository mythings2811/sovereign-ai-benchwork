# Phase 7 — Product Decision Review

## 1. Executive Decision

### Phase-7 status

# **PRODUCT DECISIONS CLOSED WITH TARGETED VALIDATION**

The Phase-6 findings do not require a change to the fundamental product concept.

The product is now sufficiently coherent to establish a **product decision baseline**.

The remaining uncertainty is concentrated in:

* first deployment/customer profile;
* empirical hardware envelope;
* quantitative workflow-quality thresholds;
* agent reliability;
* customer acceptance of security/sovereignty evidence;
* final commercial positioning.

These are now treated as **controlled validation items**, not reasons to reopen the product concept.

The governing principle remains:

> **Reduce uncertainty through evidence and explicit decisions; do not silently convert assumptions into requirements.**

This is consistent with the project's evidence standard and decision methodology.

---

# 2. Product Decision Baseline

The following are now treated as **product-level decisions**.

| Decision                            | Status                                                          |
| ----------------------------------- | --------------------------------------------------------------- |
| Product category                    | **DECIDED**                                                     |
| Core problem                        | **DECIDED**                                                     |
| Core value proposition              | **DECIDED**                                                     |
| Sovereignty as core requirement     | **DECIDED**                                                     |
| Primary market direction            | **DECIDED — industrial engineering first**                      |
| Primary user direction              | **DECIDED — technical engineer / engineering knowledge worker** |
| Core product loop                   | **DECIDED**                                                     |
| Canonical workflows                 | **DECIDED**                                                     |
| Evidence-governed knowledge         | **DECIDED**                                                     |
| Bounded agentic execution           | **DECIDED**                                                     |
| External authorization              | **DECIDED**                                                     |
| Verification-native execution       | **DECIDED**                                                     |
| Provenance/auditability             | **DECIDED**                                                     |
| Multimodal technical processing     | **DECIDED**                                                     |
| P&ID structural representation      | **DECIDED**                                                     |
| Human consequential authority       | **DECIDED**                                                     |
| Code execution boundary             | **DECIDED**                                                     |
| OT autonomy boundary                | **DECIDED — prohibited for MVP**                                |
| Local/no-external-AI core operation | **DECIDED**                                                     |
| Single-system MVP boundary          | **DECIDED**                                                     |
| Exact first customer                | **OPEN**                                                        |
| Exact quantitative NFRs             | **VALIDATION REQUIRED**                                         |
| Exact hardware specification        | **VALIDATION REQUIRED**                                         |
| Exact model stack                   | **OPEN — Phase 8/architecture**                                 |
| Exact software architecture         | **OPEN — Phase 8/architecture**                                 |

The project already established that product direction, users, sovereignty, workload categories and research methodology are known decisions, while model stack, agent framework, RAG architecture, inference engine, sandbox technology, orchestration and deployment topology were deliberately unresolved.

---

# 3. Decision D-01 — Product Identity

## Decision

**Adopt:**

> **Sovereign Enterprise AI Workbench / Agentic Knowledge-Work Execution Environment**

PRD-level definition:

> **The Sovereign Agentic AI Workbench is a self-hosted AI execution environment for confidential enterprise knowledge work. It enables authorized technical and knowledge workers to investigate organizational information, analyze documents and engineering material, execute bounded multi-step workflows, and produce verified enterprise artifacts while keeping data and AI processing within a controlled deployment boundary.**

## Alternatives considered

| Alternative                    | Decision     | Reason                                |
| ------------------------------ | ------------ | ------------------------------------- |
| Local chatbot                  | Reject       | Too narrow                            |
| RAG platform                   | Reject       | Implementation-centric                |
| AI agent platform              | Reject       | Does not express sovereignty/evidence |
| Document intelligence platform | Reject       | Too narrow                            |
| Generic enterprise AI platform | Reject       | Too broad                             |
| Sovereign AI workbench         | **Selected** | Best representation of actual product |
| Autonomous enterprise AI       | Reject       | Incorrect authority model             |

## Confidence

**High**

The product definition is already supported by the research-to-product chain. The core idea is explicitly an internal AI workbench that keeps confidential information within the organization.

---

# 4. Decision D-02 — Primary Market

## Decision

### First market direction

> **Confidentiality-sensitive industrial engineering organizations, with refinery/process-industry environments as the primary target direction.**

Secondary markets:

1. PSUs / industrial public-sector organizations;
2. defence-linked manufacturing;
3. government technical organizations;
4. other engineering-intensive confidential enterprises.

## Why

This segment has the strongest intersection of:

* confidential information;
* engineering documents;
* P&IDs/drawings;
* inspection reports;
* historical technical knowledge;
* high consequence of incorrect information;
* need for local processing.

This is already supported by the product definition and workflow evidence.

## What is *not* decided

The exact first customer organization remains open.

### Status

**DECIDED at market-direction level**

**OPEN at first-customer level**

---

# 5. Decision D-03 — Primary User

## Decision

> **Technical engineer / engineering knowledge worker**

The initial product experience should optimize for a user who routinely works across:

* technical documents;
* organizational knowledge;
* engineering information;
* inspection material;
* drawings/P&IDs;
* evidence-based analysis.

Supporting users:

* inspection/reliability professional;
* technical analyst;
* documentation/approval professional;
* developer;
* management reviewer.

Administrative users remain distinct:

* system administrator;
* security administrator;
* deployment/operator;
* AI governance/compliance.

The distinction is important because the user performs the work while governance/security roles control the environment.

### Status

# **DECIDED**

---

# 6. Decision D-04 — MVP Workflow Boundary

This is the most important scope decision.

## Decision

### Core MVP

1. **W3 — Organizational Knowledge Investigation**
2. **W1 — Inspection / Technical Report Analysis**
3. **W2 — P&ID / Engineering Drawing Analysis**
4. **W4 — Technical Report / Approval Artifact Generation**

### Conditional/supporting MVP

5. **W5 — Controlled Code-Assisted Technical Analysis**

The five workflows are retained because collectively they exercise the product's core capabilities without requiring universal enterprise automation.

---

# 7. MVP Workflow Hierarchy

## Tier 1 — Product-Proving Workflows

### W3 — Organizational Knowledge Investigation

Purpose:

> Prove the general sovereign enterprise knowledge-work loop.

Core chain:

```text
Question
 ↓
Task understanding
 ↓
Authorization
 ↓
Evidence retrieval
 ↓
Authority/revision filtering
 ↓
Evidence sufficiency
 ↓
Synthesis
 ↓
Verification
 ↓
Evidence-linked result
 ↓
Audit
```

## W1 — Inspection / Technical Report Analysis

Purpose:

> Prove industrial document intelligence.

Exercises:

* scans;
* OCR;
* tables;
* images;
* historical information;
* cross-document reasoning;
* evidence-grounded findings.

## W2 — P&ID / Engineering Drawing Analysis

Purpose:

> Prove the strongest technical/multimodal differentiator.

Exercises:

* visual evidence;
* OCR/layout;
* engineering entities;
* topology;
* relationships;
* revisions;
* domain verification.

The project explicitly resolved P&ID interpretation as image + OCR/layout + engineering graph + domain rules, with the engineer retaining consequential authority.

## W4 — Technical Report / Approval Artifact Generation

Purpose:

> Prove that the system converts verified analysis into usable enterprise deliverables.

## W5 — Controlled Code-Assisted Analysis

Purpose:

> Validate safe computational execution.

It remains conditional because its security and operational burden is materially higher than W3/W1/W2/W4.

### Final decision

# **W3 + W1 + W2 + W4 = committed MVP**

# **W5 = conditional MVP capability**

---

# 8. Decision D-05 — MVP Demonstration Sequence

## Decision

Use:

> **W3 → W1 → W2 → W4**

### Rationale

| Sequence | Demonstrates                           |
| -------- | -------------------------------------- |
| W3       | General sovereign knowledge-work loop  |
| W1       | Industrial document intelligence       |
| W2       | Engineering/multimodal differentiation |
| W4       | Verified enterprise output             |

W5 can be demonstrated separately as a security/technical capability rather than making it the main product story.

This preserves both the broad product proposition and the industrial differentiation. The established workflow ranking supports W3 first, followed by W1 and W2.

---

# 9. Decision D-06 — Core Product Loop

## Decision

Freeze the following as the canonical product behavior:

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

Not:

```text
Prompt
 ↓
LLM
 ↓
Answer
```

The difference is fundamental to product identity. The project explicitly defines the product as an execution environment around confidential knowledge work rather than merely an inference interface.

### Status

# **FROZEN**

---

# 10. Decision D-07 — Evidence as a First-Class Product Object

## Decision

The Workbench shall treat **evidence** as a first-class product concept.

Evidence must carry, where applicable:

* source identity;
* authorization;
* authority;
* revision;
* temporal validity;
* provenance;
* source region;
* extraction context;
* verification state.

Semantic similarity alone is insufficient.

The research established that enterprise knowledge must distinguish relevant, current, authoritative, authorized and validated information.

### Status

# **FROZEN**

---

# 11. Decision D-08 — Evidence Sufficiency

## Decision

The system must explicitly determine whether available evidence is sufficient for the requested conclusion.

Possible states:

```text
SUFFICIENT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
UNVERIFIABLE
```

Possible responses:

```text
Retrieve more
Ask user
Escalate
Request approval
Abstain
Stop
```

The system must not treat retrieval completion as evidence sufficiency.

This follows directly from the established evidence-gate model.

### Status

# **FROZEN**

---

# 12. Decision D-09 — Agent Authority

## Decision

The agent may decide:

* task decomposition;
* evidence search;
* capability selection;
* permitted tool selection;
* retrieval refinement;
* bounded retry;
* escalation;
* bounded workflow progression.

The agent may **not** decide:

* its own permissions;
* organizational authority;
* formal approval;
* consequential engineering authority;
* unrestricted OT action.

Canonical security chain:

```text
Identity
 ↓
Security Context
 ↓
Policy
 ↓
Capability
 ↓
Agent
 ↓
Tool Request
 ↓
Policy Re-check
 ↓
Execution
```

The research explicitly establishes that agent authority must remain outside the LLM.

### Status

# **FROZEN**

---

# 13. Decision D-10 — Autonomy Boundary

## Decision

| Level | Meaning                          | MVP            |
| ----- | -------------------------------- | -------------- |
| L0    | User-directed                    | **Allowed**    |
| L1    | Assisted                         | **Allowed**    |
| L2    | Bounded agentic execution        | **Core**       |
| L3    | Conditional autonomy             | **Limited**    |
| L4    | Autonomous organizational action | **Prohibited** |

### Consequential rule

> The system may automate reasoning and bounded execution; it may not autonomously assume organizational authority.

This resolves the principal autonomy/security contradiction.

### Status

# **FROZEN**

---

# 14. Decision D-11 — Human Responsibility

## Decision

Humans retain final responsibility for:

* consequential engineering decisions;
* safety decisions;
* formal approvals;
* legal decisions;
* financial decisions;
* personnel decisions;
* physical-world actions;
* OT/production actions.

The AI provides:

* investigation;
* extraction;
* correlation;
* reasoning;
* drafting;
* computation;
* evidence organization.

### Status

# **FROZEN**

---

# 15. Decision D-12 — P&ID Representation

## Decision

Do **not** use a pure image or OCR representation.

Required conceptual representation:

```text
Visual observation
       +
OCR / layout evidence
       +
Engineering structural representation
       +
Domain interpretation
       +
Human engineering authority
```

The minimum engineering representation must preserve relevant:

* equipment;
* instruments;
* valves;
* piping;
* tags;
* connections;
* flow relationships;
* spatial relationships;
* source regions;
* revisions;
* cross-document references.

### Status

# **FROZEN AT PRODUCT-CONCEPT LEVEL**

The exact ontology/schema remains an architecture/data-design matter.

---

# 16. Decision D-13 — Verification

## Decision

Verification is part of completion, not an optional post-processing feature.

Verification shall combine as appropriate:

```text
Deterministic checks
+
Evidence checks
+
Semantic/model checks
+
Numerical checks
+
Policy checks
+
Human/domain review
```

The system must never equate:

* model confidence with correctness;
* citation with correctness;
* successful execution with correct result;
* successful artifact generation with acceptable artifact.

The research explicitly rejects those equivalences.

### Status

# **FROZEN**

---

# 17. Decision D-14 — Completion Semantics

## Decision

Workflow completion shall be determined by **explicit completion predicates**, not an LLM saying "done."

Completion requires satisfaction of the applicable workflow contract.

Example:

```text
Objective satisfied
AND
authorization satisfied
AND
required evidence obtained
AND
evidence sufficient
AND
required processing completed
AND
verification passed
AND
required human acceptance completed
AND
audit/provenance captured
```

Not every workflow requires every predicate.

### Status

# **FROZEN**

---

# 18. Decision D-15 — Failure and Abstention

## Decision

Abstention is a **successful safety behavior**, not necessarily a system failure.

The system shall distinguish:

* successful completion;
* incomplete;
* insufficient evidence;
* conflict;
* stale evidence;
* authorization failure;
* verification failure;
* security block;
* resource failure;
* unrecoverable failure.

Recovery model:

```text
Detect
 ↓
Classify
 ↓
Recover if safe
 ↓
Retry only when justified
 ↓
Re-verify
 ↓
Complete / escalate / abstain / stop
```

Blind retry is rejected.

This follows the failure model already established in the workflow specification.

### Status

# **FROZEN**

---

# 19. Decision D-16 — Sovereignty

## Decision

"Sovereign" shall **not** mean merely:

> software is installed locally.

It means the deployment establishes a controlled boundary covering:

* confidential data;
* intermediate representations;
* model execution;
* retrieval;
* tools;
* generated code;
* artifacts;
* network communication;
* model/software supply chain;
* updates;
* relevant telemetry.

The sovereignty claim must be demonstrated through evidence.

The project explicitly establishes local processing, no external AI API dependency, controlled networking, zero-egress posture, offline model/artifact management and sovereignty evidence as hard constraints.

### Status

# **FROZEN**

---

# 20. Decision D-17 — Zero Egress

## Decision

Zero-egress is a distinct security requirement.

It must be:

```text
Enforced
+
Observed
+
Adversarially tested
```

Not:

```text
"We configured the application not to call the Internet."
```

### Status

# **FROZEN**

---

# 21. Decision D-18 — Supply-Chain Sovereignty

## Decision

The sovereignty boundary includes:

* models;
* model weights;
* inference dependencies;
* OCR models;
* packages;
* containers;
* drivers;
* software dependencies;
* update bundles.

Controlled offline lifecycle is therefore a product/deployment requirement.

The research identifies software/model supply-chain integrity as part of sovereignty rather than a separate convenience feature.

### Status

# **FROZEN**

---

# 22. Decision D-19 — Security Boundary

## Decision

The Workbench is responsible for controlling:

* identity context received by the product;
* task context;
* data access;
* model exposure;
* tool access;
* code execution;
* artifacts;
* provenance;
* audit;
* product-controlled network communication;
* policy enforcement.

It does not claim to replace:

* enterprise identity systems;
* physical security;
* enterprise network security;
* site security;
* human organizational authority.

### Status

# **FROZEN**

---

# 23. Decision D-20 — OT / ICS Boundary

## Decision

The MVP may analyze:

* engineering information;
* operational documentation;
* P&IDs;
* maintenance/inspection material;
* technical history.

It shall **not** provide unrestricted autonomous control over:

* PLC;
* DCS;
* SIS;
* physical equipment;
* production-control state.

The research explicitly identifies OT/CII as a separate risk boundary.

### Status

# **FROZEN**

---

# 24. Decision D-21 — Code Execution

## Decision

Code execution is permitted only as a **bounded computational capability**.

Generated code is treated as untrusted.

The product must conceptually provide:

* isolation;
* resource limits;
* restricted filesystem;
* restricted credentials;
* network isolation;
* execution records;
* result validation.

Successful process execution does not constitute correctness.

### Status

# **FROZEN AT REQUIREMENT LEVEL**

The exact sandbox implementation remains an architecture decision.

---

# 25. Decision D-22 — Artifact Generation

## Decision

Artifact generation is a core output capability, but artifact formats are deliberately limited.

Initial emphasis:

* technical reports;
* findings;
* approval-note drafts;
* structured enterprise documents.

Additional formats such as broad spreadsheet/presentation generation remain conditional.

### Critical rule

> **Draft generation is not approval.**

The AI can prepare an approval artifact; authorized humans approve/release it.

### Status

# **FROZEN**

---

# 26. Decision D-23 — Provenance

## Decision

Important outputs must be traceable:

```text
Source
 ↓
Processing
 ↓
Evidence
 ↓
Derived information
 ↓
Claim
 ↓
Decision/analysis
 ↓
Artifact
```

This is a product trust property, not merely an audit database.

The research establishes source-to-claim-to-decision-to-artifact provenance as a core requirement.

### Status

# **FROZEN**

---

# 27. Decision D-24 — Auditability

## Decision

Significant workflow execution must preserve enough information to reconstruct:

* who;
* what task;
* what information;
* what permissions;
* what capabilities/models;
* what evidence;
* what tools;
* what actions;
* what failures;
* what retries;
* what verification;
* what approvals;
* what output;
* what environment/version.

Audit is therefore part of the product trust model.

### Status

# **FROZEN**

---

# 28. Decision D-25 — Knowledge Model

## Decision

The Workbench shall use a **governed evidence model**, not simply a "knowledge base."

Knowledge must support states such as:

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

AI-derived information cannot silently become authoritative enterprise knowledge.

### Status

# **FROZEN**

---

# 29. Decision D-26 — Multimodality

## Decision

Core MVP modalities:

* text;
* scanned documents;
* images;
* tables;
* drawings;
* P&IDs.

Conditional/future:

* handwriting;
* audio;
* video;
* broader advanced modalities.

The original product concept includes multimodal processing, but Phase 7 narrows this into workflow-relevant modalities rather than promising universal multimodality.

### Status

# **FROZEN**

---

# 30. Decision D-27 — Architecture Independence

## Decision

The product PRD shall specify **what must happen**, not which technology performs it.

Therefore the following remain open:

* model family;
* model size;
* inference engine;
* agent framework;
* retrieval engine;
* database;
* OCR implementation;
* sandbox technology;
* deployment topology;
* orchestration implementation.

The project methodology explicitly distinguishes established product decisions from unresolved technology decisions.

### Status

# **FROZEN PRINCIPLE**

---

# 31. Decision D-28 — Multi-Model Product Strategy

## Decision

The product shall support **multiple local AI capabilities**.

It shall not require one universal model to perform every workload.

The product-level requirement is:

> Different tasks may use different local AI capabilities, and capability selection may adapt to task requirements, verification needs and resource constraints.

### Not yet decided

* number of models;
* model families;
* model sizes;
* quantization;
* routing algorithm.

### Status

# **DECIDED AT PRODUCT LEVEL**

# **IMPLEMENTATION OPEN**

---

# 32. Decision D-29 — Hardware Boundary

## Decision

### Hard

> MVP must operate on a single workstation/server.

### Soft

> Mid-range GPU is preferred.

### Not yet decided

* exact GPU;
* VRAM;
* CPU;
* RAM;
* storage;
* concurrency;
* latency;
* model residency.

These must be experimentally established.

The existing constraint register explicitly marks GPU memory, CPU/RAM, storage, concurrency and model residency as validation items.

### Status

# **BOUNDARY FROZEN**

# **NUMERICAL ENVELOPE OPEN**

---

# 33. Decision D-30 — Product Quality Philosophy

## Decision

The Workbench shall be evaluated as an **end-to-end workflow system**, not as a collection of individually impressive components.

Primary evaluation unit:

> **Verified workflow completion**

Supporting metrics include:

* retrieval quality;
* authority accuracy;
* revision accuracy;
* authorization accuracy;
* grounding;
* OCR;
* multimodal interpretation;
* P&ID topology;
* verification;
* artifact quality;
* resource behavior;
* failure/recovery;
* security.

### Status

# **FROZEN**

---

# 34. Decision D-31 — Quantitative Threshold Policy

## Decision

Do **not** invent thresholds at this stage.

Threshold-setting procedure:

```text
Benchmark baseline
 ↓
Observe failure distribution
 ↓
Identify unacceptable failure classes
 ↓
Set minimum acceptance threshold
 ↓
Set engineering target
 ↓
Set stretch target
```

Thresholds must be evidence-backed.

This preserves the project's explicit requirement that unresolved quantitative values remain "Requires Validation" rather than being fabricated.

### Status

# **FROZEN POLICY**

# **VALUES OPEN**

---

# 35. Decision D-32 — Customer Qualification

## Decision

Production qualification must use customer-representative data.

Public/synthetic data may support:

* development;
* regression;
* initial experimentation;
* model comparison.

Customer-local data is required for:

* final workflow qualification;
* authority/revision validation;
* ACL validation;
* domain terminology;
* P&ID conventions;
* production acceptance.

The research explicitly establishes customer-local data as necessary for production qualification.

### Status

# **FROZEN**

---

# 36. Decision D-33 — First Customer

## Decision

### No unsupported choice will be made.

The project has enough evidence to establish:

> **industrial engineering / refinery-oriented organizations as the first market direction**

but not enough evidence to name a specific first customer or exact deployment environment.

### Required next evidence

* customer interviews;
* workflow observation;
* security review;
* representative corpus;
* hardware environment;
* acceptance criteria;
* deployment constraints.

### Status

# **OPEN QUESTION**

This is deliberately not converted into a false product decision.

---

# 37. Decision D-34 — Commercial Positioning

## Decision

The product should **not** be positioned primarily as:

> "Private ChatGPT."

Nor:

> "Local LLM platform."

Nor:

> "Enterprise RAG."

The stronger positioning is:

> **Sovereign AI execution for confidential technical knowledge work.**

Supporting message:

> Investigate internal knowledge, analyze technical documents, execute bounded AI workflows and produce verified enterprise outputs without sending confidential information to external AI services.

### Status

# **PROVISIONALLY FROZEN**

Final messaging requires customer/competitive validation.

---

# 38. Decision D-35 — Differentiation

## Decision

The differentiator is **not an individual technology**.

It is the integrated combination:

```text
Sovereignty
+
Enterprise evidence
+
Technical multimodality
+
Bounded agentic execution
+
Controlled tools
+
Verification
+
Provenance
+
Enterprise artifacts
+
Auditability
```

### Strategic interpretation

The defensible layer is expected to develop around:

* customer-specific workflow knowledge;
* evaluation corpus;
* evidence/provenance model;
* deployment/security profiles;
* verified workflow behavior;
* operational integration.

This remains a **strategic hypothesis**, not a proven moat.

### Status

# **PROVISIONALLY DECIDED**

---

# 39. Final Product Boundary

## Inside the product

```text
Confidential task
        ↓
Task understanding
        ↓
Security context
        ↓
Evidence discovery
        ↓
Enterprise knowledge
        ↓
Document/multimodal processing
        ↓
Bounded agent reasoning
        ↓
Controlled tools
        ↓
Verification
        ↓
Artifact/result
        ↓
Human acceptance where required
        ↓
Provenance + audit
        ↓
Sovereignty evidence
```

## Outside the product

```text
Unrestricted autonomous organization
        X

Autonomous OT control
        X

Formal organizational approval
        X

Universal enterprise automation
        X

Consumer AI assistant
        X

Giant model-training infrastructure
        X

Universal digital twin
        X

Universal enterprise ontology
        X

Unrestricted external communication
        X
```

This preserves the original hard boundaries against scope expansion.

---

# 40. Decision Register

| ID   | Decision                            | Status                  | Confidence | Validation                |
| ---- | ----------------------------------- | ----------------------- | ---------- | ------------------------- |
| D-01 | Product identity                    | **Decided**             | High       | None required             |
| D-02 | Industrial engineering first market | **Decided**             | High       | Customer validation       |
| D-03 | Technical engineer primary user     | **Decided**             | High       | User validation           |
| D-04 | Four committed MVP workflows        | **Decided**             | High       | Workflow validation       |
| D-05 | W3→W1→W2→W4 demo sequence           | **Decided**             | High       | Demo validation           |
| D-06 | Core execution loop                 | **Frozen**              | High       | None                      |
| D-07 | Evidence first-class                | **Frozen**              | High       | Implementation validation |
| D-08 | Evidence sufficiency gate           | **Frozen**              | High       | Benchmark                 |
| D-09 | External agent authority            | **Frozen**              | High       | Security test             |
| D-10 | L0–L3 bounded autonomy              | **Frozen**              | High       | Risk validation           |
| D-11 | Human consequential authority       | **Frozen**              | High       | Governance validation     |
| D-12 | P&ID structural representation      | **Frozen conceptually** | High       | Engineering benchmark     |
| D-13 | Layered verification                | **Frozen**              | High       | Evaluation                |
| D-14 | Predicate-based completion          | **Frozen**              | High       | Workflow test             |
| D-15 | Explicit failure/abstention         | **Frozen**              | High       | Adversarial test          |
| D-16 | Sovereignty as composite property   | **Frozen**              | High       | Deployment test           |
| D-17 | Zero-egress                         | **Frozen**              | High       | Adversarial network test  |
| D-18 | Supply-chain sovereignty            | **Frozen**              | High       | Deployment validation     |
| D-19 | Security boundary                   | **Frozen**              | High       | Security validation       |
| D-20 | OT autonomy prohibited              | **Frozen**              | High       | Security review           |
| D-21 | Controlled code execution           | **Frozen conceptually** | High       | Sandbox validation        |
| D-22 | Verified artifact generation        | **Frozen**              | High       | Artifact benchmark        |
| D-23 | Claim/evidence provenance           | **Frozen**              | High       | Traceability test         |
| D-24 | Auditability                        | **Frozen**              | High       | Audit replay              |
| D-25 | Governed evidence states            | **Frozen**              | High       | Data validation           |
| D-26 | Core multimodality                  | **Frozen**              | High       | Workflow benchmark        |
| D-27 | Architecture independence           | **Frozen principle**    | High       | Review                    |
| D-28 | Multiple local capabilities         | **Decided**             | High       | Hardware/model benchmark  |
| D-29 | Single-system MVP                   | **Frozen**              | High       | Hardware qualification    |
| D-30 | Workflow-level evaluation           | **Frozen**              | High       | Evaluation                |
| D-31 | Evidence-backed thresholds          | **Frozen policy**       | High       | Benchmark                 |
| D-32 | Customer-local qualification        | **Frozen**              | High       | Pilot                     |
| D-33 | First exact customer                | **Open**                | —          | Customer validation       |
| D-34 | Commercial positioning              | **Provisional**         | Medium     | Buyer validation          |
| D-35 | Durable moat                        | **Hypothesis**          | Medium     | Market validation         |

---

# 41. Remaining Product Decisions

Only the following remain materially open.

## Critical

### P-OPEN-01 — First deployment profile

**Question:** Which exact customer environment becomes the first qualification target?

**Impact:** Very High

**Status:** Open

---

### P-OPEN-02 — MVP hardware envelope

**Question:** What hardware can support the committed workflows at acceptable quality/performance?

**Impact:** Critical

**Status:** Requires Validation

---

### P-OPEN-03 — Workflow reliability threshold

**Question:** What verified completion/recovery/abstention behavior is acceptable?

**Impact:** Critical

**Status:** Requires Validation

---

### P-OPEN-04 — Quality thresholds

**Question:** What quality level is required for W1/W2/W3/W4?

**Impact:** Critical

**Status:** Requires Validation

---

### P-OPEN-05 — Security acceptance profile

**Question:** What exact adversarial/security evidence will the first customer require?

**Impact:** Critical

**Status:** Requires Validation

---

## High

### P-OPEN-06 — W2 qualification level

If W2 remains committed MVP, engineering benchmark results must determine its supported scope.

### P-OPEN-07 — W5 inclusion level

Determine whether W5 remains conditional or becomes a committed MVP workflow after sandbox/hardware validation.

### P-OPEN-08 — Artifact format

Select the initial artifact format based on actual customer workflow.

### P-OPEN-09 — Audit retention

Requires customer/legal/security policy.

### P-OPEN-10 — Authority hierarchy

Requires customer-specific enterprise metadata.

---

# 42. Explicitly Deferred

The following must **not** be decided in Phase 7:

* exact LLM;
* model size;
* quantization;
* inference engine;
* routing implementation;
* agent framework;
* RAG engine;
* vector database;
* OCR engine;
* sandbox implementation;
* database;
* orchestration technology;
* deployment topology.

These are Phase-8 architecture/technology-selection decisions.

The project's prerequisite framework explicitly requires technologies to be evaluated against project-specific criteria rather than selected by popularity or generic capability.

---

# 43. Decision Conflicts Resolved

## Conflict A — Product breadth vs MVP feasibility

### Resolution

Keep four committed workflows and one conditional workflow.

**Resolved.**

---

## Conflict B — Agent autonomy vs organizational authority

### Resolution

Agent controls bounded execution; external policy controls authority.

**Resolved.**

---

## Conflict C — Multimodality vs hardware

### Resolution

Multimodality is required, but workload-specific capability activation and empirical hardware qualification determine implementation breadth.

**Resolved at product level; hardware validation pending.**

---

## Conflict D — Auditability vs privacy

### Resolution

Auditability remains mandatory, but exact retention/redaction/deletion policy is deployment-specific.

**Product principle resolved; policy details open.**

---

## Conflict E — Offline operation vs lifecycle updates

### Resolution

Runtime can remain offline while updates occur through controlled offline supply-chain mechanisms.

**Resolved.**

---

## Conflict F — Generic enterprise market vs technical specialization

### Resolution

Start with industrial engineering; do not optimize MVP for generic enterprise productivity.

**Resolved.**

---

# 44. Decision Quality Audit

## Facts

* Confidential enterprise knowledge is the central problem.
* Sovereignty is a hard requirement.
* Multimodal technical information is required.
* P&ID interpretation requires structural representation.
* Human consequential authority remains necessary.
* Agent permissions must be externally controlled.
* Customer-local data is required for production qualification.

## Conclusions

* The product should be an execution workbench rather than a chatbot.
* Evidence should be a first-class product object.
* Verification should be part of completion.
* Industrial engineering is the correct initial product direction.

## Assumptions

* The committed workflows can meet quality requirements on practical hardware.
* Users will prefer the proposed evidence/verification model.
* The combined product proposition has sufficient commercial differentiation.

## Estimates

None frozen.

## Hypotheses

* Customer-specific evaluation/provenance/deployment knowledge will form part of the long-term moat.
* Adaptive multi-model execution will provide a useful quality/resource trade-off.

## Unknowns

* exact hardware;
* exact performance;
* exact reliability;
* exact quality thresholds;
* first customer;
* exact deployment assurance profile.

This classification follows the project's explicit requirement to distinguish facts, inferences, assumptions and open questions.

---

# 45. Phase-7 Readiness Matrix

| Product Area             | Decision Status           |
| ------------------------ | ------------------------- |
| Product identity         | **READY**                 |
| Product problem          | **READY**                 |
| Primary market direction | **READY**                 |
| Primary user             | **READY**                 |
| Core workflows           | **READY**                 |
| MVP boundary             | **READY**                 |
| Product loop             | **READY**                 |
| Evidence model           | **READY**                 |
| Agent authority          | **READY**                 |
| Autonomy boundary        | **READY**                 |
| Human responsibility     | **READY**                 |
| Multimodality            | **READY**                 |
| P&ID conceptual boundary | **READY**                 |
| Verification             | **READY**                 |
| Failure/abstention       | **READY**                 |
| Security boundary        | **READY**                 |
| Sovereignty              | **READY**                 |
| OT boundary              | **READY**                 |
| Artifact boundary        | **READY**                 |
| Audit/provenance         | **READY**                 |
| Hardware boundary        | **READY WITH VALIDATION** |
| Quality thresholds       | **READY WITH VALIDATION** |
| Reliability thresholds   | **READY WITH VALIDATION** |
| First deployment profile | **OPEN**                  |
| Exact technology         | **DEFERRED**              |
| Architecture             | **DEFERRED**              |

---

# 46. Final Phase-7 Gate

# **GATE A — PRODUCT DECISION BASELINE ESTABLISHED**

Phase 7 does **not** claim that the system is technically validated.

It establishes that the product decisions required to proceed are sufficiently clear.

### Product definition

**PASS**

### Scope

**PASS**

### Workflow hierarchy

**PASS**

### Human/AI boundary

**PASS**

### Security boundary

**PASS**

### Sovereignty boundary

**PASS**

### Verification model

**PASS**

### Evidence model

**PASS**

### Failure model

**PASS**

### MVP boundary

**PASS**

### Quantitative qualification

**PENDING TARGETED VALIDATION**

### First deployment

**OPEN**

### Architecture

**DEFERRED CORRECTLY**

---

# 47. Phase-7 Final Product Decision

The authoritative product thesis is now:

> **The Sovereign Agentic AI Workbench is a self-hosted execution environment for confidential technical knowledge work. It allows authorized engineering and technical users to investigate enterprise knowledge, analyze heterogeneous technical information, execute bounded multi-step AI workflows and produce verified enterprise outputs while keeping confidential information and AI processing within a controlled deployment boundary.**

Its product architecture at the conceptual level is:

```text
                 USER
                   │
                   ▼
            CONFIDENTIAL TASK
                   │
                   ▼
          TASK UNDERSTANDING
                   │
                   ▼
        SECURITY / AUTHORIZATION
                   │
                   ▼
       EVIDENCE + CAPABILITY NEED
              ┌────┴────┐
              ▼         ▼
       ENTERPRISE    MULTIMODAL
        KNOWLEDGE     PROCESSING
              └────┬────┘
                   ▼
             PLAN / REASON
                   │
                   ▼
          BOUNDED EXECUTION
                   │
             ┌─────┴─────┐
             ▼           ▼
          TOOLS       CODE*
             │           │
             └─────┬─────┘
                   ▼
              VERIFICATION
                   │
             ┌─────┴─────┐
             ▼           ▼
          RESULT      ARTIFACT
             │           │
             └─────┬─────┘
                   ▼
          HUMAN ACCEPTANCE
            WHEN REQUIRED
                   │
                   ▼
        PROVENANCE + AUDIT
                   │
                   ▼
        SOVEREIGNTY EVIDENCE

* only for bounded supported workflows
```

The product is therefore **not**:

> "an LLM running locally."

It is:

> **a governed, evidence-driven, bounded AI execution environment for confidential technical knowledge work.**

---

# 48. Phase-8 Input Contract

Phase 8 can now proceed from a stable product decision baseline.

It should answer:

1. What architecture best implements the frozen product behavior?
2. What technical primitives are mandatory?
3. Which candidates satisfy the requirements?
4. Which alternatives fail?
5. What should be selected and why?
6. What must remain replaceable?
7. What architecture satisfies the sovereignty/security boundaries?
8. What architecture can meet the measured hardware envelope?
9. What components require prototype validation?
10. What is the minimum viable implementation?

The architecture-selection process must continue to use the project's evidence discipline:

```text
Requirement
 ↓
Constraint
 ↓
Architecture alternative
 ↓
Mechanism
 ↓
Benchmark
 ↓
Failure mode
 ↓
Security implication
 ↓
Operational implication
 ↓
Comparison
 ↓
Decision
```

The project control layer explicitly defines this evidence-to-decision progression as the intended research/design process.

---

# FINAL STATUS

## **PHASE 7 — COMPLETE**

### Gate:

# **A — PRODUCT DECISION BASELINE ESTABLISHED**

### Frozen now

**Product identity + target direction + primary user + MVP workflows + product loop + evidence model + bounded autonomy + human authority + verification + provenance + audit + sovereignty + security + multimodal boundary + OT boundary + artifact boundary + scope exclusions.**

### Still validation-dependent

**First deployment + hardware envelope + quantitative quality + reliability + security acceptance + customer qualification.**

### Explicitly deferred

**Architecture + technology stack + exact models + inference engine + agent framework + retrieval implementation + sandbox technology + deployment topology.**

**Next phase: Phase 8 — Architecture & Technology Selection.**
