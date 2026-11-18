import sys
from dg import *
import numpy as np

OUT = sys.argv[1] if len(sys.argv) > 1 else "figs"


# ------------------------------------------------------------------ UML sequence
def sequence():
    W, Hh = 18, 16.8
    fig, ax = canvas(W, Hh)
    text(ax, 0.3, 0.35, "sd Route an unanswered question  (UML 2.5 sequence diagram, one MVP feature)", size=8.5, ha="left", weight="bold", color=NAVY)
    lifelines = [("Student", ":Student", 1.4), ("Portal", ":Ask Nuki portal", 4.3), ("Retr", ":Retrieval +\nAI service", 7.2),
                 ("DB", ":Request\ndatabase", 10.0), ("Mail", ":VNUK email\nservice", 12.8), ("Office", ":Department\noffice", 15.9)]
    X = {k: x for k, _, x in lifelines}
    top, bot = 1.0, 15.85
    for k, lab, x in lifelines:
        box(ax, x - 1.15, top, 2.3, 0.85, lab, fc=BLUE if k not in ("Student", "Office") else "white", ec=NAVY, r=0.05, size=6.8)
        ax.add_line(Line2D([x, x], [top + 0.85, bot], color=GREY, lw=0.7, ls=(0, (4, 3))))
    # actor stick figures for humans
    def act(x0, y0, x1, y1):
        ax.add_patch(Rectangle((x0 - 0.09, y0), 0.18, y1 - y0, fc="white", ec=INK, lw=0.7, zorder=3))
    def msg(y, a, b, label, ret=False, la="center"):
        xa, xb = X[a], X[b]
        d = 0.09 if xb > xa else -0.09
        arrow(ax, xa + d, y, xb - d, y, color=INK, lw=0.8, ls=(0, (4, 2)) if ret else "-", head="->" if ret else "-|>", ms=7)
        mx = (xa + xb) / 2
        text(ax, mx, y - 0.2, label, size=6.2, color=INK if not ret else GREY)
    def selfmsg(y, a, label):
        x = X[a] + 0.09
        poly_arrow(ax, [(x, y), (x + 0.6, y), (x + 0.6, y + 0.35), (x, y + 0.35)], ms=6, lw=0.8)
        text(ax, x + 0.7, y + 0.17, label, size=6.2, ha="left")
    y = 2.5
    act(X["Portal"], 2.3, X["Portal"], 15.6)
    msg(y, "Student", "Portal", "1: ask(question)")
    y += 0.65; msg(y, "Portal", "Retr", "2: retrieve(question)")
    act(X["Retr"], y - 0.05, X["Retr"], y + 0.7)
    y += 0.65; msg(y, "Retr", "Portal", "3: passages, topic, decision flag", ret=True)
    # alt fragment
    fy0 = y + 0.35
    y += 1.25
    msg(y, "Portal", "Student", "4: answer card (source, owner, review date)", ret=True)
    y += 0.65; msg(y, "Student", "Portal", "5: rate(1–5)")
    y += 0.65; msg(y, "Portal", "DB", "6: logEvent(rating)")
    act(X["DB"], y - 0.05, X["DB"], y + 0.3)
    fmid = y + 0.45
    y += 1.2
    msg(y, "Portal", "Student", "7: can't answer; send to owner office?", ret=True)
    y += 0.65; msg(y, "Student", "Portal", "8: confirm")
    y += 0.65; msg(y, "Portal", "DB", "9: createRequest(context)")
    act(X["DB"], y - 0.05, X["DB"], y + 0.7)
    y += 0.0; selfmsg(y + 0.05, "DB", "10: check duplicate")
    y += 0.75; msg(y, "DB", "Portal", "11: REQ-2611-0042", ret=True)
    y += 0.65; msg(y, "Portal", "Mail", "12: send(office, cc student, context, status link)")
    act(X["Mail"], y - 0.05, X["Mail"], y + 0.7)
    y += 0.65; msg(y, "Mail", "Office", "13: routed email [REQ-ID]")
    act(X["Office"], y - 0.05, X["Office"], 14.4)
    y += 0.65; msg(y, "Office", "Student", "14: reply in normal email", ret=False)
    fy1 = y + 0.35
    # opt fragment reminder
    oy0 = y + 0.5
    y += 1.2; msg(y, "Portal", "Mail", "15: reminder(REQ-ID)")
    oy1 = y + 0.3
    y += 0.8; msg(y, "Office", "Portal", "16: statusLink(resolved, contextRating)")
    y += 0.65; msg(y, "Portal", "DB", "17: updateStatus(REQ-ID, closed)")
    y += 0.65; msg(y, "Portal", "Student", "18: rate-your-answer email", ret=True)
    # alt frame
    rect(ax, 0.5, fy0, 17.0, fy1 - fy0, fc="none", ec=NAVY, lw=0.9)
    ax.add_patch(Polygon([(0.5, fy0), (1.45, fy0), (1.45, fy0 + 0.25), (1.3, fy0 + 0.4), (0.5, fy0 + 0.4)], fc="white", ec=NAVY, lw=0.9))
    text(ax, 0.62, fy0 + 0.2, "alt", size=6.8, weight="bold", ha="left", color=NAVY)
    text(ax, 1.65, fy0 + 0.22, "[enough approved evidence and not an official decision]", size=6.2, ha="left", color=NAVY)
    ax.add_line(Line2D([0.5, 17.5], [fmid, fmid], color=NAVY, lw=0.8, ls=(0, (5, 3))))
    text(ax, 0.65, fmid + 0.22, "[else]", size=6.2, ha="left", color=NAVY)
    # opt frame
    rect(ax, 3.2, oy0, 10.6, oy1 - oy0, fc="none", ec=AMBER, lw=0.9)
    ax.add_patch(Polygon([(3.2, oy0), (4.05, oy0), (4.05, oy0 + 0.25), (3.9, oy0 + 0.4), (3.2, oy0 + 0.4)], fc="white", ec=AMBER, lw=0.9))
    text(ax, 3.3, oy0 + 0.2, "opt", size=6.8, weight="bold", ha="left", color=AMBER)
    text(ax, 4.25, oy0 + 0.22, "[no status after 2 working days]", size=6.2, ha="left", color=AMBER)
    footnote(ax, 0.3, 16.25, "Notation: UML 2.5.1 sequence diagram (OMG, 2017). Solid arrow = synchronous message; dashed arrow = reply; tall boxes = activations;")
    footnote(ax, 0.3, 16.58, "alt = alternative fragments with guards in [ ]; opt = optional fragment. Message 14 goes by the office's normal email; Nuki only receives the status link.")
    save(fig, f"{OUT}/fig_uml_sequence.png")


