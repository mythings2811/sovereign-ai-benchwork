# Sovereign Agentic AI Workbench
## R1 User Research → R2 Market Research → R3 Competitor Research

**Research date:** 12 September 2026  
**Research scope:** Confidential enterprise knowledge work in industrial, engineering, government, PSU, defence-linked and other high-sensitivity environments.

---

## 0. Research Control Layer

### Authoritative project definition

The Sovereign Agentic AI Workbench is defined as a self-hosted, air-gapped AI execution environment for confidential enterprise knowledge work. It is intended to bring the productivity of modern AI assistants inside an organization's controlled infrastructure using local models, local knowledge, local tools, agentic execution, multimodal processing, artifact generation, verification, auditability and demonstrable network isolation.

### Hard constraints used in this research

- Confidential data remains inside the controlled environment.
- Core functionality does not depend on external AI APIs.
- Multiple open-weight models are supported and new models can be added without redesigning the product.
- Agent actions are controlled and observable.
- AI-generated code is sandboxed and verified before acceptance.
- MVP operation is feasible on a single workstation/server with a mid-range GPU.
- Hardware, caching, storage and retrieval infrastructure must be engineered precisely.
- The sovereignty claim must be technically demonstrable.

### Research order

R1 establishes users, workflows, pain points, current workarounds and requirements. R2 uses R1 to establish market conditions and adoption constraints. R3 uses R1+R2 to identify incumbent capabilities and competitive gaps. This is consistent with the supplied sequential research workflow.

### Evidence discipline

Evidence is prioritized as official documentation, research papers, standards/government sources, technical reports and independent technical analysis, with vendor material used when it documents actual product behavior or customer deployments. Vendor claims are not treated as independent validation. Search snippets are not treated as evidence.

### Classification

- **FACT:** directly supported by cited evidence.
- **OBSERVATION:** repeated pattern across sources.
- **INFERENCE:** conclusion derived from evidence.
- **ASSUMPTION:** currently unverified proposition.
- **OPEN QUESTION:** materially unresolved.

Confidence reflects evidence quality and corroboration, not certainty of business success.

---

# R1 — USER RESEARCH

## R1-01 — P&ID / engineering drawing review

**Research Stream:** R1 — User Research  
**Research Topic:** Engineering drawing and P&ID review  
**Research Question:** Where does engineering-drawing review create measurable knowledge-work burden, and what capabilities are required to assist without removing expert accountability?

**User / Organization**  
Process, instrumentation, control and safety engineers in EPC/oil-and-gas engineering environments.

**Actual Workflow**  
Engineers inspect complex engineering drawings/P&IDs, cross-check symbols, equipment/instrument relationships and design consistency, identify discrepancies, and review the results before acceptance.

**Pain Point**  
Important design errors are buried inside complex drawings and the review is labor-intensive. Engineering organizations therefore spend significant expert hours on repetitive quality checking.

**Current Solution**  
Manual expert review, supported by conventional engineering software and rule-based checks.

**Failure / Limitation**  
Manual review consumes engineering hours and can miss errors. AI approaches themselves remain constrained by data quality, preprocessing, security and legal issues; therefore model output cannot simply become an autonomous engineering approval.

**Required Capability**  
Multimodal drawing understanding, layout-aware extraction, domain-aware consistency checks, provenance/citations, confidence or uncertainty visibility, and human review before consequential action.

**Source**  
Rimma Dzhusupova, Richa Banotra, Jan Bosch, Helena Holmström Olsson, “Using artificial intelligence to find design errors in the engineering drawings,” *Journal of Software: Evolution and Process*, 2023. DOI: https://doi.org/10.1002/smr.2543

**Source Type:** Research paper / engineering case study.

**Key Finding**  
**FACT:** McDermott researchers developed AI software to quality-check complex P&IDs and identify design mistakes. The paper explicitly identifies data quality, preprocessing, security and legal constraints as challenges to industrial AI deployment.

**Evidence**  
The authors describe a deep-learning quality-checking system for P&IDs in the EPC industry and position the value in reducing engineering hours. They also state that industrial AI deployment requires overcoming data-quality, preprocessing, data-security and legal constraints.

**Project Relevance**  
Directly relevant to the workbench's stated multimodal engineering-drawing workload and sovereignty requirements.

**Implication**  
A serious workbench cannot treat scanned drawings as ordinary text documents. The system needs a separate visual/document intelligence path and must expose evidence to the engineer instead of returning an opaque conclusion.

**Limitations / Failure**  
The study is one industrial case and does not establish universal accuracy. It does not justify autonomous approval of engineering decisions.

**Confidence:** High for existence of workload and feasibility of AI assistance; Medium for generalizable productivity magnitude.

**Open Question**  
What accuracy, false-negative tolerance and review protocol are acceptable for specific drawing classes such as P&IDs, single-line diagrams and layout drawings?

**Researcher Notes**  
This is a high-value workflow because the cost of an error is much larger than the cost of a chatbot response. That increases the value of verification, traceability and human sign-off.

---

## R1-02 — Cross-document engineering change / Management of Change

**Research Stream:** R1 — User Research  
**Research Topic:** Cross-document dependency tracing in industrial engineering documentation  
**Research Question:** How do engineers identify the impact of a change across heterogeneous engineering documents, and where does existing information management break down?

**User / Organization**  
Process engineers and technical reviewers working with Shell engineering documentation in Management of Change (MoC) contexts.

**Actual Workflow**  
Engineers trace equipment tags, instrument identifiers and operating parameters across Word reports, Excel spreadsheets and engineering drawings, then determine which documents/sections may be affected by a change.

**Pain Point**  
Cross-document dependencies are latent rather than machine-readable. Engineers must manually trace relationships across multiple document types.

**Current Solution**  
Manual review, source-document search and engineer knowledge of domain conventions.

**Failure / Limitation**  
Manual tracing is slow and incomplete. A recent Shell/Huracán study demonstrates that even a purpose-built AI system can miss indirect chemical dependencies and a pure-addition P&ID case.

**Required Capability**  
Cross-document retrieval, entity resolution, provenance-preserving relationship extraction, change-impact reasoning and review prioritization.

**Source**  
Bas Filius, TU Delft MSc thesis, 2026, “Inferring Cross-Document Dependencies in Heterogeneous Engineering Documentation: A Knowledge Graph Approach to Management of Change Impact Analysis,” carried out at Huracán in collaboration with Shell. Repository: https://repository.tudelft.nl/file/File_fdfb2aa1-0f2e-474e-93a4-215095f7a905

**Source Type:** Academic thesis / industrial research.

**Key Finding**  
**FACT:** The study used nine document types across six process units and 12 Shell MoC cases. It achieved document-level macro recall 0.904, precision 0.706 and F1 0.776. In 9/12 cases, all modified documents were correctly identified.

**Evidence**  
The reported ground truth contained 467 change locations. Missed cases included enclosure-calculation documents linked through indirect chemistry-mediated dependencies and one pure-addition case where a P&ID was missed. The graph approach outperformed the strongest non-graph baseline on F1.

**Project Relevance**  
Directly relevant to the workbench's local enterprise retrieval and agentic analysis capabilities.

