# R6 — Innovation Research

**Objective:** Identify technically credible innovations that directly address the R4/R5 bottlenecks and could make the Sovereign Agentic AI Workbench more reliable, efficient, verifiable, and differentiated—without prematurely freezing implementation choices.

The R6 scope is explicitly to search for newer or unconventional mechanisms that overcome the failures discovered in R5, especially around adaptive routing, multimodal RAG, agentic document intelligence, verifiable execution, provenance, resource-aware orchestration, heterogeneous local models, and sovereignty verification.  The research sequence requires R6 to build on all previous streams, especially Technical and Failure Research. 

---

## R6-01 — Task-level and step-level adaptive model routing

### Research Stream

R6 — Innovation Research

### Research Topic

Adaptive local multi-model routing

### Research Question

Can the workbench select models dynamically according to task difficulty, execution state, resource conditions, and observed failure risk instead of assigning one model statically?

### Sources

OI-MAS, TRACE-Router, HW-Router, R2V-Agent, FLARE and related 2026 routing research.

### Source Type

Research papers / reproducible experimental studies.

### Key Finding

**FACT:** Recent routing research is moving from static request-level selection toward **state-aware, task-aware and hardware-aware routing**.

OI-MAS jointly selects agent roles and model scales according to the evolving reasoning state. Its experiments report substantial reductions in inference cost while maintaining or improving accuracy on its evaluated benchmarks.

TRACE-Router instead argues that for long-horizon agentic workflows, the routing decision should align with the **task-level feedback signal** rather than independently routing every model call. It binds all calls in a task to the selected backend and learns from delayed task-level reward.

HW-Router adds real-time hardware signals—queue lengths, KV-cache utilization, GPU state and recent serving latency—to model selection. In its two-GPU experiments, it reports large latency and SLO improvements relative to static routing baselines.

R2V-Agent goes further by routing **during execution**: a small model acts by default, a process verifier estimates residual risk, and a stronger model is invoked only when the calibrated risk crosses a threshold.

### Why This Matters

R5 established two independent constraints:

1. A larger model cannot simply be used for everything because of GPU/latency limits.
2. A small model can become dangerous when the task becomes harder after intermediate failures or ambiguous evidence.

Therefore the project's router should not be:

```text
task → choose model → execute
```

It should evolve toward:

```text
task
 ↓
initial capability/resource estimate
 ↓
model selection
 ↓
execute
 ↓
observe state + evidence + resource conditions
 ↓
risk estimate
 ├── continue
 ├── switch model
 ├── invoke specialist
 ├── verify
 └── escalate
```

### Project Relevance

Directly addresses the MVP's constrained-GPU requirement and R5's VRAM contention, false-completion and mid-trajectory failure findings. The project already requires automatic model/capability selection. 

### Implication

**Innovation Opportunity: Resource- and risk-aware local model router.**

The router should treat these as routing features:

```text
Task features
+
Capability requirements
+
Evidence modality
+
Current agent state
+
Failure history
+
GPU availability
+
KV-cache pressure
+
Model residency
+
Observed verifier confidence
```

This is more defensible than a router based only on prompt classification.

### Limitation

Most published routing experiments are not evaluated on the exact combination of:

* air-gapped deployment;
* multimodal technical documents;
* engineering/P&ID workloads;
* single mid-range GPU;
* local model switching.

Several reported gains are therefore evidence for the **mechanism**, not proof of project-level gains.

### Confidence

**High** for the innovation direction; **Medium** for expected improvement in this project.

### Open Question

Should routing operate at task level, step level, or use a hierarchical model:

```text
task-level commitment
        +
step-level escalation
        +
hardware-aware admission
```

---

# R6-02 — Calibration-aware escalation rather than raw confidence

### Research Topic

Uncertainty-driven local model collaboration

### Research Question

Can the workbench decide when a small model should ask a larger local model for help using calibrated risk rather than raw model confidence?

### Key Finding

**FACT:** R2V-Agent reports that residual failure risk can be estimated during an agent trajectory and used for selective escalation. UCCI shows that raw token uncertainty can be calibrated to error probability, and Conformal Cascade replaces arbitrary confidence thresholds with calibrated prediction-set based deferral in settings with finite answer spaces.

These approaches share an important principle:

> **Uncertainty should have operational semantics before it controls a routing decision.**

### Project Relevance

R5 showed that small models can become unreliable after:

* tool failures;
* bad retrieval;
* prompt injection;
* incomplete observations;
* accumulated reasoning errors.

A static “use 7B for simple tasks, 30B for hard tasks” policy cannot observe this transition.

### Innovation

Create a local **Escalation Controller**:

```text
Small model
    ↓
candidate action
    ↓
cheap verifier
    ↓
calibrated risk
    ├── low → accept
    ├── medium → local deliberation
    └── high → stronger local model
```

The middle state is important.

Instead of:

```text
small → large
```

use:

```text
small
 ↓
small + verifier
 ↓
small + specialist
 ↓
large
 ↓
human
```

### Advantage

This could conserve scarce VRAM while reserving the largest model for genuinely difficult states.

### Limitation

Calibration is distribution-sensitive. A calibrated router on generic benchmarks does not automatically remain calibrated on engineering documents, P&IDs or Indian enterprise terminology.

### Confidence

**Medium-High**

### Open Question

What project-specific calibration dataset is sufficient to establish safe escalation thresholds?

---

# R6-03 — Structure-aware multimodal RAG

### Research Topic

Multimodal agentic RAG

### Research Question

Can retrieval exploit document structure and visual evidence instead of treating a document as independent text chunks or page images?

### Key Finding

**FACT:** Several 2026 systems converge on a structural approach.

MM-BizRAG explicitly preserves document structure and separates retrieval representation from generation-time multimodal context.

LAD-RAG constructs a symbolic document graph containing layout and cross-page relationships and uses query-adaptive retrieval.

VLD-RAG combines sparse text retrieval and visual retrieval with consistency-aware fusion and a verifier-guided retrieval loop.

ViDoRe V3 shows that multimodal retrieval and visual grounding remain materially important for visually rich enterprise documents.

### Why This Matters

This directly attacks one of the strongest R5 failure modes:

```text
document
 ↓
independent chunks
 ↓
lost page/layout relationship
 ↓
wrong evidence selection
```

A more advanced representation is:

```text
Document
 ├── Page
 │    ├── section
 │    ├── paragraph
 │    ├── table
 │    ├── figure
 │    └── region
 │
 ├── cross-page relation
 ├── revision
 └── authority
```

### Innovation

Build a **dual/tri-representation retrieval layer**:

```text
                     Query
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       lexical       semantic      visual
          │            │            │
          └────────────┼────────────┘
                       ↓
               structural graph
                       ↓
             evidence selection
```

The graph should not necessarily become another large database. It can initially be a lightweight document-topology index containing:

* parent/child sections;
* page adjacency;
* table continuity;
* figure references;
* footnote links;
* revision relationships;
* source authority.

### Project Relevance

This directly supports engineering reports, manuals, SOPs, board documents and visually rich PDFs.

### Limitation

Graph extraction introduces another failure point. An incorrect graph can make retrieval worse.

### Confidence

**High**

### Open Question

Can a lightweight structural graph deliver most of the benefit without requiring a full enterprise knowledge graph?

---

# R6-04 — Evidence-gated retrieval

### Research Topic

Agentic document intelligence

### Research Question

Can the system determine that retrieved evidence is insufficient *before* the LLM generates a consequential answer?

### Source

TechRAG, VLD-RAG, SLEUTH and related evidence-density research.

### Key Finding

**FACT:** TechRAG explicitly introduces evidence sufficiency scoring and retrieval retries before answer generation. SLEUTH similarly focuses on constructing compact, evidence-dense multimodal contexts rather than simply passing large retrieved sets to a VLM.

### Innovation

Replace:

```text
retrieve top-k
 ↓
generate
```

with:

```text
retrieve
 ↓
evidence sufficiency test
 ├── sufficient → reason
 └── insufficient
       ↓
  reformulate / broaden / traverse
       ↓
  test again
```

A sufficiency test can use deterministic signals before an expensive model call:

```text
required entities present?
required time range covered?
required document class present?
conflicting evidence?
expected table/figure found?
minimum source count?
```

### Why It Matters

R5 explicitly identified missing evidence as a failure that should result in **NO SAFE ANSWER**, rather than model completion.

### Project Relevance

High for:

* MoC dependency analysis;
* inspection reports;
* SOP queries;
* engineering calculations;
* revision comparison.

### Innovation Status

**Strong Innovation Candidate**

This is more useful to the project than simply adding another retriever because it changes the **control semantics of retrieval**.

### Confidence

**High**

### Open Question

Can evidence sufficiency be largely deterministic, or must it depend on a learned local evaluator?

---

# R6-05 — Context compression as a first-class subsystem

### Research Topic

Long-document reasoning under constrained GPU

### Research Question

Can the workbench reduce multimodal context cost without losing the evidence needed for downstream reasoning?

### Key Finding

**FACT:** DocSLM demonstrates aggressive multimodal compression combined with streaming abstention for long documents. It reports substantially lower token use and latency than larger document VLM baselines.