# ------------------------------------------------------------------ UML component
def component():
    fig, ax = canvas(18, 10.8)
    text(ax, 0.3, 0.35, "Conceptual architecture (UML 2.5 component diagram)", size=8.5, ha="left", weight="bold", color=NAVY)
    def comp(x, y, w, h, name, sub="", fc="white", ec=NAVY, ls="-"):
        box(ax, x, y, w, h, "", fc=fc, ec=ec, r=0.05, ls=ls)
        text(ax, x + w / 2, y + 0.3, "«component»", size=5.6, color=GREY)
        text(ax, x + w / 2, y + 0.62, name, size=6.8, weight="bold", color=INK)
        if sub:
            text(ax, x + w / 2, y + h - 0.32, sub, size=5.9, color=GREY)
        # component icon
        ix, iy = x + w - 0.42, y + 0.14
        rect(ax, ix, iy, 0.28, 0.32, fc="white", ec=INK, lw=0.5)
        rect(ax, ix - 0.07, iy + 0.06, 0.14, 0.07, fc="white", ec=INK, lw=0.5)
        rect(ax, ix - 0.07, iy + 0.19, 0.14, 0.07, fc="white", ec=INK, lw=0.5)
        return (x, y, w, h)
    # packages
    def pkg(x, y, w, h, name, fc):
        rect(ax, x, y, w, h, fc=fc, ec=GREY, lw=0.8)
        rect(ax, x, y - 0.35, max(2.6, len(name) * 0.13), 0.35, fc=fc, ec=GREY, lw=0.8)
        text(ax, x + 0.12, y - 0.17, name, size=6.4, ha="left", weight="bold", color=GREY)
    pkg(0.4, 1.2, 12.1, 8.3, "Ask Nuki (pilot scope)", LANE2)
    pkg(12.9, 1.2, 4.7, 5.0, "VNUK existing systems", LANE)
    pkg(12.9, 6.8, 4.7, 2.7, "External (optional)", LANE)
    c_portal = comp(0.8, 1.6, 3.4, 1.5, "Student chat portal", "web UI, EN/VI")
    c_status = comp(0.8, 3.7, 3.4, 1.5, "Status + feedback page", "link in every email")
    c_dash = comp(0.8, 5.8, 3.4, 1.5, "Pilot log + admin", "KPIs, content gaps")
    c_flow = comp(4.9, 1.6, 3.3, 1.5, "Workflow + routing", "topic, owner office, rules")
    c_retr = comp(4.9, 3.7, 3.3, 1.5, "Retrieval gateway", "approved passages only")
    c_mon = comp(4.9, 5.8, 3.3, 1.5, "Audit + monitoring", "events, alerts")
    c_db = comp(8.9, 1.6, 3.2, 1.5, "Request database", "REQ-ID, status, history")
    c_kb = comp(8.9, 3.7, 3.2, 1.5, "Approved knowledge base", "source, owner, review date")
    c_hook = comp(8.9, 5.8, 3.2, 1.5, "Monitoring webhook", "alert to team chat")
    c_id = comp(13.3, 1.6, 3.9, 1.5, "Identity directory", "read-only account list / SSO")
    c_mail = comp(13.3, 3.95, 3.9, 1.5, "Institutional email", "office mailboxes")
    c_ai = comp(13.3, 7.4, 3.9, 1.5, "AI model API", "classify, draft; no training")
    # out of scope
    box(ax, 0.8, 7.85, 11.3, 1.25, "", fc="white", ec=MAROON, r=0.05, ls=(0, (4, 2)))
    text(ax, 6.45, 8.2, "Out of scope: EMS, LMS, grades, tuition and official academic records", size=6.6, color=MAROON, weight="bold")
    text(ax, 6.45, 8.65, "no interface; questions about them are routed to the owner office", size=6.1, color=MAROON)
    # dependencies (dashed, open arrow) with «use»
    def dep(p1, p2=None, lab=None, lx=None, ly=None):
        poly_arrow(ax, p1 if isinstance(p1, list) else [p1, p2], color=INK, lw=0.7, ls=(0, (4, 2)), head="->", ms=7)
        if lab:
            text(ax, lx, ly, lab, size=5.6, color=GREY)
    dep((4.2, 2.35), (4.9, 2.35))
    dep((6.55, 3.1), (6.55, 3.7))
    dep((8.2, 2.35), (8.9, 2.35))
    dep((8.2, 4.45), (8.9, 4.45))
    dep([(4.2, 4.45), (4.55, 4.45), (4.55, 2.7), (4.9, 2.7)])
    dep((8.2, 6.55), (8.9, 6.55))
    dep((4.2, 6.55), (4.9, 6.55))
    dep([(8.2, 1.95), (8.55, 1.95), (8.55, 1.45), (12.75, 1.45), (12.75, 1.85), (13.3, 1.85)])
    dep([(12.1, 2.7), (12.6, 2.7), (12.6, 4.7), (13.3, 4.7)])
    dep([(8.2, 4.95), (8.5, 4.95), (8.5, 7.6), (13.3, 7.6)])
    text(ax, 10.9, 7.42, "«use» passages only, no personal data", size=5.6, color=GREY)
    footnote(ax, 0.3, 9.95, "Notation: UML 2.5.1 component diagram (OMG, 2017). Boxes = components; dashed open arrows = «use» dependencies; tabbed frames = packages.")
    footnote(ax, 0.3, 10.3, "Every component sends events to audit + monitoring; identity, security and privacy controls apply to all. The request database replaces a bare request ID as the reusable core asset.")
    save(fig, f"{OUT}/fig_uml_component.png")


