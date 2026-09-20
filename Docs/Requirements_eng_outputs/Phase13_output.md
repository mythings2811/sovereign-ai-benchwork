# SOVEREIGN AGENTIC AI WORKBENCH

## PHASE 13 — DATA & KNOWLEDGE ARCHITECTURE SPECIFICATION

**Phase:** 13  
**Predecessor:** Phase 12 — Component Architecture  
**Successor:** Phase 14 — Data Model & Schema Design  
**Status:** **DATA & KNOWLEDGE ARCHITECTURE BASELINE ESTABLISHED — READY FOR DETAILED DATA DESIGN**  
**Primary domain:** Enterprise Data, Knowledge, Evidence, Retrieval and Provenance

---

# 1. Objective

The objective of Phase 13 is to establish the logical data and knowledge architecture of the Sovereign Agentic AI Workbench.

The architecture must answer:

> What information exists in the system, what each information object means, how objects relate to one another, who owns them, how they are created and transformed, how authorization and classification propagate, how validity is determined, how retrieval operates, how evidence becomes usable for reasoning, and how important outputs can be traced back to organizational sources?

The architecture must support:

```text
SOURCE
  ↓
DOCUMENT
  ↓
REVISION
  ↓
REGION / LOCATION
  ↓
EXTRACTED INFORMATION
  ↓
EVIDENCE
  ↓
DERIVED INFORMATION
  ↓
CLAIM
  ↓
RESULT
  ↓
ARTIFACT
```

This chain is authoritative for the knowledge architecture.

Retrieval is a mechanism within this architecture, not the architecture itself.

---

# 2. Phase Boundary

## 2.1 Phase 13 determines

- logical data concepts;
- entities and relationships;
- information ownership;
- source and document identity;
- revision semantics;
- temporal validity;
- authorization propagation;
- classification propagation;
- extraction representations;
- evidence representation;
- derived-information representation;
- claim representation;
- result and artifact lineage;
- provenance events;
- retrieval representations;
- indexing projections;
- evidence bundles;
- conflict representation;
- ingestion lifecycle;
- knowledge update lifecycle;
- deletion and revocation semantics;
- data quality;
- consistency requirements;
- cache constraints;
- data-governance rules.

## 2.2 Phase 13 does not freeze

- exact SQL tables;
- exact vector-database collections;
- exact object-storage implementation;
- framework-specific classes;
- application source code;
- ORM mappings;
- physical partitioning;
- final index configuration;
- production retention periods;
- customer-specific classification taxonomies.

Those belong to detailed data design and deployment qualification.

---

# 3. Architectural Authority

Phase 13 inherits the following authority:

1. Final PRD
2. Final SRS
3. Product decisions
4. Phase 10 System Architecture
5. Phase 11 Technology Selection
6. Phase 12 Component Architecture
7. Research evidence
8. Security qualification requirements

The Phase 9 SRS establishes that the system must preserve source identity, authority, revision, temporal validity, authorization, provenance and evidence state, and that retrieval relevance cannot substitute for authorization.

Phase 10 establishes the same principle architecturally:

> indexes are projections of governed evidence rather than the authoritative knowledge layer.

---

# 4. Design Principles

## DK-01 — Source Is Not Document

A source identifies the origin of information.

A document identifies the logical information object.

A source may contain many documents.

---

## DK-02 — Document Is Not Revision

A document represents logical identity.

A revision represents a particular version of that document.

The newest revision is not automatically the authoritative revision.

---

## DK-03 — Extraction Is Not Evidence

OCR, parsing, vision and structural extraction produce representations.

They do not automatically establish truth.

---

## DK-04 — Evidence Is First Class

Evidence is the governed unit that can legitimately support reasoning, claims and decisions.

---

## DK-05 — Retrieval Is a Projection

Search indexes, embeddings and reranking structures are derived projections.

They cannot become the authoritative knowledge store.

---

## DK-06 — Authorization Precedes Reasoning

Unauthorized information must not reach model reasoning merely because retrieval found it.

---

## DK-07 — Classification Propagates

Derived information must not automatically receive a lower classification than its source.

---

## DK-08 — Provenance Is Preserved Through Transformation

Every material transformation must retain lineage to its inputs.

---

## DK-09 — AI-Derived Information Is Not Automatically Authoritative

Model output is derived information unless independently established otherwise.

---

## DK-10 — Conflicts Are Represented

The system must not silently collapse contradictory evidence or claims.

---

## DK-11 — Temporal Validity Is Independent of Revision

"Latest" and "valid at time T" are different queries.

---

## DK-12 — Data and Instructions Remain Distinct

Instructions embedded inside documents remain untrusted content and cannot modify control-plane authority.

---

## DK-13 — Deletion Does Not Necessarily Mean Provenance Destruction

Retention, legal hold, audit and provenance requirements may outlive source availability.

---

## DK-14 — Knowledge State Is Separate From Search State

An index can be stale while canonical evidence remains valid.

---

# 5. Canonical Knowledge Object Model

The canonical logical model is:

```text
Source
  │
  └── Document
        │
        └── Revision
              │
              ├── Region
              │
              └── Extracted Information
                      │
                      └── Evidence
                            │
                            └── Derived Information
                                  │
                                  └── Claim
                                        │
                                        ├── Result
                                        │
                                        └── Artifact
```

Cross-cutting relationships:

```text
Authorization
Classification
Authority
Temporal Validity
Verification
Provenance
Conflict
Processing
Audit
```

These are not optional annotations. They are architectural relationships.

---

# 6. SOURCE MODEL

## 6.1 Definition

A `Source` represents the origin from which organizational information enters or is made available to the workbench.

Examples:

- uploaded file;
- directory;
- shared drive;
- document-management system;
- database;
- enterprise repository;
- engineering system;
- archive;
- approved export;
- controlled external reference.

## 6.2 Logical attributes

```text
Source
├── source_id
├── source_type
├── source_system
├── source_locator
├── owner
├── authority_profile
├── authorization_scope
├── classification
├── ingestion_method
├── source_timestamp
├── status
├── trust_profile
└── provenance
```

## 6.3 Source identity

Filename alone is insufficient.

Identity should use an appropriate combination of:

- organizational identifier;
- source identifier;
- document identifier;
- content hash;
- metadata;
- source location;
- manual identity resolution where required.

The architecture must distinguish:

```text
same logical document
```

from:

```text
different document
```

even when filenames are identical.

---

# 7. DOCUMENT MODEL

A `Document` is the logical information object associated with a source.

```text
Document
├── document_id
├── source_id
├── title
├── document_type
├── owner
├── classification
├── authorization_scope
├── domain
├── document_family
├── lifecycle_state
└── creation_metadata
```

A document may have zero, one or many revisions.

```text
Document
 ├── Revision A
 ├── Revision B
 ├── Revision C
 └── Revision D
```

The document identifier must remain stable across revisions wherever organizational semantics establish that the object is the same logical document.

