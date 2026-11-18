"""Project artifacts workbook: product backlog (full fields) plus the report's working tables."""
import re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

OUT = sys.argv[1]
NAVY, TEAL = "14324A", "DCEEED"
hdr_font = Font(bold=True, color="FFFFFF", name="Arial", size=10)
hdr_fill = PatternFill("solid", fgColor=NAVY)
body_font = Font(name="Arial", size=10)
thin = Side(style="thin", color="C9D3D9")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")

wb = Workbook()


def sheet(title, headers, rows, widths, note=None):
    ws = wb.create_sheet(title)
    r0 = 1
    if note:
        ws.cell(1, 1, note).font = Font(name="Arial", size=10, italic=True, color="555555")
        r0 = 3
    for j, h in enumerate(headers, 1):
        c = ws.cell(r0, j, h); c.font = hdr_font; c.fill = hdr_fill; c.alignment = wrap; c.border = border
    for i, row in enumerate(rows, r0 + 1):
        for j, v in enumerate(row, 1):
            c = ws.cell(i, j, v); c.font = body_font; c.alignment = wrap; c.border = border
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(r0, j).column_letter].width = w
    ws.freeze_panes = ws.cell(r0 + 1, 2)
    ws.auto_filter.ref = f"A{r0}:{ws.cell(r0, len(headers)).column_letter}{r0 + len(rows)}"
    return ws


# ------------------------------------------------------------------ README
ws = wb.active; ws.title = "README"
lines = [
    ("DBB43005 Group 1 – Ask Nuki: project artifacts", True),
    ("Companion workbook to the final report (DBB43005_Group1_FinalReport). Each sheet is a working version of an artifact in the report.", False),
    ("", False),
    ("Sheet", True),
    ("Product Backlog – ordered backlog with user story, priority, owner, acceptance criteria, dependency, status, effort, evidence source and wave (report 5.3–5.4).", False),
    ("Definition of Done – checklist every backlog item must pass.", False),
    ("Sprint & Pilot Plan – Sprint 1 day plan and the three-week pilot (report 5.5, 7.4).", False),
    ("RACI – task-level RACI with POC testers and decision tasks (report Table 12).", False),
    ("Stakeholders – influence–impact map and engagement strategy (report Table 1).", False),
    ("Change Impact / Resistance / ADKAR – Chapter 7 tables.", False),
    ("Department Scaling / Readiness – unit of scale and Gate 4 checklist (report 8.2, 8.5).", False),
    ("KPI Plan / KPI Dictionary – measurement plan by wave and metric definitions (report Table 22, Appendix A).", False),
    ("Risk Register – final risk register (report Table 23).", False),
    ("", False),
    ("Status values: Done (prototype) = built and demonstrated in the class prototype; To do (pilot) = needed before or during the VNUK pilot; Later = Wave 2–3.", False),
    ("Targets are proposed pilot thresholds, not measured VNUK baselines. Named VNUK roles (Director/Dean, Head of Academic Affairs, IT team) are still to be confirmed.", False),
]
for i, (t, b) in enumerate(lines, 1):
    c = ws.cell(i, 1, t); c.font = Font(name="Arial", size=12 if i == 1 else 10, bold=b, color=NAVY if b else "222222")
ws.column_dimensions["A"].width = 130