# ------------------------------------------------------------------ Stakeholder influence-impact grid
def stakeholder_grid():
    fig, ax = canvas(17, 11.4)
    text(ax, 0.3, 0.35, "Stakeholder influence–impact grid", size=8.5, ha="left", weight="bold", color=NAVY)
    x0, y0, w, h = 1.6, 1.0, 10.0, 8.6
    q = [("Keep satisfied", "brief on evidence; ask for decisions at gates", x0, y0, AMBERL),
         ("Manage closely", "co-own the pilot; named in the RACI as A", x0 + w / 2, y0, PINK),
         ("Monitor", "inform through the change story", x0, y0 + h / 2, LIGHT),
         ("Keep informed and involve", "POC testers; co-design and feedback", x0 + w / 2, y0 + h / 2, GREENL)]
    for name, sub, qx, qy, fc in q:
        rect(ax, qx, qy, w / 2, h / 2, fc=fc, ec="white", lw=1.5)
        text(ax, qx + 0.15, qy + 0.3, name, size=7.2, ha="left", weight="bold", color=NAVY)
        text(ax, qx + 0.15, qy + 0.62, sub, size=6.0, ha="left", color=GREY)
    arrow(ax, x0, y0 + h, x0 + w + 0.3, y0 + h, lw=1.0)
    arrow(ax, x0, y0 + h, x0, y0 - 0.3, lw=1.0)
    text(ax, x0 + w / 2, y0 + h + 0.45, "Impact of the change on the group's daily work  →", size=7, color=INK)
    text(ax, x0 - 0.45, y0 + h / 2, "Influence over the decision to implement  →", size=7, rot=90)
    text(ax, x0 + 0.1, y0 + h + 0.2, "low", size=6, color=GREY, ha="left"); text(ax, x0 + w - 0.1, y0 + h + 0.2, "high", size=6, color=GREY, ha="right")
    # stakeholders: (name, impact 0-1, influence 0-1, color)
    S = [("VNUK Director / Dean\n(sponsor)", 0.30, 0.84, MAROON, "D"),
         ("Head of Academic Affairs\n(content owner)", 0.86, 0.80, MAROON, "AA"),
         ("VNUK IT team +\nprivacy adviser", 0.62, 0.66, MAROON, "IT"),
         ("Heads of next offices\n(IT Support, Student Affairs,\nFinance, Assessment)", 0.18, 0.62, AMBER, "NO"),
         ("Office staff\n(POC testers)", 0.90, 0.34, GREEN, "OS"),
         ("Final-year students\n(POC testers)", 0.74, 0.22, GREEN, "ST"),
         ("Lecturers and\nfaculty advisers", 0.28, 0.30, GREY, "LF")]
    for name, im, inf, col, k in S:
        cx, cy = x0 + im * w, y0 + (1 - inf) * h
        ax.add_patch(Circle((cx, cy), 0.22, fc=col, ec="white", lw=1.0, zorder=4))
        dx = 0.35
        ha = "left"
        if k in ("OS", "AA"):
            ha, dx = "right", -0.35
        text(ax, cx + dx, cy, name, size=6.3, ha=ha, color=INK)
    # side panel: where they appear
    px = 12.3
    box(ax, px, 1.0, 4.4, 8.6, "", fc="white", ec=GREY, r=0.08)
    text(ax, px + 0.2, 1.35, "How the grid feeds the plan", size=7, ha="left", weight="bold", color=NAVY)
    lines = [("Manage closely", "Accountable (A) in the RACI;\nsign off Gate 1 inputs"),
             ("Keep satisfied", "Director decides Gates 1, 3, 4;\nnext offices join only when\ntheir readiness check passes"),
             ("Keep informed and\ninvolve", "Students and office staff are\nthe proof-of-concept testers;\nResponsible for testing tasks"),
             ("Monitor", "Change story and the\nmonthly evidence brief")]
    yy = 2.0
    for t1, t2 in lines:
        text(ax, px + 0.2, yy, t1, size=6.4, ha="left", weight="bold", color=INK, va="top")
        text(ax, px + 0.2, yy + (0.62 if "\n" in t1 else 0.36), t2, size=6.1, ha="left", color=GREY, va="top")
        yy += 1.95
    footnote(ax, 0.3, 10.55, "Grid type: influence/impact grid (PMI, 2017; see also Bourne & Walker, 2005; Ackermann & Eden, 2011). Positions are the team's judgement after")
    footnote(ax, 0.3, 10.9, "the Session 9 review, not survey data. Colour = engagement strategy.")
    save(fig, f"{OUT}/fig_stakeholder_grid.png")


# ------------------------------------------------------------------ Kotter 8 steps
def kotter():
    fig, ax = canvas(18, 10.6)
    text(ax, 0.3, 0.35, "Change management plan on Kotter's eight steps", size=8.5, ha="left", weight="bold", color=NAVY)
    steps = [("1", "Create urgency", "Evidence brief: 23 real requests,\n8 reply-all to a whole cohort,\nno FAQ page on vnuk.udn.vn", "Prepare"),
             ("2", "Build a guiding\ncoalition", "Director (sponsor), Head of\nAcademic Affairs, IT team lead,\nGroup 1 product team", "Prepare"),
             ("3", "Form vision\nand strategy", "\"Ask once: approved answer or\none tracked handoff.\" Non-AI\nservice first, AI only if it adds value", "Prepare"),
             ("4", "Communicate\nthe vision", "Change story for students and\nstaff; 15-min office walkthrough;\nonboarding in week 1", "Week 1"),
             ("5", "Remove\nobstacles", "Staff keep their email; one\nstatus link; read-only sign-in;\nguide template + backup owner", "Weeks 1–2"),
             ("6", "Generate\nshort-term wins", "Share first rated answers and\nfirst closed requests in the\nweekly evidence brief", "Week 2"),
             ("7", "Sustain\nacceleration", "Week-3 gate; expand to all\nfinal-year students and more\ngraduation-journey topics", "Wave 2 · expand"),
             ("8", "Anchor in\nculture", "Nuki in student onboarding;\nresponse window in office\nprocedure; review calendar", "Wave 3 · scale")]
    phases = [("Create a climate for change", 0, 3, PINK), ("Engage and enable the organisation", 3, 6, BLUE), ("Implement and sustain", 6, 8, GREENL)]
    pcol = {0: PINK, 1: PINK, 2: PINK, 3: BLUE, 4: BLUE, 5: BLUE, 6: GREENL, 7: GREENL}
    bw, gap, x0 = 4.15, 0.25, 0.35
    for k, (name, a_, b_, fc) in enumerate(phases):
        ax.add_patch(Rectangle((0.35 + k * 5.2, 0.75), 0.35, 0.3, fc=fc, ec="none"))
        text(ax, 0.8 + k * 5.2, 0.9, name, size=6.3, ha="left", color=NAVY, weight="bold")
    for i, (n, t, d, when) in enumerate(steps):
        r, c = divmod(i, 4)
        x = x0 + c * (bw + gap)
        y = 1.4 + r * 4.05
        box(ax, x, y, bw, 3.75, "", fc=pcol[i], ec=NAVY, r=0.12)
        ax.add_patch(Circle((x + 0.42, y + 0.5), 0.27, fc=MAROON, ec="none"))
        text(ax, x + 0.42, y + 0.5, n, size=7.5, color="white", weight="bold")
        text(ax, x + 0.85, y + 0.52, t.replace("\n", " "), size=6.9, ha="left", weight="bold", color=NAVY)
        text(ax, x + 0.25, y + 1.05, d, size=6.2, ha="left", va="top", color=INK)
        rect(ax, x, y + 3.15, bw, 0.6, fc="white", ec=NAVY, lw=0.9)
        text(ax, x + bw / 2, y + 3.45, when, size=6.4, color=MAROON, weight="bold")
        if c < 3:
            arrow(ax, x + bw + 0.02, y + 1.9, x + bw + gap - 0.02, y + 1.9, ms=7)
    footnote(ax, 0.3, 9.75, "Framework: Kotter (1995) eight-step model, grouped in three phases. Resistance responses follow Kotter and Schlesinger (2008); individual adoption")
    footnote(ax, 0.3, 10.1, "is tracked with ADKAR (Hiatt, 2006). Timing row links each step to the pilot roadmap and the expand and scale waves.")
    save(fig, f"{OUT}/fig_kotter.png")


