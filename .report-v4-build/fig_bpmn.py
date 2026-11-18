import sys
from dg import *

OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def pool(ax, y, h, name, x0=0.3, x1=17.7, fc=LANE):
    rect(ax, x0, y, x1 - x0, h, fc=fc, ec=INK, lw=0.8)
    rect(ax, x0, y, 0.7, h, fc="white", ec=INK, lw=0.8)
    text(ax, x0 + 0.35, y + h / 2, name, size=6.8, rot=90, weight="bold", color=NAVY)


def to_be():
    fig, ax = canvas(18, 14.9)
    text(ax, 0.3, 0.35, "To-be process: academic enquiry from question to closure (BPMN 2.0 collaboration diagram)", size=8.5, ha="left", weight="bold", color=NAVY)
    pool(ax, 0.8, 2.6, "Student")
    pool(ax, 3.6, 4.8, "Ask Nuki portal\n(VNUK system)", fc=LANE2)
    pool(ax, 8.6, 2.6, "Department office")
    pool(ax, 11.4, 2.5, "Content owner +\nproduct team")
    H = 1.0
    # ---------- Student ----------
    sy = 2.1
    start_event(ax, 1.55, sy, label="Question arises")
    task(ax, 2.2, sy - H/2, 1.75, H, "Sign in with\nVNUK account", icon="user")
    task(ax, 4.3, sy - H/2, 1.75, H, "Ask question\n(EN or VI)", icon="user")
    task(ax, 9.5, sy - H/2, 1.85, H, "Read answer,\nrate it 1–5", icon="user")
    end_event(ax, 12.0, sy, label="Answered")
    task(ax, 13.3, sy - H/2, 1.85, H, "Read staff reply,\nrate it 1–5", icon="user")
    end_event(ax, 16.9, sy, label="Closed")
    arrow(ax, 1.87, sy, 2.2, sy); arrow(ax, 3.95, sy, 4.3, sy)
    arrow(ax, 11.35, sy, 11.68, sy); arrow(ax, 15.15, sy, 16.58, sy)
    # ---------- Nuki ----------
    ny = 4.85
    task(ax, 2.2, ny - H/2, 1.75, H, "Verify account\n(read-only list)", icon="service")
    task(ax, 4.3, ny - H/2, 1.95, H, "Classify topic,\nretrieve approved\nguidance", icon="service")
    gateway(ax, 7.0, ny, label="Enough approved evidence and\nnot an official decision?", lab_dy=-0.82)
    task(ax, 7.8, ny - H/2, 1.75, H, "Show answer\nwith source, owner,\nreview date", icon="service")
    task(ax, 10.0, ny - H/2, 1.85, H, "Log rating; low\nor unanswered\ngoes to gap queue", icon="service")
    end_event(ax, 12.45, ny)
    arrow(ax, 3.95, ny, 4.3, ny); arrow(ax, 6.25, ny, 6.58, ny); arrow(ax, 7.42, ny, 7.8, ny)
    text(ax, 7.6, ny - 0.2, "yes", size=6, color=GREEN)
    arrow(ax, 9.55, ny, 10.0, ny); arrow(ax, 11.85, ny, 12.13, ny)
    ry = 7.05
    task(ax, 7.8, ry - H/2, 1.75, H, "Create request\nID, email office\n(student copied)", icon="send")
    poly_arrow(ax, [(7.0, ny + 0.42), (7.0, ry), (7.8, ry)])
    text(ax, 6.85, ny + 1.15, "no", size=6, color=MAROON, ha="right")
    task(ax, 10.0, ry - H/2, 1.9, H, "Track status\nof request", icon="service")
    arrow(ax, 9.55, ry, 10.0, ry)
    timer_event(ax, 11.6, ry + 0.5, r=0.25)
    task(ax, 10.0, 7.95, 1.45, 0.34, "Send reminder", size=6)
    poly_arrow(ax, [(11.6, ry + 0.75), (11.6, 8.12), (11.45, 8.12)], ms=6)
    poly_arrow(ax, [(10.0, 8.12), (9.8, 8.12), (9.8, ry + 0.25), (10.0, ry + 0.25)], ms=6)
    text(ax, 11.88, 7.95, "after 2 days", size=6, color=GREY, ha="left")
    task(ax, 12.6, ry - H/2, 1.85, H, "Close request,\ninvite student\nrating", icon="service")
    arrow(ax, 11.9, ry, 12.6, ry)
    end_event(ax, 15.15, ry)
    arrow(ax, 14.45, ry, 14.83, ry)
    datastore(ax, 4.8, 6.25, 1.0, 0.8)
    text(ax, 4.65, 6.65, "Approved\nknowledge base", size=6.2, color=GREY, ha="right")
    assoc(ax, [(5.3, 6.25), (5.3, ny + H/2)])
    datastore(ax, 5.95, 7.3, 0.9, 0.7)
    text(ax, 5.8, 7.65, "Request\ndatabase", size=6.2, color=GREY, ha="right")
    assoc(ax, [(6.85, 7.65), (7.8, 7.4)])
    # ---------- Office ----------
    oy = 9.95
    message_event(ax, 8.65, oy, label="Routed email")
    task(ax, 9.4, oy - H/2, 1.95, H, "Reply to student\nin normal email\n(AI draft optional)", icon="user")
    task(ax, 11.8, oy - H/2, 1.95, H, "Log status, rate\ncontext via link\nin email", icon="user")
    end_event(ax, 14.5, oy, label="Resolved")
    arrow(ax, 8.99, oy, 9.4, oy); arrow(ax, 11.35, oy, 11.8, oy); arrow(ax, 13.75, oy, 14.18, oy)
    # ---------- Content ----------
    cy = 12.65
    timer_event(ax, 1.55, cy, r=0.3, label="Weekly")
    task(ax, 2.2, cy - H/2, 2.0, H, "Review ratings,\ngaps and KPIs", icon="user")
    task(ax, 4.7, cy - H/2, 2.3, H, "Approve or update\nguidance in the\nknowledge base", icon="user")
    gateway(ax, 7.75, cy, label="Asked often?", lab_dy=-0.68)
    task(ax, 8.6, cy - H/2, 1.9, H, "Publish as plain\nFAQ page", icon="user")
    end_event(ax, 11.2, cy)
    arrow(ax, 1.85, cy, 2.2, cy); arrow(ax, 4.2, cy, 4.7, cy); arrow(ax, 7.0, cy, 7.33, cy)
    arrow(ax, 8.17, cy, 8.6, cy); arrow(ax, 10.5, cy, 10.88, cy)
    text(ax, 8.38, cy - 0.2, "yes", size=6, color=GREEN)
    poly_arrow(ax, [(7.75, cy + 0.42), (7.75, cy + 0.72), (11.2, cy + 0.72), (11.2, cy + 0.32)], ms=6)
    text(ax, 7.95, cy + 0.6, "no", size=6, color=MAROON, ha="left")
    # ---------- message flows ----------
    message_flow(ax, [(3.07, sy + H/2), (3.07, ny - H/2)])
    message_flow(ax, [(5.17, sy + H/2), (5.17, ny - H/2)])
    message_flow(ax, [(8.68, ny - H/2), (8.68, 3.05), (9.95, 3.05), (9.95, sy + H/2)], label="answer card", lx=8.75, ly=2.88)
    message_flow(ax, [(10.9, sy + H/2), (10.9, ny - H/2)], label="rating", lx=11.3, ly=3.35)
    message_flow(ax, [(8.65, ry + H/2), (8.65, oy - 0.34)])
    message_flow(ax, [(10.35, oy - H/2), (10.35, 9.05), (15.7, 9.05), (15.7, 2.95), (14.9, 2.95), (14.9, sy + H/2)], label="reply email (cc)", lx=14.9, ly=8.88)
    message_flow(ax, [(13.3, oy - H/2), (13.3, ry + H/2)], label="status", lx=13.6, ly=8.3)
    message_flow(ax, [(13.9, ry - H/2), (13.9, sy + H/2)], label="rate-your-\nanswer email", lx=14.1, ly=4.2)
    message_flow(ax, [(11.2, ny + H/2), (11.2, 5.75), (2.95, 5.75), (2.95, cy - H/2)], label="gap queue", lx=3.1, ly=5.95)
    footnote(ax, 0.3, 14.25, "Notation: BPMN 2.0 (OMG, 2011). Pools = participants; solid arrows = sequence flow; dashed arrows = message flow; dotted lines = data association;")
    footnote(ax, 0.3, 14.6, "thin circle = start event; thick circle = end event; double circle = timer or message event; diamond with X = exclusive gateway; cylinder = data store.")
    save(fig, f"{OUT}/fig_bpmn_tobe.png")


