**Objective — Phase 1:** Convert the closed Phase-0 Research Decision Base into an evidence-backed **Product Requirement Candidate Register**, with explicit priorities, acceptance concepts, dependencies, conflicts, gaps, and a readiness gate for Phase 2. The phase must remain product/requirement-focused and must not freeze architecture or technology. This follows the Phase-1 prompt's explicit transformation of **Evidence → Finding → Product Implication → Requirement / Decision / Open Question**. 

Phase 0 is treated as the primary decision base. Its gate was **B — READY WITH TARGETED VALIDATION**, meaning the product behavior can now be specified even though workflow, hardware, reliability, artifact, and deployment-specific validation remain open. 

# Phase 1 — Research-to-Requirement Synthesis

## 1. Requirement engineering boundary

I am applying these boundaries strictly:

* **Requirements:** what the product must achieve.
* **Acceptance concepts:** how the requirement can eventually be tested.
* **Decisions:** product-level choices justified by evidence.
* **Open questions:** unresolved matters that cannot responsibly be frozen.
* **Technology:** deliberately not selected here.
* **Architecture:** deliberately not designed here.

This is directly required by the Phase-1 prompt, including its prohibition on selecting implementation technologies, final models, agent frameworks, RAG implementation, databases, or architecture.  

---

# 2. Requirement hierarchy

The resulting hierarchy is:

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
Sovereignty Requirements
        ↓
Data Requirements
        ↓
Evaluation Requirements
        ↓
Deployment Requirements
        ↓