# ------------------------------------------------------------------ Product backlog
B = [
# id, epic, story, moscow, rank, owner, AC, dependency, status, points, evidence, wave
("PB-01", "Foundation", "As a content owner, I want every guide stored with source, owner, scope and review date, so that students and staff use current, approved information.", "Must", 1, "Zsombi", "Schema has source, owner, applicability, review date; a guide without them cannot be published; expired guides hidden.", "—", "Done (prototype)", 5, "Lecturer feedback; mailbox review (rules learned only by asking)", "Wave 1"),
("PB-02", "Foundation", "As Academic Affairs, I want to approve the first 24 guides drafted from real replies, so that Nuki only answers from authoritative content.", "Must", 2, "Head of AA (content officer)", "24 guides reviewed; each marked approved with date; rejected guides removed.", "PB-01; named content owner", "To do (pilot)", 5, "24 draft guides from mailbox and daotao portal", "Wave 1"),
("PB-03", "Access", "As VNUK, I want only verified student and staff accounts to use the portal, read-only, so that personal data stays protected.", "Must", 3, "Zsombi", "Non-VNUK email refused; check is read-only; no grades, fees or records read.", "IT approval of account list / SSO", "Done (prototype); SSO to do", 3, "Law 91/2025; IT/privacy review", "Wave 1"),
("PB-04", "Student journey", "As a final-year student, I find I don’t know which office owns my question, so I want one place to ask in English or Vietnamese.", "Must", 4, "Tamas", "Chat accepts EN and VI with or without accents; topic chips shown; answer within 10 s median.", "PB-01", "Done (prototype)", 5, "Interviews; 8 reply-all requests", "Wave 1"),
("PB-05", "Student journey", "As a student, I want an answer card with steps, owner office, source and date, so that I can act and trust the answer.", "Must", 5, "Tamas", "Every answer shows steps, owner, source, review date; rating 1–5 with ‘why?’ under 4.", "PB-01, PB-04", "Done (prototype)", 3, "CX research; credit-limit refusals", "Wave 1"),
("PB-06", "Safety", "As Academic Affairs, I want Nuki to refuse official decisions (eligibility, grades, fees), so that no student acts on a guessed answer.", "Must", 6, "Tamas", "Test set of decision questions: 100% refused and offered routing; 0 critical wrong answers in pilot.", "PB-05; test set", "Done (prototype)", 3, "NIST AI RMF; UNESCO 2023", "Wave 1"),
("PB-07", "Routing", "As a staff member, I find requests arrive without context or at the wrong office, so I want one email with full context, a request ID and the student copied.", "Must", 7, "Tamas", "Email has verified student, topic, question, what Nuki showed, REQ-ID; goes to owner office; staff context rating ≥4/5.", "PB-08; office mailboxes", "Done (prototype)", 5, "Mailbox: forwarding between offices", "Wave 1"),
("PB-08", "Routing", "As the service owner, I want a request database with one ID per request and duplicate blocking, so that nothing is routed twice and every case is tracked.", "Must", 8, "Zsombi", "Unique REQ-ID; resending the same question points to existing ID; status history stored.", "PB-03", "Done (prototype)", 5, "Lecturer feedback: ‘request database’", "Wave 1"),
("PB-09", "Closure", "As office staff, I want to log status and rate context from a link in the email, so that I don’t learn a new system.", "Must", 9, "Tamas", "Link opens status page for that REQ-ID; statuses Received / In progress / Resolved / Forward; no login beyond the link token.", "PB-07, PB-08", "Done (prototype)", 3, "Staff feedback: ‘no extra inbox’", "Wave 1"),
("PB-10", "Closure", "As a student, I want to see my request status and rate the staff reply, so that I know it is solved.", "Should", 10, "Yuhan", "My-requests page shows Sent → Resolved; rate-your-answer email after closure.", "PB-09", "Done (prototype)", 2, "Interviews: no visible owner", "Wave 1"),
("PB-11", "Closure", "As the service owner, I want an automatic reminder after 2 working days without status, so that requests don’t stall.", "Should", 11, "Tamas", "Reminder sent once with the same link; logged in pilot log.", "PB-09; response window agreed", "Done (prototype)", 2, "4–5-day advising delay (CX)", "Wave 1"),
("PB-12", "Measurement", "As the service owner, I want events, ratings and status logged, so that I can decide continue, pivot, pause or stop on evidence.", "Must", 12, "Zsombi", "KPIs in pilot log computed automatically; weekly export; no personal data in analytics.", "PB-08", "Done (prototype)", 5, "DeLone & McLean model", "Wave 1"),
("PB-13", "Resilience", "As a student, I want a status page with office emails if the portal is down, so that urgent questions still reach someone.", "Should", 13, "Zsombi", "Outage page lists office emails by topic; webhook alerts team chat within 5 min.", "Hosting choice", "To do (pilot)", 3, "NFR resilience", "Wave 1"),
("PB-14", "Discovery", "As the BA, I want a two-week student and staff baseline, so that pilot results can be compared fairly.", "Must", 14, "Maddie", "Volume, first reply, repeat contact, wrong-office rate and staff minutes captured for 2 weeks.", "Office cooperation", "To do (pilot)", 5, "Appendix A, C", "Wave 1"),
("PB-15", "Trust", "As the IT/privacy reviewer, I want a controls checklist (data minimisation, retention, access, hosting), so that I can sign off before launch.", "Must", 15, "Zsombi", "Checklist signed by IT/privacy before Gate 1; retention period set.", "IT reviewer named", "To do (pilot)", 3, "Law 91/2025; Decree 356/2025", "Wave 1"),
("PB-16", "Learning loop", "As Academic Affairs, I want a weekly content-gap queue of low-rated and unanswered questions, so that guides improve and frequent ones become FAQ pages.", "Should", 16, "Maddie", "Queue shows gaps with counts; each gap classified and closed or turned into a guide/FAQ within a week.", "PB-12", "Done (prototype)", 3, "Session logs; token-cost saving", "Wave 1"),
("PB-17", "Department: IT Support", "As an IT Support officer, I find login and Canvas problems reach me days later via other offices, so I want access issues routed to IT on first contact.", "Could", 17, "Maddie", "≥90% of access questions reach IT first time; no forwarding.", "Gate 4 readiness for IT Support", "Later", 5, "4 of 23 mailbox requests", "Wave 3"),
("PB-18", "Department: Student Affairs", "As a Student Affairs officer, I find letter requests arrive without the right form, so I want a checklist with the BM.ĐT form code before routing.", "Could", 18, "Maddie", "Form code and documents present in ≥90% of requests.", "Gate 4 readiness", "Later", 3, "4 of 23 mailbox requests", "Wave 3"),
("PB-19", "Department: Finance", "As a Finance officer, I find tuition questions mix rules with personal balances, so I want rules answered and personal cases routed with an ID.", "Could", 19, "Maddie", "No answer states an individual balance; personal cases routed with REQ-ID.", "Privacy rule for financial data", "Later", 3, "2 of 23 mailbox requests", "Wave 3"),
("PB-20", "Department: Assessment", "As an Assessment Unit officer, I find re-marking requests arrive late or at the wrong office, so I want the deadline and form shown first.", "Could", 20, "Maddie", "No re-marking request routed to Academic Affairs in test set.", "Deadline calendar", "Later", 3, "Re-marking guides drafted", "Wave 3"),
("PB-21", "AI layer", "As the service owner, I want to test AI retrieval against the non-AI service, so that AI is kept only if it adds measurable value.", "Could", 21, "Tamas", "A/B on the same questions: AI kept only if ratings or self-service improve with no rise in critical errors or cost per request.", "Gate 2; test set", "Later", 8, "Report 4.5; NIST AI RMF", "Wave 2"),
("PB-22", "AI layer", "As office staff, I want a suggested reply draft from the approved guide, so that I answer routed requests faster.", "Won’t (this pilot)", 22, "Tamas", "Draft always editable; staff must send it themselves; usage logged.", "PB-21", "Done (prototype, off by default)", 3, "Staff effort KPI", "Wave 2"),
]
ws = sheet("Product Backlog",
           ["ID", "Epic", "User story", "Priority (MoSCoW)", "Rank", "Owner", "Acceptance criteria", "Dependency", "Status", "Effort (pts)", "Evidence source", "Wave"],
           [list(b) for b in B], [8, 16, 60, 13, 7, 16, 48, 24, 20, 9, 30, 9],
           note="Ordered product backlog (rank 1 = highest). Definition of Done: see next sheet. Effort in story points (Fibonacci).")