**Implication**  
Enterprise knowledge retrieval should not stop at semantic similarity. For engineering domains, the product should preserve structure, identifiers and provenance and support relationship-aware reasoning over heterogeneous documents.

**Limitations / Failure**  
The evaluation covered six process units from a single operator and explicitly states that cross-client generalizability was not established. Region-level localization performance was materially lower than document-level detection.

**Confidence:** High for the workflow/problem; Medium for generalization of reported metrics.

**Open Question**  
How much of the required dependency graph can be constructed automatically for a new enterprise without pre-existing asset registries or ontology work?

**Researcher Notes**  
This is a strong argument for an internal knowledge layer that preserves document provenance rather than flattening all enterprise content into an undifferentiated vector index.

---

## R1-03 — Inspection-report and technical-document processing

**Research Stream:** R1 — User Research  
**Research Topic:** Inspection, technical report and documented-safety-analysis workflows  
**Research Question:** Which inspection/reporting steps are repetitive enough to automate, and where do human review and validation remain necessary?

**User / Organization**  
Industrial safety/engineering teams, including a U.S. national laboratory environment and oilfield-service organizations.

**Actual Workflow**  
Collect source documents; extract relevant facts; consolidate evidence; draft analysis/report content; validate against source material; format and submit a controlled deliverable.

**Pain Point**  
Manual extraction and report preparation are time-consuming. Documents may be distributed across files and contain tables, images and structured evidence.

**Current Solution**  
Manual document review plus specialized low-code/internal software. In the INL case, AI was used in a controlled government-cloud environment to draft a documented safety-analysis chapter.

**Failure / Limitation**  
AI-generated material can contain formatting artifacts, omissions and failed cross-section validation. Therefore “document generation” is not equivalent to “validated report.”

**Required Capability**  
Document intelligence, structured extraction, source-linked synthesis, automated validation, template-constrained artifact generation and mandatory human review for high-consequence outputs.

**Source**  
Idaho National Laboratory / Nuclear Regulatory Commission-related case research: “Evaluation of AI-Enabled Digital Documented Safety Analysis: A Case Study” (2026). Use the INL/NRIC publication source for the detailed case record.  
Supporting enterprise example: Microsoft Learn, “SLB enhances productivity with Power Platform and AI,” https://learn.microsoft.com/en-us/power-platform/guidance/case-studies/slb-enhances-productivity

**Source Type:** Government laboratory / official enterprise case study.

**Key Finding**  
**FACT:** AI-assisted document workflows can reduce manual effort materially, but report generation still requires validation and human oversight. SLB also demonstrates production document-processing automation where AI extracts fields from large volumes of shipping/invoice documents and then applies business validation.

**Evidence**  
The INL evaluation reports an SME-estimated reduction in effort of roughly 50% for the studied documentation task, but also identifies formatting, redundancy, prompt artifacts, incomplete outputs and cross-section validation failures. SLB's official case study describes extraction of shipment details from documents and business validations; a related invoice workflow extracted 22 fields and produced an Excel report.

**Project Relevance**  
Direct match to inspection-report, technical-document and artifact-generation use cases.

**Implication**  
The workbench needs a verification stage between model output and final artifact. The output layer must be evidence-linked and template-aware rather than a simple “write a report” operation.

**Limitations / Failure**  
INL results are task-specific; SLB is a vendor-hosted enterprise case and should not be treated as an independent benchmark.

**Confidence:** High for workflow characteristics; Medium for quantified productivity.

**Open Question**  
Which validation checks can be deterministic and which still require a human reviewer for inspection, safety and regulatory documents?

**Researcher Notes**  
The product opportunity is stronger when the workbench owns the whole chain: extraction → grounding → analysis → validation → controlled artifact.

---

## R1-04 — Internal knowledge search

**Research Stream:** R1 — User Research  
**Research Topic:** Permission-aware internal knowledge retrieval  
**Research Question:** Why does conventional enterprise search fail for policy, technical and operational questions, and what must AI do differently?

**User / Organization**  
Employees, managers, engineers and technical staff working across distributed enterprise repositories.

**Actual Workflow**  
Search SharePoint/file repositories, identify the authoritative/current document, read relevant passages, reconcile context, and apply the answer to the task.

**Pain Point**  
Employees must understand repository structure and document hierarchy before they can locate authoritative information.

**Current Solution**  
SharePoint/search/repository navigation plus domain knowledge.

**Failure / Limitation**  
Keyword search produces document lists instead of direct, cited answers. Permission boundaries and version precedence complicate the problem.

**Required Capability**  
Permission-aware retrieval, source attribution, document authority/version precedence, hybrid retrieval, reranking and citation-backed synthesis.

**Source**  
IBM, “From scattered policies to grounded answers: Building a permission-aware knowledge assistant with IBM watsonx Orchestrate,” 23 July 2026, https://www.ibm.com/new/product-blog/building-a-permission-aware-knowledge-assistant-with-ibm-watsonx-orchestrate

**Source Type:** Official enterprise case study.

**Key Finding**  
**FACT:** In the SCEA case, more than 800 employees relied on policies, procedures, forms and operational documents distributed through Microsoft 365/SharePoint. The assistant was built to return answers with citations while preserving document permissions.

**Evidence**  
The case explicitly describes the repository-navigation problem and the need for central-office policy precedence over local documents in some cases. The retrieval layer validates permissions before returning document chunks and preserves source attribution.

**Project Relevance**  
Directly relevant to internal manuals, SOPs and historical organizational knowledge.

**Implication**  
The knowledge layer should treat authorization and document authority as first-class retrieval logic. A vector database by itself is not sufficient.

**Limitations / Failure**  
The SCEA productivity value was a business-case estimate rather than a measured production outcome. The pilot did not implement all hierarchy-ranking capabilities.

**Confidence:** High for workflow and access-control requirements; Medium for ROI.

**Open Question**  
How should conflicting document versions and conflicting departmental policies be ranked when metadata quality is poor?

**Researcher Notes**  
“RAG” should be interpreted as governed enterprise retrieval, not just embedding similarity.

---

## R1-05 — Confidential-data restrictions and shadow AI behavior

**Research Stream:** R1 — User Research  
**Research Topic:** Public AI usage for confidential work  
**Research Question:** Do employees actually avoid public AI when policy prohibits it, and what data flows are occurring?

**User / Organization**  
Knowledge workers in large enterprises, especially teams handling source code, intellectual property, financial information and controlled documents.

**Actual Workflow**  
Employees use AI for drafting, summarization, coding, data analysis and document work; information is often pasted or uploaded from enterprise systems into browser-based AI tools.

**Pain Point**  
Employees have a productivity incentive to use capable AI even when sanctioned channels are unavailable or slow.

**Current Solution**  
Mixture of official enterprise AI tools, personal accounts and ad hoc browser-based tools. Some organizations respond with blocking or restrictive policy.

**Failure / Limitation**  
Blocking does not eliminate demand and can shift users to other tools/accounts/devices. Unmanaged data transfer becomes difficult to observe.

**Required Capability**  
A capable sanctioned alternative inside the enterprise boundary, with policy enforcement, visible audit trails and enough functionality to compete with the convenience of public AI.

**Source**  
PagerDuty, “Shadow AI Survey,” 11 June 2026, https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/  
Supporting telemetry: LayerX “Enterprise AI and SaaS Data Security Report,” and Cyberhaven “2026 AI Adoption & Risk Report.”