Acceptance Criteria
```

This preserves the Phase-0 starting hierarchy and the Phase-1 requirement taxonomy. 

---

# 3. Product Requirement Candidate Register

The Phase-1 prompt specifies the exact fields for this register: Requirement ID, Requirement, Source Research, Evidence, Source, Rationale, Priority, Type, Acceptance Concept, Dependency, Confidence, Open Issue, and Status. 

## 3.1 Product & User Experience

| ID         | Requirement                                                                                                                                                                              | Source Research | Evidence                                                                                                           | Source                                 | Rationale                                                                       | Priority     | Type       | Acceptance Concept                                                                | Dependency                    | Confidence | Open Issue                                         | Status               |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------- | ------------ | ---------- | --------------------------------------------------------------------------------- | ----------------------------- | ---------- | -------------------------------------------------- | -------------------- |
| PRD-UX-001 | The system shall allow an authorized user to submit confidential enterprise knowledge-work tasks without transferring the underlying confidential information to an external AI service. | R1/R2, EF-01/02 | Confidential enterprise information is the core problem; no external AI API dependency is a hard constraint.       | Phase 0 EF-01, EF-02, SR-01/SR-02      | Establishes the fundamental user proposition.                                   | **Critical** | User       | Execute representative confidential tasks with no external AI service dependency. | Sovereignty requirements      | High       | None at requirement level.                         | **Candidate**        |
| PRD-UX-002 | The system shall provide conversational, task-oriented interaction for confidential enterprise workflows.                                                                                | R1/R3           | Market expectations include conversational interaction while the product is intended for knowledge-work execution. | Phase 0 Competitive Requirements       | A sovereign system still needs usable AI-assistant interaction.                 | High         | User       | Representative users complete defined workflows through the task interface.       | PRD-UX-001                    | High       | Exact UX patterns remain open.                     | **Candidate**        |
| PRD-UX-003 | The system shall allow users to inspect the status and outcome of significant task-execution steps.                                                                                      | R5/R6/R8        | Silent and partial failures, tool misuse, provenance loss, and false completion require observable execution.      | Phase 0 FM-08/FM-11/FM-18/FM-19; SR-11 | Users and administrators need to distinguish execution from claimed completion. | High         | Functional | Execution trace exposes defined significant steps and outcomes.                   | Agent execution; auditability | High       | Exact level of UI exposure requires UX validation. | **Strong Candidate** |
| PRD-UX-004 | The system shall clearly distinguish successful completion, incomplete execution, insufficient evidence, conflict, authorization failure, and verification failure.                      | R5/R7           | Phase 0 explicitly rejects LLM-declared completion and identifies multiple evidence/execution failure states.      | Phase 0 EF-06, FM-06/FM-11             | Prevents users from interpreting failure as successful completion.              | High         | Functional | Inject each failure class and verify distinct resulting state.                    | Verification; evidence gate   | High       | Exact user-facing terminology may change.          | **Strong Candidate** |

---

## 3.2 Business Requirements

| ID         | Requirement                                                                                                                                       | Source Research    | Evidence                                                                            | Source                                               | Rationale                                                             | Priority     | Type     | Acceptance Concept                                                                         | Dependency                               | Confidence | Open Issue                                 | Status               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------ | ---------------------------------------- | ---------- | ------------------------------------------ | -------------------- |
| PRD-BR-001 | The product shall enable confidential enterprise knowledge work using AI while keeping processing within the customer's defined control boundary. | R1/R4/R8, EF-01/02 | Confidential data + local processing + sovereignty are core product constraints.    | Phase 0 EF-01/02; SR-01/SR-02                        | This is the core business proposition.                                | **Critical** | Business | Demonstrate representative confidential workflows entirely within the approved boundary.   | Sovereignty; deployment                  | High       | Exact first customer profile remains open. | **Candidate**        |
| PRD-BR-002 | The product shall support complex knowledge workflows rather than being limited to conversational question answering.                             | R1/R3/R5           | Competitive baseline and research establish multi-step execution as a product need. | Phase 0 Competitive Requirements; EF-01; FM register | Differentiates the product from a local chatbot.                      | **Critical** | Business | Complete representative multi-step workflows from task submission through verified output. | Agentic execution                        | High       | MVP workflow set remains to be validated.  | **Candidate**        |
| PRD-BR-003 | The product shall provide enterprise AI productivity while preserving organizational control, evidence, verification, and auditability.           | R1–R8              | These properties recur across the research decision base.                           | Phase 0 product direction and EF-01–EF-15            | Defines the combined value proposition rather than isolated features. | **Critical** | Business | Evaluate representative workflows against productivity and control criteria.               | UX, execution, verification, sovereignty | High       | Business ROI thresholds remain open.       | **Strong Candidate** |

---

# 3.3 Task Understanding

| ID         | Requirement                                                                                                                                                                 | Source Research | Evidence                                                                            | Source                               | Rationale                                                              | Priority | Type       | Acceptance Concept                                                          | Dependency                           | Confidence | Open Issue                                          | Status               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------- | -------- | ---------- | --------------------------------------------------------------------------- | ------------------------------------ | ---------- | --------------------------------------------------- | -------------------- |
| PRD-TU-001 | The system shall interpret a user's task sufficiently to identify the requested outcome, relevant information, required capabilities, and applicable execution constraints. | R1/R5/R6        | Product execution loop begins with task understanding and risk/capability analysis. | Phase 0 product definition; EF-06/07 | Agent execution cannot safely begin without establishing task context. | High     | Functional | Test task set with expected task objective/capability classification.       | Security context; workflow execution | High       | Exact task taxonomy remains open.                   | **Strong Candidate** |
| PRD-TU-002 | The system shall identify when a task requires evidence from organizational knowledge rather than relying solely on model-generated knowledge.                              | R5/R7           | Evidence-governed retrieval is a core conclusion.                                   | EF-06; DR-05/08                      | Prevents unsupported answers in enterprise workflows.                  | High     | Functional | Tasks requiring enterprise evidence trigger appropriate evidence retrieval. | Knowledge retrieval                  | High       | Exact evidence-triggering rules require validation. | **Strong Candidate** |
| PRD-TU-003 | The system shall identify tasks or steps requiring human approval before consequential action.                                                                              | R5/R8           | High-consequence actions require appropriate human approval.                        | SR-16; EF-07                         | Autonomy must be bounded by consequence.                               | High     | Security   | Submit risk-tiered tasks and verify approval is required where configured.  | Policy; security context             | High       | Exact risk classification remains open.             | **Strong Candidate** |

---

# 3.4 Model / Capability Selection

The requirements deliberately specify **capability selection**, not particular models. Phase 0 explicitly retained the model portfolio and exact model choices as validation-dependent. 

| ID         | Requirement                                                                                                                                               | Source Research | Evidence                                                                                            | Source                                       | Rationale                                                                           | Priority | Type       | Acceptance Concept                                                         | Dependency                   | Confidence  | Open Issue                                          | Status                  |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- | -------- | ---------- | -------------------------------------------------------------------------- | ---------------------------- | ----------- | --------------------------------------------------- | ----------------------- |
| PRD-MC-001 | The system shall support multiple locally hosted AI capabilities appropriate to different task requirements.                                              | R4/R6/R7        | Heterogeneous workloads and resource constraints favor multi-model capability.                      | Phase 0 EF-03/12; CR-01; technology register | Avoids dependence on one universal model.                                           | High     | Functional | Execute heterogeneous workload suite requiring different capabilities.     | Local inference              | High        | Exact model portfolio unresolved.                   | **Strong Candidate**    |
| PRD-MC-002 | The system shall be capable of selecting or escalating capabilities when the current capability is insufficient for the task or verification requirement. | R5/R6/R7        | Phase 0 identifies adaptive routing and verification-driven escalation as strong candidates.        | Phase 0 technology/approach register; FM-17  | Enables quality/resource trade-offs without requiring one maximum-capability model. | High     | Functional | Force difficult cases and verify appropriate escalation or abstention.     | PRD-MC-001; verification     | Medium-High | Exact escalation thresholds require benchmark data. | **Strong Candidate**    |
| PRD-MC-003 | Capability selection shall operate within the deployment's measured computational/resource constraints.                                                   | R4/R5/R7        | GPU OOM and hardware contention are identified failure modes; single-system MVP is a hard boundary. | FM-15; hardware constraints; CR-01           | Capability quality cannot be considered independently of resource feasibility.      | High     | NFR        | Run workload suite while measuring resource envelope and failure behavior. | Hardware/resource management | High        | Exact resource envelope unresolved.                 | **Requires Validation** |

---

# 3.5 Agentic Execution

| ID         | Requirement                                                                                                                                                            | Source Research | Evidence                                                                                             | Source                                              | Rationale                                                           | Priority     | Type       | Acceptance Concept                                                                                   | Dependency                           | Confidence  | Open Issue                                         | Status               |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------- | -------------------------------------------------- | -------------------- |
| PRD-AE-001 | The system shall execute multi-step workflows in which intermediate outputs can inform subsequent steps.                                                               | R1/R3/R5/R6     | Agentic multi-step execution is a hard product constraint.                                           | Phase 0 Known Constraints; Competitive Requirements | Core distinction from simple chat/search.                           | **Critical** | Workflow   | Execute defined multi-step workflows and verify correct state progression.                           | Task understanding; tools; knowledge | High        | Initial workflow set unresolved.                   | **Candidate**        |
| PRD-AE-002 | The system shall maintain execution state sufficiently to identify completed, pending, failed, and partially completed workflow steps.                                 | R5              | Partial completion and interruption are explicit failure modes.                                      | FM-19                                               | Prevents false completion and ambiguous recovery.                   | High         | Functional | Interrupt workflows at different stages and inspect resulting state.                                 | Agent execution                      | High        | Recovery semantics remain to be specified.         | **Strong Candidate** |
| PRD-AE-003 | The system shall bound retries and recovery behavior according to failure classification rather than retrying indefinitely.                                            | R5              | Infinite retry is an identified failure mode.                                                        | FM-10                                               | Prevents resource exhaustion and masks semantic failures.           | High         | Functional | Inject transient, permanent, authorization, and semantic failures and verify bounded behavior.       | Execution state                      | High        | Exact retry policy remains open.                   | **Candidate**        |
| PRD-AE-004 | The system shall determine workflow completion using explicit completion conditions rather than solely relying on an AI-generated completion statement.                | R5              | Phase 0 explicitly rejects LLM “done” as a completion authority.                                     | FM-11                                               | Prevents false completion.                                          | High         | Functional | Construct incomplete workflows where the model claims completion and verify task remains incomplete. | Verification                         | High        | Exact completion predicates are workflow-specific. | **Candidate**        |
| PRD-AE-005 | The system shall support risk-appropriate levels of autonomy, including autonomous reasoning, bounded execution, approval-required execution, and stopping/abstention. | R5/R8           | Phase 0 resolves autonomy/security tension through risk-tiered autonomy.                             | CR-02; SR-16                                        | Provides automation without granting unrestricted authority.        | **Critical** | Security   | Test workflows across defined risk classes and verify corresponding autonomy behavior.               | Policy; security context             | High        | Risk taxonomy requires validation.                 | **Strong Candidate** |
| PRD-AE-006 | Dynamic workflow behavior shall remain constrained by explicitly permitted workflow operations and security policy.                                                    | R6              | Dynamic constrained workflow grammar was preferred over unrestricted autonomous workflow generation. | CR-03; R6 decision base                             | Preserves adaptability while retaining reproducibility and control. | High         | Security   | Attempt prohibited workflow transitions and verify prevention.                                       | Policy; capability controls          | Medium-High | Exact workflow grammar remains open.               | **Strong Candidate** |

---

# 3.6 Tool Execution

| ID         | Requirement                                                                                                                   | Source Research | Evidence                                                                                                     | Source             | Rationale                                            | Priority     | Type       | Acceptance Concept                                                                 | Dependency               | Confidence  | Open Issue                                              | Status               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------ | ------------------ | ---------------------------------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------- | ------------------------ | ----------- | ------------------------------------------------------- | -------------------- |
| PRD-TE-001 | The system shall expose tools to agents only through explicit capability and authorization controls.                          | R5/R8           | Agent authorization must remain outside the LLM.                                                             | EF-07; SR-06/SR-07 | Prevents unrestricted agent authority.               | **Critical** | Security   | Attempt authorized and unauthorized tool calls and verify policy enforcement.      | Security context; policy | High        | Exact policy model unresolved.                          | **Candidate**        |
| PRD-TE-002 | Each tool capability shall have explicitly defined inputs, outputs, permissions, side effects, and execution risk.            | R6/R8           | Phase 0 identifies typed capability/tool contracts as a strong candidate and tool misuse as a major failure. | SR-07; FM-08/FM-09 | Makes tool behavior governable and verifiable.       | High         | Security   | Inspect capability definitions and execute representative tools against contracts. | Tool framework           | Medium-High | Minimum schema remains open.                            | **Strong Candidate** |
| PRD-TE-003 | Tool results shall be independently validated when their semantic correctness materially affects downstream execution.        | R5              | Syntactically valid but semantically incorrect tool outputs are a known failure.                             | FM-09              | Prevents downstream propagation of tool errors.      | High         | Functional | Inject plausible but incorrect tool results and verify detection/escalation.       | Verification             | High        | Which tools require verification is workflow-dependent. | **Strong Candidate** |
| PRD-TE-004 | Consequential external side effects shall require explicit authorization consistent with the applicable security/risk policy. | R5/R8           | High-consequence actions require approval and authorization external to model reasoning.                     | SR-06/SR-16        | Separates reasoning authority from action authority. | **Critical** | Security   | Attempt consequential action without authorization and verify denial.              | Policy; identity         | High        | Exact consequential-action taxonomy remains open.       | **Candidate**        |

---

# 3.7 Knowledge Retrieval

| ID         | Requirement                                                                                                                                                                                                                                      | Source Research | Evidence                                                               | Source              | Rationale                                                                     | Priority     | Type       | Acceptance Concept                                                                                     | Dependency               | Confidence | Open Issue                                             | Status               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ---------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------ | ---------- | ------------------------------------------------------ | -------------------- |
| PRD-KR-001 | The system shall retrieve enterprise information using relevance together with applicable authority, revision, authorization, and temporal constraints.                                                                                          | R5/R7           | Relevance alone cannot establish current or authoritative information. | EF-04; DR-03/04     | Prevents stale or unauthorized knowledge from being treated as truth.         | **Critical** | Data       | Create current/stale/unauthorized/conflicting corpus cases and verify retrieval behavior.              | Metadata; access control | High       | Customer authority hierarchy remains open.             | **Candidate**        |
| PRD-KR-002 | The system shall distinguish authoritative, current, superseded, conflicting, and unverifiable knowledge states.                                                                                                                                 | R5/R7           | Explicit evidence-state model established.                             | EF-04/05; DR-07     | Enables safe reasoning over enterprise history.                               | High         | Data       | Query corpus containing different knowledge states and verify classification.                          | Metadata/versioning      | High       | Exact state transition governance requires validation. | **Candidate**        |
| PRD-KR-003 | The system shall detect when available evidence is insufficient for a requested conclusion.                                                                                                                                                      | R5/R6/R7        | Evidence sufficiency is a preferred requirement.                       | EF-06; DR-08        | Prevents unsupported conclusions.                                             | **Critical** | Functional | Provide incomplete evidence and verify insufficient-evidence outcome.                                  | Evidence layer           | High       | Exact sufficiency predicates remain workflow-specific. | **Candidate**        |
| PRD-KR-004 | When evidence is insufficient, conflicted, stale, unauthorized, or unverifiable, the system shall take an appropriate safe response such as retrieving more evidence, abstaining, escalating, requesting approval, asking the user, or stopping. | R5/R7/R8        | These behaviors are explicitly established in Phase 0.                 | EF-06; FM-06; SR-16 | Converts evidence uncertainty into controlled product behavior.               | **Critical** | Functional | Inject each evidence failure state and verify appropriate response.                                    | PRD-KR-003; policy       | High       | Exact response mapping requires workflow validation.   | **Strong Candidate** |
| PRD-KR-005 | The system shall support retrieval units appropriate to the structure and semantics of the source information rather than imposing a single universal retrieval unit.                                                                            | R7              | Universal fixed-size chunking was rejected.                            | DR-09; RA-05        | Different enterprise information types require different evidence boundaries. | High         | Data       | Evaluate retrieval on tables, sections, figures, P&ID structures, code and other representative units. | Document representation  | High       | Exact retrieval-unit taxonomy remains open.            | **Strong Candidate** |
| PRD-KR-006 | Important generated claims shall retain links to the evidence used to support them.                                                                                                                                                              | R6/R7           | Claim/evidence provenance is a core research conclusion.               | EF-11; DR-05        | Enables traceability and user inspection.                                     | High         | Data       | Select generated claims and trace them to source evidence.                                             | Provenance               | High       | Exact UI presentation remains open.                    | **Candidate**        |

---

# 3.8 Document Intelligence

| ID         | Requirement                                                                                                                                                                                               | Source Research | Evidence                                                                                     | Source             | Rationale                                                                     | Priority     | Type       | Acceptance Concept                                                 | Dependency                | Confidence | Open Issue                                     | Status               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------ | ------------------------- | ---------- | ---------------------------------------------- | -------------------- |
| PRD-DI-001 | The system shall ingest and process enterprise documents including PDF, DOCX, XLSX, PPTX, scanned documents, images, engineering drawings, P&IDs, and code where required by supported workflows.         | R1/R4/R7        | These are explicitly identified target information classes.                                  | DR-01; EF-01/03    | Defines the minimum heterogeneous information surface.                        | **Critical** | Functional | Ingest representative files from each required class.              | Document processing       | High       | Email-like content remains workflow-dependent. | **Candidate**        |
| PRD-DI-002 | The system shall preserve document structure needed for downstream retrieval and reasoning, including sections, tables, figures, page references, coordinates, reading order, and relevant relationships. | R7              | Structural preservation is explicitly required.                                              | DR-02              | Text extraction alone is insufficient for technical documents.                | High         | Data       | Compare source documents with preserved structural representation. | Ingestion                 | High       | Exact representation depends on source type.   | **Candidate**        |
| PRD-DI-003 | The system shall preserve source-region information for important extracted values and interpretations.                                                                                                   | R5/R7           | OCR corruption and provenance loss require source-region provenance.                         | FM-05/FM-18; DR-05 | Enables verification against original evidence.                               | High         | Data       | Trace extracted values to document/page/region evidence.           | Structural preservation   | High       | Exact granularity remains open.                | **Strong Candidate** |
| PRD-DI-004 | The system shall identify and expose extraction uncertainty where document quality or processing ambiguity affects downstream use.                                                                        | R5              | OCR corruption and structurally valid but semantically incorrect parsing are known failures. | FM-05; R5          | Prevents extracted content from being treated as unquestionable source truth. | High         | Functional | Test degraded scans/layouts and verify uncertainty is surfaced.    | Extraction QA; provenance | High       | Exact uncertainty representation remains open. | **Strong Candidate** |

---

# 3.9 Multimodal Processing

| ID         | Requirement                                                                                                                                    | Source Research | Evidence                                                                                                       | Source          | Rationale                                                                   | Priority     | Type       | Acceptance Concept                                                                          | Dependency              | Confidence | Open Issue                                             | Status               |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------- | ----------------------- | ---------- | ------------------------------------------------------ | -------------------- |
| PRD-MM-001 | The system shall support reasoning over textual, visual, scanned, tabular, and structurally represented information when required by the task. | R1/R4/R7        | Text-only RAG cannot adequately represent target engineering information.                                      | EF-03           | Multimodality is a core product requirement.                                | **Critical** | Functional | Execute representative multimodal workflows.                                                | Document intelligence   | High       | Exact modality coverage per MVP workflow remains open. | **Candidate**        |
| PRD-MM-002 | For engineering drawings and P&IDs, the system shall preserve both visual evidence and relevant structural/engineering relationships.          | R5/R7           | Image-only P&ID reasoning was rejected; image + OCR/layout + engineering graph is the resolved representation. | EF-03; RA-03/04 | Engineering meaning cannot be reliably derived from image or OCR alone.     | **Critical** | Data       | Evaluate topology/relationship questions against representative P&IDs.                      | Engineering information | High       | Exact minimum graph scope remains open.                | **Strong Candidate** |
| PRD-MM-003 | Visual or extracted interpretations of engineering information shall not automatically be treated as consequential engineering authority.      | R7/R8           | Human engineer remains consequential authority in the resolved P&ID representation.                            | EF-03           | Prevents model interpretation from becoming uncontrolled engineering truth. | High         | Security   | Test consequential engineering decisions and verify required validation/authority boundary. | Verification; approval  | High       | Exact approval model depends on workflow.              | **Candidate**        |

---

# 3.10 Engineering Information

| ID         | Requirement                                                                                                                                | Source Research | Evidence                                                               | Source                              | Rationale                                                                   | Priority | Type       | Acceptance Concept                                                                     | Dependency             | Confidence | Open Issue                                       | Status               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ---------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------------- | ---------------------- | ---------- | ------------------------------------------------ | -------------------- |
| PRD-EI-001 | The system shall represent relevant engineering entities and relationships sufficiently to support supported engineering workflows.        | R7              | P&IDs require structural engineering representation.                   | EF-03; R7 P&ID resolution           | Enables topology and relationship reasoning.                                | High     | Functional | Run defined P&ID relationship queries and compare against validated reference answers. | Multimodal processing  | High       | Exact domain ontology must remain minimum-scope. | **Strong Candidate** |
| PRD-EI-002 | Engineering evidence shall retain source document, revision, page/region, and confidence or extraction context for relevant relationships. | R5/R7           | Relationship provenance is part of the minimum P&ID graph requirement. | R7 P&ID representation; FM-04/FM-18 | Allows engineering users to inspect the basis of interpreted relationships. | High     | Data       | Trace selected engineering relationships back to source evidence.                      | PRD-EI-001; provenance | High       | Exact confidence representation remains open.    | **Strong Candidate** |
| PRD-EI-003 | The product shall not require a complete enterprise digital twin or universal enterprise ontology as a prerequisite for MVP workflows.     | R7              | Both approaches were explicitly rejected for MVP.                      | RA-17/18; CR-04                     | Protects scope and keeps the MVP focused on validated workflows.            | Medium   | Business   | Verify MVP scope does not depend on complete digital-twin coverage.                    | Scope definition       | High       | Future expansion remains possible.               | **Candidate**        |

---

# 3.11 Code Generation & Execution

| ID         | Requirement                                                                                                                                               | Source Research | Evidence                                                                     | Source                         | Rationale                                                               | Priority     | Type         | Acceptance Concept                                                                               | Dependency        | Confidence | Open Issue                                              | Status               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------- | ------------ | ------------ | ------------------------------------------------------------------------------------------------ | ----------------- | ---------- | ------------------------------------------------------- | -------------------- |
| PRD-CE-001 | The system shall support generation of executable code where required by supported workflows.                                                             | R4/R5/R7        | Code generation is part of the intended artifact/tool workflow.              | Phase 0 product capability set | Enables calculations, transformations and technical automation.         | High         | Functional   | Execute supported code-generation workflows.                                                     | Agent execution   | High       | Exact languages/workflows remain open.                  | **Candidate**        |
| PRD-CE-002 | Generated code shall execute only within an isolated execution environment with controlled resources, filesystem access, credentials, and network access. | R4/R5/R8        | Generated code is untrusted; Docker alone was rejected.                      | EF-09; SR-09/SR-10; FM-12/13   | Limits blast radius of malicious or defective code.                     | **Critical** | Security     | Execute adversarial and resource-intensive code and verify isolation boundaries.                 | Security controls | High       | Exact isolation mechanism remains validation-dependent. | **Candidate**        |
| PRD-CE-003 | Code execution shall produce an execution record sufficient to identify the code/action, environment, outcome, and relevant verification result.          | R5/R6/R8        | Execution records and proof-carrying action concepts support accountability. | EF-11; SR-11; FM-12/13         | Makes generated-code execution auditable.                               | High         | Auditability | Inspect execution record after representative code runs.                                         | Provenance/audit  | High       | Exact record schema remains open.                       | **Strong Candidate** |
| PRD-CE-004 | Generated code and its outputs shall undergo validation appropriate to the consequence of the workflow before being accepted as a successful result.      | R5              | Code and artifacts can be syntactically valid but semantically wrong.        | FM-09/FM-16/FM-17; EF-10       | Prevents executable but incorrect output from being treated as correct. | High         | Evaluation   | Introduce intentionally incorrect but executable code/output and verify rejection or escalation. | Verification      | High       | Exact verifier classes remain workflow-dependent.       | **Candidate**        |

---

# 3.12 Artifact Generation

| ID         | Requirement                                                                                           | Source Research | Evidence                                                                     | Source                                              | Rationale                                                          | Priority     | Type       | Acceptance Concept                                                   | Dependency                    | Confidence | Open Issue                                              | Status                  |
| ---------- | ----------------------------------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------ | ------------ | ---------- | -------------------------------------------------------------------- | ----------------------------- | ---------- | ------------------------------------------------------- | ----------------------- |
| PRD-AG-001 | The system shall generate usable enterprise artifacts in the formats required by supported workflows. | R1/R3/R4        | Artifact generation is an explicit hard capability and competitive baseline. | Phase 0 Known Constraints; Competitive Requirements | Converts analysis into usable business output.                     | **Critical** | Functional | Generate artifacts for each selected MVP workflow.                   | Agent execution; verification | High       | Exact MVP artifact classes require workflow validation. | **Candidate**           |
| PRD-AG-002 | Generated artifacts shall be structurally valid for their intended file format.                       | R5              | Artifact corruption is an explicit failure mode.                             | FM-16; V6                                           | Prevents unusable files.                                           | High         | NFR        | Automated structural validation of representative outputs.           | Artifact engine               | High       | Exact validation rules per format remain open.          | **Candidate**           |
| PRD-AG-003 | Generated artifacts shall preserve required evidence/provenance for consequential claims or outputs.  | R6/R7           | Important artifacts must retain provenance.                                  | EF-11; SR-12                                        | Keeps the artifact connected to its evidence basis.                | High         | Data       | Trace selected artifact content to evidence.                         | Provenance; verification      | High       | Exact artifact provenance UX remains open.              | **Strong Candidate**    |
| PRD-AG-004 | Artifact acceptance shall evaluate both structural correctness and human usefulness.                  | R5/R7           | Phase 0 identifies artifact quality as an unvalidated high-risk assumption.  | EG-06; FM-16                                        | A structurally valid artifact may still be operationally unusable. | High         | Evaluation | Human + automated acceptance assessment on representative artifacts. | PRD-AG-002                    | High       | Quality thresholds require validation.                  | **Requires Validation** |

---

# 3.13 Verification

| ID         | Requirement                                                                                                                         | Source Research | Evidence                                                                       | Source                   | Rationale                                 | Priority     | Type       | Acceptance Concept                                                                   | Dependency                     | Confidence | Open Issue                                                 | Status               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------ | ------------------------ | ----------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------ | ---------- | ---------------------------------------------------------- | -------------------- |
| PRD-VR-001 | Important task outputs shall undergo verification before being represented as successfully completed.                               | R5/R6           | Generation does not equal correctness.                                         | EF-10; FM-01/FM-16/FM-17 | Core trust requirement.                   | **Critical** | Functional | Compare system behavior with and without injected output errors.                     | Verification mechanisms        | High       | Exact definition of "important" remains workflow-specific. | **Candidate**        |
| PRD-VR-002 | Verification shall use more than one verification mode where the consequence or failure risk warrants it.                           | R5/R6           | Layered deterministic, semantic/model, and human verification was established. | EF-10                    | Reduces correlated verifier failure.      | High         | Evaluation | Inject failures detectable by different verification layers.                         | PRD-VR-001                     | High       | Exact layer combinations require validation.               | **Strong Candidate** |
| PRD-VR-003 | The system shall support abstention, escalation, or human review when verification cannot establish acceptable correctness.         | R5/R7           | Insufficient evidence and verifier failure require safe non-success outcomes.  | EF-06/10; FM-17          | Prevents forced answers.                  | **Critical** | Functional | Provide unverifiable/ambiguous outputs and verify safe escalation.                   | Evidence sufficiency; approval | High       | Exact escalation criteria remain open.                     | **Candidate**        |
| PRD-VR-004 | Completion and verification status shall be derived from observable checks or predicates rather than an unverified model assertion. | R5              | False completion is explicit failure.                                          | FM-11                    | Makes completion objectively inspectable. | High         | Evaluation | Contradict model's completion claim with failed predicate and verify non-completion. | Workflow state                 | High       | Workflow-specific predicates remain open.                  | **Candidate**        |

---

# 3.14 Security

| ID          | Requirement                                                                                                                   | Source Research | Evidence                                                       | Source                      | Rationale                                          | Priority     | Type     | Acceptance Concept                                                                | Dependency                | Confidence | Open Issue                                           | Status               |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------------------------- | ------------ | -------- | --------------------------------------------------------------------------------- | ------------------------- | ---------- | ---------------------------------------------------- | -------------------- |
| PRD-SEC-001 | Authorization for agents, tools, data, and consequential actions shall be enforced independently of model reasoning.          | R5/R8           | Authorization external to LLM is a core security conclusion.   | EF-07; SR-06                | Prevents the model from granting itself authority. | **Critical** | Security | Attempt policy-violating actions generated by the model and verify denial.        | Identity/security context | High       | Exact policy mechanism remains open.                 | **Candidate**        |
| PRD-SEC-002 | Untrusted enterprise content shall not be able to alter authorization, security policy, or other control-plane decisions.     | R5/R8           | Prompt injection can originate in enterprise documents.        | EF-08; SR-08                | Air-gap does not prevent data-plane attacks.       | **Critical** | Security | Adversarial documents attempt to modify policy/tool behavior; verify containment. | Security context; policy  | High       | Adversarial thresholds require R11-style validation. | **Candidate**        |
| PRD-SEC-003 | The system shall enforce least-privilege access to enterprise data and tools.                                                 | R5/R8           | Unauthorized retrieval/tool misuse are explicit failure modes. | FM-03/FM-08; SR-06/07       | Limits confidentiality and integrity impact.       | **Critical** | Security | Test users/agents with different authorization scopes.                            | Identity; ACL             | High       | Customer role models remain open.                    | **Candidate**        |
| PRD-SEC-004 | Secrets and credentials shall not be exposed to untrusted generated code or model reasoning beyond explicitly authorized use. | R5/R8           | Secrets isolation is a hard security constraint.               | SR-10; security constraints | Prevents credential-based compromise/exfiltration. | **Critical** | Security | Attempt credential discovery/access from generated code and tools.                | Sandbox; policy           | High       | Secret classes/customer mechanism remain open.       | **Candidate**        |
| PRD-SEC-005 | Security-relevant actions and policy decisions shall be auditable.                                                            | R5/R8           | Auditability is a hard requirement.                            | SR-11; FM-08                | Enables investigation and governance.              | High         | Security | Verify auditable records for representative security-relevant actions.            | Auditability              | High       | Exact retention/export requirements remain open.     | **Candidate**        |
| PRD-SEC-006 | The system shall detect or safely handle malicious inputs including malicious documents and adversarial task content.         | R5/R8           | Malicious documents and prompt injection are explicit threats. | EF-08; FM-07                | Internal data cannot automatically be trusted.     | High         | Security | Execute defined malicious-input suite and assess containment.                     | Control/data separation   | High       | Full adversarial suite is future validation.         | **Strong Candidate** |

---

# 3.15 Data Sovereignty

| ID          | Requirement                                                                                                                                                              | Source Research | Evidence                                                                                             | Source          | Rationale                                                                   | Priority     | Type        | Acceptance Concept                                                                                      | Dependency                 | Confidence | Open Issue                                                      | Status               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ---------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------- | -------------------------- | ---------- | --------------------------------------------------------------- | -------------------- |
| PRD-SOV-001 | Core product functionality shall operate without requiring external AI APIs.                                                                                             | R4/R8           | Explicit hard sovereignty constraint.                                                                | SR-01           | Defines local AI independence.                                              | **Critical** | Sovereignty | Disconnect external AI services and execute core workflow suite.                                        | Local models               | High       | None for core requirement.                                      | **Candidate**        |
| PRD-SOV-002 | Confidential task data, processing, intermediate data, and generated outputs shall remain within the defined deployment boundary unless explicitly authorized by policy. | R4/R8           | Data boundary is a hard constraint.                                                                  | SR-02           | Defines what sovereignty protects.                                          | **Critical** | Sovereignty | Track representative data through complete workflows and verify boundary adherence.                     | Network/data controls      | High       | Exact customer boundary definition remains deployment-specific. | **Candidate**        |
| PRD-SOV-003 | Sovereign deployments shall deny external network communication by default.                                                                                              | R8              | External communication denial is established.                                                        | SR-03           | Reduces egress/exfiltration paths.                                          | **Critical** | Sovereignty | Attempt outbound connections through application, tools, generated code, DNS and other supported paths. | Network enforcement        | High       | Customer-approved exceptions remain open.                       | **Candidate**        |
| PRD-SOV-004 | Network isolation shall be enforced independently of application-level AI logic.                                                                                         | R8              | Application assertion alone is insufficient.                                                         | SR-04           | Prevents compromised software from bypassing the sovereignty boundary.      | **Critical** | Security    | Attempt egress from multiple execution surfaces and verify independent enforcement.                     | Deployment controls        | High       | Exact deployment enforcement mechanism is architectural.        | **Candidate**        |
| PRD-SOV-005 | The product shall provide evidence that supports verification of its actual network behavior and sovereignty posture.                                                    | R5/R8           | “Observed no traffic” alone was rejected; evidence must combine enforcement and observation/testing. | SR-05; RA-16    | Sovereignty must be technically demonstrable.                               | **Critical** | Sovereignty | Generate sovereignty evidence during controlled adversarial testing.                                    | Network enforcement; audit | High       | Exact evidence accepted by customers remains open.              | **Strong Candidate** |
| PRD-SOV-006 | Offline deployments shall support controlled management of approved models and software artifacts without requiring unrestricted online access.                          | R8              | Supply-chain/update sovereignty is a hard concern.                                                   | EF-14; SR-13/14 | Offline operation cannot imply uncontrolled or permanently frozen software. | High         | Deployment  | Install/update using controlled offline artifacts and verify integrity.                                 | Supply-chain controls      | High       | Exact update process requires customer validation.              | **Strong Candidate** |
| PRD-SOV-007 | Models and software dependencies deployed in security-sensitive environments shall have identifiable versions and integrity information.                                 | R8              | SBOM/AIBOM/VEX and integrity controls identified.                                                    | EF-14; SR-13/14 | Sovereignty includes software/model supply chain.                           | High         | Security    | Inspect deployment manifest and verify artifact identity/integrity.                                     | Release management         | High       | Exact assurance level remains deployment-specific.              | **Strong Candidate** |

---

# 3.16 Auditability & Provenance

| ID         | Requirement                                                                                                                                     | Source Research | Evidence                                                                          | Source           | Rationale                                                         | Priority     | Type         | Acceptance Concept                                                                    | Dependency                    | Confidence  | Open Issue                                          | Status               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------- | ------------ | ------------ | ------------------------------------------------------------------------------------- | ----------------------------- | ----------- | --------------------------------------------------- | -------------------- |
| PRD-AP-001 | Important outputs shall retain provenance linking claims or artifacts to their supporting evidence.                                             | R6/R7           | Source → evidence → claim → decision → artifact provenance is established.        | EF-11; DR-05     | Enables verification and trust.                                   | **Critical** | Data         | Select output claims and reconstruct evidence lineage.                                | Evidence layer                | High        | Exact provenance graph representation remains open. | **Candidate**        |
| PRD-AP-002 | Significant task executions shall retain records of relevant actions, inputs, authorization context, outcomes, and verification results.        | R5/R6/R8        | Execution auditability and proof-carrying action envelope are supported concepts. | SR-11; FM-08; R6 | Supports investigation and accountability.                        | High         | Auditability | Inspect execution record after representative workflows.                              | Security context              | High        | Exact retention policy unresolved.                  | **Strong Candidate** |
| PRD-AP-003 | Provenance and audit records shall distinguish source evidence from AI-derived knowledge and conclusions.                                       | R7              | AI-derived knowledge cannot automatically become authoritative.                   | EF-05; DR-07     | Prevents derived knowledge from masquerading as source truth.     | High         | Data         | Inspect lineage of source, derived evidence and generated conclusion.                 | Knowledge states              | High        | Exact UI semantics remain open.                     | **Candidate**        |
| PRD-AP-004 | The system shall preserve sufficient execution/environment identity to support investigation of configuration drift and reproducibility issues. | R5              | Configuration drift and environment fingerprinting are explicit concerns.         | FM-20            | Helps determine whether a result remains qualified after changes. | Medium       | Auditability | Change controlled environment versions and verify execution records distinguish them. | Deployment/version management | Medium-High | Exact environment fingerprint scope remains open.   | **Strong Candidate** |

---

# 3.17 Data & Knowledge

| ID         | Requirement                                                                                                                                                                            | Source Research | Evidence                                                                                               | Source                                  | Rationale                                                                | Priority     | Type       | Acceptance Concept                                                      | Dependency               | Confidence | Open Issue                                                   | Status               |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------ | ------------ | ---------- | ----------------------------------------------------------------------- | ------------------------ | ---------- | ------------------------------------------------------------ | -------------------- |
| PRD-DK-001 | Source artifacts shall remain identifiable as the evidentiary roots from which derived representations and knowledge are produced.                                                     | R7              | Three-tier data strategy makes source artifacts immutable evidence roots.                              | DR requirements; EF-05/11               | Prevents derived representations from replacing source evidence.         | **Critical** | Data       | Reconstruct derived data back to source artifact.                       | Ingestion/provenance     | High       | Exact immutability mechanism is implementation-level.        | **Candidate**        |
| PRD-DK-002 | Enterprise information shall preserve ownership, authority, classification, ACL, revision, effective date, and source-system metadata where available and relevant.                    | R7/R8           | Required metadata is explicitly established.                                                           | DR-03; EF-04                            | Enables authority, access, temporal, and security-aware reasoning.       | **Critical** | Data       | Ingest documents with metadata and verify preservation/use.             | Ingestion; authorization | High       | Exact customer metadata availability requires validation.    | **Candidate**        |
| PRD-DK-003 | The system shall support temporal knowledge including revisions, supersession, effective time, and historical information where relevant to workflows.                                 | R5/R7           | Temporal validity is a core requirement.                                                               | EF-04; DR-04                            | Prevents historical information from being presented as current.         | High         | Data       | Test revision histories and effective dates.                            | Metadata                 | High       | Customer temporal semantics vary.                            | **Candidate**        |
| PRD-DK-004 | Derived knowledge shall have explicit lifecycle states distinguishing candidate, validated, approved, superseded, conflicted, unverifiable, and rejected information where applicable. | R7              | Explicit knowledge-state model established.                                                            | EF-05; DR-07                            | Prevents AI-derived information from silently becoming authoritative.    | High         | Data       | Transition sample knowledge through defined states and verify behavior. | Provenance; governance   | High       | Exact transition authority remains open.                     | **Candidate**        |
| PRD-DK-005 | The system shall support access-controlled retrieval of enterprise knowledge consistent with the requesting user's authorization.                                                      | R5/R7/R8        | Unauthorized retrieval is a critical failure.                                                          | FM-03; DR-03; SR-06                     | Confidentiality requires retrieval-level authorization.                  | **Critical** | Data       | Cross-user ACL test across identical queries.                           | Identity; authorization  | High       | Exact ACL integration remains open.                          | **Candidate**        |
| PRD-DK-006 | The system shall preserve multiple forms of evidence when required by the source, including textual, visual, tabular, structural, and relationship evidence.                           | R7              | Multiple retrieval surfaces and structured representations are required.                               | DR-02/06/09; EF-03                      | Prevents loss of critical information during ingestion/retrieval.        | High         | Data       | Compare multimodal/structural workflow results with source corpus.      | Document intelligence    | High       | Exact evidence representation varies by workflow.            | **Strong Candidate** |
| PRD-DK-007 | Production qualification shall support evaluation against customer-owned representative data.                                                                                          | R7              | Public/synthetic data cannot represent customer terminology, revisions, ACLs, conventions and history. | EF-13; DR-10; EG-05                     | Customer-specific qualification is mandatory for production credibility. | **Critical** | Evaluation | Run frozen benchmark against approved customer corpus.                  | Customer onboarding      | High       | Customer data availability remains an assumption.            | **Candidate**        |
| PRD-DK-008 | Evaluation data and derived representations used for qualification shall be identifiable by version/fingerprint sufficient to reproduce the qualification context.                     | R7              | Frozen/fingerprinted evaluation corpus is mandatory.                                                   | R7 EF-13 / evaluation corpus conclusion | Prevents benchmark drift and invalid comparisons.                        | High         | Evaluation | Modify corpus/version and verify qualification identity changes.        | Version management       | High       | Exact fingerprint schema remains implementation-independent. | **Candidate**        |

---

# 3.18 Evaluation

| ID         | Requirement                                                                                                                                                                                              | Source Research | Evidence                                                                   | Source                      | Rationale                                                    | Priority     | Type       | Acceptance Concept                                                 | Dependency             | Confidence | Open Issue                                          | Status               |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------ | ------------ | ---------- | ------------------------------------------------------------------ | ---------------------- | ---------- | --------------------------------------------------- | -------------------- |
| PRD-EV-001 | The product shall support objective evaluation of representative end-to-end workflows rather than relying solely on isolated model benchmarks.                                                           | R5/R7           | Phase 0 identifies end-to-end reliability as a critical gap.               | EG-03; V4                   | Product success depends on workflow outcomes.                | **Critical** | Evaluation | Frozen end-to-end benchmark with repeated trials.                  | Workflow definitions   | High       | Exact metrics remain to be finalized.               | **Candidate**        |
| PRD-EV-002 | Evaluation shall measure task completion, step correctness, tool-call correctness, evidence sufficiency, verification success, abstention, recovery, latency, and resource consumption where applicable. | R5              | These measures are explicitly listed for V4.                               | Phase 0 V4                  | Captures system behavior rather than model quality alone.    | High         | Evaluation | Execute benchmark and record all applicable metrics.               | Instrumentation        | High       | Thresholds remain open.                             | **Strong Candidate** |
| PRD-EV-003 | Evaluation shall include difficult and representative cases rather than being based only on corpus size.                                                                                                 | R7              | Heterogeneity and difficult cases matter more than raw volume.             | EF-12; V2                   | Prevents inflated qualification from easy homogeneous data.  | High         | Evaluation | Evaluate heterogeneous/difficult corpus against workflow coverage. | Customer corpus        | High       | Exact corpus composition requires validation.       | **Candidate**        |
| PRD-EV-004 | Evaluation shall explicitly measure unsafe or unacceptable failure modes in addition to successful-task performance.                                                                                     | R5/R8           | Wrong-but-plausible output and security failures are critical.             | FM register; V5             | High success rate alone can hide dangerous failure behavior. | **Critical** | Evaluation | Run failure/adversarial suite and classify outcomes.               | Security; verification | High       | R11 adversarial research remains future validation. | **Strong Candidate** |
| PRD-EV-005 | Qualification shall record the environment and relevant model/software/data versions used to produce the evaluation result.                                                                              | R5/R7           | Configuration drift and frozen evaluation corpus are established concerns. | FM-20; R7 evaluation corpus | Prevents qualification claims from becoming context-free.    | High         | Evaluation | Re-run qualification after controlled version change.              | Provenance/versioning  | High       | Exact version manifest remains open.                | **Candidate**        |

---

# 3.19 Hardware & Resource Management

| ID         | Requirement                                                                                                                                                 | Source Research          | Evidence                                                                                                                  | Source                       | Rationale                                                           | Priority     | Type       | Acceptance Concept                                                         | Dependency            | Confidence | Open Issue                         | Status                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------- | ------------ | ---------- | -------------------------------------------------------------------------- | --------------------- | ---------- | ---------------------------------- | ----------------------- |
| PRD-HR-001 | The MVP shall operate on a single workstation/server within the project's defined hardware boundary.                                                        | Project constraints / R4 | Single-workstation/server demonstration is a hard MVP boundary.                                                           | Phase 0 Hardware Constraints | Prevents MVP scope from depending on distributed infrastructure.    | **Critical** | Deployment | Demonstrate complete selected MVP workflows on one reference system.       | All core capabilities | High       | Reference hardware not yet frozen. | **Candidate**           |
| PRD-HR-002 | The system shall monitor and manage computational resource consumption sufficiently to prevent uncontrolled resource exhaustion during supported workflows. | R4/R5/R7                 | GPU OOM and resource contention are known failures.                                                                       | FM-15; EG-02                 | Resource failure can invalidate otherwise correct product behavior. | High         | NFR        | Stress workload and verify controlled behavior before resource exhaustion. | Runtime telemetry     | High       | Exact safety margins unresolved.   | **Strong Candidate**    |
| PRD-HR-003 | The product shall define measurable resource/performance envelopes for qualified workloads.                                                                 | R5/R7                    | Hardware validation requires VRAM, RAM, CPU, storage, latency, throughput, concurrency, KV pressure and failure behavior. | V3                           | Makes the hardware constraint objectively testable.                 | **Critical** | Evaluation | Produce benchmark envelope for each priority workflow.                     | Hardware benchmark    | High       | Exact thresholds require V3.       | **Requires Validation** |
| PRD-HR-004 | Resource constraints shall not cause the system to falsely report successful completion.                                                                    | R5                       | Resource exhaustion can cause partial completion and false completion.                                                    | FM-15/FM-19                  | Resource failure must surface as a controlled state.                | High         | NFR        | Force resource exhaustion and verify incomplete/failed state is exposed.   | Execution state       | High       | Recovery strategy remains open.    | **Strong Candidate**    |

---

# 3.20 Deployment & Operations

| ID         | Requirement                                                                                                                                                     | Source Research | Evidence                                                                                | Source                                  | Rationale                                                                           | Priority     | Type       | Acceptance Concept                                                                       | Dependency                        | Confidence  | Open Issue                                      | Status               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------- | --------------------------------- | ----------- | ----------------------------------------------- | -------------------- |
| PRD-DO-001 | The product shall support controlled/offline deployment consistent with the customer's defined sovereignty boundary.                                            | R4/R8           | Offline/local deployment is a hard constraint.                                          | SR-01–SR-05                             | Core deployment model.                                                              | **Critical** | Deployment | Deploy and operate representative workflow without external AI/service dependency.       | Sovereignty                       | High        | Exact deployment profile remains open.          | **Candidate**        |
| PRD-DO-002 | Security-sensitive software and model updates shall be deployable through a controlled offline process with integrity verification.                             | R8              | Offline supply-chain management is a core sovereignty requirement.                      | EF-14; SR-13/14                         | Allows maintenance without compromising sovereignty.                                | High         | Deployment | Install approved update bundle and verify integrity/version identity.                    | Supply-chain controls             | High        | Exact customer approval process open.           | **Strong Candidate** |
| PRD-DO-003 | The product shall support deployment/security profiles that bound capabilities according to the customer's operational and security environment.                | R8              | Generic product + sector-specific compliance is resolved toward common core + profiles. | CR-07                                   | Avoids hard-coding one regulatory environment while preserving security boundaries. | High         | Deployment | Deploy at least two differentiated policy profiles and verify behavior differences.      | Policy engine                     | Medium-High | First commercial profile remains open.          | **Strong Candidate** |
| PRD-DO-004 | OT/ICS interaction shall be explicitly bounded by deployment policy and shall not provide unrestricted autonomous manipulation of process-control state in MVP. | R8              | Full autonomous OT control is explicitly rejected.                                      | EF-15; SR-15; RA-16 equivalent decision | Limits consequence in CII/OT environments.                                          | **Critical** | Security   | Attempt prohibited OT action and verify policy denial.                                   | Deployment profile; authorization | High        | Exact OT boundary depends on customer.          | **Candidate**        |
| PRD-DO-005 | The product shall support operational requalification when relevant models, software, dependencies, data representations, or configurations change.             | R5/R8           | Configuration drift can invalidate qualification.                                       | FM-20; SR-14                            | Maintains validity of previous assurance claims.                                    | High         | Deployment | Change qualified component and verify requalification requirement is triggered/recorded. | Version/provenance                | Medium-High | Trigger policy requires operational validation. | **Strong Candidate** |

---

# 3.21 Administration & Governance

| ID          | Requirement                                                                                                                                  | Source Research | Evidence                                                        | Source             | Rationale                                           | Priority     | Type         | Acceptance Concept                                                 | Dependency         | Confidence | Open Issue                                         | Status               |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------- | ------------------ | --------------------------------------------------- | ------------ | ------------ | ------------------------------------------------------------------ | ------------------ | ---------- | -------------------------------------------------- | -------------------- |
| PRD-GOV-001 | Administrators shall be able to define or enforce authorization boundaries for users, data, tools, and consequential actions.                | R5/R8           | External authorization is a core security principle.            | SR-06/07/16        | Security cannot depend on model behavior.           | **Critical** | Security     | Configure policy and verify authorized/unauthorized cases.         | Identity/policy    | High       | Exact administrative UX remains open.              | **Candidate**        |
| PRD-GOV-002 | Administrators shall be able to identify the versions and integrity state of deployed models and relevant software components.               | R8              | Supply-chain controls require identifiable versions/integrity.  | SR-13/14           | Supports controlled deployment and requalification. | High         | Deployment   | Inspect deployed component inventory and integrity status.         | Release management | High       | Exact inventory scope remains open.                | **Strong Candidate** |
| PRD-GOV-003 | The system shall expose sufficient audit information for authorized administrators to investigate significant execution and security events. | R5/R8           | Auditability is a hard requirement.                             | SR-11; FM register | Supports governance and incident investigation.     | High         | Auditability | Reconstruct predefined test incidents from audit records.          | PRD-AP-002         | High       | Retention/export requirements remain open.         | **Candidate**        |
| PRD-GOV-004 | The product shall distinguish customer-owned authoritative knowledge from AI-derived knowledge and preserve the applicable governance state. | R7              | AI-derived knowledge cannot automatically become authoritative. | EF-05; DR-07       | Protects organizational knowledge integrity.        | High         | Data         | Test ingestion, derivation, validation and supersession lifecycle. | Knowledge state    | High       | Governance ownership requires customer validation. | **Candidate**        |

---

# 4. Requirements deliberately **not** frozen

Phase 0 contains several technically interesting candidates. They are **not converted into implementation requirements** at this stage.

| Item                                                | Current treatment          | Reason                                   |
| --------------------------------------------------- | -------------------------- | ---------------------------------------- |
| Specific model family                               | Open / Requires Validation | Quality/resource benchmark incomplete    |
| Specific model-serving engine                       | Open                       | Architecture/technology decision         |
| Specific retrieval engine                           | Open                       | Architecture/technology decision         |
| Specific document-processing framework              | Open                       | Requires customer-corpus validation      |
| Specific agent framework                            | Open                       | Architecture decision                    |
| Specific sandbox implementation                     | Open                       | Security/performance validation required |
| Specific database                                   | Open                       | Architecture decision                    |
| Full cryptographic proof of neural inference        | Rejected for MVP           | Excessive complexity                     |
| Complete enterprise ontology                        | Rejected for MVP           | Excessive scope                          |
| Complete digital twin                               | Rejected for MVP           | Excessive scope                          |
| Unrestricted autonomous OT control                  | Rejected                   | Consequence/security conflict            |
| Giant universal model                               | Rejected                   | Hardware/resource conflict               |
| Local chatbot + vector database as complete product | Rejected                   | Insufficient capability surface          |

This is consistent with Phase 0's explicit separation between technology/approach status and product requirements. 

---

# 5. Requirement classification summary

The current register contains **77 requirement candidates**.

| Requirement class          | Approx. count | Role                               |
| -------------------------- | ------------: | ---------------------------------- |
| Business                   |             3 | Product outcome                    |
| User / UX                  |             4 | User interaction/outcome           |
| Task understanding         |             3 | Task interpretation                |
| Model/capability selection |             3 | Adaptive capability behavior       |
| Agentic execution          |             6 | Multi-step execution               |
| Tool execution             |             4 | Governed actions                   |
| Knowledge retrieval        |             6 | Evidence-grounded knowledge access |
| Document intelligence      |             4 | Enterprise document handling       |
| Multimodal                 |             3 | Visual/technical understanding     |
| Engineering information    |             3 | P&ID/engineering structures        |
| Code execution             |             4 | Untrusted computation              |
| Artifacts                  |             4 | Enterprise deliverables            |
| Verification               |             4 | Correctness/completion             |
| Security                   |             6 | Security controls                  |
| Sovereignty                |             7 | Sovereign operation                |
| Audit/provenance           |             4 | Traceability                       |
| Data/knowledge             |             8 | Evidence/data governance           |
| Evaluation                 |             5 | Qualification                      |
| Hardware/resource          |             4 | Feasibility/performance            |
| Deployment/operations      |             5 | Controlled deployment              |
| Governance                 |             4 | Administration                     |

**Important:** the count is not itself a completeness claim. Several requirements are intentionally grouped at product-behavior level and will be decomposed only when Phase 2/PRD work establishes the necessary scope.

---

# 6. Requirement maturity classification

The register should not treat every requirement as equally mature.

## A. Confirmed / Strongly supported

These are sufficiently grounded to form the core product contract:

* local operation;
* no external AI API dependency for core functionality;
* confidential data boundary;
* multimodal technical-document capability;
* enterprise knowledge authority/revision;
* permission-aware retrieval;
* evidence sufficiency;
* controlled agent/tool authority;
* sandboxed code execution;
* layered verification;
* artifact generation;
* provenance;
* auditability;
* customer-local qualification;
* controlled sovereignty;
* bounded OT interaction;
* single-system MVP boundary.

These follow directly from the established Phase-0 findings and hard constraints.  

## B. Strong Requirement Candidates

These are highly justified product behaviors but require validation before final PRD freezing:

* adaptive capability escalation;
* risk-tiered autonomy;
* constrained dynamic workflows;
* typed tool contracts;
* detailed provenance behavior;
* evidence sufficiency response mapping;
* customer-specific security profiles;
* resource-aware execution;
* proof/execution records;
* advanced engineering structural reasoning.

## C. Requires Validation

These should **not** be disguised as requirements with arbitrary numbers:

* latency thresholds;
* throughput;
* concurrency;
* VRAM/resource envelope;
* minimum model quality;
* exact artifact quality thresholds;
* exact prompt-injection resistance thresholds;
* sandbox assurance/performance thresholds;
* customer acceptance of sovereignty evidence;
* first deployment security profile.

This follows the Phase-0 evidence-gap register. 

---

# 7. Research → Requirement Traceability Matrix

The Phase-1 prompt requires every Critical and High requirement to have traceability through **Requirement → Finding → Evidence → Source → Product Implication → Confidence → Validation**. 

Rather than duplicating every cell of the central register, the following is the consolidated high-level traceability map. The detailed evidence/source fields in the register above are the authoritative row-level trace.

| Requirement family        | Primary Phase-0 findings | Evidence basis           | Product implication                       | Validation |
| ------------------------- | ------------------------ | ------------------------ | ----------------------------------------- | ---------- |
| Confidential local work   | EF-01/02                 | R1/R2 + hard constraints | Local confidential execution              | V1/V4      |
| Multimodal knowledge      | EF-03                    | R1/R4/R7                 | Visual + textual + structural processing  | V2/V4      |
| Authority/revision        | EF-04                    | R1/R5/R7                 | Temporal/authority-aware knowledge        | V2/V4      |
| Knowledge lifecycle       | EF-05                    | R5/R7                    | Derived knowledge cannot equal truth      | V2/V4      |
| Evidence sufficiency      | EF-06                    | R5/R6/R7                 | Retrieve/refuse/escalate/ask              | V4         |
| External authorization    | EF-07                    | R5/R8                    | LLM cannot self-authorize                 | V5         |
| Internal prompt injection | EF-08                    | R5/R8                    | Data/control-plane separation             | V5         |
| Code isolation            | EF-09                    | R4/R5/R8                 | Controlled hostile-code execution         | V5         |
| Layered verification      | EF-10                    | R5/R6                    | Correctness must be established           | V4/V6      |
| Provenance                | EF-11                    | R6/R7                    | Claims/artifacts traceable to evidence    | V4/V6      |
| Heterogeneous evaluation  | EF-12                    | R7                       | Representative difficult workflows        | V2/V4      |
| Customer qualification    | EF-13                    | R7                       | Production validation on customer data    | V2         |
| Supply-chain sovereignty  | EF-14                    | R8                       | Approved offline software/model lifecycle | V7         |
| OT boundary               | EF-15                    | R8                       | No unrestricted OT autonomy               | V5/V7      |
| Agent reliability         | FM-01–20                 | R5                       | Controlled failure/recovery               | V4/V5      |
| Hardware feasibility      | FM-15 / CR-01            | R4/R5/R7                 | Measured resource envelope                | V3         |
| Competitive baseline      | R3                       | competitor research      | Search/docs/files/tasks/artifacts/UX      | V1/V4      |

---

# 8. Requirement Conflict Register

The Phase-1 prompt explicitly requires conflicts to be preserved rather than arbitrarily resolved. 

| Conflict ID | Requirement A                               | Requirement B                              | Conflict                                                                                     | Impact                                      | Current Resolution                                                    | Validation Needed          |
| ----------- | ------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------- | -------------------------- |
| RC-01       | PRD-MC-001 multi-model capability           | PRD-HR-001 single-system MVP               | More capability diversity can increase resource pressure.                                    | Model portfolio complexity and performance. | Require capability diversity but constrain it by measured envelope.   | V3                         |
| RC-02       | PRD-AE-005 autonomy                         | PRD-SEC-001/004 external authorization     | More autonomy increases action risk.                                                         | Workflow friction vs automation.            | Risk-tiered autonomy.                                                 | V1/V4/V5                   |
| RC-03       | PRD-AE-006 dynamic workflows                | PRD-EV-005 reproducible qualification      | Dynamic behavior can reduce reproducibility.                                                 | Debugging/qualification complexity.         | Constrained dynamic workflow behavior.                                | V4                         |
| RC-04       | PRD-KR-001 broad retrieval                  | PRD-KR-003 evidence sufficiency            | More evidence can improve recall but increase irrelevant/stale material.                     | Retrieval quality and latency.              | Govern retrieval by authority, revision and sufficiency.              | V2/V4                      |
| RC-05       | PRD-AP-002 durable audit                    | Privacy/data minimization requirements     | Long-lived audit records may conflict with customer-specific deletion/retention obligations. | Compliance and forensic capability.         | Support both at requirement level; do not freeze retention semantics. | V7 + legal/customer review |
| RC-06       | PRD-SOV-003 offline/no-egress               | PRD-SOV-006 security updates               | Secure maintenance requires controlled update paths.                                         | Operational maintenance.                    | Controlled offline update mechanism.                                  | V7                         |
| RC-07       | PRD-MM-002 engineering structural reasoning | PRD-HR-003 constrained resources           | Rich multimodal/structural processing may exceed target hardware.                            | MVP feasibility.                            | Requirement retained; implementation/model strategy remains open.     | V3                         |
| RC-08       | PRD-AG-004 human artifact quality           | PRD-AE-005 automation                      | Human approval/quality checks can reduce workflow speed.                                     | Productivity vs assurance.                  | Risk-based verification/approval.                                     | V1/V6                      |
| RC-09       | PRD-DO-003 generic platform                 | PRD-DO-004 OT/security profiles            | Sector-specific controls increase product complexity.                                        | Product scope.                              | Common core + deployment profiles.                                    | V7                         |
| RC-10       | PRD-KR-002 historical knowledge             | PRD-KR-001 current authoritative knowledge | Historical evidence can be relevant but dangerous when interpreted as current.               | Temporal reasoning.                         | Explicit revision/effective-state semantics.                          | V2                         |

---

# 9. Requirement Gap Register

These are **not invented requirements**. They are places where the current requirement set cannot responsibly be made more precise without validation.

| Gap ID | Gap                                           | Impact                                           | Classification          | Resolution              |
| ------ | --------------------------------------------- | ------------------------------------------------ | ----------------------- | ----------------------- |
| RG-01  | Exact 3–5 MVP workflows                       | Determines functional scope                      | **Open Question**       | V1                      |
| RG-02  | Primary MVP user/persona                      | Determines UX and permissions                    | **Open Question**       | V1                      |
| RG-03  | First target organization/security profile    | Determines deployment constraints                | **Open Question**       | V7                      |
| RG-04  | Quantitative latency/throughput targets       | Determines NFR acceptance                        | **Requires Validation** | V3                      |
| RG-05  | Required concurrency                          | Determines resource envelope                     | **Requires Validation** | V3                      |
| RG-06  | Reference GPU/hardware                        | Determines deployment feasibility                | **Requires Validation** | V3                      |
| RG-07  | Minimum acceptable task reliability           | Determines agent autonomy boundary               | **Requires Validation** | V4                      |
| RG-08  | Minimum multimodal/P&ID quality               | Determines qualification                         | **Requires Validation** | V2/V4                   |
| RG-09  | Exact artifact acceptance thresholds          | Determines artifact release criteria             | **Requires Validation** | V6                      |
| RG-10  | Exact security/adversarial thresholds         | Determines security qualification                | **Requires Validation** | V5                      |
| RG-11  | Sandbox assurance level                       | Determines security profile                      | **Requires Validation** | V5/V7                   |
| RG-12  | Customer authority hierarchy                  | Determines retrieval governance                  | **Open Question**       | V1/V2                   |
| RG-13  | Customer metadata availability                | Determines data onboarding                       | **Requires Validation** | V2                      |
| RG-14  | Audit retention/deletion semantics            | Potential privacy/audit conflict                 | **Open Question**       | V7                      |
| RG-15  | Accepted sovereignty evidence                 | Determines deployment proof                      | **Requires Validation** | V7                      |
| RG-16  | Exact human-approval boundaries               | Determines autonomy                              | **Requires Validation** | V1/V4                   |
| RG-17  | Supported code languages/use cases            | Determines code-execution scope                  | **Open Question**       | V1                      |
| RG-18  | Exact evaluation thresholds                   | Determines qualification                         | **Requires Validation** | V4                      |
| RG-19  | Exact model portfolio                         | Implementation decision, not product requirement | **Open Question**       | V3                      |
| RG-20  | Exact retrieval/document/sandbox technologies | Architecture decision                            | **Open Question**       | Later engineering phase |

---

# 10. Missing-requirement assessment

The Phase-1 prompt requires a systematic search for missing requirements across workflow, security, data, agent behavior, tools, multimodality, verification, artifacts, auditability, deployment, operations and evaluation. 

| Domain            | Status       | Assessment                                                                                            |
| ----------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| Problem           | **COMPLETE** | Core confidential knowledge-work problem represented                                                  |
| Users             | **PARTIAL**  | User classes known; primary MVP persona requires validation                                           |
| Workflows         | **PARTIAL**  | Capability requirements established; priority workflows unresolved                                    |
| Sovereignty       | **COMPLETE** | Explicit, enforceable and evidence-oriented                                                           |
| Agentic execution | **COMPLETE** | Execution, state, completion, recovery and autonomy covered                                           |
| Knowledge         | **COMPLETE** | Authority, revision, states, provenance, sufficiency covered                                          |
| Multimodality     | **COMPLETE** | Text/visual/structural technical information covered                                                  |
| Tools             | **COMPLETE** | Authorization, contracts, side effects and validation covered                                         |
| Code              | **COMPLETE** | Generation, isolation, credentials, network, verification covered                                     |
| Artifacts         | **PARTIAL**  | Capability established; exact quality thresholds open                                                 |
| Verification      | **COMPLETE** | Layering, completion, abstention/escalation covered                                                   |
| Auditability      | **COMPLETE** | Execution and claim/artifact provenance covered                                                       |
| Hardware          | **PARTIAL**  | Constraint established; quantitative envelope open                                                    |
| Security          | **COMPLETE** | Major research-derived threats/controls represented                                                   |
| Evaluation        | **PARTIAL**  | Evaluation behavior defined; thresholds pending R10/validation                                        |
| Deployment        | **PARTIAL**  | Sovereignty/deployment model defined; first customer profile open                                     |
| Administration    | **COMPLETE** | Authorization, component identity, audit and governance covered                                       |
| Extensibility     | **PARTIAL**  | Capability/model replaceability is preserved, but extension governance remains to be formalized later |

### Result

There are **no identified critical conceptual requirement domains missing**.

The partial areas are primarily **parameterization and validation**, not missing product concepts.

---

# 11. Rejected requirement directions

The following should remain explicitly outside the product requirement baseline unless a future phase reopens them with evidence:

### Rejected

1. Dependence on external cloud AI APIs.
2. Product defined as a local chatbot only.
3. Image-only P&ID reasoning.
4. OCR-only engineering understanding.
5. Universal fixed-size retrieval units.
6. AI-derived knowledge automatically becoming authoritative.
7. One scalar confidence score.
8. One giant model serving every workload.
9. Dozens of tiny specialists as a product requirement.
10. Unrestricted autonomous tool access.
11. Model-controlled authorization.
12. Retry-until-success.
13. Citation treated as proof of correctness.
14. Checkpointing treated as exactly-once side effects.
15. Docker alone treated as sufficient hostile-code isolation.
16. “No observed traffic” treated as sovereignty proof.
17. Complete digital twin as MVP requirement.
18. Universal enterprise ontology as MVP requirement.
19. Public datasets as production qualification.
20. Full autonomous OT/ICS control.
21. Hyperscale cloud infrastructure as an MVP capability.
22. Giant foundation-model training as an MVP capability.

These exclusions are directly consistent with the Phase-0 rejected approaches and project constraints. 

---

# 12. Critical requirement set

The following constitute the **minimum product proposition**. If one of these disappears, the Workbench starts losing its defining identity.

### Sovereignty

* **PRD-SOV-001** — no external AI API dependency.
* **PRD-SOV-002** — confidential data remains inside defined boundary.
* **PRD-SOV-003/004** — default-deny external communication with independent enforcement.
* **PRD-SOV-005** — sovereignty evidence.

### Confidential knowledge work

* **PRD-BR-001**
* **PRD-UX-001**
* **PRD-AE-001**

### Enterprise knowledge

* **PRD-KR-001**
* **PRD-KR-003**
* **PRD-KR-004**
* **PRD-DK-001**
* **PRD-DK-002**
* **PRD-DK-007**

### Multimodal engineering

* **PRD-MM-001**
* **PRD-MM-002**

### Governed agency

* **PRD-AE-005**
* **PRD-TE-001**
* **PRD-TE-004**
* **PRD-SEC-001**
* **PRD-SEC-002**
* **PRD-SEC-003**

### Safe computation

* **PRD-CE-002**

### Verification

* **PRD-VR-001**
* **PRD-VR-003**
* **PRD-VR-004**

### Enterprise output

* **PRD-AG-001**

### Traceability

* **PRD-AP-001**

### Evaluation

* **PRD-EV-001**
* **PRD-EV-004**

### Hardware feasibility

* **PRD-HR-001**

This is the first useful **MVP requirement spine**.

---

# 13. Product requirement dependency structure

At product level, the dependencies now look like this:

```text
CONFIDENTIAL USER TASK
        │
        ▼
