# CHAPTER 1. EXECUTIVE SUMMARY

VNUK Institute for Research and Executive Education is a member of the University of Danang whose mission includes delivering modern, world-class educational programmes, equipping learners with the skills to take charge of their future, and providing faculty and learners with a friendly and inspiring environment for study and work (VNUK, n.d.-a). This project therefore treats student support as part of VNUK’s educational operating environment rather than as a peripheral administrative function. The selected transformation domain is Student Support and Academic Navigation, with a deliberately narrow initial product area: academic enquiry guidance and routing. The design now treats both students and staff as primary users. Students need a clear next step, accurate guidance and transparent handoff; staff need complete, correctly routed requests, maintainable content and lower avoidable clarification effort.

The evidence base comes from Customer Experience module research conducted mainly in December 2025–January 2026, later qualitatively revalidated by Group 1 in October 2026. The reported CSE study covered 15 students and five faculty members, while the material available for detailed review covers ten students or alumni and one faculty member. The BMS survey contains eight respondents. Individual CSE accounts include a four-to-five-day advising email response and a missed graduation notice that was subsequently resolved with faculty help. In BMS, seven of eight respondents reported heat-related fatigue or productivity effects and four of eight reported insufficient practical time. These results identify service and operational frictions but do not constitute representative institution-wide baselines (Customer Experience project teams, 2026a, 2026b; Group 1, 2026).

Three broader candidate domains were compared using the Week 3 value–feasibility criteria: Student Support and Academic Navigation, Practical Learning and Resource Operations, and Academic Progression and Milestone Management. Student Support ranked highest in the team’s conditional assessment because a bounded guidance-and-routing pilot can begin without direct access to grades, official registration records or major physical investment. This conclusion remains conditional on staff capacity, content ownership and demand validation. The strongest correction arising from lecturer feedback is therefore not to broaden the solution, but to tighten it: one product area, one measurable service journey, and two user groups.

The recommendation is to run an evidence-led, dual-user pilot. The long-term product area is a VNUK Student Support and Academic Navigation service, but the initial MVP should test a bounded academic enquiry journey using approved guidance, request preparation, accountable handoff and basic case status. CSE provides the strongest documented starting evidence; IBM and BMS should enter the same product experiment only after comparable student and staff baselines are collected. AI remains an optional layer rather than the product itself. This sequencing is consistent with higher-education digital-transformation research, which shows that meaningful transformation depends on organizational processes, people, data and governance as well as technology (Fernández et al., 2023), and with UNESCO’s human-centred approach to generative AI in education (UNESCO, 2023).

The initial decision request is approval to validate and pilot the service rather than approval for university-wide AI deployment. Wave 1 should establish the student and staff baseline, nominate a service owner, validate staff-maintained content, test the staff workflow and confirm privacy controls under Vietnam’s current Personal Data Protection Law No. 91/2025/QH15 and Decree No. 356/2025/ND-CP. The business case is intentionally balanced: student effort, staff capacity, service quality and organizational learning are considered alongside content-maintenance cost, technology cost, adoption effort and digital-trust risk. Scale should occur only if the service produces measurable value for both students and staff and the AI layer demonstrably outperforms a simpler searchable guidance service.

# CHAPTER 2. ORGANIZATION, INDUSTRY, AND TECHNOLOGY CONTEXT

## 2.1 Organization, Mission, and Strategic Alignment

VNUK is the VN-UK Institute for Research and Executive Education within the University of Danang. Its institutional vision is to become an international-standard university that conducts breakthrough research and develops well-rounded human resources in a creative and humanistic environment. Its stated mission includes delivering modern, world-class educational programmes, equipping learners with essential skills for their future, and creating a friendly and inspiring environment for both faculty and learners (VNUK, n.d.-a; VNUK, n.d.-b). VNUK also emphasizes innovation, empathy and perseverance as core values.

The selected domain has a direct but bounded relationship to that mission. Student Support and Academic Navigation does not itself create academic learning outcomes; rather, it removes avoidable service friction that can prevent students from navigating programmes, understanding procedures and reaching authorised academic support. For staff, a clearer service model can reduce low-value clarification and redirection, allowing more time for complex academic or pastoral work. This link is strategically relevant because an inspiring learning-and-working environment depends not only on curriculum quality but also on the reliability of the journeys surrounding that curriculum. The University of Danang likewise emphasizes a learner-centred approach, innovation and digital transformation in its institutional development (University of Danang, 2025).

## 2.2 Dual Users and Value Proposition

The product is now defined around two primary user groups. The first is students, who need to identify the correct procedure, prepare a complete request, reach the responsible unit and know what happens next. The second is staff, including academic advisers, programme representatives and administrative staff, who need requests to arrive with sufficient context, to be routed to the correct owner and to be supported by current, approved guidance. IT, management, data/privacy roles and programme leaders remain important stakeholders, but they are not the only users of the product.

This dual-user framing corrects a weakness in the Week 5 presentation, which described staff mainly as content owners or reviewers. It also changes the baseline and the business case. A service is not successful if students experience less effort but staff inherit more checking, escalation or maintenance work. Accordingly, the value proposition is: enable students to complete the correct next step with less uncertainty, while enabling staff to resolve better-formed and better-routed enquiries with sustainable total effort. This is consistent with human-centred technology implementation research in higher education, which stresses stakeholder perceptions, implementation context and measurable use rather than technology availability alone (Chugh et al., 2023).

## 2.3 Higher-Education and Technology Pressures

Higher-education institutions face pressure to digitize services without fragmenting them into isolated tools. A multivocal review of digital transformation in higher education found that transformation is organizational and strategic, involving processes, human factors and information as well as technology (Fernández et al., 2023). This matters for VNUK because the diagnosed problem is not the absence of communication channels; it is the inconsistent connection between guidance, routing, ownership and measurement.

Student expectations also increasingly include self-service access to institutional resources, referral systems, registration tools, digital nudges and virtual support. The 2024 EDUCAUSE student technology survey explicitly examines student attitudes toward these categories, including AI-enabled support and all-in-one institutional service access (EDUCAUSE, 2024). The survey should not be interpreted as evidence that VNUK students demand a chatbot, but it demonstrates that self-service and digitally mediated support are legitimate design options in contemporary higher education.

Data is another pressure and opportunity. Jisc argues that student services can become more responsive and scalable when institutions use existing data with robust governance and architecture, while keeping the human experience central (Peck, 2023). Research on analytics in higher education similarly emphasizes data-driven decision-making but also identifies governance and capability requirements (Stojanov & Daniel, 2024). For VNUK, the immediate implication is modest: the project should first capture service events consistently—category, owner, response, resolution and repeat contact—before attempting advanced analytics.