---

# 8. REVISION MODEL

A `Revision` represents a specific version of a logical document.

```text
Revision
├── revision_id
├── document_id
├── source_version
├── revision_label
├── content_hash
├── publication_date
├── effective_date
├── superseded_date
├── approval_state
├── authority
├── validity
├── ingestion_timestamp
└── provenance
```

## 8.1 Revision states

Conceptually:

```text
DRAFT
PENDING_APPROVAL
CURRENT
SUPERSEDED
OBSOLETE
WITHDRAWN
UNKNOWN
```

The exact customer taxonomy remains configurable.

## 8.2 Critical rule

The architecture shall **not** implement:

```text
newest timestamp = authoritative
```

Authority may depend on:

- formal approval;
- organizational revision;
- effective date;
- withdrawal;
- applicability;
- document type;
- business rules.

---

# 9. TEMPORAL MODEL

Temporal validity is represented independently.

The system should distinguish:

```text
created_at
published_at
effective_from
effective_until
observed_at
ingested_at
used_at
superseded_at
```

This permits queries such as:

> What was the applicable engineering information on date T?

rather than merely:

> What is the newest document?

## 9.1 Temporal dimensions

At minimum:

### Valid time

When the information is applicable in the organization or real world.

### System time

When the system observed, ingested or recorded the information.

This supports a future bi-temporal implementation without forcing one physical database model in Phase 13.

---

# 10. REGION / LOCATION MODEL

A `Region` identifies where information occurs within a representation.

Possible hierarchy:

```text
Document
  ↓
Revision
  ↓
Page
  ↓
Section / Table / Region
  ↓
Bounding Box
  ↓
Element
```

For text:

- page;
- paragraph;
- section;
- table;
- row;
- column;
- cell.

For visual material:

- page;
- bounding box;
- coordinates;
- region;
- detected object;
- spatial relationship.

## 10.1 Location stability

Page numbers and coordinates may change after reprocessing.

Therefore evidence location should contain:

- representation identity;
- representation version;
- location coordinates;
- source-region relationship;
- stable element identifier where possible;
- content hash where useful.

A reprocessed representation must not silently invalidate historical provenance.

---

# 11. EXTRACTED INFORMATION

`ExtractedInformation` represents a machine-produced representation of source material.

Examples:

- OCR text;
- table;
- detected equipment;
- detected tag;
- symbol;
- line;
- paragraph;
- numerical value;
- image region;
- layout structure;
- spatial relationship.

The architectural distinction is:

```text
Extracted Information
        ≠
Evidence
```

For example:

```text
OCR:
"Pressure = 12.4 bar"
```

is an observation.

It becomes governed evidence only after the relevant source, revision, location, authorization, authority, applicability and provenance conditions have been established.

---

# 12. EXTRACTION PROVENANCE

Every material extraction shall preserve:

```text
Source
↓
Source Region
↓
Processing Operation
↓
Extractor
↓
Extractor Version
↓
Representation
```

Metadata includes where applicable:

- parser;
- OCR engine;
- VLM;
- extraction model;
- preprocessing;
- configuration;
- software version;
- model version;
- timestamp;
- source region;
- transformation identity.

This permits reconstruction of how a representation was produced.

---

# 13. REPRESENTATION MODEL

One source may have multiple representations:

```text
Raw File
 ├── Native Structure
 ├── OCR Text
 ├── Layout
 ├── Tables
 ├── Images
 ├── Image Regions
 ├── Entities
 ├── Relationships
 ├── Engineering Structure
 └── Embeddings
```

These representations are related views of the same source, not independent facts.

Each representation therefore requires:

```text
representation_id
parent_source/revision
representation_type
representation_version
content_hash
processing_provenance
```

---

# 14. RAW SOURCE PRESERVATION

The canonical architecture should preserve the original source where policy permits.

The source vault should support:

- content hash;
- integrity checking;
- access control;
- version association;
- retention;
- deletion state;
- archival state;
- provenance.

The system should be able to determine:

```text
Which source produced this representation?
Which processing pipeline produced this representation?
Which representation produced this evidence?
```

where required by policy.

---

# 15. ENGINEERING DOMAIN REPRESENTATION

For P&IDs and engineering drawings, the data model separates:

```text
Observed Visual Information
        ↓
Extracted Entity
        ↓
Spatial Relationship
        ↓
Structural Connectivity
        ↓
Interpreted Engineering Information
        ↓
Verified Engineering Fact
```

Candidate engineering entities include:

- equipment;
- instrument;
- line;
- valve;
- tag;
- connection;
- relationship;
- topology;
- spatial relation;
- engineering attribute.

The system must never collapse:

```text
visual recognition
```

into:

```text
verified engineering truth
```

The Phase 10 architecture explicitly requires visual observations, extracted entities, spatial relationships, structural connectivity, engineering interpretation and consequential conclusions to remain separate.

---

# 16. EVIDENCE MODEL

`Evidence` is the central governed knowledge object.

Conceptually:

```text
Evidence
├── evidence_id
├── source_reference
├── document_reference
├── revision_reference
├── location_reference
├── representation_reference
├── content
├── authority
├── authorization
├── classification
├── temporal_validity
├── applicability
├── extraction_context
├── provenance
├── verification_state
├── conflict_state
└── quality_state
```

Evidence represents information that the system is willing to use as support for reasoning under explicit conditions.

---

# 17. EVIDENCE STATES

Canonical states:

```text
SUFFICIENT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
UNVERIFIABLE
```

## 17.1 SUFFICIENT

Evidence satisfies the applicable task-level sufficiency requirements.

The system may proceed.

## 17.2 INSUFFICIENT

The system must:

- retrieve more;
- request information;
- escalate;
- ask the user;
- abstain;
- or stop.

## 17.3 CONFLICTED

The system exposes the conflict.

It must not silently choose an interpretation.

## 17.4 STALE

The evidence is retained for historical purposes but cannot silently be treated as current authority.

## 17.5 UNAUTHORIZED

The evidence cannot enter the reasoning context.

## 17.6 UNVERIFIABLE

The information may be presented as uncertain or unresolved but must not be silently promoted to established fact.

---

# 18. EVIDENCE SUFFICIENCY

Evidence sufficiency is a multidimensional assessment.

Conceptual vector:

```text
Sufficiency =
{
  relevance,
  completeness,
  authority,
  revision_validity,
  temporal_validity,
  authorization,
  source_quality,
  consistency,
  verification,
  task_fit
}
```

Therefore:

```text
retrieval_count >= K
```

is not an evidence-sufficiency criterion.

A single authoritative document may be sufficient.

A hundred low-authority chunks may be insufficient.

---

# 19. AUTHORIZATION MODEL

Authorization is evaluated before evidence becomes available to reasoning wherever technically practical.

Canonical flow:

```text
User Identity
      ↓
Task Scope
      ↓
Authorization Policy
      ↓
Document Authorization
      ↓
Revision Authorization
      ↓
Region Authorization
      ↓
Evidence Authorization
      ↓
Agent Context
```

