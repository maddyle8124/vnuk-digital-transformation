"""Build report_v4.md from the v3 body plus the Session 9 feedback changes.

Markers used by build_docx.py:
  TABLE[key]: caption          -> numbered table caption (next pipe table)
  FIG[key]: file | caption     -> numbered figure caption + image
  {T:key} / {F:key}            -> cross-reference numbers
"""
import re

src = open("body_v3.md", encoding="utf-8").read()
# fix the unstyled chapter 6 heading
src = src.replace("**CHAPTER 6. DATA, AI, TECHNOLOGY ARCHITECTURE, AND DIGITAL TRUST**", "# CHAPTER 6. DATA, AI, TECHNOLOGY ARCHITECTURE, AND DIGITAL TRUST")

# ---- split into sections keyed by heading text
parts = re.split(r"(?m)^(#{1,3} .*)$", src)
order, sec = [], {}
pre = parts[0]
for i in range(1, len(parts), 2):
    h = parts[i].strip()
    order.append(h)
    sec[h] = parts[i + 1].strip("\n")


def key(prefix):
    m = [h for h in order if h.lstrip("# ").startswith(prefix)]
    assert len(m) == 1, (prefix, m)
    return m[0]


def rep(prefix, old, new, count=1):
    k = key(prefix)
    assert old in sec[k], (prefix, old[:60])
    sec[k] = sec[k].replace(old, new, count)


def setsec(prefix, body):
    sec[key(prefix)] = body.strip("\n")


def append(prefix, body):
    k = key(prefix)
    sec[k] = sec[k] + "\n\n" + body.strip("\n")


def caption_before(prefix, header_start, tkey, caption):
    k = key(prefix)
    i = sec[k].index(header_start)
    sec[k] = sec[k][:i] + f"TABLE[{tkey}]: {caption}\n\n" + sec[k][i:]


# =====================================================================  CHAPTER 1
append("CHAPTER 1.", """
This version (v4) responds to the Session 9 review. The service flow is now drawn in standard notations: BPMN 2.0 for the end-to-end process and UML 2.5 for one feature and for the architecture. A stakeholder influence–impact grid names the people who decide whether to implement the service, and the RACI gives the pilot students and office staff explicit testing tasks. A change-management plan built on Kotter's eight steps now sits in Chapter 7. Chapter 8 now has a scaling and measurement plan that separates expanding within a department from scaling to new departments. Appendix D lists each lecturer comment and where it is addressed.
""")

# =====================================================================  2.5 Stakeholder map
setsec("2.5 ", """
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
""")

# =====================================================================  3.2 evidence chart
append("3.2 ", """
A second, more recent source is one team member's VNUK mailbox for 2022–2026. It holds 23 academic requests: 12 are the member's own and 11 come from other students, who are anonymised. Figure {F:requests} shows where they went; almost half went to Academic Affairs. Eight were sent by reply-all to a whole cohort mailing list, so many students saw each question and no office owned it. Two were refused because of rules the student learned only by asking: the 23-credit limit and the registration window. A check of vnuk.udn.vn on 11 November 2026 found no FAQ or help page. These counts show a routing pattern; they are not prevalence estimates.

FIG[requests]: fig_requests.png | Where 23 Real Academic Requests Went
""")

# =====================================================================  3.4 as-is BPMN
rep("3.4 ", "so each cause remains a testable hypothesis rather than a conclusion.",
    """so each cause remains a testable hypothesis rather than a conclusion.

Figure {F:asis} models this current journey in BPMN 2.0, the international standard notation for business processes (Object Management Group [OMG], 2011; ISO/IEC, 2013). Using a standard notation places the pain points on a model that others can check, rather than on a free-form sketch. Two pools show the participants. A parallel gateway shows students trying several channels at once, and a loop shows repeat contact when no clear answer arrives.

FIG[asis]: fig_bpmn_asis.png | As-Is Academic Enquiry Process (BPMN 2.0)""")

