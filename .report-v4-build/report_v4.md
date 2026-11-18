# CHAPTER 1. EXECUTIVE SUMMARY

VNUK, a member institute of the University of Danang, aims to offer modern programmes in a friendly and inspiring environment (VNUK, n.d.-a). This report treats student support as part of that environment. The selected domain is Student Support and Academic Navigation, and the first product, Ask Nuki, covers academic enquiry guidance and routing. Students and staff are both primary users. Students need a clear next step and a transparent handoff; staff need complete, correctly routed requests and guidance they can maintain.

The evidence combines Customer Experience research (15 CSE students and five faculty members; a BMS survey of eight) with a review of 23 real requests from one VNUK mailbox. Eight of those requests were sent by reply-all to a whole cohort, and VNUK's website has no FAQ page (Customer Experience project teams, 2026a, 2026b; Group 1, 2026). These sources show failures and routing patterns, not institution-wide prevalence. Student Support ranked first of three candidate domains because a guidance-and-routing pilot needs no access to grades or official records.

The recommendation is a bounded, dual-user pilot. Ask Nuki answers from guidance approved by Academic Affairs, refuses to guess on official decisions and routes everything else once to the right office with a request ID. The non-AI service comes first, and AI is kept only if it adds measurable value (Fernández et al., 2023; UNESCO, 2023). The decision requested is Gate 1: a three-week pilot with five final-year CSE students. Growth follows only on evidence, first by expanding within Academic Affairs and then by scaling one department at a time. Each step has a readiness check, a measurement plan and a stage gate, and every design choice respects Vietnam's Personal Data Protection Law No. 91/2025/QH15. Appendix D maps each Session 9 comment to the section that answers it.

# CHAPTER 2. ORGANIZATION, INDUSTRY, AND TECHNOLOGY CONTEXT



## 2.1 Organization, Mission, and Strategic Alignment

VNUK's vision is to become an international-standard university, and its mission includes modern programmes, essential skills for learners and a friendly, inspiring environment for faculty and learners (VNUK, n.d.-a; VNUK, n.d.-b). Student Support and Academic Navigation does not create learning outcomes itself. It removes service friction that stops students from following procedures and reaching the right support, and it frees staff time from low-value clarification. This links directly to the University of Danang's learner-centred and digital-transformation priorities (University of Danang, 2025).

## 2.2 Dual Users and Value Proposition

The product has two primary user groups. Students need to find the correct procedure, prepare a complete request, reach the responsible unit and know what happens next. Staff, including advisers and administrative officers, need requests that arrive complete, correctly routed and supported by current, approved guidance. The value proposition is therefore dual: students complete the next step with less uncertainty, and staff resolve better-formed enquiries without hidden extra work. A service is not successful if students save effort but staff inherit more checking or maintenance. This framing follows research stressing stakeholder perceptions and implementation context over technology availability (Chugh et al., 2023).

## 2.3 Higher-Education and Technology Pressures

Higher-education transformation is organisational, involving processes, people and information as well as technology (Fernández et al., 2023). VNUK's problem is not a lack of channels but the weak link between guidance, routing, ownership and measurement. Students increasingly expect self-service and all-in-one access to institutional services (EDUCAUSE, 2024), although this does not prove that VNUK students want a chatbot. Data-supported student services can be more responsive when governance keeps the human experience central (Peck, 2023; Stojanov & Daniel, 2024); the first step for VNUK is simply to capture service events consistently. Generative AI adds potential and risk: UNESCO (2023) and NIST (2023, 2024) call for human oversight, testing and lifecycle controls. These principles support keeping academic decisions with authorised staff and retaining a non-AI fallback.

## 2.4 Relevant Technologies, Feasibility, and Regulation

The minimum technology set is a controlled knowledge repository, request routing, case tracking, basic analytics and a simple interface. Retrieval-based AI may later support classification and answering from approved material, but the service must work without it. That gives a fair comparison: if search and routing alone deliver the same outcomes at lower cost and risk, the AI layer should not be scaled. Readiness is partial. Channels and expertise exist, but integration, budget, demand data and staff time for content governance are not yet confirmed.

Personal-data handling must follow Law No. 91/2025/QH15 on Personal Data Protection, in force since 1 January 2026, and Decree No. 356/2025/ND-CP (National Assembly of Vietnam, 2025; Government of Vietnam, 2025). Practical controls are data minimisation, a stated purpose, role-based access, retention rules, logging and assessment before any cross-border processing. The report does not claim legal clearance; VNUK's authorised reviewers decide the final approach.

## 2.5 Stakeholder Map

Stakeholders are mapped on an influence–impact grid, a standard stakeholder-analysis tool that places each group by its influence over the decision to implement and by how much the change affects its daily work (Project Management Institute [PMI], 2017; Bourne & Walker, 2005; Ackermann & Eden, 2011). After the Session 9 review, the map names the people who make the implementation decision: the VNUK Director or Dean as sponsor, the Head of Academic Affairs as service owner and the VNUK IT team. Earlier versions referred only to "management". The grid feeds three later artefacts: the engagement strategy for each group (Chapter 7), the accountable roles in the RACI (Table {T:raci}) and the decision owners in the adoption roadmap (Figure {F:roadmap}).

FIG[grid]: fig_stakeholder_grid.png | Stakeholder Influence–Impact Grid

TABLE[stake]: Stakeholder Map with Influence, Impact and Engagement Strategy

| **Stakeholder** | **Primary need** | **Influence** | **Impact** | **Strategy and role** |
|----|----|----|----|----|
| VNUK Director / Dean (sponsor) | Strategic fit, evidence, risk control | High | Low–medium | Keep satisfied; approves Gates 1, 3 and 4 and funding |
| Head of Academic Affairs (service and content owner) | Accurate guidance; sustainable office workload | High | High | Manage closely; accountable for approved guidance and for the week-3 decision |
| VNUK IT team and privacy adviser | Secure, supportable and lawful solution | High | Medium | Manage closely; accountable for identity, data and hosting controls |
| Heads of other offices (IT Support, Student Affairs, Finance, Assessment Unit) | Clear routing; no extra inbox | Medium–high | Low now; high when they join | Keep satisfied; each decides whether its office joins in Wave 3 |
| Office staff (resolvers) | Complete requests, clear ownership, no hidden work | Low–medium | High | Keep informed and involve; proof-of-concept testers |
| Final-year students | Correct next step, low effort, visible status | Low | High | Keep informed and involve; proof-of-concept testers |
| Lecturers and faculty advisers | Fewer misdirected questions | Low | Low–medium | Monitor; informed through the change story |

Positions are the team's judgement and the named individuals still need VNUK confirmation. Students and office staff have the highest impact and the least influence, so the plan involves them directly as testers. The Director, the Head of Academic Affairs and the IT team have the most influence, so the plan asks them for decisions at defined gates rather than consulting them informally.

# CHAPTER 3. CURRENT-STATE DIAGNOSIS AND PRIORITY-DOMAIN SELECTION



## 3.1 Evidence Base and Limitations

The diagnosis combines student interviews, faculty material, survey charts and reconstructed journeys from earlier Customer Experience work. Research was conducted mainly during December 2025–January 2026. Group 1 later contacted departmental stakeholders in October 2026 and qualitatively revalidated that the issues remained relevant, but no repeat survey was administered. The reported CSE study covered 15 students and five faculty members; the material reviewed in depth for this project covers ten students or alumni and one faculty member. The BMS survey contains eight respondents, and a completed BMS faculty transcript was not available for this assessment (Customer Experience project teams, 2026a, 2026b; Group 1, 2026).