**Source Type:** Commissioned survey / security telemetry.

**Key Finding**  
**FACT:** In PagerDuty's survey of 1,250 office professionals at organizations with at least $500M annual revenue, two-thirds reported using AI tools at work despite believing the use was not permitted. 88% reported sharing work-related information with public AI tools; 31% reported sharing financial information or confidential company documents/strategies. LayerX telemetry reports that 77% of users paste data into GenAI tools and that a large majority of those paste events occur through unmanaged accounts.

**Evidence**  
The PagerDuty survey also reports that 77% of respondents believe company AI restrictions limit professional growth. LayerX reports GenAI as a major corporate-to-personal data movement channel. These sources have different methods and populations; they should not be collapsed into one universal prevalence estimate.

**Project Relevance**  
Directly supports the need for a sanctioned, sovereign alternative rather than a “ban AI” strategy.

**Implication**  
Security and productivity are coupled. A sovereign workbench must be useful enough to displace unsafe workarounds, not merely secure enough for IT approval.

**Limitations / Failure**  
PagerDuty and LayerX are vendor-sponsored research. Exact prevalence varies materially with sample definition and telemetry method.

**Confidence:** High that shadow AI is a real enterprise phenomenon; Medium on exact prevalence percentages.

**Open Question**  
For the target Indian industrial/government market, what proportion of blocked or discouraged AI demand is actually being redirected to consumer tools or personal accounts?

**Researcher Notes**  
The strongest product argument is not “the cloud is dangerous”; it is “employees already have the demand, so provide a safer and equally useful path.”

---

## R1-06 — Trust, human approval and agent autonomy

**Research Stream:** R1 — User Research  
**Research Topic:** Trust requirements for AI agents  
**Research Question:** Which enterprise tasks users are willing to delegate, and where does trust collapse?

**User / Organization**  
Enterprise knowledge workers and senior decision-makers adopting AI agents.

**Actual Workflow**  
Employees use agents for analysis, collaboration, document work and increasingly multi-step workflows that interact with enterprise systems.

**Pain Point**  
High-stakes actions require confidence that the agent is correct, authorized and auditable.

**Current Solution**  
Mostly assisted workflows and point agents, with human review.

**Failure / Limitation**  
Trust decreases as consequences increase and as agents gain more autonomy. Governance maturity lags adoption.

**Required Capability**  
Human approval gates, explicit permissions, action previews, reversible operations where possible, complete execution traces, result validation and role-based tool access.

**Source**  
PwC, “PwC’s AI Agent Survey,” 16 May 2025, https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html  
Supporting source: Deloitte, “The State of AI in the Enterprise — 2026 AI report,” https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html

**Source Type:** Enterprise survey / industry research.

**Key Finding**  
**FACT:** PwC reports that 28% of surveyed executives ranked lack of trust in AI agents as a top-three challenge. Reported trust was higher for data analysis (38%), performance improvement (35%) and daily collaboration (31%), but much lower for financial transactions (20%) and autonomous employee interactions (22%). Deloitte reports that only roughly one in five companies has a mature governance model for autonomous AI agents.

**Evidence**  
Both sources independently show that adoption is advancing faster than governance and that trust is task-dependent rather than binary.

**Project Relevance**  
Directly determines the control model for the workbench's agent runtime.

**Implication**  
The agent should not be designed as an unconstrained autonomous worker. It should be designed as a policy-bounded executor whose autonomy level changes with task risk.

**Limitations / Failure**  
Survey data measures perceptions, not technical reliability. The numerical trust values are not direct probabilities of safe execution.

**Confidence:** High for directional trust pattern; Medium for exact percentages as universal parameters.

**Open Question**  
What risk taxonomy should determine when the workbench requires approval, dual control or completely disallows autonomous execution?

**Researcher Notes**  
The product UX should make “what the agent plans to do” and “what it actually did” visibly distinct.

---

## R1-07 — Current point solutions improve isolated workflow steps

**Research Stream:** R1 — User Research  
**Research Topic:** Existing internal automation in oilfield and industrial operations  
**Research Question:** What does enterprise automation already solve, and what remains fragmented?

**User / Organization**  
SLB operational, tax, project and delivery teams.

**Actual Workflow**  
Project discovery; validation/review; extracting structured fields from shipping documents/invoices; mapping information between systems; producing Excel outputs.

**Pain Point**  
Manual extraction, duplicate data entry, weak cross-site visibility and spreadsheet-driven review create delays and errors.

**Current Solution**  
Power Apps, Power Automate, AI Builder, Dataverse, SharePoint and Azure Functions.

**Failure / Limitation**  
These solutions are effective, but the documented examples are workflow-specific and ecosystem-specific. They do not establish a general-purpose sovereign execution layer.

**Required Capability**  
An extensible tool/agent layer that can execute across files, search, code, spreadsheets and internal systems while remaining governed.

**Source**  
Microsoft Learn, “SLB enhances productivity with Power Platform and AI,” https://learn.microsoft.com/en-us/power-platform/guidance/case-studies/slb-enhances-productivity

**Source Type:** Official enterprise case study.

**Key Finding**  
**FACT:** SLB used AI-powered project discovery to connect geographically distributed initiatives, automated document processing for shipping records, and an invoice workflow that extracted 22 fields and compiled an Excel output. The case reports processing more than 1,000 emails and 200 vendor invoices per month and states that the workflow saves approximately one FTE-equivalent workload.

**Evidence**  
The documented workflows combine AI extraction with deterministic validation and downstream system actions.

**Project Relevance**  
Shows the user is not asking merely for “AI answers”; the useful unit of value is an end-to-end business workflow.

**Implication**  
The workbench's differentiator should be orchestration of heterogeneous local capabilities rather than a better chat response alone.

**Limitations / Failure**  
Vendor case study; productivity figures are organization-specific.

**Confidence:** High for existence of the workflow pattern; Medium for ROI generalization.

**Open Question**  
Which generic tool abstractions cover most target enterprise workflows without becoming another proprietary low-code platform?

**Researcher Notes**  
The project should explicitly benchmark end-to-end completion, not isolated model accuracy.

---

## R1-08 — Users need familiarity plus governance

**Research Stream:** R1 — User Research  
**Research Topic:** User experience expectations for enterprise AI assistants  
**Research Question:** What makes a secure assistant acceptable enough to replace existing workarounds?

**User / Organization**  
Enterprise employees accustomed to browser-based assistants and productivity software.

**Actual Workflow**  
Natural-language request → attach or reference internal files → receive answer/draft → inspect/correct → export or execute.

**Pain Point**  
Security-approved systems can become unattractive when users must navigate complex infrastructure concepts or multiple separate tools.

**Current Solution**  
Public AI assistants for convenience, plus fragmented enterprise software.

**Failure / Limitation**  
The enterprise either loses productivity by forcing manual work or loses control by allowing unsanctioned external tools.

**Required Capability**  
Modern conversational UX, local file handling, transparent status, clear permissions, visible citations, action previews and a straightforward artifact path.

**Source**  
IBM SCEA case study and Open WebUI official documentation.  
IBM: https://www.ibm.com/new/product-blog/building-a-permission-aware-knowledge-assistant-with-ibm-watsonx-orchestrate  
Open WebUI: https://docs.openwebui.com/