# =====================================================================  3.6 chart
rep("3.6 ", "The selection is therefore conditional on staff capacity, approved content and ownership.",
    """The selection is therefore conditional on staff capacity, approved content and ownership.

FIG[priority]: fig_priority.png | Weighted Prioritisation of Candidate Domains""")

# =====================================================================  4.4 BDN
append("4.4 ", """
Figure {F:bdn} expresses the same logic as a benefits dependency network (Ward & Daniel, 2012). It shows that the benefits depend on enabling changes and business changes, not on the technology alone. The enabling changes are Academic Affairs approving dated guides, offices agreeing routing rules and a response window, and students and staff being onboarded. The business changes are students asking in one place first, offices answering routed requests with one ID, and a weekly review that turns frequent questions into FAQ pages. Each benefit has an owner in the measurement plan (Table {T:kpi}).

FIG[bdn]: fig_bdn.png | Benefits Dependency Network for Ask Nuki
""")

# =====================================================================  4.7.4 break-even
append("4.7.4", """
FIG[breakeven]: fig_breakeven.png | Illustrative Break-Even Analysis

Figure {F:breakeven} also shows why growth matters. The Wave 1 working baseline of about 120 eligible enquiries a month is well below break-even, so the pilot is justified as learning rather than as saving. The economic case depends on expanding to more students and scaling to more departments under the conditions in Chapter 8.
""")

# =====================================================================  captions for kept tables
caption_before("3.3 ", "| **Dimension**", "baseline", "Dual-User Baseline Framework")
caption_before("3.5 ", "| **Candidate**", "cand", "Candidate Domains and Capability Assessment")
caption_before("4.2 ", "| **User / need**", "needs", "User and Business Needs")
caption_before("4.3 ", "| Objective", "obj", "Objectives and Measurement")
caption_before("4.5 ", "| **Initiative**", "portfolio", "Coherent Solution Portfolio")
caption_before("4.7.5", "| **Risk**", "riskcase", "Risk Case")
caption_before("5.3 ", "| **User story**", "stories", "Core User Stories and Acceptance Criteria")
caption_before("5.4 ", "| **Rank**", "backlog", "Ordered Product Backlog")
caption_before("5.6 ", "| Pod role", "pod", "Agile Pod Roles")
caption_before("5.11 ", "| **Capability**", "sourcing", "Capability and Sourcing Plan")
caption_before("Appendix A", "| **Metric**", "dict", "Dual-User Baseline Measurement Dictionary")

# =====================================================================  5.3 department user stories
append("5.3 ", """
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
""")

# =====================================================================  5.6 pod table rows
rep("5.6 ", "| Academic Affairs content owner | Approve authoritative guidance and update it when policies change | Institutional role; named owner required before pilot |",
    "| Head of Academic Affairs (service owner) and content owner | Approve authoritative guidance and update it when policies change; record the week-3 decision | Institutional role; named owner required before pilot |")
rep("5.6 ", "| Student pilot panel | Complete representative tasks and report usefulness, effort and unmet needs | Five students across the three-week pilot |",
    "| Pilot students (proof-of-concept testers) | Use Nuki for real graduation-journey questions; rate answers; report effort and unmet needs | Five final-year CSE students across the three-week pilot |\n| Office staff (proof-of-concept testers) | Answer routed requests in normal email; log status and rate context through the link | Staff in Academic Affairs and related offices, weeks 1–3 |\n| VNUK Director / Dean (sponsor) | Approve pilot scope and budget (Gate 1) and any expansion or scaling (Gates 3–4) | Decisions at gates, informed by a weekly evidence brief |")

# =====================================================================  5.7 RACI
setsec("5.7 ", """
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
""")