These limitations are consequential. Historical counts are not current prevalence estimates. One student’s four-to-five-day advising response is evidence that a failure occurred, not evidence that VNUK’s average response time is four to five days. Likewise, the BMS n=8 survey can identify issues for investigation but cannot support population-level claims. The analysis therefore separates observed evidence, team interpretation and unverified assumptions.

## 3.2 Recorded Student and Staff-Side Evidence

CSE accounts show variation rather than uniform failure: one student needed four to five LMS login attempts and waited four to five days for an advising reply, while an alumnus missed a graduation notice but was then helped by faculty (Customer Experience project teams, 2026a). BMS respondents mainly reported practical-learning barriers, such as heat-related fatigue (seven of eight) and insufficient practical time (four of eight), which belong to a separate domain (Customer Experience project teams, 2026b). Staff-side evidence is weaker: there is no systematic workload baseline yet, so one will be collected before launch.

A more recent source is one team member's VNUK mailbox for 2022–2026, with 23 academic requests (12 the member's own, 11 from other students, anonymised). Figure {F:requests} shows that almost half went to Academic Affairs. Eight were sent by reply-all to a whole cohort list, and two were refused because of rules the student learned only by asking. A check of vnuk.udn.vn on 11 November 2026 found no FAQ or help page. These counts show a routing pattern, not prevalence.

FIG[requests]: fig_requests.png | Where 23 Real Academic Requests Went

## 3.3 Dual-User Baseline Framework

TABLE[baseline]: Dual-User Baseline Framework

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

The current journey is: question raised, guidance sought, need clarified, resolved or routed, answer confirmed. Likely causes of repeat contact are dispersed guidance, unclear ownership, incomplete requests and staff workload; the evidence does not separate them, so each remains a hypothesis to test. Figure {F:asis} models this journey in BPMN 2.0, the standard notation for business processes (Object Management Group [OMG], 2011; ISO/IEC, 2013), so the pain points sit on a model others can check. A parallel gateway shows students trying several channels at once, and a loop shows repeat contact. Practical learning and academic progression follow different journeys with physical or authoritative-data constraints, so they stay outside this product.

FIG[asis]: fig_bpmn_asis.png | As-Is Academic Enquiry Process (BPMN 2.0)

## 3.5 Candidate Domains and Capability Assessment

TABLE[cand]: Candidate Domains and Capability Assessment

| **Candidate** | **Value signal** | **Key capability position** | **Main constraint** |
|----|----|----|----|
| A. Student Support & Academic Navigation | Guidance, enquiry resolution and repeat-contact reduction | Channels/expertise partial; guidance/routing/data gaps | Owner, staff capacity and maintainable content |
| B. Practical Learning & Resource Operations | Practical-time and physical-resource pain points | Many usage/capacity/tool unknowns | Physical constraints and weak baseline |
| C. Academic Progression & Milestones | High consequence of status/notice errors | Portal/records partial | Authoritative data and approval dependencies |

The Week 3 capability assessment used six dimensions: roadmap, talent, operating model, technology, data and adoption. For Student Support, the immediate gaps were accountable ownership, organized guidance, routing and case tracking; technology and talent were assessed as partial rather than absent. This pattern reinforces the decision to treat the transformation as service redesign supported by digital capability.

## 3.6 Consistent Prioritization and Decision

The prioritization framework weights Value Potential at 30%, Feasibility at 25%, Strategic Relevance at 20%, Urgency at 15% and Learning Value at 10%. Group 1’s proposed scores produced 4.10/5 for Student Support, 3.80 for Academic Progression and 3.50 for Practical Learning. These are structured team judgments, not measured financial returns. A sensitivity test showed that if Student Support feasibility falls from four to two, its score falls to 3.60 and Academic Progression leads. The selection is therefore conditional on staff capacity, approved content and ownership.

FIG[priority]: fig_priority.png | Weighted Prioritisation of Candidate Domains

The priority decision is Student Support and Academic Navigation. To respond to lecturer feedback that the MVP must be journey-led, the first release follows one end-to-end journey: a final-year student’s path to graduation. This journey is long enough to touch several offices—registration of remaining and required modules, academic advising, VSTEP, physical and defence education, project topic registration, and graduation applications and transcripts—yet bounded to one cohort and one clear outcome. Course registration on its own was rejected as the MVP journey because it is short and would push the product towards automated registration, which is out of scope. CSE final-year students provide the first context; IBM and BMS follow only after the same dual-user baseline is collected.

# CHAPTER 4. TRANSFORMATION VISION, VALUE LOGIC, AND SOLUTION PORTFOLIO



## 4.1 Vision and Future State

> *Within 12 months, VNUK will transform academic enquiry navigation from fragmented and reactive support into a coordinated, trackable and measurable dual-user service that helps students reach the correct next step while enabling staff to receive clearer, better-routed enquiries and reduce avoidable repetitive work.*

The vision remains technology-neutral. Higher-education transformation research warns against equating transformation with tool adoption; organizational processes, information, people and governance must change together (Fernández et al., 2023). AI may support the future state, but a reliable non-AI path remains part of the design.

## 4.2 User and Business Needs

TABLE[needs]: User and Business Needs

| **User / need** | **Current friction** | **Desired outcome** |
|----|----|----|
| Student: understand next step | Scattered guidance and uncertainty | Verified procedure and responsible contact |
| Student: complete request | Missing documents/context can trigger follow-up | Checklist and structured request |
| Staff: receive actionable case | Clarification and redirection | Correct category, context and ownership |
| Staff: maintain guidance | Information can be dispersed or outdated | Named source, owner and review date |
| Management: improve service | Limited case-level evidence | Comparable KPI and benefit evidence |

## 4.3 Objectives and Measurement

TABLE[obj]: Objectives and Measurement

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

Figure {F:bdn} expresses the same logic as a benefits dependency network (Ward & Daniel, 2012). It shows that the benefits depend on enabling changes and business changes, not on the technology alone. The enabling changes are Academic Affairs approving dated guides, offices agreeing routing rules and a response window, and students and staff being onboarded. The business changes are students asking in one place first, offices answering routed requests with one ID, and a weekly review that turns frequent questions into FAQ pages. Each benefit has an owner in the measurement plan (Table {T:kpi}).

FIG[bdn]: fig_bdn.png | Benefits Dependency Network for Ask Nuki

## 4.5 Coherent Solution Portfolio

TABLE[portfolio]: Coherent Solution Portfolio

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

FIG[breakeven]: fig_breakeven.png | Illustrative Break-Even Analysis

Figure {F:breakeven} also shows why growth matters. The Wave 1 working baseline of about 120 eligible enquiries a month is well below break-even, so the pilot is justified as learning rather than as saving. The economic case depends on expanding to more students and scaling to more departments under the conditions in Chapter 8.

### 4.7.5 Risk Case

TABLE[riskcase]: Risk Case

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

TABLE[stories]: Core User Stories and Acceptance Criteria

| **User story** | **Acceptance focus** |
|----|----|
| As a student, I want to select my type of academic request and see the verified procedure and responsible contact, so that I can complete the correct next step without repeatedly contacting different staff. | Applicable guidance shown; required steps/documents visible; correct responsible unit displayed. |
| As a staff member, I want student enquiries to arrive with the correct category and required information, so that I can resolve cases faster and spend less time clarifying or redirecting requests. | Request includes agreed mandatory fields; correct queue/owner; incomplete requests flagged before submission. |
| As a programme/content owner, I want to review and update approved guidance in one place, so that students and staff use current information. | Every item has source, owner, programme/cohort applicability and review date. |
| As a service owner, I want case and workload measures to be captured consistently, so that I can decide whether to continue, adapt or scale the product. | Category, timestamps, owner, resolution, repeat-contact and effort data available without unnecessary personal data. |

A shared safety rule applies across stories: when approved guidance is missing, conflicting or insufficient, the product must stop and route the case to an authorised staff member rather than infer an academic or financial decision.