# ------------------------------------------------------------------ Adoption roadmap gantt
def roadmap():
    fig, ax = canvas(18, 10.2)
    text(ax, 0.3, 0.35, "Three-week pilot adoption roadmap with decision owners", size=8.5, ha="left", weight="bold", color=NAVY)
    cols = ["Prepare\n(2 weeks before)", "Week 1\nEnable", "Week 2\nUse", "Week 3\nDecide"]
    lx, cx, cw = 0.3, 4.2, 3.3
    for i, c in enumerate(cols):
        rect(ax, cx + i * cw, 0.85, cw, 0.75, fc=NAVY, ec="white", lw=1.2)
        text(ax, cx + i * cw + cw / 2, 1.22, c, size=6.6, color="white", weight="bold")
    rows = [("VNUK Director / Dean", "sponsor · decides", MAROON),
            ("Head of Academic Affairs", "content owner", MAROON),
            ("VNUK IT team + privacy", "controls owner", MAROON),
            ("Office staff", "POC testers", GREEN),
            ("5 final-year students", "POC testers", GREEN),
            ("Group 1 product team", "Maddie, Tamas, Zsombi, Yuhan", NAVY)]
    ry0, rh = 1.75, 1.15
    for j, (n, s, col) in enumerate(rows):
        y = ry0 + j * rh
        rect(ax, lx, y, cx - lx - 0.1, rh - 0.1, fc=LANE, ec="none")
        rect(ax, lx, y, 0.12, rh - 0.1, fc=col, ec="none")
        text(ax, lx + 0.3, y + 0.38, n, size=6.6, ha="left", weight="bold")
        text(ax, lx + 0.3, y + 0.72, s, size=5.9, ha="left", color=GREY)
        for i in range(4):
            rect(ax, cx + i * cw, y, cw, rh - 0.1, fc="white", ec="#E5E7EB", lw=0.6)
    def bar(row, c0, c1, label, fc=BLUE, ec=NAVY):
        y = ry0 + row * rh + 0.18
        x = cx + c0 * cw + 0.1
        box(ax, x, y, (c1 - c0) * cw - 0.2, rh - 0.46, label, fc=fc, ec=ec, r=0.1, size=5.9)
    def gate(row, c, label):
        y = ry0 + row * rh + (rh - 0.1) / 2
        x = cx + c * cw
        ax.add_patch(Polygon([(x, y - 0.32), (x + 0.32, y), (x, y + 0.32), (x - 0.32, y)], fc=MAROON, ec="white", lw=1, zorder=5))
        text(ax, x, y + 0.5, label, size=5.8, color=MAROON, weight="bold")
    bar(0, 0, 0.85, "Approve scope,\nteam, budget", fc=PINK, ec=MAROON); gate(0, 1, "Gate 1")
    bar(0, 1.15, 3.55, "Receives weekly evidence brief", fc=LANE, ec=GREY); gate(0, 3.93, "")
    text(ax, cx + 3.93 * cw - 0.45, ry0 + 0.5, "Week-3\ndecision", size=5.8, color=MAROON, weight="bold", ha="right")
    bar(1, 0, 1, "Name owner; approve 24 guides", fc=PINK, ec=MAROON)
    bar(1, 1, 4, "Weekly content-gap review; approve fixes and FAQ pages", fc=PINK, ec=MAROON)
    bar(2, 0, 1, "Sign off account list + controls", fc=PINK, ec=MAROON)
    bar(2, 1, 4, "Monitoring alerts; incident response; privacy check at week 3", fc=LANE, ec=GREY)
    bar(3, 1, 2, "15-min walkthrough;\nclose a test case", fc=GREENL, ec=GREEN)
    bar(3, 2, 4, "Answer routed emails; log status; rate context\n(workload check end of week 2)", fc=GREENL, ec=GREEN)
    bar(4, 1, 2, "Onboarding; one guided\nquestion each", fc=GREENL, ec=GREEN)
    bar(4, 2, 4, "Real graduation-journey questions; rate answers;\nexit interview in week 3", fc=GREENL, ec=GREEN)
    bar(5, 0, 1, "Baseline; build; test set", fc=BLUE)
    bar(5, 1, 4, "Every week: test → feedback → backlog → fix → retest", fc=BLUE)
    footnote(ax, 0.3, 9.25, "Red = decision-makers (Manage closely / Keep satisfied); green = proof-of-concept testers. Diamonds = decision points. The week-3 decision uses the four")
    footnote(ax, 0.3, 9.6, "pilot numbers in the decision-logic figure. A five-student pilot tests usability and workflow fit; it is not evidence of university-wide impact.")
    save(fig, f"{OUT}/fig_roadmap.png")