TASK UNDERSTANDING
        │
        ├──────────────► SECURITY CONTEXT / AUTHORIZATION
        │
        ▼
EVIDENCE REQUIREMENT IDENTIFICATION
        │
        ▼
ENTERPRISE KNOWLEDGE / MULTIMODAL EVIDENCE
        │
        ├── authority
        ├── revision
        ├── authorization
        ├── provenance
        └── structural/visual evidence
        │
        ▼
EVIDENCE SUFFICIENCY
        │
   ┌────┼──────────────┐
   │    │              │
   ▼    ▼              ▼
SUFFICIENT  INSUFFICIENT  CONFLICTED/STALE/
   │         │            UNAUTHORIZED
   │         │              │
   │         └──────┬───────┘
   │                ▼
   │        RETRIEVE / ASK /
   │        ESCALATE / STOP
   │
   ▼
WORKFLOW PLANNING
   │
   ▼
CONTROLLED CAPABILITIES / TOOLS
   │
   ▼
EXECUTION
   │
   ├── code → isolation
   ├── tools → authorization
   └── data → policy boundary
   │
   ▼
VERIFICATION
   │
   ├── PASS ──────────────┐
   ├── FAIL               │
   ├── INSUFFICIENT       │
   └── HUMAN REVIEW       │
                          ▼
                    ARTIFACT / RESULT
                          │
                          ▼
                 PROVENANCE + AUDIT
                          │
                          ▼
                    RELEASE / USER