Generative AI adds both potential and risk. UNESCO recommends a human-centred approach that protects privacy, preserves human agency and requires institutional validation of GenAI use in education (UNESCO, 2023). NIST’s AI Risk Management Framework and Generative AI Profile similarly emphasize lifecycle risk management, testing, evaluation, transparency and controls rather than treating AI deployment as a one-time technical decision (NIST, 2023, 2024). These principles support the project’s decision to keep authorised staff responsible for academic decisions and to retain a non-AI fallback.

## 2.4 Relevant Technologies, Feasibility, and Regulation

The minimum technology set is intentionally simple: a controlled knowledge repository, structured request form, routing logic, case tracking, basic analytics and a user interface. A retrieval-based AI layer may later support classification, summarization or question answering from approved material, but the service should remain useful without it. This creates a valid comparison condition: if ordinary search and structured routing produce equivalent outcomes with lower cost and risk, the AI layer should not be scaled.

Current organizational readiness is partial. Existing communication channels and academic expertise provide a starting point, but the project has not established integration readiness, a dedicated development budget, reliable enquiry volume, or staff time available for content governance. Feasibility therefore depends more on service ownership and maintainable knowledge than on technical novelty.

Personal-data handling must be designed against the current Vietnamese legal environment. Law No. 91/2025/QH15 on Personal Data Protection took effect on 1 January 2026 and establishes rights, obligations and responsibilities for personal-data processing, while Decree No. 356/2025/ND-CP provides implementation measures (National Assembly of Vietnam, 2025; Government of Vietnam, 2025). For this project, practical controls include data minimization, transparent purpose, role-based access, separate treatment of public guidance and identifiable cases, retention rules, logging and assessment before any cross-border vendor processing. The report does not claim legal clearance; authorised VNUK reviewers must determine the final compliance approach.

## 2.5 Stakeholder Map

| **Stakeholder / user** | **Primary need** | **Role in the transformation** |
|----|----|----|
| Students | Correct next step, low effort, transparent routing and status | Primary product user; discovery, pilot and usability evidence |
| Academic / administrative staff | Complete requests, clear ownership, reusable approved guidance, sustainable workload | Primary product user; resolver, content owner and workflow co-designer |
| Programme representatives | Programme-specific accuracy and policy authority | Approve guidance, exceptions and review cycle |
| Student/academic services owner | Service standards, workload visibility and accountability | Proposed domain/product owner |
| IT / digital team | Maintainable, secure and supportable solution | Platform, integration and technical enablement |
| Management | Strategic fit, measurable benefits, risk control | Sponsor, funding and stage-gate decisions |
| Data/privacy/security roles | Lawful and secure processing | Guardrails, review and assurance |

# CHAPTER 3. CURRENT-STATE DIAGNOSIS AND PRIORITY-DOMAIN SELECTION

## 3.1 Evidence Base and Limitations

The diagnosis combines student interviews, faculty material, survey charts and reconstructed journeys from earlier Customer Experience work. Research was conducted mainly during December 2025–January 2026. Group 1 later contacted departmental stakeholders in October 2026 and qualitatively revalidated that the issues remained relevant, but no repeat survey was administered. The reported CSE study covered 15 students and five faculty members; the material reviewed in depth for this project covers ten students or alumni and one faculty member. The BMS survey contains eight respondents, and a completed BMS faculty transcript was not available for this assessment (Customer Experience project teams, 2026a, 2026b; Group 1, 2026).

These limitations are consequential. Historical counts are not current prevalence estimates. One student’s four-to-five-day advising response is evidence that a failure occurred, not evidence that VNUK’s average response time is four to five days. Likewise, the BMS n=8 survey can identify issues for investigation but cannot support population-level claims. The analysis therefore separates observed evidence, team interpretation and unverified assumptions.

## 3.2 Recorded Student and Staff-Side Evidence

CSE material shows variability rather than uniform service failure. One student recalled four to five LMS login attempts and a four-to-five-day advising email response. One alumnus reported missing a graduation notice and later receiving faculty help, while also describing regular thesis supervision. These accounts identify both failure points and effective staff intervention (Customer Experience project teams, 2026a).

BMS respondents reported operational barriers that are distinct from enquiry navigation. Seven of eight reported heat-related fatigue or productivity effects, six of eight reported heavy workload, five of eight reported rushing to leave a hot lab, and four of eight reported insufficient practical time. Laboratory satisfaction was more mixed than the narrative alone suggested, with a weighted mean of 3.63/5 and four of eight respondents rating the lab four or five (Customer Experience project teams, 2026b). These findings support keeping practical-resource issues as a separate domain rather than treating the Student Support Hub as a universal solution.

Staff-side evidence is currently weaker than student-side evidence. The CSE research included faculty participants, and individual cases show staff resolving problems, but the available material does not provide a systematic staff workload baseline. This gap is now explicit rather than hidden. Before pilot launch, VNUK should collect a comparable staff baseline covering handling time, repeated questions, misrouting, clarification, information search, escalation and content-maintenance effort. Lecturer feedback that 'staff are also users' therefore changes the measurement design rather than merely adding another stakeholder label.

## 3.3 Dual-User Baseline Framework

| **Dimension** | **Student baseline** | **Staff baseline** | **Why it matters** |
|----|----|----|----|
| Demand | Number of enquiries by category and programme | Cases received by category / owner | Defines eligible volume and workload |
| Speed | First-response and resolution time | Handling time and queue / wait time | Separates user waiting from staff effort |
| Effort | Repeat contacts, handoffs, information re-entry | Clarification, redirection and information-search time | Tests whether effort is reduced on both sides |
| Quality | Correct next step / resolution | Misrouted, incomplete or reopened cases | Prevents speed from masking errors |
| Adoption | Use of standard route vs. informal channels | Workflow compliance and content use | Tests real operating-model change |
| Sustainability | Satisfaction / confidence | Perceived workload plus maintenance minutes | Avoids shifting hidden work to staff |

Baseline collection should use the same case definitions before and during the pilot. Automated acknowledgements must be separated from substantive responses, and 'resolution' should mean a confirmed answer or completed referral rather than message receipt. Case counts should be reported alongside percentages to avoid misleading rates in small samples.

Until VNUK provides case data, the team uses the following working baseline for the final-year graduation journey (method in Appendix C): about 120 eligible academic enquiries per month from final-year CSE students, rising to about 60 per week during registration and graduation-application windows; a median first substantive reply of one working day, with about 20% taking more than three working days; about 30% of students contacting more than one channel or office for the same issue; about 15% of requests first sent to the wrong office; and about 8 minutes of staff handling time per routed email. In the 23 requests reviewed from one student mailbox, 8 (35%) were sent by reply-all to a whole cohort mailing list and 2 were refused because of a rule the student learned only by asking.

## 3.4 Current Journeys and Causal Hypotheses

