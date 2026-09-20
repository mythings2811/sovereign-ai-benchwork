# Phase 5 — Non-Functional Requirement & Quality Attribute Validation

## 1. Phase Objective

Establish a **measurable quality contract** for the Sovereign Agentic AI Workbench.

Phase 5 does **not** select models, frameworks, databases, inference engines, sandbox technologies or final architecture.

It answers:

> **How good, fast, reliable, secure, resource-efficient and demonstrably sovereign must the product be for the MVP to be considered acceptable?**

The phase converts the remaining Phase-4 open questions into:

* measurable quality attributes;
* metric definitions;
* test methods;
* benchmark datasets;
* acceptance gates;
* target-setting procedures;
* unresolved thresholds;
* validation experiments;
* release qualification rules.

The resulting framework is intended to support later architecture and technology selection.

---

# 2. Current State

Phase 4 established the functional product contract and five canonical workflows:

1. Organizational Knowledge Investigation
2. Inspection / Technical Report Analysis
3. P&ID / Engineering Drawing Analysis
4. Technical Artifact Generation
5. Controlled Code-Assisted Analysis

The product requirement baseline is substantially complete.

The unresolved portion is primarily **quantitative**.

Phase 1 already identified that the incomplete areas are parameterization and validation rather than missing product concepts.

Phase 0 identified the highest-risk assumptions as:

1. mid-range GPU feasibility;
2. agent reliability;
3. customer acceptance;
4. customer-data availability;
5. artifact quality;
6. security deployment acceptance.

---

# 3. Phase 5 Principle

## Do not invent numbers.

The project explicitly prohibits silently freezing:

* latency;
* throughput;
* file-size limits;
* context limits;
* concurrency;
* GPU/CPU/RAM/storage requirements;
* reliability percentages;
* retrieval-quality thresholds;
* artifact-quality thresholds;
* P&ID accuracy thresholds;
* security-assurance thresholds;
* availability;
* retention.

Therefore every quantitative requirement receives one of four states:

| Status                  | Meaning                                                     |
| ----------------------- | ----------------------------------------------------------- |
| **Established**         | Supported by existing evidence                              |
| **Candidate Target**    | Useful engineering target, but not yet acceptance-qualified |
| **Requires Validation** | Must be determined experimentally                           |
| **Open Question**       | Cannot yet be responsibly quantified                        |

This is consistent with the project's evidence discipline: uncertainty must remain explicit rather than being converted into artificial certainty.

---

# 4. Quality Model

The Phase-5 quality model is:

```text
                    PRODUCT QUALITY
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
   Functional         Trustworthiness      Operational
    Quality               │                Quality
       │                  │                  │
       │          ┌───────┼───────┐          │
       │          │       │       │          │
   Workflow      Accuracy Security Reliability Performance
   Success       Grounding Sovereignty       Resource
   Retrieval     Verification Privacy        Availability
   Multimodal    Provenance  Auditability     Scalability
   Artifacts     Abstention  Resilience       Maintainability
   Code          Safety      Supply Chain     Observability
```

ISO/IEC 25010:2023 is useful as a general product-quality reference because it explicitly supports requirements specification, testing objectives, acceptance criteria and product-quality measurement.

For this project, however, generic software quality attributes are insufficient. They must be combined with **AI-specific evaluation and sovereignty/security measurements**.

---

# 5. Quality Attribute Register

| ID    | Quality Attribute               | Importance | Phase-5 Status      |
| ----- | ------------------------------- | ---------: | ------------------- |
| QA-01 | Task success                    |   Critical | Requires Validation |
| QA-02 | End-to-end workflow reliability |   Critical | Requires Validation |
| QA-03 | Evidence grounding              |   Critical | Requires Validation |
| QA-04 | Retrieval quality               |   Critical | Requires Validation |
| QA-05 | Authority/revision correctness  |   Critical | Requires Validation |
| QA-06 | Multimodal extraction quality   |   Critical | Requires Validation |
| QA-07 | P&ID structural accuracy        |   Critical | Requires Validation |
| QA-08 | Verification effectiveness      |   Critical | Requires Validation |
| QA-09 | Artifact correctness            |   Critical | Requires Validation |
| QA-10 | Code correctness                |       High | Requires Validation |
| QA-11 | Safe abstention                 |   Critical | Requires Validation |
| QA-12 | Authorization enforcement       |   Critical | Acceptance gate     |
| QA-13 | Prompt-injection resistance     |   Critical | Requires Validation |
| QA-14 | Sandbox containment             |   Critical | Requires Validation |
| QA-15 | Zero-egress behavior            |   Critical | Acceptance gate     |
| QA-16 | Supply-chain integrity          |   Critical | Acceptance gate     |
| QA-17 | Latency                         |       High | Requires Validation |
| QA-18 | Throughput                      |       High | Requires Validation |
| QA-19 | GPU/resource efficiency         |   Critical | Requires Validation |
| QA-20 | Resource isolation              |       High | Requires Validation |
| QA-21 | Availability/recovery           |       High | Requires Validation |
| QA-22 | Observability completeness      |       High | Requires Validation |
| QA-23 | Provenance completeness         |   Critical | Requires Validation |
| QA-24 | Human usability                 |       High | Requires Validation |
| QA-25 | Maintainability/extensibility   |     Medium | Requires Validation |