# =====================================================================  5.8 notation + diagrams
append("5.8 ", """
### 5.8.1 Modelling Notation for the Full Service Flow

The free-form workflow sketch used in the Session 9 presentation has been replaced by standard notations, each chosen for its level of detail. For the full, cross-department service the report uses a BPMN 2.0 collaboration diagram (OMG, 2011). BPMN is the international standard for business-process models (ISO/IEC, 2013) and is designed for processes that cross organisational boundaries. Each participant is a pool, work inside a pool is joined by sequence flows, and messages between participants are drawn as separate message flows (Dumas et al., 2018). This suits Ask Nuki because the service is defined by handoffs between students, the portal, offices and content owners, not by the software alone. Figure {F:tobe} shows the to-be process; Figure {F:asis} in Section 3.4 shows the current process for comparison.

FIG[tobe]: fig_bpmn_tobe.png | To-Be Academic Enquiry Process (BPMN 2.0 Collaboration Diagram)

### 5.8.2 Interaction Model for One Feature

For a single feature the report uses a UML 2.5 sequence diagram (OMG, 2017), which shows the messages exchanged between participants, in time order, for one scenario. Figure {F:seq} models the most important MVP feature: routing a question Nuki cannot answer, from the student's question to closure through the status link. The alt fragment separates the answered path from the routed path, and the opt fragment shows the two-day reminder. The BPMN diagram gives managers and offices a view of the process; the sequence diagram gives the engineers the exact interactions they must build and test.

FIG[seq]: fig_uml_sequence.png | Route an Unanswered Question (UML 2.5 Sequence Diagram)
""")

# =====================================================================  6.3 component
rep("6.3 ", "(3) request and status store;", "(3) request database;")
append("6.3 ", """
Figure {F:comp} shows this architecture as a UML component diagram (OMG, 2017). After the Session 9 review, the reusable asset is described as a request database rather than as a request ID alone. The database holds each request ID with its routing, status history, ratings and closure, and it is what makes duplicate detection, reminders, KPIs and audit possible.

FIG[comp]: fig_uml_component.png | Conceptual Architecture (UML 2.5 Component Diagram)
""")

# =====================================================================  CHAPTER 7
k7 = key("CHAPTER 7.")
first7 = sec[k7].split("\n\n")[0]
training = [p for p in sec[k7].split("\n\n") if p.startswith("Training should be role-specific")][0]
sec[k7] = first7 + """

This chapter follows the Session 9 sequence. It assesses the change impact on each group, identifies the sources of resistance and the response to each, sets out a change-management plan on a recognised model, and closes with the adoption roadmap and its decision owners."""
new7 = {
"7.1 Change-Impact Assessment": """
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
""",
"7.2 Sources of Resistance and How They Will Be Overcome": """
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
""",
"7.3 Change-Management Framework": """
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
""",
"7.4 Adoption Roadmap and Decision Owners": """
Figure {F:roadmap} shows the three-week pilot roadmap by stakeholder. Decision-makers have their own rows. The Director approves the pilot scope and budget at Gate 1. The Head of Academic Affairs and the IT team approve guidance and controls before launch, and the service owner records the week-3 decision. Students and office staff are the proof-of-concept testers, so their rows hold testing tasks with measurable outputs rather than training attendance. Every week the product team runs the same short loop: test, feedback, backlog, fix and retest. Table {T:adoptplan} gives the message, support, measure, risk and exit criterion for each phase.

FIG[roadmap]: fig_roadmap.png | Three-Week Pilot Adoption Roadmap with Decision Owners

TABLE[adoptplan]: Pilot Adoption Plan by Phase

| **Phase (owner)** | **Audience and message** | **Training and support** | **Measure** | **Main risk and response** | **Exit** |
|----|----|----|----|----|----|
| Prepare (Maddie) | Director, Head of AA, IT team: "help us set it up safely" | Guide template; controls checklist | Owners named; guides approved | No owner: escalate to the Director | Gate 1 passed |
| Week 1 (Yuhan) | Five students and office staff: "ask Nuki first; one link closes a case" | Onboarding; job aid; 15-minute staff walkthrough | Each student asks once; each office closes a test case | Students forget: reminder message | All five active |
| Week 2 (Tamas) | Students: real graduation-journey questions | Office hours; outage page; alerts | Ratings 4–5; right office first time | Wrong answer: pause the AI layer | No critical errors |
| Week 3 (Maddie) | Service owner and Director: evidence brief | Retrospective; fix list | The four week-3 numbers | Staff overload: narrow the topics | Decision recorded |
""",
"7.5 Talent, Training and Culture": training + """

Culture is the slowest layer to change and corresponds to Kotter's final step. The aim is that answering once, updating the guide and closing the request through the link become normal office practice. Nuki should also become part of student onboarding, and the agreed response window should be written into office procedure. These steps belong to Wave 3 and are measured by repeat use and by the absence of side-channel duplicates, not by announcements.
""",
}