For Student Support and Academic Navigation, the reconstructed journey is: question raised → find approved guidance → clarify the need → resolve or route → answer/referral confirmed. Possible causes of repeated contact include dispersed guidance, unclear ownership, incomplete requests and case complexity. Staff workload may also influence delays. The existing evidence does not isolate causal contribution, so each cause remains a testable hypothesis rather than a conclusion.

Practical learning follows a different journey: learning need → resource allocation → access/supervision check → session completion → return/maintenance. Reported insufficient practical time may arise from scheduling, capacity, supervision or facilities; a support hub cannot resolve physical scarcity or heat. Academic progression also differs because it requires authoritative verification of rules and student status. Maintaining these boundaries reduces solution overreach and avoids double-counting benefits.

## 3.5 Candidate Domains and Capability Assessment

| **Candidate** | **Value signal** | **Key capability position** | **Main constraint** |
|----|----|----|----|
| A. Student Support & Academic Navigation | Guidance, enquiry resolution and repeat-contact reduction | Channels/expertise partial; guidance/routing/data gaps | Owner, staff capacity and maintainable content |
| B. Practical Learning & Resource Operations | Practical-time and physical-resource pain points | Many usage/capacity/tool unknowns | Physical constraints and weak baseline |
| C. Academic Progression & Milestones | High consequence of status/notice errors | Portal/records partial | Authoritative data and approval dependencies |

The Week 3 capability assessment used six dimensions: roadmap, talent, operating model, technology, data and adoption. For Student Support, the immediate gaps were accountable ownership, organized guidance, routing and case tracking; technology and talent were assessed as partial rather than absent. This pattern reinforces the decision to treat the transformation as service redesign supported by digital capability.

## 3.6 Consistent Prioritization and Decision

The prioritization framework weights Value Potential at 30%, Feasibility at 25%, Strategic Relevance at 20%, Urgency at 15% and Learning Value at 10%. Group 1’s proposed scores produced 4.10/5 for Student Support, 3.80 for Academic Progression and 3.50 for Practical Learning. These are structured team judgments, not measured financial returns. A sensitivity test showed that if Student Support feasibility falls from four to two, its score falls to 3.60 and Academic Progression leads. The selection is therefore conditional on staff capacity, approved content and ownership.

The priority decision is Student Support and Academic Navigation. To respond to lecturer feedback that the MVP must be journey-led, the first release follows one end-to-end journey: a final-year student’s path to graduation. This journey is long enough to touch several offices—registration of remaining and required modules, academic advising, VSTEP, physical and defence education, project topic registration, and graduation applications and transcripts—yet bounded to one cohort and one clear outcome. Course registration on its own was rejected as the MVP journey because it is short and would push the product towards automated registration, which is out of scope. CSE final-year students provide the first context; IBM and BMS follow only after the same dual-user baseline is collected.

# CHAPTER 4. TRANSFORMATION VISION, VALUE LOGIC, AND SOLUTION PORTFOLIO

## 4.1 Vision and Future State

> *Within 12 months, VNUK will transform academic enquiry navigation from fragmented and reactive support into a coordinated, trackable and measurable dual-user service that helps students reach the correct next step while enabling staff to receive clearer, better-routed enquiries and reduce avoidable repetitive work.*

The vision remains technology-neutral. Higher-education transformation research warns against equating transformation with tool adoption; organizational processes, information, people and governance must change together (Fernández et al., 2023). AI may support the future state, but a reliable non-AI path remains part of the design.

## 4.2 User and Business Needs

| **User / need** | **Current friction** | **Desired outcome** |
|----|----|----|
| Student: understand next step | Scattered guidance and uncertainty | Verified procedure and responsible contact |
| Student: complete request | Missing documents/context can trigger follow-up | Checklist and structured request |
| Staff: receive actionable case | Clarification and redirection | Correct category, context and ownership |
| Staff: maintain guidance | Information can be dispersed or outdated | Named source, owner and review date |
| Management: improve service | Limited case-level evidence | Comparable KPI and benefit evidence |

## 4.3 Objectives and Measurement

| Objective | Metric | Baseline position | Pilot decision rule |
|----|----|----|----|
| Accurate, useful guidance | Staff-reviewed correctness and student usefulness rating | Test set and user ratings to be established | At least 80% of assessed answers receive 4 or 5 out of 5; zero critical wrong guidance |
| Correct first routing | Correct owner on first assignment | Routing baseline to be established | At least 80% of assessed handoffs reach the correct owner first time |
| Lower student effort | Repeat contact for same issue within 7 days | To be measured | Compare with baseline; no increase and aim for a relative reduction |
| Faster confirmed resolution | Median request-to-resolution time | To be measured | Compare with baseline without increasing unresolved cases |
| Lower avoidable staff effort | Clarification and redirection minutes per resolved case | To be measured | Reduction after including maintenance and escalation |
| Sustainable total workload | Handling plus content review and maintenance minutes | To be measured | No material increase in total effort per resolved case |
| Accountable content | % published items with source, owner and review date | Fragmented | 100% before student access |
| Adoption and closure | Eligible requests using standard route; status or closure recorded | To be measured | Threshold set after the pilot baseline; no unresolved duplicate routing |

All targets are proposed pilot thresholds and require institutional agreement. The design intentionally includes both benefit and burden metrics. A reduction in student follow-up is not counted as success if it is achieved by transferring hidden verification work to staff.

## 4.4 Value Logic

The value chain is: approved and maintained guidance improves answer consistency; structured request preparation reduces missing information; routing and visible ownership reduce handoffs; case data reveals recurring defects; and feedback supports continuous improvement. Student value is lower uncertainty and effort. Staff value is better-formed work and more capacity for complex cases. Organizational value is a reusable service model, measurable performance and stronger knowledge ownership. Jisc’s work on student analytics similarly argues that data-supported services can improve responsiveness and resource targeting when governance and human experience remain central (Peck, 2023).

## 4.5 Coherent Solution Portfolio

| **Initiative** | **Role** | **Primary user value** | **Dependency** |
|----|----|----|----|
| Approved knowledge base + content governance | Foundation | Consistent guidance for students and staff | Named content owners and sources |
| Structured request + checklist | Lighthouse | Fewer incomplete requests | Defined request taxonomy |
| Routing, handoff and case status | Lighthouse | Correct owner and visible progression | Service owner and workflow |
| Service analytics | Foundation / learning | Evidence on volume, resolution and workload | Consistent event capture |
| AI classification / retrieval support | Scale option | Faster discovery/triage | Trusted knowledge, test set and risk controls |
| AI-assisted staff response drafting | Later scale | Potential staff productivity | Human review and quality evidence |
| Opt-in reminders / proactive support | Later option | Reduced missed actions | Verified deadlines and consent basis |