After the lecturer's feedback, the team also wrote user stories for each department that receives student questions (Table {T:deptstories}). They keep the role–goal–benefit structure of agile user stories (Cohn, 2004) but start from the problem the role meets today ("As a …, I find …, so …"). This links each real friction to the Ask Nuki feature that addresses it. A department's stories become its acceptance tests when it joins in Wave 3.

TABLE[deptstories]: Problem-First User Stories by Department

| **Department** | **User story: "As a …, I find …, so …"** | **Ask Nuki feature** | **Acceptance criteria** |
|----|----|----|----|
| Academic Affairs | As an Academic Affairs officer, I find the same credit-limit and registration-window questions arrive by email and reply-all every term, so I want students to read an approved answer first. | Dated guide with source and owner; answer card; FAQ page for frequent questions | At least 80% of credit-limit questions answered without an email; every guide shows owner and review date |
| Academic Affairs | As a graduation-application handler, I find requests arrive without the student's programme, cohort or form code, so I want routed requests to carry full context. | Routed email with verified student, topic, question, what Nuki showed and request ID | Staff context rating at least 4/5; no clarification email needed in at least 80% of cases |
| Assessment Unit | As an Assessment Unit officer, I find re-marking (phúc khảo) requests arrive after the deadline or at the wrong office, so I want students to see the deadline and the correct form first. | Re-marking guide with deadline and form; routing rule to the assessment mailbox | No re-marking request routed to Academic Affairs in the pilot test set |
| IT Support | As an IT Support officer, I find login and missing-Canvas-course problems go first to Academic Affairs or Finance and reach me days later, so I want them routed to IT on first contact. | Topic classification routes access issues to IT; self-help steps first | At least 90% of access questions reach IT first time; no forwarding between offices |
| Student Affairs | As a Student Affairs officer, I find students ask for confirmation letters and transcripts without knowing which form applies, so I want each request to name the form and documents. | Procedure checklist with form code (BM.ĐT.xx) before routing | Request includes form code and required documents in at least 90% of cases |
| Finance | As a Finance officer, I find tuition questions mix general rules with personal balances I should not discuss in a group thread, so I want general rules answered and personal cases routed with an ID. | General tuition guide; personal-balance questions refused by Nuki and routed | No answer states an individual balance; personal cases routed with a request ID |
| All offices (student view) | As a final-year student, I find I do not know which office owns my question and I email several, so I want one place that answers it or sends it once to the right office. | One front door; duplicate check; status tracking | No duplicate routing; the student sees the status until the request is closed |

## 5.4 Ordered Product Backlog

TABLE[backlog]: Ordered Product Backlog

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

Sprint 1 is a two-week learning Sprint, not a production deployment (Schwaber & Sutherland, 2020). The Sprint Goal is: a student selects a request scenario, sees a verified procedure and reaches the responsible unit when staff help is required; the receiving staff member gets the agreed minimum context. Days 1-2 audit enquiries and confirm taxonomy and baseline definitions; Days 3-4 structure guidance, staff workflow and ownership; Days 5-7 build the HTML flow; Days 8-9 run student and staff usability and QA tests; Day 10 reviews evidence and updates the backlog. The following three-week pilot tests the refined flow with five students. Live academic-record integration remains outside the MVP.

## 5.6 Agile Pod Archetype and User Representation

The recommended archetype is a journey-led product pod: it owns one end-to-end journey and a persistent service, keeping users, content owners and platform specialists in one feedback loop (Team Topologies, n.d.; DBB43005 teaching team, 2026b). A small MVP needs three capabilities, namely business analysis, software engineering, and UX/UI with quality assurance, so no separate researcher, project manager or data scientist is required. Three roles sit with VNUK: Academic Affairs approves and updates guidance, the IT team and privacy adviser review controls, and the Director or Dean decides at the gates.

TABLE[pod]: Agile Pod Roles

| Pod role | Primary accountability | Capacity approach |
|----|----|----|
| Maddie - Business Analyst | Turns customer feedback and product performance data into requirements, acceptance criteria and an ordered backlog; owns stakeholder alignment | Protected capacity across discovery, pilot and review |
| Tamas - Software Engineer | Chat portal, server, AI/API integration, and the institutional email and status-link service | Protected engineering capacity during build and pilot |
| Zsombi - Software Engineer | Student and staff account allowlist, knowledge database and retrieval, event logging and monitoring | Protected engineering capacity during build and pilot |
| Yuhan - UX/UI, QA and Customer-Facing Lead | Student journey and interface, testing, collecting student and staff feedback, and verifying improvements | Embedded throughout discovery, testing and pilot |
| Head of Academic Affairs (service owner) and content owner | Approve authoritative guidance and update it when policies change; record the week-3 decision | Institutional role; named owner required before pilot |
| VNUK IT / privacy adviser | Review identity, security, retention, hosting and AI-risk controls | Part-time shared specialist |
| Pilot students (proof-of-concept testers) | Use Nuki for real graduation-journey questions; rate answers; report effort and unmet needs | Five final-year CSE students across the three-week pilot |
| Office staff (proof-of-concept testers) | Answer routed requests in normal email; log status and rate context through the link | Staff in Academic Affairs and related offices, weeks 1–3 |
| VNUK Director / Dean (sponsor) | Approve pilot scope and budget (Gate 1) and any expansion or scaling (Gates 3–4) | Decisions at gates, informed by a weekly evidence brief |

## 5.7 Roles, Capacity, and Decision Rights

The four-student project team has protected capacity for the three-week pilot, while institutional roles remain subject to VNUK confirmation. The working loop is: Yuhan runs tests with students and staff and gathers their feedback; Maddie combines that feedback with the product's performance data and writes requirements; Tamas and Zsombi build and release the changes; Yuhan retests.

The RACI was revised after the Session 9 review in two ways. First, the proof-of-concept (POC) testers now have their own columns and Responsible tasks: the five pilot students and the office staff who answer their routed requests. During adoption these groups test the service, so listing them as only "informed" understated their role. Second, the decision-making tasks are explicit rows, owned by the people who decide whether to implement: the VNUK Director or Dean as sponsor, the Head of Academic Affairs as service owner and the VNUK IT team. Each row has exactly one Accountable role, following standard responsibility-assignment practice (PMI, 2017).

TABLE[raci]: Task-Level RACI Including POC Testers and Decision Tasks

| **Task** | **Maddie** | **Tamas** | **Zsombi** | **Yuhan** | **Pilot students** | **Office staff** | **Head of AA** | **IT team, privacy** | **Director, Dean** |
|----|----|----|----|----|----|----|----|----|----|
| *Delivery* |  |  |  |  |  |  |  |  |  |
| Define requirements, journey scope and ordered backlog | A | I | I | C | C | C | C | I | I |
| Map and test the student journey | A | I | I | R | C | C | C | I | I |
| Approve and update academic guidance | C | I | I | C | I | C | A | I | I |
| Build portal, routing, AI and email workflow | C | A | R | C | I | I | I | C | I |
| Implement identity, logging, retention and monitoring | C | C | R | I | I | I | I | A | I |
| *Proof-of-concept testing* |  |  |  |  |  |  |  |  |  |
| Use Nuki for real questions and rate answers | C | I | I | A | R | I | I | I | I |
| Answer routed requests, log status, rate context | C | I | I | C | I | R | A | I | I |
| Run usability, QA and feedback cycles; fix and retest | C | R | R | A | C | C | I | I | I |
| *Decisions* |  |  |  |  |  |  |  |  |  |
| Approve pilot scope, team and budget (Gate 1) | R | I | I | I | I | I | C | C | A |
| Approve sign-in list, data controls and hosting | C | C | R | I | I | I | I | A | I |
| Agree routing rules and response window for the office | R | I | I | C | I | C | A | I | I |
| Decide continue, pivot, pause or stop at week 3 | R | I | I | C | C | C | A | C | I |
| Allow the AI retrieval test (Gate 2) | C | R | C | I | I | I | A | C | I |
| Approve expansion and each new department (Gates 3–4) | R | I | I | C | I | C | C | C | A |