The architecture explicitly rejects:

```text
Retrieve Everything
       ↓
Filter Later
```

as the default pattern.

Phase 10 establishes the same requirement: authorization must occur before evidence becomes available to reasoning wherever practical.

---

# 20. AUTHORIZATION PROPAGATION

Authorization must be considered across:

```text
Source
 ↓
Document
 ↓
Revision
 ↓
Region
 ↓
Evidence
 ↓
Derived Information
 ↓
Claim
 ↓
Result
 ↓
Artifact
```

## 20.1 Derived information

Derived information inherits restrictions from its inputs unless a valid policy establishes another handling rule.

## 20.2 Mixed-authority derivation

If:

```text
Evidence A = Restricted
Evidence B = Internal
```

then:

```text
Derived X
```

must carry a policy-determined composite restriction.

The system must not assume:

```text
summary = lower classification
```

---

# 21. CLASSIFICATION PROPAGATION

Classification is an independent metadata dimension.

Conceptual flow:

```text
CONFIDENTIAL SOURCE
       ↓
CONFIDENTIAL EVIDENCE
       ↓
CONFIDENTIAL DERIVATION
       ↓
RESTRICTED CLAIM
       ↓
RESTRICTED ARTIFACT
```

Classification may be strengthened by composition.

It must not be silently downgraded because information has been:

- summarized;
- paraphrased;
- embedded;
- reranked;
- generated;
- calculated.

Any declassification is an explicit policy decision.

---

# 22. DERIVED INFORMATION

`DerivedInformation` is information produced by transforming one or more evidence objects.

Examples:

- summary;
- calculation;
- comparison;
- inferred relationship;
- structured engineering representation;
- statistical result;
- extracted conclusion.

Conceptual model:

```text
DerivedInformation
├── derived_id
├── input_evidence[]
├── transformation
├── creator
├── model/process
├── verification_state
├── classification
├── authorization
├── temporal_scope
└── provenance
```

Many-to-many relationships are required.

---

# 23. DERIVATION GRAPH

The system must support:

```text
Evidence A ─────┐
                ├──→ Derived X
Evidence B ─────┘
```

and:

```text
Evidence A
    ↓
Derived X
    ↓
Claim Y
    ↓
Artifact Z
```

This graph is required for lineage reconstruction.

---

# 24. CLAIM MODEL

A `Claim` is an assertion presented by the system.

```text
Claim
├── claim_id
├── content
├── claim_type
├── evidence_refs
├── derivation_refs
├── verification_state
├── authority
├── authorization
├── temporal_applicability
├── classification
├── creator
├── model/process
└── provenance
```

## 24.1 Claim distinction

The system must distinguish:

```text
Source Fact
```

from:

```text
System Inference
```

from:

```text
Human Judgment
```

This distinction is critical for engineering workflows.

---

# 25. CLAIM TYPES

The logical taxonomy should support:

- directly observed;
- extracted;
- calculated;
- inferred;
- summarized;
- compared;
- interpreted;
- verified;
- human-approved.

The final physical taxonomy remains configurable.

---

# 26. CONFLICTING CLAIMS

The system must represent:

```text
Claim A
   ↕
Conflict
   ↕
Claim B
```

Conflict metadata should include:

- conflict type;
- evidence sources;
- revisions;
- temporal context;
- conflicting values;
- resolution status;
- resolver;
- resolution timestamp.

Possible states:

```text
UNRESOLVED
RESOLVED
ESCALATED
ABSTAINED
SUPERSEDED
```

No silent conflict resolution.

---

# 27. RESULT MODEL

A `Result` is the output of a workflow.

It may contain:

- answer;
- findings;
- calculations;
- structured data;
- recommendations;
- references;
- claims;
- verification status;
- evidence references;
- provenance.

A result can be:

```text
COMPLETE
PARTIAL
ABSTAINED
FAILED
```

A result is not necessarily an artifact.

---

# 28. ARTIFACT MODEL

An `Artifact` is a generated deliverable.

Examples:

- technical report;
- approval-note draft;
- spreadsheet;
- structured document;
- code;
- engineering analysis output.

Logical model:

```text
Artifact
├── artifact_id
├── version
├── task
├── creator
├── claims
├── evidence_refs
├── verification
├── provenance
├── authorization
├── classification
├── release_state
└── timestamp
```

Artifact lifecycle:

```text
GENERATED
    ↓
CHECKED
    ↓
VERIFIED
    ↓
HUMAN-APPROVED
```

Generation does not imply approval. The SRS explicitly requires these states to remain distinct.

---

# 29. ARTIFACT LINEAGE

A reviewer must be able to navigate:

```text
Artifact
   ↓
Claim
   ↓
Derived Information
   ↓
Evidence
   ↓
Revision
   ↓
Document
   ↓
Source
```

The reverse direction must also be supportable where appropriate:

```text
Source
 ↓
Evidence
 ↓
Claims
 ↓
Artifacts
```

This permits impact analysis when a source is withdrawn or superseded.

---

# 30. PROVENANCE MODEL

The canonical provenance graph is:

```text
SOURCE
  ↓
DOCUMENT
  ↓
REVISION
  ↓
REGION
  ↓
EXTRACTION
  ↓
EVIDENCE
  ↓
DERIVATION
  ↓
CLAIM
  ↓
RESULT
  ↓
ARTIFACT
```

Processing operations are first-class provenance events.

---

# 31. PROVENANCE EVENT

Conceptual event:

```text
ProvenanceEvent
├── event_id
├── actor
├── component
├── task
├── execution
├── inputs
├── operation
├── tool/model
├── version
├── configuration_reference
├── timestamp
├── outputs
└── source_references
```

## 31.1 Mandatory event categories

At minimum for material transformations:

- ingestion;
- parsing;
- OCR;
- multimodal extraction;
- normalization;
- indexing;
- retrieval;
- evidence formation;
- derivation;
- model invocation;
- tool execution;
- verification;
- artifact generation;
- artifact release;
- source revocation.

---

# 32. MODEL PROVENANCE

When a model contributes materially, preserve:

```text
model_identity
model_version
capability_identity
execution_id
configuration_reference
evidence_references
timestamp
```

Prompt/context contents should only be retained where policy and reproducibility requirements justify it.

The goal is:

```text
What model/process contributed?
What evidence was available?
What configuration was used?
What output resulted?
```

without making sensitive prompt storage mandatory.

---

# 33. RETRIEVAL REPRESENTATION

The retrieval engine must not return merely:

```text
text_chunk
```

It should return an evidence-aware object:

```text
RetrievedEvidence
├── evidence_id
├── content_reference
├── document
├── revision
├── location
├── authority
├── authorization
├── classification
├── temporal_validity
├── relevance
├── provenance
├── verification_state
└── conflict_state
```

This prevents retrieval from becoming detached from governance.