---

# 6. Performance Validation

## 6.1 Performance must be workflow-based

Do not optimize for isolated:

> tokens/second

as the primary product metric.

The product is an execution environment.

Therefore the relevant measurement is:

> **time and resources required to produce an acceptable verified outcome.**

The benchmark must measure:

* task start → first useful response;
* task completion time;
* retrieval time;
* document-processing time;
* model inference time;
* tool execution time;
* verification time;
* artifact-generation time;
* total workflow duration;
* GPU memory;
* GPU utilization;
* CPU utilization;
* RAM;
* storage;
* KV-cache pressure;
* queueing;
* failures;
* retries;
* escalation.

---

# 7. Performance Metrics

| Metric                      | Definition                               | Status              |
| --------------------------- | ---------------------------------------- | ------------------- |
| P50 end-to-end latency      | median workflow completion time          | Requires Validation |
| P95 end-to-end latency      | 95th percentile workflow completion time | Requires Validation |
| TTFT                        | time to first meaningful model output    | Requires Validation |
| TPOT                        | time per generated output token          | Requires Validation |
| Retrieval latency P95       | retrieval + filtering + reranking time   | Requires Validation |
| Document processing latency | ingestion/extraction time per document   | Requires Validation |
| Verification latency        | time required for verification stage     | Requires Validation |
| Artifact generation latency | source-to-artifact generation time       | Requires Validation |
| GPU peak memory             | maximum VRAM consumption                 | Requires Validation |
| GPU average utilization     | utilization during workload              | Requires Validation |
| CPU peak utilization        | maximum CPU utilization                  | Requires Validation |
| RAM peak                    | maximum resident memory                  | Requires Validation |
| Storage growth              | storage consumed per corpus/workflow     | Requires Validation |
| Failure rate                | failed workflows / attempted workflows   | Requires Validation |
| Retry rate                  | workflows requiring retry / workflows    | Requires Validation |

---

# 8. Hardware Envelope

The single-workstation/server boundary is established.

The exact hardware envelope is not.

The project specifically identifies mid-range GPU feasibility as a high-risk assumption.

Therefore Phase 5 must establish a **reference hardware envelope experimentally**.

## Required benchmark dimensions

```text
GPU
├── VRAM
├── compute utilization
├── memory bandwidth
└── thermal/power behavior

CPU
├── cores
├── utilization
└── document-processing load

RAM
├── baseline
├── peak
└── concurrency pressure

Storage
├── model footprint
├── index footprint
├── document footprint
└── artifact/log growth
```

### Acceptance principle

The system passes hardware qualification only if the **complete representative workflow suite** executes within the validated resource envelope.

A model that fits in VRAM but causes unacceptable end-to-end workflow failure does not satisfy the requirement.

---

# 9. Resource Envelope Experiment

The experiment must vary:

* model size;
* quantization;
* context size;
* image resolution;
* document size;
* concurrent tasks;
* model residency;
* retrieval corpus size;
* output length;
* verification depth.

Measure:

```text
Quality
    vs
Latency
    vs
VRAM
    vs
RAM
    vs
Concurrency
```

This produces the project's actual **quality/resource frontier**.

No model should be selected merely because it has the highest benchmark quality.

---

# 10. Reliability

Reliability must be measured at multiple levels.

## 10.1 Component reliability

Examples:

* inference failure;
* OCR failure;
* document parser failure;
* retrieval failure;
* tool failure;
* sandbox failure;
* artifact-generation failure.

## 10.2 Workflow reliability

Primary metric:

> **Verified workflow completion rate**

A workflow is successful only when its defined completion predicates and verification requirements are satisfied.

This follows the established requirement that generation does not equal success.

