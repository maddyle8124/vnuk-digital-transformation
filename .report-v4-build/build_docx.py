import copy, re, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from PIL import Image

SRC = "../DBB43005_Group1_VNUK_Report_v3.docx"
OUT = sys.argv[1] if len(sys.argv) > 1 else "../DBB43005_Group1_VNUK_Report_v4.docx"
TEXT_W = 9405  # twips available between margins

doc = Document(SRC)
body = doc.element.body
els = list(body.iterchildren())
toc_idx = next(i for i, e in enumerate(els) if e.tag == qn("w:p") and "TABLE OF CONTENTS" in "".join(t.text or "" for t in e.iter(qn("w:t"))))
for e in els[toc_idx:]:
    if e.tag != qn("w:sectPr"):
        body.remove(e)
sectPr = body.find(qn("w:sectPr"))

# title-page date
for p in doc.paragraphs:
    for r in p.runs:
        if "October 2026" in r.text:
            r.text = r.text.replace("October 2026", "November 2026")


def new_p(style=None):
    p = OxmlElement("w:p")
    sectPr.addprevious(p)
    from docx.text.paragraph import Paragraph
    para = Paragraph(p, doc._body)
    if style:
        para.style = doc.styles[style]
    return para


def add_runs(para, text, size=None, bold_all=False, italic_all=False):
    # **bold** and *italic*
    tokens = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text)
    for t in tokens:
        if not t:
            continue
        b = bold_all; i = italic_all
        if t.startswith("**") and t.endswith("**"):
            t = t[2:-2]; b = True
        elif t.startswith("*") and t.endswith("*") and len(t) > 1:
            t = t[1:-1]; i = True
        r = para.add_run(t)
        if b: r.bold = True
        if i: r.italic = True
        if size: r.font.size = Pt(size)
    return para


def field(para, instr, cached=""):
    def fc(t):
        r = OxmlElement("w:r"); f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), t); r.append(f); return r
    para._p.append(fc("begin"))
    r = OxmlElement("w:r"); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "; r.append(it); para._p.append(r)
    para._p.append(fc("separate"))
    r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = cached; r.append(t); para._p.append(r)
    para._p.append(fc("end"))


def page_break():
    p = new_p()
    p.add_run().add_break(WD_BREAK.PAGE)


md = open("report_v4.md", encoding="utf-8").read()
# numbering
tnum, fnum = {}, {}
for m in re.finditer(r"^(TABLE|FIG)\[(\w+)\]", md, flags=re.M):
    d = tnum if m.group(1) == "TABLE" else fnum
    d[m.group(2)] = len(d) + 1
md = re.sub(r"\{T:(\w+)\}", lambda m: str(tnum[m.group(1)]), md)
md = re.sub(r"\{F:(\w+)\}", lambda m: str(fnum[m.group(1)]), md)
heads = re.findall(r"^(#{1,3}) (.*)$", md, flags=re.M)
tcaps = re.findall(r"^TABLE\[\w+\]: (.*)$", md, flags=re.M)
fcaps = [c.split("|")[1].strip() for c in re.findall(r"^FIG\[\w+\]: (.*)$", md, flags=re.M)]

# ---------- front matter: static TOC, list of figures, list of tables with real page numbers
import json, os
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
PAGES = json.load(open("pages.json")) if os.path.exists("pages.json") else {}


def entry(text, page, level=1, bold=False):
    p = new_p()
    pf = p.paragraph_format
    pf.left_indent = Cm(0.6 * (level - 1))
    pf.space_after = Pt(3 if level > 1 else 5)
    pf.space_before = Pt(0 if level > 1 else 4)
    pf.line_spacing = 1.0
    pf.first_line_indent = Cm(0); pf.right_indent = Cm(0)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.tab_stops.add_tab_stop(Cm(15.8), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    pf.left_indent = Cm(0.6 * (level - 1)); r = p.add_run(text); r.font.size = Pt(11); r.bold = bold
    r = p.add_run("\t" + str(page)); r.font.size = Pt(11); r.bold = bold


for title, items in [("TABLE OF CONTENTS", [(t, len(h)) for h, t in heads]),
                     ("LIST OF FIGURES", [(f"Figure {i + 1}. {c}", 2) for i, c in enumerate(fcaps)]),
                     ("LIST OF TABLES", [(f"Table {i + 1}. {c}", 2) for i, c in enumerate(tcaps)])]:
    h = new_p("TOC Heading"); h.add_run(title)
    for text, lvl in items:
        key = text.split(". ")[0] if title != "TABLE OF CONTENTS" else text
        entry(text, PAGES.get(key, ""), level=lvl if title == "TABLE OF CONTENTS" else 1, bold=(lvl == 1 and title == "TABLE OF CONTENTS"))
    page_break()


def caption(kind, title):
    p = new_p("Caption")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(8)
    r = p.add_run(f"{kind} "); r.bold = True; r.italic = False
    field(p, f"SEQ {kind} \\* ARABIC", str((tnum if kind == 'Table' else fnum)[cur_key]))
    for rr in p._p.findall(qn("w:r"))[1:]:
        rp = OxmlElement("w:rPr"); b = OxmlElement("w:b"); rp.append(b); rr.insert(0, rp)
    r = p.add_run(". "); r.bold = True
    r = p.add_run(title); r.italic = True
    for rr in p.runs:
        rr.font.color.rgb = RGBColor(0, 0, 0)
        rr.font.size = Pt(11)
    return p


def crop_title(path):
    im = Image.open(path)
    w, h = im.size
    name = path.split("/")[-1]
    if name in ("fig_requests.png", "fig_priority.png", "fig_breakeven.png"):
        top = int(h * 0.13)
    else:
        top = int(0.66 / 2.54 * 220)
    out = "figs_report/" + name
    im.crop((0, top, w, h)).save(out)
    return out


def add_figure(fname, title):
    caption("Figure", title)
    path = crop_title("figs/" + fname)
    p = new_p()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = False
    im = Image.open(path)
    width_cm = 16.4
    max_h_cm = 21.0
    h_cm = width_cm * im.height / im.width
    if h_cm > max_h_cm:
        width_cm = max_h_cm * im.width / im.height
    p.add_run().add_picture(path, width=Cm(width_cm))


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    s = OxmlElement("w:shd"); s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill); tcPr.append(s)