# =====================================================================  CHAPTER 8
k8 = key("CHAPTER 8.")
sec[k8] = """This chapter answers the Session 9 question of how the service would grow if the pilot succeeds. Earlier versions grouped two different moves under the word "scale". This version separates expanding within a department that is already live from scaling to new departments. Both moves use the same gates and the same measurement model."""
gov_old = sec[key("8.3 ")]
risk_old = sec[key("8.4 ")]
gov_new = gov_old.replace("Stage Gate 4 approves broader scale only after unit economics and repeatable capabilities are evidenced.",
                          "Stage Gate 4 is applied to each new department using the readiness check in Table {T:ready}, and approves it only when unit economics and repeatable capabilities are evidenced.")
risk_new = risk_old.replace("| Scope creep across programmes/services | High | Medium | Product owner | One product area; explicit backlog boundary and stage gates |",
                            "| Scope creep across programmes/services | High | Medium | Product owner | One product area; explicit backlog boundary and stage gates |\n| Expansion overloads Academic Affairs | Medium | High | Service owner | Expand cohort by cohort; monitor staff effort weekly; pause expansion if effort rises |\n| Next department not ready or declines ownership | Medium | Medium | Director / Dean | Readiness check; the department joins only when ready; continue with live departments |")
assert risk_new != risk_old
risk_new = risk_new.replace("| **Risk** | **Likelihood**", "TABLE[risk]: Final Risk Register\n\n| **Risk** | **Likelihood**", 1)