SLEUTH similarly constructs compact evidence-dense multimodal contexts after retrieval.

AgentPack provides an independent implementation-oriented example of an offline document-to-context compiler using hierarchical maps and hybrid retrieval.

### Innovation

Introduce a local **Context Compiler**:

```text
raw retrieved evidence
        ↓
salience analysis
        ↓
duplicate elimination
        ↓
cross-page joining
        ↓
table/figure preservation
        ↓
evidence compression
        ↓
model-ready context
```

The key is that compression should preserve:

```text
claim
source
page
region
revision
relationship
```

rather than merely summarizing prose.

### Why It Matters

This attacks:

* long-context VRAM pressure;
* retrieval noise;
* model distraction;
* single-GPU constraints.

### Project Relevance

Very high.

### Limitation

Compression can itself become an information-loss mechanism. For technical documents, dropping one footnote or qualifier can invalidate the conclusion.

### Confidence

**High** for the mechanism; **Medium** for its safe application to engineering evidence.

### Open Question

What information must never be compressed in safety-critical engineering evidence?

---

# R6-06 — Visual retrieval as a complement to OCR, not an OCR replacement

### Research Topic

Vision-first document retrieval

### Research Question

Can visual retrieval recover information that OCR/text retrieval systematically misses?

### Key Finding

**FACT:** ViDoRe V3 reports that visual retrievers can outperform textual ones for some visually rich retrieval settings, while textual rerankers can still substantially improve final retrieval quality.

PULSAR demonstrates a production vision-first retrieval architecture using pooled late-interaction representations and reports substantial retrieval-efficiency improvements in a real enterprise setting.

### Innovation

Instead of deciding between:

```text
OCR retrieval
```

and

```text
visual retrieval
```

use:

```text
Text index
+
Visual index
+
Structural metadata
```

with selective invocation.

For example:

```text
Query
 ↓
Does query require:
  exact identifier? → text-first
  chart/figure/layout? → visual-first
  both? → hybrid
```

### Project Relevance

Particularly relevant to:

* P&IDs;
* engineering drawings;
* charts;
* slide decks;
* scanned reports;
* photographs.

### Limitation

Visual late-interaction indexes can be expensive in storage and computation. PULSAR's demonstrated production scale cannot be assumed for a single-GPU workstation.

### Confidence

**High**

### Open Question

Can compact visual representations such as NeoMME-style small encoders or pooled representations make visual retrieval practical on the project's hardware envelope?

---

# R6-07 — Small multimodal specialist models instead of one giant VLM

### Research Topic

Hybrid small-model/large-model local agents

### Research Question

Can several smaller specialized models outperform a single large VLM under the project's constrained hardware envelope?

### Key Finding

**FACT:** MACT demonstrates agent-wise specialization for visual document understanding, allocating different roles and adaptive compute to planning, execution, judgment and answer generation.

DocSLM demonstrates that smaller document-focused VLMs can provide competitive performance under substantially reduced token and parameter budgets.

LiteSearch-VL shows that trajectory distillation can transfer tool-use behavior into very small multimodal models, although its results also show that search behavior can improve without fully solving answer verification.

### Innovation

Rather than:

```text
30B VLM does everything
```

use:

```text
2–4B document/visual specialist
        +
3–8B reasoning model
        +
small OCR/layout model
        +
small verifier
        +
larger local model only on escalation
```

### Project Relevance

This may be the most important hardware-oriented innovation in the R6 stream.

### Potential Architecture

```text
               Task
                 ↓
        Resource-aware Router
                 ↓
       ┌─────────┼──────────┐
       ↓         ↓          ↓
   OCR/Layout   Vision    Reasoning
    specialist  specialist  model
       │         │          │
       └─────────┼──────────┘
                 ↓
              Verifier
                 ↓
         Strong model only
         when necessary
```

### Limitation

More models mean:

* more model files;
* more compatibility testing;
* more lifecycle management;
* more routing complexity.

### Confidence

**Medium-High**

### Open Question

What is the smallest useful collection of specialists that improves end-to-end performance without creating a maintenance problem?

---

# R6-08 — Verification-aware planning

### Research Topic

Self-verifying / verification-aware agents

### Research Question

Can the plan itself specify how each step will be verified before execution begins?

### Key Finding

**FACT:** VERIMAP integrates verification functions directly into task decomposition. Each planned node has structured I/O and planner-defined verification conditions.

POLARIS similarly represents enterprise workflows as typed DAGs with validators, compliance constraints and bounded repair.

MACT provides another related pattern: separate planning, execution, judgment and answer roles.

### Innovation

Move from:

```text
plan → execute → inspect
```

to:

```text
plan
 ↓
for every node:
   define expected output
   define preconditions
   define postconditions
   define validator
 ↓
execute
 ↓
verify
```

### Example

```text
Node: Extract inspection pressure

Input:
  inspection_report

Expected:
  pressure_value: float
  unit: enum
  source_page: integer

Validator:
  value exists
  unit valid
  page evidence present
  source hash matches
```

### Project Relevance

This directly solves R5's:

* false completion;
* tool-result corruption;
* malformed handoffs;
* verification blind spots.

### Innovation Status

**Very Strong Candidate**

This should probably become one of the central architectural innovations explored in R6.

### Confidence

**High**

### Open Question

How much planner-generated verification can be safely trusted, and which validators must come from fixed developer-defined rules?

---

# R6-09 — Proof-carrying execution

### Research Topic

Verifiable AI execution

### Research Question

Can every consequential agent action carry machine-verifiable evidence that it was authorized, executed and recorded correctly?

### Sources

Proof of Execution, Proof-Carrying Agent Actions, CAVA and related execution-verification research.

### Key Finding

**FACT:** Proof of Execution (PoE) formalizes an execution as a contract + causal event stream + replay context and checks authorization, path compliance, deny-side null effect, history integrity and replayability.

CAVA adds canonical action identity so semantically equivalent runtime representations can map to the same governed action.

PCAA similarly frames actions as certificate-bearing objects with admissibility, approval and outcome checkpoints.

### Important R5 Connection

R5 concluded:

> **The system cannot trust the agent's own assertion that an action succeeded.**

These innovations turn the record from:

```text
agent says: "I succeeded"
```

into:

```text
verifier derives:
authorized
+
action identity
+
execution evidence
+
outcome
```

### Innovation

Introduce a **Proof-Carrying Action Envelope**:

```text
Action
 ├── task
 ├── principal
 ├── capability
 ├── canonical action
 ├── inputs/hash
 ├── approval
 ├── tool execution
 ├── outputs/hash
 ├── side-effect class
 ├── validation
 └── evidence
```

Then:

```text
verdict = derived_from_checks(packet)
```

rather than reading a status field supplied by the agent.

### Project Relevance

Extremely high for:

* file writes;
* code execution;
* artifact release;
* approval workflows;
* internal-system actions.

### Limitation

Cryptographic execution proofs of full LLM inference remain substantially more expensive than ordinary application-level verification. zkAgent's current results demonstrate promising proof/verification performance but on substantially smaller models and controlled workloads than the project's eventual target.

### Confidence

**High** for the architectural pattern; **Medium** for full cryptographic verification of production-scale local LLM inference.

---

# R6-10 — Claim-to-evidence provenance graphs

### Research Topic

Provenance-aware AI agents

### Research Question

Can the workbench let a reviewer move from a final claim directly to the exact documents, regions, transformations and validation events supporting it?

### Key Finding

**FACT:** The LEDGER work proposes layered trace graphs connecting:

```text
claims
 ↕
workflow nodes
 ↕
evidence
 ↕
artifacts
 ↕
actions
```

The provenance survey likewise frames execution provenance as a typed graph linking retrieval, tool use, memory, evidence and decisions.

### Innovation

Create a first-class **Claim Graph**:

```text
Final claim
   ↓ supports
Evidence item
   ↓ extracted-from
Page region
   ↓ belongs-to
Document revision
   ↓ authorized-by
Policy/source authority
```

For generated artifacts:

```text
Artifact paragraph
      ↓
Claim
      ↓
Evidence
      ↓
Page / cell / drawing region
      ↓
Validation result
```

### Project Relevance

This is directly aligned with the project's auditability and verification requirements. 

### Potential Differentiation

This could make the workbench substantially more useful than generic private-chat systems because the deliverable becomes:

> **an artifact plus its evidence lineage**

rather than only an artifact.

### Limitation

LEDGER itself acknowledges that higher-level semantic graph construction can contain interpretation errors. Deterministic source anchors should therefore remain visible beneath any inferred semantic graph.

### Confidence

**High**

### Open Question

Which provenance relations should be deterministic and which can be model-inferred?

---

# R6-11 — Derive-don't-trust verification envelopes

### Research Topic

Self-verifying outputs

### Research Question

Can the system ensure that a successful status is computed from evidence rather than merely asserted by the agent?

### Key Finding

**FACT:** Proof Packets propose a small deterministic envelope where the verifier derives one of three statuses:

```text
Match
Drift
Unverifiable
```

rather than trusting a claimed status embedded in the packet.

This directly addresses R5's false-completion problem.

### Innovation

Adopt the same principle broadly:

```text
               Evidence
                  ↓
            deterministic checks
                  ↓
             derived verdict
```

