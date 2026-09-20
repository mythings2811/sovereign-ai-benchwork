# R7 — DATA & KNOWLEDGE RESEARCH

## 1. R7 Executive Finding

The biggest R7 finding is:

> **The Workbench does not primarily need a “knowledge base.” It needs a governed evidence system from which multiple knowledge representations can be derived.**

A conventional architecture:

```text
Documents
   ↓
OCR
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector DB
   ↓
LLM
```

is inadequate for this project.

The evidence from R5 + R6 + current R7 research supports:

```text
                         ORIGINAL SOURCES
                               │
                               ▼
                    Immutable Source Store
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
        Document Representation       Structured Extraction
                │                             │
                ▼                             ▼
       Evidence / Provenance Layer      Entity / Relation Layer
                │                             │
        ┌───────┼────────┬─────────┐          │
        ▼       ▼        ▼         ▼          ▼
      Lexical Semantic Visual   Structural   Knowledge Graph
        │       │        │         │          │
        └───────┴────────┴─────────┴──────────┘
                         │
                         ▼
                Governed Retrieval
                         │
                         ▼
                Evidence Sufficiency
                         │
                         ▼
                  Agent Reasoning
                         │
                         ▼
              Claim / Decision / Artifact
                         │
                         ▼
                 Provenance Graph
```

This is not overengineering for this product. It follows directly from the failure modes already established in R5: parsing errors, stale retrieval, wrong revisions, authorization leakage, missing evidence, P&ID topology errors and evidence/claim mismatch.

The research-control documents explicitly require R7 to inherit **technical approaches + workflows + failure + innovation findings**, rather than researching data in isolation. 

---

# 2. What Data Does the Workbench Actually Need?

I would divide the data into **six fundamentally different classes**.

| Data class                    | Examples                                                    | Primary purpose               | R7 decision      |
| ----------------------------- | ----------------------------------------------------------- | ----------------------------- | ---------------- |
| **Source artifacts**          | PDF, DOCX, XLSX, PPTX, image, email, code                   | Ground truth                  | Mandatory        |
| **Document structure**        | sections, tables, figures, coordinates, reading order       | Retrieval + evidence          | Mandatory        |
| **Enterprise metadata**       | owner, department, ACL, revision, effective date, authority | Governance                    | Mandatory        |
| **Structured domain data**    | equipment, tags, instruments, relationships, specifications | Engineering reasoning         | Strong Candidate |
| **Derived knowledge**         | entities, relations, rules, summaries, embeddings           | Retrieval/reasoning           | Derived only     |
| **Execution/evaluation data** | traces, verifier results, corrections, failures             | Routing + quality improvement | Mandatory        |

This distinction matters because **derived knowledge must never silently replace the source artifact**.

For example:

```text
P&ID.pdf
    ↓
Extracted pump P-101
    ↓
P-101 connected_to V-204
    ↓
Embedding
```

The final three objects are derived. The PDF remains the evidentiary root.

---

# 3. Source Data Strategy

## 3.1 Public data is sufficient for engineering R&D

There is now considerably more useful public engineering data than R6 had available.

### P&ID data