## 10.3 Recovery reliability

Measure whether the system correctly handles:

* transient failure;
* permanent failure;
* semantic failure;
* authorization failure;
* insufficient evidence;
* conflicting evidence;
* stale evidence;
* interrupted execution;
* resource exhaustion.

---

# 11. Reliability Metric Model

For workflow \(w\):

$$
R_w =
\frac{\text{verified successful executions}}
{\text{eligible execution attempts}}
$$

Do **not** count:

* model-declared completion;
* syntactically valid output;
* successful API/tool invocation;
* generated artifact existence

as successful completion by themselves.

---

# 12. Failure Severity

A simple aggregate reliability score is insufficient.

Failures should be weighted by consequence.

Recommended classification:

| Severity | Example                                                               |
| -------- | --------------------------------------------------------------------- |
| S0       | Cosmetic/UI issue                                                     |
| S1       | Recoverable workflow inconvenience                                    |
| S2       | Incorrect non-consequential result                                    |
| S3       | Materially misleading technical result                                |
| S4       | Security/authorization/provenance failure                             |
| S5       | Potential safety, physical, legal or major organizational consequence |

The acceptance policy should impose progressively stricter thresholds as consequence increases.

---

# 13. Retrieval Quality

Retrieval quality must be evaluated independently from final answer quality.

The evaluation corpus must contain:

* authoritative documents;
* superseded documents;
* conflicting documents;
* unauthorized documents;
* temporally invalid documents;
* duplicate documents;
* documents containing relevant and irrelevant evidence;
* structured tables;
* figures;
* P&IDs;
* scanned documents.

This follows the Phase-0 conclusion that relevance alone cannot establish enterprise truth.

---

# 14. Retrieval Metrics

Required measurements:

### Recall@K

Did the retrieval system retrieve the evidence required to answer the task?

### Precision@K

How much of retrieved evidence is actually relevant?

### Authority accuracy

Did the system select the authoritative source?

### Revision accuracy

Did it select the correct revision?

### Authorization accuracy

Did it exclude evidence the user was not permitted to access?

### Temporal accuracy

Did it correctly distinguish current and historical evidence?

### Sufficiency accuracy

Did the system correctly determine whether evidence was sufficient?

---

# 15. Retrieval Acceptance Principle

A retrieval system must not pass solely because:

> "The relevant document appeared somewhere in Top-K."

The real requirement is:

```text
Correct evidence
+
Correct authority
+
Correct revision
+
Correct authorization
+
Correct temporal state
+
Sufficient evidence
```

This follows the established requirement that enterprise knowledge must preserve authority, revision, authorization and temporal constraints.

---

# 16. Grounding Quality

For generated claims:

$$
Grounding\ Precision =
\frac{\text{supported important claims}}
{\text{important claims evaluated}}
$$

Also measure:

$$
Unsupported\ Claim\ Rate =
\frac{\text{unsupported important claims}}
{\text{important claims}}
$$

And:

$$
Evidence\ Attribution\ Coverage =
\frac{\text{important claims with traceable evidence}}
{\text{important claims}}
$$

These are **candidate metrics**, not frozen thresholds.

---

# 17. Multimodal Quality

Multimodal evaluation must separate:

1. extraction;
2. interpretation;
3. structural reasoning;
4. consequential conclusion.

A VLM answer being semantically plausible is not sufficient.

---

# 18. Document Intelligence Metrics

Measure separately:

* OCR character/word accuracy;
* table extraction accuracy;
* reading-order accuracy;
* section reconstruction accuracy;
* figure association;
* page/region localization;
* coordinate accuracy;
* entity extraction;
* relationship extraction;
* source-region provenance.

The critical requirement is not simply:

> "Can the document be converted into text?"

It is:

> **Can the system preserve the evidence structure required for downstream reasoning?**

---

# 19. P&ID Quality

P&ID evaluation must use a structured reference representation.

Measure:

### Entity detection

$$
Precision_{entity}, Recall_{entity}, F1_{entity}
$$

### Relationship detection

$$
Precision_{relation}, Recall_{relation}, F1_{relation}
$$

### Topology correctness

Percentage of evaluated relationships for which the inferred connectivity agrees with the validated reference.

### Tag accuracy

Correct identification of equipment/instrument/valve/line tags.

### Provenance coverage

Percentage of inferred engineering relationships traceable to source page/region.

The project already rejected image-only and OCR-only P&ID reasoning and requires visual evidence plus structural engineering relationships.

---