```

This is a **requirement dependency model**, not an architecture diagram. It deliberately describes product behavior rather than component topology.

---

# 14. What Phase 1 has actually decided

There are several important product-level decisions now defensible.

## Decision D-01 — Product category

The product is **not**:

> a self-hosted chatbot.

It is:

> **a sovereign AI execution environment for confidential enterprise knowledge work.**

Phase 0 explicitly reached this implication from the user/problem evidence. 

---

## Decision D-02 — Core product loop

The minimum product loop is:

```text
Task
→ Evidence
→ Understand
→ Execute
→ Verify
→ Produce
→ Trace
```

Not:

```text
Prompt
→ LLM
→ Answer
```

---

## Decision D-03 — Evidence is a product object

Evidence is not merely a hidden RAG implementation detail.

The product must be able to reason about:

```text
source
revision
authority
authorization
structure
visual evidence
provenance
validity
sufficiency
conflict
```

That follows directly from EF-04–EF-06 and the Phase-0 data requirements. 

---

## Decision D-04 — Agent autonomy is conditional

The product can automate reasoning and workflow progression.

It cannot allow:

```text
LLM → self-authorize → execute consequence
```

The product contract is:

```text
Reason freely within allowed boundaries
+
act only within externally enforced authority
+
verify before consequential completion
```

---

## Decision D-05 — Verification is part of the product

Verification is not merely a future QA subsystem.

For important workflows:

```text
Generation ≠ Success
```

Success requires evidence that the expected outcome actually satisfies the applicable acceptance conditions.

---

## Decision D-06 — Customer adaptation is part of production qualification

The product cannot be qualified solely against public benchmark data.

Customer terminology, revisions, authority hierarchy, ACLs, engineering conventions and organizational history materially affect performance. 

---

# 15. Phase-1 readiness assessment

## Product Requirement Readiness

| Area                  | Status                 | Assessment                                                       |
| --------------------- | ---------------------- | ---------------------------------------------------------------- |
| Business outcome      | **COMPLETE**           | Product proposition is clear                                     |
| User outcome          | **PARTIAL**            | User classes known; primary persona needs validation             |
| Core workflows        | **PARTIAL**            | Workflow capabilities defined; MVP workflow priority unresolved  |
| Task understanding    | **COMPLETE**           | Sufficient behavioral definition                                 |
| Agent execution       | **COMPLETE**           | Multi-step, state, recovery and autonomy defined                 |
| Tool execution        | **COMPLETE**           | Authorization and execution behavior defined                     |
| Knowledge retrieval   | **COMPLETE**           | Authority/revision/evidence/sufficiency defined                  |
| Document intelligence | **COMPLETE**           | Required information classes and structural preservation defined |
| Multimodal            | **COMPLETE**           | Core requirement established                                     |
| Engineering/P&ID      | **COMPLETE**           | Product-level representation requirement established             |
| Code execution        | **COMPLETE**           | Isolation/verification requirements established                  |
| Artifacts             | **PARTIAL**            | Output classes known; acceptance thresholds open                 |
| Verification          | **COMPLETE**           | Behavioral requirement sufficiently defined                      |
| Security              | **COMPLETE**           | Major security behavior established                              |
| Sovereignty           | **COMPLETE**           | Explicit and testable at requirement level                       |
| Provenance/audit      | **COMPLETE**           | Core traceability defined                                        |
| Data governance       | **COMPLETE**           | Source/derived/operational knowledge requirements established    |
| Evaluation            | **PARTIAL**            | Evaluation model defined; quantitative thresholds open           |
| Hardware              | **PARTIAL**            | Constraint known; actual envelope unvalidated                    |
| Deployment            | **PARTIAL**            | Core deployment principle known; first profile unresolved        |
| Administration        | **COMPLETE**           | Core governance behavior defined                                 |
| Exact technologies    | **INTENTIONALLY OPEN** | Correctly deferred                                               |
| Architecture          | **INTENTIONALLY OPEN** | Correctly deferred                                               |

---

# 16. Phase-1 targeted validation set

The Phase-0 validations remain relevant, but Phase 1 now gives them a more precise purpose.

| Validation                            | Requirement areas affected                  | Why it matters                                              |
| ------------------------------------- | ------------------------------------------- | ----------------------------------------------------------- |
| **V1 — Priority Workflow Validation** | UX, workflows, autonomy, artifacts          | Determines what actually belongs in MVP                     |
| **V2 — Representative Corpus**        | knowledge, documents, multimodality, P&IDs  | Determines whether requirements are achievable on real data |
| **V3 — Hardware Envelope**            | models/capabilities, NFRs, deployment       | Determines quantitative resource/performance constraints    |
| **V4 — End-to-End Agent Benchmark**   | agent, tools, verification, completion      | Determines acceptable autonomy/reliability                  |
| **V5 — Security Adversarial Suite**   | security, sandbox, prompt injection, egress | Determines security qualification                           |
| **V6 — Artifact Acceptance**          | artifacts, verification                     | Determines usable-output threshold                          |
| **V7 — Customer Security Review**     | sovereignty, deployment, audit, compliance  | Determines deployment-specific security requirements        |

These are consistent with the Phase-0 validation plan. 

---

# 17. Phase-1 Gate Decision

# **B — READY WITH TARGETED VALIDATION**

This is the strongest defensible Phase-1 decision.

### Why not A — READY?

Because the requirement set still contains high-impact variables whose values cannot responsibly be frozen:

1. first 3–5 MVP workflows;
2. primary MVP user;
3. target deployment/security profile;
4. hardware/performance envelope;
5. end-to-end reliability threshold;
6. artifact acceptance thresholds;
7. adversarial-security thresholds;
8. customer sovereignty evidence acceptance;
9. exact autonomy boundaries;
10. customer-local data qualification conditions.

These are not conceptual gaps; they are **validation-dependent parameters**.

### Why not C — NOT READY?

Because the product's required behavior is now sufficiently defined across the critical dimensions:

```text
Confidential work
        ↓