---

# 34. RETRIEVAL ARCHITECTURE

The logical retrieval stack is:

```text
TASK
 ↓
IDENTITY
 ↓
AUTHORIZATION
 ↓
TASK/EVIDENCE REQUIREMENTS
 ↓
VALIDITY FILTERING
 ↓
METADATA FILTERING
 ↓
LEXICAL / SEMANTIC / STRUCTURAL / VISUAL RETRIEVAL
 ↓
RERANKING
 ↓
EVIDENCE ASSESSMENT
 ↓
EVIDENCE BUNDLE
 ↓
CONTEXT COMPILATION
 ↓
REASONING
```

The exact physical filter order may vary by implementation, but security and authorization constraints must never be weakened to improve retrieval recall.

---

# 35. RETRIEVAL DIMENSIONS

Evidence ranking must consider:

1. authorization;
2. authority;
3. validity;
4. revision;
5. temporal applicability;
6. relevance;
7. completeness;
8. source quality;
9. verification state;
10. structural/visual relevance where applicable.

Semantic similarity is therefore only one ranking dimension.

---

# 36. CHUNKING ARCHITECTURE

Chunking is a representation strategy rather than a knowledge model.

Supported logical chunk types include:

- semantic;
- structural;
- page-aware;
- section-aware;
- table-aware;
- image-region;
- engineering-object;
- multimodal.

Fixed-size chunking is not the canonical architecture.

A chunk must remain traceable to:

```text
Document
Revision
Location
Representation
Content Hash
Representation Version
```

---

# 37. EMBEDDING MODEL

Embeddings are retrieval projections.

An embedding conceptually contains:

```text
Embedding
├── embedding_id
├── representation_id
├── model
├── model_version
├── vector_version
├── dimensionality
├── timestamp
├── authorization_reference
└── provenance
```

An embedding is not authoritative evidence.

---

# 38. EMBEDDING VERSIONING

When the embedding model changes:

```text
Representation
   ├── Embedding V1
   └── Embedding V2
```

The architecture must support:

- coexistence;
- migration;
- re-indexing;
- rollback;
- invalidation;
- version-aware retrieval.

Re-indexing must not alter canonical evidence.

---

# 39. INDEX CONSISTENCY

Canonical data is authoritative.

Indexes are projections.

```text
Canonical Evidence
       ↓
Index Projection
```

The system must handle:

- indexing delay;
- failed indexing;
- partial indexing;
- stale indexes;
- reindexing;
- rollback.

A stale index must not imply stale canonical knowledge.

---

# 40. AUTHORIZATION-CONSISTENT INDEXING

Authorization affects:

- indexing;
- search;
- retrieval;
- caching;
- embeddings;
- reranking;
- context assembly.

The architecture must prevent an index from becoming an unauthorized side channel.

A user must not receive protected information merely because:

```text
the vector store returned it
```

---

# 41. CACHE ARCHITECTURE

Caching is permitted only when cache identity preserves applicable governance.

Cache keys must conceptually incorporate:

```text
task_scope
authorization_scope
source_revision
temporal_context
representation_version
policy_version
provenance
```

Unsafe pattern:

```text
query → global answer cache
```

Preferred:

```text
authorized context
      ↓
scoped cache
      ↓
result
```

A cache invalidation event must occur when relevant source, authorization, policy or representation state changes.

---

# 42. EVIDENCE BUNDLE

For complex workflows, the retrieval system may produce an `EvidenceBundle`.

Example:

```text
Evidence Bundle
├── Current Inspection Report
├── Previous Inspection
├── Equipment Datasheet
├── Applicable Standard
└── Approval Record
```

Logical fields:

```text
bundle_id
task_purpose
evidence[]
conflicts[]
sufficiency
authorization
classification
provenance
```

The bundle is a contextual projection.

The individual evidence objects remain canonical.

---

# 43. CONTEXT COMPILATION

The system should compile model context from governed evidence rather than passing arbitrary retrieval output directly.

```text
Authorized Evidence
        ↓
Evidence Assessment
        ↓
Conflict Handling
        ↓
Relevance Selection
        ↓
Context Compilation
        ↓
Model
```

Context compilation should preserve:

- evidence identifiers;
- source references;
- revision;
- location;
- authority;
- temporal scope;
- uncertainty;
- conflict state.

---

# 44. KNOWLEDGE INGESTION LIFECYCLE

Canonical lifecycle:

```text
SOURCE DISCOVERY
      ↓
AUTHORIZATION
      ↓
ACQUISITION
      ↓
INTEGRITY CHECK
      ↓
DOCUMENT IDENTIFICATION
      ↓
REVISION IDENTIFICATION
      ↓
PARSING
      ↓
OCR / VISION
      ↓
STRUCTURE EXTRACTION
      ↓
NORMALIZATION
      ↓
METADATA REGISTRATION
      ↓
EVIDENCE REGISTRATION
      ↓
INDEXING
      ↓
VALIDATION
      ↓
AVAILABLE
```

The Phase 13 brief explicitly requires this lifecycle and explicit ingestion states rather than collapsing all processing into a single ingestion operation.

---

# 45. INGESTION STATES

```text
DISCOVERED
AUTHORIZED
INGESTING
PARSED
EXTRACTED
NORMALIZED
INDEXED
VALIDATED
AVAILABLE
FAILED
QUARANTINED
SUPERSEDED
DELETED
```

A revision cannot become authoritative merely because it reached `INDEXED`.

It must satisfy the applicable validation and authority conditions.

---

# 46. MALICIOUS DOCUMENT HANDLING

Documents are treated as untrusted inputs.

Threats include:

- malformed PDFs;
- decompression bombs;
- embedded scripts;
- macros;
- hostile metadata;
- prompt injection;
- malicious images;
- malicious spreadsheets;
- parser exploits;
- resource exhaustion.

Canonical boundary:

```text
UNTRUSTED SOURCE
       ↓
SAFE PROCESSING BOUNDARY
       ↓
EXTRACTED REPRESENTATION
       ↓
GOVERNED EVIDENCE
```

Document content cannot directly modify:

- policy;
- permissions;
- identity;
- authority;
- task control;
- security state.

This follows the system-wide invariant that untrusted content cannot acquire control-plane authority.

---

# 47. DOCUMENT PROCESSING ISOLATION

Document processors should be treated as potentially exploitable processing components.

Isolation requirements must address:

- parser vulnerabilities;
- resource exhaustion;
- oversized documents;
- malicious embedded content;
- unsafe libraries;
- unexpected subprocess execution.

The exact physical isolation mechanism remains governed by the Phase 12 execution architecture and Phase 11 technology baseline.

---

# 48. DATA QUALITY MODEL

Data quality is multidimensional.

```text
Quality
├── completeness
├── correctness
├── consistency
├── authority
├── freshness
├── revision correctness
├── authorization correctness
├── provenance completeness
├── extraction quality
└── structural correctness
```