**Source Type:** Official product documentation / enterprise case study.

**Key Finding**  
**OBSERVATION:** Successful private-AI implementations increasingly preserve a familiar conversational interface while hiding the underlying complexity. IBM kept the user interaction inside an existing Microsoft environment; Open WebUI explicitly positions itself as a self-hosted AI platform with RAG, tools and local models.

**Evidence**  
IBM's SCEA case states that keeping the interface in a familiar environment reduces adoption barriers. Open WebUI documents local deployment, model connectivity, RAG and tool calling.

**Project Relevance**  
Directly supports the “modern AI assistant inside company walls” UX goal.

**Implication**  
The product should abstract infrastructure complexity from end users while making security/permissions visible when they matter.

**Limitations / Failure**  
These sources document product design and a specific case, not a controlled comparative usability study.

**Confidence:** Medium.

**Open Question**  
Which UX elements are mandatory for high adoption among engineering and government users who are less tolerant of opaque automation?

**Researcher Notes**  
Do not copy consumer UI blindly. High-sensitivity workflows need stronger visibility and approval affordances than consumer assistants.

---

# R2 — MARKET RESEARCH

## R2-01 — Enterprise AI demand is real, but enterprise-scale deployment remains immature

**Research Stream:** R2 — Market Research  
**Research Topic:** Enterprise AI adoption stage  
**Research Question:** Is the market still experimental, or has demand moved into scaled organizational deployment?

**Research Question Answer**  
**FACT:** Enterprise AI usage is widespread, but scaling remains incomplete. This creates a market for infrastructure, governance and execution layers rather than just model access.

**Source**  
McKinsey, “The state of AI in 2025: Agents, innovation, and transformation,” 5 Nov 2025, https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

**Source Type:** Reputable industry research.

**Key Finding**  
88% of respondents reported regular AI use in at least one business function. Nearly two-thirds had not yet begun scaling AI across the enterprise. 62% reported at least experimenting with AI agents; 23% reported scaling an agentic AI system somewhere in the enterprise and 39% were experimenting. Knowledge management and IT were among the functions with the most agentic use.

**Project Relevance**  
The workbench should solve the scale problem, not merely participate in another pilot.

**Implication**  
The value proposition must be framed around repeatable, auditable end-to-end workflows with measurable outcomes.

**Limitations**  
Survey responses are not direct measurements of deployed system counts or revenue impact.

**Confidence:** High.

**Open Question**  
What portion of these enterprise deployments specifically require hard on-premise or air-gapped operation?

---

## R2-02 — The AI market is large, but sovereign AI is not a cleanly measured TAM

**Research Stream:** R2 — Market Research  
**Research Topic:** Market size and segment definition  
**Research Question:** What public market-size evidence exists specifically for sovereign/on-prem enterprise AI?

**Key Finding**  
**FACT:** Public analyst data supports a very large overall enterprise AI/GenAI market, but a standardized, independently measured “sovereign AI workbench” TAM is not clearly available.

**Evidence**  
IDC's FutureScape cites $307B enterprise AI spending in 2025, growing to $632B in 2028, and $69.1B GenAI spending in 2025 growing beyond $202B in 2028. Gartner forecast $643.86B worldwide GenAI spending in 2025. Neither figure is equivalent to the addressable market for an air-gapped workbench.

**Sources**  
IDC FutureScape 2025: https://info.idc.com/rs/081-ATC-910/images/US-IDC-FutureScape-2025-GenAI_ebook.pdf  
Gartner, 31 Mar 2025: https://www.gartner.com/en/newsroom/press-releases/2025-03-31-gartner-forecasts-worldwide-genai-spending-to-reach-644-billion-in-2025

**Source Type:** Market analyst.

**Project Relevance**  
Prevents the team from inventing an inflated sovereign-AI TAM from broad GenAI numbers.

**Implication**  
Market sizing should be bottom-up: number of target organizations × deployable sites/workgroups × annual software/support value, segmented by security class and workload. A top-down sovereign-AI TAM should be treated as an OPEN QUESTION until a defensible definition is established.

**Limitations**  
Published market definitions differ, and broad AI spend includes hardware, services and cloud that are not addressable by this product.

**Confidence:** High.

**Open Question**  
How many Indian and international target organizations operate the exact security boundary that makes external AI unacceptable or materially constrained?

---

## R2-03 — Manufacturing, engineering and knowledge management are unusually relevant use domains

**Research Stream:** R2 — Market Research  
**Research Topic:** Vertical attractiveness  
**Research Question:** Which enterprise functions show both AI demand and workflows aligned to the product's strengths?

**Key Finding**  
**OBSERVATION:** Manufacturing, energy/resource industries, engineering and knowledge management repeatedly appear as active AI domains, while their workflows also contain sensitive data, heterogeneous documents and operational dependencies.

**Evidence**  
McKinsey reports AI use in knowledge management, IT and manufacturing-related cost benefits. Deloitte identifies search/knowledge management as a major GenAI impact area and R&D/knowledge management among high-potential agentic use cases. The Federal Reserve reports accelerating work-related GenAI adoption in manufacturing. Industrial case studies show document extraction, project discovery, engineering drawing analysis and cross-document dependency analysis.

**Sources**  
McKinsey: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai  
Deloitte: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html  
Federal Reserve: https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

**Project Relevance**  
Strongly aligned to target organizations such as refineries, PSUs and engineering-heavy enterprises.

**Implication**  
The initial go-to-market should not target “all enterprise knowledge workers.” A vertical wedge around sensitive technical knowledge work is more defensible and easier to validate.

**Limitations**  
Cross-industry survey data does not directly establish purchase intent in the target Indian organizations.

**Confidence:** Medium-High.

**Open Question**  
Which single vertical has the shortest procurement path while still having the hard sovereignty pain needed to justify a new platform?

---

## R2-04 — Security, governance, integration and readiness are larger constraints than raw AI awareness

**Research Stream:** R2 — Market Research  
**Research Topic:** Adoption barriers  
**Research Question:** Why do enterprises fail to move from AI interest to production deployment?

**Key Finding**  
**FACT / OBSERVATION:** Organizations report growing AI usage, but infrastructure, data, risk/governance, talent, integration and workflow redesign remain binding constraints.

**Evidence**  
Deloitte reports that 42% of organizations consider strategy highly prepared while being less prepared on infrastructure, data, risk and talent; only 34% are deeply transforming. IDC predicts that over one-third of organizations would remain stuck in an experimental, point-solution phase in 2026 and explicitly identifies integration with legacy systems/data architectures and specialized talent as obstacles. PwC reports workflow integration and organizational change as material barriers to agents.

**Sources**  
Deloitte: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html  
IDC: https://info.idc.com/rs/081-ATC-910/images/US-IDC-FutureScape-2025-GenAI_ebook.pdf  
PwC: https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html

**Project Relevance**  
The workbench must reduce integration and operational burden, not merely provide a model endpoint.

**Implication**  
The product architecture should package the execution loop, model management, retrieval, tools, logging and verification as one operational unit.

**Limitations**  
Most published surveys cover broader enterprise AI, not air-gapped industrial deployments.

**Confidence:** High.