# 20. Engineering Safety Rule

No numerical P&ID threshold should automatically authorize consequential engineering action.

Even a high measured P&ID accuracy does not transfer engineering authority from the engineer to the AI.

Therefore:

```text
Model accuracy
      ≠
Engineering authority
```

---

# 21. Verification Effectiveness

Verification itself requires evaluation.

Measure:

* true errors detected;
* false alarms;
* missed errors;
* verifier agreement;
* verifier independence;
* escalation rate;
* acceptance rate after verification.

Core metrics:

$$
Verifier\ Recall =
\frac{Errors\ detected}{Actual\ injected\ errors}
$$

$$
Verifier\ False\ Acceptance\ Rate =
\frac{Incorrect\ outputs\ accepted}{Incorrect\ outputs}
$$

The second metric is particularly important.

A verifier that frequently says "PASS" is not necessarily a good verifier.

---

# 22. Verification Independence

Where possible, avoid:

```text
Model A generates
       ↓
Model A verifies
```

as the sole verification mechanism.

Phase 5 should test:

* deterministic checks;
* independent computational checks;
* independent model checks;
* source/evidence checks;
* human checks where required.

NIST's current AI RMF measurement guidance emphasizes rigorous testing, performance assessment, uncertainty and independent review as useful elements of TEVV.

---

# 23. Artifact Quality

Artifact quality must be decomposed.

## Structural quality

* valid file;
* opens correctly;
* expected sections;
* expected tables;
* expected formatting;
* no corruption.

## Content quality

* requested content present;
* no missing required sections;
* no fabricated facts;
* correct values;
* correct references.

## Evidence quality

* consequential claims traceable;
* citations/evidence preserved;
* source identity retained.

## Human usefulness

* readable;
* usable;
* appropriate structure;
* acceptable to intended user.

The project already identifies structurally valid but operationally unusable artifacts as a known risk.

---

# 24. Artifact Acceptance

For each supported artifact class:

```text
Artifact PASS =
Structural PASS
AND
Content PASS
AND
Evidence PASS
AND
Verification PASS
AND
Human acceptance where required
```

A file merely opening successfully is not an artifact-quality pass.

---

# 25. Code-Assisted Analysis

Code evaluation must measure:

* syntactic validity;
* execution success;
* unit-test success;
* numerical correctness;
* expected output;
* resource compliance;
* sandbox policy compliance;
* absence of unauthorized network access;
* absence of unauthorized filesystem access;
* reproducibility where applicable.

Primary metric:

> **Verified computational task success rate**

not:

> code generation success rate.

---

# 26. Safe Abstention

The system must be evaluated not only on answering correctly but also on **refusing correctly**.

Test cases must include:

* insufficient evidence;
* contradictory evidence;
* stale evidence;
* unauthorized evidence;
* ambiguous request;
* unsupported modality;
* failed verification;
* unavailable tool;
* policy-prohibited action.

Metrics:

| Metric                  | Meaning                              |
| ----------------------- | ------------------------------------ |
| Correct answer rate     | correctly answers answerable tasks   |
| Correct abstention rate | refuses/escalates unanswerable tasks |
| Unsafe answer rate      | answers when it should abstain       |
| Unsafe action rate      | attempts prohibited action           |
| Over-abstention rate    | refuses answerable tasks             |

For a sovereign enterprise system, **unsafe answer/action rate deserves more weight than raw answer rate**.

---

# 27. Security Quality Attributes

Security validation must cover:

1. authorization;
2. least privilege;
3. prompt injection;
4. sensitive-information disclosure;
5. tool misuse;
6. excessive agency;
7. malicious documents;
8. generated-code attacks;
9. sandbox escape;
10. resource exhaustion;
11. supply-chain compromise;
12. egress.

OWASP's current LLM/GenAI risk taxonomy explicitly includes prompt injection, sensitive information disclosure, supply chain, improper output handling, excessive agency, vector/embedding weaknesses, misinformation and unbounded consumption.

---

# 28. Authorization Acceptance

The following must be tested:

```text
authorized user
authorized data
authorized capability
authorized action
authorized side effect
```

Negative tests must be first-class.

Example:

```text
Given user lacks access to document X
When agent attempts retrieval of X
Then retrieval is denied
And denial is auditable
And the model cannot override the denial
```

---

# 29. Prompt-Injection Validation

Test both:

### Direct injection

User attempts to override policy.

### Indirect injection

Malicious instructions are embedded inside:

* PDF;
* DOCX;
* spreadsheet;
* webpage-like imported data;
* OCR text;
* source code;
* retrieved enterprise documents.

Success criterion:

> Untrusted content must not acquire control-plane authority.

This is particularly important because air-gapping does not eliminate data-plane manipulation.

OWASP identifies prompt injection and excessive agency as distinct application risks.

---

# 30. Sandbox Validation

The sandbox must be tested against:

* filesystem escape;
* process escape;
* credential discovery;
* environment-variable access;
* network access;
* host access;
* resource exhaustion;
* persistence;
* privilege escalation;
* malicious dependencies.

The project explicitly rejects Docker-only isolation as sufficient hostile-code assurance.

Exact sandbox acceptance thresholds remain **Requires Validation**.

---

# 31. Sovereignty Validation

Sovereignty receives a dedicated acceptance model.

```text
Sovereignty =
Data Boundary
+
Compute Boundary
+
Network Enforcement
+
Network Observation
+
Supply Chain Integrity
+
Version Identity
+
Operational Evidence
```

A log saying "no network calls occurred" is not sufficient.

---

# 32. Zero-Egress Acceptance

The validation suite should include:

### Positive tests

Expected local operation succeeds.

### Negative tests

Attempt:

* DNS resolution;
* outbound TCP;
* outbound UDP;
* HTTP/HTTPS;
* proxy use;
* IPv6 egress;
* alternative network interface;
* tool-mediated communication;
* generated-code communication.

### Observation

Capture independently:

* network flows;
* DNS;
* connection attempts;
* blocked connections;
* process identity;
* destination;
* timestamp.

### Acceptance

No unauthorized external communication is successfully established.

This follows the project's existing sovereignty requirement that enforcement must exist outside application logic and that actual behavior must be evidenced.

---

# 33. Supply-Chain Validation

Every deployable release should be associated with:

* version identity;
* dependency inventory;
* model identity;
* model hash;
* software package identity;
* artifact integrity;
* approved release manifest.

For high-security deployment profiles, validate the offline update process as a separate workflow.

Sovereignty is therefore not merely runtime isolation.

It includes:

> **what software/model entered the environment and whether it was approved.**

---

# 34. Auditability

Audit completeness should be measured.

For every significant workflow, verify that the system can reconstruct:

```text
WHO
WHAT
WHEN
WHY
WITH WHICH AUTHORITY
USING WHICH CAPABILITY
USING WHICH EVIDENCE
USING WHICH MODEL/VERSION
WHICH TOOLS
WHICH ACTIONS
WHICH RESULTS
WHICH VERIFICATION
WHICH APPROVAL
WHICH FINAL ARTIFACT
```

Metric:

$$
Audit\ Coverage =
\frac{Required\ audit\ events\ captured}
{Required\ audit\ events}
$$

---

# 35. Provenance Completeness

For sampled important claims:

$$
Provenance\ Coverage =
\frac{Claims\ with\ valid\ evidence\ lineage}
{Claims\ sampled}
$$

Lineage should support:

```text
Claim
 ↓
Evidence
 ↓
Source
 ↓
Revision
 ↓
Processing
 ↓
Workflow
 ↓
Artifact
```

The project has already established provenance as a product-level requirement rather than merely an implementation detail.

---

# 36. Observability

Observability should answer:

> **What happened?**

not:

> **What did the model say happened?**

Required event classes:

* task received;
* task classification;
* capability selection;
* evidence retrieval;
* policy decision;
* tool invocation;
* tool result;
* model invocation;
* verification;
* retry;
* escalation;
* failure;
* approval;
* artifact creation;
* release;
* security event;
* network event.

---

# 37. Usability

Usability validation should focus on workflow completion rather than generic UI preference.

Measure:

* task completion without administrator assistance;
* time to understand execution state;
* time to inspect evidence;
* time to detect failure;
* time to recover;
* human acceptance rate;
* user-reported trust;
* unnecessary interaction count.

Critical UX requirement:

> Users must understand whether the system **completed, failed, abstained, or requires them to act**.

---

# 38. Quality Gates

Phase 5 establishes the following gate model.

## Gate G0 — Functional

All five workflows execute through their defined behavioral paths.

## Gate G1 — Evidence

Retrieval, provenance, authority and evidence-sufficiency tests pass.

## Gate G2 — Verification

Important outputs are verified and unsafe outputs are rejected/escalated.

## Gate G3 — Security

Authorization, prompt-injection, tool and sandbox tests pass.

## Gate G4 — Sovereignty

Zero-egress and offline-operation evidence passes.