R = Responsible; A = Accountable; C = Consulted; I = Informed. Where the Head of Academic Affairs is Accountable for guidance, a named content officer does the work. The head of each receiving office is also Consulted on Gate 4. Decision rights stay separate from consultation. The pod makes delivery decisions within agreed guardrails, Academic Affairs keeps authority over academic guidance, and the Director keeps authority over whether the service is implemented, expanded or scaled.

## 5.8 Product–Platform Interaction Model

The product uses one authenticated student front door while existing systems and departmental ownership remain behind it. Three interfaces carry the service. First, the student chat portal: a web application that only verified VNUK students can use, checked read-only against the institution’s student and staff account list. Second, the approved knowledge base: not public, stored in a database and reached only through a retrieval gateway that passes approved passages to the AI service, which writes the answer shown to the student with its source, owner and review date. Third, institutional email: when an answer is not good enough, the portal suggests the office that owns the topic, the student confirms, and the system sends one email to that office with the full context and a request ID, copying the student. Offices resolve the request in their normal email. Each email carries a footer link to a status-and-feedback page for that request ID, where staff log the status and rate whether the context was enough, and the student can rate the staff answer. If no status is logged within two days, the system sends a reminder with the same link. The portal centralizes access and routing; it does not replace EMS, LMS, official academic systems or departmental ownership, and it never guesses an answer it cannot support.

### 5.8.1 Modelling Notation for the Full Service Flow

The free-form workflow sketch used in the Session 9 presentation has been replaced by standard notations, each chosen for its level of detail. For the full, cross-department service the report uses a BPMN 2.0 collaboration diagram (OMG, 2011). BPMN is the international standard for business-process models (ISO/IEC, 2013) and is designed for processes that cross organisational boundaries. Each participant is a pool, work inside a pool is joined by sequence flows, and messages between participants are drawn as separate message flows (Dumas et al., 2018). This suits Ask Nuki because the service is defined by handoffs between students, the portal, offices and content owners, not by the software alone. Figure {F:tobe} shows the to-be process; Figure {F:asis} in Section 3.4 shows the current process for comparison.

FIG[tobe]: fig_bpmn_tobe.png | To-Be Academic Enquiry Process (BPMN 2.0 Collaboration Diagram)

### 5.8.2 Interaction Model for One Feature

For a single feature the report uses a UML 2.5 sequence diagram (OMG, 2017), which shows the messages exchanged between participants, in time order, for one scenario. Figure {F:seq} models the most important MVP feature: routing a question Nuki cannot answer, from the student's question to closure through the status link. The alt fragment separates the answered path from the routed path, and the opt fragment shows the two-day reminder. The BPMN diagram gives managers and offices a view of the process; the sequence diagram gives the engineers the exact interactions they must build and test.

FIG[seq]: fig_uml_sequence.png | Route an Unanswered Question (UML 2.5 Sequence Diagram)

## 5.9 Operating-Model Recommendation

A hub-and-spoke operating model is the best initial fit. Product and service ownership should sit close to Student/Academic Services and programme operations, while scarce technology, security, data and AI capabilities remain shared. A fully embedded model would require stronger local product and engineering maturity than the evidence currently supports; a fully centralized digital factory would risk recreating business handoffs. The hybrid model therefore balances domain ownership with shared guardrails.

## 5.10 Portfolio Governance and Funding

Funding should follow evidence rather than guarantee a multi-year AI build. A stage/evidence mechanism is appropriate for the uncertain pilot: release enough capacity for baseline, prototype and evaluation; then continue, pivot, scale or stop based on agreed evidence. Portfolio review questions should cover strategic fit, student and staff value, learning, capability constraints, risk effectiveness and the next capacity decision.

Five guardrails are recommended: (1) financial capacity envelope and benefit owner; (2) architecture/data standards; (3) privacy, security and AI-risk controls; (4) student/staff service-quality and accessibility standards; and (5) delivery and escalation rules. AI investment should require evidence of incremental value over the non-AI alternative.

## 5.11 Capability and Sourcing Plan

TABLE[sourcing]: Capability and Sourcing Plan

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

# CHAPTER 6. DATA, AI, TECHNOLOGY ARCHITECTURE, AND DIGITAL TRUST



## 6.1 Data Requirements and Readiness

The minimum data model should capture only what is necessary to operate and evaluate the service: request ID, request category, programme or context, timestamps, assigned owner, status, resolution type, repeat contact, handoff count, duplicate-routing flag, student or staff feedback and handling or maintenance effort. Personal identifiers should be separated from aggregated analytics where possible. Identity data is used only for access verification in the MVP. Data quality rules should define mandatory fields, valid categories, closure conditions, duplicate detection and review responsibilities. Data ownership should be split between the service owner for operational data and Academic Affairs or programme content owners for authoritative guidance.

Readiness is currently low-to-partial because baseline event data is not consistently captured. The project should therefore treat analytics as a design requirement from the beginning rather than as a later dashboard exercise. This aligns with evidence that higher-education analytics requires robust data governance and architecture before more advanced predictive or AI use (Peck, 2023; Stojanov & Daniel, 2024).

## 6.2 AI Use Cases and Boundaries

The initial AI use cases are narrow: classify the enquiry topic, retrieve relevant approved content, write a clear answer from it, summarize the conversation for the routed email and suggest a staff reply draft. AI must not infer registration status, eligibility, grades, tuition liability or other authoritative decisions; such questions are routed. Each answer has a 1–5 rating, and a low rating opens a short ‘why?’ prompt. Sessions are logged and reviewed weekly: frequently asked questions become plain FAQ pages that students can read without calling the AI, which also reduces token cost, and poorly rated or unanswered questions enter a reviewed content-gap queue. Conversations are not automatically used to retrain the model; Maddie and Academic Affairs classify each gap, approve any content change and refresh the retrieval index through a controlled process.

## 6.3 Conceptual Architecture

The conceptual architecture has seven connected elements: (1) authenticated student and staff interface; (2) workflow and routing; (3) request database; (4) approved knowledge repository; (5) retrieval and optional AI classification or drafting service; (6) institutional email service; and (7) analytics, audit and monitoring. Identity and access, logging, security and privacy controls cut across all elements. The architecture supports request IDs, staff status updates, closure confirmation, duplicate-routing detection, reminder messages and an outage webhook. Direct academic-record transactions remain outside the first pilot.

Figure {F:comp} shows this architecture as a UML component diagram (OMG, 2017). After the Session 9 review, the reusable asset is described as a request database rather than as a request ID alone. The database holds each request ID with its routing, status history, ratings and closure, and it is what makes duplicate detection, reminders, KPIs and audit possible.

FIG[comp]: fig_uml_component.png | Conceptual Architecture (UML 2.5 Component Diagram)

## 6.4 Nonfunctional Requirements and Trust Controls

- Accuracy and routing: at least 80% of rated answers score 4–5; zero critical wrong guidance; at least 75% answered without an office; at least 80% of routed requests reach the right office first time (proposed thresholds).

- Traceability: every answer shows its source or owner office; every guide has an owner and review date.

- Privacy and security: minimum data, role-based access, defined retention and approved identity, logging and hosting before identifiable cases are stored.

- Accessibility: usable on common devices, in clear language, without requiring AI conversation.

- Resilience: on failure, a webhook alerts the team and students see a status page listing each office's email; failed emails are retried, reminders follow two days without status, and duplicates link to one request ID.