**Open Question**  
Which implementation complexity will become the dominant bottleneck in a mid-range GPU, single-server deployment: inference, document processing, retrieval, or agent/tool orchestration?

---

## R2-05 — India provides a strategically supportive sovereignty context

**Research Stream:** R2 — Market Research  
**Research Topic:** India-specific sovereign AI momentum  
**Research Question:** Does India's current policy and infrastructure direction support demand for sovereign/private AI?

**Key Finding**  
**FACT:** India is explicitly building domestic AI capability and articulating trust, accountability, understandable systems and sovereign capability as national priorities.

**Evidence**  
The February 2026 India AI Governance Guidelines describe trust as foundational, emphasize meaningful human control, accountability and understandable-by-design systems, and encourage resource-efficient lightweight models. A 6 Aug 2026 PIB release states that the IndiaAI Mission has a five-year outlay of Rs. 10,371.92 crore, 15 compute-service providers, 237 supported compute projects, 93.18 lakh sanctioned GPU hours, 20 indigenous foundation-model proposals selected, and 20 AI solutions deployed across public-sector institutions.

**Sources**  
MeitY / PIB, “India’s AI Governance Philosophy,” 15 Feb 2026: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026215790801.pdf  
Press Information Bureau, 6 Aug 2026: https://www.pib.gov.in/PressReleasePage.aspx?lang=1&PRID=2295477&reg=48

**Source Type:** Government.

**Project Relevance**  
Directly relevant to Indian government/PSU and strategic-industry deployments.

**Implication**  
India is not merely an end market; it is a policy environment in which domestic compute, indigenous models and trusted AI are increasingly legitimate procurement narratives.

**Limitations**  
National policy does not prove that target enterprises will buy this particular product.

**Confidence:** High for policy direction; Medium for commercial demand.

**Open Question**  
Which procurement mechanisms or public-sector programs can shorten the path from pilot to paid deployment for sovereign enterprise AI?

---

## R2-06 — Buyers are moving toward agents, but expect governance to catch up

**Research Stream:** R2 — Market Research  
**Research Topic:** Agentic AI market readiness  
**Research Question:** Is agentic execution commercially premature for the target market?

**Key Finding**  
**OBSERVATION:** Agent adoption is early but no longer experimental-only. However, governance maturity lags adoption and high-stakes autonomy remains constrained.

**Evidence**  
McKinsey reports 23% of organizations scaling at least one agentic system and 39% experimenting. PwC reports 79% of surveyed companies have adopted agents and 88% plan to increase AI-related budgets due to agents, while only a minority are fundamentally redesigning workflows. Deloitte similarly finds agentic usage ahead of governance maturity.

**Implication**  
An agentic workbench is commercially relevant, but the market-ready architecture must expose control, approval and auditing as core features rather than optional enterprise extras.

**Confidence:** High for direction; Medium for target-market extrapolation.

**Open Question**  
What is the optimal default autonomy level for engineering and government users during the first production deployment?

---

# R3 — COMPETITOR RESEARCH

## R3-01 — Palantir AIP / Foundry / Apollo

**Type:** Direct/near-direct enterprise operating platform competitor.

**Deployment / Sovereignty**  
Palantir documents a unified architecture spanning AIP, Foundry and Apollo, with zero-trust security, granular human/agent access scopes, lineage/audit and deployment across sensitive environments. Palantir and NVIDIA also document sovereign, on-premise and air-gapped reference architectures.

**Core capabilities**  
Data integration, ontology/semantic layer, workflows, agents, applications, governance, evaluations, infrastructure management and mission-critical deployment.

**Strongest overlap**  
End-to-end operational AI, secure enterprise data, agentic execution, auditability, defense/industrial workloads.

**Key limitations vs project**  
The platform is much broader and operationally heavier than a single-workstation MVP. It is built as an enterprise operating environment rather than a lightweight product targeted at mid-range GPU deployments.

**Pricing / Licensing**  
Public page does not expose a simple list price for the full platform; enterprise contracting is the normal model.

**Evidence**  
Palantir architecture documentation: https://palantir.com/docs/foundry/architecture-center/platforms/  
Palantir sovereign model engine: https://www.palantir.com/sovereignaios-modelengine/  
Palantir/NVIDIA sovereign AI OS reference architecture material: https://www.businesswire.com/news/home/20260312795208/en/Palantir-and-NVIDIA-Team-to-Deliver-Sovereign-AI-Operating-System-Reference-Architecture

**Project Relevance**  
Palantir is the strongest benchmark for what “AI as an operational system” means at enterprise scale.

**Analyst Assessment:** Strong benchmark; not an architecture to replicate wholesale.

**Open Question**  
Can the workbench reproduce a small subset of Palantir-like governed execution at orders-of-magnitude lower infrastructure and integration cost?

---

## R3-02 — IBM watsonx Orchestrate + enterprise knowledge stack

**Type:** Direct/near-direct orchestration and knowledge-platform competitor.

**Deployment / Sovereignty**  
IBM documents a hybrid architecture supporting on-premises deployment, agent orchestration and governed enterprise knowledge access.

**Core capabilities**  
Agent control plane, tool/workflow orchestration, governed agent catalog, knowledge agents, citation-backed answers, enterprise integration.

**Strongest overlap**  
Agent orchestration + internal knowledge + governance.

**Key limitations vs project**  
The value proposition is distributed across a broader IBM ecosystem. It is not specifically optimized around an air-gapped single-GPU technical-workbench experience or engineering/P&ID workflows.

**Pricing / Licensing**  
No simple public list price for the target enterprise configuration; sales-led.

**Evidence**  
IBM watsonx Orchestrate: https://www.ibm.com/products/watsonx-orchestrate  
IBM/Atolio sovereign knowledge case: https://www-api.ibm.com/adobe/assets/urn:aaid:aem:28ca2ba7-bd56-4880-869b-e6e73fe901e9/original/as/Atolio%20on%20IBM%20Fusion%20for%20Sovereign%20AI.pdf

**Analyst Assessment:** Strong competitor for enterprise orchestration/governance; partial match for the product's specialized sovereign-workbench thesis.

---

## R3-03 — GitLab Duo Self-Hosted / Agent Platform

**Type:** Direct competitor for internal software/code workflows; partial competitor for general workbench execution.

**Deployment / Sovereignty**  
Fully self-hosted configurations can operate in isolated/offline networks with a self-hosted AI Gateway and local model infrastructure. GitLab provides explicit offline deployment instructions.

**Core capabilities**  
Code suggestions, code explanation, test generation, refactoring, code fixes, code review and agent platform workflows.

**Strongest overlap**  
Local models, agentic execution, logs, offline deployment, sandboxed workflow infrastructure and developer productivity.

**Key limitations vs project**  
The product is strongly centered on software development and the GitLab lifecycle. It does not establish a general-purpose confidential technical workbench spanning engineering documents, P&IDs, inspection reports, enterprise retrieval and business artifacts.

**Pricing / Licensing**  
Self-hosted capabilities require GitLab enterprise subscriptions/add-ons. Offline Agent Platform self-hosted uses an Enterprise License Agreement according to GitLab documentation; no public simple list price is exposed.