new8 = {
"8.1 Expand Versus Scale": """
Moore et al. (2015) distinguish three ways of scaling: scaling out (reaching more people and places), scaling up (changing institutional rules and policy) and scaling deep (changing culture and relationships). For Ask Nuki these become three concrete moves, shown in Figure {F:expand}:

- Expand (Wave 2) means growing within Academic Affairs, the department already live. The user base grows from the five pilot students to all final-year CSE students, then to final-year IBM and BMS students, and more topics on the graduation journey are added. The core and the department stay the same; volume and topic coverage grow. After Gate 2 the AI retrieval layer is tested against the non-AI service.

- Scale (Wave 3) means replicating the service to a new department. Each new office joins as a separate unit with its own guide owner, contacts, local rules and response window, and it reuses the core unchanged.

- Scale up and deep comes once at least two departments run on the core with sustained benefit. VNUK can then make Ask Nuki the official first route for academic questions in office procedures and student onboarding (scaling up). Answering once and updating the guide then becomes part of how offices work (scaling deep).

FIG[expand]: fig_expand_scale.png | Expand Versus Scale: What Grows in Each Wave
""",
"8.2 Unit of Scale: the Department": """
Following the lecturer's feedback, the unit of scale is a department (office), not a programme. A department owns a coherent set of student questions and has a mailbox and a head who can accept ownership. It is also where routing rules, response windows and guide approval sit. Programmes and cohorts are treated as user groups within the expand step rather than as separate units. The order in Table {T:depts} follows demand in the mailbox review, then each office's readiness. Typical questions for offices after Academic Affairs still need to be validated with the offices themselves.

TABLE[depts]: Department Scaling Sequence

| **Order** | **Department** | **Demand evidence** | **Typical questions** | **Local configuration** | **Main readiness condition** |
|----|----|----|----|----|----|
| 1 (pilot) | Academic Affairs | 11 of 23 requests | Credit limit, registration window, graduation application (BM.ĐT forms), VSTEP | Guide owner, form codes, cohort rules | Named content owner; guides approved |
| 2 | IT Support | 4 of 23 | Login, missing Canvas course, email access | Self-help steps; IT mailbox | Routing rule for access issues agreed |
| 3 | Student Affairs | 4 of 23 | Confirmation letters and student records (to validate) | Forms and documents; office hours | Guide owner; response window agreed |
| 4 | Finance | 2 of 23 | Tuition deadlines and payment methods | General rules only; personal balances routed | Privacy rule for personal financial data |
| 5 | Assessment Unit | Re-marking guides already drafted | Re-marking (phúc khảo), exam schedules | Deadlines and forms | Deadline calendar maintained |
""",
"8.3 Reusable Core and Local Configuration": """
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
""",
"8.4 Three-Wave Roadmap": """
Figure {F:waves} and Table {T:waves} set out the three waves. Exit from each wave depends on evidence, not on a date.

FIG[waves]: fig_waves.png | Three Waves over 18 Months with Stage Gates

TABLE[waves]: Three-Wave Roadmap

| **Wave** | **Scope** | **Data and technology** | **People and adoption** | **Exit evidence** |
|----|----|----|----|----|
| Wave 1: Prove (0–3 months) | Academic Affairs; five, then all, final-year CSE students; non-AI service first | Request database, approved knowledge base, analytics events | Named owners; co-design; students and staff as POC testers | Baseline complete; content maintainable; privacy approved; week-3 decision recorded |
| Wave 2: Expand (3–9 months) | Academic Affairs; all final-year students in CSE, IBM and BMS; more graduation-journey topics | Dashboard; AI retrieval tested against the non-AI service (Gate 2) | Wider staff use; one champion per programme | Measured student and staff improvement; stable routing; AI adds measurable value or is dropped |
| Wave 3: Scale (9–18 months) | Next departments one at a time: IT Support, Student Affairs, Finance, Assessment Unit | Reusable integrations; selective AI drafting | Department heads accept ownership; persistent product operating model | Each department passes Gate 4 and sustains its KPIs; cost per resolved request acceptable |
""",
"8.5 Readiness Check for a New Department": """
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
""",
"8.6 Measurement Plan": """
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
""",
"8.7 Governance, Stage Gates and Decision Logic": gov_new + """

Figure {F:decision} shows the decision logic for the end of the three-week pilot. Ownership and safety are checked before performance targets, so a missing owner or a critical wrong answer is decided before ratings and routing are considered. The same logic, with wave-specific thresholds, is reused at Gates 2–4. Gate owners follow the RACI in Table {T:raci}. The Director approves Gates 1, 3 and 4; the service owner allows the AI test at Gate 2 and records the week-3 decision.

FIG[decision]: fig_decision.png | Week-3 Decision Logic
""",
"8.8 Final Risk Register": risk_new,
}

# =====================================================================  CHAPTER 9 & 10
k9 = key("CHAPTER 9.")
s9 = sec[k9]
s9 = s9.replace("Third, the project has moved further away from technology-first reasoning.", "The project has also moved further away from technology-first reasoning.")
s9 = s9.replace("Fourth, the business case is intentionally modest.", "The business case is also intentionally modest.")
s9 += """

Finally, the Session 9 review exposed three presentation-level weaknesses that were also analytical weaknesses. First, the workflow had been drawn free-form, which made it hard to check; it is now modelled in BPMN 2.0 and UML. Second, the stakeholder analysis described groups but not the people who decide whether to implement. The influence–impact grid and the revised RACI now name the sponsor, the service owner and the IT team, and they give the proof-of-concept testers explicit tasks. Third, "scale" had been used loosely. The report now separates expanding within a department from scaling to new departments, uses the department as the unit of scale, and attaches a readiness check and a measurement plan to each move."""
sec[k9] = s9

rep("CHAPTER 10.", "and (6) allocate protected staff review capacity.",
    "(6) allocate protected staff review capacity; and (7) confirm the decision-makers named in the RACI: the Director or Dean as sponsor, the Head of Academic Affairs as service owner and the VNUK IT team as controls owner.")
append("CHAPTER 10.", """
If the pilot succeeds, growth follows Chapter 8. The service first expands within Academic Affairs to all final-year students. It then scales one department at a time, each after passing the readiness check, and every step is measured with the same model and decided at a gate.
""")