# CHAPTER 7. CHANGE, ADOPTION, TALENT, AND CULTURE

Adoption is a workflow change, not merely a communications campaign. Students must know when to use the standard route; staff must trust the content, accept clear ownership, use the request ID and update status or closure rather than recreating informal side channels. Academic Affairs must approve and maintain guidance. The three-week pilot with five students provides usability and workflow evidence, not a general prevalence estimate.

This chapter follows the Session 9 sequence. It assesses the change impact on each group, identifies the sources of resistance and the response to each, sets out a change-management plan on a recognised model, and closes with the adoption roadmap and its decision owners.

## 7.1 Change-Impact Assessment

Figure {F:grid} in Section 2.5 positions each group by influence and impact. Table {T:impact} adds each group's readiness and the specific change in behaviour it must make, with a measure and an exit criterion for each. Readiness is lowest where impact is highest. The content owner must take on a review calendar, and office staff must log status for routed requests, so these two groups receive the most support.

TABLE[impact]: Change-Impact Assessment

| **Stakeholder** | **Future behaviour** | **Readiness** | **Impact** | **Measure** | **Exit criterion** |
|----|----|----|----|----|----|
| Final-year students | Ask Nuki first; rate answers; use the tracked request | Medium | High | Weekly use; rating | At least 80% of answers rated 4–5 |
| Office staff | Reply in normal email; log status through one link | Low–medium | High | Status-link use; minutes per case | No rise in time per case |
| Head of Academic Affairs and content owner | Approve and update dated guides on a calendar | Low | High | On-time reviews | 100% of guides dated |
| VNUK IT team and privacy adviser | Approve sign-in list, data controls and hosting | Medium | Medium | Controls completed | Signed off before launch |
| VNUK Director / Dean | Decide at gates on evidence | Medium | Low–medium | Decisions recorded | Gate decision logged |
| Heads of next offices | Prepare guides and contacts before joining | Low (not yet engaged) | Low now | Readiness check | Passes the Gate 4 check |

## 7.2 Sources of Resistance and How They Will Be Overcome

Resistance is expected, and the team treats it as information about the design rather than as opposition to defeat. Kotter and Schlesinger (2008) identify four common sources of resistance: parochial self-interest, misunderstanding and lack of trust, different assessments of costs and benefits, and low tolerance for change. They also describe six approaches for dealing with it, ranging from education and participation to negotiation and, as a last resort, coercion. Table {T:resist} applies that framework to each group. The plan uses only education, participation, facilitation and negotiation. Manipulation and coercion are excluded because the pilot depends on voluntary use and on staff goodwill.

TABLE[resist]: Sources of Resistance and Responses

| **Group** | **Likely concern** | **Source of resistance** | **Approach** | **Concrete response (owner)** |
|----|----|----|----|----|
| Office staff | "This adds another inbox to my day." | Parochial self-interest: extra work, loss of control | Participation; facilitation and support | Staff keep their email and log status with one link; they co-design the routed email; workload check in week 2 (Maddie) |
| Head of Academic Affairs and content owner | "I have no time to review guides." | Different assessment of costs and benefits | Negotiation and agreement; facilitation | Guide template, review calendar and backup owner; FAQ pages cut repeat emails (Head of AA, Maddie) |
| VNUK IT team and privacy adviser | "Who sees student data? What if the AI is wrong?" | Misunderstanding and lack of trust | Education and communication; participation | Read-only sign-in; no grades or fees; controls checklist signed before launch; monitoring alerts (Zsombi) |
| VNUK Director / Dean | "Is this worth the effort?" | Different assessment of costs and benefits | Education and communication | Weekly evidence brief, break-even logic and a recorded week-3 decision (Maddie) |
| Final-year students | "Why not just email, like always?" | Low tolerance for change: habit | Education; participation; facilitation | Instant approved answer or one tracked request; onboarding; co-design sessions (Yuhan) |
| Heads of next offices | "Our questions are different." | Parochial self-interest | Participation; negotiation | Each office sets its own rules, contacts and response window on the shared core (Maddie) |

## 7.3 Change-Management Framework

The plan follows Kotter's (1995) eight-step model for organisational change, grouped in three phases: creating a climate for change, engaging and enabling the organisation, and implementing and sustaining the change. Figure {F:kotter} maps each step to a concrete Ask Nuki action and to its place in the timeline.

FIG[kotter]: fig_kotter.png | Change-Management Plan on Kotter's Eight Steps

Kotter's model works at the level of the organisation. At the level of the individual, adoption is tracked with the ADKAR model (Hiatt, 2006): Awareness, Desire, Knowledge, Ability and Reinforcement. Table {T:adkar} defines observable behaviour at each ADKAR stage for students and for staff, so the team measures adoption instead of assuming it. Diffusion research supports starting with a small group of willing users whose experience is visible to their peers (Rogers, 2003); the five pilot students and their office contacts play that role.

TABLE[adkar]: Adoption Stages (ADKAR) with Observable Behaviour and Evidence

| **ADKAR stage** | **Student behaviour** | **Staff behaviour** | **Evidence** | **Support** |
|----|----|----|----|----|
| Awareness | Knows Nuki exists and what it cannot answer | Knows routed requests arrive with an ID | Share of pilot group briefed | Change story; briefing |
| Desire | Chooses to try Nuki instead of reply-all | Willing to log status by link | First question asked; first test case closed | Co-design; "what stays the same" message |
| Knowledge | Knows how to ask, rate and track | Knows routing, closure and response-window rules | Onboarding completed; job aid used | Onboarding; 15-minute walkthrough; job aid |
| Ability | Asks clearly; gets an answer or routes once | Closes real cases within the window | Weekly use; status-link use; time per case | Office hours; champions; direct-department route |
| Reinforcement | Returns to Nuki instead of emailing | No side-channel duplicates | Repeat use after week 1; duplicate count | Weekly evidence brief; visible fixes; recognition |

## 7.4 Adoption Roadmap and Decision Owners

Figure {F:roadmap} shows the three-week pilot roadmap by stakeholder. Decision-makers have their own rows. The Director approves the pilot scope and budget at Gate 1. The Head of Academic Affairs and the IT team approve guidance and controls before launch, and the service owner records the week-3 decision. Students and office staff are the proof-of-concept testers, so their rows hold testing tasks with measurable outputs rather than training attendance. Every week the product team runs the same short loop: test, feedback, backlog, fix and retest. Table {T:adoptplan} gives the message, support, measure, risk and exit criterion for each phase.

FIG[roadmap]: fig_roadmap.png | Three-Week Pilot Adoption Roadmap with Decision Owners

TABLE[adoptplan]: Pilot Adoption Plan by Phase

| **Phase (owner)** | **Audience and message** | **Training and support** | **Measure** | **Main risk and response** | **Exit** |
|----|----|----|----|----|----|
| Prepare (Maddie) | Director, Head of AA, IT team: "help us set it up safely" | Guide template; controls checklist | Owners named; guides approved | No owner: escalate to the Director | Gate 1 passed |
| Week 1 (Yuhan) | Five students and office staff: "ask Nuki first; one link closes a case" | Onboarding; job aid; 15-minute staff walkthrough | Each student asks once; each office closes a test case | Students forget: reminder message | All five active |
| Week 2 (Tamas) | Students: real graduation-journey questions | Office hours; outage page; alerts | Ratings 4–5; right office first time | Wrong answer: pause the AI layer | No critical errors |
| Week 3 (Maddie) | Service owner and Director: evidence brief | Retrospective; fix list | The four week-3 numbers | Staff overload: narrow the topics | Decision recorded |

## 7.5 Talent, Training and Culture