Possible status lattice:

| Status           | Meaning                            |
| ---------------- | ---------------------------------- |
| **Verified**     | Required evidence/checks pass      |
| **Drift**        | Evidence contradicts claimed state |
| **Unverifiable** | Required evidence missing          |

### Project Relevance

Very high.

This semantic distinction is superior to a binary:

```text
success / failure
```

because enterprise AI frequently encounters **insufficient evidence**, which is not necessarily an execution error.

### Confidence

**High**

### Open Question

Can this three-state model be extended into a general evidence-status lattice for document, retrieval, tool and artifact verification?

---

# R6-12 — Security-context continuity across the complete execution path

### Research Topic

Sovereign agent architecture

### Research Question

Can authorization, provenance and policy context remain intact as a task passes through routing, retrieval, tools, sandbox and artifact generation?

### Key Finding

**FACT:** CONTINUITY identifies **security-context discontinuity** as a distinct failure class: individually correct controls can become ineffective when security context is dropped, widened or rebound at component boundaries.

Its proposed solution carries authenticated context through transitions using signed grants, provenance commitments, role-bound receipts, typed releases and effect-bound execution permits.

### Why This Is Important

R5 showed that:

```text
ACL correct
+
tool policy correct
+
sandbox correct
```

does not automatically imply:

```text
end-to-end execution secure
```

because the context connecting those controls may be lost.

### Innovation

Introduce a persistent **Execution Security Context**:

```text
Principal
Task
Authorization
Source provenance
Delegation
Policy state
Data sensitivity
Risk class
Approval state
```

This travels with the task rather than being reconstructed independently at each subsystem.

### Project Relevance

This could unify:

* retrieval permissions;
* model routing authorization;
* tool access;
* sandbox policy;
* artifact release;
* approval.

### Confidence

**High** as an architectural principle; **Medium** as a complete implementation because the cited work remains recent.

### Open Question

What minimum security-context fields must survive every internal API boundary?

---

# R6-13 — Sovereignty proof through elimination, not only observation

### Research Topic

Novel zero-egress architectures

### Research Question

Can sovereignty be strengthened by structurally removing communication capability rather than merely monitoring it?

### Key Finding

**FACT:** A recent sovereign-AI architecture research line studies receive-only / physically unidirectional communication, arguing that eliminating return channels can reduce the remote attack surface under an explicitly defined threat model.

This is much stronger than:

```text
network exists
+
firewall says deny
```

because it changes the architecture itself.

### Innovation Relevance

For the normal enterprise Workbench this is probably excessive.

But it suggests a differentiated **High-Assurance Sovereign Mode**:

```text
Normal Sovereign Mode
  → controlled LAN
  → default-deny egress
  → audited traffic

High-Assurance Mode
  → physically isolated compute
  → controlled inbound transfer
  → no return network path
```

### Project Relevance

Especially relevant to:

* defence-linked manufacturing;
* classified environments;
* strategic government workloads;
* highly sensitive engineering systems.

### Limitation

This is operationally much more difficult and may exceed MVP requirements. The relevant research is also architectural/theoretical rather than proof that this deployment model is commercially necessary for the target market.

### Confidence

**Medium**

### Status

**Research Opportunity, not MVP requirement**

### Open Question

Could a modular sovereignty architecture support both normal air-gapped enterprise mode and a physically one-way high-assurance mode without duplicating the software stack?

---

# R6-14 — Dynamic workflow generation

### Research Topic

Resource-aware agent orchestration

### Research Question

Can the execution workflow itself change according to task difficulty instead of using one static graph for all tasks?

### Key Finding

**FACT:** LAS, Dyserve, ReActNet and related work demonstrate that static workflows can waste compute and that dynamic scheduling can select only the necessary operators.

Dyserve formulates serving strategy selection over structured workflow subgraphs and considers model choice, verification, speculative execution and retry jointly.

LAS uses a lightweight gate and scheduler to decide whether to early-exit, verify, repair or reroute.

### Innovation

The workbench could maintain a **Workflow Grammar**:

```text
Allowed operations:
  retrieve
  inspect
  parse
  reason
  verify
  retry
  escalate
  approve
  artifact
```

Then dynamically instantiate:

```text
Task A:
retrieve → reason → artifact

Task B:
retrieve → parse → verify → reason → artifact

Task C:
parse → graph → verify → human approval
```

### Why This Matters

This could prevent the opposite failure of both:

* over-automation;
* under-verification.

### Project Relevance

Very high.

### Limitation

Dynamic workflows increase reproducibility and debugging complexity.

### Confidence

**Medium-High**

### Open Question

What constraints should make the dynamic workflow generator safe and auditable?

