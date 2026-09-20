Understood. Based on the project artifacts, **Phases 0–8 have been completed through the Final PRD**. The current state is no longer “research → PRD discovery.” The product definition is now established, and the next work should move into **system engineering**.

The final PRD explicitly marks **“Architecture status: Ready to begin”** while keeping technology selection unfrozen. 

## Current position

```text
R1–R8 Research
      ↓
Phase 0 — Research Closure
      ↓
Phase 1 — Requirement Synthesis
      ↓
Phase 2 — Product Scope
      ↓
Phase 3 — Workflow Definition
      ↓
Phase 4 — Requirement Engineering
      ↓
Phase 5 — NFR / Quality Validation
      ↓
Phase 6 — Product Validation
      ↓
Phase 7 — Product Decision Review
      ↓
Phase 8 — FINAL PRD
      │
      │  ← WE ARE HERE
      ↓
SYSTEM ENGINEERING
```

The product decisions are sufficiently closed to establish the engineering baseline: product category, target market/user, workflows, evidence governance, bounded agentic execution, authorization, verification, provenance, multimodality, sovereignty, and the OT/autonomy boundary are decided. Exact model stack and software architecture remain intentionally open. 

---

# What comes next

I would **not** jump directly from PRD → coding.

The next sequence should be:

### Phase 9 — System Requirements Specification

Convert the PRD into **system-level engineering requirements**.

Focus:

* system boundaries
* actors
* system responsibilities
* external interfaces
* system inputs/outputs
* system states
* security boundaries
* trust boundaries
* performance requirements
* resource envelope
* failure requirements
* deployment constraints
* operational requirements
* verification requirements

Output:

> **System Requirements Specification (SRS)**

The key distinction is:

**PRD = what the product must accomplish**

**SRS = what the system must technically guarantee**

---

### Phase 10 — System Architecture

Now answer:

> **How should the system be structured to satisfy the PRD and SRS?**

Define the major architectural domains, for example:

```text
                    USER
                      │
                      ▼
              ┌───────────────┐
              │ Task Interface│
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Task / Policy │
              │    Control    │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Knowledge   Model /      Agent
       & Evidence  Capability   Runtime
                    Layer
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Tool Layer
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Documents       Code         Enterprise
   / OCR           Sandbox       Tools
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Verification
                      │
                      ▼
              Artifact / Result
                      │
                      ▼
             Provenance / Audit
```

This is where architectural alternatives should be compared rather than assumed.

---

# Phase 11 — Architecture Decision & Technology Selection

Only **after** the architecture is defined should the team select concrete technologies.

This is where you evaluate:

* LLMs
* VLMs
* embedding models
* rerankers
* inference engines
* OCR
* document parsers
* vector/search systems
* agent runtime
* orchestration
* sandbox
* storage
* metadata systems
* observability
* APIs
* UI/backend technologies

The PRD deliberately keeps these decisions open. 

The selection process should therefore be:

```text
Requirement
    ↓
Architecture role
    ↓
Candidate technologies
    ↓
Benchmark
    ↓
Security evaluation
    ↓
Hardware evaluation
    ↓
Integration evaluation
    ↓
Decision
```

Not:

```text
Popular technology
      ↓
Try to fit product around it
```

---

# Phase 12 — Component Architecture

Break the system architecture into implementable subsystems.

For example:

1. Identity & authorization
2. Task management
3. Policy engine
4. Model/capability registry
5. Model routing
6. Agent runtime
7. Workflow engine
8. Knowledge ingestion
9. Retrieval/evidence engine
10. Document intelligence
11. OCR
12. Multimodal processing
13. P&ID processing
14. Tool runtime
15. Code sandbox
16. Verification engine
17. Artifact generation
18. Provenance
19. Audit
20. Observability
21. Resource management
22. Deployment/update management

Each component then gets:

* responsibility
* interfaces
* inputs
* outputs
* state
* dependencies
* failure modes
* security boundary
* performance requirements
* test requirements

---

# Phase 13 — Data & Knowledge Architecture

This deserves its own phase because **evidence is a first-class product object**, not simply “RAG data.”

The architecture must determine how to represent and preserve:

```text
Source
  ↓
Document
  ↓
Revision
  ↓
Region / Page
  ↓
Extracted information
  ↓
Evidence
  ↓
Derived information
  ↓
Claim
  ↓
Result / Artifact
```

The PRD requires authority, revision, temporal validity, authorization and provenance to influence evidence handling. 

This phase should therefore establish the actual data model, ingestion lifecycle, indexing strategy and evidence relationships.

---

# Phase 14 — Agent Runtime & Tool Architecture

Now design the actual execution mechanism around the PRD's bounded-agent model.

The central control model is:

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
   ↓
Result
   ↓