**Evidence**  
GitLab Duo Self-Hosted: https://docs.gitlab.com/18.8/administration/gitlab_duo_self_hosted/  
Offline deployment: https://docs.gitlab.com/administration/gitlab_duo_self_hosted/offline_deployment/  
Add-on/licensing: https://docs.gitlab.com/subscriptions/subscription-add-ons/

**Analyst Assessment:** Strong proof that customers will pay for local/air-gapped agentic AI; strong competitor in coding, incomplete competitor for cross-domain technical work.

**Open Question**  
How much of GitLab's execution and governance pattern can be generalized without importing its application assumptions?

---

## R3-04 — Onyx

**Type:** Direct/near-direct enterprise knowledge/search/agent competitor.

**Deployment / Sovereignty**  
Onyx documents self-hosted and air-gapped deployment patterns with local models and local retrieval.

**Core capabilities**  
Enterprise search, RAG, permission-aware retrieval, connectors, deep research, custom agents, MCP/OpenAPI actions.

**Strongest overlap**  
Internal knowledge, enterprise connectors, permission-aware retrieval, agents and self-hosting.

**Key limitations vs project**  
Its strongest product identity is enterprise knowledge/search. The public material does not establish the same depth across engineering drawing interpretation, sandboxed code verification and business-artifact generation as the proposed workbench.

**Pricing / Licensing**  
Vendor/secondary public material indicates a free self-hosted/open-source path, paid cloud and custom enterprise offerings. Treat exact current licensing boundaries as a validation item before commercial use.

**Evidence**  
Onyx self-hosted RAG overview: https://onyx.app/insights/self-hosted-rag  
Onyx sovereign AI overview: https://onyx.app/insights/sovereign-ai

**Analyst Assessment:** Strong competitor for the knowledge layer; weaker evidence for the full engineering execution layer.

**Open Question**  
Can the proposed product differentiate enough through technical-workflow depth to avoid competing directly as a generic enterprise-search platform?

---

## R3-05 — RAGFlow

**Type:** Direct competitor for document-heavy RAG and agent workflows.

**Deployment / Sovereignty**  
Self-hosted via Docker; local LLMs can be used. RAGFlow documents offline caveats because some OCR/model assets may try to download from Hugging Face unless pre-staged.

**Core capabilities**  
Deep document parsing, OCR, table/layout extraction, visual chunk review, citations, hybrid retrieval, configurable ingestion pipelines, multimodal parsing, agents, MCP and code execution sandboxing.

**Strongest overlap**  
Scanned PDFs, complex technical documents, multimodal processing, RAG, agent workflows and local deployment.

**Key limitations vs project**  
Operational complexity is non-trivial. The platform depends on several supporting services; the default offline/document-processing path needs careful asset pre-staging. Enterprise governance/security depth is less mature/documented than the largest commercial platforms.

**Pricing / Licensing**  
Open-source platform; licensing of dependencies must still be checked for the exact deployment/use case.

**Evidence**  
Official documentation: https://ragflow.io/docs/configurations  
Official quickstart: https://github.com/infiniflow/ragflow/blob/d32e05d5/docs/quickstart.mdx  
Agent ingestion pipeline: https://github.com/infiniflow/ragflow/blob/53afc323/docs/guides/agent/agent_quickstarts/ingestion_pipeline_quickstart.md  
FAQ: https://github.com/infiniflow/ragflow/blob/main/docs/faq.mdx

**Analyst Assessment:** Very strong reference for document intelligence; potentially the closest open-source technical foundation for document-heavy workflows, but not the complete product thesis.

**Open Question**  
Can RAGFlow's document stack be integrated without inheriting an unnecessarily broad platform footprint?

---

## R3-06 — Open WebUI

**Type:** Indirect/partial competitor; local AI interface and agent harness.

**Deployment / Sovereignty**  
Self-hosted and designed to run offline with local model providers.

**Core capabilities**  
Chat interface, local models, RAG, tool calling, task models, local terminal/agent harness and browser-based interaction.

**Strongest overlap**  
Modern UX on local infrastructure and model-provider flexibility.

**Key limitations vs project**  
It is fundamentally a general AI interface rather than an engineering-specific execution environment with enterprise knowledge governance, validated artifact pipelines and domain-aware workflows.

**Pricing / Licensing**  
Open-source/community deployment is available; exact commercial licensing terms should be checked for the target deployment before product packaging.

**Evidence**  
Official documentation: https://docs.openwebui.com/

**Analyst Assessment:** Important UX benchmark and possible component/inspiration; weak as a standalone answer to the full problem.

**Open Question**  
Can the project's differentiator remain visible when users already have a strong local-chat option such as Open WebUI?

---

## R3-07 — Nutanix Enterprise AI / GPT-in-a-Box

**Type:** Infrastructure/platform competitor and complement.

**Deployment / Sovereignty**  
On-premise, public cloud and dark-site/air-gapped deployments are supported.

**Core capabilities**  
Model deployment, model/API endpoints, RBAC, model testing, monitoring, GPU monitoring and event auditing.

**Strongest overlap**  
Private AI infrastructure, operational control and local model serving.

**Key limitations vs project**  
Nutanix Enterprise AI does not itself provide the full business-facing AI workbench; it is primarily a platform for deploying/operating AI models and APIs.

**Pricing / Licensing**  
Commercial enterprise licensing; public pages do not provide a simple equivalent list price for the complete private-AI deployment.

**Evidence**  
Nutanix Enterprise AI FAQ: https://www.nutanix.com/products/nutanix-enterprise-ai/faq

**Analyst Assessment:** More likely a deployment partner/complement than the product's direct application-level competitor.

---

## R3-08 — VMware Private AI Foundation with NVIDIA

**Type:** Infrastructure/platform competitor and complement.

**Deployment / Sovereignty**  
Connected and disconnected/air-gapped deployments are explicitly documented. Air-gapped deployment requires local infrastructure such as bastion/admin hosts, registries, package mirrors and local content.

**Core capabilities**  
Private AI infrastructure, model serving, Kubernetes-based deployment, agent application support, observability and lifecycle management.

**Strongest overlap**  
Air-gap deployment engineering and private agent infrastructure.

**Key limitations vs project**  
Infrastructure-heavy. It does not itself solve the user-facing confidential knowledge-work problem or the domain workflow layer.

**Evidence**  
VMware/Broadcom documentation: https://techdocs.broadcom.com/us/en/vmware-cis/private-ai/foundation-with-nvidia/9-1/deploying-private-ai-foundation-with-nvidia/setup-workflow-for-private-ai-services.html

**Analyst Assessment:** Strong infrastructure benchmark; not a direct product substitute.

---

## R3-09 — Red Hat AI

**Type:** Platform competitor/complement.

**Deployment / Sovereignty**  
Supports enterprise AI on hybrid cloud and server environments, with open-source foundations and local inference paths.

**Core capabilities**  
Model/inference infrastructure, vLLM-based serving, model/application lifecycle, agent support and enterprise governance.

**Strongest overlap**  
Enterprise local AI platform, model flexibility and governance.

**Key limitations vs project**  
It is a platform foundation rather than the final end-user workbench for engineering knowledge work.

**Evidence**  
Official product page: https://www.redhat.com/en/products/ai

**Analyst Assessment:** Strong potential infrastructure layer; not a direct substitute for the proposed application/workbench.

