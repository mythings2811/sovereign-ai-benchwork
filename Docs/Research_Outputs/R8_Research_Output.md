**Objective:** Complete R8 — Regulatory / Security Research for the Sovereign Agentic AI Workbench, using R1–R7 as the accumulated evidence base and converting regulatory/security findings into enforceable product requirements, rejected approaches, residual risks, and architecture questions.

# R8 — Regulatory / Security Research

## 1. Research Stream

**Research Stream:** R8 — Regulatory / Security Research

**R8 purpose:** Determine whether the Workbench can provide **technically demonstrable sovereignty and controlled agent execution**, rather than merely asserting that data is private. The supplied R8 control document explicitly requires the chain **Claim → Threat → Attack mechanism → Control → Verification mechanism → Residual risk**.  

R8 is correctly positioned as the final validation layer after R1–R7: security/regulatory research is supposed to consume the complete accumulated research rather than restart technology discovery. 

The project's hard constraints remain binding: confidential data stays inside controlled infrastructure, no external AI dependency for core operation, multiple open-weight models, controlled/observable agents, sandboxed and verified code, single-server/mid-range-GPU MVP feasibility, and technically demonstrable sovereignty. 

---

# 2. R8-01 — Sovereignty Is a Security Property, Not a Network Setting

### Research Topic

Technical sovereignty / zero-egress assurance

### Research Question

What must be true before the Workbench can credibly claim that confidential information remains within the controlled environment?

### Sources

[CERT-In Directions / FAQs](https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf?utm_source=chatgpt.com)

[MeitY GI Cloud Reference Architecture](https://egovstandards.gov.in/sites/default/files/2026-03/GI%20Cloud%20Reference%20Architecture.pdf?utm_source=chatgpt.com)

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf?utm_source=chatgpt.com)

### Source Type

Government guidance / standards / security framework.

### Key Finding

**FACT:** No single control establishes sovereignty.

A system can have local model inference while still permitting unintended network egress, external DNS resolution, remote telemetry, update downloads, third-party dependencies, unauthorized tool connections, or supply-chain compromise.

CERT-In's incident/logging requirements reinforce the need for security events to be recorded and retained; MeitY's cloud architecture treats security governance, operations, encryption, data integrity and location as distinct concerns; NIST treats AI security as a lifecycle risk rather than a deployment flag.

**INFERENCE:** The Workbench's sovereignty claim therefore needs at least five independently controlled dimensions:

```text
1. Data boundary
2. Network boundary
3. Identity / authorization boundary
4. Supply-chain boundary
5. Evidence / audit boundary
```

### Evidence

The existing R4 research already established that an air-gap requires offline artifact/model management and that zero-egress must be measured rather than asserted. 

R5 additionally established that local deployment does not remove prompt-injection or agent-manipulation risk. 

### Project Relevance

This is the central claim of the product.

### Implication

The Workbench should define **Sovereignty Evidence** as a composite property:

```text
Sovereignty =
    network enforcement
  + observed traffic
  + dependency closure
  + local model/artifact provenance
  + authorization evidence
  + execution evidence
  + immutable audit trail
```

A customer-facing “Sovereign” status should be **derived from these checks**, not supplied by the application.

### Limitations / Failure

No technical architecture can prove the absence of every undiscovered covert channel. The assurance level depends on the threat model, hardware trust assumptions, operating system, administrators, physical access and customer network architecture.

### Confidence

**High**

### Open Question

What minimum evidence package will target customers consider sufficient to substantiate “zero external data transfer”?

---

# 3. R8-02 — Zero-Egress Requires Enforcement Outside the AI Application

### Research Topic

Network isolation and egress proof

### Research Question

Can the Workbench prove that agents, models, tools and sandboxes cannot exfiltrate information?

### Sources