# ------------------------------------------------------------------ Expand vs scale
def expand_scale():
    fig, ax = canvas(18, 9.7)
    text(ax, 0.3, 0.35, "Expand versus scale: what grows in each wave", size=8.5, ha="left", weight="bold", color=NAVY)
    depts = [("Academic Affairs", "11 of 23"), ("IT Support", "4 of 23"), ("Student Affairs", "4 of 23"), ("Finance", "2 of 23"), ("Assessment Unit", "re-marking")]
    users = ["All students\n(all years)", "All final-year\nCSE, IBM, BMS", "All final-year\nCSE students", "5 final-year CSE\nstudents (pilot)"]
    gx, gy, cw, ch = 3.4, 1.3, 2.25, 1.55
    for i, (d, n) in enumerate(depts):
        text(ax, gx + i * cw + cw / 2, gy + 4 * ch + 0.35, d, size=6.6, weight="bold")
        text(ax, gx + i * cw + cw / 2, gy + 4 * ch + 0.68, n + (" requests" if "of" in n else ""), size=5.8, color=GREY)
    for j, u in enumerate(users):
        text(ax, gx - 0.15, gy + j * ch + ch / 2, u, size=6.3, ha="right")
    def cell(i, j, fc, label="", ec="white"):
        rect(ax, gx + i * cw, gy + j * ch, cw, ch, fc=fc, ec=ec, lw=1.5)
        if label:
            text(ax, gx + i * cw + cw / 2, gy + j * ch + ch / 2, label, size=6.0, color=INK)
    for i in range(5):
        for j in range(4):
            cell(i, j, "#F3F4F6")
    cell(0, 3, MAROON); text(ax, gx + cw / 2, gy + 3 * ch + ch / 2, "Wave 1\nPROVE\n0–3 months", size=6.3, color="white", weight="bold")
    cell(0, 2, PINK, "Wave 2\nEXPAND"); cell(0, 1, PINK, "Wave 2\nEXPAND")
    for i in range(1, 5):
        cell(i, 1, GREENL, f"Wave 3\nSCALE\nunit {i + 1}")
    for i in range(0, 5):
        cell(i, 0, "#E9EEF6", "later: all years,\nafter evidence")
    # arrows
    arrow(ax, gx - 2.8, gy + 3.8 * ch, gx - 2.8, gy + 0.9 * ch, color=MAROON, lw=1.6, ms=11)
    text(ax, gx - 3.1, gy + 2.4 * ch, "EXPAND: more students and topics\nin a department already live", size=6.3, rot=90, color=MAROON, weight="bold")
    arrow(ax, gx + 1.05 * cw, gy - 0.35, gx + 5 * cw, gy - 0.35, color=GREEN, lw=1.6, ms=11)
    text(ax, gx + 3.0 * cw, gy - 0.6, "SCALE: replicate to the next department, one unit at a time, on the reusable core", size=6.3, color=GREEN, weight="bold")
    # side panel definitions
    px = gx + 5 * cw + 0.3
    pw = 18 - px - 0.2
    box(ax, px, 1.0, pw, 6.6, "", fc="white", ec=GREY, r=0.08)
    text(ax, px + 0.15, 1.3, "Definitions", size=7, ha="left", weight="bold", color=NAVY)
    text(ax, px + 0.15, 1.6, "Expand (Wave 2)\nsame department and\nsame core; more users\n(5 → all final-year,\n3 programmes) and more\ngraduation-journey topics;\nAI retrieval tested\nagainst the non-AI\nservice.", size=5.9, ha="left", va="top")
    text(ax, px + 0.15, 4.6, "Scale (Wave 3)\na new department joins as\na unit with its own guide\nowner, contacts, rules and\nresponse window; it reuses\nthe core unchanged.", size=5.9, ha="left", va="top")
    footnote(ax, 0.3, 8.65, "Unit of scale = one department (office) that owns a set of student questions. Order follows demand in the 23-request mailbox review, then readiness.")
    footnote(ax, 0.3, 9.0, "In Moore et al.'s (2015) terms, expanding and scaling are both scaling out; making Nuki the official front door in office procedures is scaling up;")
    footnote(ax, 0.3, 9.35, "changing how staff share and update answers is scaling deep. Each move needs the readiness check and gate in Section 8.")
    save(fig, f"{OUT}/fig_expand_scale.png")