The principal alternative is a searchable guidance hub with the same structured request and staff handoff but no conversational AI. This alternative is important because it allows incremental value from AI to be measured. If the AI layer does not improve task completion, routing, effort or user experience enough to justify added cost and risk, the simpler service should be retained.

## 4.6 Assumptions, Dependencies, and Risk Gates

The proposal assumes that programme representatives can approve guidance, staff can allocate time to resolve escalations, a bounded set of common enquiries exists, and students will use a standard entry route. It also assumes that the same product area can transfer across CSE, IBM and BMS after local content and workflow validation. None of these assumptions should be treated as established fact.

The dependency sequence is: confirm domain/product owner → collect dual-user baseline → define enquiry taxonomy and closure rules → approve knowledge → test staff workflow → pilot student guidance/routing → introduce AI retrieval/classification → compare AI with non-AI alternative → scale. Critical wrong guidance, inability to maintain content, unacceptable privacy risk, unmanageable escalation load or no incremental AI value are stop/pivot triggers.

## 4.7 Balanced Initial Business Case

### 4.7.1 User Value Case

Student benefits are time and effort rather than assumed revenue: fewer repeated contacts, clearer next steps, faster confirmed resolution and more consistent access to information. These outcomes should remain non-monetized until reliable time-saved evidence and an agreed valuation method exist.

### 4.7.2 Staff and Operational Value Case

Staff value is released capacity, not automatic cash saving. Potential benefits include less clarification, less redirection, lower duplication and improved visibility of case ownership. To avoid benefit inflation, any time saved must be net of content maintenance, quality review, escalation and exception handling.

### 4.7.3 Capability and Investment Case

Required investment includes content preparation, process mapping, workflow configuration, user research, training, analytics, privacy/security review, hosting or model usage, support and evaluation. Existing staff expertise and communication channels reduce some setup effort, but dedicated product ownership, data discipline and change capacity are still required.

### 4.7.4 Illustrative Sensitivity and Break-Even Logic

For sensitivity analysis only, let N be eligible enquiries per month, p the proportion resolved without substantive staff handling, t the avoided handling minutes, and w the loaded staff cost per hour. Let M be monthly content/quality cost and R monthly technology/operating cost. Gross capacity value = N × p × t × w / 60; net value = gross capacity value − M − R. These variables must be populated with measured VNUK data before an investment decision.

Using the earlier illustrative scenario—not a VNUK forecast—N=500, p=.40, t=8 minutes, w=VND100,000/hour, M=VND1,000,000 and R=VND1,000,000 produces about VND2.67 million gross monthly capacity value and VND0.67 million net. At N=200, the same assumptions yield a monthly loss of roughly VND0.93 million; operating break-even is about 375 eligible enquiries. The result demonstrates why demand validation and staff baseline measurement are decision-critical.

### 4.7.5 Risk Case

| **Risk** | **Potential effect** | **Control / decision response** |
|----|----|----|
| Incorrect or outdated guidance | Student action error; rework; loss of trust | Approved sources, content owner, review date, refusal/escalation |
| AI hallucination / misclassification | Wrong routing or misleading advice | Restricted knowledge, test set, human review, confidence threshold |
| Privacy / data misuse | Legal and trust impact | Data minimization, access control, retention, privacy assessment |
| Low student adoption | No service value | Co-design, simple route, compare with current channels |
| Staff workload transfer | Hidden cost and resistance | Measure maintenance, escalation and handling effort |
| No incremental AI value | Extra cost and risk | Stop AI layer; retain simpler service |

# CHAPTER 5. AGILE DIGITAL PRODUCT AND DELIVERY MODEL

## 5.1 Digital Product Definition

The product is a continuing VNUK Student Support and Academic Navigation service. Its long-term product boundary is the end-to-end academic enquiry journey: a student identifies the correct procedure, receives approved next-step guidance, prepares a complete request and reaches the responsible unit; staff receive and resolve that request with sustainable effort. The initial MVP is journey-led rather than a collection of unrelated features. It tests one service journey through a small number of representative request scenarios.

The long-term product may serve multiple programme contexts and journeys, but the first experiment is bounded to one journey: a final-year student’s path to graduation. Course-registration, academic-advising and general administrative questions (such as transcripts, student confirmation letters and the graduation application form BM.ĐT.09) are handled as touchpoints along that journey rather than as separate scopes. The product does not register courses, approve graduation, change official records or make academic eligibility decisions. CSE remains the first evidence-rich context; IBM and BMS are later transfer contexts, not separate products.

## 5.2 Product Goal and MVP

> *Product Goal: Improve students’ ability to identify the correct procedure and complete the next action, while enabling staff to receive better-formed, correctly routed enquiries and reducing avoidable repetitive work.*

The MVP is a human-supported HTML guidance-and-routing prototype with authenticated access, approved content, request categories, procedure checklists, a student intake flow, a request ID, staff email handoff, status and closure links, feedback and basic analytics. Read-only identity verification is in scope so only approved student or staff accounts can access the portal. Direct access to grades, enrolment records, tuition, official academic records or live EMS/LMS transactions remains out of scope.

The pilot will run for three weeks with five final-year CSE students and the staff who handle their requests in Academic Affairs and the related offices. The team will use short Agile cycles: students use the service, feedback is collected, findings become backlog items, the team fixes or refines them, and the change is retested. IBM and BMS should enter the same product experiment only after comparable baselines and content owners are confirmed.

## 5.3 User Stories and Acceptance Criteria

| **User story** | **Acceptance focus** |
|----|----|
| As a student, I want to select my type of academic request and see the verified procedure and responsible contact, so that I can complete the correct next step without repeatedly contacting different staff. | Applicable guidance shown; required steps/documents visible; correct responsible unit displayed. |
| As a staff member, I want student enquiries to arrive with the correct category and required information, so that I can resolve cases faster and spend less time clarifying or redirecting requests. | Request includes agreed mandatory fields; correct queue/owner; incomplete requests flagged before submission. |
| As a programme/content owner, I want to review and update approved guidance in one place, so that students and staff use current information. | Every item has source, owner, programme/cohort applicability and review date. |
| As a service owner, I want case and workload measures to be captured consistently, so that I can decide whether to continue, adapt or scale the product. | Category, timestamps, owner, resolution, repeat-contact and effort data available without unnecessary personal data. |

A shared safety rule applies across stories: when approved guidance is missing, conflicting or insufficient, the product must stop and route the case to an authorised staff member rather than infer an academic or financial decision.

## 5.4 Ordered Product Backlog