Training should be role-specific: students need to understand the service boundary and feedback flow; Maddie needs the requirements and backlog workflow; Tamas and Zsombi need release, monitoring and data controls; Yuhan needs the test and feedback protocol; resolvers need routing and closure rules; content owners need approval and review procedures; and the pod needs analytics and AI-risk literacy. Reinforcement should use visible metrics, feedback and retrospective learning rather than compliance messaging alone.

Culture is the slowest layer to change and corresponds to Kotter's final step. The aim is that answering once, updating the guide and closing the request through the link become normal office practice. Nuki should also become part of student onboarding, and the agreed response window should be written into office procedure. These steps belong to Wave 3 and are measured by repeat use and by the absence of side-channel duplicates, not by announcements.

# CHAPTER 8. IMPLEMENTATION, SCALING, PERFORMANCE, AND GOVERNANCE

This chapter answers the Session 9 question of how the service would grow if the pilot succeeds. Earlier versions grouped two different moves under the word "scale". This version separates expanding within a department that is already live from scaling to new departments. Both moves use the same gates and the same measurement model.

## 8.1 Expand Versus Scale

Moore et al. (2015) distinguish three ways of scaling: scaling out (reaching more people and places), scaling up (changing institutional rules and policy) and scaling deep (changing culture and relationships). For Ask Nuki these become three concrete moves, shown in Figure {F:expand}:

- Expand (Wave 2) means growing within Academic Affairs, the department already live. The user base grows from the five pilot students to all final-year CSE students, then to final-year IBM and BMS students, and more topics on the graduation journey are added. The core and the department stay the same; volume and topic coverage grow. After Gate 2 the AI retrieval layer is tested against the non-AI service.

- Scale (Wave 3) means replicating the service to a new department. Each new office joins as a separate unit with its own guide owner, contacts, local rules and response window, and it reuses the core unchanged.

- Scale up and deep comes once at least two departments run on the core with sustained benefit. VNUK can then make Ask Nuki the official first route for academic questions in office procedures and student onboarding (scaling up). Answering once and updating the guide then becomes part of how offices work (scaling deep).

FIG[expand]: fig_expand_scale.png | Expand Versus Scale: What Grows in Each Wave

## 8.2 Unit of Scale: the Department

Following the lecturer's feedback, the unit of scale is a department (office), not a programme. A department owns a coherent set of student questions and has a mailbox and a head who can accept ownership. It is also where routing rules, response windows and guide approval sit. Programmes and cohorts are treated as user groups within the expand step rather than as separate units. The order in Table {T:depts} follows demand in the mailbox review, then each office's readiness. Typical questions for offices after Academic Affairs still need to be validated with the offices themselves.

TABLE[depts]: Department Scaling Sequence

| **Order** | **Department** | **Demand evidence** | **Typical questions** | **Local configuration** | **Main readiness condition** |
|----|----|----|----|----|----|
| 1 (pilot) | Academic Affairs | 11 of 23 requests | Credit limit, registration window, graduation application (BM.ĐT forms), VSTEP | Guide owner, form codes, cohort rules | Named content owner; guides approved |
| 2 | IT Support | 4 of 23 | Login, missing Canvas course, email access | Self-help steps; IT mailbox | Routing rule for access issues agreed |
| 3 | Student Affairs | 4 of 23 | Confirmation letters and student records (to validate) | Forms and documents; office hours | Guide owner; response window agreed |
| 4 | Finance | 2 of 23 | Tuition deadlines and payment methods | General rules only; personal balances routed | Privacy rule for personal financial data |
| 5 | Assessment Unit | Re-marking guides already drafted | Re-marking (phúc khảo), exam schedules | Deadlines and forms | Deadline calendar maintained |

## 8.3 Reusable Core and Local Configuration

Each new department is faster and safer to add because it reuses the core (Table {T:core}). The request database is the centre of that core: every request has one ID, a status history, ratings and a closure record, whichever office handles it. The test for any local change is whether it protects a real local rule or brings back avoidable complexity. Only the first is allowed.

TABLE[core]: Reusable Core and Local Configuration

| **Reusable core (same in every department)** | **Local configuration (set by each department)** |
|----|----|
| Portal pattern and read-only sign-in | Department contacts and mailbox |
| Knowledge schema: source, owner, review date | Local policies and rules |
| Request taxonomy and routing-rules engine | Topic list and routing rules for its questions |
| Request database: request ID, status history, ratings, closure, duplicate check | Response window and reminder timing |
| Email handoff and status-and-feedback link | Review calendar and backup owner |
| Event and KPI definitions; test sets | Office hours and champions |
| Privacy controls and governance routines | Programme and cohort rules where relevant |

## 8.4 Three-Wave Roadmap

Figure {F:waves} and Table {T:waves} set out the three waves. Exit from each wave depends on evidence, not on a date (DBB43005 teaching team, 2026a).

FIG[waves]: fig_waves.png | Three Waves over 18 Months with Stage Gates

TABLE[waves]: Three-Wave Roadmap

| **Wave** | **Scope** | **Data and technology** | **People and adoption** | **Exit evidence** |
|----|----|----|----|----|
| Wave 1: Prove (0–3 months) | Academic Affairs; five, then all, final-year CSE students; non-AI service first | Request database, approved knowledge base, analytics events | Named owners; co-design; students and staff as POC testers | Baseline complete; content maintainable; privacy approved; week-3 decision recorded |
| Wave 2: Expand (3–9 months) | Academic Affairs; all final-year students in CSE, IBM and BMS; more graduation-journey topics | Dashboard; AI retrieval tested against the non-AI service (Gate 2) | Wider staff use; one champion per programme | Measured student and staff improvement; stable routing; AI adds measurable value or is dropped |
| Wave 3: Scale (9–18 months) | Next departments one at a time: IT Support, Student Affairs, Finance, Assessment Unit | Reusable integrations; selective AI drafting | Department heads accept ownership; persistent product operating model | Each department passes Gate 4 and sustains its KPIs; cost per resolved request acceptable |

## 8.5 Readiness Check for a New Department

Before Gate 4, each department is checked against Table {T:ready}. The verdict is ready, conditional or not ready. A conditional verdict names a gap owner and a date, and the department joins only when every row is ready. This keeps scaling paced by readiness rather than by announcement.

TABLE[ready]: Readiness Check for a Department to Join (Gate 4)

| **Criterion** | **Evidence required** | **Confirmed by** |
|----|----|----|
| Ownership | Head of department accepts ownership; named guide owner and backup | Director / Dean |
| Content | The department's ten most frequent questions have approved, dated guides | Department guide owner |
| Workflow | Routing rules and response window agreed; staff walkthrough completed | Head of department; Maddie |
| Baseline | Two weeks of volume, first-reply time and handling time captured | Maddie; Zsombi |
| Controls | The office's data needs fit the existing identity and privacy controls | VNUK IT team and privacy adviser |
| Capacity | Staff time for status links and guide upkeep confirmed | Head of department |

## 8.6 Measurement Plan

Figure {F:vtree} sets out the value-driver tree. It splits net service value into the cash drivers from the break-even formula in Section 4.7.4 (eligible enquiries, self-service share, minutes saved and staff cost, minus guide upkeep and running cost) and two non-cash branches, student value and risk. Each leaf names the KPI that measures it and the lever owner. The tree also shows the economic reason for growth: the self-service share and minutes saved are set within Academic Affairs, while eligible enquiries rise only through expanding (Wave 2) and scaling (Wave 3).

FIG[vtree]: fig_value_tree.png | Value-Driver Tree for Ask Nuki