---

## R3-10 — NVIDIA NIM / AI Enterprise

**Type:** Model-serving/infrastructure layer, not a complete user-facing competitor.

**Deployment / Sovereignty**  
NVIDIA documents explicit two-phase air-gap deployment with pre-staged model assets, local registries and no API keys in the isolated phase.

**Core capabilities**  
Production inference serving and AI infrastructure.

**Strongest overlap**  
Air-gapped model serving and hardware-aware deployment.

**Key limitations vs project**  
Inference is only one layer. It does not solve enterprise retrieval, agent workflows, document intelligence, business artifacts, governance UX or end-to-end task execution by itself.

**Evidence**  
Official air-gap deployment documentation: https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html

**Analyst Assessment:** Foundational component/partner, not a standalone workbench substitute.

---

# R3 — INDIRECT ALTERNATIVES

## IA-01 — Manual work + fragmented internal software

**Strength:** Best sovereignty; no new AI infrastructure.  
**Weakness:** Highest labor/time burden and poor cross-document reasoning.  
**Observed pattern:** Engineering review, inspection reporting, document consolidation and internal knowledge search remain heavily dependent on human navigation and expertise.

**Project implication:** The value proposition must demonstrate time-to-result and quality improvement, not just local inference.

---

## IA-02 — Public cloud AI assistants

**Strength:** Best general-purpose model quality and familiar UX.  
**Weakness:** Fails the hard requirement when external data transfer is prohibited. Also creates governance/visibility issues when employees use personal or unmanaged accounts.

**Project implication:** The workbench competes primarily by offering a secure alternative with enough capability and UX to displace unsafe workarounds.

---

## IA-03 — Internal point solutions / custom scripts

**Strength:** Can be tailored exactly to one workflow.  
**Weakness:** Creates a collection of disconnected systems, duplicated infrastructure, inconsistent logging, and inconsistent model/tool governance.

**Project implication:** The product should sell a reusable execution substrate: one task interface, one policy model, one tool layer, one audit system and replaceable model/knowledge components.

---

## IA-04 — Local open-source stack assembled in-house

**Typical pattern:** vLLM/llama.cpp/Ollama + RAGFlow/Open WebUI/Onyx + vector/search infrastructure + custom agent code + custom document processing + custom artifact generation.

**Strength:** Maximum flexibility and potentially low software licensing cost.  
**Weakness:** Integration, maintenance, security hardening and observability become the organization's responsibility.

**Project implication:** This is the most serious “build it ourselves” alternative and therefore the benchmark for proving product value. The workbench must materially reduce integration burden and provide a better governed end-to-end workflow.

---

# CROSS-STREAM SYNTHESIS

## 1. What the research establishes

1. **The underlying problem is real.** Confidential technical and business knowledge is still processed through manual or fragmented workflows because organizations cannot always use public AI with the data they need.
2. **The most valuable workloads are not simple chat.** They involve extraction, retrieval, reasoning, validation, tool use and production of a controlled business artifact.
3. **Engineering documents are a distinct technical workload.** P&IDs, drawings, scanned reports and heterogeneous office documents cannot be reduced to plain-text RAG without losing relevant structure.
4. **Internal knowledge retrieval is a permissions and authority problem.** Correct retrieval requires user authorization, provenance, source attribution and version/authority handling.
5. **Agent autonomy is accepted asymmetrically.** Trust is higher for analysis/collaboration and lower for high-stakes actions, making approval and policy controls fundamental.
6. **Enterprise AI adoption is increasing while production scaling remains immature.** The market is moving toward agents, but integration, governance, data readiness and operational complexity remain constraints.
7. **India is creating a supportive sovereign-AI environment.** Government policy explicitly emphasizes trusted, accountable AI and domestic AI capability.
8. **Competitors already cover most individual layers.** Palantir covers governed operational AI, IBM covers orchestration, GitLab covers self-hosted coding agents, RAGFlow covers document-heavy RAG, Onyx covers knowledge search/agents, and infrastructure vendors cover private inference.
9. **The observed gap is architectural, not feature-count based.** Publicly documented competitors do not clearly demonstrate one lightweight product optimized around the full combination of air-gapped operation, multi-model local routing, engineering multimodality, governed agentic execution, sandboxed code, artifact generation and technically demonstrable zero egress on a mid-range single-server target.

The ninth statement is an **INFERENCE**, not an established market fact. It reflects the public capabilities examined in this research and must be tested against additional private/vendor evidence before being used as an absolute “no competitor exists” claim.

---

# ESTABLISHED FINDINGS

### EF-01 — Sovereignty is a product requirement, not merely an infrastructure setting
The user's target workflows require local processing of sensitive data. Public cloud capability cannot be the core dependency under the hard constraint set.

### EF-02 — End-to-end execution is more valuable than conversational response quality alone
The strongest enterprise examples combine retrieval, extraction, validation, automation and output generation.

### EF-03 — Human oversight is structurally necessary for high-stakes workflows
Current evidence does not support treating engineering, safety, legal or financially consequential outputs as autonomous by default.

### EF-04 — Document structure and provenance are first-class data
The engineering-document studies show that tags, relationships, layout and cross-document dependencies carry information that generic semantic search can miss.

### EF-05 — A sovereign AI product has to be operationally useful enough to replace risky workarounds
Security-only positioning is insufficient because users have a strong productivity incentive to use capable external tools.

---

# REJECTED / INADEQUATE APPROACHES

## RA-01 — “Just build a private chatbot”
Rejected because the validated workflows require tools, retrieval, multimodality, verification and artifact generation.

## RA-02 — “One local model for everything”
Rejected as a design hypothesis. The product requirements explicitly call for multiple models and task-based selection, and enterprise workloads differ materially in modality and reasoning requirements.

## RA-03 — “Generic vector RAG is the enterprise knowledge layer”
Rejected as insufficient. Permission enforcement, document authority, provenance and heterogeneous engineering relationships are equally important.

## RA-04 — “Block public AI and the risk disappears”
Rejected by user-behavior evidence. Demand for AI continues under restrictive policy and can move to unmanaged channels.

## RA-05 — “Agent autonomy should be maximized”
Rejected. Trust falls for higher-stakes actions, and governance maturity lags agent adoption.

## RA-06 — “A large market number proves the opportunity”
Rejected. Broad GenAI market spend cannot be substituted for a defensible sovereign-workbench TAM.

---

# FAILURE / RISK FINDINGS

## FR-01 — Document parsing failure
Scanned, multi-column, tabular and visual documents can be parsed incorrectly. This can propagate into incorrect retrieval and wrong artifacts.

## FR-02 — Retrieval failure
A semantically relevant chunk may still be unauthorized, stale or from the wrong authority level.

## FR-03 — Cross-document reasoning failure
Indirect dependencies and pure-addition cases can be missed even by specialized engineering research systems.

## FR-04 — Agent/tool failure
Agents can select the wrong tool, call tools in the wrong order, or continue after a failed intermediate step.

## FR-05 — Hallucination / unsupported synthesis
Even citation-backed systems can produce incorrect summaries if evidence selection or synthesis is wrong.

## FR-06 — Hardware contention
Local inference, OCR, embeddings, reranking and agent tasks may compete for memory and GPU resources on a single mid-range server.