| **Rank** | **Backlog item** | **Type** | **Why now** |
|----|----|----|----|
| 1 | Approved content model | Control | Foundation for search and AI |
| 2 | Programme/request context | User | Relevance and correct guidance |
| 3 | Procedure / next-step checklist | User | Core student value |
| 4 | Correct department / owner | User | Routing |
| 5 | Safe escalation and closure rule | Control | Risk and accountability |
| 6 | Structured request template | User/staff | Reduce clarification |
| 7 | Content expiry and review workflow | Control | Currency |
| 8 | Dual-user test set and baseline | Discovery | Evidence |
| 9 | Request and workload analytics | Technical | Measurement |
| 10 | Case status visibility | User | Reduce follow-up |
| 11 | Privacy and retention controls | Control | Digital trust |
| 12 | Conversational AI layer | Technical | Later option after foundations |

## 5.5 Initial Sprint Plan

Sprint 1 is a two-week learning Sprint, not a production deployment. The Sprint Goal is: a student selects a request scenario, sees a verified procedure and reaches the responsible unit when staff help is required; the receiving staff member gets the agreed minimum context. Days 1-2 audit enquiries and confirm taxonomy and baseline definitions; Days 3-4 structure guidance, staff workflow and ownership; Days 5-7 build the HTML flow; Days 8-9 run student and staff usability and QA tests; Day 10 reviews evidence and updates the backlog. The following three-week pilot tests the refined flow with five students. Live academic-record integration remains outside the MVP.

## 5.6 Agile Pod Archetype and User Representation

The recommended archetype is a journey-led product pod because the product owns an end-to-end user journey and a persistent digital service. The long-term product is Student Support and Academic Navigation; the MVP is the bounded academic-enquiry journey within that product. The pod should keep users, content owners and platform specialists in the same feedback loop while preserving clear interfaces with shared VNUK services.

For a small MVP the team needs three capabilities: business analysis, software engineering, and UX/UI with quality assurance. Maddie is the Business Analyst: she turns customer-facing feedback and the product’s own performance data into requirements and an ordered backlog for the developers. Tamas and Zsombi are the Software Engineers who build and run the service. Yuhan leads UX/UI and acts as tester and customer-facing contact, collecting student and staff feedback and checking that fixes work. Research is shared between the BA and UX/UI roles, so no separate researcher, project manager or data scientist is needed. Three roles sit with VNUK rather than the team: Academic Affairs approves the guidance and updates it when policy changes; a VNUK IT or privacy adviser reviews identity, data and AI controls; and a VNUK service owner decides whether to continue, pause or stop.

| Pod role | Primary accountability | Capacity approach |
|----|----|----|
| Maddie - Business Analyst | Turns customer feedback and product performance data into requirements, acceptance criteria and an ordered backlog; owns stakeholder alignment | Protected capacity across discovery, pilot and review |
| Tamas - Software Engineer | Chat portal, server, AI/API integration, and the institutional email and status-link service | Protected engineering capacity during build and pilot |
| Zsombi - Software Engineer | Student and staff account allowlist, knowledge database and retrieval, event logging and monitoring | Protected engineering capacity during build and pilot |
| Yuhan - UX/UI, QA and Customer-Facing Lead | Student journey and interface, testing, collecting student and staff feedback, and verifying improvements | Embedded throughout discovery, testing and pilot |
| Academic Affairs content owner | Approve authoritative guidance and update it when policies change | Institutional role; named owner required before pilot |
| VNUK IT / privacy adviser | Review identity, security, retention, hosting and AI-risk controls | Part-time shared specialist |
| Student pilot panel | Complete representative tasks and report usefulness, effort and unmet needs | Five students across the three-week pilot |

## 5.7 Roles, Capacity, and Decision Rights

The four-student project team has protected capacity for the three-week pilot, while institutional roles remain subject to VNUK confirmation. The working loop is: Yuhan gathers feedback from students and staff and runs tests; Maddie combines that feedback with the product’s performance data and writes requirements; Tamas and Zsombi build and release the changes; Yuhan retests. Academic Affairs approves and updates authoritative guidance. VNUK IT or the privacy adviser reviews access and trust controls, and the VNUK service owner holds the continue, pause or stop decision.

| Task | Responsible | Accountable | Consulted | Informed |
|----|----|----|----|----|
| Define requirements, journey scope and ordered backlog | Maddie | Maddie | Yuhan; Academic Affairs | Tamas; Zsombi |
| Map and test the student enquiry journey | Yuhan | Maddie | Five pilot students; Academic Affairs | Tamas; Zsombi |
| Approve academic guidance and review policy changes | Academic Affairs | Academic Affairs content owner | Maddie; Yuhan | Tamas; Zsombi |
| Build portal, routing, AI and email workflow | Tamas; Zsombi | Tamas | Maddie; Yuhan; VNUK IT | Academic Affairs |
| Implement identity, logging, retention and monitoring controls | Zsombi | VNUK IT / privacy adviser | Tamas; Maddie | Yuhan; Academic Affairs |
| Run usability, QA and pilot feedback cycles | Yuhan | Yuhan | Maddie; five pilot students; Academic Affairs | Tamas; Zsombi |
| Decide continue, pivot, pause or stop | Maddie | VNUK service/domain owner | Academic Affairs; VNUK IT; Yuhan | Tamas; Zsombi; sponsor |

Task-level accountability is shown in Table 11. Each activity has one accountable owner. Decision rights remain separate from consultation: the pod can make delivery decisions within agreed guardrails, while Academic Affairs retains authority over academic guidance and the VNUK service owner retains authority over operational continuation, pause or stop decisions.

## 5.8 Product–Platform Interaction Model

The product uses one authenticated student front door while existing systems and departmental ownership remain behind it. Three interfaces carry the service. First, the student chat portal: a web application that only verified VNUK students can use, checked read-only against the institution’s student and staff account list. Second, the approved knowledge base: not public, stored in a database and reached only through a retrieval gateway that passes approved passages to the AI service, which writes the answer shown to the student with its source, owner and review date. Third, institutional email: when an answer is not good enough, the portal suggests the office that owns the topic, the student confirms, and the system sends one email to that office with the full context and a request ID, copying the student. Offices resolve the request in their normal email. Each email carries a footer link to a status-and-feedback page for that request ID, where staff log the status and rate whether the context was enough, and the student can rate the staff answer. If no status is logged within two days, the system sends a reminder with the same link. The portal centralizes access and routing; it does not replace EMS, LMS, official academic systems or departmental ownership, and it never guesses an answer it cannot support.

## 5.9 Operating-Model Recommendation

A hub-and-spoke operating model is the best initial fit. Product and service ownership should sit close to Student/Academic Services and programme operations, while scarce technology, security, data and AI capabilities remain shared. A fully embedded model would require stronger local product and engineering maturity than the evidence currently supports; a fully centralized digital factory would risk recreating business handoffs. The hybrid model therefore balances domain ownership with shared guardrails.

## 5.10 Portfolio Governance and Funding