Measurement uses the DeLone and McLean (2003) information-systems success model. The model links system quality, information quality and service quality to use and user satisfaction, and through those to net benefits (Figure {F:delone}). It fits Ask Nuki because it measures the whole chain from a working service to a realised benefit. When a result is weak, the team can tell whether the cause is the system, the content, the service or adoption. Table {T:kpi} turns the model into a measurement plan: each KPI has a definition, a data source, a target for each wave, an owner and a review cadence. Wave 1 targets are proposed pilot thresholds. Targets for Waves 2 and 3 are proposals that will be reset from the measured baseline. Every number comes from request-database events, ratings, status links, monitoring logs or a two-week staff time sample, so measurement needs no manual reporting.

FIG[delone]: fig_delone.png | KPIs Mapped to the DeLone and McLean IS Success Model

TABLE[kpi]: Measurement Plan by Wave

| **KPI (dimension)** | **Definition** | **Source** | **Wave 1 target** | **Wave 2–3 target (proposed)** | **Owner and cadence** |
|----|----|----|----|----|----|
| Answer usefulness (information quality) | Share of rated answers scored 4 or 5 | Portal ratings | At least 80% | At least 85% | Head of AA and Maddie; weekly |
| Critical wrong guidance (information quality) | Answers implying eligibility, grades, finance or official decisions | QA review of logs | 0 | 0 | Head of AA; immediate |
| Guide currency (information quality) | Share of guides with source, owner and review date, and not expired | Knowledge base | 100% | 100% | Content owners; on publish and monthly |
| Correct first routing (service quality) | Routed requests reaching the right office first time | Request database | At least 80% | At least 90% | Service owner; weekly |
| Staff context rating (service quality) | Mean staff rating of routed-email context | Status link | At least 4 of 5 | At least 4 of 5 | Service owner; weekly |
| Adoption (use) | Weekly active students divided by eligible students; return after week 1 | Portal events | At least 3 of 5 students return | At least 40% of eligible students each month | Yuhan; weekly |
| Self-service rate (net benefit) | Share of questions answered without routing | Request database | At least 75% | At least 75% in each department | Maddie; weekly |
| Staff effort per request (net benefit) | Handling plus guide-upkeep minutes per resolved request | Staff time sample | No more than baseline | 20% below baseline | Service owner; weeks 2–3, then monthly |
| Repeat contact (net benefit) | Same student, same issue, within 7 days | Request database and email audit | No more than baseline | Below baseline | Maddie; monthly |
| Duplicate routing (system quality) | Open duplicates for the same issue | Request database | 0 | 0 | Tamas; daily |
| Availability (system quality) | Uptime in service hours; time for an outage alert to reach the team | Monitoring | At least 99%; under 5 minutes | At least 99.5% | Zsombi; daily |
| Cost per resolved request (net benefit) | Monthly running and content cost divided by resolved requests | Finance and request database | Recorded | Falls as volume grows; break-even near 375 a month | Director (sponsor); quarterly |

## 8.7 Governance, Stage Gates and Decision Logic

Governance focuses on outcomes, capacity and risk rather than Sprint tasks. Gate 1 opens the pilot once owner, baseline, content, identity and privacy are ready. Gate 2 allows an AI test only after the non-AI service works. Gate 3 approves expansion once both user groups benefit and routing is accurate. Gate 4 is applied to each new department through the readiness check in Table {T:ready}. The AI layer is paused when ratings fall below 70% in a week, unsupported answers or duplicates recur, staff rate context below 3 of 5, or access controls fail; guides and email routing continue meanwhile. The MVP stops if fewer than three of five students keep using it, no office owns the guidance, critical errors stay unresolved or two corrective cycles show no improvement.

Figure {F:decision} shows the week-3 decision logic. Ownership and safety are checked before performance targets, and the same logic is reused at Gates 2–4. The Director approves Gates 1, 3 and 4; the service owner allows the AI test and records the week-3 decision (Table {T:raci}).

FIG[decision]: fig_decision.png | Week-3 Decision Logic

## 8.8 Final Risk Register

TABLE[risk]: Final Risk Register

| **Risk** | **Likelihood** | **Impact** | **Owner** | **Treatment** |
|----|----|----|----|----|
| Outdated / incorrect academic guidance | Medium | High | Content owner | Versioning, review date, refusal/escalation |
| Staff capacity insufficient | Medium | High | Domain owner | Baseline workload, protected capacity, limit scope |
| Low student adoption | Medium | Medium | Product/change lead | Co-design, usability, channel transition plan |
| AI adds no value | Medium | Medium | Product owner | A/B comparison with non-AI service; stop AI layer |
| Personal-data misuse | Low–Medium | High | Privacy/data owner | Data minimization, access, assessment, vendor controls |
| Integration delays | Medium | Medium | IT lead | Pilot without live integration; API only after evidence |
| Scope creep across programmes/services | High | Medium | Product owner | One product area; explicit backlog boundary and stage gates |
| Expansion overloads Academic Affairs | Medium | High | Service owner | Expand cohort by cohort; monitor staff effort weekly; pause expansion if effort rises |
| Next department not ready or declines ownership | Medium | Medium | Director / Dean | Readiness check; the department joins only when ready; continue with live departments |

# CHAPTER 9. CRITICAL EVALUATION AND LESSONS

The proposal changed materially through critique. First, it no longer treats students as the only users: staff can gain or lose from the same product, so both are measured, including hidden upkeep work. Second, it moved away from technology-first reasoning. Isolated technology does not amount to transformation (Fernández et al., 2023), so approved knowledge, ownership, workflow and measurement now come before AI, and the non-AI service is a real alternative rather than a placeholder.

Third, the business case is deliberately modest. The capacity model supports sensitivity analysis but cannot prove a return without measured demand, effort and cost, and student time is not converted into cash without a defensible method. Fourth, the Session 9 review exposed weaknesses that were analytical as well as presentational: a free-form workflow (now BPMN and UML), stakeholders without named decision-makers (now an influence–impact grid and a RACI with sponsor, service owner, IT team and testers), and a loose idea of scale (now expanding within a department, then scaling department by department).

The main limitation remains evidence quality. Student data is small and partly historical, staff workload data is not systematic and IBM evidence is missing, so transferability is a question for the pilot, not an assumption. The legal and technical sections name relevant controls but do not replace VNUK's own legal, security or procurement review.

# CHAPTER 10. CONCLUSION AND DECISION REQUEST

Student Support and Academic Navigation remains the recommended domain, with a narrower and more defensible scope: a bounded, dual-user pilot of academic enquiry guidance and routing. The decision requested is approval of Gate 1, not university-wide AI deployment.

Conditions to proceed are: (1) confirm the Director or Dean as sponsor, the Head of Academic Affairs as service owner and the VNUK IT team as controls owner; (2) collect comparable student and staff baselines; (3) approve the initial guides and content owners; (4) confirm privacy and security arrangements; and (5) protect staff time for reviews. The service continues if student effort, resolution, routing and staff workload all improve with acceptable risk; it is adapted if value appears but workflow or content needs correction; and the AI layer is paused or stopped if critical errors occur, guides cannot be maintained or the simpler service performs as well. If the pilot succeeds, the service expands within Academic Affairs to all final-year students and then scales one department at a time, each step measured with the same model and decided at a gate.

# References

Ackermann, F., & Eden, C. (2011). Strategic management of stakeholders: Theory and practice. Long Range Planning, 44(3), 179–196. https://doi.org/10.1016/j.lrp.2010.08.001

Bourne, L., & Walker, D. H. T. (2005). Visualising and mapping stakeholder influence. Management Decision, 43(5), 649–660. https://doi.org/10.1108/00251740510597699

Chugh, R., Turnbull, D., Cowling, M. A., Vanderburg, R., & Vanderburg, M. A. (2023). Implementing educational technology in higher education institutions: A review of technologies, stakeholder perceptions, frameworks and metrics. Education and Information Technologies, 28, 16403–16429. https://doi.org/10.1007/s10639-023-11846-x