def as_is():
    fig, ax = canvas(18, 9.6)
    text(ax, 0.3, 0.35, "As-is process: how a final-year student gets an academic answer today (BPMN 2.0)", size=8.5, ha="left", weight="bold", color=NAVY)
    pool(ax, 0.8, 3.9, "Student")
    pool(ax, 4.9, 3.6, "Lecturers, peers\nand offices")
    sy = 2.55
    start_event(ax, 1.55, sy, label="Question arises")
    task(ax, 2.2, sy - 0.45, 1.8, 0.9, "Search old\nnotices\nand emails", icon="user")
    arrow(ax, 1.87, sy, 2.2, sy); arrow(ax, 4.0, sy, 4.18, sy)
    gateway(ax, 4.6, sy, kind="+", label="tries several\nchannels at once", lab_dy=-0.95)
    ys = [1.35, 2.55, 3.75]
    labels = ["Email a lecturer\nor adviser", "Reply-all to the\ncohort list", "Walk to an office\nor ask friends"]
    for yy, lb in zip(ys, labels):
        task(ax, 5.6, yy - 0.42, 1.9, 0.84, lb, icon="user")
        if yy == sy:
            arrow(ax, 5.02, sy, 5.6, sy); arrow(ax, 7.5, sy, 8.45, sy)
        else:
            poly_arrow(ax, [(5.02, sy), (5.1, sy), (5.1, yy), (5.6, yy)], ms=6)
            poly_arrow(ax, [(7.5, yy), (8.1, yy), (8.1, sy), (8.45, sy)], ms=6)
    gateway(ax, 8.87, sy, kind="x")
    task(ax, 9.8, sy - 0.45, 1.8, 0.9, "Wait; no ID,\nno visible owner", icon="user")
    arrow(ax, 9.29, sy, 9.8, sy)
    gateway(ax, 12.3, sy, label="Clear answer?", lab_dy=-0.7)
    arrow(ax, 11.6, sy, 11.88, sy)
    task(ax, 13.2, sy - 0.45, 1.8, 0.9, "Act on answer", icon="user")
    arrow(ax, 12.72, sy, 13.2, sy)
    text(ax, 12.95, sy - 0.2, "yes", size=6, color=GREEN)
    end_event(ax, 16.3, sy, label="Done (no record)")
    arrow(ax, 15.0, sy, 15.98, sy)
    poly_arrow(ax, [(12.3, sy + 0.42), (12.3, 4.4), (3.1, 4.4), (3.1, sy + 0.45)], color=MAROON, ms=7)
    text(ax, 9.9, 4.22, "no: ask again in another channel (repeat contact)", size=6.2, color=MAROON)
    oy = 6.4
    message_event(ax, 5.0, oy, label="Message arrives")
    task(ax, 5.8, oy - 0.45, 2.0, 0.9, "Check if it is\nmy office's topic", icon="user")
    gateway(ax, 8.6, oy, label="Mine?", lab_dy=-0.65)
    task(ax, 9.5, oy - 0.45, 2.0, 0.9, "Answer from\nmemory or past\nemails", icon="user")
    task(ax, 9.5, 7.35, 2.0, 0.75, "Forward to\nanother office", icon="user")
    arrow(ax, 5.34, oy, 5.8, oy); arrow(ax, 7.8, oy, 8.18, oy); arrow(ax, 9.02, oy, 9.5, oy)
    text(ax, 9.25, oy - 0.2, "yes", size=6, color=GREEN)
    poly_arrow(ax, [(8.6, oy + 0.42), (8.6, 7.72), (9.5, 7.72)], ms=6)
    text(ax, 8.75, 7.55, "no", size=6, color=MAROON, ha="left")
    end_event(ax, 12.2, oy)
    arrow(ax, 11.5, oy, 11.88, oy)
    poly_arrow(ax, [(11.5, 7.72), (12.2, 7.72), (12.2, oy + 0.32)], ms=6)
    message_flow(ax, [(6.2, 3.75 + 0.42), (6.2, 5.25), (5.0, 5.25), (5.0, oy - 0.34)])
    message_flow(ax, [(10.5, oy - 0.45), (10.5, sy + 0.45)], label="reply, if any", lx=11.15, ly=5.3)
    footnote(ax, 0.3, 9.0, "Notation: BPMN 2.0 (OMG, 2011). Pain points from interviews and the 23-request mailbox review: no request ID, unclear owner, repeat contact,")
    footnote(ax, 0.3, 9.33, "forwarding between offices. Symbols as in the to-be diagram.")
    save(fig, f"{OUT}/fig_bpmn_asis.png")


if __name__ == "__main__":
    to_be()
    as_is()