Verification
```

The agent must **not** be the authority boundary. That is already a frozen product decision. 

This phase should define:

* planning
* state
* workflow execution
* tool invocation
* retries
* recovery
* escalation
* stopping
* completion predicates
* permissions
* tool contracts
* execution traces

---

# Phase 15 — Security & Sovereignty Architecture

This should be treated as a major engineering phase, not a security checklist at the end.

Define:

* trust boundaries
* network boundaries
* identity
* authorization
* data isolation
* model isolation
* tool permissions
* code isolation
* credential handling
* secrets
* logging
* provenance
* zero-egress enforcement
* supply-chain controls
* offline update mechanism
* malicious-document handling
* prompt injection defenses
* sandbox escape defenses

The PRD specifically defines sovereignty as broader than local installation and includes data, intermediate representations, models, retrieval, tools, generated code, artifacts, network communication, supply chain and updates. 

---

# Phase 16 — Reference Deployment Architecture

Now establish the actual deployment target.

For example:

```text
                 SINGLE SERVER
        ┌──────────────────────────┐
        │                          │
        │       Workbench          │
        │                          │
        │  ┌────────────────────┐  │
        │  │ Application Layer  │  │
        │  └────────────────────┘  │
        │                          │
        │  ┌───────┐ ┌──────────┐ │
        │  │ Agent │ │ Retrieval│ │
        │  └───────┘ └──────────┘ │
        │                          │
        │  ┌───────┐ ┌──────────┐ │
        │  │Models │ │Documents │ │
        │  └───────┘ └──────────┘ │
        │                          │
        │  ┌────────────────────┐  │
        │  │ Sandbox / Tools    │  │
        │  └────────────────────┘  │
        │                          │
        │  ┌────────────────────┐  │
        │  │ Audit / Provenance │  │
        │  └────────────────────┘  │
        │                          │
        └────────────┬─────────────┘
                     │
              Controlled Network
                     │
             No Uncontrolled Egress
```

Then validate this against the actual hardware envelope.

Phase 5 already established that the correct metric is **complete verified workflow performance**, not simply model tokens/second. 

---

# Phase 17 — Prototype / Technical Spikes

Before building the entire system, validate the highest-risk architectural assumptions.

Priority spikes should probably include:

1. **Local model quality**
2. **Multimodal document processing**
3. **P&ID structural interpretation**
4. **Evidence-aware retrieval**
5. **Agent reliability**
6. **Verification effectiveness**
7. **Sandbox security**
8. **Zero-egress operation**
9. **End-to-end hardware feasibility**
10. **Artifact generation**

The purpose is not to create disconnected demos.

Each spike should answer a specific architectural uncertainty.

---

# Phase 18 — MVP Implementation

Only after the above decisions:

```text
Architecture
      ↓
Components
      ↓
Technology decisions
      ↓
Interfaces
      ↓
Implementation
```

Build the committed product path first:

### W3

Organizational Knowledge Investigation

### W1

Inspection / Technical Report Analysis

### W2

P&ID / Engineering Drawing Analysis

### W4

Technical Report / Approval Artifact Generation

W5 remains conditional rather than allowing code execution to expand the project boundary. 

---

# Phase 19 — System Integration & Evaluation

Then evaluate the **complete system**, not isolated components.

```text
User Task
   ↓
Task Understanding
   ↓
Capability Selection
   ↓
Evidence
   ↓
Agent Execution
   ↓
Tools
   ↓
Verification
   ↓
Artifact
   ↓
Human Acceptance
   ↓
Audit
```

Measure:

* verified task success
* workflow reliability
* grounding
* retrieval quality
* authority/revision correctness
* multimodal quality
* P&ID accuracy
* verification effectiveness
* safe abstention
* artifact quality
* latency
* resource usage
* security
* zero-egress
* provenance completeness

This follows the Phase-5 quality model. 

---

# Phase 20 — Hardening & Security Validation

Adversarially test:

* prompt injection
* malicious documents
* unauthorized retrieval
* privilege escalation
* tool misuse
* credential leakage
* sandbox escape
* filesystem escape
* network egress
* resource exhaustion
* corrupted inputs
* conflicting evidence
* stale evidence
* model failure
* verification failure
* partial execution

The system should demonstrate that it **fails safely**, not merely that it works under ideal inputs.

---

# Phase 21 — Final MVP Qualification

Final qualification should be a gate:

```text
PRD Requirements
       ↓
System Requirements
       ↓
Architecture
       ↓
Implementation
       ↓
Integration
       ↓
Evaluation
       ↓
Security
       ↓
Hardware
       ↓
Sovereignty
       ↓
Human Acceptance
       ↓
       PASS
```

The final question becomes:

> **Does the implemented system satisfy the frozen PRD under the validated deployment and quality envelope?**

---

## The complete roadmap from here

| Phase  | Objective                           | Main output                          |
| ------ | ----------------------------------- | ------------------------------------ |
| **9**  | System Requirements                 | SRS                                  |
| **10** | System Architecture                 | Architecture baseline                |
| **11** | Architecture/Technology Decisions   | ADRs + technology baseline           |
| **12** | Component Architecture              | Component specifications             |
| **13** | Data & Knowledge Architecture       | Evidence/data architecture           |
| **14** | Agent & Tool Architecture           | Execution architecture               |
| **15** | Security & Sovereignty Architecture | Security architecture                |
| **16** | Deployment Architecture             | Reference deployment                 |
| **17** | Technical Validation                | Architecture-risk evidence           |
| **18** | MVP Implementation                  | Working system                       |
| **19** | Integration & Evaluation            | Qualification results                |
| **20** | Hardening                           | Security/reliability-hardened system |
| **21** | Final Qualification                 | MVP release/demo                     |

### Important boundary

From this point onward, the project changes character:

**Phases 0–8:**
`Research → Product Definition → PRD`

**Phases 9–16:**
`PRD → Engineering Definition → Architecture`

**Phases 17–21:**
`Architecture → Implementation → Validation → Qualification`

So the **next immediate phase is Phase 9 — System Requirements Specification**, not model selection and not coding.

The final PRD already establishes the product boundary; the job now is to turn that product contract into an **engineering contract** without reopening decisions that have already been closed. 