[PID2Graph dataset](https://zenodo.org/records/14803338?utm_source=chatgpt.com) provides P&IDs paired with graph structures, including symbol nodes, bounding boxes and line edges. The released archive is approximately **9.3 GB**. [PID2Graph dataset](https://zenodo.org/records/14803338?utm_source=chatgpt.com)

More importantly, the data problem has been attacked through topology-preserving synthesis.

[SynthPID](https://arxiv.org/abs/2604.16513?utm_source=chatgpt.com) reports 665 topology-preserving synthetic P&IDs and shows that topology-preserving synthetic generation substantially outperforms random template generation. Its experiments obtained **63.8% edge mAP using synthetic data alone**, versus approximately 33% for the cited template-synthetic baseline. [SynthPID](https://arxiv.org/abs/2604.16513?utm_source=chatgpt.com)

This is highly relevant to the Workbench because proprietary plant drawings cannot simply become an externally collected training corpus.

### Engineering diagrams

[Enginuity benchmark](https://arxiv.org/html/2606.03410v1?utm_source=chatgpt.com) provides engineering diagrams from publicly released U.S. military service and repair manuals, including diagram/parts-table pairs and domain-expert VQA.

### Industrial multimodal data

IRIS-v2 provides industrial scene imagery, point clouds, CAD information, pipe routing and P&ID data, giving another route to testing relationships between physical assets and engineering documentation.

**Conclusion:** Public datasets are sufficient for **algorithm development, regression testing and initial model selection**.

They are **not sufficient for production qualification** against an Indian refinery/PSU's actual document distribution.

---

# 4. The Real Production Dataset Must Be Customer-Owned

This is the critical R7 conclusion.

There is no realistic public dataset containing:

* an actual refinery's complete P&ID collection;
* its revision history;
* its internal SOP hierarchy;
* its engineering document dependencies;
* its proprietary tag conventions;
* its access-control structure;
* its historical MoC packages;
* its inspection records;
* its approval workflow;
* its actual organizational terminology.

Therefore:

> **The product's ultimate data advantage must come from customer-local evaluation and knowledge adaptation, not from attempting to acquire a giant universal training corpus.**

This also fits the sovereignty requirement: confidential customer data should remain inside the deployment.

The Workbench therefore needs two distinct data programs:

### A. Development data

Public + synthetic + internally authored.

Used for:

* parser development
* routing
* agent workflows
* sandbox testing
* retrieval mechanics
* benchmark infrastructure
* generic model evaluation.

### B. Customer adaptation/evaluation data

Customer-owned.

Used for:

* retrieval evaluation
* terminology
* authority hierarchy
* document classes
* P&ID conventions
* entity resolution
* workflow validation
* acceptance testing.

---

# 5. R7 Data Sources

## Tier 1 — Public authoritative / standards-based

Strongest sources for the knowledge schema:

* DEXPI
* ISO/IEC-related engineering standards where licensed/available
* IDTA/AAS
* ISA-related models
* OPC UA information models
* CFIHOS
* ISO 15926 reference concepts
* public government technical manuals.

DEXPI is particularly important.

[DEXPI specifications](https://dexpi.org/specifications/?utm_source=chatgpt.com) now describes **DEXPI 2.0**, covering standardized plant and process models, including P&IDs, and provides open specifications and supporting materials. [DEXPI specifications](https://dexpi.org/specifications/?utm_source=chatgpt.com)

This means we should **not invent a proprietary P&ID ontology from scratch**.

Use existing standards as semantic anchors and create a **Workbench-specific canonical layer above them**.

---

# 6. R7 Resolves the P&ID Representation Question

R6 asked:

> What representation is sufficient for P&ID reasoning?

The evidence is now strong enough to answer.

## Decision

### **Preferred representation: multimodal evidence + structured engineering graph**

Not:

* image only;
* OCR only;
* coordinates only;
* graph only.

Instead:

```text
P&ID
 │
 ├── original raster/PDF
 │
 ├── OCR text
 │
 ├── bounding boxes
 │
 ├── symbols
 │
 ├── tags
 │
 ├── lines
 │
 ├── junctions
 │
 ├── topology
 │
 ├── engineering attributes
 │
 ├── revision metadata
 │
 └── provenance
          ↓
     Engineering Graph
```

This conclusion is now supported by multiple directions of evidence.

[DEXPI](https://dexpi.org/specifications/?utm_source=chatgpt.com) explicitly models P&ID plant structure/topology and engineering objects.

[PID2Graph](https://zenodo.org/records/14803338?utm_source=chatgpt.com) provides graph-level P&ID ground truth.

And the very recent [Grounded and Faithful P&ID Reasoning](https://arxiv.org/abs/2609.05880?utm_source=chatgpt.com) reports a substantial improvement when VLM reasoning is constrained through a recovered evidence graph rather than relying on image-only reasoning.

### Therefore:

**Image = observation**

**OCR/layout = extracted evidence**

**Engineering graph = structural representation**

**Domain rules = semantic interpretation**

**Human engineer = consequential authority**

That is the correct hierarchy.

---

# 7. Minimum P&ID Graph

We can now answer another R6 question: *How much graph is enough?*

Do **not** build a complete digital twin.

The MVP minimum graph is:

```text
Entity
 ├── equipment
 ├── instrument
 ├── valve
 ├── piping segment
 ├── nozzle
 ├── junction
 ├── control element
 └── document region

Relationships
 ├── CONNECTS_TO
 ├── LOCATED_NEAR
 ├── HAS_TAG
 ├── PART_OF
 ├── FEEDS
 ├── CONTROLLED_BY
 ├── REFERENCES
 └── APPEARS_IN
```

Each relation needs:

```text
relation_id
source_entity
predicate
target_entity
confidence
source_document
source_revision
page
bounding_region
extraction_method
asserted_at
```

### Decision

**Strong Candidate → minimum structural graph.**

Do not implement a complete plant ontology in MVP.

---

# 8. Enterprise Knowledge Must Be Temporal

R5 established that semantic relevance can select obsolete documents.

R7 therefore resolves the data model question:

## A document needs more than a `version` field.

At minimum:

```text
document_id
revision_id
revision_number
effective_from
effective_to
issued_at
supersedes
superseded_by
status
authority_level
owner
source_system
```

For facts derived from documents:

```text
fact_id
valid_from
valid_to
asserted_at
source_revision
```

This gives us two different concepts:

### Valid time

When the fact was true in the enterprise.

### System/assertion time

When the Workbench learned or recorded the fact.

This is exactly the direction supported by current manufacturing knowledge-graph research, including work combining **SHACL + provenance + bi-temporal versioning + decision objects**.

[Composable Trust Infrastructure for Manufacturing Knowledge Graphs](https://arxiv.org/abs/2608.21418?utm_source=chatgpt.com)

### Decision

**Bi-temporal knowledge representation: Strong Candidate.**

For the MVP, implement the fields even if the underlying database remains relational/document-oriented.

---

# 9. Knowledge Is Not Automatically Truth

This is perhaps the most important R7 rule.

The Workbench should maintain:

```text
SOURCE
   ↓
EXTRACTED
   ↓
CANDIDATE
   ↓
VALIDATED
   ↓
APPROVED KNOWLEDGE
```

Never:

```text
SOURCE
   ↓
LLM extraction
   ↓
TRUTH
```

This follows the evidence failures from R5.

Current industrial KG research also supports validation before publication rather than discovering bad semantic objects after they have contaminated consumers.

### Proposed knowledge states

| State          | Meaning                                         |
| -------------- | ----------------------------------------------- |
| `RAW`          | Original source                                 |
| `PARSED`       | Machine-extracted representation                |
| `CANDIDATE`    | Derived entity/fact not yet validated           |
| `VALIDATED`    | Passed deterministic/semantic checks            |
| `APPROVED`     | Allowed into authoritative knowledge projection |
| `SUPERSEDED`   | Replaced by newer approved knowledge            |
| `CONFLICTED`   | Competing assertions                            |
| `UNVERIFIABLE` | Insufficient evidence                           |
| `REJECTED`     | Failed validation                               |

This is preferable to assigning one scalar `confidence` and pretending it means truth.

---

# 10. Provenance Architecture — R6 Question Solved

R6 asked:

> What should the canonical provenance representation be?

The answer is now reasonably clear.

Use **PROV-style provenance semantics**, but don't force the entire Workbench into RDF.

W3C PROV-O provides a standardized model for representing entities, activities, agents and derivations. [W3C PROV-O](https://www.w3.org/TR/prov-o/?utm_source=chatgpt.com)

DCAT 3 adds useful dataset/catalog concepts, including versioning and checksums. [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/?utm_source=chatgpt.com)

### Recommended internal model

```text
SourceArtifact
      │
      ▼
ProcessingActivity
      │
      ▼
EvidenceItem
      │
      ▼
DerivedFact
      │
      ▼
Claim
      │
      ▼
Decision
      │
      ▼
Artifact
```

Every edge should carry provenance.

Example:

```json
{
  "claim_id": "CLM-001",
  "claim": "P-101 feeds V-204",
  "supported_by": [
    {
      "document_id": "PID-001",
      "revision": "Rev-7",
      "page": 42,
      "bbox": [812, 430, 1140, 620],
      "evidence_type": "graph_edge",
      "source_hash": "..."
    }
  ]
}
```

### Decision

**Strong Candidate → provenance graph.**

But:

> **Do not make RDF/SPARQL a mandatory application-layer dependency in MVP.**

Use a canonical JSON/domain model internally and map it to PROV-compatible semantics where interoperability is required.

That is the simpler architecture.

---

# 11. R6 Context Compiler Question — Solved

The context compiler should preserve:

```text
claim
source
document
revision
page
region
entity
relationship
authority
validity
confidence
```

It should **not** simply summarize retrieved chunks.

### Proposed transformation

```text
Retrieved evidence
       ↓
Deduplicate
       ↓
Authority filtering
       ↓
Revision filtering
       ↓
Conflict detection
       ↓
Relationship expansion
       ↓
Salience selection
       ↓
Context compression
       ↓
Model context
```

Critically:

> Compression may remove wording, but must not remove the evidence identity.

Therefore:

```text
compressed_context
      +
evidence_ids
      +
source_map
```

must travel together.

### Decision

**Strong Candidate → provenance-preserving context compiler.**

---

# 12. R6 Evidence Sufficiency Question — Solved

We can now define evidence sufficiency without relying solely on an LLM.

## Evidence Sufficiency Gate

A query becomes answerable only if required predicates are satisfied.

For example:

```text
Question:
"What is the current pressure limit for P-101?"

Required:
✓ equipment resolved
✓ property resolved
✓ current revision found
✓ authoritative source found
✓ value extracted
✓ unit identified
✓ no unresolved conflict
```

Then:

```text
ALL REQUIRED CONDITIONS
        │
     satisfied?
     /       \
   YES        NO
   │           │
Reason      Retrieve / abstain
```

### Evidence states

```text
SUFFICIENT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
UNVERIFIABLE
```

This is much stronger than:

```text
retriever returned 5 chunks
```

### Decision

**Preferred architectural mechanism.**

---

# 13. R7 Chunking Finding

Do **not** choose one universal chunk size.

The data itself determines the retrieval unit.

Docling's current representation supports structural elements, headings, tables, figures, page numbers, hierarchical paths and provenance. Its native chunking can preserve this structure. [Docling document representation](https://docling-project-docling.mintlify.app/concepts/docling-document?utm_source=chatgpt.com)

Therefore:

### Recommended retrieval units

| Content           | Retrieval unit                 |
| ----------------- | ------------------------------ |
| SOP prose         | section/subsection             |
| Policy            | clause/section                 |
| Table             | table + row/column context     |
| Figure            | figure + caption + linked text |
| P&ID              | entity/relationship/region     |
| Spreadsheet       | sheet/table/range              |
| Email             | message/thread                 |
| Code              | file/function/class            |
| Calculation       | formula block + inputs         |
| Inspection report | finding/observation/section    |

### Decision

**Structure-aware chunking: Preferred.**

Token count becomes a **constraint**, not the definition of a knowledge unit.

---

# 14. Data Quality Model

R7 should establish a formal quality vector.

Not:

```text
document_quality = 0.91
```

Instead:

```text
Completeness
Accuracy
StructuralIntegrity
TemporalValidity
Authority
Authorization
Provenance
Consistency
Freshness
ExtractionConfidence
```

For example:

```text
EvidenceItem
 ├── completeness
 ├── extraction_confidence
 ├── source_authority
 ├── temporal_validity
 ├── authorization
 ├── structural_validity
 └── semantic_validation
```

This matters because a document can be:

* 99% OCR-complete,
* 100% authorized,
* but semantically wrong.

Or:

* semantically excellent,
* but obsolete.

One scalar cannot represent that.

---

# 15. Data Quality Gates

R7 should introduce **four ingestion gates**.

### Gate 1 — File integrity

```text
hash
format
size
readability
malware
duplicate
```

### Gate 2 — Structural integrity

```text
page count
reading order
table structure
coordinates
figure associations
OCR completeness
```

### Gate 3 — Enterprise metadata

```text
owner
classification
ACL
revision
authority
effective date
source system
```

### Gate 4 — Semantic integrity

```text
entity resolution
units
identifiers
relationships
domain constraints
contradictions
```

Only then:

```text
PUBLISH TO KNOWLEDGE PROJECTION
```

This matches the emerging industrial-KG pattern of schema/constraint validation before publication rather than cleaning a corrupted knowledge graph later.

---

# 16. Data Volume — An Important Correction

The Workbench does **not** need enormous data volume to prove its architecture.

The binding variable is **data heterogeneity and structural complexity**, not raw document count.

A corpus containing:

```text
5,000 clean PDFs
```

may be easier than:

```text
500 mixed:
PDF + scan + Excel + P&ID + DOCX + revisions + conflicting SOPs
```

For MVP evaluation, I would therefore optimize for a **representative corpus**, not a huge corpus.

### Suggested pilot corpus

```text
100–300 documents
+
20–50 difficult documents
+
10–20 P&IDs
+
10–20 spreadsheets
+
10–20 scanned reports
+
10–20 revision/conflict cases
+
10–20 cross-document workflows
```

These are **engineering targets, not externally validated requirements**.

Do not present them as market evidence.

---

# 17. R7 Public Dataset Portfolio

The useful dataset portfolio is now:

| Dataset/resource       | Use                                    | Status           |
| ---------------------- | -------------------------------------- | ---------------- |
| PID2Graph              | P&ID graph extraction                  | Strong Candidate |
| SynthPID               | synthetic P&ID training                | Strong Candidate |
| Enginuity              | engineering diagram VLM evaluation     | Strong Candidate |
| Industrial-Instruction | industrial technical QA                | Candidate        |
| EnterpriseRAG-Bench    | enterprise retrieval stress testing    | Strong Candidate |
| WorkSurface-Bench      | document/table/graph routing           | Strong Candidate |
| SeedRG methodology     | leakage-resistant benchmark generation | Strong Candidate |
| EnterpriseRAG          | noisy/gap/conflict retrieval           | Strong Candidate |
| Customer-local corpus  | production qualification               | **Mandatory**    |

The last item is the most important.

---

# 18. Synthetic Data — R7 Decision

R7 resolves another major issue:

> **Synthetic data should supplement scarce proprietary data, not pretend to replace it.**

The strongest evidence is SynthPID.

The key lesson isn't merely “synthetic data works.”

It is:

> **Synthetic data works when the generation process preserves the structure that matters in the target domain.**

Randomly generated P&IDs are structurally unrealistic.

Topology-preserving synthetic P&IDs are much more useful.

Therefore:

```text
Customer seed structure
        ↓
structure-preserving perturbation
        ↓
synthetic training examples
        ↓
public/general model development
```

This can potentially become a significant proprietary-data advantage **without exporting the original customer drawings**.

### Decision

**Strong Candidate: structure-preserving synthetic augmentation.**

---

# 19. Evaluation Corpus Must Be Frozen and Fingerprinted

This is a major R7 → R10 dependency.

Every evaluation needs:

```text
corpus_manifest_hash
document_hashes
chunking_version
parser_version
embedding_model
reranker
retrieval_configuration
knowledge_schema_version
model_version
prompt/workflow version
```

Otherwise:

```text
Evaluation A = 87%
Evaluation B = 91%
```

does not tell us whether the system improved.

The corpus may have changed.

Recent RAG research specifically identifies this corpus/evaluation contamination problem.

### Decision

**Mandatory.**

Add:

```text
EvaluationEnvironmentFingerprint
```

to the architecture.

---

# 20. R6 Model Routing — Solved Further by R7

R6 asked:

> Task-level, step-level or hierarchical routing?

The evidence now suggests:

## **Hierarchical routing**

Not one or the other.

```text
                 Task Router
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
       Simple      Complex     High-risk
          │          │           │
       small       adaptive    strong path
                    │
             Step Router
                    │
        ┌───────────┼──────────┐
        ▼           ▼          ▼
     retrieve     reason      verify
```

Why?

TRACE-Router shows the value of task-level routing for delayed task outcomes, while step-level work such as STEER and other adaptive approaches demonstrates that individual calls within a task can have different computational requirements. HW-Router additionally shows that routing must consider actual hardware state rather than static model size.

[TRACE-Router](https://arxiv.org/abs/2607.22465?utm_source=chatgpt.com)
[STEER](https://doi.org/10.1609/aaai.v40i37.40413?utm_source=chatgpt.com)
[HW-Router](https://arxiv.org/abs/2608.14575?utm_source=chatgpt.com)

### Final architecture

```text
Level 1:
Task classification

Level 2:
Workflow/capability routing

Level 3:
Step-level model selection

Level 4:
Verification-driven escalation
```

### Decision

**Strong Candidate → hierarchical routing.**

---

# 21. R6 Resource Prediction — Solved

R5 showed that VRAM is dynamic.

R7 now gives the router the necessary data.

The router should learn from:

```text
model
quantization
context length
input tokens
image count
image resolution
output tokens
concurrency
KV-cache pressure
model residency
GPU utilization
queue length
recent TTFT
recent TPOT
verification outcome
```

This is almost exactly the class of signals explored by HW-Router. [HW-Router](https://arxiv.org/abs/2608.14575?utm_source=chatgpt.com)

### Important correction

Do **not** attempt perfect prediction.

Use:

```text
predicted resource envelope
+
safety margin
```

and route based on:

```text
SAFE
MARGINAL
UNSAFE
```

### Decision

**Strong Candidate.**

---

# 22. Small Model Portfolio — R6 Question Solved

The evidence no longer supports:

> “Use one large model everywhere.”

Nor:

> “Use dozens of tiny specialists.”

The correct MVP portfolio is approximately:

```text
1 × primary reasoning model
1 × multimodal/document model
1 × small routing/verifier model
1 × OCR/layout specialist
1 × embedding model
1 × reranker
```

Some may be CPU-hosted.

Some may share infrastructure.

The exact model identities remain a benchmark question.

### Therefore:

**Architecture decision: multi-model.**

**Exact model portfolio: Requires Validation.**

This is an important distinction.

---

# 23. R6 Verification Question — Solved

R6 asked whether verification should be:

* deterministic;
* model-based;
* human.

Answer:

## **All three, in layers.**

```text
                    Output
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Deterministic              Semantic
   validation                 validation
          │                       │
          └───────────┬───────────┘
                      ▼
                Risk decision
                      │
              high consequence?
                /          \
              no            yes
              │              │
            release        human
```

### Deterministic validation

Use wherever possible:

* schema
* units
* numeric calculations
* file integrity
* required sections
* citations
* revision
* ACL
* formula validity
* graph constraints
* tool outcome contracts.

### Model verification

Use for:

* semantic consistency
* natural-language interpretation
* evidence support
* nuanced classification.

### Human

Use for:

* engineering approval
* safety
* regulatory decisions
* irreversible actions
* ambiguous evidence.

### Decision

**Preferred architecture.**

---

# 24. R6 “Derive, Don't Trust” — Solved

Do not let the agent write:

```text
status = "verified"
```

and accept that.

Instead:

```text
deterministic checks
+
evidence checks
+
semantic checks
+
policy checks
        ↓
DERIVED STATUS
```

Use:

```text
VERIFIED
DRIFT
CONFLICTED
INSUFFICIENT
UNVERIFIABLE
REJECTED
```

This should become a core data model rather than merely a UI feature.

---

# 25. R6 Proof-Carrying Execution — MVP Scope Resolved

R6 considered full proof-carrying execution.

The current evidence suggests the correct boundary.

Research such as [Proof-Carrying Agent Actions](https://arxiv.org/abs/2606.04104?utm_source=chatgpt.com) and [Proof of Execution](https://arxiv.org/pdf/2607.05397?utm_source=chatgpt.com) supports canonical action envelopes, authorization binding, outcome closure and replay-oriented evidence.

But:

> **Do not cryptographically prove the internal neural computation in MVP.**

Instead prove:

```text
WHO
WHAT
UNDER WHICH POLICY
USING WHICH AUTHORITY
WITH WHICH EVIDENCE
WHICH ACTION OCCURRED
WHAT RESULT OCCURRED
WHAT WAS VERIFIED
```

### Canonical action record

```text
Action
 ├── action_id
 ├── task_id
 ├── actor
 ├── capability
 ├── parameters_hash
 ├── policy_version
 ├── approval_id
 ├── evidence_ids
 ├── execution_environment
 ├── outcome
 ├── verification
 └── timestamp
```

### Decision

**Strong Candidate for MVP.**

Full cryptographic attestation:

**Later / high-assurance profile.**

---

# 26. R6 Security Context Continuity — Solved

Security context must travel with data.

Minimum:

```text
principal
role
session_id
task_id
classification
authorization_scope
source_permissions
purpose
policy_version
data_boundary
```

When data moves:

```text
retrieval
 ↓
context compiler
 ↓
LLM
 ↓
tool
 ↓
artifact
```

the relevant security context must not disappear.

This is particularly important because R5 established that authorization can fail **before** generation even when the final answer appears harmless.

Current authorization-first retrieval research supports enforcing authorization before learned retrieval components consume content.

### Decision

**Strong Candidate → security-context envelope.**

---

# 27. R6 Capability Graph — Solved

The agent should not see:

```text
500 tools
```

It should see a capability graph.

Example:

```text
READ_DOCUMENT
      │
      ├── SEARCH
      ├── EXTRACT_TABLE
      └── EXTRACT_ENTITY
              │
              ▼
        ANALYZE_DOCUMENT
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
   CALCULATE  VERIFY  SUMMARIZE
                         │
                         ▼
                   CREATE_REPORT
```

Each tool declares:

```text
inputs
outputs
permissions
side_effects
risk
resource_cost
verification
recovery_class
```

Then the planner can only compose compatible operations.

### Decision

**Strong Candidate.**

This is much safer than exposing arbitrary tool descriptions and asking the LLM to improvise.

---

# 28. R6 Dynamic Workflow Generation — Resolved

Do not choose between:

```text
fully fixed workflow
```

and:

```text
fully autonomous workflow generation
```

Use a **constrained workflow grammar**.

```text
Allowed operations:

RETRIEVE
PARSE
COMPARE
CALCULATE
VERIFY
ESCALATE
ASK
CREATE_ARTIFACT
REQUEST_APPROVAL
STOP
```

The planner may compose these.

It may **not invent arbitrary capabilities**.

Therefore:

```text
Dynamic planning
       +
bounded workflow grammar
       +
typed tools
       +
verification predicates
       +
hard execution limits
```

### Decision

**Strong Candidate.**

This resolves much of the reproducibility-vs-flexibility tension.

---

# 29. R6 Sovereignty Architecture — Partially Solved

The strongest sovereignty question cannot be completely solved by software alone.

There are levels:

### Level 1 — Application-local

```text
all models local
all data local
```

Insufficient as proof.

### Level 2 — Host-enforced

```text
application
+
network namespace
+
firewall
+
DNS controls
```

Much stronger.

### Level 3 — Independently observed

```text
host enforcement
+
packet capture
+
DNS monitoring
+
adversarial tests
```

Strong evidence.

### Level 4 — structurally impossible egress

Hardware/network architecture makes prohibited communication physically or logically impossible.

Highest assurance.

### MVP decision

**Level 2 + Level 3.**

Level 4 becomes:

**High-Assurance Deployment Research.**

This keeps the MVP realistic without weakening the sovereignty claim.

---

# 30. Consolidated R6 Open Question Resolution

| R6 question                        | Current answer                                       | Status                     |
| ---------------------------------- | ---------------------------------------------------- | -------------------------- |
| Task vs step routing               | Hierarchical                                         | **Strong Candidate**       |
| Resource prediction                | Runtime telemetry + learned envelope + safety margin | **Strong Candidate**       |
| Model portfolio                    | Small multi-model portfolio                          | **Architecture Preferred** |
| Exact model sizes                  | Benchmark required                                   | Requires Validation        |
| Evidence sufficiency               | Predicate-based gate                                 | **Preferred**              |
| P&ID representation                | Image + OCR/layout + engineering graph               | **Preferred**              |
| Minimum P&ID graph                 | Entities + topology + tags + provenance              | **Strong Candidate**       |
| Context compression                | Provenance-preserving compiler                       | **Strong Candidate**       |
| Verification                       | Deterministic + semantic + human                     | **Preferred**              |
| Completion predicate               | State-derived mandatory predicates                   | **Preferred**              |
| Provenance                         | Claim/evidence/action provenance graph               | **Strong Candidate**       |
| Proof-carrying execution           | Canonical action envelope, not neural proof          | **Strong Candidate**       |
| Security context                   | Propagating security envelope                        | **Strong Candidate**       |
| Capability graph                   | Typed capability dependency graph                    | **Strong Candidate**       |
| Dynamic workflows                  | Bounded workflow grammar                             | **Strong Candidate**       |
| Full KG                            | Not MVP                                              | **Rejected for MVP**       |
| Full cryptographic inference proof | Not MVP                                              | **Rejected for MVP**       |
| Physical/unidirectional air-gap    | High-assurance profile                               | Research Opportunity       |
| One universal parser               | No                                                   | **Rejected**               |
| Vector-only knowledge              | No                                                   | **Rejected**               |
| Single model                       | No                                                   | **Rejected**               |

---

# 31. The R7 Knowledge Architecture I Would Now Build

The accumulated evidence now supports a much clearer architecture:

```text
┌───────────────────────────────────────────────────────────┐
│                    SOURCE SYSTEMS                          │
│ PDF DOCX XLSX PPTX EMAIL CODE IMAGE P&ID ERP/PLM/etc.   │
└─────────────────────────┬─────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────┐
│                IMMUTABLE SOURCE STORE                     │
│ content hash • original artifact • metadata • ACL         │
└─────────────────────────┬─────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────┐
│              DOCUMENT / DATA PROCESSING                   │
│ parser • OCR • layout • table • VLM • spreadsheet parser  │
└─────────────────────────┬─────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────┐
│             CANONICAL EVIDENCE REPRESENTATION             │
│ text • table • figure • coordinates • page • source hash  │
│ revision • authority • provenance • extraction metadata   │
└───────────────┬───────────────────────────┬───────────────┘
                │                           │
                ▼                           ▼
       ┌─────────────────┐        ┌────────────────────┐
       │ Retrieval Views │        │ Knowledge Views   │
       │                 │        │                    │
       │ lexical         │        │ entities           │
       │ semantic        │        │ relations          │
       │ visual          │        │ rules              │
       │ structural      │        │ engineering graph  │
       └────────┬────────┘        └─────────┬──────────┘
                │                           │
                └──────────────┬────────────┘
                               ▼
                    ┌────────────────────┐
                    │ GOVERNANCE LAYER   │
                    │ ACL                 │
                    │ authority           │
                    │ revision            │
                    │ temporal validity   │
                    │ conflicts           │
                    │ evidence status     │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ RETRIEVAL ROUTER   │
                    │ text/table/graph/  │
                    │ visual selection   │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ CONTEXT COMPILER   │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ EVIDENCE GATE      │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ AGENT / MODEL      │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ VERIFICATION       │
                    └─────────┬──────────┘
                              ▼
                    CLAIM / ACTION / ARTIFACT
                              │
                              ▼
                    PROVENANCE / AUDIT GRAPH
```

---

# 32. What We Should NOT Build

R7 provides enough evidence to reject several tempting directions.

### Rejected

**1. Giant universal enterprise ontology**

Too expensive and unnecessary.

**2. Vector database as the knowledge layer**

Storage ≠ knowledge governance.

**3. LLM-generated knowledge directly entering the authoritative layer**

Unsafe.

**4. Universal fixed chunk size**

Data structures differ.

**5. Training a giant model on customer documents**

Not required for the core product and conflicts with the sovereignty/data-isolation philosophy.

**6. Full digital twin in MVP**

Massive scope expansion.

**7. Full enterprise knowledge graph before proving workflows**

Premature.

**8. Public datasets as production qualification**

Insufficient domain fidelity.

**9. Synthetic data as a substitute for customer validation**

Invalid.

**10. One confidence number**

Cannot represent authority, freshness, authorization and extraction quality simultaneously.

---

# 33. R7 Final Data Strategy

The Workbench should therefore have **three knowledge tiers**.

## Tier 1 — Evidence Vault

Authoritative.

```text
original files
hashes
revisions
ACL
metadata
provenance
```

Never rewritten by an LLM.

---

## Tier 2 — Derived Knowledge

Machine-generated.

```text
entities
relations
chunks
embeddings
graphs
summaries
rules
indexes
```

Rebuildable from Tier 1.

---

## Tier 3 — Operational Knowledge

Runtime-derived.

```text
claims
decisions
execution traces
verification
approvals
artifacts
corrections
```

Linked back to Tier 1 and Tier 2.

This separation is extremely important.

If an embedding model changes:

```text
Tier 2 rebuild
```

without destroying:

```text
Tier 1 evidence
```

If the ontology changes:

```text
Tier 2 re-materialize
```

If the model changes:

```text
Tier 3 evaluation changes
```

but historical execution evidence remains.

That gives the system **reproducibility and replaceability**, which are central project constraints.

---

# 34. R7 Established Findings

| ID      | Finding                                                                    | Status                                | Confidence  |
| ------- | -------------------------------------------------------------------------- | ------------------------------------- | ----------- |
| R7-EF01 | Source artifacts must remain immutable evidence roots                      | **Mandatory**                         | High        |
| R7-EF02 | Customer-local data is required for production qualification               | **Mandatory**                         | High        |
| R7-EF03 | Public datasets are sufficient for R&D/regression, not final qualification | **Established**                       | High        |
| R7-EF04 | Structure-preserving synthetic data is useful for scarce engineering data  | **Strong Candidate**                  | Medium-High |
| R7-EF05 | Documents require structured intermediate representation                   | **Preferred**                         | High        |
| R7-EF06 | P&IDs require engineering graph representation                             | **Preferred**                         | High        |
| R7-EF07 | Knowledge requires temporal/version semantics                              | **Strong Candidate**                  | High        |
| R7-EF08 | Provenance must exist at evidence/claim level                              | **Strong Candidate**                  | High        |
| R7-EF09 | Evidence sufficiency must be an explicit gate                              | **Preferred**                         | High        |
| R7-EF10 | Retrieval should expose multiple knowledge surfaces                        | **Preferred**                         | Medium-High |
| R7-EF11 | Chunking should follow document structure                                  | **Preferred**                         | High        |
| R7-EF12 | Knowledge states must distinguish candidate/validated/approved/conflicted  | **Preferred**                         | High        |
| R7-EF13 | Evaluation corpus must be fingerprinted                                    | **Mandatory**                         | High        |
| R7-EF14 | Security metadata must propagate with evidence                             | **Strong Candidate**                  | High        |
| R7-EF15 | Derived knowledge must remain rebuildable                                  | **Mandatory architectural principle** | High        |

---

# 35. Most Important Architectural Consequence

R4 originally looked roughly like:

```text
RAG + VLM + Agent + Tools + Verification
```

R5 showed why that is insufficient.

R6 added:

```text
adaptive routing
evidence gates
verification-aware planning
provenance
structured actions
```

R7 now reveals the underlying foundation:

> **All of those mechanisms depend on a canonical evidence/data layer.**

So the architecture should now be thought of as:

```text
                    SOVEREIGN AI WORKBENCH
                              │
              ┌───────────────┴───────────────┐
              │                               │
       INTELLIGENCE PLANE                EVIDENCE PLANE
              │                               │
       models / agents                 source / knowledge
       routing / planning              provenance / versions
       reasoning / tools               ACL / authority
       verification                    structures / graphs
              │                               │
              └───────────────┬───────────────┘
                              │
                       CONTROL PLANE
                              │
               policy / execution / audit
```

This is a stronger conceptual architecture than treating “RAG” as a subsystem.

---

# 36. Final R7 Thesis

The Workbench's competitive data architecture should be:

> **An immutable, provenance-aware, temporally governed evidence layer from which lexical, semantic, visual and structural knowledge projections are generated and selectively exposed to adaptive agents.**

That gives us a coherent answer to the R5 failures and R6 innovations:

```text
Bad parsing
→ evidence provenance

Stale retrieval
→ temporal knowledge

Wrong authority
→ authority metadata

ACL leakage
→ authorization-first retrieval

P&ID hallucination
→ engineering graph

Context overload
→ context compiler

Weak model
→ adaptive routing

False completion
→ state predicates

Bad verification
→ layered verification

Tool misuse
→ capability graph

Unverifiable execution
→ action/provenance envelope

Model replacement
→ rebuildable derived knowledge

Air-gap
→ local immutable evidence + offline supply chain
```

That is the real R7 result.

### Current architecture status

**We have now reduced the major R6 uncertainty substantially.** The remaining uncertainty is no longer primarily conceptual. It has moved into **empirical validation**:

1. exact model portfolio;
2. exact GPU/resource envelope;
3. exact retrieval engine;
4. exact embedding/reranker;
5. P&ID graph extraction accuracy on customer drawings;
6. customer-specific authority/version metadata quality;
7. evidence-gate thresholds;
8. actual end-to-end workflow accuracy.

Those should now be tested rather than debated.

**Next Action:** R8 should take this R7 data/evidence architecture as an input and stress-test it against **sovereignty, security, privacy, authorization, supply-chain, data classification, retention, audit and deployment requirements**—rather than reopening R4/R5/R6 technology discovery. This follows the defined research sequence: R7 passes its data requirements, sources, pipelines and quality constraints into R8. 