n = len(B) + 3
dv = DataValidation(type="list", formula1='"Done (prototype),Done (prototype); SSO to do,Done (prototype, off by default),To do (pilot),In progress,Later"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"I4:I{n}")
dv2 = DataValidation(type="list", formula1='"Must,Should,Could,Won’t (this pilot)"', allow_blank=True)
ws.add_data_validation(dv2); dv2.add(f"D4:D{n}")
ws.conditional_formatting.add(f"I4:I{n}", FormulaRule(formula=[f'LEFT(I4,4)="Done"'], fill=PatternFill("solid", fgColor="DCEEED")))
ws.conditional_formatting.add(f"I4:I{n}", FormulaRule(formula=[f'LEFT(I4,5)="To do"'], fill=PatternFill("solid", fgColor="F1E4DB")))
r = n + 2
ws.cell(r, 2, "Total effort (pts)").font = Font(name="Arial", size=10, bold=True)
ws.cell(r, 10, f"=SUM(J4:J{n})").font = Font(name="Arial", size=10, bold=True)
ws.cell(r + 1, 2, "Wave 1 effort (pts)").font = Font(name="Arial", size=10, bold=True)
ws.cell(r + 1, 10, f'=SUMIF(L4:L{n},"Wave 1",J4:J{n})').font = Font(name="Arial", size=10, bold=True)
ws.cell(r + 2, 2, "Items done in prototype").font = Font(name="Arial", size=10, bold=True)
ws.cell(r + 2, 10, f'=COUNTIF(I4:I{n},"Done*")').font = Font(name="Arial", size=10, bold=True)

sheet("Definition of Done", ["#", "Criterion", "Checked by"], [
    (1, "Acceptance criteria met and demonstrated on the test set", "Yuhan"),
    (2, "Tested with at least one student and one staff member; feedback logged", "Yuhan"),
    (3, "Guidance used by the item has source, owner and review date, approved by Academic Affairs", "Head of AA"),
    (4, "No personal data beyond the agreed minimum; access and retention unchanged or re-approved", "Zsombi / IT"),
    (5, "Events and KPIs for the item appear in the pilot log", "Zsombi"),
    (6, "Refusal and routing still work for official-decision questions (regression test)", "Tamas"),
    (7, "Backlog and report updated; Product Owner accepts", "Maddie"),
], [6, 90, 20])

sheet("Sprint & Pilot Plan", ["Period", "Goal", "Activities", "Owner", "Exit / output"], [
    ("Sprint 1 · days 1–2", "Shared definitions", "Audit enquiries; confirm taxonomy and baseline definitions", "Maddie", "Taxonomy and baseline sheet agreed"),
    ("Sprint 1 · days 3–4", "Content and workflow", "Structure guides; map staff workflow and ownership", "Maddie, Yuhan", "Guide schema filled; workflow agreed"),
    ("Sprint 1 · days 5–7", "Build", "Build sign-in, chat, answer card, routing email, status link", "Tamas, Zsombi", "Working flow on test data"),
    ("Sprint 1 · days 8–9", "Test", "Usability and QA with students and staff", "Yuhan", "Defects and feedback logged"),
    ("Sprint 1 · day 10", "Review", "Sprint review; reorder backlog", "Maddie", "Updated backlog"),
    ("Pilot · prepare", "Make it safe", "Name owners; approve 24 guides; sign off controls; capture baseline", "Maddie", "Gate 1 passed (Director)"),
    ("Pilot · week 1", "Enable", "Onboard 5 students; 15-min staff walkthrough; each closes a test case", "Yuhan", "All 5 students active"),
    ("Pilot · week 2", "Use", "Real graduation-journey questions; office hours; monitoring", "Tamas", "0 critical errors; workload check"),
    ("Pilot · week 3", "Decide", "Review the 4 numbers; fix gaps; retest", "Maddie", "Week-3 decision recorded (service owner)"),
], [20, 20, 60, 16, 36])


def md_table(key):
    md = open("report_v4.md", encoding="utf-8").read()
    m = re.search(r"TABLE\[" + key + r"\]: (.*)\n\n((?:\|.*\n)+)", md)
    rows = [[c.strip().replace("**", "").replace("*", "") for c in l.strip().strip("|").split("|")] for l in m.group(2).strip().split("\n")]
    rows = [r for r in rows if not re.match(r"^-+$", r[0])]
    return rows[0], rows[1:]


for key, title, widths in [("raci", "RACI", [44] + [12] * 9), ("stake", "Stakeholders", [30, 34, 12, 16, 46]),
                           ("impact", "Change Impact", [26, 36, 16, 10, 24, 26]), ("resist", "Resistance", [22, 30, 30, 28, 50]),
                           ("adkar", "ADKAR", [16, 34, 34, 30, 30]), ("depts", "Department Scaling", [9, 18, 20, 36, 30, 30]),
                           ("ready", "Readiness (Gate 4)", [16, 60, 30]), ("kpi", "KPI Plan", [30, 40, 24, 18, 22, 28]),
                           ("dict", "KPI Dictionary", [26, 70, 26]), ("risk", "Risk Register", [36, 12, 10, 18, 50])]:
    h, rows = md_table(key)
    sheet(title, h, rows, widths)

wb.save(OUT)
print("saved", OUT)