# ------------------------------------------------------------------ DeLone & McLean measurement model
def delone():
    fig, ax = canvas(18, 10.4)
    text(ax, 0.3, 0.35, "Measurement model: KPIs mapped to the DeLone and McLean IS success model", size=8.5, ha="left", weight="bold", color=NAVY)
    def card(x, y, w, h, title, items, fc):
        box(ax, x, y, w, h, "", fc=fc, ec=NAVY, r=0.12)
        text(ax, x + 0.15, y + 0.32, title, size=7, ha="left", weight="bold", color=NAVY)
        text(ax, x + 0.15, y + 0.62, items, size=5.9, ha="left", va="top")
    card(0.4, 1.0, 5.0, 2.55, "System quality", "• Portal availability ≥ 99% in pilot hours\n• Outage alert reaches team < 5 min\n• 0 open duplicate routings\n• Median answer time < 10 s", LANE2)
    card(0.4, 3.85, 5.0, 2.55, "Information quality", "• ≥ 80% answers rated 4–5\n• 0 critical wrong guidance\n• 100% guides with source, owner,\n  review date; 0 expired guides", LANE2)
    card(0.4, 6.7, 5.0, 2.55, "Service quality", "• ≥ 80% correct office first time\n• Staff context rating ≥ 4 of 5\n• Requests closed within the\n  agreed response window [TBC]", LANE2)
    card(6.6, 1.0, 4.6, 3.6, "Use", "• Weekly active students / eligible\n• Share of questions asked in Nuki\n  vs. direct email (email audit)\n• Students who return after week 1\n• Staff status-link use per request", "white")
    card(6.6, 5.65, 4.6, 3.6, "User satisfaction", "• Student answer rating (1–5)\n  with a 'why?' on low scores\n• Student rating of staff reply\n• Staff rating of request context\n• Exit interview themes", "white")
    card(12.4, 2.5, 5.2, 5.4, "Net benefits", "Students\n• ≥ 75% answered without an office\n• Repeat contact within 7 days ↓\n• Time to confirmed answer ↓\n\nStaff\n• Minutes per request ≤ baseline,\n  incl. guide upkeep\n\nVNUK\n• Cost per resolved request\n• Net capacity value per month", GREENL)
    for yy in (2.27, 5.12, 7.97):
        ax.add_line(Line2D([5.4, 6.0], [yy, yy], color=INK, lw=0.8))
    ax.add_line(Line2D([6.0, 6.0], [2.27, 7.97], color=INK, lw=0.8))
    arrow(ax, 6.0, 2.8, 6.6, 2.8, lw=0.8, ms=7)
    arrow(ax, 6.0, 7.45, 6.6, 7.45, lw=0.8, ms=7)
    arrow(ax, 8.9, 4.6, 8.9, 5.65, head="<|-|>", lw=0.8, ms=7)
    arrow(ax, 11.2, 2.8, 12.4, 4.0, lw=0.8, ms=7)
    arrow(ax, 11.2, 7.45, 12.4, 6.4, lw=0.8, ms=7)
    arrow(ax, 15.0, 7.9, 15.0, 9.25, lw=0.8, ms=7, color=MAROON)
    poly_arrow(ax, [(15.0, 9.25), (8.9, 9.25)], color=MAROON, lw=0.8, ms=7)
    text(ax, 12.4, 9.45, "feedback loop: weekly review and gate decisions", size=6.0, color=MAROON)
    footnote(ax, 0.3, 9.85, "Model: DeLone and McLean (2003). Targets are proposed pilot thresholds, not measured VNUK baselines. Data source for every KPI: request-database events,")
    footnote(ax, 0.3, 10.18, "ratings, status links, monitoring logs and a two-week staff time sample.")
    save(fig, f"{OUT}/fig_delone.png")


# ------------------------------------------------------------------ Waves and gates timeline
def waves():
    fig, ax = canvas(18, 7.4)
    text(ax, 0.3, 0.35, "Three waves over 18 months, each opened by a stage gate", size=8.5, ha="left", weight="bold", color=NAVY)
    x0, x1 = 1.0, 17.4
    def mx(m):
        return x0 + (x1 - x0) * m / 18
    arrow(ax, x0, 5.4, x1 + 0.2, 5.4, lw=0.9)
    for m in range(0, 19, 3):
        ax.add_line(Line2D([mx(m), mx(m)], [5.3, 5.5], color=INK, lw=0.8))
        text(ax, mx(m), 5.75, f"{m} mo", size=6, color=GREY)
    W = [(0, 3, "Wave 1 · PROVE", "Academic Affairs;\n5 CSE final-year\nstudents; non-AI\nfirst; baseline", MAROON, 2.7),
         (3, 9, "Wave 2 · EXPAND", "Academic Affairs, all final-year students\n(CSE, IBM, BMS); more journey topics;\nAI retrieval tested vs non-AI", AMBER, 2.0),
         (9, 18, "Wave 3 · SCALE", "Next departments one by one: IT Support →\nStudent Affairs → Finance → Assessment Unit,\neach on the reusable core with its own owner", GREEN, 1.3)]
    for a, b, t, d, col, top in W:
        rect(ax, mx(a) + 0.05, top, mx(b) - mx(a) - 0.1, 5.2 - top, fc="white", ec=col, lw=1.2)
        rect(ax, mx(a) + 0.05, top, mx(b) - mx(a) - 0.1, 0.42, fc=col, ec=col)
        text(ax, mx(a) + 0.2, top + 0.21, t, size=6.6, ha="left", color="white", weight="bold")
        text(ax, mx(a) + 0.2, top + 0.6, d, size=5.8, ha="left", va="top")
    G = [(0, "G1", "Director:\npilot ready"), (3, "G2", "Service owner:\nAI test allowed"), (5.2, "G3", "Director:\nexpand approved"), (9, "G4", "Director: each\nnew department")]
    for m, g, lab in G:
        x = mx(m)
        ax.add_patch(Polygon([(x, 5.1), (x + 0.3, 5.4), (x, 5.7), (x - 0.3, 5.4)], fc=MAROON, ec="white", lw=1, zorder=5))
        text(ax, x, 6.2, g, size=6.4, weight="bold", color=MAROON)
        text(ax, x, 6.65, lab, size=5.6, color=GREY)
    footnote(ax, 0.3, 7.15, "Exit from a wave is evidence, not a date. Gate owners follow the RACI. G4 is repeated for every new department.")
    save(fig, f"{OUT}/fig_waves.png")


# ------------------------------------------------------------------ Week-3 decision logic
def decision():
    fig, ax = canvas(18, 6.6)
    ax.set_ylim(6.6, 0.9)
    start_event(ax, 0.8, 3.2)
    task(ax, 1.4, 2.6, 2.4, 1.2, "Service owner\nreviews 4 numbers\n+ ownership", icon="user")
    arrow(ax, 1.12, 3.2, 1.4, 3.2)
    gs = [(5.0, "Office owns the guides\nand students still use it?", "Stop", "End MVP; hand guides and\n23 cases to Academic Affairs", "no"),
          (8.6, "Zero critical wrong\nanswers?", "Pause AI", "Switch off AI answers; guides\nand email routing continue", "no"),
          (12.2, "Ratings ≥ 80%, routing ≥ 80%,\nstaff time not up?", "Pivot", "Fix the weak guide or route;\nretest for one more week", "no")]
    arrow(ax, 3.8, 3.2, 4.58, 3.2)
    for i, (x, q, out, act, lab) in enumerate(gs):
        gateway(ax, x, 3.2, s=0.42, label=q, lab_dy=-0.85)
        col = MAROON if out != "Pivot" else AMBER
        box(ax, x - 1.45, 4.55, 2.9, 1.15, "", fc="white", ec=col, r=0.12)
        text(ax, x, 4.8, out, size=6.8, weight="bold", color=col)
        text(ax, x, 5.3, act, size=5.8)
        arrow(ax, x, 3.62, x, 4.55, color=col)
        text(ax, x + 0.12, 4.05, lab, size=6, color=col, ha="left")
        nxt = gs[i + 1][0] - 0.42 if i < 2 else 14.8
        arrow(ax, x + 0.42, 3.2, nxt, 3.2)
        text(ax, x + 0.7, 3.02, "yes", size=6, color=GREEN)
    box(ax, 14.8, 2.55, 2.9, 1.3, "", fc=GREENL, ec=GREEN, r=0.12)
    text(ax, 16.25, 2.85, "Continue → Gate 2", size=6.8, weight="bold", color=GREEN)
    text(ax, 16.25, 3.4, "Keep Nuki live; prepare\nthe Wave 2 expansion", size=5.8)
    text(ax, 0.3, 1.25, "Week-3 decision logic: continue, pivot, pause AI or stop", size=8.5, ha="left", weight="bold", color=NAVY)
    footnote(ax, 0.3, 6.25, "Notation: BPMN 2.0 exclusive gateways (OMG, 2011). Checks run in order of severity, so ownership and safety failures are decided before performance targets.")
    save(fig, f"{OUT}/fig_decision.png")