## Gate G5 — Hardware

Representative workloads operate inside the validated resource envelope.

## Gate G6 — Reliability

Workflow reliability reaches the experimentally established acceptance threshold.

## Gate G7 — Artifact

Supported artifacts pass structural, content and human-acceptance criteria.

## Gate G8 — Release

All mandatory gates pass simultaneously.

---

# 39. Evaluation Corpus

The evaluation corpus should be frozen and versioned.

Minimum composition should represent:

### W3

* authoritative/current documents;
* stale revisions;
* conflicting documents;
* ACL differences;
* cross-document investigations.

### W1

* scanned reports;
* poor scans;
* tables;
* historical inspections;
* multi-document findings.

### W2

* P&IDs;
* engineering drawings;
* topology cases;
* ambiguous symbols;
* OCR/layout degradation.

### W4

* report templates;
* approval-note templates;
* evidence-heavy outputs.

### W5

* numerical calculations;
* code-generation cases;
* intentionally incorrect code;
* resource-abuse cases;
* security attacks.

---

# 40. Corpus Fingerprinting

Every benchmark release should record:

```text
corpus_manifest_hash
document hashes
document revisions
parser version
chunking/representation version
embedding version
reranker version
model versions
workflow version
verification version
evaluation version
```

This prevents a benchmark from silently changing between experiments.

---

# 41. Statistical Discipline

For each metric record:

* sample size;
* point estimate;
* confidence interval where appropriate;
* test conditions;
* corpus version;
* system version;
* hardware;
* model configuration;
* failure cases;
* excluded cases and exclusion reason.

Do not report:

> "Accuracy = 92%"

without specifying:

> 92% of what, on which corpus, under which configuration, using which ground truth?

NIST explicitly recommends representative test sets and documented methodology for AI accuracy measurement.

---

# 42. LLM-as-Judge Policy

LLM-based evaluation may be used as **one evaluation instrument**, not as unquestioned ground truth.

Where practical:

```text
Automated deterministic check
        +
Independent evaluator
        +
Human evaluation
        ↓
Final benchmark judgment
```

The project research stream itself identifies evaluator reliability, false positives/negatives and human-vs-AI evaluation as issues requiring dedicated evaluation science.

---

# 43. Proposed Target-Setting Procedure

Rather than inventing final thresholds now:

### Step 1

Run baseline system.

### Step 2

Run representative benchmark.

### Step 3

Measure failure distribution.

### Step 4

Identify unacceptable failure classes.

### Step 5

Set **minimum acceptable threshold**.

### Step 6

Set **engineering target** above minimum.

### Step 7

Set **stretch target**.

Example:

| Level   | Meaning                      |
| ------- | ---------------------------- |
| Minimum | Below this = product fails   |
| Target  | Normal release objective     |
| Stretch | Strong engineering objective |

The numerical values should be established from benchmark results and customer/workflow validation.

---

# 44. Threshold Register

| Requirement                          | Minimum | Target | Stretch | Current Status      |
| ------------------------------------ | ------: | -----: | ------: | ------------------- |
| End-to-end workflow success          |     TBD |    TBD |     TBD | Requires Validation |
| Unsafe answer rate                   |     TBD |    TBD |     TBD | Requires Validation |
| Correct abstention                   |     TBD |    TBD |     TBD | Requires Validation |
| Retrieval recall                     |     TBD |    TBD |     TBD | Requires Validation |
| Authority accuracy                   |     TBD |    TBD |     TBD | Requires Validation |
| Revision accuracy                    |     TBD |    TBD |     TBD | Requires Validation |
| P&ID relationship F1                 |     TBD |    TBD |     TBD | Requires Validation |
| Artifact acceptance                  |     TBD |    TBD |     TBD | Requires Validation |
| Code task correctness                |     TBD |    TBD |     TBD | Requires Validation |
| P95 latency                          |     TBD |    TBD |     TBD | Requires Validation |
| GPU peak utilization                 |     TBD |    TBD |     TBD | Requires Validation |
| Workflow failure rate                |     TBD |    TBD |     TBD | Requires Validation |
| Prompt-injection unsafe-success rate |     TBD |    TBD |     TBD | Requires Validation |
| Sandbox escape rate                  |     TBD |    TBD |     TBD | Requires Validation |
| Unauthorized action rate             |     TBD |    TBD |     TBD | Requires Validation |
| Unauthorized egress success rate     |   **0** |  **0** |   **0** | Acceptance Gate     |
| Audit completeness                   |     TBD |    TBD |     TBD | Requires Validation |
| Provenance coverage                  |     TBD |    TBD |     TBD | Requires Validation |