Cohn, M. (2004). User stories applied: For agile software development. Addison-Wesley.

Customer Experience project teams. (2026a). Customer Experience module research on CSE student journeys \[Unpublished interview records and project analyses\]. VNUK Institute for Research and Executive Education.

Customer Experience project teams. (2026b). Customer Experience module research on BMS student experience \[Unpublished survey results and project report\]. VNUK Institute for Research and Executive Education.

DBB43005 teaching team. (2026a). Session 4: Digital strategy and transformation roadmap \[Course slides\]. VNUK Institute for Research and Executive Education.

DBB43005 teaching team. (2026b). Session 6: Cross-functional teams, operating models, and digital capabilities \[Course slides\]. VNUK Institute for Research and Executive Education.

DeLone, W. H., & McLean, E. R. (2003). The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19(4), 9–30. https://doi.org/10.1080/07421222.2003.11045748

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). Fundamentals of business process management (2nd ed.). Springer. https://doi.org/10.1007/978-3-662-56509-4

EDUCAUSE. (2024). 2024 students and technology survey. https://www.educause.edu/research-and-publications/research/analytics-services/surveys/2024/educause-student-survey

Fernández, A., Gómez, B., Binjaku, K., & Meçe, E. K. (2023). Digital transformation initiatives in higher education institutions: A multivocal literature review. Education and Information Technologies, 28, 12351–12382. https://doi.org/10.1007/s10639-022-11544-0

Government of Vietnam. (2025). Decree No. 356/2025/ND-CP detailing a number of articles and measures for implementation of the Law on Personal Data Protection.

Group 1. (2026). Follow-up validation of BMS and CSE issue status \[Unpublished team communication with departmental contacts\]. VNUK Institute for Research and Executive Education.

Hiatt, J. M. (2006). ADKAR: A model for change in business, government and our community. Prosci Learning Center Publications.

ISO/IEC. (2013). Information technology — Object Management Group Business Process Model and Notation (ISO/IEC 19510:2013). International Organization for Standardization.

Kotter, J. P. (1995). Leading change: Why transformation efforts fail. Harvard Business Review, 73(2), 59–67.

Kotter, J. P., & Schlesinger, L. A. (2008). Choosing strategies for change. Harvard Business Review, 86(7/8), 130–139.

Moore, M.-L., Riddell, D., & Vocisano, D. (2015). Scaling out, scaling up, scaling deep: Strategies of non-profits in advancing systemic social innovation. Journal of Corporate Citizenship, 58, 67–84.

National Assembly of Vietnam. (2025). Law No. 91/2025/QH15 on Personal Data Protection.

National Institute of Standards and Technology. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0) (NIST AI 100-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

National Institute of Standards and Technology. (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1

Object Management Group. (2011). Business Process Model and Notation (BPMN), version 2.0 (formal/2011-01-03). https://www.omg.org/spec/BPMN/2.0/

Object Management Group. (2017). OMG Unified Modeling Language (OMG UML), version 2.5.1 (formal/17-12-05). https://www.omg.org/spec/UML/2.5.1/

Peck, E. (2023). Student analytics: A core specification for engagement and wellbeing analytics. Jisc. https://www.jisc.ac.uk/reports/student-analytics-a-core-specification-for-engagement-and-wellbeing-analytics

Project Management Institute. (2017). A guide to the project management body of knowledge (PMBOK guide) (6th ed.). Project Management Institute.

Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.

Schwaber, K., & Sutherland, J. (2020). The Scrum Guide: The definitive guide to Scrum: The rules of the game. https://scrumguides.org/scrum-guide.html

Stojanov, A., & Daniel, B. K. (2024). A decade of research into the application of big data and analytics in higher education: A systematic review of the literature. Education and Information Technologies, 29, 5807–5831. https://doi.org/10.1007/s10639-023-12033-8

Team Topologies. (n.d.). Key concepts and practices for applying a Team Topologies approach to team-of-teams org design. https://teamtopologies.com/key-concepts

UNESCO. (2023). Guidance for generative AI in education and research. https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

University of Danang. (2025). Annual Report UD–2024: Highlights and development orientation. https://vnuk.udn.vn/en/the-university-of-danang-introduces-the-annual-report-ud-2024/

VNUK. (n.d.-a). Vision–mission–core values. https://vnuk.udn.vn/en/vision-mission-corevalues/

VNUK. (n.d.-b). Introduction. https://vnuk.udn.vn/en/about-us/

Ward, J., & Daniel, E. (2012). Benefits management: How to increase the business value of your IT projects (2nd ed.). Wiley.

# Appendix A. Dual-User Baseline Measurement Dictionary

TABLE[dict]: Dual-User Baseline Measurement Dictionary

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

# Appendix C. Estimated Baseline Figures

The baseline figures in Section 3.3 are working estimates, not measured VNUK data. They will be replaced with measured values during Wave 1.

Eligible enquiries (about 120 per month; about 60 per week at peak): scaled from the report’s illustrative volume of 500 enquiries per month across VNUK, assuming final-year CSE students generate about a quarter of academic enquiries, with peaks taken from the registration and graduation windows seen in the mailbox review.

First reply (median one working day; about 20% over three working days): Academic Affairs replied the same or the next working day in every thread reviewed; the four-to-five-day advising delay reported in interviews is used as the long tail.

Multiple channels (about 30%): based on interview accounts of students contacting lecturers, friends and offices about the same issue, and on the 35% reply-all share in the mailbox sample.

Wrong office first (about 15%): based on login and access questions first sent to Academic Affairs or Finance and then forwarded to IT in the mailbox sample.

Staff handling time (8 minutes per routed email): the report’s illustrative scenario value.

Mailbox sample (23 requests; 8 reply-all; 2 refused): counted directly from one team member’s VNUK mailbox, 2022–2026, with other students anonymised and registration-portal overload reports excluded.

# Appendix D. Session 9 Feedback Response Log

TABLE[feedback]: Session 9 Lecturer Feedback and Where It Is Addressed

| **Slide** | **Lecturer comment (whiteboard)** | **Change made** | **Where in this report** |
|----|----|----|----|
| 4–5 | Use a standard template for the workflow diagram; a UML sequence diagram is acceptable for a small feature | Full flow redrawn as BPMN 2.0 (to-be and as-is); routing feature as a UML sequence diagram; architecture as a UML component diagram | Sections 3.4, 5.8 and 6.3 |
| 6 | Assess impact on an influence–impact grid; carry these groups into the RACI and the roadmap | Influence–impact grid with named decision-makers; groups feed the RACI and the roadmap | Sections 2.5 and 7.1 |
| 7 | Write user stories for different departments ("As a …, I find [problem] → solution"); mention sources of resistance | Problem-first user stories for six departments; resistance analysed with Kotter and Schlesinger (2008) | Sections 5.3 and 7.2 |
| 7 | Add a change-management slide based on a reference | Change plan on Kotter's eight steps; individual adoption on ADKAR | Section 7.3 |
| 9 | Session 9 is adoption: the POC testers are students and staff; add decision-making tasks to the RACI | RACI adds pilot students, office staff and Director columns plus decision rows | Section 5.7 |
| 10 | Add the stakeholders who decide to implement (Dean, heads, IT team) | Roadmap rows for the Director, Head of Academic Affairs and IT team, with gates | Section 7.4 |
| 12 | Change "programme" to "department" as the unit of scale | Department is the unit of scale, with a sequence of five offices | Section 8.2 |
| 13 | Replace "request ID" with "request database" | Request database named as the core asset | Sections 6.3 and 8.3 |
| 14 | Clarify "expand" versus "scale"; focus more on the scaling and measurement plan | Expand and scale defined (Moore et al., 2015); readiness check; DeLone and McLean measurement plan with targets by wave | Sections 8.1–8.6 |