A single scalar "quality score" must not replace these dimensions.

---

# 49. DATA QUALITY STATES

```text
VALID
PARTIALLY_VALID
INVALID
UNKNOWN
REQUIRES_REPROCESSING
QUARANTINED
```

Downstream behavior must depend on state.

For example:

```text
INVALID
   ↓
No retrieval availability
```

whereas:

```text
PARTIALLY_VALID
   ↓
Restricted availability with explicit limitations
```

may be appropriate for some workflows.

---

# 50. INGESTION VALIDATION GATES

Before knowledge becomes generally retrievable, validate:

1. file integrity;
2. document identity;
3. revision identity;
4. metadata;
5. authorization;
6. extraction;
7. provenance;
8. source linkage;
9. indexing consistency;
10. applicable data-quality conditions.

Failure at a critical gate produces:

```text
FAILED
```

or:

```text
QUARANTINED
```

rather than silently available data.

---

# 51. VERSIONING

Version control applies to:

```text
Source
Document
Revision
Representation
Parser
OCR
VLM
Embedding
Index
Evidence
Derived Information
Claim
Artifact
```

Processing-version changes create new lineage branches where material behavior changes.

They must not overwrite history in a way that destroys reproducibility.

---

# 52. IMMUTABILITY

Strong candidates for immutable treatment:

- original source objects;
- historical revisions;
- provenance events;
- security-relevant audit events.

Derived objects should generally be versioned rather than destructively overwritten.

This distinction permits:

```text
what the system believed before
```

to remain distinguishable from:

```text
what the system believes after reprocessing
```

---

# 53. SOURCE REVOCATION

A source may become:

- withdrawn;
- superseded;
- incorrect;
- unauthorized;
- compromised.

Consequences may include:

```text
STALE
INVALID
REVOKED
REQUIRES_REVIEW
```

The impact graph should identify:

```text
Source
 ↓
Evidence
 ↓
Derived Information
 ↓
Claims
 ↓
Artifacts
```

that depend on the revoked source.

This enables impact analysis rather than blind deletion.

---

# 54. DELETE SEMANTICS

Deletion must distinguish:

```text
data availability
```

from:

```text
lineage history
```

Potential mechanisms:

- hard deletion;
- soft deletion;
- tombstone;
- legal hold;
- archival;
- downstream invalidation.

The correct policy is deployment-specific.

The architecture therefore defines the semantics without inventing a universal retention period.

---

# 55. KNOWLEDGE UPDATE LIFECYCLE

New revision:

```text
NEW REVISION
     ↓
DETECT
     ↓
VALIDATE
     ↓
PROCESS
     ↓
INDEX
     ↓
VALIDATE
     ↓
ACTIVATE
     ↓
SUPERSEDE PREVIOUS REVISION
```

Critical rule:

> A partially processed revision must never silently become the authoritative current revision.

Activation is a control-plane decision.

---

# 56. TEMPORAL SEARCH

The architecture supports three distinct query classes:

### Current

```text
What is currently applicable?
```

### Historical

```text
What was applicable at time T?
```

### System-history

```text
What information did the system have or use at time T?
```

These must not be conflated.

---

# 57. AUTHORITY-AWARE SEARCH

Search ranking cannot reduce to:

```text
similarity score
```

Conceptual precedence:

```text
Authorization
   ↓
Applicability
   ↓
Authority
   ↓
Revision / Temporal Validity
   ↓
Relevance
   ↓
Completeness
```

A highly similar draft must not automatically outrank an authoritative approved source.

---

# 58. RETRIEVAL FAILURE MODEL

The retrieval layer must distinguish:

```text
NO_RESULT
INSUFFICIENT
CONFLICTED
STALE
UNAUTHORIZED
LOW_QUALITY
TIMEOUT
INDEX_UNAVAILABLE
```

Possible responses:

```text
RETRIEVE_MORE
ASK_USER
ESCALATE
REQUEST_AUTHORIZATION
USE_ALTERNATE_SOURCE
ABSTAIN
STOP
```

The correct response is determined by task risk and policy.

---

# 59. KNOWLEDGE GRAPH POSITION

The architecture does not require a universal enterprise ontology or graph database.

Instead:

```text
Canonical Evidence Model
        +
Domain-Specific Structured Representations
        +
Derivation / Provenance Graph
        +
Retrieval Projections
```

This is preferable to making one giant ontology the central dependency of the MVP.

For P&IDs, structured graph/topology representations are appropriate because connectivity is materially different from textual similarity.

---

# 60. RELATIONAL VS GRAPH SEMANTICS

The logical model requires graph relationships.

It does **not** require a graph database.

Examples:

```text
Evidence → supports → Claim
Evidence → conflicts_with → Evidence
Revision → supersedes → Revision
Representation → derived_from → Source
Claim → derived_from → Evidence
Artifact → contains → Claim
```

These relationships may ultimately be implemented through relational structures, graph structures, or a hybrid.

The logical requirement is preservation of relationship semantics.

---

# 61. KNOWLEDGE CONSISTENCY MODEL

The system must distinguish:

### Canonical consistency

The authoritative data model is internally consistent.

### Projection consistency

Indexes correctly represent canonical data.

### Retrieval consistency

A retrieval response corresponds to currently authorized canonical evidence.

### Provenance consistency

Every material derived object can be traced to its declared inputs.

### Authorization consistency

No object becomes available beyond its permitted scope.

---

# 62. CROSS-COMPONENT DATA CONTRACTS

Phase 13 establishes the logical contracts consumed by Phase 12 components.

## Knowledge Ingestion Manager

Produces:

```text
Source
Document
Revision
Representation
ProcessingEvent
```

## Document Intelligence Engine

Produces:

```text
ExtractedInformation
Representation
ExtractionProvenance
```

## Retrieval Engine

Consumes:

```text
Identity
Task
Authorization
Query
```

Produces:

```text
RetrievedEvidence
EvidenceBundle
```

## Evidence Manager

Owns:

```text
Evidence
EvidenceState
Sufficiency
Conflict
Authorization
```

## Agent Runtime

Consumes governed:

```text
EvidenceBundle
```

It does not directly query arbitrary stores.

## Provenance Manager

Owns:

```text
ProvenanceEvent
Lineage
DerivationRelationship
```

---

# 63. SECURITY INVARIANTS

The data architecture must preserve:

### INV-DK-01

Unauthorized evidence cannot enter model context.

### INV-DK-02

Semantic relevance cannot override authorization.

### INV-DK-03

Source existence does not imply authority.

### INV-DK-04

Newest revision does not automatically imply validity.

### INV-DK-05

Extracted information does not automatically become evidence.

### INV-DK-06

Evidence does not automatically become verified fact.

### INV-DK-07

Derived information retains source lineage.

### INV-DK-08

Classification cannot silently decrease through transformation.

### INV-DK-09

Revoked sources cannot silently remain authoritative.

### INV-DK-10