### Important exception

Some security properties are not ordinary optimization metrics.

For example:

> **Unauthorized external communication succeeding in a sovereign deployment is not an acceptable percentage-based trade-off.**

The desired acceptance condition is zero successful unauthorized egress.

---

# 45. Requirement Classification After Phase 5

## Frozen / Acceptance-Gated

* local processing;
* no external AI dependency;
* authorization external to model;
* least privilege;
* prompt-injection containment;
* sandboxed execution;
* zero-egress requirement;
* auditability;
* provenance;
* evidence sufficiency;
* human authority for consequential actions.

## Quantitatively Pending

* latency;
* throughput;
* reliability;
* retrieval quality;
* multimodal quality;
* P&ID quality;
* artifact quality;
* code correctness;
* resource envelope;
* concurrency;
* availability;
* recovery time;
* usability.

## Deployment-Specific

* retention;
* deletion;
* exact security profile;
* assurance level;
* hardware attestation;
* OT boundary;
* customer authority hierarchy.

---

# 46. Phase 5 Requirement Updates

The following requirement families should now receive explicit measurement definitions.

### NFR-PERF

Add:

* measurement workload;
* P50/P95/P99 where relevant;
* resource conditions;
* hardware identity;
* concurrency condition.

### NFR-REL

Add:

* successful workflow definition;
* failure taxonomy;
* recovery definition;
* severity weighting.

### NFR-QUAL

Add:

* task accuracy;
* grounding;
* retrieval;
* multimodal;
* P&ID;
* artifact;
* code metrics.

### NFR-SEC

Add:

* attack classes;
* successful attack definition;
* unsafe action definition;
* false-negative treatment.

### NFR-SOV

Add:

* enforcement test;
* observation test;
* adversarial egress test;
* supply-chain verification test.

### NFR-AUD

Add:

* event coverage;
* provenance coverage;
* reconstruction test.

---

# 47. Phase 5 Validation Matrix

| Domain                     | Primary Test                    | Secondary Test          | Human Review    |
| -------------------------- | ------------------------------- | ----------------------- | --------------- |
| W3 knowledge investigation | retrieval benchmark             | adversarial corpus      | Yes             |
| W1 inspection              | extraction + workflow benchmark | degraded scans          | Yes             |
| W2 P&ID                    | graph/topology benchmark        | visual perturbation     | **Yes**         |
| W4 artifacts               | structural/content validation   | usability test          | **Yes**         |
| W5 code                    | execution/test benchmark        | adversarial code        | Conditional     |
| Agent                      | end-to-end task benchmark       | interruption/recovery   | Yes             |
| Security                   | attack suite                    | regression suite        | Security review |
| Sovereignty                | egress test                     | deployment audit        | Security review |
| Hardware                   | resource benchmark              | soak/stress test        | No              |
| Audit                      | trace reconstruction            | tamper/omission tests   | Yes             |
| Provenance                 | lineage benchmark               | conflict/revision tests | Yes             |

---

# 48. Phase 5 Risks

| Risk                                  | Consequence              | Treatment                           |
| ------------------------------------- | ------------------------ | ----------------------------------- |
| Thresholds chosen arbitrarily         | False product confidence | Benchmark first                     |
| Aggregate score hides severe failures | Unsafe release           | Severity-weighted gates             |
| Synthetic corpus too easy             | Inflated quality         | Difficult representative corpus     |
| LLM judge bias                        | Invalid evaluation       | Independent/deterministic checks    |
| Benchmark leakage                     | False performance        | Frozen corpus                       |
| Hardware tested only in isolation     | Production failure       | End-to-end workload                 |
| Average latency hides tail latency    | Poor UX                  | P95/P99                             |
| Security tested only positively       | Missed attack paths      | Negative/adversarial tests          |
| Artifact judged only structurally     | Unusable output          | Human acceptance                    |
| Retrieval judged only by final answer | Hidden evidence failure  | Independent retrieval evaluation    |
| Model upgrade changes results         | Qualification drift      | Versioned benchmark/requalification |

---

# 49. Phase 5 Decision Register