---

# R6-15 — Tool-schema graphs for local enterprise tools

### Research Topic

Reliable tool composition

### Research Question

Can the system plan tool chains using explicit schema dependencies rather than free-form tool descriptions?

### Key Finding

**FACT:** HyperAgent models tools as a Tool–Schema Hypergraph and dynamically derives support subgraphs according to unmet input requirements.

The important concept is:

```text
Tool A output schema
       ↓
Tool B required input schema
```

becomes an explicit machine-readable dependency.

### Innovation

Build a local **Capability Graph**:

```text
read_pdf
   ↓ produces
Document
   ↓ accepted by
extract_table
   ↓ produces
StructuredTable
   ↓ accepted by
calculate
   ↓ produces
Result
   ↓ accepted by
create_excel
```

The agent then reasons over **capabilities**, not merely tool names.

### Project Relevance

This directly strengthens R5's typed-tool/outcome-contract architecture.

### Potential Benefit

It can prevent the agent from proposing impossible or semantically invalid tool chains before execution.

### Confidence

**High** for mechanism; **Medium** for benefit on the exact workbench.

### Open Question

Can a capability graph be maintained automatically as new enterprise tools are installed?

---

# R6-16 — Local model collaboration without unrestricted multi-agent autonomy

### Research Topic

Heterogeneous model collaboration

### Research Question

Can multiple local models collaborate while keeping authority centralized?

### Key Finding

Current research increasingly uses specialized models for:

* planning;
* execution;
* judgment;
* retrieval;
* visual processing;
* verification.

However, R5 showed that every additional agent creates another possible failure boundary.

### Innovation

Use:

```text
central orchestrator
      │
      ├── Vision Specialist
      ├── Retrieval Specialist
      ├── Coding Specialist
      ├── Reasoning Specialist
      └── Verification Specialist
```

but **only the central execution authority can produce effectful actions**.

This combines specialization with the R5 principle of avoiding privilege collapse.

### Relevance

High.

### Important Distinction

Do not build:

```text
agent A can spawn arbitrary agent B
agent B can spawn C
...
```

Instead:

```text
orchestrator
 ↓
declared specialist
 ↓
typed result
 ↓
central verifier
```

### Confidence

**Medium-High**

### Open Question

What is the maximum useful number of specialists before coordination cost exceeds capability gains?

---

# R6 Innovation Synthesis

The research does **not** suggest that the workbench should become a giant multi-agent platform with dozens of emerging components.

The stronger pattern is a much tighter architecture:

```text
                     ┌──────────────────────┐
                     │   USER WORKBENCH     │
                     └──────────┬───────────┘
                                ↓
                     Security Context
                                ↓
                       Task / Risk Analysis
                                ↓
                   Resource + Capability Router
                                ↓
                    Dynamic Workflow Planner
                                ↓
              ┌─────────────────┼──────────────────┐
              ↓                 ↓                  ↓
        Text/RAG path      Visual path       Tool path
              │                 │                  │
              └───────────────┬─┴──────────────────┘
                              ↓
                   Evidence / Context Compiler
                              ↓
                    Evidence Sufficiency Gate
                         ┌────┴─────┐
                         ↓          ↓
                       PASS       FAIL
                         ↓          ↓
                     Reason      Retrieve again
                         ↓
                  Process Verification
                         ↓
                 Model Escalation if needed
                         ↓
                  Typed Action Execution
                         ↓
                  Independent Verification
                         ↓
                 Proof / Provenance Envelope
                         ↓
                 Deterministic Artifact Engine
                         ↓
                   Approval / Release Gate
                         ↓
              Tamper-Evident Audit / Sovereignty
```

This is an **innovation direction**, not yet the final architecture.

---

# R6 Established Findings

## EF-01 — Adaptive routing has moved beyond simple prompt classification

Current research supports routing based on evolving task state, resource conditions and residual risk rather than only initial prompt characteristics.

**Project effect:** strengthen the R4 Model Gateway into a resource/risk-aware control layer.

---

## EF-02 — Evidence sufficiency should be a first-class decision

Recent multimodal/technical RAG work increasingly inserts evidence assessment and retrieval refinement before final generation.

**Project effect:** implement evidence-gated retrieval rather than fixed top-k retrieval alone.

---

## EF-03 — Structure-aware multimodal retrieval is a meaningful improvement direction

Document structure, layout, visual evidence and cross-page relationships can materially improve retrieval over naïve independent chunks.

**Project effect:** investigate a structured document graph alongside lexical/vector/visual indices.

---

## EF-04 — Small specialized models can be strategically valuable under constrained hardware