Indexes cannot become an unauthorized information channel.

### INV-DK-11

Caches cannot bypass authorization or revision semantics.

### INV-DK-12

Untrusted document content cannot modify control-plane state.

---

# 64. SECURITY QUALIFICATION ALIGNMENT

The Phase 13 design directly supports the project's security qualification baseline.

The qualification requires zero unauthorized evidence entering an execution context, zero cases where retrieval relevance overrides authorization, zero unauthorized retrievals, and complete enforcement of tested authorization restrictions. 
Therefore the following are **Tier-1 data architecture invariants**, not performance targets:

```text
Unauthorized evidence exposed = 0
Unauthorized retrieval = 0
Cross-task leakage = 0
Cross-user leakage = 0
Credential exposure through knowledge path = 0
Prompt injection → authority = 0
```

---

# 65. DATA-PLANE SECURITY

The data architecture assumes all of the following may be hostile or incorrect:

- uploaded documents;
- OCR;
- VLM output;
- retrieved text;
- tool output;
- generated code;
- model-generated claims.

Therefore:

```text
DATA
  ≠
INSTRUCTIONS
  ≠
AUTHORITY
```

The data model must preserve these distinctions.

---

# 66. DATA-QUALITY FAILURE HANDLING

Examples:

| Failure | Required behavior |
|---|---|
| Corrupt source | Quarantine |
| Unknown document identity | Hold for resolution |
| Unknown revision | Do not treat as current authority |
| OCR corruption | Mark representation quality |
| Missing provenance | Restrict downstream use |
| Unauthorized source | Deny availability |
| Conflicting revisions | Represent conflict |
| Stale index | Reindex / bypass |
| Invalid extraction | Reprocess or quarantine |
| Revoked source | Invalidate affected knowledge where required |

---

# 67. P&ID DATA MODEL

The P&ID representation should preserve:

```text
Drawing
 ├── Page
 │    ├── Region
 │    ├── Text
 │    ├── Symbol
 │    └── Line
 │
 ├── Equipment
 ├── Instrument
 ├── Valve
 ├── Tag
 ├── Connection
 ├── SpatialRelation
 └── Topology
```

Each engineering object retains:

```text
source_reference
revision
location
extraction_method
confidence
verification_state
provenance
```

The topology representation is derived knowledge until verified.

It is not a substitute for the original drawing.

---

# 68. NUMERICAL DATA

Numerical information must retain:

- original value;
- unit;
- source;
- location;
- transformation;
- normalized value;
- conversion;
- calculation provenance;
- verification status.

Example:

```text
12.4 bar
```

must not become merely:

```text
12.4
```

without preserving the unit semantics and source lineage.

Derived calculations must preserve:

```text
inputs
operation
formula/process
output
verification
```

---

# 69. MIXED-SOURCE DERIVATION

When a claim uses multiple sources:

```text
Evidence A
Evidence B
Evidence C
     ↓
Derived X
     ↓
Claim Y
```

the claim inherits the relevant:

- authorization constraints;
- classification;
- temporal context;
- conflict state;
- provenance.

The system must retain all material supporting inputs.

---

# 70. HUMAN KNOWLEDGE

Human review is represented as a distinct provenance and authority event.

```text
AI-Derived Information
        ↓
Human Review
        ↓
Human Judgment
        ↓
Approval
```

A human approval event is not simply another model-generated claim.

The actor identity and approval context must be recorded.

---

# 71. KNOWLEDGE AUTHORITY HIERARCHY

The architecture supports a configurable authority hierarchy rather than hard-coding a universal one.

Conceptual examples:

```text
Approved Controlled Document
        >
Current Approved Standard
        >
Approved Engineering Record
        >
Draft
        >
Historical Record
        >
Unverified Upload
        >
User Note
```

The exact ordering is customer policy.

The architecture requires that such ordering be representable.

---

# 72. SOURCE APPLICABILITY

Authority alone is insufficient.

A document may be authoritative but irrelevant to the task.

Therefore:

```text
Authority
+
Applicability
+
Validity
+
Authorization
```

must all be assessed.

This avoids:

```text
authoritative but wrong-context document
```

being selected solely because of its authority.

---

# 73. DATA ACCESS MODEL

Data access should be evaluated across:

```text
Actor
Task
Source
Document
Revision
Region
Evidence
Action
```

A permission decision therefore has a context rather than merely:

```text
user_can_read_document = true
```

---

# 74. DATA LINEAGE REQUIREMENT

For any material output, the system should be able to answer:

1. Which source was used?
2. Which document?
3. Which revision?
4. Which location?
5. Which extraction process?
6. Which evidence?
7. Which derivation?
8. Which model/process?
9. Which claim?
10. Which verification?
11. Which artifact?
12. Which approval?

This is the minimum conceptual lineage chain.

---

# 75. DATA RETENTION ARCHITECTURE

Retention is policy-driven.

The logical model must support independent retention for:

```text
Raw Sources
Representations
Evidence
Derived Information
Claims
Artifacts
Provenance
Audit
Telemetry
```

Retention of one class must not automatically imply deletion of every related class.

---

# 76. PROVENANCE VS AUDIT VS OBSERVABILITY

These remain separate.

### Provenance

> Where did this information come from?

### Audit

> What happened?

### Observability

> Is the system operating correctly?

They share correlation identifiers but must not be collapsed into one generic event store.

Phase 10 explicitly establishes this distinction.

---

# 77. DATA CORRELATION IDENTIFIERS

Material data objects should support correlation through:

```text
tenant/deployment
user
task
execution
workflow
step
source
revision
representation
evidence
claim
artifact
provenance_event
```

The precise identifier implementation is deferred.

The semantic relationships are mandatory.

---

# 78. OFFLINE KNOWLEDGE OPERATION

The architecture must operate without external network dependency.

Knowledge lifecycle therefore supports:

```text
Offline Acquisition
 ↓
Integrity Validation
 ↓
Controlled Import
 ↓
Processing
 ↓
Indexing
 ↓
Validation
 ↓
Activation
```

The same controlled lifecycle applies to model/software dependencies where relevant.

---

# 79. SOVEREIGNTY IMPLICATION

The data architecture contributes to sovereignty by ensuring that confidential knowledge has no architectural dependency on external retrieval or external AI processing.

However:

> A local data store alone does not prove sovereignty.

Sovereignty remains a system-level property requiring independent network enforcement and observation.

The SRS explicitly requires zero unauthorized external transfer, offline operation and independent network observability.

---

# 80. PERFORMANCE IMPLICATIONS

The architecture intentionally avoids premature numerical thresholds.

Phase 13 establishes what must be measurable:

```text
ingestion throughput
retrieval latency
indexing latency
reprocessing cost
storage growth
embedding footprint
cache efficiency
context size
provenance traversal cost
concurrent retrieval
authorization filtering overhead
```

Exact targets belong to the validated hardware/performance program.

---