| Decision                                                          | Status        |
| ----------------------------------------------------------------- | ------------- |
| Quality must be measured end-to-end                               | **Preferred** |
| Workflow success is the primary product-level performance measure | **Preferred** |
| Component benchmarks alone are insufficient                       | **Preferred** |
| Representative customer-like corpus required                      | **Preferred** |
| Frozen evaluation corpus required                                 | **Preferred** |
| Quantitative thresholds must be experimentally established        | **Mandatory** |
| Security acceptance uses adversarial testing                      | **Mandatory** |
| Zero-egress uses independent enforcement + observation            | **Mandatory** |
| LLM-as-judge is not sole ground truth                             | **Preferred** |
| P&ID evaluation requires structural reference data                | **Preferred** |
| Artifact acceptance combines automated + human criteria           | **Preferred** |
| Hardware qualification is end-to-end                              | **Mandatory** |
| Security failures are severity-weighted                           | **Preferred** |
| Technology selection occurs before benchmark design               | **Rejected**  |

---

# 50. Architecture Questions Created by Phase 5

Phase 5 should not answer these by choosing technologies.

It should hand architecture the following questions:

1. What resource-management mechanism can maintain the validated hardware envelope?
2. How should models be selected under measured latency/quality constraints?
3. How should evidence sufficiency be represented?
4. How should provenance survive context compression?
5. Which retrieval strategy achieves the required authority/revision metrics?
6. Which multimodal pipeline achieves required document/P&ID metrics?
7. What execution isolation satisfies the validated sandbox threat model?
8. What policy enforcement point guarantees authorization independence?
9. How should zero-egress enforcement be implemented?
10. What artifact-generation mechanism satisfies structural and human acceptance?
11. How should verification be composed to achieve the measured false-acceptance target?
12. What telemetry is required to reproduce benchmark results?
13. How should model/version changes trigger requalification?
14. What deployment profile corresponds to the first customer?

---

# 51. Phase 5 Gate

## Gate B — READY FOR TARGETED EXPERIMENTATION

Phase 5 should **not** be considered complete merely because a metric table exists.

The phase is complete when:

* every open quantitative NFR has a defined measurement method;
* every critical quality attribute has a benchmark;
* representative evaluation corpus is defined;
* security attack classes are defined;
* hardware benchmark protocol is defined;
* sovereignty verification protocol is defined;
* acceptance thresholds are either evidence-backed or explicitly marked Requires Validation;
* no invented performance claims have entered the PRD;
* architecture questions are clearly separated from architecture decisions.

### Current assessment

**Requirement measurement framework: READY**

**Quantitative acceptance thresholds: NOT YET VALIDATED**

**Product definition: remains stable**

**Architecture selection: intentionally deferred**

---

# 52. Phase 5 Deliverables

Phase 5 produces the following artifacts:

1. **Quality Attribute Register**
2. **NFR Measurement Dictionary**
3. **Workflow Evaluation Specification**
4. **Evaluation Corpus Specification**
5. **Hardware Benchmark Specification**
6. **Reliability Test Specification**
7. **Retrieval Evaluation Specification**
8. **Multimodal/P&ID Evaluation Specification**
9. **Artifact Acceptance Specification**
10. **Security/Adversarial Test Specification**
11. **Sovereignty/Zero-Egress Verification Specification**
12. **Audit/Provenance Validation Specification**
13. **Threshold Register**
14. **Phase-5 Decision Register**
15. **Phase-5 Open Question Register**
16. **Architecture Input Register**

---

# 53. Final Phase-5 Conclusion

### Established

The Workbench now has a sufficiently mature product requirement structure to define **how quality must be measured**.

The remaining uncertainty is primarily empirical rather than conceptual.

The project already has the necessary foundations:

```text
Research
   ↓
Product Definition
   ↓
Workflows
   ↓
Requirements
   ↓
Quality Attributes
   ↓
Measurement
   ↓
Benchmark
   ↓
Acceptance
```

This is preferable to selecting an architecture first and discovering later that the system cannot satisfy the requirements.

NIST's current evaluation guidance similarly frames trustworthy AI evaluation around repeatable TEVV, measurement, uncertainty, benchmarking and documented results.

### Not yet established

The following must **not** be presented as product facts until measured:

* exact GPU;
* model sizes;
* latency;
* throughput;
* concurrency;
* workflow reliability percentage;
* retrieval accuracy;
* P&ID accuracy;
* artifact acceptance rate;
* code correctness rate;
* sandbox assurance level;
* prompt-injection success threshold;
* customer usability threshold.

### Phase-5 thesis

> **The Workbench should be qualified as an end-to-end evidence-governed execution system, not as a collection of individually impressive AI components.**

That is the critical transition from **requirements engineering** to **engineering qualification**.