## FR-07 — Air-gap operational burden
Offline environments require pre-staged model assets, container images, registries and update procedures. Air-gap is therefore an operational discipline, not simply “turn off the internet.”

## FR-08 — Governance drift
An approved AI tool can become dangerous if permissions, connectors, models or workflow definitions change without corresponding policy updates.

---

# OPEN QUESTIONS

1. What exact Indian customer segment has the strongest combination of pain, procurement authority and ability to run a single-server private AI deployment?
2. What security classification boundary will the first product actually support: internal/confidential, restricted, isolated network, or formally air-gapped/classified environments?
3. What are the minimum acceptable accuracy/recall thresholds for P&ID, inspection and engineering-document tasks?
4. Which model-routing strategies produce a reliable quality/latency trade-off under a mid-range GPU budget?
5. How should document authority and revision precedence be modeled when metadata is incomplete or inconsistent?
6. Which agent actions require mandatory approval, dual approval or are forbidden?
7. What is the lowest operational footprint that still supports reliable multi-user deployment?
8. Which artifacts require deterministic code/template generation versus direct model generation?
9. What exact open-source licensing combinations remain commercially safe for a packaged enterprise product?
10. How much implementation and support effort will customers tolerate compared with building a bespoke internal system?

---

# ARCHITECTURE / ENGINEERING QUESTIONS PASSED TO R4

1. What system architecture can combine model routing, agent execution, RAG, multimodal document intelligence and artifact generation without turning the MVP into an unmaintainable distributed system?
2. What local inference architecture gives acceptable latency and concurrency on the target mid-range GPU class?
3. How should the permission-aware knowledge layer represent source ACLs, document authority, versioning and provenance?
4. What document pipeline is required to preserve text, table, image, drawing and layout semantics?
5. Which agent runtime primitives are mandatory: state machine/graph execution, retries, checkpoints, approval gates, compensation/rollback and trace logging?
6. What sandbox boundary is sufficient for AI-generated code and spreadsheet/programmatic transformations?
7. How should model selection be evaluated experimentally rather than assumed from benchmark popularity?
8. What observability schema is required to prove what model, tool, document and network path were used for each task?
9. How can zero-egress operation be verified technically at runtime rather than inferred from configuration?
10. Which open-source components can be replaced independently without changing the application-level contracts?

---

# COMPETITIVE POSITIONING INFERENCE

The evidence suggests the product should **not** position itself as another generic local-chat product.

The more defensible wedge is:

> **A sovereign AI execution workbench for confidential technical knowledge work — combining local multi-model reasoning, governed enterprise retrieval, multimodal document understanding, controlled tools, verification and auditable artifact generation in one air-gapped environment.**

This positioning is an **INFERENCE** derived from the user research, market evidence and competitor comparison. It is not a claim that the market has already validated willingness to pay for exactly this bundle.

The differentiator should therefore be the **execution loop**:

**Task understanding → capability/model routing → multimodal/document processing → governed knowledge retrieval → agent planning → controlled tool execution → verification → artifact generation → audit / sovereignty proof**

rather than model novelty alone.

---

# SOURCE REGISTER

### Primary / high-authority sources used

1. McKinsey — The state of AI in 2025: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
2. Federal Reserve — Monitoring AI Adoption in the U.S. Economy, 2026: https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
3. Deloitte — State of AI in the Enterprise 2026: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html
4. PwC — AI Agent Survey: https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html
5. IDC — FutureScape Worldwide Generative AI 2025 Predictions: https://info.idc.com/rs/081-ATC-910/images/US-IDC-FutureScape-2025-GenAI_ebook.pdf
6. Gartner — 2025 GenAI spending forecast: https://www.gartner.com/en/newsroom/press-releases/2025-03-31-gartner-forecasts-worldwide-genai-spending-to-reach-644-billion-in-2025
7. India MeitY / PIB — AI Governance Philosophy, Feb 2026: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026215790801.pdf
8. India PIB — Indigenous Foundation Models, AI Compute and Semicon 2.0, Aug 2026: https://www.pib.gov.in/PressReleasePage.aspx?lang=1&PRID=2295477&reg=48
9. Dzhusupova et al., Wiley, 2023 — P&ID design-error AI: https://doi.org/10.1002/smr.2543
10. TU Delft / Bas Filius thesis, 2026 — Engineering document dependencies: https://repository.tudelft.nl/file/File_fdfb2aa1-0f2e-474e-93a4-215095f7a905
11. Microsoft Learn — SLB productivity and document processing: https://learn.microsoft.com/en-us/power-platform/guidance/case-studies/slb-enhances-productivity
12. IBM — Permission-aware knowledge assistant case, 2026: https://www.ibm.com/new/product-blog/building-a-permission-aware-knowledge-assistant-with-ibm-watsonx-orchestrate
13. NIST AI RMF GenAI Profile: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf
14. GitLab Duo Self-Hosted: https://docs.gitlab.com/18.8/administration/gitlab_duo_self_hosted/
15. GitLab offline deployment: https://docs.gitlab.com/administration/gitlab_duo_self_hosted/offline_deployment/
16. RAGFlow documentation: https://ragflow.io/docs/configurations
17. RAGFlow quickstart: https://github.com/infiniflow/ragflow/blob/d32e05d5/docs/quickstart.mdx
18. Open WebUI documentation: https://docs.openwebui.com/
19. Palantir architecture: https://palantir.com/docs/foundry/architecture-center/platforms/
20. NVIDIA NIM air-gap deployment: https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html
21. Nutanix Enterprise AI FAQ: https://www.nutanix.com/products/nutanix-enterprise-ai/faq
22. VMware Private AI Foundation: https://techdocs.broadcom.com/us/en/vmware-cis/private-ai/foundation-with-nvidia/9-1/deploying-private-ai-foundation-with-nvidia/setup-workflow-for-private-ai-services.html
23. Red Hat AI: https://www.redhat.com/en/products/ai
24. Palantir sovereign AI model engine: https://www.palantir.com/sovereignaios-modelengine/
25. Dell + Palantir on-prem AI OS: https://www.dell.com/en-us/blog/dell-and-palantir-introduce-an-on-premises-ai-operating-system/
26. PagerDuty Shadow AI Survey: https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/
27. LayerX Enterprise AI/SaaS Security Report: https://go.layerxsecurity.com/hubfs/LayerX%5FEnterprise%5FAI%5Fand%5FSaaS%5FData%5FSecurity%5FReport.pdf
28. Cyberhaven AI Adoption & Risk Report 2026: https://info.cyberhaven.com/hubfs/Webflow_Resources/Cyberhaven-AI-Risk-Report-2026.pdf

---

# SOURCE-TRACEABILITY NOTE

This report follows the supplied research rules: research questions are explicit; source material is inspected rather than inferred from snippets; vendor claims are distinguished from independent evidence; limitations and unresolved questions are recorded; and conclusions are tied back to the Sovereign Agentic AI Workbench.

The supplied project context establishes the product definition, target workflows and hard constraints. The supplied research workflow establishes the sequential R1 → R2 → R3 order. The supplied output schema requires each significant finding to state the stream, topic, research question, source, finding, evidence, project relevance, implication, limitations/failure, confidence, open question and researcher notes.