# 81. STORAGE LOGICAL DOMAINS

The storage architecture should conceptually separate:

```text
1. Source Vault
2. Canonical Metadata Store
3. Representation Store
4. Evidence Store
5. Retrieval Indexes
6. Task/Execution State
7. Provenance Store
8. Audit Store
9. Artifact Store
10. Model/Processing Registry
11. Temporary Processing Storage
```

Physical co-location is permitted for MVP where security and operational requirements remain satisfied.

Logical separation is mandatory.

---

# 82. PHASE 11 TECHNOLOGY ALIGNMENT

Phase 13 does not reopen Phase 11 technology decisions.

The logical architecture is compatible with the current baseline:

```text
Qdrant
    → retrieval projection

SQLite
    → local control/metadata where appropriate

Docling / PaddleOCR
    → document representations

Qwen embedding/reranking capabilities
    → retrieval projections

Application-owned evidence model
    → canonical knowledge semantics

Application-owned provenance model
    → lineage

OpenTelemetry
    → operational observability
```

These implementations remain subordinate to the logical model.

---

# 83. REJECTED DATA ARCHITECTURES

## 83.1 Vector DB as knowledge authority

**Rejected.**

Reason:

- loses authority semantics;
- weak revision semantics;
- weak temporal semantics;
- insufficient provenance;
- authorization becomes fragile;
- difficult conflict representation.

---

## 83.2 Chunks as canonical knowledge

**Rejected.**

Chunks are retrieval representations.

---

## 83.3 OCR text as truth

**Rejected.**

OCR is an extraction mechanism.

---

## 83.4 VLM as P&ID truth

**Rejected.**

Visual interpretation must remain distinguishable from structural and engineering verification.

---

## 83.5 Global unrestricted cache

**Rejected.**

Potential cross-user, cross-task and revision leakage.

---

## 83.6 Retrieve-then-authorize

**Rejected as default.**

Authorization must be applied before reasoning receives protected evidence wherever practical.

---

## 83.7 Timestamp-only revision model

**Rejected.**

Organizational authority is not reducible to recency.

---

## 83.8 Destructive reprocessing

**Rejected.**

Would damage reproducibility and lineage.

---

## 83.9 One giant enterprise ontology

**Rejected for MVP.**

Domain-specific structured representations are preferable to imposing an unnecessarily large ontology dependency.

---

# 84. DECISION REGISTER

| ID | Decision | Status |
|---|---|---|
| DKD-01 | Source, Document and Revision are distinct entities | **Preferred** |
| DKD-02 | Evidence is first-class | **Preferred** |
| DKD-03 | Retrieval indexes are projections | **Preferred** |
| DKD-04 | Authorization precedes reasoning exposure | **Mandatory** |
| DKD-05 | Revision semantics are explicit | **Preferred** |
| DKD-06 | Temporal validity is independent | **Preferred** |
| DKD-07 | Classification propagates | **Preferred** |
| DKD-08 | Derived information retains lineage | **Mandatory** |
| DKD-09 | Claims retain evidence support | **Mandatory** |
| DKD-10 | Conflicts are explicit | **Mandatory** |
| DKD-11 | P&ID topology is separate from visual recognition | **Preferred** |
| DKD-12 | Provenance is application-owned logically | **Preferred** |
| DKD-13 | Raw sources are retained subject to policy | **Strong Candidate** |
| DKD-14 | Indexes may be rebuilt without changing canonical evidence | **Preferred** |
| DKD-15 | Cache scope includes authorization/revision | **Mandatory** |
| DKD-16 | Document processors are untrusted inputs | **Mandatory** |
| DKD-17 | Deletion supports tombstone/revocation semantics | **Strong Candidate** |
| DKD-18 | Bi-temporal semantics are architecturally supported | **Strong Candidate** |
| DKD-19 | Universal enterprise ontology is not MVP dependency | **Rejected** |
| DKD-20 | Vector DB as knowledge authority | **Rejected** |

---

# 85. OPEN QUESTIONS

The following remain intentionally unresolved.

## OQ-DK-01 — Classification taxonomy

Which exact classification levels must the first deployment support?

**Status:** Open Question.

---

## OQ-DK-02 — Authorization granularity

Will customer authorization apply at:

- document;
- revision;
- page;
- region;
- field;
- evidence;

level?

**Status:** Requires customer validation.

---

## OQ-DK-03 — Bi-temporal implementation

Is full bi-temporal storage required for MVP or only architecturally supported?

**Status:** Requires workflow validation.

---

## OQ-DK-04 — Source identity resolution

How much automatic document identity resolution is acceptable before human review is required?

**Status:** Requires experimentation.

---

## OQ-DK-05 — P&ID canonical schema

What minimum engineering topology schema is sufficient for W2 without introducing a full plant ontology?

**Status:** Requires technical design.

---

## OQ-DK-06 — Evidence sufficiency policy

What minimum evidence sufficiency rules apply to each MVP workflow?

**Status:** Requires workflow-specific qualification.

---

## OQ-DK-07 — Retention/deletion

What retention and legal-hold policies must the first customer deployment support?

**Status:** Customer/security decision.

---

## OQ-DK-08 — Revocation impact

When a source is revoked, which downstream claims/artifacts must automatically become invalid or require review?

**Status:** Requires policy definition.

---

## OQ-DK-09 — Mixed-classification derivation

What customer-specific policy governs outputs derived from multiple classification levels?

**Status:** Open.

---

## OQ-DK-10 — Retrieval authorization implementation

What combination of canonical filtering and index-level filtering provides the strongest security/performance balance?

**Status:** Phase 14/technical validation.

---

## OQ-DK-11 — Representation retention

Which intermediate representations must be retained versus reproducibly regenerated?

**Status:** Storage/performance validation.

---

## OQ-DK-12 — Provenance retention

What minimum provenance event set is required for each workflow to satisfy audit and reproducibility objectives?

**Status:** Requires qualification.

---

# 86. VALIDATION PLAN

Phase 13 must be validated through representative data rather than by schema inspection alone.

## V-DK-01 — Document identity

Test:

- duplicate filenames;
- renamed files;
- identical content;
- different revisions;
- conflicting metadata.

---

## V-DK-02 — Revision correctness

Test:

- current revision;
- superseded revision;
- historical query;
- draft versus approved;
- withdrawn document.

---

## V-DK-03 — Authorization

Test:

- authorized user;
- unauthorized user;
- mixed-authority bundle;
- cross-task retrieval;
- cross-user retrieval.

Security pass condition follows the established qualification baseline: unauthorized evidence exposure must remain **0**.

---

## V-DK-04 — Prompt injection

Test malicious instructions embedded in:

- PDF;
- DOCX;
- spreadsheet;
- OCR;
- image;
- retrieved text.

Required result:

```text
DATA ≠ AUTHORITY
```

No unauthorized control-plane action.

The security baseline requires 100% preservation of this separation and zero unauthorized tool execution or retrieval.