# =====================================================================  references
refs_new = [
    "Ackermann, F., & Eden, C. (2011). Strategic management of stakeholders: Theory and practice. Long Range Planning, 44(3), 179–196. https://doi.org/10.1016/j.lrp.2010.08.001",
    "Bourne, L., & Walker, D. H. T. (2005). Visualising and mapping stakeholder influence. Management Decision, 43(5), 649–660. https://doi.org/10.1108/00251740510597699",
    "Cohn, M. (2004). User stories applied: For agile software development. Addison-Wesley.",
    "DeLone, W. H., & McLean, E. R. (2003). The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19(4), 9–30. https://doi.org/10.1080/07421222.2003.11045748",
    "Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). Fundamentals of business process management (2nd ed.). Springer. https://doi.org/10.1007/978-3-662-56509-4",
    "Hiatt, J. M. (2006). ADKAR: A model for change in business, government and our community. Prosci Learning Center Publications.",
    "ISO/IEC. (2013). Information technology — Object Management Group Business Process Model and Notation (ISO/IEC 19510:2013). International Organization for Standardization.",
    "Kotter, J. P. (1995). Leading change: Why transformation efforts fail. Harvard Business Review, 73(2), 59–67.",
    "Kotter, J. P., & Schlesinger, L. A. (2008). Choosing strategies for change. Harvard Business Review, 86(7/8), 130–139.",
    "Moore, M.-L., Riddell, D., & Vocisano, D. (2015). Scaling out, scaling up, scaling deep: Strategies of non-profits in advancing systemic social innovation. Journal of Corporate Citizenship, 58, 67–84.",
    "Object Management Group. (2011). Business Process Model and Notation (BPMN), version 2.0 (formal/2011-01-03). https://www.omg.org/spec/BPMN/2.0/",
    "Object Management Group. (2017). OMG Unified Modeling Language (OMG UML), version 2.5.1 (formal/17-12-05). https://www.omg.org/spec/UML/2.5.1/",
    "Project Management Institute. (2017). A guide to the project management body of knowledge (PMBOK guide) (6th ed.). Project Management Institute.",
    "Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
    "Ward, J., & Daniel, E. (2012). Benefits management: How to increase the business value of your IT projects (2nd ed.). Wiley.",
]
kr = key("References")
old_refs = [r for r in sec[kr].split("\n\n") if r.strip()]
all_refs = sorted(set(old_refs + refs_new), key=lambda r: re.sub(r"[^a-z]", "", r.lower()))
sec[kr] = "\n\n".join(all_refs)

# =====================================================================  appendices: order A, B, C, D
appD = """
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
"""

# rebuild order
out = []
for h in order:
    name = h.lstrip("# ")
    if name.startswith("8.1 Three-Wave") or name.startswith("8.2 KPI") or name.startswith("8.3 Governance") or name.startswith("8.4 Final"):
        continue
    if name.startswith("Appendix B") or name.startswith("Appendix C"):
        continue
    out.append(h + "\n\n" + sec[h])
    if name.startswith("CHAPTER 7."):
        for t, b in new7.items():
            out.append("## " + t + "\n\n" + b.strip("\n"))
    if name.startswith("CHAPTER 8."):
        for t, b in new8.items():
            out.append("## " + t + "\n\n" + b.strip("\n"))
    if name.startswith("Appendix A"):
        b = key("Appendix B"); c = key("Appendix C")
        out.append(b + "\n\n" + sec[b])
        out.append(c + "\n\n" + sec[c])
        out.append("# Appendix D. Session 9 Feedback Response Log\n\n" + appD.strip("\n"))

md = "\n\n".join(out) + "\n"
# chapter 7 old table removal (kept first paragraph only already)
open("report_v4.md", "w", encoding="utf-8").write(md)
print("ok", len(md))
for m in sorted(set(re.findall(r"\{[TF]:(\w+)\}", md))):
    pass
defined = set(re.findall(r"(?:TABLE|FIG)\[(\w+)\]", md))
used = set(re.findall(r"\{[TF]:(\w+)\}", md))
print("undefined refs:", used - defined)