[CERT-In Cyber Security Audit Guidelines 2025](https://www.cert-in.org.in/PDF/Comprehensive_Cyber_Security_Audit_Policy_Guidelines.pdf?utm_source=chatgpt.com)

[MeitY Cloud Security Best Practices](https://www.meity.gov.in/writereaddata/files/2.%20WI3_Cloud%20Security%20Best%20Practices_06112020.pdf?utm_source=chatgpt.com)

[NCIIPC CII Guidelines](https://nciipc.gov.in/documents/NCIIPC_Guidelines_V2.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** Application-level assertions such as `network_enabled=false` are not sufficient security evidence.

A process may communicate through dependencies that the application does not explicitly classify as network calls. DNS, package managers, runtime update paths, model-loading logic, telemetry libraries, container interfaces and administrative channels all need consideration.

CERT-In's 2025 audit guidance expects broad coverage of networks, applications, OT/ICS, APIs, code, data security and incident response rather than a narrow application review.

### Evidence

R4 already concluded that:

```text
Application
   ↓
host / namespace enforcement
   ↓
firewall / network policy
   ↓
traffic observation
   ↓
independent evidence
```

is materially stronger than relying on the application itself. 

### Project Relevance

The Workbench's sovereignty demonstration is an explicit MVP requirement. 

### Implication

The deployment architecture should enforce egress at multiple layers:

```text
Agent/tool/sandbox
      ↓
namespace / interface controls
      ↓
host firewall / allowlist
      ↓
network boundary
      ↓
packet / flow monitoring
      ↓
audit evidence
```

The system should also deliberately test:

* direct TCP/UDP attempts
* DNS
* IPv6
* proxy paths
* localhost-to-host escape paths
* container networking
* model download attempts
* package-manager activity
* telemetry endpoints
* retry/failure paths
* malicious generated code.

### Limitations / Failure

Packet observation proves observed behavior; it does not by itself prove the nonexistence of a hidden hardware or firmware channel.

### Confidence

**High**

### Open Question

Whether the customer will permit packet capture, DNS telemetry, eBPF-based monitoring or equivalent network instrumentation in the highest-security deployment.

---

# 4. R8-03 — Air-Gap Also Requires Supply-Chain and Update Sovereignty

### Research Topic

Offline deployment / supply-chain assurance

### Research Question

What happens when the Workbench is air-gapped but its software, models and dependencies originate from external ecosystems?

### Sources

[CERT-In AI/OEM Security Guidelines 2026](https://www.cert-in.org.in/PDF/OEM_and_Technology_Providers_Guidelines.pdf?utm_source=chatgpt.com)

[CERT-In SBOM / AIBOM Guidelines v2.0](https://cert-in.org.in/PDF/TechnicalGuidelines-on-SBOM,QBOM&CBOM,AIBOM_and_HBOM_ver2.0.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** A disconnected runtime can still consume untrusted software or model artifacts.

CERT-In's 2026 technology-provider guidance calls for vulnerability assessment, software composition analysis, dependency analysis, threat modelling, penetration testing, continuous monitoring and updated inventories. Its SBOM/xBOM guidance recommends SBOM use for government/public-sector/essential-service procurement and points to SPDX or CycloneDX formats, VEX and vulnerability integration.

### Evidence

The official guidance specifically extends visibility to software, hardware, cryptography, AI and related dependencies.

### Project Relevance

The Workbench will necessarily contain:

```text
OS
CUDA / drivers
Python packages
containers
inference engines
models
tokenizers
OCR models
embedding models
rerankers
document parsers
sandbox runtimes
Office libraries
security tooling
```

### Implication

A **Sovereign Release Bundle** should become a first-class product artifact:

```text
Release Manifest
 ├── application version
 ├── model hashes
 ├── model licenses
 ├── container digests
 ├── package lockfiles
 ├── SBOM
 ├── AIBOM
 ├── VEX
 ├── cryptographic signatures
 ├── CVE status
 ├── compatibility matrix
 └── verification instructions
```

The customer-side deployment should verify the bundle **before installation**, not merely trust its source.

### Limitations / Failure

SBOMs provide inventory visibility; they do not guarantee that a component is benign.

### Confidence

**High**

### Open Question

What level of artifact signing, provenance attestation and offline update approval is appropriate for the defence/high-assurance deployment profile?

---

# 5. R8-04 — CERT-In Creates a Real Auditability Requirement

### Research Topic

Indian cybersecurity audit requirements

### Research Question

How should the Workbench be designed so that a customer can audit the complete AI system rather than only its web application?

### Source

[CERT-In Comprehensive Cyber Security Audit Policy Guidelines 2025](https://www.cert-in.org.in/PDF/Comprehensive_Cyber_Security_Audit_Policy_Guidelines.pdf?utm_source=chatgpt.com)

### Source Type

Government cybersecurity guideline.

### Key Finding

**FACT:** CERT-In's 2025 audit guidance calls for comprehensive ICT coverage and identifies a broad assessment universe including applications, networks, cloud infrastructure, OT/ICS, APIs, databases, source code, data security, incident response, AI systems, vendor risk and software/AI bills of materials. It states that audits should occur at least annually, with additional audits based on risk and after major changes.

### Project Relevance

This maps unusually well to the Workbench's architecture because the product itself crosses all of these surfaces.

### Implication

Auditability must be an **architectural primitive**, not a post-hoc reporting module.

The Workbench should maintain an inventory of:

```text
Model
Model revision
Inference engine
Parser version
Embedding / reranker
Tool version
Sandbox version
Policy version
Network policy
Configuration
Dependency versions
Security findings
Test results
```

A major version change should trigger a security/regression qualification process.

This extends R4's version-pinned serving architecture and R7's evaluation-environment fingerprinting. 

### Limitations / Failure

CERT-In applicability and detailed obligations can depend on the organization, sector and contractual context.

### Confidence

**High**

### Open Question

Which changes count as “major” for Workbench purposes and should therefore automatically invalidate a prior security qualification?

---

# 6. R8-05 — DPDP Requires Data Governance Even in a Sovereign Deployment

### Research Topic

Digital personal data protection

### Research Question

Does keeping enterprise AI on-premise eliminate data-protection obligations?

### Sources

[MeitY Digital Personal Data Protection Rules 2025](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025686cadad39.pdf&utm_source=chatgpt.com)

[India DPDP Act 2023](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** Local deployment does not remove personal-data governance requirements.

The DPDP framework places obligations on Data Fiduciaries around lawful processing, reasonable security safeguards, breach response and other data-governance requirements. The 2025 Rules establish a staged implementation model and additional obligations for Significant Data Fiduciaries.

**Important qualification:** The DPDP regime does **not** amount to a universal “all Indian personal data must stay in India” rule. Cross-border transfer restrictions and sectoral localisation requirements operate separately.

### Evidence

The 2025 Rules include security safeguards, breach notification mechanisms and additional SDF obligations. Rule 13 includes DPIA/audit duties for SDFs and a mechanism for restricting transfer of specified categories of personal data and associated traffic data.

### Project Relevance

The Workbench can process:

* employee correspondence
* vendor contact information
* financial records
* inspection personnel data
* HR material
* identity records
* customer information.

Therefore personal data can enter the Workbench even though the core product is not a consumer data platform.

### Implication

The data layer needs:

```text
data classification
purpose
lawful-basis / processing metadata
owner
access scope
retention policy
deletion policy
legal hold
processor relationship
breach status
audit trail
```

R7's three-tier data model is therefore strengthened:

```text
Evidence Vault
     ↓
Derived Knowledge
     ↓
Operational Knowledge
```

with privacy metadata attached throughout, rather than treating privacy as a storage-layer concern only. 

### Limitations / Failure

Exact obligations depend on the organization's role, data type, sector and whether it is designated or later classified as a Significant Data Fiduciary.

### Confidence

**High**

### Open Question

What is the exact DPDP applicability and implementation schedule for each initial target customer category as of the customer's deployment date?

---

# 7. R8-06 — SDF-Level Governance Is a Product Readiness Signal, Not a Universal Requirement

### Research Topic

Significant Data Fiduciary obligations

### Research Question

Should the Workbench be designed to support the stronger DPDP governance regime even if the customer is not currently an SDF?

### Sources

[DPDP Rules 2025 — MeitY](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025686cadad39.pdf&utm_source=chatgpt.com)

### Key Finding

**FACT:** Rule 13 imposes stronger obligations on Significant Data Fiduciaries, including periodic DPIA/audit, reporting of significant observations, algorithmic due diligence and potential localisation restrictions for specified data.

**OBSERVATION:** The governance pattern is directly compatible with the Workbench's existing architecture.

### Implication

The product should be **SDF-ready** without claiming that every customer is legally subject to SDF duties.

Useful product capabilities include:

```text
AI system inventory
model/version registry
processing inventory
DPIA evidence export
algorithmic-change record
risk register
audit evidence
data-flow map
processor inventory
retention policy
```

### Limitations / Failure

Do not state that every enterprise must currently implement the full SDF regime. The designation mechanism and commencement schedule are deployment-specific and evolving.

### Confidence

**Medium-High**

### Open Question

Which DPDP controls should be mandatory across all Workbench deployments versus activated only by a customer policy/deployment profile?

---

# 8. R8-07 — CII/OT Changes the Architecture Fundamentally

### Research Topic

Critical Information Infrastructure / Operational Technology

### Research Question

Can the Workbench be placed directly inside a critical industrial control environment?

### Sources

[NCIIPC CII Guidelines](https://nciipc.gov.in/documents/NCIIPC_Guidelines_V2.pdf?utm_source=chatgpt.com)

[NCIIPC CII Identification Guidelines](https://nciipc.gov.in/documents/Guidelines_for_Identification_of_CII.pdf?utm_source=chatgpt.com)

[QCI-NCIIPC CAF for Critical Sector Entities](https://padd.qci.org.in/wp-content/uploads/2025/03/FAQs_Awareness-Programs_-CAF_CS_CSE_FAQs.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** Indian CII guidance explicitly treats critical systems and their IT/OT dependencies as a distinct security environment. QCI-NCIIPC's CAF extends controls through IT, OT/ICS, asset inventory, threat modelling, vulnerability assessment, penetration testing and defence-in-depth.

### Evidence

NCIIPC defines CII around the potential national-security/economic/public-safety consequences of incapacitation and places responsibility for protection on the operating entity.

The CAF introduces layered controls and explicitly aligns OT/ICS requirements with IEC 62443 and NIST SP 800-82.

### Project Relevance

The target customer set includes refineries, PSUs, industrial enterprises and defence-linked manufacturers. Some deployments may therefore touch or sit adjacent to CII.

### Implication

**Do not design the MVP as a free-form OT control agent.**

The safer architecture is:

```text
                 Enterprise AI Zone
                        │
                  governed gateway
                        │
                    DMZ / zone
                        │
             ┌──────────┴──────────┐
             │                     │
       OT observation        approved data transfer
             │                     │
          OT / ICS             source systems
```

The Workbench should initially support **analysis of OT/engineering information**, not direct autonomous manipulation of PLC/DCS/SIS/process-control state.

### Limitations / Failure

Whether a particular customer system is formally CII/protected depends on government designation and the specific system.

### Confidence

**High**

### Open Question

What precisely is the permitted data boundary between the Workbench and the customer's OT/ICS environment for refinery and PSU deployments?

---

# 9. R8-08 — Power-Sector Regulation Demonstrates the Need for Sector Profiles

### Research Topic

Sector-specific industrial regulation

### Research Question

Can one generic Workbench compliance model cover all industrial customers?

### Source

[Central Electricity Authority Cyber Security in Power Sector Regulations 2026](https://www.medianama.com/wp-content/uploads/2026/08/Central-Electricity-Authority-Cyber-Security-in-Power-Sector-Regulations-2026.pdf?utm_source=chatgpt.com)

### Source Type

Sector-specific government regulation, accessed through a secondary-hosted copy.

### Key Finding

**FACT:** The 2026 CEA regulations create power-sector-specific controls around OT/IT, cyber incident response, CISO responsibilities, monitoring, asset registers, isolation of CII and retention of security records; their commencement is scheduled for April 1, 2027, subject to provisions that may commence separately.

### Project Relevance

This is a concrete example that security obligations vary by sector and system criticality.

### Implication

The Workbench should use **deployment/security profiles**, not one universal compliance mode.

Suggested internal profiles:

| Profile                 | Intended environment                 | Core posture                                                          |
| ----------------------- | ------------------------------------ | --------------------------------------------------------------------- |
| Enterprise Confidential | industrial/private enterprise        | local-only, default-deny egress, governed agents                      |
| Government / CII        | government + critical infrastructure | stronger segmentation, audit, inventory, sector controls              |
| Defence / Restricted    | classified/defence-linked            | physical isolation where required, controlled media, higher assurance |
| High-Assurance          | extreme-security deployment          | optional one-way/physically isolated architecture                     |

These are **product profiles**, not legal classifications.

### Limitations / Failure

Power-sector regulations should not be generalized into requirements for refineries or every PSU.

### Confidence

**Medium-High**

### Open Question

Which sector profiles should be formally implemented first: general industrial, government/CII, defence, or energy/oil-and-gas?

---

# 10. R8-09 — Defence Deployments Need a Different Assurance Boundary

### Research Topic

Defence and classified information

### Research Question

What additional architectural constraints arise when the Workbench processes classified defence information?

### Sources

[Defence Security Manual for Licensed Defence Industries 2025](https://www.ddpmod.gov.in/sites/default/files/77f959c9e7b74c6c2eaafce2d6689965f7b35ea78757c3ea9ef2eb754810da0a/beabd9aab30691b4e4fc964347d15860f6402db3e2acfb48addf22b988ebde4d.pdf?utm_source=chatgpt.com)

[Defence Acquisition Procedure 2020](https://www.ddpmod.gov.in/sites/default/files/2024-02/dap-2020-11-nov-21_0_0.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** The 2025 defence security manual establishes minimum security safeguards for DPSUs and licensed defence companies and permits stronger project-specific requirements. It addresses classified information protection, personnel/security responsibilities, cyber security, audits, document security, subcontracting and physical safeguards.

It also states that defence organizations dealing with classified information can be subject to additional requirements beyond its baseline.

### Project Relevance

Defence-linked manufacturing is an explicit target environment.

### Implication

The Workbench should support:

```text
need-to-know access
Indian-resident accountable security roles
physical/media controls
classified-zone segregation
controlled update process
third-party/vendor controls
independent security assessment
security incident escalation
```

For high-security deployments, a workstation architecture should be capable of operating **without persistent connection to a general corporate network**.

### Critical qualification

Do not claim:

> “The Workbench is compliant with the Official Secrets Act.”

That is not a software property. Compliance depends on the customer's legal status, contracts, classification regime, facility controls and operating procedures.

### Confidence

**High**

### Open Question

What assurance level must the product itself achieve before it can be introduced into a classified customer environment?

---

# 11. R8-10 — Least Privilege Must Be Enforced Outside the Model

### Research Topic

Agent authorization and excessive agency

### Research Question

Can a language model safely determine its own permissions?

### Sources

[CERT-In AI/OEM Security Guidelines 2026](https://www.cert-in.org.in/PDF/OEM_and_Technology_Providers_Guidelines.pdf?utm_source=chatgpt.com)

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf?utm_source=chatgpt.com)

R5/R6 accumulated evidence.

### Key Finding

**FACT:** AI-specific security guidance emphasizes human oversight, monitoring, logging, threat modelling and controls around prompt injection, malicious code, credential theft, privilege escalation and data leakage.

**INFERENCE:** An LLM should never be the authority that grants itself capability.

R5 already established that indirect prompt injection can originate from enterprise documents and that tool access needs explicit policy boundaries. 

### Implication

Use:

```text
User identity
   ↓
Policy engine
   ↓
Security context
   ↓
Allowed capabilities
   ↓
Agent
   ↓
Typed tool request
   ↓
Policy re-check
   ↓
Execution
```

not:

```text
Agent → decide whether it is allowed
```

This directly extends the R6 security-context continuity finding. 

### Required minimum security context

```text
principal
role
session_id
task_id
classification
authorization_scope
data_boundary
source_permissions
policy_version
risk_class
approval_state
```

### Confidence

**High**

### Open Question

Which policy language and enforcement mechanism can express these controls without making the agent runtime unmanageably complex?

---

# 12. R8-11 — Prompt Injection Is Not Solved by Air-Gapping

### Research Topic

Indirect prompt injection

### Research Question

What security risk remains even when there is no external network connection?

### Sources

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf?utm_source=chatgpt.com)

[CERT-In AI/OEM Security Guidelines 2026](https://www.cert-in.org.in/PDF/OEM_and_Technology_Providers_Guidelines.pdf?utm_source=chatgpt.com)

[OWASP GenAI Security Project](https://genai.owasp.org/?utm_source=chatgpt.com)

### Key Finding

**FACT:** Malicious instructions can be embedded in retrieved content, documents, images, spreadsheets, tool outputs or other data supplied to an agent.

**Critical R5 conclusion:** air-gapping blocks external exfiltration paths but does not stop **instruction-confusion attacks**. 

### Implication

Maintain a hard separation between:

```text
CONTROL PLANE
 ├── policy
 ├── authorization
 ├── tool capabilities
 ├── workflow constraints
 └── approvals

DATA PLANE
 ├── documents
 ├── OCR
 ├── retrieved text
 ├── images
 ├── tool results
 └── user content
```

The model may interpret data-plane content, but data-plane content cannot directly change control-plane authority.

### Required controls

* untrusted-content labels
* tool policy outside model context
* strict typed tools
* approval for consequential actions
* content sanitization where appropriate
* prompt-injection evaluation corpus
* malicious-document regression tests.

### Confidence

**High**

### Open Question

Which prompt-injection classes can be prevented structurally and which can only be contained through least privilege and limited agency?

---

# 13. R8-12 — Sandboxing Must Remain Independent of Sovereignty Controls

### Research Topic

Generated-code security

### Research Question

Does a strong sandbox make generated code safe enough for the Workbench?

### Sources

[gVisor security documentation](https://gvisor.dev/docs/architecture_guide/security/?utm_source=chatgpt.com)

[Firecracker documentation](https://firecracker-microvm.github.io/?utm_source=chatgpt.com)

R5 sandbox research.

### Key Finding

**FACT:** Sandboxing reduces blast radius but does not eliminate all risk.

R5 established:

* plain Docker is insufficient as the sole boundary for hostile generated code;
* gVisor is a strong MVP candidate;
* Firecracker provides a stronger isolation option;
* network policy must remain independent from the sandbox. 

### Implication

Treat code execution as a **separate security domain**:

```text
Generated code
     ↓
policy evaluation
     ↓
isolated runtime
     ↓
read-only input projection
     ↓
resource/time limits
     ↓
network isolation
     ↓
output validation
     ↓
effect record
```

Do not allow the sandbox to receive broad access to:

* host filesystem
* credentials
* model directories
* enterprise network
* arbitrary sockets
* persistent secrets.

### Confidence

**High**

### Open Question

Whether gVisor is sufficient for the first commercial security profile or should be replaced by VM-level isolation for all deployments.

---

# 14. R8-13 — Security Must Cover the Entire AI Supply Chain

### Research Topic

Model / AI component security

### Research Question

Does ordinary software supply-chain security adequately cover an AI Workbench?

### Sources

[CERT-In SBOM/AIBOM Guidelines v2.0](https://cert-in.org.in/PDF/TechnicalGuidelines-on-SBOM,QBOM&CBOM,AIBOM_and_HBOM_ver2.0.pdf?utm_source=chatgpt.com)

[CERT-In AI/OEM Security Guidelines 2026](https://www.cert-in.org.in/PDF/OEM_and_Technology_Providers_Guidelines.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** CERT-In's recent guidance explicitly expands supply-chain visibility to AI-related components alongside conventional software and hardware.

### Implication

The Workbench should maintain an **AI Bill of Materials**, not just an SBOM:

```text
Application
Models
Model revisions
Quantization
Adapters
Tokenizers
Embeddings
Rerankers
OCR models
VLM processors
Prompts/policies
Inference engines
Datasets / evaluation corpus
Containers
Python packages
Drivers
CUDA
GPU firmware
```

Each component should have:

```text
identity
version
hash
origin
license
dependency
security status
approval status
```

### Confidence

**High**

### Open Question

Whether customer procurement teams will require formal AIBOM delivery as a contract artifact or treat it as internal security evidence.

---

# 15. R8-14 — AI Risk Management Should Become a Native Product Process

### Research Topic

AI governance framework

### Research Question

Can NIST AI RMF provide a useful internal governance structure for the Workbench?

### Sources

[NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf?utm_source=chatgpt.com)

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** NIST's framework structures AI risk management into **GOVERN, MAP, MEASURE and MANAGE** and explicitly recommends lifecycle testing, documentation, human oversight, provenance, inventory and ongoing monitoring.

The GenAI profile additionally addresses provenance, pre-deployment evaluation, incident disclosure and risk-specific governance.

### Project Relevance

This is directly compatible with R5/R6/R7:

```text
Govern
   ↓
Map
   ↓
Measure
   ↓
Manage
```

maps naturally onto:

```text
Policy
   ↓
Threat / workflow context
   ↓
TEVV + security tests
   ↓
Release / monitor / remediate
```

### Implication

Create an internal **AI System Record** for each model/workflow:

```text
intended purpose
risk class
model/version
data sources
known limitations
evaluation corpus
evaluation results
security tests
human-oversight policy
approved capabilities
deployment profile
incident history
change history
```

### Limitation

NIST AI RMF is voluntary guidance, not Indian law.

### Confidence

**High**

### Open Question

What should the Workbench expose directly to customers versus retain as internal engineering/governance evidence?

---

# 16. R8-15 — Critical Infrastructure Is Becoming an Explicit AI Governance Domain

### Research Topic

AI in critical infrastructure

### Research Question

Is the Workbench's industrial/critical-infrastructure target environment becoming a recognized special case in AI governance?

### Source

[NIST Trustworthy AI in Critical Infrastructure Profile project](https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure?utm_source=chatgpt.com)

[NIST Critical Infrastructure AI RMF Concept Note](https://www.nist.gov/system/files/documents/2026/04/08/Concept%20Note_%20Development%20of%20the%20NIST%20AI%20RMF%20Trustworthy%20Use%20of%20AI%20in%20Critical%20Infrastructure%20Profile.pdf?utm_source=chatgpt.com)

### Key Finding

**FACT:** In April 2026, NIST began development of a dedicated AI RMF profile for trustworthy AI in critical infrastructure, explicitly covering AI across IT, OT and ICS and focusing on safety, security, reliability, capacity and efficiency.

### Implication

This strengthens—not establishes as law—the project's decision to treat industrial AI differently from consumer AI.

The Workbench should model:

```text
AI risk
+
operational consequence
+
connectivity
+
autonomy
+
data sensitivity
```

rather than model quality alone.

### Confidence

**High** for the direction; **Medium** for the eventual final requirements of the profile because the work is still under development.

### Open Question

What controls will the final critical-infrastructure AI profile formalize, and how closely will they map to the Workbench's deployment profiles?

---

# 17. R8-16 — EU AI Act Is a Useful Global Design Benchmark, Not an Indian Legal Requirement

### Research Topic

International regulatory readiness

### Research Question

Would an AI-Act-aware architecture improve the Workbench's global defensibility?

### Sources

[EU AI Act consolidated 2026 text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02024R1689-20260727&utm_source=chatgpt.com)

[European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com)

### Key Finding

**FACT:** The EU AI Act establishes risk-based obligations around risk management, documentation, logging, human oversight, accuracy, robustness and cybersecurity for high-risk systems. The Act became broadly applicable on August 2, 2026, with staggered implementation dates for different obligations and use cases.

### Project Relevance

These requirements independently converge with R5/R6/R8:

```text
risk management
logging
human oversight
technical documentation
testing
accuracy/robustness
cybersecurity
post-deployment monitoring
```

### Implication

The Workbench should be **EU-AI-Act-ready by architecture**, without representing that the Act governs an Indian deployment automatically.

### Limitation

Applicability depends on the product's role, market, intended purpose and deployment context.

### Confidence

**High**

### Open Question

What exact provider/deployer/component role would the Workbench occupy in a future EU deployment?

---

# 18. Consolidated Security Proof Model

The R8 research now allows the project's original proof model to be made more concrete.

The supplied research control layer requires:

```text
Claim
 ↓
Threat
 ↓
Attack mechanism
 ↓
Control
 ↓
Verification
 ↓
Residual risk
```



For the Workbench:

| Security claim                           | Threat                             | Control                                               | Verification                              | Residual risk                  |
| ---------------------------------------- | ---------------------------------- | ----------------------------------------------------- | ----------------------------------------- | ------------------------------ |
| Confidential data does not leave         | malicious/unintended egress        | default-deny host/network policy                      | packet/flow telemetry + adversarial tests | undiscovered channel           |
| Agent cannot exceed permissions          | prompt injection / confused deputy | external policy engine + least privilege              | authorization trace                       | policy/model integration error |
| Generated code cannot compromise host    | malicious code / sandbox escape    | gVisor/Firecracker + resource and network controls    | escape tests + runtime telemetry          | sandbox vulnerability          |
| Retrieved evidence is authorized/current | stale or unauthorized source       | ACL + authority + revision filtering                  | evidence-status checks                    | bad metadata                   |
| Artifact is safe to release              | synthesis/validation error         | deterministic validators + evidence checks + approval | release gate                              | validator blind spot           |
| Software supply chain is controlled      | compromised dependency/model       | signed manifest + SBOM/AIBOM/VEX                      | offline verification                      | compromised trusted component  |
| Audit trail is trustworthy               | tampering / omission               | append-only/tamper-evident logs                       | integrity verification                    | privileged compromise          |
| Sovereignty claim is credible            | hidden egress/dependency           | structural isolation + independent observation        | repeatable sovereignty test               | unknown covert path            |

This should become the basis for the eventual **Sovereignty & Security Validation Protocol**.

---

# 19. R8 Architectural Consequence

The accumulated evidence now supports a stronger architecture than the original R4 diagram.

```text
                    USER
                      │
                      ▼
             Identity / Session
                      │
                      ▼
              Security Context
                      │
                      ▼
              Policy / Risk Gate
                      │
                      ▼
             Task + Capability Router
                      │
          ┌───────────┼────────────┐
          ▼           ▼            ▼
      Retrieval     Models       Tools
          │           │            │
          ▼           ▼            ▼
   Evidence Layer   Model GW    Tool Policy
          │           │            │
          └───────┬───┴────────────┘
                  ▼
             Agent Runtime
                  │
        ┌─────────┼──────────┐
        ▼         ▼          ▼
    Planning   Execution   Verification
        │         │          │
        └─────────┼──────────┘
                  ▼
           Approval Gate
                  │
                  ▼
         Deterministic Artifact
                  │
                  ▼
       Final Verification / Release
                  │
                  ▼
       Proof + Provenance Envelope
                  │
        ┌─────────┴──────────┐
        ▼                    ▼
   Audit / SIEM       Sovereignty Evidence

Cross-cutting:
────────────────────────────────────────────
Network Enforcement
Supply-Chain Controls
SBOM / AIBOM / VEX
Data Classification
Retention / Privacy
Security Monitoring
Change Management
Security Regression
────────────────────────────────────────────
```

This is the logical culmination of R4's modular architecture, R5's layered failure containment, R6's security-context continuity/proof-carrying execution, and R7's governed evidence system.   

---

# 20. Established Findings

These are the strongest R8 conclusions.

### EF-01 — Sovereignty must be continuously testable

**Status:** Established
**Confidence:** High

Sovereignty is not equivalent to “local inference” or “air-gapped network.” It requires enforceable and independently observable controls across network, data, identity, supply chain and audit layers.

---

### EF-02 — External AI API prohibition is necessary but insufficient

**Status:** Established
**Confidence:** High

Removing cloud AI dependencies does not solve unauthorized tool use, malicious documents, stale evidence, local privilege escalation, sandbox escapes or compromised dependencies.

---

### EF-03 — Policy authority must exist outside the model

**Status:** Established
**Confidence:** High

The agent should propose actions; an external policy/control layer should authorize them.

This follows directly from R5 prompt-injection and R6 security-context findings.  

---

### EF-04 — Auditability must be built into the architecture

**Status:** Established
**Confidence:** High

CERT-In's current audit framework and the project's own sovereignty requirement both push toward comprehensive, traceable evidence rather than application logs alone.

---

### EF-05 — Supply-chain control is part of sovereignty

**Status:** Established
**Confidence:** High

Models, containers, packages, drivers, OCR engines and inference infrastructure are part of the trusted computing base.

---

### EF-06 — Data sovereignty and privacy are different properties

**Status:** Established
**Confidence:** High

Keeping data physically local does not automatically satisfy privacy governance; conversely, DPDP does not universally require all personal data to remain in India.

---

### EF-07 — CII/OT deployments need a distinct security boundary

**Status:** Established
**Confidence:** High

The Workbench should analyze and process industrial knowledge without becoming a free-form autonomous bridge into control systems.

---

### EF-08 — Risk-based human oversight is structurally necessary

**Status:** Established
**Confidence:** High

R1 trust research, R5 failure research, R6 verification research, NIST guidance, EU AI Act design and Indian cybersecurity guidance all converge on the same architectural pattern: autonomy must be proportional to consequence.

---

# 21. Relevant Findings

The findings with the greatest direct impact on product design are:

| Finding                                                 | Product impact             | Status                                                          |
| ------------------------------------------------------- | -------------------------- | --------------------------------------------------------------- |
| Sovereignty Evidence Record                             | core product capability    | **Preferred**                                                   |
| Host/network-enforced zero egress                       | infrastructure requirement | **Mandatory**                                                   |
| External authorization engine                           | agent security             | **Preferred**                                                   |
| Persistent execution security context                   | cross-component security   | **Strong Candidate**                                            |
| Proof-carrying action envelope                          | consequential actions      | **Strong Candidate**                                            |
| SBOM + AIBOM + VEX                                      | supply chain               | **Strong Candidate → near-Mandatory for regulated deployments** |
| Security/change qualification per model/runtime version | release engineering        | **Mandatory**                                                   |
| Data classification + retention engine                  | privacy/compliance         | **Strong Candidate**                                            |
| Sector-specific deployment profiles                     | commercial architecture    | **Preferred**                                                   |
| OT/ICS isolation gateway                                | industrial deployments     | **Strong Candidate**                                            |
| Tamper-evident audit store                              | assurance                  | **Preferred**                                                   |
| Independent security regression suite                   | validation                 | **Mandatory**                                                   |

---

# 22. Rejected Approaches

### R8-RJ01 — “Air-gapped = secure”

**Rejected.**

Prompt injection, malicious code, privilege abuse and compromised local components remain possible.

---

### R8-RJ02 — Application-only egress blocking

**Rejected.**

The control can be bypassed or undermined by infrastructure, runtime or dependency behavior.

---

### R8-RJ03 — Application logs as proof of zero egress

**Rejected.**

The component making the claim should not be the sole verifier of the claim.

---

### R8-RJ04 — One universal compliance profile

**Rejected.**

Industrial enterprise, government/CII and defence environments have materially different requirements.

---

### R8-RJ05 — LLM decides whether an action is permissible

**Rejected.**

Authorization cannot depend on the component being authorized.

---

### R8-RJ06 — SBOM alone

**Rejected as incomplete.**

AI models, model revisions, inference engines and AI-specific dependencies require additional provenance.

---

### R8-RJ07 — Sandbox alone

**Rejected.**

Sandbox isolation does not independently solve network, credential, resource, policy or supply-chain risks. R5 already established this. 

---

### R8-RJ08 — “ISO 27001 compliant” as the product's sovereignty claim

**Rejected.**

ISO certification and sovereignty are related but non-equivalent. A certification framework cannot substitute for technical evidence of actual deployment behavior.

---

### R8-RJ09 — Direct autonomous OT/process control in MVP

**Rejected.**

The safety/security consequences exceed the evidence currently available and are unnecessary to prove the Workbench's core value proposition.

---

# 23. Failure / Risk Findings

| Failure                              |    Severity | Detection                                 | Primary mitigation                    |
| ------------------------------------ | ----------: | ----------------------------------------- | ------------------------------------- |
| Hidden egress path                   |    Critical | packet/flow monitoring                    | infrastructure-level default deny     |
| Malicious enterprise document        |        High | adversarial test + content classification | data/control-plane separation         |
| Privilege escalation via tool        |    Critical | authorization trace                       | external policy enforcement           |
| Compromised model/package            |        High | signatures/SBOM/VEX                       | offline signed release pipeline       |
| Sandbox escape                       |    Critical | adversarial escape suite                  | gVisor/Firecracker + defence in depth |
| Audit log tampering                  |        High | hash/integrity verification               | append-only/tamper-evident store      |
| Stale/conflicting privacy metadata   |        High | policy consistency checks                 | data governance layer                 |
| Wrong CII boundary                   |    Critical | architecture review                       | deployment-specific zoning            |
| Regulatory drift                     | Medium-High | regulatory monitoring                     | compliance-control versioning         |
| Excessive autonomy                   |        High | risk classifier                           | risk-based approval gates             |
| Retention conflict                   | Medium-High | policy engine                             | classification + legal-hold semantics |
| Customer-specific sector rule missed |        High | compliance matrix                         | deployment profile selection          |

---

# 24. Open Questions

R8 does **not** eliminate all uncertainty. These remain genuine engineering/legal questions:

### OQ-01

What exact security classification/deployment profile is the first commercial target?

### OQ-02

What Indian sector-specific obligations apply separately to:

* refinery / oil & gas
* PSU
* general manufacturing
* government office
* defence-linked manufacturing.

### OQ-03

What exact customer evidence is required before they accept a zero-egress claim?

### OQ-04

What is the acceptable log-retention period when privacy minimization and security/forensics requirements conflict?

### OQ-05

How should immutable audit evidence coexist with data-subject deletion requirements?

### OQ-06

What level of hardware/firmware attestation is realistically achievable on the MVP workstation?

### OQ-07

Should high-assurance deployments mandate Firecracker rather than gVisor?

### OQ-08

Which security certifications should eventually be pursued: ISO 27001-related assurance, STQC, Common Criteria, customer-specific assessment, or some combination?

### OQ-09

What constitutes a “major” AI system change that forces requalification?

### OQ-10

What OT/ICS data-transfer architecture will be acceptable to refinery and PSU security teams?

### OQ-11

How should model licensing, model provenance and foreign-origin components be handled for defence deployments?

### OQ-12

What exact role would the Workbench occupy under the EU AI Act for future international deployments?

---

# 25. Architecture / Engineering Questions

These should now be handed to the architecture/engineering phase rather than reopened as open-ended research.

## Security Policy Kernel

* RBAC, ABAC or hybrid?
* Which policy language?
* How are permissions evaluated at every tool boundary?
* How are emergency overrides handled?
* How is policy versioning captured?

## Sovereignty Proof

* What network instrumentation is mandatory?
* Where is egress enforced?
* How are DNS and IPv6 controlled?
* How are packet/flow records made tamper-evident?
* What is the minimum reproducible “zero-egress test”?

## Identity / Security Context

R6 already identifies the need for continuity across boundaries. 

Architecture must determine:

```text
principal
role
task
session
classification
policy
authorization
risk
approval
provenance
```

and how these are cryptographically or otherwise strongly bound to actions.

## Audit Architecture

* append-only database or WORM object store?
* hash chain or signed event records?
* customer SIEM integration?
* offline audit export?
* time synchronization?
* administrator activity logging?

## Supply Chain

* offline registry?
* signing authority?
* model verification?
* SBOM/AIBOM schema?
* VEX handling?
* vulnerability requalification?
* rollback?

## Data Governance

* classification engine
* retention engine
* deletion engine
* legal hold
* privacy metadata
* processor inventory
* data-flow mapping.

## AI Security Testing

The Workbench needs a permanent security regression suite covering:

```text
prompt injection
indirect prompt injection
malicious files
tool manipulation
privilege escalation
credential exposure
sandbox escape
resource exhaustion
egress attempts
poisoned knowledge
wrong-session retrieval
stale knowledge
model substitution
artifact manipulation
```

## Deployment Profiles

The architecture should permit configuration without changing the underlying software:

```text
Enterprise
Government/CII
Defence/Restricted
High-Assurance
```

---

# 26. R8 Decision Register

| ID    | Decision / Principle                                                                  | Status               | Confidence  |
| ----- | ------------------------------------------------------------------------------------- | -------------------- | ----------- |
| R8-01 | Sovereignty is a composite, continuously testable property                            | **Preferred**        | High        |
| R8-02 | Zero-egress enforcement must be external to application logic                         | **Mandatory**        | High        |
| R8-03 | Sovereignty includes offline supply-chain control                                     | **Mandatory**        | High        |
| R8-04 | Security evidence must be audit-native                                                | **Preferred**        | High        |
| R8-05 | Data classification/privacy metadata must propagate through the workflow              | **Strong Candidate** | High        |
| R8-06 | Workbench should be SDF-ready without assuming SDF applicability                      | **Strong Candidate** | Medium-High |
| R8-07 | OT/ICS should be separated through security zones/gateways                            | **Preferred**        | High        |
| R8-08 | Deployment profiles should replace universal compliance assumptions                   | **Preferred**        | High        |
| R8-09 | Defence deployments require a higher-assurance profile                                | **Strong Candidate** | High        |
| R8-10 | Authorization must exist outside the model                                            | **Preferred**        | High        |
| R8-11 | Prompt injection must be treated as an internal security threat                       | **Mandatory**        | High        |
| R8-12 | Sandbox and network isolation are independent controls                                | **Mandatory**        | High        |
| R8-13 | SBOM + AIBOM + VEX should be first-class release artifacts                            | **Strong Candidate** | High        |
| R8-14 | NIST AI RMF should inform internal governance/crosswalk                               | **Strong Candidate** | High        |
| R8-15 | Critical-infrastructure AI deserves differentiated risk treatment                     | **Strong Candidate** | High        |
| R8-16 | EU AI Act readiness should influence architecture without being treated as Indian law | **Strong Candidate** | High        |

---

# 27. R8 → Final System Thesis

R1–R7 progressively established:

```text
R1  → high-value confidential workflows
R2  → market need and adoption constraints
R3  → competitive expectation
R4  → viable technical building blocks
R5  → failure boundaries
R6  → differentiated mechanisms
R7  → governed evidence/data architecture
R8  → security, sovereignty and regulatory constraints
```

The cumulative architecture is therefore no longer simply:

> “a private ChatGPT with local models.”

It is better defined as:

> **A policy-bounded, evidence-governed, locally executable AI system whose actions, data flows, models, tools, artifacts and security boundaries are continuously observable and independently verifiable.**

The key transition is from:

```text
LOCAL AI
```

to:

```text
VERIFIABLE LOCAL AI EXECUTION
```

and from:

```text
AIR-GAPPED
```

to:

```text
TECHNICALLY DEMONSTRABLE SOVEREIGNTY
```

This is consistent with the project's stated purpose: the research is successful only when it materially improves the team's ability to design, build, validate and differentiate the Workbench. 

## Final R8 conclusion

**The architecture can satisfy the sovereignty objective, but only if sovereignty is treated as a system property spanning identity, policy, data, models, tools, sandbox, network, supply chain, artifact release and audit evidence.**

The strongest architectural consequence from R8 is therefore:

```text
                 SOVEREIGN AI WORKBENCH
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
     SECURITY          EVIDENCE         EXECUTION
        │                │                 │
     policy           provenance        controlled
     identity         audit             tools
     network          verification      sandbox
     supply chain     compliance        artifacts
     data governance  sovereignty       approvals
        │                │                 │
        └────────────────┼─────────────────┘
                         │
                         ▼
               INDEPENDENT ASSURANCE
```

That is the point at which the R4–R8 research becomes an architecture discipline rather than a technology catalogue.

### Source and control-layer grounding

The R8 conclusions above are grounded in the supplied research-control requirements to use source-based evidence, preserve contradictions and uncertainty, and finish with established findings, rejected approaches, relevant findings, open questions and architecture questions.  

**Suggestion:** R8 is now sufficient to freeze a **Security & Sovereignty Architecture Specification** next: trust boundaries, security contexts, policy enforcement points, audit schema, zero-egress proof protocol, deployment profiles, and the minimum assurance test suite.