---

## V-DK-05 — Provenance

For every material result, reconstruct:

```text
Artifact
 → Claim
 → Evidence
 → Revision
 → Source
```

---

## V-DK-06 — Revocation

Withdraw a source and verify:

- retrieval behavior;
- evidence state;
- claim impact;
- artifact impact;
- audit;
- provenance.

---

## V-DK-07 — Index consistency

Create:

- indexing delay;
- partial index;
- stale index;
- reindex;
- rollback.

Verify canonical evidence remains authoritative.

---

## V-DK-08 — P&ID lineage

Trace:

```text
Drawing
 → Region
 → OCR/Visual Extraction
 → Entity
 → Relationship
 → Topology
 → Claim
```

and identify every transformation.

---

## V-DK-09 — Cache isolation

Test:

- user A → user B;
- task A → task B;
- revision A → revision B;
- classification A → classification B.

Required result:

```text
0 unauthorized leakage
```

---

## V-DK-10 — Resource pressure

Test ingestion and retrieval under CPU/RAM/storage pressure.

Security controls must not fail open.

The security qualification baseline requires zero security-control bypasses caused by resource exhaustion and 100% bounded-resource enforcement.

---

# 87. REQUIREMENT TRACEABILITY

| Architecture requirement | Phase 13 response |
|---|---|
| Evidence-first knowledge | Evidence is canonical object |
| Authorization | Propagated from identity to evidence |
| Revision correctness | Explicit revision entity |
| Temporal validity | Independent temporal model |
| Provenance | Graph + processing events |
| Multimodal | Multiple linked representations |
| P&ID | Separate visual/structural/engineering layers |
| Retrieval | Governed projection |
| Verification | Evidence/claim state |
| Artifact lineage | Artifact → claim → evidence → source |
| Security | Authorization and classification propagation |
| Sovereignty | Offline/local data architecture |
| Auditability | Material data events retained |
| Extensibility | Logical model independent of physical technology |

---

# 88. ARCHITECTURAL CONSEQUENCES

Phase 13 establishes several important consequences for implementation.

### Consequence 1

The retrieval engine cannot be the owner of enterprise knowledge semantics.

### Consequence 2

The Evidence Manager becomes one of the most security-critical components in the system.

### Consequence 3

The canonical data model must be richer than the vector-search model.

### Consequence 4

Source revision and temporal validity must participate in retrieval decisions.

### Consequence 5

P&ID processing requires structured representations in addition to embeddings.

### Consequence 6

Provenance must be generated during processing, not reconstructed after the fact.

### Consequence 7

Authorization metadata must travel with evidence.

### Consequence 8

Reprocessing creates lineage branches rather than replacing history.

### Consequence 9

Cache design is a security concern, not merely a performance concern.

### Consequence 10

The first customer deployment must provide enough organizational metadata to establish authority and applicability.

---

# 89. PHASE 13 GATE

## Gate Result

# **GATE A — DATA & KNOWLEDGE ARCHITECTURE BASELINE ESTABLISHED**

The phase establishes:

- canonical data concepts;
- source/document/revision separation;
- location model;
- extraction representation;
- evidence model;
- evidence states;
- authorization propagation;
- classification propagation;
- temporal semantics;
- derived-information model;
- claim model;
- result/artifact lineage;
- provenance architecture;
- retrieval architecture;
- chunking architecture;
- embedding/index projection model;
- evidence bundles;
- context compilation;
- ingestion lifecycle;
- update/revocation lifecycle;
- data-quality model;
- deletion semantics;
- consistency requirements;
- security invariants;
- validation plan;
- decision register;
- open questions.

No architectural contradiction requiring Phase 13 rework has been identified.

The remaining uncertainty is primarily **implementation-level and customer-policy-level**, not conceptual.

---

# 90. PHASE 14 HANDOFF

Phase 14 should now convert this logical architecture into a detailed **Data Model & Schema Specification**.

Phase 14 should define:

1. canonical entity schemas;
2. identifiers;
3. relationship schemas;
4. state enums;
5. authorization structures;
6. classification structures;
7. temporal structures;
8. provenance-event schemas;
9. evidence schemas;
10. claim schemas;
11. artifact lineage schemas;
12. retrieval-result schemas;
13. index projection schemas;
14. P&ID structural schemas;
15. data validation rules;
16. integrity constraints;
17. migration/versioning strategy;
18. storage mapping;
19. serialization formats;
20. API/event contracts.

Phase 14 should **not** silently reopen:

- the evidence-first architecture;
- authorization-before-reasoning principle;
- source/document/revision separation;
- provenance requirement;
- P&ID representation separation;
- index-as-projection principle.

Those are now architectural baselines.

Technology-specific storage choices may be refined only where Phase 14 identifies a genuine incompatibility with the approved architecture.

---

# 91. FINAL ESTABLISHED FINDINGS

The Phase 13 architecture establishes the following with high confidence:

1. The workbench requires a governed knowledge architecture, not merely RAG.
2. Source, document and revision must be separate logical entities.
3. Extraction outputs cannot automatically be treated as evidence.
4. Evidence must be first class.
5. Authorization must propagate into evidence and reasoning context.
6. Authority, applicability, revision and temporal validity must remain distinct.
7. Retrieval indexes are projections of canonical governed knowledge.
8. Claims must retain evidence relationships.
9. Derived information must retain lineage.
10. Artifacts must retain backward lineage to their supporting claims and evidence.
11. P&ID knowledge requires visual, extracted, spatial, structural and engineering representations.
12. Conflicts must be explicit rather than silently resolved.
13. Reprocessing must preserve historical lineage.
14. Source revocation requires downstream impact handling.
15. Caching is subject to authorization, revision and provenance constraints.
16. Document-processing pipelines must treat enterprise files as potentially hostile.
17. Data architecture directly participates in security qualification.
18. Sovereignty depends on the broader system/network architecture and cannot be established by local storage alone.

The resulting architecture is therefore:

```text
                 ENTERPRISE SOURCES
                        │
                        ▼
                 SOURCE / DOCUMENT
                        │
                        ▼
                    REVISION
                        │
                        ▼
               REPRESENTATIONS
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
        TEXT          VISUAL       STRUCTURE
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                     EVIDENCE
                        │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
         AUTHORITY   TEMPORAL  AUTHORIZATION
              │         │         │
              └─────────┼─────────┘
                        ▼
                EVIDENCE ASSEMBLY
                        │
                        ▼
                     REASONING
                        │
                        ▼
               DERIVED INFORMATION
                        │
                        ▼
                      CLAIMS
                        │
                  ┌─────┴─────┐
                  ▼           ▼
                RESULT      ARTIFACT
                  │           │
                  └─────┬─────┘
                        ▼
                    PROVENANCE
                        │
                        ▼
                  AUDIT / REVIEW
```

**Phase 13 status: COMPLETE.**

**Next phase: Phase 14 — Data Model & Schema Design.**