# ------------------------------------------------------------------ Benefits dependency network
def bdn():
    fig, ax = canvas(18, 9.7)
    text(ax, 0.3, 0.35, "Benefits dependency network for Ask Nuki", size=8.5, ha="left", weight="bold", color=NAVY)
    cols = [("IS/IT enablers", ["Chat portal with\nread-only sign-in", "Approved knowledge\nbase + retrieval", "Request database,\nemail + status link", "Analytics and\nmonitoring"], BLUE),
            ("Enabling changes", ["Academic Affairs\napproves dated guides", "Offices agree routing\nrules + response window", "Students and staff\nonboarded"], LANE2),
            ("Business changes", ["Students ask in one\nplace first", "Offices answer routed\nrequests with one ID", "Weekly gap review;\nfrequent Qs → FAQ"], AMBERL),
            ("Benefits", ["Fewer repeat contacts;\nfaster confirmed answer", "Less clarifying and\nforwarding for staff", "Service data for\ndecisions"], GREENL),
            ("Objectives", ["Correct next step with\nless student effort", "Sustainable staff\nworkload", "Evidence-based\nscale decisions"], PINK)]
    cw, gap, x0 = 3.05, 0.42, 0.35
    pos = {}
    for i, (t, items, fc) in enumerate(cols):
        x = x0 + i * (cw + gap)
        text(ax, x + cw / 2, 1.05, t, size=7, weight="bold", color=NAVY)
        n = len(items)
        for j, it in enumerate(items):
            y = 1.5 + j * (7.0 / n) + (7.0 / n - 1.2) / 2
            box(ax, x, y, cw, 1.2, it, fc=fc, ec=NAVY, r=0.12, size=6.1)
            pos[(i, j)] = (x, y + 0.6)
    links = [((0, 0), (1, 2)), ((0, 1), (1, 0)), ((0, 2), (1, 1)), ((0, 3), (1, 1)),
             ((1, 0), (2, 0)), ((1, 2), (2, 0)), ((1, 1), (2, 1)), ((1, 0), (2, 2)), ((0, 3), (1, 2)),
             ((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 0)), ((2, 1), (3, 2)), ((2, 2), (3, 2)),
             ((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2))]
    for a, b in links:
        xa, ya = pos[a]; xb, yb = pos[b]
        arrow(ax, xa + cw, ya, xb, yb, lw=0.6, ms=6, color=GREY)
    footnote(ax, 0.3, 9.05, "Framework: benefits dependency network (Ward & Daniel, 2012). Read left to right: each benefit depends on the business and enabling")
    footnote(ax, 0.3, 9.35, "changes before it, not on the technology alone.")
    save(fig, f"{OUT}/fig_bdn.png")