Funding should follow evidence rather than guarantee a multi-year AI build. A stage/evidence mechanism is appropriate for the uncertain pilot: release enough capacity for baseline, prototype and evaluation; then continue, pivot, scale or stop based on agreed evidence. Portfolio review questions should cover strategic fit, student and staff value, learning, capability constraints, risk effectiveness and the next capacity decision.

Five guardrails are recommended: (1) financial capacity envelope and benefit owner; (2) architecture/data standards; (3) privacy, security and AI-risk controls; (4) student/staff service-quality and accessibility standards; and (5) delivery and escalation rules. AI investment should require evidence of incremental value over the non-AI alternative.

## 5.11 Capability and Sourcing Plan

| **Capability** | **Core?** | **Recommended sourcing** | **Reason** |
|----|----|----|----|
| Product/service ownership | Core | Build / assign internally | Must retain outcome accountability and learning |
| Academic content ownership | Core | Internal | Authoritative domain knowledge cannot be outsourced |
| UX/service design | Important | Build + short-term partner if needed | Needs close user access and knowledge transfer |
| Engineering / prototype | Mixed | Borrow/build/partner | Speed may justify external capacity, but code/data must remain portable |
| Data/analytics | Core learning capability | Build/borrow | Needed for evidence and future service improvement |
| AI specialist capability | Noncore initially | Partner / approved platform | Specialist and uncertain; retain internal governance |
| Privacy/security assurance | Core control | Shared institutional specialist | Material risk and legal responsibility |

External partners may accelerate delivery but should not own the Product Goal, backlog trade-offs, authoritative content or outcome accountability. Any partner arrangement should include knowledge transfer, documented decisions, data/code portability and an exit plan.

**CHAPTER 6. DATA, AI, TECHNOLOGY ARCHITECTURE, AND DIGITAL TRUST**

## 6.1 Data Requirements and Readiness

The minimum data model should capture only what is necessary to operate and evaluate the service: request ID, request category, programme or context, timestamps, assigned owner, status, resolution type, repeat contact, handoff count, duplicate-routing flag, student or staff feedback and handling or maintenance effort. Personal identifiers should be separated from aggregated analytics where possible. Identity data is used only for access verification in the MVP. Data quality rules should define mandatory fields, valid categories, closure conditions, duplicate detection and review responsibilities. Data ownership should be split between the service owner for operational data and Academic Affairs or programme content owners for authoritative guidance.

Readiness is currently low-to-partial because baseline event data is not consistently captured. The project should therefore treat analytics as a design requirement from the beginning rather than as a later dashboard exercise. This aligns with evidence that higher-education analytics requires robust data governance and architecture before more advanced predictive or AI use (Peck, 2023; Stojanov & Daniel, 2024).

## 6.2 AI Use Cases and Boundaries

The initial AI use cases are narrow: classify the enquiry topic, retrieve relevant approved content, write a clear answer from it, summarize the conversation for the routed email and suggest a staff reply draft. AI must not infer registration status, eligibility, grades, tuition liability or other authoritative decisions; such questions are routed. Each answer has a 1–5 rating, and a low rating opens a short ‘why?’ prompt. Sessions are logged and reviewed weekly: frequently asked questions become plain FAQ pages that students can read without calling the AI, which also reduces token cost, and poorly rated or unanswered questions enter a reviewed content-gap queue. Conversations are not automatically used to retrain the model; Maddie and Academic Affairs classify each gap, approve any content change and refresh the retrieval index through a controlled process.

## 6.3 Conceptual Architecture

The conceptual architecture has seven connected elements: (1) authenticated student and staff interface; (2) workflow and routing; (3) request and status store; (4) approved knowledge repository; (5) retrieval and optional AI classification or drafting service; (6) institutional email service; and (7) analytics, audit and monitoring. Identity and access, logging, security and privacy controls cut across all elements. The architecture supports request IDs, staff status updates, closure confirmation, duplicate-routing detection, reminder messages and an outage webhook. Direct academic-record transactions remain outside the first pilot.

## 6.4 Nonfunctional Requirements and Trust Controls

- Accuracy: at least 80% of rated answers should score 4 or 5 out of 5, with zero critical wrong guidance on eligibility, grades, finance or official records. Self-service: at least 75% of questions should be answered without routing to an office. Routing: at least 80% of routed requests should reach the correct office first time, and staff should rate the context of routed emails at 4 or more out of 5. These are proposed pilot thresholds, not measured VNUK baselines.

- Traceability: student-facing guidance should show the source or responsible office; content items require owner and review date.

- Privacy: collect the minimum data needed, apply role-based access and defined retention, and complete the required institutional/legal assessments.

- Security: use approved identity, logging and hosting controls before identifiable cases are stored.

- Accessibility: the guidance flow should be usable with common devices and support clear language rather than assume AI conversation is the only route.

- Resilience: if the portal is down or failing, a monitoring webhook posts an alert to the team’s group chat with the error and first steps, while students see a status page saying the team is fixing the problem and to try again in a few minutes. The same page lists a department email directory by topic (for example, registration and graduation questions to Academic Affairs, fees to Finance) so urgent requests still reach the right office. Email-delivery failures are retried and logged, offices receive a reminder when no status is logged after two days, and duplicate requests are linked to one request ID.

- Observability: monitor routing errors, unresolved cases, model failures and content expiry.

# CHAPTER 7. CHANGE, ADOPTION, TALENT, AND CULTURE

Adoption is a workflow change, not merely a communications campaign. Students must know when to use the standard route; staff must trust the content, accept clear ownership, use the request ID and update status or closure rather than recreating informal side channels. Academic Affairs must approve and maintain guidance. The three-week pilot with five students provides usability and workflow evidence, not a general prevalence estimate.

| **Stakeholder** | **Likely change impact** | **Adoption action** | **Measure** |
|----|----|----|----|
| Students | New standard route and request preparation | Co-design, simple onboarding, comparison with existing email | Use rate; task completion; effort |
| Staff resolvers | Routed requests arrive as one email with full context; reply in normal email and log status through one link | Workflow walkthrough, status-link training, week-2 workload review, two-day reminders | Handling time; status-link use; context rating |
| Content owners | Named review responsibility | Content templates, review calendar, backup owner | On-time review; expired-content rate |
| IT / data / privacy | New support and assurance obligations | Define service levels, controls and escalation | Incidents; support load; control completion |
| Management | Evidence-based continue/pivot/stop decisions | Quarterly portfolio review | Benefit and risk decisions made on evidence |

Training should be role-specific: students need to understand the service boundary and feedback flow; Maddie needs the requirements and backlog workflow; Tamas and Zsombi need release, monitoring and data controls; Yuhan needs the test and feedback protocol; resolvers need routing and closure rules; content owners need approval and review procedures; and the pod needs analytics and AI-risk literacy. Reinforcement should use visible metrics, feedback and retrospective learning rather than compliance messaging alone.

