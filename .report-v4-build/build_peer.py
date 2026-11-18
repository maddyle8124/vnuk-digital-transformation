import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = sys.argv[1]
d = Document()
s = d.sections[0]
s.orientation = WD_ORIENT.LANDSCAPE
s.page_width, s.page_height = s.page_height, s.page_width
for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(s, m, Cm(1.8))
st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(11)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), fill); tcPr.append(sh)


def table(headers, rows, widths):
    t = d.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"
    for j, h in enumerate(headers):
        c = t.rows[0].cells[j]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(10); shade(c, "D9EAF7")
    for row in rows:
        cells = t.add_row().cells
        for j, v in enumerate(row):
            cells[j].text = ""; r = cells[j].paragraphs[0].add_run(v); r.font.size = Pt(10)
    for row in t.rows:
        for j, w in enumerate(widths):
            row.cells[j].width = Cm(w)
    return t


h = d.add_paragraph(); h.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = h.add_run("GROUP CONTRIBUTION AND PEER-EVALUATION FORM"); r.bold = True; r.font.size = Pt(14)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("DBB43005 Digital Innovation and Transformation · Final Group Project · Group 1 · Lecturer: Dr. Đặng Trung Thành · Semester 1, 2026–2027")
p = d.add_paragraph()
r = p.add_run("Draft prepared from the roles in the report. The group must review the contribution descriptions, agree the percentages and scores together, and each member must sign. Contributions marked “confirm” need checking.")
r.italic = True; r.font.size = Pt(10); r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

d.add_paragraph().add_run("Part A. Roles and contributions").bold = True
table(["Member", "Student ID", "Role", "Main contributions (report, product, presentation)", "Presents (final deck)"], [
    ("Le Nguyen Thanh Hang (Maddie)", "22060016", "Business Analyst / Product Owner",
     "Report chapters 1, 3, 4, 9, 10 and Appendices A–D; requirements, ordered backlog and acceptance criteria; mailbox evidence review; business case and value-driver tree; stakeholder alignment (confirm)",
     "Slides 1–8, 27–28"),
    ("Liu Yu Han (Yuhan)", "23060013", "UX/UI, QA and customer-facing lead",
     "Report chapter 7 and section 5.3; student and staff journey, usability tests and feedback collection; change impact, resistance, Kotter and ADKAR plan; adoption roadmap (confirm)",
     "Slides 9–10, 18–21"),
    ("Tamás Pieskó (Tamas)", "25010613", "Software Engineer / Technical lead",
     "Prototype portal, chat, answer card, routing email and status link; AI/API integration; BPMN and UML flows; report sections 5.8 and 6.2–6.3; demo recordings (confirm)",
     "Slides 12–17 and live demo"),
    ("Zsombi Mester (Zsombi)", "25120300", "Software Engineer / Data and integration lead",
     "Sign-in allowlist, request database, retrieval, event logging and monitoring; report sections 5.6–5.7, 6.1, 6.4 and chapter 8 (scaling, measurement plan, gates, risk register) (confirm)",
     "Slides 11, 22–26"),
], [4.5, 2.2, 4.2, 11.5, 3.6])

d.add_paragraph()
d.add_paragraph().add_run("Part B. Agreed contribution and peer scores (1 = very low, 5 = excellent)").bold = True
table(["Member", "Agreed contribution (%)", "Quality of work", "Reliability and deadlines", "Collaboration", "Presentation and defence", "Average", "Comment"],
      [(n, "", "", "", "", "", "", "") for n in ("Maddie", "Yuhan", "Tamas", "Zsombi")] + [("Total", "100%", "", "", "", "", "", "")],
      [3.2, 2.8, 2.4, 2.8, 2.6, 2.8, 2.0, 7.4])

d.add_paragraph()
d.add_paragraph().add_run("Part C. Acknowledgement").bold = True
d.add_paragraph("We confirm that the contributions above are accurate, that the scores were discussed and agreed by all members, and that the project is our own original work.")
table(["Member", "Signature", "Date"], [(n, "", "") for n in ("Le Nguyen Thanh Hang", "Liu Yu Han", "Tamás Pieskó", "Zsombi Mester")], [8, 10, 6])
d.save(OUT)
print("saved", OUT)