# ------------------------------------------------------------------ charts
def charts():
    import matplotlib.pyplot as plt
    # requests by office
    fig = plt.figure(figsize=(16 / 2.54, 6.4 / 2.54), dpi=220)
    ax = fig.add_axes([0.24, 0.27, 0.7, 0.57])
    names = ["Academic Affairs", "IT Support", "Student Affairs", "Finance", "Faculty / lecturers"]
    vals = [11, 4, 4, 2, 2]
    ax.barh(names[::-1], vals[::-1], color=[GREY, GREY, NAVY, NAVY, MAROON], height=0.6)
    for i, v in enumerate(vals[::-1]):
        ax.text(v + 0.2, i, str(v), va="center", fontsize=7)
    ax.set_xlim(0, 13); ax.tick_params(labelsize=7); ax.set_xlabel("Requests (n = 23)", fontsize=7)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.text(0.02, 0.92, "Where 23 real academic requests went (one VNUK mailbox, 2022–2026)", fontsize=8.5, weight="bold", color=NAVY)
    fig.text(0.02, 0.04, "Other students anonymised; registration-portal overloads excluded. Small sample: shows routing pattern, not prevalence.", fontsize=6.2, style="italic", color=GREY)
    fig.savefig(f"{OUT}/fig_requests.png", dpi=220, facecolor="white"); plt.close(fig)
    # prioritisation
    fig = plt.figure(figsize=(16 / 2.54, 6.0 / 2.54), dpi=220)
    ax = fig.add_axes([0.36, 0.22, 0.58, 0.6])
    names = ["A. Student Support &\nAcademic Navigation", "C. Academic Progression\n& Milestones", "B. Practical Learning &\nResource Operations"]
    vals = [4.10, 3.80, 3.50]
    ax.barh(names[::-1], vals[::-1], color=[GREY, GREY, MAROON], height=0.55)
    for i, v in enumerate(vals[::-1]):
        ax.text(v + 0.04, i, f"{v:.2f}", va="center", fontsize=7)
    ax.plot([3.60], [2], marker="|", markersize=14, color=AMBER, mew=2)
    ax.text(3.6, 2.42, "3.60 if feasibility\nfalls from 4 to 2", fontsize=6, color=AMBER, ha="center")
    ax.set_xlim(3.0, 4.5); ax.tick_params(labelsize=7); ax.set_xlabel("Weighted score out of 5", fontsize=7)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.text(0.02, 0.92, "Weighted prioritisation of candidate domains (Session 3 criteria)", fontsize=8.5, weight="bold", color=NAVY)
    fig.text(0.02, 0.04, "Weights: value 30%, feasibility 25%, strategic relevance 20%, urgency 15%, learning value 10%. Team judgement, not measured returns.", fontsize=6.2, style="italic", color=GREY)
    fig.savefig(f"{OUT}/fig_priority.png", dpi=220, facecolor="white"); plt.close(fig)
    # break-even
    fig = plt.figure(figsize=(16 / 2.54, 7.0 / 2.54), dpi=220)
    ax = fig.add_axes([0.12, 0.2, 0.84, 0.62])
    N = np.linspace(0, 800, 200)
    gross = N * 0.40 * 8 * 100000 / 60 / 1e6
    net = gross - 2.0
    ax.plot(N, gross, color=NAVY, lw=1.4, label="Gross capacity value")
    ax.plot(N, net, color=MAROON, lw=1.6, label="Net value (after VND 2M/month cost)")
    ax.axhline(0, color=GREY, lw=0.7)
    ax.axvline(375, color=AMBER, lw=0.9, ls="--")
    ax.text(385, -1.6, "break-even ≈ 375\nenquiries / month", fontsize=6.3, color=AMBER)
    ax.axvline(120, color=GREY, lw=0.8, ls=":")
    ax.text(128, 2.6, "Wave 1 working\nbaseline ≈ 120", fontsize=6.3, color=GREY)
    ax.plot([500], [0.667], "o", color=MAROON, ms=3.5)
    ax.text(510, 0.2, "N = 500: +0.67M", fontsize=6.3, color=MAROON)
    ax.set_xlabel("Eligible enquiries per month (N)", fontsize=7); ax.set_ylabel("VND million / month", fontsize=7)
    ax.tick_params(labelsize=7); ax.legend(fontsize=6.3, frameon=False, loc="upper left")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.text(0.02, 0.92, "Illustrative break-even: why the pilot must expand beyond one cohort to pay back", fontsize=8.5, weight="bold", color=NAVY)
    fig.text(0.02, 0.04, "p = 0.40 self-served, t = 8 minutes saved, w = VND 100,000/hour, M + R = VND 2M/month. Scenario values, not a VNUK forecast.", fontsize=6.2, style="italic", color=GREY)
    fig.savefig(f"{OUT}/fig_breakeven.png", dpi=220, facecolor="white"); plt.close(fig)


if __name__ == "__main__":
    which = sys.argv[2:] or ["sequence", "component", "stakeholder_grid", "kotter", "roadmap", "expand_scale", "delone", "waves", "decision", "bdn", "charts"]
    for w in which:
        globals()[w]()


def value_tree():
    fig, ax = canvas(18, 11.3)
    text(ax, 0.3, 0.35, "Value-driver tree for Ask Nuki", size=8.5, ha="left", weight="bold", color=NAVY)
    def node(x, y, w, h, t, sub, fc, ec=NAVY):
        box(ax, x, y, w, h, "", fc=fc, ec=ec, r=0.12)
        text(ax, x + w / 2, y + 0.34, t, size=6.8, weight="bold", color=INK)
        if sub:
            text(ax, x + w / 2, y + h - 0.36, sub, size=5.8, color=GREY)
    def link(x1, y1, x2, y2):
        mx = (x1 + x2) / 2
        poly_arrow(ax, [(x1, y1), (mx, y1), (mx, y2), (x2, y2)], head="-", lw=0.8, color=GREY)
    node(0.4, 5.0, 3.0, 1.5, "Net service value", "per month, plus non-cash value", PINK, MAROON)
    # level 2
    L2 = [(1.85, "Capacity value (cash)", "N × p × t × w / 60", GREENL),
          (5.1, "Running cost (cash)", "M content + R technology", AMBERL),
          (7.5, "Student value (non-cash)", "effort and certainty", BLUE),
          (9.4, "Risk and trust", "must stay within limits", LANE2)]
    for y, t, sub, fc in L2:
        node(4.3, y, 3.4, 1.3, t, sub, fc)
        link(3.4, 5.75, 4.3, y + 0.65)
    # level 3 drivers with KPI
    L3 = [(1.55, 0, "Eligible enquiries N", "≈120 / month now; break-even ≈375"),
          (2.75, 0, "Self-service share p", "KPI: ≥75% answered without an office"),
          (3.95, 0, "Minutes saved t, staff cost w", "8 min; VND 100,000/h (scenario)"),
          (5.15, 1, "Guide upkeep M", "KPI: minutes per guide; 100% dated"),
          (6.35, 1, "Hosting + AI usage R", "FAQ pages cut AI tokens"),
          (7.55, 2, "Repeat contact, time to answer", "KPI: 7-day repeat contact ↓"),
          (8.75, 2, "Right office first time", "KPI: ≥80% → 90%"),
          (9.95, 3, "Critical wrong guidance", "KPI: 0, else pause AI")]
    parents = [1.85, 5.1, 7.5, 9.4]
    for y, p, t, sub in L3:
        node(8.6, y - 0.5, 4.6, 1.05, t, sub, "white")
        link(7.7, parents[p] + 0.65, 8.6, y + 0.02)
        box(ax, 13.6, y - 0.5, 4.0, 1.05, "", fc=LIGHT, ec="#D1D5DB", r=0.1)
    owners = ["Wave 2 expand, Wave 3 scale", "Head of AA + Maddie, weekly", "Service owner, staff time sample",
              "Content owners, monthly", "Zsombi, monthly", "Maddie, monthly", "Service owner, weekly", "Head of AA, immediate"]
    for (y, *_), o in zip(L3, owners):
        text(ax, 15.6, y + 0.02, o, size=5.9, color=INK)
    text(ax, 15.6, 0.75, "Lever and owner", size=6.6, weight="bold", color=NAVY)
    text(ax, 10.9, 0.75, "Driver and KPI", size=6.6, weight="bold", color=NAVY)
    footnote(ax, 0.3, 11.05, "Cash drivers use the report's break-even formula (Section 4.7.4); scenario values, not VNUK forecasts. Student value and risk are not converted into cash.")
    save(fig, f"{OUT}/fig_value_tree.png")