# CHAPTER 8. IMPLEMENTATION, SCALING, PERFORMANCE, AND GOVERNANCE

## 8.1 Three-Wave Roadmap

| **Wave** | **Business/service** | **Data & technology** | **People & adoption** | **Exit evidence** |
|----|----|----|----|----|
| Wave 1: Prove (0–3 months) | One bounded enquiry journey; dual-user baseline; content and routing pilot | Basic workflow, case tracking, approved knowledge, analytics events | Named owner; staff/student co-design; training | Baseline complete; content maintainable; pilot usable; privacy controls approved |
| Wave 2: Expand (3–9 months) | More request categories and matched programme comparison | Status visibility; analytics dashboard; AI classification/retrieval test | Wider staff adoption and content ownership | Measured student/staff improvement; stable routing; acceptable AI quality |
| Wave 3: Scale (9–18 months) | Broader programme rollout where transferability is proven | Reusable integrations; selective AI-assisted response/proactive support | Persistent product operating model | Sustained KPI benefit; repeatable capabilities; acceptable unit economics |

Scale should occur by unit of proven transferability, not by institution-wide announcement. The unit of scale is a programme or repeatable academic-enquiry category. The reusable core is the portal pattern, knowledge schema, request taxonomy, routing rules, request ID, email handoff, event definitions, test sets, privacy controls and governance routines. Local configuration includes contacts, policies, programme or cohort rules and review calendars. A programme joins only when content ownership, workflow, baseline and required controls are ready.

## 8.2 KPI and Benefit Ownership

| **KPI** | **Benefit owner** | **Review cadence** |
|----|----|----|
| Correct guidance / routing | Product owner + programme content owner | Sprint / monthly |
| Repeat contact and resolution time | Service/domain owner | Monthly |
| Staff clarification/redirection effort | Service/domain owner | Monthly |
| Total staff workload incl. maintenance | Service owner + sponsor | Monthly / stage gate |
| Adoption by students and staff | Change/adoption lead | Monthly |
| Content currency | Programme/content owners | Monthly |
| Privacy/security/AI incidents | Risk/privacy + IT | Immediate + quarterly |
| Net capacity value / operating cost | Sponsor / finance | Quarterly |

## 8.3 Governance and Stage Gates

Governance should focus on outcomes, capacity and risk rather than micromanaging Sprint tasks. Stage Gate 1 approves the pilot after owner, baseline, content, identity and privacy readiness are confirmed. Stage Gate 2 approves AI testing only after the non-AI service works and the test set is ready. Stage Gate 3 approves expansion only after dual-user benefits, routing accuracy and workload sustainability are demonstrated. Pause the AI layer when students use the service but rate its answers poorly (below 70% rated 4–5 in a week), when repeated unsupported answers, bugs or duplicate requests appear, when requests go to the wrong office and lengthen resolution, when staff rate context below 3 out of 5, or when privacy or access controls fail; plain guidance and email routing may continue while the cause is fixed. Stop the MVP when fewer than three of the five pilot students keep using it after onboarding and fixes, when no VNUK office accepts ownership of the guidance, when approved access cannot be established, when critical errors remain unresolved, or when the pilot shows no credible improvement after two corrective cycles. Stage Gate 4 approves broader scale only after unit economics and repeatable capabilities are evidenced.

## 8.4 Final Risk Register

| **Risk** | **Likelihood** | **Impact** | **Owner** | **Treatment** |
|----|----|----|----|----|
| Outdated / incorrect academic guidance | Medium | High | Content owner | Versioning, review date, refusal/escalation |
| Staff capacity insufficient | Medium | High | Domain owner | Baseline workload, protected capacity, limit scope |
| Low student adoption | Medium | Medium | Product/change lead | Co-design, usability, channel transition plan |
| AI adds no value | Medium | Medium | Product owner | A/B comparison with non-AI service; stop AI layer |
| Personal-data misuse | Low–Medium | High | Privacy/data owner | Data minimization, access, assessment, vendor controls |
| Integration delays | Medium | Medium | IT lead | Pilot without live integration; API only after evidence |
| Scope creep across programmes/services | High | Medium | Product owner | One product area; explicit backlog boundary and stage gates |

# CHAPTER 9. CRITICAL EVALUATION AND LESSONS

The proposal has changed materially through critique. First, the original framing risked treating students as the only user group. Lecturer feedback exposed the operational blind spot: staff can receive either benefit or additional hidden work from the same product. The revised design therefore measures dual-user value and embeds staff representation in the pod. Second, the Week 5 presentation framed the product as university-wide while the report proposed a CSE-first guidance use case. The revised model separates the long-term Student Support product from the initial academic-enquiry journey and its three test scenarios. Third, the design now uses one student-facing front door while preserving existing systems and departmental ownership behind it. Fourth, the simpler non-AI service, controlled email handoff and reviewed content-gap workflow precede any AI expansion.

Third, the project has moved further away from technology-first reasoning. Higher-education digital-transformation research indicates that isolated technology initiatives do not constitute transformation without organizational alignment (Fernández et al., 2023), and UNESCO cautions against uncritical GenAI adoption in education (UNESCO, 2023). Accordingly, the approved knowledge base, ownership, workflow and measurement now precede AI. The simpler non-AI service is treated as a serious alternative rather than a temporary placeholder.

Fourth, the business case is intentionally modest. The illustrative capacity model is useful for sensitivity analysis but cannot establish ROI without measured demand, handling effort, content cost and technology quotations. Student time saved and service consistency may justify experimentation even when direct financial payback is weak, but those benefits should not be converted into cash without a defensible valuation method. This avoids double counting and false precision.

The main contextual limitation remains evidence quality. Current student data is small and partly historical, staff workload data is not systematic, and IBM-specific evidence has not yet been established. Therefore, the report should not claim that the same pain point has the same magnitude across all three programmes. Transferability is an empirical question for the pilot, not an assumption. Similarly, legal and technical sections identify relevant controls but do not substitute for authorized VNUK legal, security or procurement review.

# CHAPTER 10. CONCLUSION AND DECISION REQUEST

Student Support and Academic Navigation remains the recommended priority domain, but the recommendation is now narrower and more defensible. VNUK should proceed with a bounded, dual-user pilot focused on academic enquiry guidance and routing. The product should help students identify and complete the correct next step while helping staff receive better-formed, correctly routed cases with sustainable total workload.

The requested decision is approval for Wave 1 validation and pilot preparation, not approval for university-wide AI deployment. Proceeding conditions are: (1) nominate a domain/product owner; (2) collect comparable student and staff baselines; (3) validate the first journey and request taxonomy; (4) nominate content owners and approve the initial knowledge set; (5) confirm privacy/security arrangements; and (6) allocate protected staff review capacity. CSE is the evidence-rich starting context; IBM and BMS should enter the same product experiment after their equivalent baseline and ownership conditions are met.