Recent document/VLM research supports procedural specialization and multimodal compression rather than relying exclusively on larger monolithic models.

**Project effect:** evaluate a heterogeneous local model portfolio rather than one “best” VLM.

---

## EF-05 — Verification-aware planning is stronger than post-hoc checking alone

VERIMAP/POLARIS and related approaches show value in specifying expected outputs and verification conditions during planning.

**Project effect:** every consequential workflow node should ideally have explicit verification semantics.

---

## EF-06 — Execution provenance can become an active control mechanism

Proof-of-execution and proof-carrying-action work shifts provenance from passive logging toward a machine-checkable execution object.

**Project effect:** the audit layer could evolve into **verifiable execution**, not merely observability.

---

## EF-07 — Claim-to-evidence graphs are more useful than raw execution logs for human audit

A reviewer needs to trace a claim back to its evidence and workflow lineage.

**Project effect:** build claim/evidence provenance as a first-class UX and data structure.

---

## EF-08 — Security controls must preserve context across boundaries

Security-context continuity is an emerging architectural problem in composable agent systems.

**Project effect:** identity, policy, provenance and sensitivity should travel with the execution rather than being independently reconstructed.

---

## EF-09 — Sovereignty can be strengthened architecturally

Physical or cryptographic elimination of communication paths can provide stronger guarantees than monitoring alone under appropriate threat models.

**Project effect:** investigate a high-assurance sovereignty profile without making it an MVP assumption.

---

# Relevant Findings

| Innovation                        | R5 failure addressed            |                 Project value | Status                   |
| --------------------------------- | ------------------------------- | ----------------------------: | ------------------------ |
| Resource-aware model routing      | GPU contention                  |                     Very High | **Strong Candidate**     |
| Risk-calibrated escalation        | mid-task model failure          |                     Very High | **Strong Candidate**     |
| Evidence-gated RAG                | missing/wrong evidence          |                     Very High | **Strong Candidate**     |
| Structure-aware multimodal RAG    | cross-page/layout failure       |                     Very High | **Strong Candidate**     |
| Context compiler/compression      | VRAM + noisy context            |                     Very High | **Strong Candidate**     |
| Small multimodal specialists      | constrained GPU                 |                          High | **Candidate**            |
| Verification-aware planning       | false completion/handoff errors |                     Very High | **Strong Candidate**     |
| Proof-carrying action             | untrusted logs                  |                     Very High | **Candidate**            |
| Claim/evidence provenance graph   | audit complexity                |                     Very High | **Strong Candidate**     |
| Derive-don't-trust verifier       | false status                    |                     Very High | **Strong Candidate**     |
| Security-context continuity       | privilege/policy discontinuity  |                     Very High | **Candidate**            |
| Capability/tool schema graph      | tool misuse                     |                          High | **Strong Candidate**     |
| Dynamic workflow generation       | unnecessary compute             |                          High | **Candidate**            |
| Physical one-way sovereignty mode | zero-egress assurance           | High for special environments | **Research Opportunity** |

---

# Rejected / Inadequate Innovation Directions

### RI-01 — “Just use a larger model”

**Rejected.**

R5 demonstrates that model scale does not eliminate retrieval, tool, provenance, authorization and environmental failures. Recent routing research reinforces this distinction.

### RI-02 — “Use multi-agent debate everywhere”

**Rejected.**

Debate adds compute and another coordination surface. It should be selectively activated when uncertainty justifies it.

### RI-03 — “Use visual RAG instead of OCR”

**Rejected.**

Current evidence supports complementary textual and visual retrieval, not complete replacement of structured parsing.

### RI-04 — “Make every execution cryptographically proven”

**Not appropriate as an MVP blanket requirement.**

Full cryptographic proof of large-model inference remains substantially more expensive and technically immature relative to ordinary runtime verification.

### RI-05 — “Let the workflow generate arbitrary tools”

**Rejected.**

The innovation should increase adaptive behavior *inside a bounded capability graph*, not expand the authority surface without control.

### RI-06 — “Use a full enterprise knowledge graph from day one”

**Rejected as premature.**

The evidence supports structural graphs, but the project should first establish which graph relationships actually produce measurable retrieval/reasoning gains.

---

# Failure / Risk Findings from R6

The innovation layer introduces its own risks.

### Risk 1 — Router misclassification

A resource-aware router could send a consequential task to a weak model.

**Required control:** calibrated escalation + risk thresholds + high-consequence routing policy.

### Risk 2 — Verification circularity

The same model generating an answer and judging its own answer can share the same blind spot.

**Required control:** deterministic validators and independent specialist/verifier paths where possible.

### Risk 3 — Graph contamination

Incorrect document/tool graphs can create systematic retrieval errors.

