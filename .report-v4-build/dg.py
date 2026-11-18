"""Small drawing helpers for report figures (matplotlib, data coordinates = cm-like units)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, Ellipse, FancyArrowPatch
from matplotlib.lines import Line2D

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 8

MAROON = "#891635"
NAVY = "#192F59"
INK = "#1F2430"
GREY = "#6B7280"
LIGHT = "#F3F4F6"
LANE = "#F7F8FB"
LANE2 = "#EEF1F7"
BLUE = "#D9EAF7"
PINK = "#F6E3E8"
GREEN = "#2E7D4F"
GREENL = "#E3F1E8"
AMBER = "#B26A00"
AMBERL = "#FBEFD9"


def canvas(w, h):
    fig = plt.figure(figsize=(w / 2.54, h / 2.54), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.invert_yaxis()
    ax.axis("off")
    return fig, ax


def save(fig, path):
    fig.savefig(path, dpi=220, facecolor="white")
    plt.close(fig)


def text(ax, x, y, s, size=8, color=INK, ha="center", va="center", weight="normal", style="normal", rot=0, wrap=None):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, fontweight=weight, fontstyle=style, rotation=rot, linespacing=1.25)


def box(ax, x, y, w, h, label="", fc="white", ec=INK, lw=0.9, r=0.18, size=7.5, color=INK, weight="normal", ls="-"):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw, ls=ls)
    ax.add_patch(p)
    if label:
        text(ax, x + w / 2, y + h / 2, label, size=size, color=color, weight=weight)
    return (x, y, w, h)


def rect(ax, x, y, w, h, fc="white", ec=INK, lw=0.8, ls="-"):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, ls=ls))


def arrow(ax, x1, y1, x2, y2, color=INK, lw=0.9, ls="-", head="-|>", ms=8, conn="arc3"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=head, mutation_scale=ms, color=color, lw=lw, ls=ls,
                        connectionstyle=conn, shrinkA=0, shrinkB=0)
    ax.add_patch(a)


def poly_arrow(ax, pts, color=INK, lw=0.9, ls="-", head="-|>", ms=8):
    """Orthogonal connector through points; arrowhead on last segment."""
    for (a, b) in zip(pts[:-2], pts[1:-1]):
        ax.add_line(Line2D([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls))
    arrow(ax, pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], color=color, lw=lw, ls=ls, head=head, ms=ms)


# ---- BPMN shapes ----
def start_event(ax, x, y, r=0.32, label=None):
    ax.add_patch(Circle((x, y), r, fc="white", ec=GREEN, lw=1.0))
    if label:
        text(ax, x, y + r + 0.32, label, size=6.3, color=GREY)


def end_event(ax, x, y, r=0.32, label=None):
    ax.add_patch(Circle((x, y), r, fc="white", ec=MAROON, lw=2.4))
    if label:
        text(ax, x, y + r + 0.32, label, size=6.3, color=GREY)


def timer_event(ax, x, y, r=0.34, label=None):
    ax.add_patch(Circle((x, y), r, fc="white", ec=INK, lw=0.8))
    ax.add_patch(Circle((x, y), r * 0.8, fc="white", ec=INK, lw=0.8))
    ax.add_patch(Circle((x, y), r * 0.55, fc="white", ec=INK, lw=0.6))
    ax.add_line(Line2D([x, x], [y, y - r * 0.45], color=INK, lw=0.6))
    ax.add_line(Line2D([x, x + r * 0.35], [y, y], color=INK, lw=0.6))
    if label:
        text(ax, x, y + r + 0.32, label, size=6.3, color=GREY)


def message_event(ax, x, y, r=0.34, label=None, throw=False):
    ax.add_patch(Circle((x, y), r, fc="white", ec=INK, lw=0.8))
    ax.add_patch(Circle((x, y), r * 0.8, fc="white", ec=INK, lw=0.8))
    w, h = r * 0.9, r * 0.6
    fc = INK if throw else "white"
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc=fc, ec=INK, lw=0.6))
    ax.add_line(Line2D([x - w / 2, x, x + w / 2], [y - h / 2, y + h * 0.05, y - h / 2], color="white" if throw else INK, lw=0.6))
    if label:
        text(ax, x, y + r + 0.32, label, size=6.3, color=GREY)


def gateway(ax, x, y, s=0.42, label=None, kind="x", lab_dy=-0.62):
    ax.add_patch(Polygon([(x, y - s), (x + s, y), (x, y + s), (x - s, y)], closed=True, fc="white", ec=AMBER, lw=1.0))
    d = s * 0.38
    if kind == "x":
        ax.add_line(Line2D([x - d, x + d], [y - d, y + d], color=AMBER, lw=1.2))
        ax.add_line(Line2D([x - d, x + d], [y + d, y - d], color=AMBER, lw=1.2))
    elif kind == "+":
        ax.add_line(Line2D([x - d * 1.3, x + d * 1.3], [y, y], color=AMBER, lw=1.2))
        ax.add_line(Line2D([x, x], [y - d * 1.3, y + d * 1.3], color=AMBER, lw=1.2))
    if label:
        text(ax, x, y + lab_dy, label, size=6.3, color=GREY)


def task(ax, x, y, w, h, label, fc="white", ec=NAVY, size=6.2, icon=None):
    box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=0.9, r=0.16)
    text(ax, x + w / 2 + (0.07 if icon else 0), y + h / 2 + (0.04 if icon else 0), label, size=size)
    ix, iy = x + 0.15, y + 0.15
    if icon == "user":
        ax.add_patch(Circle((ix, iy - 0.02), 0.045, fc="none", ec=GREY, lw=0.45))
        ax.add_patch(Polygon([(ix - 0.08, iy + 0.12), (ix + 0.08, iy + 0.12), (ix + 0.06, iy + 0.04), (ix - 0.06, iy + 0.04)], fc="none", ec=GREY, lw=0.45))
    elif icon == "service":
        ax.add_patch(Circle((ix, iy + 0.02), 0.07, fc="none", ec=GREY, lw=0.5))
        ax.add_patch(Circle((ix, iy + 0.02), 0.025, fc=GREY, ec=GREY, lw=0.3))
    elif icon == "send":
        ax.add_patch(Rectangle((ix - 0.08, iy - 0.04), 0.17, 0.12, fc=INK, ec=INK, lw=0.3))
    return (x, y, w, h)


def datastore(ax, x, y, w=1.1, h=0.9, label=None):
    e = 0.18
    ax.add_patch(Rectangle((x, y + e / 2), w, h - e, fc="white", ec=INK, lw=0.8))
    ax.add_patch(Ellipse((x + w / 2, y + h - e / 2), w, e, fc="white", ec=INK, lw=0.8))
    ax.add_patch(Rectangle((x + 0.01, y + e / 2), w - 0.02, h - e - 0.02, fc="white", ec="none"))
    ax.add_patch(Ellipse((x + w / 2, y + e / 2), w, e, fc="white", ec=INK, lw=0.8))
    ax.add_line(Line2D([x, x], [y + e / 2, y + h - e / 2], color=INK, lw=0.8))
    ax.add_line(Line2D([x + w, x + w], [y + e / 2, y + h - e / 2], color=INK, lw=0.8))
    if label:
        text(ax, x + w / 2, y + h + 0.3, label, size=6.2, color=GREY)


def message_flow(ax, pts, label=None, lx=None, ly=None):
    for (a, b) in zip(pts[:-2], pts[1:-1]):
        ax.add_line(Line2D([a[0], b[0]], [a[1], b[1]], color=GREY, lw=0.8, ls=(0, (4, 2))))
    a, b = pts[-2], pts[-1]
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=8, color=GREY, lw=0.8, ls=(0, (4, 2)), shrinkA=0, shrinkB=0, fc="white"))
    ax.add_patch(Circle(pts[0], 0.06, fc="white", ec=GREY, lw=0.7, zorder=5))
    if label:
        text(ax, lx, ly, label, size=6, color=GREY, style="italic")


def assoc(ax, pts):
    for (a, b) in zip(pts[:-1], pts[1:]):
        ax.add_line(Line2D([a[0], b[0]], [a[1], b[1]], color=GREY, lw=0.7, ls=(0, (1, 1.5))))


def footnote(ax, x, y, s):
    text(ax, x, y, s, size=6.2, color=GREY, ha="left", style="italic")
