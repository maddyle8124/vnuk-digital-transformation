"""Shorten the longest prose sections of report_v4.md (in place) to meet the 6,000-8,000 word guideline.
Tables, table captions and figure markers in a section are kept; only prose is replaced."""
import re

NEW = {
"# CHAPTER 1.": """
VNUK, a member institute of the University of Danang, aims to offer modern programmes in a friendly and inspiring environment (VNUK, n.d.-a). This report treats student support as part of that environment. The selected domain is Student Support and Academic Navigation, and the first product, Ask Nuki, covers academic enquiry guidance and routing. Students and staff are both primary users. Students need a clear next step and a transparent handoff; staff need complete, correctly routed requests and guidance they can maintain.

The evidence combines Customer Experience research (15 CSE students and five faculty members; a BMS survey of eight) with a review of 23 real requests from one VNUK mailbox. Eight of those requests were sent by reply-all to a whole cohort, and VNUK's website has no FAQ page (Customer Experience project teams, 2026a, 2026b; Group 1, 2026). These sources show failures and routing patterns, not institution-wide prevalence. Student Support ranked first of three candidate domains because a guidance-and-routing pilot needs no access to grades or official records.

The recommendation is a bounded, dual-user pilot. Ask Nuki answers from guidance approved by Academic Affairs, refuses to guess on official decisions and routes everything else once to the right office with a request ID. The non-AI service comes first, and AI is kept only if it adds measurable value (Fernández et al., 2023; UNESCO, 2023). The decision requested is Gate 1: a three-week pilot with five final-year CSE students. Growth follows only on evidence, first by expanding within Academic Affairs and then by scaling one department at a time. Each step has a readiness check, a measurement plan and a stage gate, and every design choice respects Vietnam's Personal Data Protection Law No. 91/2025/QH15. Appendix D maps each Session 9 comment to the section that answers it.
""",
"## 2.1 ": """
VNUK's vision is to become an international-standard university, and its mission includes modern programmes, essential skills for learners and a friendly, inspiring environment for faculty and learners (VNUK, n.d.-a; VNUK, n.d.-b). Student Support and Academic Navigation does not create learning outcomes itself. It removes service friction that stops students from following procedures and reaching the right support, and it frees staff time from low-value clarification. This links directly to the University of Danang's learner-centred and digital-transformation priorities (University of Danang, 2025).
""",
"## 2.2 ": """
The product has two primary user groups. Students need to find the correct procedure, prepare a complete request, reach the responsible unit and know what happens next. Staff, including advisers and administrative officers, need requests that arrive complete, correctly routed and supported by current, approved guidance. The value proposition is therefore dual: students complete the next step with less uncertainty, and staff resolve better-formed enquiries without hidden extra work. A service is not successful if students save effort but staff inherit more checking or maintenance. This framing follows research stressing stakeholder perceptions and implementation context over technology availability (Chugh et al., 2023).
""",
"## 2.3 ": """
Higher-education transformation is organisational, involving processes, people and information as well as technology (Fernández et al., 2023). VNUK's problem is not a lack of channels but the weak link between guidance, routing, ownership and measurement. Students increasingly expect self-service and all-in-one access to institutional services (EDUCAUSE, 2024), although this does not prove that VNUK students want a chatbot. Data-supported student services can be more responsive when governance keeps the human experience central (Peck, 2023; Stojanov & Daniel, 2024); the first step for VNUK is simply to capture service events consistently. Generative AI adds potential and risk: UNESCO (2023) and NIST (2023, 2024) call for human oversight, testing and lifecycle controls. These principles support keeping academic decisions with authorised staff and retaining a non-AI fallback.
""",
"## 2.4 ": """
The minimum technology set is a controlled knowledge repository, request routing, case tracking, basic analytics and a simple interface. Retrieval-based AI may later support classification and answering from approved material, but the service must work without it. That gives a fair comparison: if search and routing alone deliver the same outcomes at lower cost and risk, the AI layer should not be scaled. Readiness is partial. Channels and expertise exist, but integration, budget, demand data and staff time for content governance are not yet confirmed.

Personal-data handling must follow Law No. 91/2025/QH15 on Personal Data Protection, in force since 1 January 2026, and Decree No. 356/2025/ND-CP (National Assembly of Vietnam, 2025; Government of Vietnam, 2025). Practical controls are data minimisation, a stated purpose, role-based access, retention rules, logging and assessment before any cross-border processing. The report does not claim legal clearance; VNUK's authorised reviewers decide the final approach.
""",
"## 3.2 ": """
CSE accounts show variation rather than uniform failure: one student needed four to five LMS login attempts and waited four to five days for an advising reply, while an alumnus missed a graduation notice but was then helped by faculty (Customer Experience project teams, 2026a). BMS respondents mainly reported practical-learning barriers, such as heat-related fatigue (seven of eight) and insufficient practical time (four of eight), which belong to a separate domain (Customer Experience project teams, 2026b). Staff-side evidence is weaker: there is no systematic workload baseline yet, so one will be collected before launch.

A more recent source is one team member's VNUK mailbox for 2022–2026, with 23 academic requests (12 the member's own, 11 from other students, anonymised). Figure {F:requests} shows that almost half went to Academic Affairs. Eight were sent by reply-all to a whole cohort list, and two were refused because of rules the student learned only by asking. A check of vnuk.udn.vn on 11 November 2026 found no FAQ or help page. These counts show a routing pattern, not prevalence.

FIG[requests]: fig_requests.png | Where 23 Real Academic Requests Went
""",
"## 3.4 ": """
The current journey is: question raised, guidance sought, need clarified, resolved or routed, answer confirmed. Likely causes of repeat contact are dispersed guidance, unclear ownership, incomplete requests and staff workload; the evidence does not separate them, so each remains a hypothesis to test. Figure {F:asis} models this journey in BPMN 2.0, the standard notation for business processes (Object Management Group [OMG], 2011; ISO/IEC, 2013), so the pain points sit on a model others can check. A parallel gateway shows students trying several channels at once, and a loop shows repeat contact. Practical learning and academic progression follow different journeys with physical or authoritative-data constraints, so they stay outside this product.

FIG[asis]: fig_bpmn_asis.png | As-Is Academic Enquiry Process (BPMN 2.0)
""",
"## 5.6 ": """
The recommended archetype is a journey-led product pod: it owns one end-to-end journey and a persistent service, keeping users, content owners and platform specialists in one feedback loop (Team Topologies, n.d.; DBB43005 teaching team, 2026b). A small MVP needs three capabilities, namely business analysis, software engineering, and UX/UI with quality assurance, so no separate researcher, project manager or data scientist is required. Three roles sit with VNUK: Academic Affairs approves and updates guidance, the IT team and privacy adviser review controls, and the Director or Dean decides at the gates.
""",
"## 6.4 ": """
- Accuracy and routing: at least 80% of rated answers score 4–5; zero critical wrong guidance; at least 75% answered without an office; at least 80% of routed requests reach the right office first time (proposed thresholds).

- Traceability: every answer shows its source or owner office; every guide has an owner and review date.

- Privacy and security: minimum data, role-based access, defined retention and approved identity, logging and hosting before identifiable cases are stored.

- Accessibility: usable on common devices, in clear language, without requiring AI conversation.

- Resilience: on failure, a webhook alerts the team and students see a status page listing each office's email; failed emails are retried, reminders follow two days without status, and duplicates link to one request ID.
""",
"## 8.7 ": """
Governance focuses on outcomes, capacity and risk rather than Sprint tasks. Gate 1 opens the pilot once owner, baseline, content, identity and privacy are ready. Gate 2 allows an AI test only after the non-AI service works. Gate 3 approves expansion once both user groups benefit and routing is accurate. Gate 4 is applied to each new department through the readiness check in Table {T:ready}. The AI layer is paused when ratings fall below 70% in a week, unsupported answers or duplicates recur, staff rate context below 3 of 5, or access controls fail; guides and email routing continue meanwhile. The MVP stops if fewer than three of five students keep using it, no office owns the guidance, critical errors stay unresolved or two corrective cycles show no improvement.

Figure {F:decision} shows the week-3 decision logic. Ownership and safety are checked before performance targets, and the same logic is reused at Gates 2–4. The Director approves Gates 1, 3 and 4; the service owner allows the AI test and records the week-3 decision (Table {T:raci}).

FIG[decision]: fig_decision.png | Week-3 Decision Logic
""",
"# CHAPTER 9.": """
The proposal changed materially through critique. First, it no longer treats students as the only users: staff can gain or lose from the same product, so both are measured, including hidden upkeep work. Second, it moved away from technology-first reasoning. Isolated technology does not amount to transformation (Fernández et al., 2023), so approved knowledge, ownership, workflow and measurement now come before AI, and the non-AI service is a real alternative rather than a placeholder.

Third, the business case is deliberately modest. The capacity model supports sensitivity analysis but cannot prove a return without measured demand, effort and cost, and student time is not converted into cash without a defensible method. Fourth, the Session 9 review exposed weaknesses that were analytical as well as presentational: a free-form workflow (now BPMN and UML), stakeholders without named decision-makers (now an influence–impact grid and a RACI with sponsor, service owner, IT team and testers), and a loose idea of scale (now expanding within a department, then scaling department by department).

The main limitation remains evidence quality. Student data is small and partly historical, staff workload data is not systematic and IBM evidence is missing, so transferability is a question for the pilot, not an assumption. The legal and technical sections name relevant controls but do not replace VNUK's own legal, security or procurement review.
""",
"# CHAPTER 10.": """
Student Support and Academic Navigation remains the recommended domain, with a narrower and more defensible scope: a bounded, dual-user pilot of academic enquiry guidance and routing. The decision requested is approval of Gate 1, not university-wide AI deployment.

Conditions to proceed are: (1) confirm the Director or Dean as sponsor, the Head of Academic Affairs as service owner and the VNUK IT team as controls owner; (2) collect comparable student and staff baselines; (3) approve the initial guides and content owners; (4) confirm privacy and security arrangements; and (5) protect staff time for reviews. The service continues if student effort, resolution, routing and staff workload all improve with acceptable risk; it is adapted if value appears but workflow or content needs correction; and the AI layer is paused or stopped if critical errors occur, guides cannot be maintained or the simpler service performs as well. If the pilot succeeds, the service expands within Academic Affairs to all final-year students and then scales one department at a time, each step measured with the same model and decided at a gate.
""",
}