**Required control:** graph provenance, deterministic anchors and graph-quality benchmarks.

### Risk 4 — Compression destroys qualifiers

Context compression can remove the one footnote or amendment that determines correctness.

**Required control:** preserve high-risk evidence classes losslessly.

### Risk 5 — More specialists increase operational complexity

A heterogeneous model architecture increases model lifecycle and routing complexity.

**Required control:** start with a small capability portfolio and keep all models behind one Model Gateway.

### Risk 6 — Dynamic workflows reduce reproducibility

Changing execution topology can make incident reconstruction harder.

**Required control:** record the generated workflow graph and routing decisions as part of execution provenance.

---

# Open Questions

1. What routing granularity is optimal for the Workbench: task, step, or hierarchical?
2. Which local uncertainty signals remain calibrated on engineering documents?
3. Can evidence sufficiency be determined mostly through deterministic rules?
4. What minimum structural graph is useful for P&IDs and technical documents?
5. Can small multimodal models materially outperform a single larger model under the exact mid-range-GPU constraint?
6. Which context-compression operations are provably lossless for critical evidence?
7. How much verification can be deterministic?
8. Can a proof-carrying action envelope become the canonical internal execution object?
9. Which provenance relations must be cryptographically bound?
10. What security context must persist across every internal service boundary?
11. What is the minimum viable capability graph for local enterprise tools?
12. When does dynamic workflow generation improve performance enough to justify its reproducibility cost?
13. What high-assurance sovereignty architecture is appropriate for defence/government deployments?

---

# Architecture / Engineering Questions Passed to R7

R6 should pass **questions**, not final implementation decisions, in accordance with the research methodology. 

### Model / inference

* Can the router predict peak resource demand accurately enough for admission control?
* What local model portfolio covers reasoning, coding, vision and verification?
* Can small-model → verifier → large-model escalation reduce GPU pressure without increasing high-severity errors?

### Retrieval

* What document graph primitives materially improve retrieval?
* What hybrid text/visual/structural retrieval architecture fits the storage budget?
* Can evidence sufficiency be formalized as executable predicates?

### Multimodal

* Can a small visual retriever replace expensive VLM passes for initial search?
* What information should remain in image form versus structured form?
* What representations preserve engineering drawing topology?

### Agent runtime

* Can every plan node have explicit preconditions/postconditions?
* Which failures should cause retry, escalation, replanning or human approval?
* How can dynamic workflow generation remain auditable?

### Verification

* Which checks are deterministic?
* Which require an independent model?
* Which require human approval?
* Can verification status be represented as `Verified / Drift / Unverifiable`?

### Provenance

* What is the canonical claim-to-evidence representation?
* What execution information must be hash-bound?
* How should replay and provenance interact?

### Sovereignty

* What evidence proves that the complete execution stayed within the boundary?
* What additional assurance is achieved by hardware/physical communication elimination?
* Can normal and high-assurance sovereignty modes share one software architecture?

---

# R6 Final Assessment

The most significant innovation opportunity is **not another model, vector database or agent framework**.

It is the transition:

```text
AI assistant
```

to

```text
adaptive, evidence-gated, verifiable execution system
```

with four distinctive properties:

### 1. Adaptive intelligence

The system dynamically chooses:

```text
which model
which specialist
which workflow
how much compute
when to verify
when to escalate
```

rather than using a static chain.

### 2. Evidence-bounded intelligence

The system knows the difference between:

```text
evidence supports claim
evidence conflicts with claim
evidence is insufficient
```

rather than treating retrieval as context stuffing.

### 3. Verifiable execution

The agent does not get to declare:

> “I completed the task.”

The runtime derives whether the task was completed from:

```text
authorization
+
actions
+
evidence
+
outputs
+
validation
```

### 4. Sovereignty as an engineering property

The system does not merely say:

> “Your data is private.”

It produces technical evidence showing:

```text
what entered
what model ran
what data was retrieved
what tools executed
what artifacts were created
what policy applied
what network paths existed
what traffic was observed
what was verified
```

This direction is tightly aligned with the original product vision: a self-hosted execution environment combining local models, model selection, agentic execution, local knowledge, multimodal processing, tools, artifacts, verification, auditability and demonstrable sovereignty.  

**R6 therefore establishes a credible innovation thesis:**

> **The Workbench should compete not by being a private chatbot, but by making local AI execution adaptive, evidence-bounded, failure-aware, and independently verifiable under severe sovereignty and hardware constraints.**

The next stream, **R7 — Data Research**, should now determine what documents, datasets, annotations, enterprise metadata, evaluation corpora, provenance records and data-quality mechanisms are required to make these innovations actually work. 