The next stage should create the non-AI guidance/routing service first and then test whether AI provides measurable incremental value. Continue if student effort, confirmed resolution, routing quality and staff workload all move in the intended direction with acceptable risk. Adapt if the service creates value but workflow, content or adoption needs correction. Pause or stop the AI layer if critical misleading guidance occurs, staff cannot maintain the knowledge, privacy controls are inadequate, escalation becomes unsustainable, or the simpler service performs equally well with less cost and risk.

# References

Chugh, R., Turnbull, D., Cowling, M. A., Vanderburg, R., & Vanderburg, M. A. (2023). Implementing educational technology in higher education institutions: A review of technologies, stakeholder perceptions, frameworks and metrics. Education and Information Technologies, 28, 16403–16429. https://doi.org/10.1007/s10639-023-11846-x

Customer Experience project teams. (2026a). Customer Experience module research on CSE student journeys \[Unpublished interview records and project analyses\]. VNUK Institute for Research and Executive Education.

Customer Experience project teams. (2026b). Customer Experience module research on BMS student experience \[Unpublished survey results and project report\]. VNUK Institute for Research and Executive Education.

DBB43005 teaching team. (2026a). Session 4: Digital strategy and transformation roadmap \[Course slides\]. VNUK Institute for Research and Executive Education.

DBB43005 teaching team. (2026b). Session 6: Cross-functional teams, operating models, and digital capabilities \[Course slides\]. VNUK Institute for Research and Executive Education.

EDUCAUSE. (2024). 2024 students and technology survey. https://www.educause.edu/research-and-publications/research/analytics-services/surveys/2024/educause-student-survey

Fernández, A., Gómez, B., Binjaku, K., & Meçe, E. K. (2023). Digital transformation initiatives in higher education institutions: A multivocal literature review. Education and Information Technologies, 28, 12351–12382. https://doi.org/10.1007/s10639-022-11544-0

Government of Vietnam. (2025). Decree No. 356/2025/ND-CP detailing a number of articles and measures for implementation of the Law on Personal Data Protection.

Group 1. (2026). Follow-up validation of BMS and CSE issue status \[Unpublished team communication with departmental contacts\]. VNUK Institute for Research and Executive Education.

National Assembly of Vietnam. (2025). Law No. 91/2025/QH15 on Personal Data Protection.

National Institute of Standards and Technology. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0) (NIST AI 100-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

National Institute of Standards and Technology. (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1

Peck, E. (2023). Student analytics: A core specification for engagement and wellbeing analytics. Jisc. https://www.jisc.ac.uk/reports/student-analytics-a-core-specification-for-engagement-and-wellbeing-analytics

Schwaber, K., & Sutherland, J. (2020). The Scrum Guide: The definitive guide to Scrum: The rules of the game. https://scrumguides.org/scrum-guide.html

Stojanov, A., & Daniel, B. K. (2024). A decade of research into the application of big data and analytics in higher education: A systematic review of the literature. Education and Information Technologies, 29, 5807–5831. https://doi.org/10.1007/s10639-023-12033-8

Team Topologies. (n.d.). Key concepts and practices for applying a Team Topologies approach to team-of-teams org design. https://teamtopologies.com/key-concepts

UNESCO. (2023). Guidance for generative AI in education and research. https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

University of Danang. (2025). Annual Report UD–2024: Highlights and development orientation. https://vnuk.udn.vn/en/the-university-of-danang-introduces-the-annual-report-ud-2024/

VNUK. (n.d.-a). Vision–mission–core values. https://vnuk.udn.vn/en/vision-mission-corevalues/

VNUK. (n.d.-b). Introduction. https://vnuk.udn.vn/en/about-us/

# Appendix A. Dual-User Baseline Measurement Dictionary

| **Metric** | **Operational definition** | **Source** |
|----|----|----|
| Eligible enquiry volume | Number of enquiries within the pilot taxonomy during the measurement window | Case log / email audit |
| First substantive response | Time from request receipt to first non-automated response that addresses the issue | Case timestamps |
| Confirmed resolution | Answer confirmed or referral completed with no unresolved required action | Case closure |
| Repeat contact | Same user contacts again about the same unresolved issue within 7 days | Case/thread match |
| Handoff count | Number of changes in responsible person/unit before resolution | Case history |
| Clarification effort | Staff minutes spent requesting missing information | Time sample / staff log |
| Redirection effort | Staff minutes spent identifying and forwarding to correct owner | Time sample / staff log |
| Content-maintenance effort | Minutes spent creating, checking or updating approved guidance | Content log |
| Routing accuracy | Cases sent to the correct owner on first assignment / assessed cases | QA review |
| User-rated answer usefulness | Student rating of the answer on a 1-5 scale; record reason for ratings below 4 | Portal feedback |
| Duplicate routing | Same request ID or materially identical request sent to more than one department without an intentional escalation | Request log / email audit |
| Closure confirmation | Staff or student confirms that the answer or referral completed the required next step | Status link / case log |

# Appendix C. Estimated Baseline Figures

The baseline figures in Section 3.3 are working estimates, not measured VNUK data. They will be replaced with measured values during Wave 1.

Eligible enquiries (about 120 per month; about 60 per week at peak): scaled from the report’s illustrative volume of 500 enquiries per month across VNUK, assuming final-year CSE students generate about a quarter of academic enquiries, with peaks taken from the registration and graduation windows seen in the mailbox review.

First reply (median one working day; about 20% over three working days): Academic Affairs replied the same or the next working day in every thread reviewed; the four-to-five-day advising delay reported in interviews is used as the long tail.

Multiple channels (about 30%): based on interview accounts of students contacting lecturers, friends and offices about the same issue, and on the 35% reply-all share in the mailbox sample.

Wrong office first (about 15%): based on login and access questions first sent to Academic Affairs or Finance and then forwarded to IT in the mailbox sample.

Staff handling time (8 minutes per routed email): the report’s illustrative scenario value.

Mailbox sample (23 requests; 8 reply-all; 2 refused): counted directly from one team member’s VNUK mailbox, 2022–2026, with other students anonymised and registration-portal overload reports excluded.

# Appendix B. Staff Validation Interview Guide

- What types of student academic enquiries do you receive most frequently?

- Which enquiries are most commonly sent to the wrong person or unit?

- What information is often missing when students contact you?

- Which enquiries usually require repeated clarification or follow-up?

- Approximately where does your time go: answering, clarifying, redirecting, checking rules, or updating information?

- Which common questions could safely be supported by approved self-service guidance?

- Which questions must always remain with authorised staff?

- What would make a Student Support and Academic Navigation service useful rather than additional work for you?

- What risks would make you unwilling to use or maintain the service?