md = open("report_v4.md", encoding="utf-8").read()
parts = re.split(r"(?m)^(#{1,3} .*)$", md)
for i in range(1, len(parts), 2):
    h = parts[i]
    for k, v in NEW.items():
        if h.startswith(k):
            old = parts[i + 1]
            kept = []
            lines = old.split("\n")
            j = 0
            while j < len(lines):
                l = lines[j]
                if l.startswith("TABLE["):
                    kept.append(l); j += 1
                    while j < len(lines) and not lines[j].startswith("|"):
                        j += 1
                    blk = []
                    while j < len(lines) and lines[j].startswith("|"):
                        blk.append(lines[j]); j += 1
                    kept.append("\n" + "\n".join(blk))
                    continue
                j += 1
            new = v.strip("\n")
            if kept:
                new += "\n\n" + "\n".join(kept).strip("\n")
            parts[i + 1] = "\n\n" + new + "\n\n"
            break
md = "".join(parts)
for old, new in [("Sprint 1 is a two-week learning Sprint, not a production deployment.", "Sprint 1 is a two-week learning Sprint, not a production deployment (Schwaber & Sutherland, 2020)."),
                 ("Exit from each wave depends on evidence, not on a date.", "Exit from each wave depends on evidence, not on a date (DBB43005 teaching team, 2026a).")]:
    assert old in md, old
    md = md.replace(old, new)
open("report_v4.md", "w", encoding="utf-8").write(md)

body = md.split("# References")[0]
prose = "\n".join(l for l in body.split("\n") if l.strip() and not l.startswith(("|", "TABLE[", "FIG[", "#")))
print("prose words:", len(re.findall(r"[\w’'-]+", prose)))