Local sovereign execution
        ↓
Task understanding
        ↓
Enterprise evidence
        ↓
Multimodal understanding
        ↓
Controlled agentic execution
        ↓
Verification
        ↓
Enterprise artifact
        ↓
Provenance + audit
```

Phase 0 explicitly established that unresolved questions of this type do not block product definition. 

---

# 18. Phase-1 closure statement

The transformation is now:

```text
RESEARCH
    ↓
EVIDENCE
    ↓
FINDING
    ↓
PRODUCT IMPLICATION
    ↓
REQUIREMENT
    ↓
PRIORITY
    ↓
ACCEPTANCE CONCEPT
    ↓
DEPENDENCY
    ↓
VALIDATION / OPEN ISSUE
```

The most important result is that we have **not** allowed the research to prematurely dictate implementation.

For example:

> Research suggests Qwen3-VL.

does **not** become:

> “The product shall use Qwen3-VL.”

Instead it becomes:

> **The product shall support sufficiently capable local multimodal processing for the defined engineering-document workloads under the measured deployment resource envelope.**

Likewise:

> Research suggests OpenSearch.

does **not** become:

> “The product shall use OpenSearch.”

It becomes:

> **The product shall retrieve enterprise evidence using relevance together with authority, revision, authorization, temporal and structural constraints.**

That distinction is explicitly required by the Phase-1 prompt. 

---

# Final Phase-1 Decision

| Gate                                                     | Decision                               |
| -------------------------------------------------------- | -------------------------------------- |
| **Product requirements sufficiently defined?**           | **YES**                                |
| **Core product proposition captured?**                   | **YES**                                |
| **Critical security/sovereignty requirements captured?** | **YES**                                |
| **Data/knowledge requirements captured?**                | **YES**                                |
| **Agent/tool/verification behavior captured?**           | **YES**                                |
| **MVP workflow priority finalized?**                     | **NO — validation required**           |
| **Quantitative NFRs finalized?**                         | **NO — validation required**           |
| **Customer deployment profile finalized?**               | **NO — validation required**           |
| **Technology selection required now?**                   | **NO**                                 |
| **Architecture required now?**                           | **NO**                                 |
| **Critical requirement gaps blocking Phase 2?**          | **NO**                                 |
| **Phase-1 Gate**                                         | **B — READY WITH TARGETED VALIDATION** |

## Phase 2 input

The primary output from Phase 1 is now:

> **A product-level requirement baseline defining what the Sovereign Agentic AI Workbench must achieve, why each requirement exists, how it will eventually be validated, what depends on it, and which uncertainties must remain open.**

Therefore:

# **PHASE 1 CLOSED — READY WITH TARGETED VALIDATION**

**Next phase:** **Phase 2 — Product Scope & Boundary Definition.**

The key change entering Phase 2 is that we should **not carry the entire 77-requirement register forward as an undifferentiated backlog**. Phase 2 should use it to establish the **MVP boundary, supported workflows, exclusions, user boundary, capability boundary, autonomy boundary, deployment boundary, and explicit out-of-scope surface**.