def add_table(rows):
    hdr = [c.replace("**", "").strip() for c in rows[0]]
    data = rows[1:]
    n = len(hdr)
    t = doc.add_table(rows=0, cols=n)
    sectPr.addprevious(t._tbl)
    t.style = doc.styles["Table Grid"]
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    wide = n >= 8
    fs = 8 if wide else (9.5 if n >= 5 else 10.5)
    # widths
    lens = []
    for j in range(n):
        L = max([len(hdr[j])] + [len(r[j]) for r in data if j < len(r)])
        lens.append(L)
    if wide:
        ws = [2500] + [int((TEXT_W - 2500) / (n - 1))] * (n - 1)
    else:
        wts = [max(8, min(L, 120)) ** 0.75 for L in lens]
        ws = [int(TEXT_W * x / sum(wts)) for x in wts]
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(ws[j]))

    def fill_row(vals, header=False, section=False):
        row = t.add_row()
        if header:
            trPr = row._tr.get_or_add_trPr(); th = OxmlElement("w:tblHeader"); trPr.append(th)
        cant = OxmlElement("w:cantSplit"); row._tr.get_or_add_trPr().append(cant)
        for j, c in enumerate(row.cells):
            c.width = Emu(ws[j] * 635)
            txt = vals[j] if j < len(vals) else ""
            p = c.paragraphs[0]
            p.style = doc.styles["Table Text"]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            if wide and j > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs(p, txt, size=(6.8 if (wide and header and j > 0) else fs), bold_all=header or (wide and txt.strip() == "A" and not header))
            if header:
                shade(c, "D9EAF7")
            elif section:
                shade(c, "F2F2F2")
        if section:
            a = row.cells[0]; b = row.cells[-1]
            m = a.merge(b)
            for extra in m.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
    fill_row(hdr, header=True)
    for r in data:
        sec = r[0].startswith("*") and r[0].endswith("*") and all(not x.strip() for x in r[1:])
        fill_row(r, section=sec)
    sp = new_p(); sp.paragraph_format.space_after = Pt(2)


lines = md.split("\n")
i = 0
cur_key = None
first_h1 = True
while i < len(lines):
    ln = lines[i]
    if not ln.strip():
        i += 1; continue
    m = re.match(r"^(#{1,3}) (.*)$", ln)
    if m:
        lvl = len(m.group(1))
        if lvl == 1 and not first_h1:
            page_break()
        first_h1 = False
        p = new_p(f"Heading {lvl}")
        p.add_run(m.group(2))
        i += 1; continue
    m = re.match(r"^TABLE\[(\w+)\]: (.*)$", ln)
    if m:
        cur_key = m.group(1)
        caption("Table", m.group(2))
        i += 1; continue
    m = re.match(r"^FIG\[(\w+)\]: (.*)$", ln)
    if m:
        cur_key = m.group(1)
        f, title = [x.strip() for x in m.group(2).split("|")]
        add_figure(f, title)
        i += 1; continue
    if ln.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            if not re.match(r"^\|[-| ]+\|$", lines[i]):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
            i += 1
        add_table(rows)
        continue
    if ln.startswith("- "):
        p = new_p("List Bullet"); add_runs(p, ln[2:].strip()); i += 1; continue
    if ln.startswith("> "):
        p = new_p(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.left_indent = Cm(1); p.paragraph_format.right_indent = Cm(1)
        add_runs(p, ln[2:].strip()); i += 1; continue
    p = new_p()
    txt = ln.replace("\\[", "[").replace("\\]", "]")
    if re.match(r"^R = Responsible|^Positions are the team", txt):
        add_runs(p, txt, size=10, italic_all=True)
    else:
        add_runs(p, txt)
    i += 1

# ask Word to refresh TOC / list fields on open
settings = doc.settings.element
doc.core_properties.title = "VNUK Digital Transformation Strategy – AI Student Support Hub (v4)"
doc.save(OUT)
print("saved", OUT, "tables", len(tnum), "figures", len(fnum))
