#!/usr/bin/env python3
"""Builds deck.html (1280x720 px slides, which print to 960x540 pt pages; inline SVG charts; images by relative path) for
the gadgets pitch deck v4.

Run: python3 -I build_deck.py   (writes deck.html next to this file; images/ comes from prepare_images.py)
v2 (27 Nov 2026): the flagship is the brand concept itself, one premium brand with a multi-category collection of
decorations, gadgets and other objects for the home.
v3 (27 Nov 2026, Oscar's ask: "get Claude to research the whole world, market size by region, then break the total up like
the bottom-up"): the market slide became two slides (the world by region; the households-to-customers funnel with Spain,
France and Germany as the beachhead), plus label-collision fixes on the price ladder, the competition map and the token chart.
v4 (27 Nov 2026, Oscar's ask: update the deck with the saved X posts in ../inspiration/): new slide 4, a moodboard of the
posts the founder keeps saving, with captions, categories, a credit per image and the patterns (observations, never a market
measurement); tie-ins on the brand (slide 3), collection (5), funnel (7) and competition (8) slides; all 29 post URLs in the
appendix. v3's slides 4 to 10 are now 5 to 11 with their content, numbers and layout unchanged. The POSTS block holds the posts.
Layout fix (27 Nov 2026, after Innovator's first render of v4, measured on that PDF): slide 7's right column is tightened so the
observation tile clears the footer (class "tight": table rows without wrapped region names, smaller paddings, the funnel canvas
740 px wide instead of 790, the observation cut to one sentence of two readings); slide 4's moodboard images are 92 px tall and its
patterns label is one line shorter; slide 3's credit lines get room; slides 5 and 7 (two-line titles) start their body 10 px lower
(class "t2"), slide 5's price ladder is 176 px tall to make that room. No number changed.
Update (28 Nov 2026, Oscar's ask: add the two posts he sent on the evening of 27 Nov, both in the inspiration list's Displays and
e-ink category; the same morning the five Wall and decor posts left the inspiration list at Oscar's request): 26 posts, six
categories. On the moodboard the e-ink tablet and the ESP32 AMOLED board replace the AirPlay board and the dropped illustration;
the water gun keeps its place (the AirPlay board stays cited in the patterns and the appendix), so the card grid keeps its size.
The e-ink pattern rests on two posts and the cheap-hardware pattern on six; the hand-made pattern is 8 of 26 (art objects only);
the lighting gap is one sentence shorter. Measured on Innovator's render of 27 Nov (right column 21 lines, ending 21 px above the
footer rule): the column is now 20 lines and the category chart one row shorter. Slide 5: the e-ink display's one-liner says
"saved posts". Slide 7: the observation gains a third reading and a third citation (its tile ended 65 px above the rule).
Appendix: 26 post URLs. No number changed.
Update (28 Nov 2026, later the same morning, Oscar's ask: add The Scout, @kinglycrow, a magnetic Wi-Fi camera listed at $25 in the
post, Desk gadgets on the inspiration list; while that was being built the list also gained the @audrlo post, 3D-printed robot-head
prototypes grown into a production home device, Desk gadgets too): 28 posts, six categories. On the moodboard the camera takes cell
10 from the bronze figures (Art objects keeps the ceramic ashtray in cell 9; the figures stay cited in the hand-made pattern and the
appendix), so the card grid keeps its size. The cheap-hardware pattern rests on seven posts, the wider-market pattern cites the
@audrlo post, the hand-made pattern is 8 of 28, the count chart's Desk gadgets row says 8; the pattern lines keep their line counts,
so the right column keeps its 20 lines. Slide 7: the observation tile gains one citation (the camera) and loses one word. Appendix:
28 post URLs. No number changed.
All numbers live in this file and in research.md (section 7 for the market work, section 8 for the posts) with their sources.
Every footnote number is generated from the SRC registry below in order of first use; a star after the number marks a
source that was seen in a search snippet only (unverified). Placeholders are marked [placeholder].
No external assets beyond images/: fonts are system fonts, charts are inline SVG, images are relative paths, so the file
prints to PDF with headless Chrome opened from file://.
"""
import html
import math
import os
from datetime import datetime, timezone

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck.html")

# ---------------------------------------------------------------- style tokens (Oscar restyles later)
PAPER = "#f6f3ec"      # slide surface, warm paper
PANEL = "#fbf9f4"      # card surface
INK = "#17150f"        # primary ink
INK2 = "#5b5750"       # secondary ink
MUTED = "#8d8980"      # axis labels, footnotes
HAIR = "#d9d3c6"       # hairlines, grid
ACCENT = "#b8371f"     # lacquer red, the one accent
GREY_MARK = "#a8a398"  # recessive marks for "others"
DARK_MARK = "#3a3630"  # second category mark
WOOD = "#c9a27a"       # object renders only
WOOD_D = "#8a6240"
WARM = "#e8c26a"       # light in object renders
SERIF = "Georgia, 'Liberation Serif', 'DejaVu Serif', 'Times New Roman', serif"
SANS = "'Inter', 'Helvetica Neue', Helvetica, Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif"

BRAND = "[Brand name placeholder]"
DRAFT_LINE = "v4 draft for Oscar's edit, 27 Nov 2026. Private. Not for distribution."

# ---------------------------------------------------------------- source registry
# key: (label, url, date, tag). tag: "v" opened and read, "s" search snippet only (unverified), "d" derived from sourced inputs.
SRC = {}
USED = []   # keys in order of first citation


def reg(key, label, url, date, tag="v"):
    SRC[key] = (label, url, date, tag)


def num(key):
    if key not in SRC:
        raise KeyError(f"unregistered source {key}")
    if key not in USED:
        USED.append(key)
    return USED.index(key) + 1


def star(key):
    return "*" if SRC[key][3] == "s" else ""


def cite(*keys):
    """Plain-text citation for SVG notes, e.g. [3, 7*]."""
    return "[" + ",".join(f"{num(k)}{star(k)}" for k in keys) + "]"   # no spaces, so a citation never splits across lines


def fn(*keys):
    """HTML footnote marker."""
    return '<sup class="fn">' + ", ".join(f"{num(k)}{star(k)}" for k in keys) + "</sup>"


def esc(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- SVG primitives
def svg(w, h, inner, extra_class=""):
    return (f'<svg class="{extra_class}" xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{esc(SANS)}">{inner}</svg>')


def txt(x, y, s, size=12, fill=INK, anchor="start", weight=400, family=None, extra="", italic=False):
    fam = f' font-family="{esc(family)}"' if family else ""
    it = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{fam}{it} {extra}>{esc(s)}</text>')


def line(x1, y1, x2, y2, stroke=HAIR, width=1, extra=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{width}" {extra}/>'


def rect(x, y, w, h, fill, rx=0, stroke="none", sw=1, extra=""):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,0):.1f}" height="{max(h,0):.1f}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def circle(cx, cy, r, fill, stroke="none", sw=1, extra=""):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def path(d, stroke=INK, fill="none", width=2, extra=""):
    return f'<path d="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def arrow_defs(color=INK2, name="arr"):
    return (f'<defs><marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 1 1 L 9 5 L 1 9" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>')


def arrow(x1, y1, x2, y2, stroke=INK2, width=1.5, name="arr"):
    return line(x1, y1, x2, y2, stroke, width, f'marker-end="url(#{name})"')


def wrap(s, max_chars):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def box(x, y, w, h, title, sub=None, fill=PANEL, stroke=HAIR, accent=False, size=13, subsize=11, dashed=False, title_weight=600, title_fill=None):
    """Rounded node with a title and optional sub-line, text wrapped to fit."""
    out = [rect(x, y, w, h, fill, rx=6, stroke=(ACCENT if accent else stroke), sw=(1.5 if accent else 1),
                extra=('stroke-dasharray="4 3"' if dashed else ""))]
    maxc = max(6, int(w / (size * 0.56)))
    tl = wrap(title, maxc)
    sl = wrap(sub, max(6, int(w / (subsize * 0.56)))) if sub else []
    total = len(tl) * (size + 3) + (len(sl) * (subsize + 3) + 4 if sl else 0)
    yy = y + h / 2 - total / 2 + size
    for t in tl:
        out.append(txt(x + w / 2, yy, t, size, title_fill or (ACCENT if accent else INK), "middle", title_weight))
        yy += size + 3
    if sl:
        yy += 4
        for t in sl:
            out.append(txt(x + w / 2, yy, t, subsize, INK2, "middle"))
            yy += subsize + 3
    return "".join(out)


def note_lines(note, w, size=10):
    return wrap(note, max(20, int(w / (size * 0.56)))) if note else []


def draw_note(out, note, w, h, size=10):
    lines = note_lines(note, w, size)
    for i, ln in enumerate(reversed(lines)):
        out.append(txt(0, h - 4 - i * (size + 2), ln, size, MUTED))
    return len(lines) * (size + 2) + 4 if lines else 0


def fmt_num(v):
    if v >= 1e9:
        return f"{v/1e9:.1f}B".replace(".0B", "B")
    if v >= 1e6:
        return f"{v/1e6:.0f}M"
    if v >= 1e3:
        return f"{v/1e3:.0f}k"
    return f"{v:g}"


# ---------------------------------------------------------------- charts
def chart_line_log(w, h, series, y_ticks, x_ticks, title, unit_label, note=None, pad=(14, 40, 44, 50)):
    top, right, bottom, left = pad
    bottom = max(bottom, 30 + len(note_lines(note, w)) * 12 + 6)   # tick labels, then the caption, with a clear gap
    px0, px1 = left, w - right
    py0, py1 = top + 18, h - bottom
    xs = [p[0] for s in series for p in s["pts"]]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = y_ticks[0], y_ticks[-1]

    def X(v):
        return px0 + (v - xmin) / (xmax - xmin) * (px1 - px0)

    def Y(v):
        return py1 - (math.log10(v) - math.log10(ymin)) / (math.log10(ymax) - math.log10(ymin)) * (py1 - py0)

    out = [txt(0, 12, title, 12, INK, weight=600)]
    for t in y_ticks:
        out.append(line(px0, Y(t), px1, Y(t), HAIR, 1))
        out.append(txt(px0 - 6, Y(t) + 4, f"${t:g}", 10, MUTED, "end"))
    for xv, lab in x_ticks:
        out.append(txt(X(xv), py1 + 14, lab, 10, MUTED, "middle"))
    out.append(line(px0, py1, px1, py1, "#c3bfb4", 1))
    out.append(txt(0, py0 - 6, unit_label, 10, MUTED, "start"))
    for s in series:
        pts = sorted(s["pts"])
        d = " ".join(f"{'M' if i == 0 else 'L'} {X(x):.1f} {Y(y):.1f}" for i, (x, y, *_) in enumerate(pts))
        out.append(path(d, s["color"], width=2))
        for x, y, *lab in pts:
            out.append(circle(X(x), Y(y), 4, s["color"], PAPER, 2))
            if lab and lab[0]:
                if X(x) > px0 + 0.75 * (px1 - px0):
                    out.append(txt(X(x) - 8, Y(y) - 9, lab[0], 10, INK2, "end"))
                else:
                    out.append(txt(X(x) + 7, Y(y) - 7, lab[0], 10, INK2))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_bars(w, h, cats, vals, title, unit, color=ACCENT, highlight_last=False, note=None, value_fmt=lambda v: f"{v:g}", pad=(14, 10, 36, 44), ymax=None):
    top, right, bottom, left = pad
    px0, px1 = left, w - right
    py0, py1 = top + 18, h - bottom
    vmax = ymax or max(vals) * 1.15
    n = len(cats)
    slot = (px1 - px0) / n
    bw = min(slot * 0.62, 44)
    out = [txt(0, 12, title, 12, INK, weight=600), txt(px0 - 6, py0 - 6, unit, 10, MUTED, "end")]
    for i in range(5):
        v = vmax * i / 4
        y = py1 - (v / vmax) * (py1 - py0)
        out.append(line(px0, y, px1, y, HAIR, 1))
        out.append(txt(px0 - 6, y + 4, fmt_num(v) if v >= 1000 else f"{v:.0f}", 10, MUTED, "end"))
    for i, (c, v) in enumerate(zip(cats, vals)):
        x = px0 + slot * i + (slot - bw) / 2
        y = py1 - (v / vmax) * (py1 - py0)
        col = color if (not highlight_last or i == n - 1) else GREY_MARK
        out.append(rect(x, y, bw, py1 - y, col, rx=3))
        out.append(txt(x + bw / 2, y - 6, value_fmt(v), 10, INK2, "middle"))
        out.append(txt(x + bw / 2, py1 + 14, str(c), 10, MUTED, "middle"))
    out.append(line(px0, py1, px1, py1, "#c3bfb4", 1))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_hbars(w, h, rows, title, note=None, lab_w=200, value_fmt=lambda v: f"{v:g}", vmax=None, color=GREY_MARK, accent_idx=None, sub_size=9.5, scale="linear"):
    """rows: list of (label, value, sublabel). Horizontal bars; scale 'linear' or 'sqrt'. Values labelled at the bar end."""
    out = [txt(0, 12, title, 12, INK, weight=600)]
    n = len(rows)
    top = 26
    nh = len(note_lines(note, w)) * 12 + 4 if note else 4
    rowh = (h - top - nh) / n
    vm = vmax or max(r[1] for r in rows)
    bar_x0 = lab_w
    bar_wmax = w - lab_w - 70
    for i, (lab, v, sub, *disp) in enumerate(rows):
        y = top + i * rowh
        frac = math.sqrt(v / vm) if scale == "sqrt" else v / vm
        bw = max(4, bar_wmax * frac)
        col = ACCENT if i == accent_idx else color
        out.append(rect(bar_x0, y + 5, bw, rowh - 10, col, rx=3))
        subs = wrap(sub, int((lab_w - 12) / (sub_size * 0.53))) if sub else []
        block = 14 + len(subs) * (sub_size + 2)
        yy = y + rowh / 2 - block / 2 + 10
        out.append(txt(bar_x0 - 10, yy, lab, 12, INK, "end", 600))
        for s in subs:
            yy += sub_size + 2.5
            out.append(txt(bar_x0 - 10, yy, s, sub_size, MUTED, "end"))
        out.append(txt(bar_x0 + bw + 8, y + rowh / 2 + 4, disp[0] if disp else value_fmt(v), 12, INK2, "start", 600))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_funnel(w, h, steps, title, note=None):
    """steps: list of (label, value, sublabel). Horizontal bars on a square-root scale."""
    out = [txt(0, 12, title, 12, INK, weight=600)]
    n = len(steps)
    top = 26
    nh = len(note_lines(note, w)) * 12 + 4 if note else 4
    rowh = (h - top - nh) / n
    vmax = max(v for _, v, _ in steps)
    lab_w = 300
    bar_x0 = lab_w
    bar_wmax = w - lab_w - 62
    sub_size = 9.5
    for i, (lab, v, sub) in enumerate(steps):
        y = top + i * rowh
        bw = max(6, bar_wmax * math.sqrt(v / vmax))
        col = ACCENT if i == n - 1 else (DARK_MARK if i == 0 else GREY_MARK)
        out.append(rect(bar_x0, y + 6, bw, rowh - 12, col, rx=3))
        subs = wrap(sub, int((lab_w - 12) / (sub_size * 0.53))) if sub else []
        block = 14 + len(subs) * (sub_size + 2)
        yy = y + rowh / 2 - block / 2 + 10
        out.append(txt(bar_x0 - 10, yy, lab, 12, INK, "end", 600))
        for s in subs:
            yy += sub_size + 2.5
            out.append(txt(bar_x0 - 10, yy, s, sub_size, MUTED, "end"))
        out.append(txt(bar_x0 + bw + 8, y + rowh / 2 + 4, fmt_num(v), 12, INK2, "start", 600))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_scatter_map(w, h, points, xlab, ylab, title, legend, note=None):
    """points: dict(name, x 0..1, y 0..1, kind, dx, dy). kind in {'tech','object','channel','us'}. legend: list of (kind, label)."""
    pad_l, pad_r, pad_t, pad_b = 36, 20, 46, 40
    pad_b = max(pad_b, 28 + len(note_lines(note, w)) * 12 + 6)   # axis labels first, then the caption on its own lines
    px0, px1, py0, py1 = pad_l, w - pad_r, pad_t, h - pad_b
    out = [txt(0, 12, title, 12, INK, weight=600),
           rect(px0, py0, px1 - px0, py1 - py0, PANEL, rx=4, stroke=HAIR),
           line((px0 + px1) / 2, py0, (px0 + px1) / 2, py1, HAIR, 1),
           line(px0, (py0 + py1) / 2, px1, (py0 + py1) / 2, HAIR, 1)]
    out.append(txt(px0, py1 + 16, xlab[0], 10, MUTED, "start"))
    out.append(txt(px1, py1 + 16, xlab[1], 10, MUTED, "end"))
    out.append(txt(px0 - 8, py1 - 2, ylab[0], 10, MUTED, "start", extra=f'transform="rotate(-90 {px0-8} {py1-2})"'))
    out.append(txt(px0 - 8, py0 + 2, ylab[1], 10, MUTED, "end", extra=f'transform="rotate(-90 {px0-8} {py0+2})"'))

    def mark(kind, x, y, big=False):
        if kind == "us":
            return circle(x, y, 9, ACCENT, PAPER, 2)
        if kind == "tech":
            return rect(x - 5.5, y - 5.5, 11, 11, DARK_MARK, rx=2, stroke=PAPER, sw=2)
        if kind == "object":
            return circle(x, y, 6, GREY_MARK, PAPER, 2)
        return f'<path d="M {x} {y-7} L {x+7} {y} L {x} {y+7} L {x-7} {y} Z" fill="{WOOD_D}" stroke="{PAPER}" stroke-width="2"/>'

    for p in points:
        x = px0 + p["x"] * (px1 - px0)
        y = py1 - p["y"] * (py1 - py0)
        k = p["kind"]
        if p.get("span"):
            sx0 = px0 + p["span"][0] * (px1 - px0)
            sx1 = px0 + p["span"][1] * (px1 - px0)
            out.append(rect(sx0, y - 7, sx1 - sx0, 14, ACCENT, rx=7, extra='opacity="0.22"'))
        out.append(mark(k, x, y))
        if k == "us":
            out.append(txt(x + p.get("dx", 12), y + p.get("dy", 4), p["name"], 12, ACCENT, p.get("anchor", "start"), 700))
        else:
            out.append(txt(x + p.get("dx", 9), y + p.get("dy", 4), p["name"], 10, INK2, p.get("anchor", "start")))
    lx, ly = px0 + 8, 32
    for kind, lab in legend:
        out.append(mark(kind, lx, ly))
        out.append(txt(lx + 12, ly + 4, lab, 10, INK2))
        lx += 12 + len(lab) * 5.4 + 16
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_gantt(w, h, rows, months, title, today_idx=None, note=None):
    lab_w = 270
    px0, px1 = lab_w, w - 16
    top = 26
    header_h = 18
    rowh = (h - top - header_h - (16 if note else 4)) / len(rows)
    n = len(months)
    mw = (px1 - px0) / n
    out = [txt(0, 12, title, 12, INK, weight=600)]
    for i, m in enumerate(months):
        x = px0 + i * mw
        out.append(line(x, top + header_h - 4, x, h - (16 if note else 4), HAIR, 1))
        out.append(txt(x + mw / 2, top + 10, m, 10, MUTED, "middle"))
    for i, (lab, s, e, state) in enumerate(rows):
        y = top + header_h + i * rowh
        col = {"done": DARK_MARK, "next": ACCENT, "later": GREY_MARK, "gate": PAPER}[state]
        stroke = ACCENT if state == "gate" else "none"
        out.append(txt(px0 - 10, y + rowh / 2 + 4, lab, 11, INK, "end"))
        out.append(rect(px0 + s * mw, y + rowh * 0.25, (e - s) * mw, rowh * 0.5, col, rx=3, stroke=stroke, sw=1.5,
                        extra=('stroke-dasharray="4 3"' if state == "gate" else "")))
    if today_idx is not None:
        x = px0 + today_idx * mw
        out.append(line(x, top + header_h - 4, x, h - (16 if note else 4), ACCENT, 1.5, 'stroke-dasharray="3 3"'))
        out.append(txt(x + 4, top + header_h + 8, "today", 9, ACCENT))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def chart_stacked_hbar(w, h, title, total_label, segments, benchmarks=None, note=None):
    out = [txt(0, 12, title, 12, INK, weight=600)]
    bx0, bx1 = 4, w - 4
    by, bh = 42, 30
    x = bx0
    for i, (lab, share, col, ph) in enumerate(segments):
        sw = (bx1 - bx0) * share
        out.append(rect(x + 1, by, sw - 2, bh, col, rx=3, extra=('stroke-dasharray="4 3"' if ph else ""), stroke=(INK2 if ph else "none")))
        out.append(txt(x + sw / 2, by + bh / 2 + 4, f"{share*100:.0f}%", 10, "#ffffff" if col in (ACCENT, DARK_MARK) else INK2, "middle", 600))
        ly = by + bh + 14 + i * 13
        out.append(rect(bx0, ly - 8, 9, 9, col, rx=2, stroke=(INK2 if ph else "none"), extra=('stroke-dasharray="3 2"' if ph else "")))
        out.append(txt(bx0 + 14, ly, lab, 10, INK2))
        x += sw
    out.append(txt(bx0, by - 8, total_label, 10.5, INK2))
    if benchmarks:
        yb = by + bh + 14 + len(segments) * 13 + 22
        out.append(txt(bx0, yb - 10, "Gross margin benchmarks, latest fiscal year", 10.5, INK2))
        for t in (0, 0.25, 0.5, 0.75):
            xx = bx0 + (bx1 - bx0) * t
            out.append(txt(xx, yb + 4, f"{t*100:.0f}%", 8.5, MUTED, "middle" if t else "start"))
        out.append(line(bx0, yb + 14, bx1, yb + 14, "#c3bfb4", 1))
        # labels are placed by a small search: three rows below the axis, three anchors; no two labels overlap and no
        # leader line passes through another label (the build fails if no such placement exists)
        items = sorted((bx0 + (bx1 - bx0) * share, f"{lab} {share*100:.0f}%") for lab, share, *_ in benchmarks)
        fs_b = 9.5

        def solve_b(k, placed):
            if k == len(items):
                return placed
            xx, t = items[k]
            wl = len(t) * fs_b * 0.54
            for row in range(3):
                for anchor in ("middle", "start", "end"):
                    x0 = {"middle": xx - wl / 2, "start": xx - 4, "end": xx + 4 - wl}[anchor]
                    x1 = x0 + wl
                    if x0 < 0 or x1 > w:
                        continue
                    ok = True
                    for q in placed:
                        if q["row"] == row and not (x1 + 6 < q["x0"] or x0 - 6 > q["x1"]):
                            ok = False
                        if q["row"] > row and x0 - 3 <= q["dot"] <= x1 + 3:
                            ok = False
                        if row > q["row"] and q["x0"] - 3 <= xx <= q["x1"] + 3:
                            ok = False
                    if ok:
                        got = solve_b(k + 1, placed + [dict(row=row, anchor=anchor, x0=x0, x1=x1, dot=xx, text=t)])
                        if got:
                            return got
            return None

        placed_b = solve_b(0, [])
        if not placed_b:
            raise RuntimeError("benchmark strip: no collision-free label placement")
        for q in placed_b:
            xx, row, anchor = q["dot"], q["row"], q["anchor"]
            out.append(circle(xx, yb + 14, 4.5, DARK_MARK, PAPER, 2))
            out.append(line(xx, yb + 18, xx, yb + 24 + row * 12, HAIR, 1))
            out.append(txt(xx + (4 if anchor == "start" else -4 if anchor == "end" else 0), yb + 34 + row * 12, q["text"], fs_b, INK2, anchor))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


# ---------------------------------------------------------------- object renders (placeholders, flat and geometric, 120x120 box)
def obj_inner(kind):
    """Shapes for one object in a 0..120 box. Placeholder renders: Oscar replaces them with the real ones."""
    o = []
    if kind == "eink":  # wall e-ink display
        o += [rect(12, 14, 96, 92, WOOD, rx=6), rect(22, 24, 76, 72, "#f9f7f0", rx=2)]
        o += [rect(30, 32, 40, 6, INK, rx=1), line(30, 46, 90, 46, HAIR, 1)]
        for i in range(5):
            o.append(rect(30, 54 + i * 7, 60 * (0.95 if i % 3 else 0.65), 2.4, "#b9b4a8", rx=1))
        o.append(rect(30, 88 - 2, 16, 5, ACCENT, rx=1))
    elif kind == "desk":  # desk AI display with a face
        o += [rect(34, 100, 52, 6, DARK_MARK, rx=3), rect(52, 84, 16, 18, DARK_MARK)]
        o += [rect(22, 18, 76, 68, DARK_MARK, rx=16), rect(30, 26, 60, 52, "#f9f7f0", rx=10)]
        o += [circle(48, 48, 5, INK), circle(72, 48, 5, INK), path("M 48 62 Q 60 70 72 62", INK, width=2.5)]
    elif kind == "key":  # solar keychain
        o += [circle(60, 16, 12, "none", INK2, 3), line(60, 28, 60, 38, INK2, 3)]
        o += [rect(40, 38, 40, 70, DARK_MARK, rx=10), rect(46, 44, 28, 28, "#2a3a55", rx=3)]
        for i in (1, 2):
            o.append(line(46, 44 + i * 9.3, 74, 44 + i * 9.3, "#6c7a96", 1))
        o.append(line(60, 44, 60, 72, "#6c7a96", 1))
        o += [circle(60, 86, 5, ACCENT), rect(52, 96, 16, 3, GREY_MARK, rx=1.5)]
    elif kind == "aqua":  # wall aquarium
        o += [rect(10, 22, 100, 76, WOOD, rx=6), rect(18, 30, 84, 60, "#dfe8e6", rx=3)]
        o += [f'<path d="M 30 62 Q 42 52 54 62 Q 42 72 30 62 Z M 54 62 L 62 54 L 62 70 Z" fill="{ACCENT}"/>']
        o += [f'<path d="M 70 46 Q 78 40 86 46 Q 78 52 70 46 Z M 86 46 L 91 41 L 91 51 Z" fill="{GREY_MARK}"/>']
        o += [f'<path d="M 66 78 Q 76 70 86 78 Q 76 86 66 78 Z M 86 78 L 92 72 L 92 84 Z" fill="none" stroke="{INK2}" stroke-width="1.2" stroke-dasharray="3 2"/>']
        o += [circle(36, 44, 2.5, "#ffffff"), circle(42, 38, 2, "#ffffff"), circle(25, 78, 3, "#ffffff")]
    elif kind == "lamp":  # work light with e-ink face
        o += [rect(18, 104, 40, 6, DARK_MARK, rx=3), path("M 38 104 L 50 58 L 82 34", DARK_MARK, width=5)]
        o += [f'<path d="M 74 24 L 104 36 L 96 54 L 66 42 Z" fill="{DARK_MARK}"/>']
        o += [f'<path d="M 70 46 L 100 58 L 112 112 L 52 112 Z" fill="{WARM}" opacity="0.28"/>']
        o += [rect(26, 66, 28, 18, "#f9f7f0", rx=2, stroke=DARK_MARK, sw=2), rect(30, 70, 14, 2.4, INK), rect(30, 75, 20, 2, "#b9b4a8"), rect(30, 79, 16, 2, "#b9b4a8")]
    elif kind == "fairy":  # Wi-Fi plug and fairy lights
        o += [rect(12, 56, 30, 30, DARK_MARK, rx=7), rect(4, 63, 8, 4, GREY_MARK), rect(4, 75, 8, 4, GREY_MARK), circle(27, 71, 6, ACCENT)]
        o += [path("M 42 71 C 56 40, 72 100, 86 62 S 108 70, 114 54", INK2, width=2)]
        for (x, y) in [(52, 54), (64, 74), (76, 76), (88, 62), (100, 66), (112, 55)]:
            o += [circle(x, y, 7, WARM, extra='opacity="0.35"'), circle(x, y, 3.6, WARM)]
    elif kind == "lock":  # fish-shaped lock
        o += [path("M 44 40 C 44 12 76 12 76 40", DARK_MARK, width=6)]
        o += [f'<path d="M 22 74 Q 54 36 86 74 Q 54 112 22 74 Z" fill="{ACCENT}"/>', f'<path d="M 86 74 L 108 54 L 108 94 Z" fill="{ACCENT}"/>']
        o += [circle(38, 70, 3, PAPER), circle(60, 78, 5, INK), rect(58.5, 80, 3, 11, INK, rx=1.5)]
    elif kind == "vase":  # decoration, no electronics
        o += [f'<path d="M 50 14 L 70 14 C 70 32 94 42 94 74 C 94 98 78 108 60 108 C 42 108 26 98 26 74 C 26 42 50 32 50 14 Z" fill="#efe9dc" stroke="{INK2}" stroke-width="1.6"/>']
        o += [rect(30, 66, 60, 8, ACCENT)]
    elif kind == "wall":  # decoration, wall piece
        o += [circle(60, 60, 48, WOOD), circle(60, 60, 36, "#efe9dc"), f'<path d="M 24 60 A 36 36 0 0 1 96 60" fill="none" stroke="{ACCENT}" stroke-width="8"/>', circle(60, 60, 10, WOOD_D)]
    elif kind == "tray":  # decoration, lacquered tray
        o += [f'<path d="M 10 62 L 110 62 L 100 94 L 20 94 Z" fill="{ACCENT}"/>', rect(18, 56, 84, 8, "#8d2a17", rx=3), circle(46, 48, 12, "#efe9dc", INK2, 1.4), rect(64, 38, 18, 18, WOOD, rx=3)]
    return "".join(o)


def obj_svg(kind, w=120, h=120):
    return svg(w, h, f'<g transform="scale({w/120:.4f} {h/120:.4f})">{obj_inner(kind)}</g>')


def obj_at(kind, x, y, s):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.3f})">{obj_inner(kind)}</g>'


def cover_scene(w, h):
    """A wall and a shelf with the collection, as one composition."""
    o = [rect(0, 0, w, h, "#ece6d8", rx=6)]
    o.append(rect(0, h - 70, w, 70, "#ded6c4"))
    sy = 292
    o.append(rect(24, sy, w - 48, 9, WOOD_D, rx=2))
    o.append(rect(24, sy + 9, w - 48, 3, "#6d4c2f"))
    o.append(obj_at("eink", 36, 40, 1.6))      # wall e-ink display
    o.append(obj_at("aqua", 250, 36, 1.6))     # wall aquarium
    o.append(obj_at("wall", 440, 56, 1.0))     # wall piece
    o.append(obj_at("vase", 30, sy - 120 * 1.05 + 14, 1.05))
    o.append(obj_at("desk", 150, sy - 120 * 1.0 + 14, 1.0))
    o.append(obj_at("lamp", 268, sy - 120 * 1.2 + 14, 1.2))
    o.append(obj_at("lock", 420, sy - 120 * 0.8 + 14, 0.8))
    o.append(obj_at("key", 500, sy - 120 * 0.7 + 14, 0.7))
    o.append(obj_at("tray", 520, 360, 0.9))
    o.append(obj_at("fairy", 40, 345, 1.1))
    return svg(w, h, "".join(o))


def eink_screen(w, h, label=None):
    """The e-ink display shown on its own: a generic day view, no named content product."""
    fw, fh = w - 20, h - 20
    fx, fy = 10, 10
    out = [rect(fx, fy, fw, fh, WOOD, rx=14)]
    ix, iy, iw, ih = fx + 22, fy + 22, fw - 44, fh - 44
    out.append(rect(ix, iy, iw, ih, "#f9f7f0", rx=3))
    out.append(txt(ix + 18, iy + 40, "Friday", 26, INK, "start", 700, SERIF))
    out.append(txt(ix + 18, iy + 62, "27 November", 13, INK2))
    out.append(line(ix + 18, iy + 74, ix + iw - 18, iy + 74, INK, 1.2))
    rows = [("08:30", "Call with the factory"), ("13:00", "Lunch"), ("18:15", "Train home")]
    for i, (t, s) in enumerate(rows):
        yy = iy + 100 + i * 28
        out.append(txt(ix + 18, yy, t, 12, ACCENT, "start", 700))
        out.append(txt(ix + 70, yy, s, 13, INK))
    out.append(rect(ix + iw - 120, iy + 22, 102, 40, "none", stroke=INK2, sw=1, rx=3))
    out.append(txt(ix + iw - 69, iy + 38, "11 C", 14, INK, "middle", 700))
    out.append(txt(ix + iw - 69, iy + 54, "clear", 10, INK2, "middle"))
    out.append(rect(ix + 18, iy + ih - 34, 76, 18, ACCENT, rx=2))
    out.append(txt(ix + 56, iy + ih - 21, "SAY IT", 9, "#ffffff", "middle", 700))
    out.append(txt(ix + iw - 18, iy + ih - 21, "\"add the train times\"", 10, MUTED, "end", italic=True))
    if label:
        out.append(txt(w / 2, h - 1, label, 10, MUTED, "middle"))
    return svg(w, h, "".join(out))


# ---------------------------------------------------------------- slide shell
def slide(num_, kicker, title, body_html, foot_sources="", extra_class=""):
    return f'''
<section class="slide {extra_class}" id="s{num_}">
  <header class="top">
    <div class="kicker">{num_:02d} <span class="dot">&middot;</span> {esc(kicker)}</div>
  </header>
  <h1>{title}</h1>
  <div class="body">{body_html}</div>
  <footer class="foot">
    <div class="left">{esc(BRAND)} <span class="dot">&middot;</span> {esc(DRAFT_LINE)}</div>
    <div class="mid">{foot_sources}</div>
    <div class="right">{num_}</div>
  </footer>
</section>'''


CSS = f"""
@page {{ size: 1280px 720px; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: #e7e2d8; font-family: {SANS}; color: {INK}; }}
.slide {{ position: relative; width: 1280px; height: 720px; background: {PAPER}; overflow: hidden; margin: 24px auto;
         box-shadow: 0 2px 14px rgba(0,0,0,.12); page-break-after: always; break-after: page; padding: 44px 60px 0 60px; }}
.slide:last-child {{ page-break-after: auto; break-after: auto; }}
@media print {{ html, body {{ background: {PAPER}; }} .slide {{ margin: 0; box-shadow: none; }} }}
.kicker {{ font-size: 12px; letter-spacing: .14em; text-transform: uppercase; color: {MUTED}; font-weight: 600; }}
.dot {{ color: {ACCENT}; }}
h1 {{ font-family: {SERIF}; font-weight: 400; font-size: 34px; line-height: 1.12; margin: 10px 0 0 0; letter-spacing: -.01em; max-width: 1120px; }}
h1 em {{ font-style: italic; color: {ACCENT}; }}
.body {{ position: absolute; left: 60px; right: 60px; top: 150px; bottom: 56px; }}
.slide.t2 .body {{ top: 160px; }}   /* slides whose title wraps to two lines: 10 px more between the title and the body */
.foot {{ position: absolute; left: 60px; right: 60px; bottom: 22px; display: flex; justify-content: space-between; align-items: baseline;
        font-size: 10.5px; color: {MUTED}; border-top: 1px solid {HAIR}; padding-top: 8px; }}
.foot .mid {{ flex: 1; margin: 0 24px; color: {MUTED}; }}
.foot .right {{ font-variant-numeric: tabular-nums; }}
p, li {{ font-size: 15px; line-height: 1.42; margin: 0 0 10px 0; color: {INK}; }}
ul {{ padding-left: 18px; margin: 0; }}
.small {{ font-size: 13px; color: {INK2}; line-height: 1.4; }}
.muted {{ color: {MUTED}; }}
.accent {{ color: {ACCENT}; }}
sup.fn {{ font-size: 9px; color: {ACCENT}; font-weight: 600; vertical-align: super; line-height: 0; margin-left: 1px; }}
.cols {{ display: grid; gap: 36px; height: 100%; }}
.cols > div {{ min-width: 0; }}
.c2 {{ grid-template-columns: minmax(0,1fr) minmax(0,1fr); }}
.c21 {{ grid-template-columns: minmax(0,1.15fr) minmax(0,1fr); }}
.c12 {{ grid-template-columns: minmax(0,1fr) minmax(0,1.25fr); }}
.c3 {{ grid-template-columns: minmax(0,1fr) minmax(0,1fr) minmax(0,1fr); }}
.small li {{ font-size: 12.5px; line-height: 1.4; margin: 0 0 6px 0; }}
.label {{ font-size: 11.5px; letter-spacing: .12em; text-transform: uppercase; color: {MUTED}; font-weight: 600; margin: 0 0 8px 0; }}
.card {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 14px 16px; }}
.card.ph {{ border-style: dashed; }}
.tile {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 12px 14px 10px 14px; }}
.tile .v {{ font-size: 30px; line-height: 1; margin: 2px 0 6px 0; letter-spacing: -.02em; color: {INK}; }}
.tile .v.ph {{ color: {MUTED}; font-size: 17px; letter-spacing: 0; }}
.tile .k {{ font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: {MUTED}; font-weight: 600; }}
.tile .m {{ font-size: 11.5px; color: {INK2}; line-height: 1.4; }}
table.t {{ border-collapse: collapse; width: 100%; font-size: 11px; line-height: 1.3; }}
table.t th {{ text-align: left; font-weight: 600; color: {MUTED}; font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px 5px 0; border-bottom: 1px solid {HAIR}; }}
table.t td {{ padding: 4px 8px 4px 0; border-bottom: 1px solid {HAIR}; vertical-align: top; color: {INK}; }}
table.t td.n {{ font-variant-numeric: tabular-nums; white-space: nowrap; }}
table.t tr.us td {{ color: {ACCENT}; font-weight: 600; }}
table.t.compact {{ font-size: 10.5px; line-height: 1.25; }}
table.t.compact td {{ padding: 3px 6px 3px 0; }}
.ph {{ color: {MUTED}; }}
.badge {{ display: inline-block; font-size: 10px; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; color: {ACCENT};
         border: 1px solid {ACCENT}; border-radius: 3px; padding: 2px 6px; vertical-align: middle; margin-left: 6px; }}
.fam {{ display: grid; grid-template-columns: 124px repeat(3, minmax(0,1fr)); gap: 12px; align-items: stretch; }}
.fam .fh {{ border-left: 3px solid {ACCENT}; padding: 4px 0 0 12px; }}
.fam .fh .t {{ font-family: {SERIF}; font-size: 20px; line-height: 1.1; margin-bottom: 6px; }}
.fam .fh .d {{ font-size: 11px; color: {INK2}; line-height: 1.35; }}
.item {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 8px 10px; display: flex; gap: 10px; align-items: center; }}
.item .r {{ flex: none; width: 70px; height: 70px; border: 1px dashed {HAIR}; border-radius: 6px; display: flex; align-items: center; justify-content: center; background: #f1ede2; }}
.item .nm {{ font-family: {SERIF}; font-size: 15px; line-height: 1.15; margin: 0 0 3px 0; }}
.item .on {{ font-size: 11px; color: {INK2}; line-height: 1.3; margin: 0 0 4px 0; }}
.item .pr {{ display: inline-block; font-size: 10.5px; color: {MUTED}; border: 1px dashed {GREY_MARK}; border-radius: 10px; padding: 1px 8px; }}
.cover {{ padding: 0; }}
.cover .body {{ top: 0; bottom: 0; left: 0; right: 0; }}
.cover .wordmark {{ position: absolute; left: 80px; top: 92px; font-family: {SERIF}; font-size: 54px; line-height: 1.05; max-width: 520px; letter-spacing: -.01em; }}
.cover .sub {{ position: absolute; left: 80px; top: 318px; font-size: 19px; line-height: 1.45; max-width: 500px; color: {INK2}; }}
.cover .meta {{ position: absolute; left: 80px; bottom: 50px; font-size: 13px; color: {MUTED}; line-height: 1.6; }}
.cover .illus {{ position: absolute; right: 60px; top: 90px; }}
.cover .rule {{ position: absolute; left: 80px; top: 290px; width: 72px; height: 3px; background: {ACCENT}; }}
.quote {{ font-family: {SERIF}; font-size: 20px; line-height: 1.35; color: {INK}; border-left: 3px solid {ACCENT}; padding-left: 16px; margin: 0 0 14px 0; }}
.steps {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }}
.step {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 12px 14px; }}
.step .n {{ font-family: {SERIF}; font-size: 26px; color: {ACCENT}; line-height: 1; margin-bottom: 6px; }}
.step .h {{ font-weight: 600; font-size: 14px; margin-bottom: 4px; }}
.step .d {{ font-size: 12.5px; color: {INK2}; line-height: 1.4; }}
.src {{ font-size: 9.5px; color: {INK2}; line-height: 1.35; column-count: 2; column-gap: 28px; }}
.src div {{ break-inside: avoid; margin-bottom: 5px; }}
.src b {{ color: {ACCENT}; font-weight: 700; margin-right: 4px; }}
.src .u {{ color: {MUTED}; word-break: break-all; }}
.hr {{ height: 1px; background: {HAIR}; margin: 10px 0; }}
.pill {{ display: inline-block; font-size: 10px; letter-spacing: .06em; text-transform: uppercase; font-weight: 700; padding: 1px 7px; border-radius: 9px; border: 1px solid {HAIR}; color: {INK2}; margin-right: 4px; }}
.mood {{ display: grid; grid-template-columns: repeat(4, 192px); gap: 10px; }}
.mood .cell {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 6px; overflow: hidden; }}
.mood .cell img {{ display: block; width: 100%; height: 92px; object-fit: cover; }}
.mood .cap {{ font-size: 9.5px; line-height: 1.25; color: {INK}; padding: 5px 7px 0 7px; min-height: 29px; }}
.mood .cat {{ font-size: 7.5px; letter-spacing: .08em; text-transform: uppercase; color: {ACCENT}; font-weight: 700; margin-right: 4px; }}
.mood .credit {{ font-size: 7.2px; line-height: 1.3; color: {MUTED}; padding: 2px 7px 4px 7px; word-break: break-all; }}
.mood .credit sup.fn {{ font-size: 7px; }}
.pat {{ padding-left: 14px; margin: 0; }}
.pat li {{ font-size: 10px; line-height: 1.35; margin: 0 0 3px 0; color: {INK}; }}
.rule {{ display: flex; gap: 10px; align-items: flex-start; padding: 9px 12px; }}
.rule .thumb {{ width: 56px; height: 56px; object-fit: cover; border-radius: 4px; flex: none; border: 1px solid {HAIR}; }}
.rule .credit-line {{ font-size: 8px; color: {MUTED}; margin-top: 5px; line-height: 1.4; word-break: normal; overflow-wrap: anywhere; }}
.rule .credit-line sup.fn {{ margin-left: 2px; }}
/* slide 7, right column: the table, the paragraph and the three tiles tightened so the observation tile clears the footer */
.tight table.t.compact td {{ padding: 2px 6px 2px 0; }}
.tight table.t.compact {{ font-size: 10px; }}
.tight table.t th {{ padding: 2px 6px 4px 0; }}
.tight table.t td:first-child {{ white-space: nowrap; }}
.tight p.small {{ line-height: 1.3; }}
.tight .tile {{ padding: 6px 12px; }}
.tight .tile .m {{ font-size: 11px; line-height: 1.25; }}
"""

# ---------------------------------------------------------------- slides that do not depend on new research
def s_cover():
    body = f'''
<div class="wordmark">{esc(BRAND)}<br><span style="font-size:30px;color:{INK2}">Objects for a considered home.</span></div>
<div class="rule"></div>
<div class="sub">One premium brand for the things you put in your home: decorations, gadgets and objects you did not know you needed. One design language across all of them. Hardware sourced in Shenzhen, design from Europe, and software only in the objects that gain from it.</div>
<div class="illus">{cover_scene(560, 440)}</div>
<div class="meta">Pitch deck, version 4 draft &middot; 27 November 2026 &middot; Oscar [surname placeholder]<br>Private. Not for distribution. Placeholder renders. Every figure carries a numbered source (appendix, research.md).</div>'''
    return f'''
<section class="slide cover" id="s1">
  <div class="body">{body}</div>
</section>'''


FAMILIES = [
    ("Decorate", "Objects with no electronics. They earn their place on the shelf.", [
        ("vase", "Shelf object", "A sculptural piece in the brand's materials. [name placeholder]"),
        ("wall", "Wall piece", "A round wall object in wood and lacquer. [name placeholder]"),
        ("lock", "Fish-shaped lock", "Interior oddity, in the tradition of Japanese specialist stores."),
    ]),
    ("Gadgets", "Objects with a small computer inside. Smart only where it helps.", [
        ("eink", "E-ink wall display", "Shows what you ask it to, on paper-like e-ink (saved posts: slide 4)."),
        ("desk", "Desk AI display", "A face, a voice and a glanceable screen for the desk (saved post: slide 4)."),
        ("key", "Solar AI keychain", "Talk to your AI from a keyring. Charges in daylight."),
    ]),
    ("Light and ambience", "Objects that change how a room feels.", [
        ("lamp", "10,000-lumen e-ink light", "A work light whose e-ink face says what it is lighting."),
        ("fairy", "Wi-Fi plug for fairy lights", "Lights that know your calendar: on for guests, off when you leave."),
        ("aqua", "Digital wall aquarium", "A living wall tank whose rare fish appear only sometimes (saved post: slide 4)."),
    ]),
]


def chart_price_lanes(w, h, lanes, xmax, title, note=None):
    """Retail list prices of named comparable objects, one lane per currency (not converted). lanes: (label, [(price, name)]).
    Labels are placed automatically: four slots per lane (two above the axis, two below) and three anchors (centred, starting at
    the dot, ending at the dot). A label is accepted only if it overlaps no other label in its slot and, for the outer slots, its
    leader line crosses no inner label. If no placement exists the build fails, so a collision cannot ship."""
    px0, px1 = 74, w - 20
    top = 22
    nh = len(note_lines(note, w)) * 12 + 4 if note else 4
    axis_h = 18
    lane_h = (h - top - nh - axis_h) / len(lanes)
    out = [txt(0, 12, title, 12, INK, weight=600)]
    fs, em = 9.5, 0.56

    def X(v):
        return px0 + v / xmax * (px1 - px0)

    for t in range(0, int(xmax) + 1, 50):
        out.append(line(X(t), top, X(t), top + lane_h * len(lanes), HAIR, 1))
        out.append(txt(X(t), top + lane_h * len(lanes) + 13, f"{t}", 9.5, MUTED, "middle"))
    slots = [("up1", -8), ("down1", 17), ("up2", -20), ("down2", 29)]
    for i, (lab, items) in enumerate(lanes):
        cy = top + i * lane_h + lane_h / 2
        out.append(txt(0, cy + 4, lab, 11, INK, "start", 700))
        out.append(line(px0, cy, px1, cy, "#c3bfb4", 1.2))
        todo = []
        for price, name in sorted(items):
            off = price > xmax
            x = px1 if off else X(price)
            s_ = f"{name} {price:g}" + (" (off scale)" if off else "")
            todo.append((x, s_, len(s_) * fs * em, off))

        def fits(cand, placed):
            slot, dy, anchor, x0, x1, far, side, x = cand
            if x0 < 36 or x1 > w - 2:
                return False
            for q in placed:
                if q["slot"] == slot and not (x1 + 8 < q["x0"] or x0 - 8 > q["x1"]):
                    return False
                # an inner label on the same side must not sit on an outer label's leader line, and vice versa
                if q["far"] and q["side"] == side and not far and x0 - 3 <= q["dot"] <= x1 + 3:
                    return False
                if far and q["side"] == side and not q["far"] and q["x0"] - 3 <= x <= q["x1"] + 3:
                    return False
            return True

        def solve(k, placed):
            if k == len(todo):
                return placed
            x, s_, wl, off = todo[k]
            for slot, dy in slots:
                for anchor in (["end", "middle", "start"] if off else ["middle", "start", "end"]):
                    x0 = {"middle": x - wl / 2, "start": x - 4, "end": x + 4 - wl}[anchor]
                    cand = (slot, dy, anchor, x0, x0 + wl, slot.endswith("2"), slot[:-1], x)
                    if fits(cand, placed):
                        got = solve(k + 1, placed + [dict(slot=slot, dy=dy, anchor=anchor, x0=x0, x1=x0 + wl, dot=x,
                                                          far=cand[5], side=cand[6], text=s_)])
                        if got:
                            return got
            return None

        placed = solve(0, [])
        if not placed:
            raise RuntimeError(f"price ladder: no collision-free label placement in lane {lab}")
        for q in placed:
            out.append(circle(q["dot"], cy, 4.5, DARK_MARK, PAPER, 2))
            if q["far"]:
                out.append(line(q["dot"], cy + (-5 if q["side"] == "up" else 5), q["dot"], cy + q["dy"] + (3 if q["side"] == "up" else -9), HAIR, 1))
            tx = {"middle": (q["x0"] + q["x1"]) / 2, "start": q["x0"], "end": q["x1"]}[q["anchor"]]
            out.append(txt(tx, cy + q["dy"], q["text"], fs, INK2, q["anchor"]))
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


def s_collection():
    rows = []
    for fam, desc, items in FAMILIES:
        cells = [f'<div class="fh"><div class="t">{esc(fam)}</div><div class="d">{esc(desc)}</div></div>']
        for kind, name, one in items:
            cells.append(f'<div class="item"><div class="r">{obj_svg(kind, 66, 66)}</div><div><div class="nm">{esc(name)}</div><div class="on">{esc(one)}</div><span class="pr">&euro; [price placeholder]</span></div></div>')
        rows.append(f'<div class="fam">{"".join(cells)}</div>')
    grid = f'<div style="display:grid;grid-template-rows:repeat(3,1fr);gap:10px;height:284px">{"".join(rows)}</div>'
    lanes = [
        ("EUR", [(39.95, "Muji alarm clock"), (59.95, "Muji digital clock"), (69, "Nothing CMF Watch Pro 2"), (142, "Nothing Ear (3)"),
                 (313, "Teenage Eng. EP-133"), (535, "Teenage Eng. OB-4")]),
        ("USD", [(79.9, "Lexon Oblio"), (99, "HAY PC Portable lamp"), (110, "Alessi Anna G"), (119.99, "Nanoleaf Shapes"),
                 (150, "Ember mug"), (179.99, "Marshall Emberton III"), (899.99, "Samsung Frame 43in")]),
    ]
    ladder = chart_price_lanes(
        1160, 176, lanes, 400, "Where comparable objects sell: retail list prices in their own currency, not converted",
        note=f"Our price per object: [placeholder], due Sat 28 Nov. Prices read on retail pages, accessed 27 Nov 2026 (HAY, Alessi, Ember, Nanoleaf and the EUR retail prices were seen in snippets only) {cite('price_v', 'price_s')}.")
    body = f'<div class="label" style="margin-bottom:6px">The collection at launch: three families, nine objects (draft, placeholder renders and prices)</div>{grid}<div style="margin-top:6px">{ladder}</div>'
    return slide(5, "Product: the collection", "The collection: decorations, gadgets and light under one name, from a shelf object to a talking display",
                 body, "Flat placeholder renders; one-liners from the 26 Nov catalogue decision; the two decor objects are concept placeholders. No saved post shows lighting (slide 4).",
                 extra_class="t2")


# ---------------------------------------------------------------- v4: the posts the founder keeps saving (slide 4; research.md section 8)
# Source list, images and the founder's comments: ../inspiration/README.md (28 posts, read-only). Captions describe the object in
# the image; post authors appear only as X handles in credit lines. Images: images/<id>.jpg, made by prepare_images.py.
# 28 Nov 2026: two posts added (Displays and e-ink); the five Wall and decor posts were removed from the list at Oscar's request
# and are gone from the deck (REMOVED below is checked by check_deck.py). Later the same morning: The Scout and the @audrlo
# production-robot post added (both Desk gadgets).
REMOVED = ["2124808965351682185", "2124365500000153752", "2124263578261700815", "2121998102206754958", "2111851254091776122"]
POSTS = [
    # Displays and e-ink (the first two were added on 28 Nov 2026)
    dict(id="2126278478295109862", handle="huntie", cat="Displays and e-ink", what="Large e-ink tablet and stylus, read in a cafe"),
    dict(id="2126078769483985199", handle="ahm3dhub", cat="Displays and e-ink", what="ESP32 board with snap-together AMOLED tiles"),
    dict(id="2125609297895903294", handle="hturan", cat="Displays and e-ink", what="Artificial life moving on a 60 Hz e-ink panel"),
    # Desk gadgets (the first two were added on 28 Nov 2026)
    dict(id="2126500872079524186", handle="audrlo", cat="Desk gadgets", what="3D-printed robot-head prototypes grown into a production home device shipped to families in the US"),
    dict(id="2126374876135231971", handle="kinglycrow", cat="Desk gadgets", what="Magnetic Wi-Fi camera at $25: an AI agent's eyes at home"),
    dict(id="2125946257852285039", handle="andreintg", cat="Desk gadgets", what="Open-frame 3D-printed PC case with a small clock"),
    dict(id="2125649169138528553", handle="kieranklaassen", cat="Desk gadgets", what="An LLM plans the day; a thermal printer prints the slips"),
    dict(id="2125257053341966427", handle="inanimate_tech", cat="Desk gadgets", what="Five promptable desk devices, one design language, orderable"),
    dict(id="2122686374998655392", handle="oliviscusAI", cat="Desk gadgets", what="Open-source robotic arm that anyone may build and sell"),
    dict(id="2117773168807166443", handle="RaemondBW", cat="Desk gadgets", what="Replacement board adds AirPlay to a flat-pack speaker"),
    dict(id="2113274039297028534", handle="luusssso", cat="Desk gadgets", what="Transparent 1990s cassette player in sea green"),
    # Furniture
    dict(id="2125588103276720393", handle="modem_works", cat="Furniture", what="A bookcase lights up the books that answer a spoken question"),
    dict(id="2116952646406041615", handle="yitong", cat="Furniture", what="A plywood table design turned into a CNC-ready file for a local shop"),
    # Art objects
    dict(id="2124080717508587904", handle="pmamtraveller", cat="Art objects", what="Hand-made art doll in embroidered linen, made around 2013"),
    dict(id="2124079010317508699", handle="pmamtraveller", cat="Art objects", what="Corsican folding knife with a floral painted handle"),
    dict(id="2123854155856880066", handle="pmamtraveller", cat="Art objects", what="Ceramic ashtray lined with blue mosaic tiles"),
    dict(id="2123544537419194476", handle="wana_visualss", cat="Art objects", what="Stone statue of a seated queen on the Syrian coast"),
    dict(id="2122938259906994637", handle="pmamtraveller", cat="Art objects", what="Three cloaked bronze figures with small gilded masks"),
    dict(id="2121669740770849167", handle="pmamtraveller", cat="Art objects", what="Bronze figure of a crowned harlequin seated in a chair"),
    dict(id="2119704977648365754", handle="artinsociety", cat="Art objects", what="2,300-year-old bronze head with alabaster and glass eyes"),
    dict(id="2113587717259075882", handle="g3p_graph", cat="Art objects", what="Prototype hand armour worn over a thin glove"),
    # Other
    dict(id="2125998015592726811", handle="womp3D", cat="Other", what="An unusual 3D print: a matte black bowl held in one hand"),
    dict(id="2123010578616659969", handle="SciFiArchives", cat="Other", what="Retrofuturistic headphone concept, knurled metal, fabric"),
    dict(id="2122893427323056464", handle="pmamtraveller", cat="Other", what="Concept art: creature heads shaped after hammers and axes"),
    dict(id="2121739170221789433", handle="kevintwohy", cat="Other", what="Book on the prototyping and industrial design behind a games console"),
    dict(id="2121458552803914203", handle="MaxLobovsky", cat="Other", what="AI-designed water gun printed in clear resin, with printed seals"),
    dict(id="2114750542941442453", handle="guilhemlettron", cat="Other", what="Palm-sized programmable drone assembled for under 20 euros"),
    dict(id="2087040759140855981", handle="asimovinc", cat="Other", what="Open-source humanoid robot sold as a complete kit for US$20,000"),
]
POST = {p["id"]: p for p in POSTS}
CATS = ["Displays and e-ink", "Desk gadgets", "Furniture", "Art objects", "Lighting", "Other"]
assert len(POSTS) == 28 and len(POST) == 28 and all(p["cat"] in CATS for p in POSTS)
assert not (set(REMOVED) & set(POST)), "a post Oscar removed is still in the list"
# the twelve shown on slide 4, in grid order (three of them are reused as thumbnails on slide 3). 28 Nov 2026: the e-ink tablet
# (cell 4) and the ESP32 AMOLED board (cell 8) replace the AirPlay board (still cited in the patterns) and the removed
# illustration; the water gun moved from cell 8 to cell 11. Later on 28 Nov: the magnetic camera (cell 10) replaces the bronze
# figures (still cited in the hand-made pattern); Art objects keeps the ceramic ashtray in cell 9.
FEATURED = ["2125588103276720393", "2125257053341966427", "2125609297895903294", "2126278478295109862",
            "2113274039297028534", "2123010578616659969", "2125946257852285039", "2126078769483985199",
            "2123854155856880066", "2126374876135231971", "2121458552803914203", "2125649169138528553"]
HANDMADE = [p["id"] for p in POSTS if p["cat"] == "Art objects"]
assert len(HANDMADE) == 8
# (title, text, post ids): observations from the 28 posts, never a measurement; mirrors the patterns section of the inspiration README.
# Line budget (slide 4, right column, 10 px text, about 60 characters a line): 21 lines in all, measured on Innovator's render of
# 27 Nov 2026, where the column ended 21 px above the footer rule. A longer line here must be paid for by a shorter one.
PATTERNS = [
    ("Cheap hardware plus an app.", "7 posts; the founder's note on the bookcase: cheap hardware from China plus an app sells.",
     ["2125588103276720393", "2114750542941442453", "2122686374998655392", "2117773168807166443", "2125649169138528553", "2126078769483985199",
      "2126374876135231971"]),
    ("Transparent and retrofuturistic.", "4 posts: see-through player, clear-resin water gun, retro headphones, open-frame PC.",
     ["2113274039297028534", "2121458552803914203", "2123010578616659969", "2125946257852285039"]),
    ("E-ink and calm screens.", "2 posts: a 60 Hz e-ink simulation; a large e-ink tablet read in a cafe.", ["2125609297895903294", "2126278478295109862"]),
    ("Ceramics and hand-made objects.", "8 of 28 lean to sculpture, bronze, dolls; ceramics is the one material the founder names.", HANDMADE),
    ("One small smart function on an ordinary object.", "4 posts: bookcase, printed day plan, AirPlay board, promptable desk devices.",
     ["2125588103276720393", "2125649169138528553", "2117773168807166443", "2125257053341966427"]),
    ("AI-assisted making.", "3 posts: a water gun modelled with AI, a CNC-ready table file, an LLM that prints plans.",
     ["2121458552803914203", "2116952646406041615", "2125649169138528553"]),
    ("A wider market than tech people.", "The founder's notes on the PC case and the hand armour; a printed prototype grown into a shipped home device.",
     ["2125946257852285039", "2113587717259075882", "2126500872079524186"]),
    ("Gap: no lighting post.", "None among the 28: a gap in the saved material, not a statement about demand.", []),
    ("Also saved, outside these patterns:", "a humanoid robot kit, a hardware-design book, tool-shaped creature art, an unusual 3D print.",
     ["2087040759140855981", "2121739170221789433", "2122893427323056464", "2125998015592726811"]),
]
assert set(sum((ids for _, _, ids in PATTERNS), [])) == set(POST), "every post is cited at least once on slide 4"


def post_date(pid):
    """Creation date (UTC) of an X post from its id: the top bits are milliseconds since 2010-11-04 01:42:54.657 UTC."""
    ms = (int(pid) >> 22) + 1288834974657
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def credit(pid, lead="Saved post"):
    """Credit line for one image: X handle and post URL, plus the appendix number."""
    p = POST[pid]
    return f'{esc(lead)}: @{esc(p["handle"])} &middot; x.com/{esc(p["handle"])}/status/{pid}{fn("x_" + pid)}'


def rule_card(n, title, text, pid, why):
    return (f'<div class="step rule"><img class="thumb" src="images/{pid}.jpg" alt=""><div><div class="h" style="margin:0">{n}. {esc(title)}</div>'
            f'<div class="d">{esc(text)}</div><div class="credit-line">{credit(pid, "Saved post (" + why + ")")}</div></div></div>')


def chart_counts(w, title):
    """Posts per category: a small horizontal count bar (observation, not a measurement)."""
    rows = sorted(((c, sum(1 for p in POSTS if p["cat"] == c)) for c in CATS), key=lambda r: -r[1])
    h = 22 + 13 * len(rows) + 4
    out = [txt(0, 12, title, 12, INK, weight=600)]
    vmax = max(v for _, v in rows)
    lab_x, bar_x = 96, 104
    bar_w = w - bar_x - 48
    for i, (lab, v) in enumerate(rows):
        y = 22 + i * 13
        gap = lab == "Lighting"
        out.append(txt(lab_x, y + 9, lab.replace("Displays and e-ink", "Displays, e-ink"), 9, INK2, "end"))
        bw = bar_w * v / vmax
        if v:
            out.append(rect(bar_x, y + 1.5, bw, 9, ACCENT if gap else GREY_MARK, rx=2))
        out.append(txt(bar_x + bw + 6, y + 9, f"{v} post" + ("" if v == 1 else "s"), 9, ACCENT if gap else INK2, "start", 700))
    return svg(w, h, "".join(out))


def s_inspiration():
    cells = []
    for pid in FEATURED:
        p = POST[pid]
        cells.append(f'<div class="cell"><img src="images/{pid}.jpg" alt="">'
                     f'<div class="cap"><span class="cat">{esc(p["cat"])}</span>{esc(p["what"])}</div>'
                     f'<div class="credit">@{esc(p["handle"])} &middot; posted {post_date(pid)}{fn("x_" + pid)}<br>x.com/{esc(p["handle"])}/status/{pid}</div></div>')
    grid = f'<div class="mood">{"".join(cells)}</div>'
    items = [f'<li><b>{esc(t)}</b> {esc(s)}{fn(*["x_" + i for i in ids]) if ids else ""}</li>' for t, s, ids in PATTERNS]
    dates = sorted(post_date(p["id"]) for p in POSTS)
    right = (f'<div class="label">Patterns in the {len(POSTS)} posts (observation, not a measurement)</div>'
             f'<ul class="pat">{"".join(items)}</ul><div style="margin-top:6px">{chart_counts(338, f"The {len(POSTS)} posts by category (observation)")}</div>')
    return slide(4, "Product: the inspiration", "Inspiration: what the founder keeps saving, and the patterns in it",
                 f'<div class="cols" style="grid-template-columns:798px minmax(0,1fr);gap:24px"><div>{grid}</div><div>{right}</div></div>',
                 f"Images belong to their authors: private reference, not for publication. The {len(POSTS)} posts were saved {dates[0]} to {dates[-1]}; patterns are observations, not a market measurement. Post dates are decoded from the post ids.")


def s_concept():
    # brand house: roof, three pillars, two foundation layers
    d = [arrow_defs()]
    W, H = 560, 392
    d.append(f'<path d="M 20 70 L 280 12 L 540 70 Z" fill="{DARK_MARK}"/>')
    d.append(txt(280, 58, "One name. One promise: objects for a considered home.", 12.5, PAPER, "middle", 600))
    px = [30, 205, 380]
    for i, (fam, desc, items) in enumerate(FAMILIES):
        x = px[i]
        d.append(rect(x, 82, 150, 150, PANEL, rx=6, stroke=HAIR))
        d.append(txt(x + 75, 104, fam, 13.5, INK, "middle", 700, SERIF))
        for j, (kind, name, _) in enumerate(items):
            d.append(f'<g transform="translate({x + 8 + j * 46:.1f} 114) scale(0.36)">{obj_inner(kind)}</g>')
        for j, (kind, name, _) in enumerate(items):
            for k, t in enumerate(wrap(name, 9)[:2]):
                d.append(txt(x + 8 + j * 46 + 21.6, 168 + k * 10.5, t, 8.5, INK2, "middle"))
        d.append(txt(x + 75, 214, "3 objects at launch [placeholder]", 8.5, MUTED, "middle"))
    d.append(rect(20, 244, 520, 54, "#efe9dc", rx=6, stroke=HAIR))
    d.append(txt(280, 264, "Shared design language", 12.5, INK, "middle", 700))
    d.append(txt(280, 282, "materials (wood, lacquer: lead under discussion), colour, typography, packaging, naming", 10.5, INK2, "middle"))
    d.append(rect(20, 306, 520, 54, "#efe9dc", rx=6, stroke=ACCENT, sw=1.5))
    d.append(txt(280, 326, "Shared layer", 12.5, ACCENT, "middle", 700))
    d.append(txt(280, 344, "one account and app, optional AI on the objects that gain from it, limited editions, gifting", 10.5, INK2, "middle"))
    d.append(txt(0, H - 6, "The brand is the product. Any two objects should look right together.", 10, MUTED))
    house = svg(W, H, "".join(d))

    f = [arrow_defs(name="a2")]
    steps = [("Discover", "a drop, a story or a gift"), ("Pre-order", "orders fund the batch"), ("Unbox", "packaging is part of the design"), ("Add the next object", "same family, same look")]
    bw, bh, gap = 108, 74, 24
    for i, (t, s) in enumerate(steps):
        x = i * (bw + gap)
        f.append(box(x, 10, bw, bh, t, s, accent=(i == 3), size=12, subsize=9.5))
        if i < 3:
            f.append(arrow(x + bw + 2, 10 + bh / 2, x + bw + gap - 2, 10 + bh / 2, name="a2"))
    lx = 3 * (bw + gap) + bw / 2
    f.append(path(f"M {lx:.1f} {10 + bh + 2} L {lx:.1f} {10 + bh + 26} L {bw / 2:.1f} {10 + bh + 26} L {bw / 2:.1f} {10 + bh + 6}", INK2, width=1.5, extra='marker-end="url(#a2)"'))
    f.append(txt((lx + bw / 2) / 2, 10 + bh + 22, "the basket grows with every object", 10, MUTED, "middle"))
    flow = svg(500, 130, "".join(f))
    rules = f'''
<div class="label" style="margin-top:6px">Three brand rules (draft, Oscar's call), each beside a post the founder saved</div>
<div class="steps" style="grid-template-columns:1fr;gap:8px">
  {rule_card(1, "Beautiful first", "The object earns its place on a shelf with the power off.", "2123854155856880066", "ceramics")}
  {rule_card(2, "Smart only where it helps", "Software is optional and never gates the object. A third of the collection has no electronics.", "2125588103276720393", "a bookcase with one small smart function")}
  {rule_card(3, "One family", "A new object is judged by whether it belongs with the others.", "2125257053341966427", "five promptable devices in one design language")}
</div>'''
    right = f'<div class="label">How a customer lives with the brand</div>{flow}{rules}'
    left = f'<div class="label">The brand house</div>{house}'
    return slide(3, "Product: the brand", "The product is the brand: one design language across decorations, gadgets and light",
                 f'<div class="cols" style="grid-template-columns:560px minmax(0,1fr);gap:40px"><div>{left}</div><div>{right}</div></div>',
                 "Object renders are flat placeholders for the real renders. Brand rules are drafts for Oscar's edit. Thumbnails are saved posts, credited beside each rule and on slide 4.")


# ---------------------------------------------------------------- v3 market data (inputs and formulas: research.md section 7)
# Every input below is a published figure (tag in research.md) except those marked ASSUMPTION.
GMI_TOTAL, GMI_FURN = 680.6, 391.5                      # US$ bn, 2025 (GMI)
NONFURN = (GMI_TOTAL - GMI_FURN) / GMI_TOTAL            # 42.5%: global non-furniture share, applied to every region (ASSUMPTION)
REGIONS = ["North America", "Europe", "Asia-Pacific", "Latin America", "Middle East & Africa"]
GMI_REG = dict(zip(REGIONS, [195.3, 188.5, 215.1, 47.6, 34.0]))                 # GMI 2025
FBI_REG = dict(zip(REGIONS, [273.09, 124.99, 369.44, 10.27, 24.47]))            # Fortune BI 2025 (Latin America = South America)
GMI_CN, GMI_JP, FBI_CN26, FBI_JP26 = 82.8, 38.7, 226.63, 56.47                  # China and Japan inside Asia-Pacific
PM_SHARE = dict(zip(REGIONS, [31, 27, 39, None, None]))                         # Persistence, 2026 shares, %
MR_SHARE = dict(zip(REGIONS, [41.81, None, None, None, None]))                  # Mordor, 2026 shares, %
TOT_FBI, TOT_PM, TOT_MR = 802.26, 859.9, 716.5
SL_TOTAL, SP_TOTAL = 9.86, 16.29                        # smart lighting (MarketsandMarkets), portable Bluetooth speakers (Fortune BI), 2025
SL_SH = dict(NA=0.38, EU=0.29, AP=0.25, RW=0.08)        # Fortune BI smart lighting regional shares, applied to the MarketsandMarkets total (ASSUMPTION)
_sp = dict(NA=0.34, EU=0.29, AP=0.27, RW=0.04)          # Fortune BI speaker shares: the four stated shares add to 94%, so normalised (ASSUMPTION)
SP_SH = {k: v / sum(_sp.values()) for k, v in _sp.items()}
LATAM_OF_RW = GMI_REG["Latin America"] / (GMI_REG["Latin America"] + GMI_REG["Middle East & Africa"])   # split of "rest of world" (ASSUMPTION)
ONLINE_SH = 0.415                                       # GMI global online share of decor, 2025 (applied to every region: ASSUMPTION)
PREMIUM_SH = 55 / 188.5                                 # GMI Europe mid-to-high share of European decor, 29% (applied to every region: ASSUMPTION)
FX = 1.0975                                             # US$ per EUR, ECB reference rate, 26 Nov 2026


def region_table():
    rows = {}
    rw = SL_TOTAL * SL_SH["RW"] + SP_TOTAL * SP_SH["RW"]
    gad = {"North America": SL_TOTAL * SL_SH["NA"] + SP_TOTAL * SP_SH["NA"], "Europe": SL_TOTAL * SL_SH["EU"] + SP_TOTAL * SP_SH["EU"],
           "Asia-Pacific": SL_TOTAL * SL_SH["AP"] + SP_TOTAL * SP_SH["AP"], "Latin America": rw * LATAM_OF_RW, "Middle East & Africa": rw * (1 - LATAM_OF_RW)}
    for r in REGIONS:
        exf = GMI_REG[r] * NONFURN
        rows[r] = dict(all=GMI_REG[r], fbi=FBI_REG[r], exf=exf, gad=gad[r], scope=exf + gad[r],
                       online=exf * ONLINE_SH, prem=exf * ONLINE_SH * PREMIUM_SH)
    return rows


REG = region_table()
WORLD_EXF = GMI_TOTAL - GMI_FURN                        # 289.1, GMI's own totals
WORLD_GAD = SL_TOTAL + SP_TOTAL                         # 26.2 upper bound, overlap with decor lighting unknown
WORLD_SCOPE = WORLD_EXF + WORLD_GAD                     # 315.3
WORLD_ONLINE = WORLD_EXF * ONLINE_SH
WORLD_PREM = WORLD_ONLINE * PREMIUM_SH

# funnel (households), world ceiling and the Spain, France, Germany beachhead
W_HH = 2.2e9                                            # world households (secondary site citing UN DESA)
R_NET, R_BUY = 0.76, 0.562                              # ITU internet use; DataReportal weekly online buyers among internet users 16+
R_HOME, R_PREM, CAP_LO, CAP_HI = 0.19, 0.10, 0.01, 0.03 # Eurostat 3-month rate (applied); premium share and capture (ASSUMPTIONS)
SPEND_EUR = 120                                         # ASSUMPTION, as in v2
W_STEPS = [W_HH, W_HH * R_NET * R_BUY]
W_STEPS.append(W_STEPS[1] * R_HOME)
W_STEPS.append(W_STEPS[2] * R_PREM)
W_CUST = (W_STEPS[3] * CAP_LO, W_STEPS[3] * CAP_HI)
B_STEPS = [92.5e6, 72.8e6]                              # v2: ES 19.75M + FR 30.9M + DE 41.8M; Eurostat online-buyer rates 70.8%, 80.2%, 81.4%
B_STEPS.append(B_STEPS[1] * R_HOME)
B_STEPS.append(B_STEPS[2] * R_PREM)
B_CUST = (B_STEPS[3] * CAP_LO, B_STEPS[3] * CAP_HI)
W_REV = tuple(c * SPEND_EUR * FX for c in W_CUST)       # US$
B_REV = tuple(c * SPEND_EUR * FX for c in B_CUST)
B_MIDHIGH = 11.0 + 4.4 + 0.1345 * 55                    # GMI: Germany, Spain, France (13.45% of 55): US$ bn, incl. furniture


def f3(v):
    """Three significant digits with a unit suffix: 2.2B, 940M, 92.5M, 13.8k."""
    for div, suf in ((1e9, "B"), (1e6, "M"), (1e3, "k")):
        if v >= div:
            x = v / div
            t = f"{x:.3g}" if x < 100 else f"{x:.0f}"
            return t + suf
    return f"{v:.0f}"


def usd_m(v):
    return f"US${v/1e6:.1f}M" if v < 1e7 else f"US${v/1e6:.0f}M"


# ---------------------------------------------------------------- v3 charts
def chart_region_bars(w, rows, title, note=None):
    """rows: dicts(name, sub, all, lo, hi, exf, gad, extra). Horizontal bars per region: reported market (grey, with a range
    whisker where a second publisher gives a value for the same year) and the brand's scope (decor without furniture + gadgets)."""
    lab_x, bx0, bw = 160, 172, 330
    vmax = 380.0
    sc = bw / vmax
    y0 = 64
    out = [txt(0, 12, title, 12, INK, weight=600)]
    # legend, two rows
    lg = [(0, 30, "grey", "Home decor incl. furniture, GMI"), (250, 30, "range", "Range from GMI to Fortune BI (both 2025)"),
          (0, 46, "accent", "Decor without furniture (42.5% of GMI: assumption)"), (330, 46, "dark", "Adjacent gadgets (smart lighting, speakers)")]
    for x, y, kind, lab in lg:
        if kind == "range":
            out.append(line(x, y - 3, x + 22, y - 3, INK, 1.6))
            out.append(line(x, y - 7, x, y + 1, INK, 1.6))
            out.append(line(x + 22, y - 7, x + 22, y + 1, INK, 1.6))
            out.append(txt(x + 28, y, lab, 10, INK2))
        else:
            col = {"grey": GREY_MARK, "accent": ACCENT, "dark": DARK_MARK}[kind]
            out.append(rect(x, y - 8, 14, 9, col, rx=2))
            out.append(txt(x + 20, y, lab, 10, INK2))
    y = y0
    for r in rows:
        sub = r.get("sub", False)
        rh = 34 if sub else 54
        bh = 9 if sub else 14
        g_y = y + (3 if sub else 6)
        a_y = y + (16 if sub else 26)
        out.append(line(0, y, 700, y, HAIR, 1))
        out.append(txt(lab_x, y + rh / 2 + 4, r["name"], 10.5 if sub else 12, INK2 if sub else INK, "end", 400 if sub else 600))
        out.append(rect(bx0, g_y, r["all"] * sc, bh, GREY_MARK, rx=2))
        end_x = bx0 + r["all"] * sc
        if r.get("lo") is not None:
            lo, hi = r["lo"], r["hi"]
            xl, xh = bx0 + lo * sc, bx0 + hi * sc
            cy = g_y + bh / 2
            out.append(line(xl, cy, xh, cy, INK, 1.6))
            out.append(line(xl, cy - 5, xl, cy + 5, INK, 1.6))
            out.append(line(xh, cy - 5, xh, cy + 5, INK, 1.6))
            end_x = max(end_x, xh)
            lab = f"{r['all']:.0f} (range {lo:.0f} to {hi:.0f})"
        else:
            lab = f"{r['all']:.1f}" + (f"  {r['extra']}" if r.get("extra") else "")
        out.append(txt(end_x + 8, g_y + bh - 1, lab, 9.5 if sub else 10.5, INK2, "start", 600))
        xe = bx0
        wd = r["exf"] * sc
        out.append(rect(xe, a_y, wd, bh, ACCENT, rx=2))
        xe += wd
        if r.get("gad"):
            wg = r["gad"] * sc
            out.append(rect(xe, a_y, wg, bh, DARK_MARK, rx=2))
            xe += wg
            lab2 = f"{r['exf'] + r['gad']:.1f}  ({r['exf']:.1f} decor + {r['gad']:.1f} gadgets)"
        else:
            lab2 = f"{r['exf']:.1f}  (decor only, no gadget split found)"
        out.append(txt(xe + 8, a_y + bh - 1, lab2, 9.5 if sub else 10.5, ACCENT, "start", 700))
        y += rh
    out.append(line(0, y, 700, y, HAIR, 1))
    h = y + 10 + (len(note_lines(note, 700)) * 12 + 4 if note else 4)
    draw_note(out, note, 700, h)
    return svg(700, h, "".join(out))


def pill(x, y, label, kind):
    """SOURCED (dark, solid) or ASSUMPTION (outlined, accent) tag."""
    wd = len(label) * 6.1 + 12
    if kind == "s":
        return rect(x, y, wd, 14, DARK_MARK, rx=7) + txt(x + wd / 2, y + 10.3, label, 8.5, "#ffffff", "middle", 700)
    return rect(x, y, wd, 14, PANEL, rx=7, stroke=ACCENT, sw=1.2) + txt(x + wd / 2, y + 10.3, label, 8.5, ACCENT, "middle", 700)


def chart_funnel_pair(w, steps, revenue, title, note=None):
    """steps: dicts(label, sub, pill=(text, 's'|'a'), world=(lo, hi|None), bh=(lo, hi|None)). Centred bars (a funnel) on a log
    scale, world in dark and the beachhead in accent. revenue: dict(label, sub, pill, world, bh) drawn as text, not bars."""
    lab_w = 310
    cx = lab_w + 190
    bar_max = 360.0
    vmin, vmax = 1e4, 2.2e9
    lg0, lg1 = math.log10(vmin), math.log10(vmax)

    def W(v):
        return max(3.0, bar_max * (math.log10(v) - lg0) / (lg1 - lg0))

    y0 = 52
    row_h = 62
    out = [txt(0, 12, title, 12, INK, weight=600)]
    out.append(rect(lab_w + 4, 24, 14, 9, DARK_MARK, rx=2))
    out.append(txt(lab_w + 24, 32, "World, if the brand reached everyone (a ceiling)", 10, INK2))
    out.append(rect(lab_w + 4, 38, 14, 9, ACCENT, rx=2))
    out.append(txt(lab_w + 24, 46, "Spain, France, Germany (the beachhead)", 10, INK2))
    y = y0
    for i, st in enumerate(steps):
        out.append(line(0, y, w, y, HAIR, 1))
        out.append(txt(0, y + 16, st["label"], 12, INK, "start", 700))
        ly = y + 29
        sub_lines = wrap(st["sub"], 58)
        assert len(sub_lines) <= 3, f"funnel sub-label too long: {st['label']}"
        for t in sub_lines:
            out.append(txt(0, ly, t, 9, INK2))
            ly += 10.5
        out.append(pill(lab_w - 8 - (len(st["pill"][0]) * 6.1 + 12), y + 5, st["pill"][0], st["pill"][1]))
        for k, (val, col) in enumerate(((st["world"], DARK_MARK), (st["bh"], ACCENT))):
            lo, hi = val
            by = y + 8 + k * 23
            if hi:
                out.append(rect(cx - W(hi) / 2, by, W(hi), 15, col, rx=2, extra='opacity="0.3"'))
            out.append(rect(cx - W(lo) / 2, by, W(lo), 15, col, rx=2))
            right = cx + W(hi or lo) / 2
            out.append(txt(right + 8, by + 11.5, f"{f3(lo)} to {f3(hi)}" if hi else f3(lo), 11, col if col == ACCENT else INK2, "start", 700))
        y += row_h
    out.append(line(0, y, w, y, HAIR, 1))
    out.append(txt(0, y + 16, revenue["label"], 12, INK, "start", 700))
    ly = y + 29
    sub_lines = wrap(revenue["sub"], 58)
    assert len(sub_lines) <= 3, "funnel revenue sub-label too long"
    for t in sub_lines:
        out.append(txt(0, ly, t, 9, INK2))
        ly += 10.5
    out.append(pill(lab_w - 8 - (len(revenue["pill"][0]) * 6.1 + 12), y + 5, revenue["pill"][0], revenue["pill"][1]))
    out.append(txt(lab_w + 14, y + 26, revenue["world"], 12, INK2, "start", 700))
    out.append(txt(lab_w + 14, y + 48, revenue["bh"], 12, ACCENT, "start", 700))
    y += 64
    out.append(line(0, y, w, y, HAIR, 1))
    h = y + 8 + (len(note_lines(note, w)) * 12 + 4 if note else 4)
    draw_note(out, note, w, h)
    return svg(w, h, "".join(out))


# ---------------------------------------------------------------- v3 market slides (slides 6 and 7 since v4)
def s_market_regions():
    rows = []
    for r in REGIONS:
        d = REG[r]
        lo, hi = min(d["all"], d["fbi"]), max(d["all"], d["fbi"])
        rows.append(dict(name=r, all=d["all"], lo=lo, hi=hi, exf=d["exf"], gad=d["gad"]))
        if r == "Asia-Pacific":
            rows.append(dict(name="China, in Asia-Pacific", sub=True, all=GMI_CN, exf=GMI_CN * NONFURN, extra=f"(Fortune BI 2026: {FBI_CN26:.0f})"))
            rows.append(dict(name="Japan, in Asia-Pacific", sub=True, all=GMI_JP, exf=GMI_JP * NONFURN, extra=f"(Fortune BI 2026: {FBI_JP26:.0f})"))
    chart = chart_region_bars(
        700, rows, "US$ bn a year, 2025: what the market reports, and the part that is the brand's scope, by region",
        note=f"Regions and base: GMI {cite('gmi_decor')}; range: Fortune BI {cite('fbi_decor')}. Gadgets: smart lighting {cite('mm_light')} with regional shares from {cite('fbi_light')}; speakers {cite('fbi_spk')}. Latin America at Fortune BI is South America only.")

    def pct(v):
        return "n/s" if v is None else f"{v:.0f}%"

    trs = []
    for r in REGIONS:
        trs.append(f"<tr><td><b>{esc(r)}</b></td><td class='n'>{GMI_REG[r]/GMI_TOTAL*100:.1f}%</td><td class='n'>{FBI_REG[r]/TOT_FBI*100:.1f}%</td>"
                   f"<td class='n'>{pct(PM_SHARE[r])}</td><td class='n'>{'n/s' if MR_SHARE[r] is None else f'{MR_SHARE[r]:.1f}%'}</td></tr>")
    trs.append(f"<tr><td><b>World, US$ bn</b></td><td class='n'><b>{GMI_TOTAL:.1f}</b></td><td class='n'><b>{TOT_FBI:.1f}</b></td><td class='n'><b>{TOT_PM:.1f}</b></td><td class='n'><b>{TOT_MR:.1f}</b></td></tr>")
    table = (f'<table class="t compact"><thead><tr><th>Share of world</th><th>GMI {fn("gmi_decor")}<br>2025</th><th>Fortune BI {fn("fbi_decor")}<br>2025</th>'
             f'<th>Persistence {fn("pm_decor")}<br>2026</th><th>Mordor {fn("mordor")}<br>2026</th></tr></thead><tbody>{"".join(trs)}</tbody></table>')
    right = f'''
<div class="tile" style="border-color:{ACCENT}">
  <div class="k">The world, in the brand's scope</div>
  <div class="v accent">US${WORLD_SCOPE:.0f}bn</div>
  <div class="m"><b>{WORLD_EXF:.0f}</b> decor without furniture (GMI 681 less furniture 392){fn("gmi_decor")} + <b>{WORLD_GAD:.0f}</b> adjacent gadgets (smart lighting 9.9, speakers 16.3; overlap unknown).{fn("mm_light", "fbi_spk")}
  Decor without furniture runs from <b>US$134bn</b> (a narrow Statista segment, 2024){fn("statista_decor")} to <b>US$441bn</b> (Grand View's base, GMI's non-furniture share applied).{fn("gvr_decor")}</div>
</div>
<div class="label" style="margin:12px 0 6px 0">Publishers disagree on where the market is</div>
{table}
<p class="small" style="margin:6px 0 0 0;font-size:11px">n/s: not stated. Grand View: North America 36.7% of US$960bn in 2024.{fn("gvr_decor")} The US alone: US$162bn (GMI) or US$192bn (IMARC), furniture included.{fn("gmi_decor", "imarc_us")} We use GMI: the lowest full base with a regional split.</p>
<p class="small" style="margin:8px 0 0 0;font-size:11px"><b>Currency and base year.</b> All market figures are US$, 2025; euros are converted at EUR 1 = US${FX} (ECB, 26 Nov 2026).{fn("ecb_fx")} The 42.5% non-furniture share is GMI's global ratio applied to every region: an <b>assumption</b>.</p>'''
    return slide(6, "Market: the world, by region",
                 f"Market: about US${WORLD_SCOPE:.0f}bn a year worldwide in decor without furniture plus adjacent gadgets, by region",
                 f'<div class="cols" style="grid-template-columns:700px minmax(0,1fr);gap:28px"><div>{chart}</div><div>{right}</div></div>',
                 "Figures with * were seen in search snippets only. Region definitions differ between publishers; research.md section 7 has every figure, date and formula.")


def s_market_funnel():
    steps = [
        dict(label="Households", sub=f"World: 2.2 billion, secondary page citing UN DESA {cite('hh_world')}. ES 19.7M, FR 30.9M, DE 41.8M from national statistics {cite('es_hh', 'fr_hh', 'de_hh')}.",
             pill=("SOURCED", "s"), world=(W_STEPS[0], None), bh=(B_STEPS[0], None)),
        dict(label="Households that buy online", sub=f"World: {R_NET*100:.0f}% use the internet {cite('itu_net')} x {R_BUY*100:.1f}% buy weekly {cite('datareportal')} = {R_NET*R_BUY*100:.1f}%. ES, FR, DE: 78.7% {cite('eu_ecom')}. Person rates stand in for households.",
             pill=("SOURCED RATES", "s"), world=(W_STEPS[1], None), bh=(B_STEPS[1], None)),
        dict(label="Bought home items online", sub=f"19% of EU individuals did so in 3 months {cite('eu_19')}. That EU rate is applied to the world and to the three countries.",
             pill=("ASSUMPTION", "a"), world=(W_STEPS[2], None), bh=(B_STEPS[2], None)),
        dict(label="Premium design-object buyers", sub="10% of those. No source found; range 5% to 15%.",
             pill=("ASSUMPTION", "a"), world=(W_STEPS[3], None), bh=(B_STEPS[3], None)),
        dict(label="Customers of the brand, year 3", sub="1% to 3% of the row above. For the world this is a ceiling if the brand reached everyone, not a plan.",
             pill=("ASSUMPTION", "a"), world=W_CUST, bh=B_CUST),
    ]
    revenue = dict(label="Yearly revenue, year 3", sub=f"EUR {SPEND_EUR} a customer a year (assumption) = US${SPEND_EUR*FX:.1f} at EUR 1 = US${FX} {cite('ecb_fx')}.",
                   pill=("ASSUMPTION", "a"), world=f"World ceiling: {usd_m(W_REV[0])} to {usd_m(W_REV[1])} a year",
                   bh=f"Spain, France, Germany: {usd_m(B_REV[0])} to {usd_m(B_REV[1])} a year")
    funnel = chart_funnel_pair(
        740, steps, revenue, "From the world's households to customers, and the beachhead inside it (bar widths on a log scale)",
        note="Each step narrows by the ratio in its label. Bar widths are logarithmic, so they show the order of magnitude, not the proportion. Not a forecast.")
    trs = []
    for r in REGIONS:
        d = REG[r]
        trs.append(f"<tr><td><b>{esc(r)}</b></td><td class='n'>{d['exf']:.1f}</td><td class='n'>{d['online']:.1f}</td><td class='n'>{d['prem']:.1f}</td></tr>")
    trs.append(f"<tr><td><b>World</b></td><td class='n'><b>{WORLD_EXF:.1f}</b></td><td class='n'><b>{WORLD_ONLINE:.1f}</b></td><td class='n'><b>{WORLD_PREM:.1f}</b></td></tr>")
    table = (f'<table class="t compact"><thead><tr><th>US$ bn, 2025</th><th>Decor without furniture</th><th>Sold online<br>x 41.5%</th><th>Premium tier<br>x {PREMIUM_SH*100:.1f}%</th></tr></thead><tbody>{"".join(trs)}</tbody></table>')
    share_hh = B_STEPS[0] / W_STEPS[0] * 100
    share_prem = B_STEPS[3] / W_STEPS[3] * 100
    # the observation sentence is kept short on purpose: at most three lines at 11 px in this column (about 65 characters a line;
    # on Innovator's render of 27 Nov 2026 the two-line tile ended 65 px above the footer rule, so a third line leaves about 51 px).
    # The citations: the PC case (wider market), the bookcase and the $25 camera (cheap hardware plus an app), the ESP32 board.
    # Four footnote numbers at 9 px take about 12 characters of the 11 px line, counted in the budget below ("modular" left the
    # third reading on 28 Nov to pay for the fourth number; the appendix entry still says the board is modular).
    observation = ("Three readings from saved posts (slide 4): a wider market than tech people; cheap hardware plus an app sells; "
                   "an AMOLED board with voice sells off the shelf from China.")
    assert len(observation) + 12 <= 185, "slide 7 observation plus its four footnote numbers must stay within three lines"
    right = f'''
<div class="label" style="margin-bottom:6px">The same funnel in dollars, by region</div>
{table}
<p class="small" style="margin:4px 0 0 0;font-size:10.5px"><b>ASSUMPTION:</b> the 42.5% non-furniture share, the 41.5% online share{fn("gmi_decor")} and the {PREMIUM_SH*100:.1f}% premium share{fn("gmi_eu_mh")} each come from one publisher and are applied to every region. Gadgets are left out (no premium split found). Latin America and Middle East and Africa are thinly sourced.</p>
<div class="tile" style="margin-top:6px">
  <div class="k">The beachhead in dollars</div>
  <div class="m">Germany 11.0 + Spain 4.4 + France 7.4 = <b>US${B_MIDHIGH:.1f}bn</b> of mid-to-high decor (US$50 to 1,000 an item), furniture included. <b>SOURCED</b>, GMI; France is 13.45% of 55, my arithmetic.{fn("gmi_eu_mh")}</div>
</div>
<div class="tile" style="margin-top:6px">
  <div class="k">Checks (my arithmetic)</div>
  <div class="m">The three countries hold <b>{share_hh:.1f}%</b> of the world's households but <b>{share_prem:.1f}%</b> of the premium buyers in the funnel, because they shop online more. Not found: regional household counts from a primary source.</div>
</div>
<div class="tile" style="margin-top:6px">
  <div class="k">What the saved posts add (observation)</div>
  <div class="m">{esc(observation)}{fn("x_2125946257852285039", "x_2125588103276720393", "x_2126374876135231971", "x_2126078769483985199")}</div>
</div>
'''
    return slide(7, "Market: from the world to customers",
                 f"Market funnel: from 2.2 billion households to {round(B_CUST[0], -3)/1e3:.0f},000 to {round(B_CUST[1], -3)/1e3:.0f},000 customers in the three-country beachhead",
                 f'<div class="cols" style="grid-template-columns:740px minmax(0,1fr);gap:24px"><div>{funnel}</div><div class="tight">{right}</div></div>',
                 "SOURCED: published, measured on that population. ASSUMPTION: our choice, to replace with pilot data. * unverified: snippet or secondary page.",
                 extra_class="t2")


def s_competition():
    pts = [
        # design-led electronics and lighting
        dict(name="Teenage Engineering", x=0.55, y=0.85, kind="tech", dy=-9, dx=-4),
        dict(name="B&O", x=0.45, y=0.92, kind="tech", dx=-9, dy=-8, anchor="end"),
        dict(name="Devialet", x=0.50, y=0.78, kind="tech", dx=-9, anchor="end"),
        dict(name="Nothing", x=0.80, y=0.70, kind="tech", dy=-9, dx=-6),
        dict(name="Marshall", x=0.30, y=0.60, kind="tech", dy=14, dx=-8),
        dict(name="Lexon", x=0.35, y=0.66, kind="tech", dx=9, dy=-4),
        dict(name="Samsung Frame", x=0.75, y=0.55, kind="tech", dx=9),
        dict(name="Sonos", x=0.80, y=0.49, kind="tech", dx=9, dy=-6),
        dict(name="Ember", x=0.60, y=0.50, kind="tech", dx=-9, anchor="end"),
        dict(name="Nanoleaf", x=0.92, y=0.40, kind="tech", dx=-9, dy=14, anchor="end"),
        dict(name="Philips Hue", x=0.85, y=0.45, kind="tech", dx=-9, dy=-4, anchor="end"),
        dict(name="Xiaomi", x=0.90, y=0.30, kind="tech", dx=-9, anchor="end"),
        dict(name="Govee", x=0.92, y=0.22, kind="tech", dx=-9, anchor="end"),
        # design furnishing and objects
        dict(name="Vitra", x=0.02, y=0.95, kind="object", dx=9),
        dict(name="Alessi", x=0.02, y=0.85, kind="object", dx=9),
        dict(name="Flos", x=0.16, y=0.90, kind="object", dx=9, dy=-6),
        dict(name="HAY, Muuto", x=0.05, y=0.75, kind="object", dx=9),
        dict(name="Muji", x=0.15, y=0.65, kind="object", dx=9),
        dict(name="Ferm Living", x=0.02, y=0.57, kind="object", dx=9),
        dict(name="Zara Home", x=0.02, y=0.36, kind="object", dx=9),
        dict(name="Maisons du Monde", x=0.02, y=0.28, kind="object", dx=9),
        # channels
        dict(name="MoMA Design Store", x=0.03, y=0.80, kind="channel", dx=9, dy=14),
        dict(name="Etsy", x=0.03, y=0.44, kind="channel", dx=9),
        dict(name="This brand (aim)", x=0.40, y=0.12, kind="us", dx=12, dy=4, span=(0.0, 0.78)),
    ]
    scatter = chart_scatter_map(
        548, 486, pts, ("Fixed object", "Shaped by software"), ("Mass utility", "Museum-grade design"),
        "Who sits where (positions are our reading, opinion)",
        [("tech", "Design-led electronics"), ("object", "Design furnishing"), ("channel", "Channel"), ("us", "This brand")],
        note="This brand aims to span from fixed decor to smart objects at a premium design level. Scores for the other brands are opinion, not measured.")
    rows = [
        ("Teenage Engineering", "EP-133 £299", "SEK 361M, EBITDA SEK 7.7M (FY2025)", "Revenue about -18%; founder says synths will stop", fn('te', 'te_synth')),
        ("Nothing", "CMF Watch Pro 2 EUR 69", "over US$500M (2024)", "US$200M Series C, Sept 2025", fn('nothing')),
        ("Marshall Group", "Emberton III US$180", "SEK 4.0bn, 19% adj. op. margin (2023)", "Growing", fn('marshall')),
        ("Bang & Olufsen", "n/a", "DKK 2.55bn, gross margin 55.0%, EBIT 1.0%", "346 own stores, net -41; thin profit", fn('bo')),
        ("Nanoleaf", "Shapes kit US$120", "US$30.9M (2025), net loss US$1.7M", "Sold for about US$40.5M, 1.3x revenue", fn('nanoleaf')),
        ("Muji", "clocks EUR 40 to 60", "JPY 785bn, op. margin 9.4% (FY Aug 2025)", "Growing, 1,412 stores: closest on range", fn('muji')),
        ("Lexon (BOW Group)", "Oblio US$80", "not found", "Design gadgets and gifts: closest on gadgets", fn('lexon')),
        ("Inanimate", "n/a", "not researched", "Five promptable desk devices under one name, orderable; seen in one saved post (slide 4)", fn('x_2125257053341966427')),
        ("HAY", "lamp US$99 to 115", "DKK 1.22bn (FY May 2025)", "MillerKnoll majority-owned; no electronics", fn('hay')),
        ("Maisons du Monde", "n/a", "EUR 947M (2025), loss EUR 406M", "Creditors take over, June 2026", fn('mdm')),
    ]
    trs = "".join(f"<tr><td><b>{esc(a)}</b></td><td class='n'>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}{e}</td></tr>" for a, b, c, d, e in rows)
    table = f'''<table class="t compact"><thead><tr><th>Brand</th><th>Hero price</th><th>Scale and margin</th><th>Outcome, Nov 2026</th></tr></thead><tbody>{trs}</tbody></table>
<div class="card" style="margin-top:10px;padding:10px 12px;border-color:{ACCENT}"><p class="small" style="margin:0 0 4px 0;font-size:12px"><b class="accent">The gap.</b> Among more than 25 brands checked, none shows decorations, gadgets and interior oddities under one name, one design language and one software layer. Muji has the range, Lexon the gadgets, Nothing and Teenage Engineering the design language. Absence in a public search is our reading, not proof. One saved post shows a small studio with five promptable desk devices under one name (slide 4): gadgets only, no decorations, scale not researched.</p>
<p class="small" style="margin:0;font-size:12px"><b>Also in the record:</b> Made.com (administration 2022){fn('made')}, Devialet (debt procedure 2024){fn('devialet')}, IKEA x Sonos Symfonisk (ended 2025).{fn('symfonisk')} Opinion: scale in home goods is hard; survivors have a clear design identity.</p></div>'''
    return slide(8, "Competition", "Competition: strong brands for each kind of object, and none that does decorations, gadgets and light as one family",
                 f'<div class="cols" style="grid-template-columns:548px minmax(0,1fr);gap:26px"><div>{scatter}</div><div>{table}</div></div>',
                 "Prices and outcomes as published at the dates in research.md section 2. Figures with * were seen in search snippets only.")


def s_problem():
    d = [arrow_defs()]
    W = 560
    cols = [
        ("Design furnishing", "HAY, Alessi, Muji", "Taste and materials", "No electronics, no software"),
        ("Gadgets", "Sonos, Nanoleaf, Govee", "Capability", "A spec-sheet look; one app per category"),
        ("Marketplace oddities", "Etsy, Amazon, AliExpress", "The unexpected, at a low price", "No brand, no common look, little trust"),
    ]
    bw, gap = 176, 16
    for i, (t, ex, gives, lacks) in enumerate(cols):
        x = i * (bw + gap)
        d.append(rect(x, 8, bw, 150, PANEL, rx=6, stroke=HAIR))
        d.append(txt(x + bw / 2, 30, t, 14, INK, "middle", 700, SERIF))
        d.append(txt(x + bw / 2, 46, ex, 10, MUTED, "middle"))
        d.append(txt(x + 12, 76, "GIVES", 9, MUTED, "start", 700))
        for k, ln in enumerate(wrap(gives, 26)):
            d.append(txt(x + 12, 91 + k * 13, ln, 11.5, INK))
        d.append(txt(x + 12, 118, "LACKS", 9, ACCENT, "start", 700))
        for k, ln in enumerate(wrap(lacks, 26)):
            d.append(txt(x + 12, 133 + k * 13, ln, 11.5, INK2))
    d.append(rect(0, 172, W - 8, 44, ACCENT, rx=6))
    d.append(txt((W - 8) / 2, 190, "The gap: one considered brand that does all three as one family", 13.5, "#ffffff", "middle", 700))
    d.append(txt((W - 8) / 2, 207, "our reading (opinion), drawn from the competition check on slide 8", 10, "#f3d9d2", "middle"))
    gap_svg = svg(W, 224, "".join(d))
    left = f'''
<div class="label">The problem</div>
{gap_svg}
<ul style="margin-top:12px">
  <li>52% of do-it-yourself smart home users report setup or connectivity problems.{fn('parks52')}</li>
  <li>55% of surveyed Brits hold at least three unused devices, and 37.9% keep old tech in a drawer.{fn('backmarket')} The world produced 62 million tonnes of e-waste in 2022; 22.3% was documented as recycled.{fn('itu')}</li>
</ul>
<div class="card" style="margin-top:8px;padding:9px 12px"><p class="small" style="margin:0"><b>What we do not claim.</b> Design is not why people buy smart-home gear: in one 2023 survey, aesthetic design ranked last of the features tested (sample not stated).{fn('futuresource')} Our bet is narrower: design wins where people shop for decor, and the smart layer is an option, not the reason to buy.</p></div>'''
    llm = chart_line_log(
        562, 216,
        [dict(name="GPT-4-class capability", color=ACCENT, pts=[
            (2023.20, 37.5, "GPT-4, $37.50"), (2023.85, 15.0, "GPT-4 Turbo, $15"),
            (2024.37, 7.5, "GPT-4o, $7.50"), (2025.10, 0.18, "Gemini 2.0 Flash, $0.18")])],
        y_ticks=[0.1, 1, 10, 100], x_ticks=[(2023.2, "Mar 2023"), (2024.0, "2024"), (2025.1, "Feb 2025")],
        title="Cheapest price to run a GPT-4-class model, USD per million tokens (log scale)",
        unit_label="USD / 1M tokens",
        note=f"Epoch AI series {cite('epoch')}; about 208x cheaper in two years (our arithmetic). a16z: about 10x a year at equal capability {cite('a16z')}.")
    online = chart_bars(214, 196, ["2019", "2022", "2025"], [8.9, 13.7, 17.0],
                        title="Share sold online, %", unit="", highlight_last=True,
                        value_fmt=lambda v: f"{v:.1f}%", ymax=22, note=f"European DIY, home and garden {cite('diy_online')}")
    facts = f'''
<div class="tile" style="flex:1;min-width:0;min-height:196px">
  <div class="k">Also in place</div>
  <p class="small" style="margin:6px 0 5px 0;font-size:11.5px"><b>A cheap, open software layer.</b> MCP has over 10,000 public servers under Linux Foundation governance;{fn('lf_mcp')} Gemma 3n runs in 2 to 3 GB;{fn('gemma')} Espressif has shipped over 1.5 billion Wi-Fi chips.{fn('espressif')}</p>
  <p class="small" style="margin:0 0 5px 0;font-size:11.5px"><b>Pre-orders work for design objects.</b> Peak Design's Roller Pro raised US$12.9M from 23,461 backers on Kickstarter in 2025.{fn('peak')}</p>
  <p class="small" style="margin:0;font-size:11.5px"><b>Import rules changed.</b> The EUR 150 duty exemption ended 1 Jul 2026; EUR 3 per item applies to small parcels.{fn('eu_duty')}</p>
</div>'''
    right = f'''
<div class="label">Why now</div>
{llm}
<div style="display:flex;gap:18px;margin-top:10px;align-items:flex-start"><div style="flex:none">{online}</div>{facts}</div>'''
    return slide(2, "Problem and why now", "The problem: home objects are either well made and mute, or capable and anonymous",
                 f'<div class="cols c2"><div>{left}</div><div>{right}</div></div>',
                 "Figures with * were seen in search snippets only. Sources are numbered in the appendix; research.md has the dates and tags.")


def s_business():
    d = [arrow_defs()]
    nodes = [
        ("Design in Europe", "one language across every object; the part that is ours"),
        ("Pre-orders and drops", "orders fund each batch; only after Oscar's gate"),
        ("ODM build in Shenzhen", "MOQ, tooling, certification; commodity inside"),
        ("Bulk freight to an EU warehouse", "duty and VAT paid once, not per parcel"),
        ("Sell direct, later wholesale", "own site first; gift and design retail after"),
        ("Optional software tier", "only on the smart objects; never gates the object"),
    ]
    bw, gap, y0 = 172, 25.6, 8
    for i, (t, s) in enumerate(nodes):
        x = i * (bw + gap)
        d.append(box(x, y0, bw, 88, t, s, accent=(i in (0, 5)), size=12.5, subsize=10))
        if i < 5:
            d.append(arrow(x + bw + 2, y0 + 44, x + bw + gap - 2, y0 + 44))
    d.append(path(f"M {5*(bw+gap)+bw/2:.1f} {y0+90} L {5*(bw+gap)+bw/2:.1f} {y0+112} L {bw/2:.1f} {y0+112} L {bw/2:.1f} {y0+94}", INK2, width=1.5, extra='marker-end="url(#arr)"'))
    d.append(txt(1160 / 2, y0 + 108, "the loop: what customers buy and ask for shapes the next object", 10, MUTED, "middle"))
    flow = svg(1160, 128, "".join(d))

    unit = chart_stacked_hbar(
        372, 236, "Where a retail price goes (structure, not a forecast)", "Retail price = 100%; unit cost awaits an ODM quote.",
        [("Unit cost: one third, the 3x rule of thumb (reported)", 0.333, DARK_MARK, False),
         ("Freight, duty, VAT, ads, returns, margin [placeholder]", 0.667, PAPER, True)],
        benchmarks=[("Peloton hw", 0.136, "middle", 1), ("Arhaus", 0.389, "end", 0), ("Sonos", 0.437, "end", 1), ("Williams-Sonoma", 0.462, "start", 0),
                    ("B&O", 0.55, "start", 1), ("Tonies", 0.628, "start", 2)],
        note=f"3x rule {cite('rule3x')}. Margins: Peloton {cite('peloton')}, Arhaus {cite('arhaus')}, Sonos {cite('sonos')}, Williams-Sonoma {cite('ws')}, B&O {cite('bo')}, Tonies {cite('tonies')}.")
    route = chart_hbars(
        372, 112, [("Direct online", 82.6, "net of 21% Spanish VAT"), ("Wholesale", 41.3, "keystone: half the net price")],
        title="Brand keeps, from a EUR 100 shelf price", lab_w=140, value_fmt=lambda v: f"EUR {v:.1f}", vmax=100, accent_idx=0, sub_size=9,
        note=f"Our arithmetic. VAT {cite('vat')}; keystone convention {cite('keystone')}.")
    col1 = f'''<div class="label">Unit economics</div>{unit}'''
    col2 = f'''
<div class="label">Two routes, and the cost of an order</div>
{route}
<p class="small" style="margin:8px 0 6px 0"><b>Ad cost per order, our arithmetic.</b> A click costs about US$0.60 (Meta, all industries, 2026){fn('meta')} and home and furniture sites convert about 1.29% of visits.{fn('cvr')} That is roughly <b>US$47 of ads per order</b>, against EUR 82.6 kept on a EUR 100 direct sale (currencies not converted). Online orders come back 19.3% of the time.{fn('nrf')}</p>
<p class="small" style="margin:0"><b>So (opinion):</b> direct sales need a price premium and repeat purchases. A family of objects that look right together can raise the basket without raising the ad cost.</p>'''
    col3 = f'''
<div class="label">Evidence for the model</div>
<ul class="small" style="padding-left:16px">
  <li><b>Object plus repeat purchase.</b> Tonies, a design-led object brand: EUR 630M revenue in 2025, 62.8% gross margin, 71% of revenue from the add-on figurines, not the box.{fn('tonies')}</li>
  <li><b>Optional software tier.</b> The category pays US$79 a year (Skylight Plus){fn('skylight')} or EUR 39.90 (reMarkable Connect).{fn('remarkable')}</li>
  <li><b>Pre-orders.</b> Roller Pro: US$12.9M, 23,461 backers.{fn('peak')} But more than three quarters of crowdfunded hardware ships late.{fn('mollick')}</li>
  <li><b>Build.</b> ODM MOQ commonly 500 to 5,000 units (reported);{fn('moq')} CE, RED and FCC with a pre-certified module: US$3,000 to 8,000.{fn('cert')}</li>
  <li><b>Freight.</b> About US$0.39 per boxed unit by full container (our arithmetic, assumed box size); small brands pay far more.{fn('freight')}</li>
</ul>'''
    return slide(9, "Business model", "Business model: a premium-brand margin on a family of objects, pre-orders before the build, software only where it helps",
                 f'{flow}<div class="cols c3" style="margin-top:10px;height:auto;gap:26px"><div>{col1}</div><div>{col2}</div><div>{col3}</div></div>',
                 "The unit-cost bar shows structure under a published rule of thumb, not a forecast. Unit cost and MOQ are placeholders until the first ODM quote.")


def register_sources():
    R = reg
    # market
    R("gmi_decor", "Global Market Insights, Home decor market (global 2025 US$680.6bn, furniture US$391.5bn, online 41.5%; North America 195.3, Europe 188.5, Asia Pacific 215.1, Latin America 47.6, Middle East and Africa 34.0; China 82.8, Japan 38.7, US 162.1)", "https://www.gminsights.com/industry-analysis/home-decor-market", "Aug 2026")
    R("gvr_decor", "Grand View Research, Home decor market (2024 US$960.14bn with North America 36.7%; 2025 US$1,037bn; furniture 50.7%)", "https://www.grandviewresearch.com/industry-analysis/home-decor-market", "updated May 2026")
    R("gmi_eu_mh", "Global Market Insights, Europe mid-to-high-range home decor market (US$55bn 2025)", "https://www.gminsights.com/industry-analysis/europe-mid-to-high-range-home-decor-market", "Oct 2026")
    R("imarc_us", "IMARC, United States home decor market (US$191.5bn 2025)", "https://www.imarcgroup.com/united-states-home-decor-market-statistics", "2026-02-10")
    R("mm_light", "MarketsandMarkets, Smart lighting market (US$9.86bn 2025; commercial lighting included)", "https://www.marketsandmarkets.com/Market-Reports/smart-lighting-market-985.html", "Oct 2026")
    R("fbi_spk", "Fortune Business Insights, Portable Bluetooth speaker market (US$16.29bn 2025; North America 34%, Europe 29%, Asia Pacific 27%, rest of world nearly 4%)", "https://www.fortunebusinessinsights.com/smart-home-market-105011", "9 Nov 2026")
    R("fbi_decor", "Fortune Business Insights, Home decor market (global 2025 US$802.26bn; Asia Pacific 369.44, North America 273.09, Europe 124.99, Middle East and Africa 24.47, South America 10.27; China 226.63 and Japan 56.47 are 2026)", "https://www.fortunebusinessinsights.com/home-d-cor-market-109906", "9 Nov 2026")
    R("pm_decor", "Persistence Market Research, Home decor market (2026 US$859.9bn; Asia Pacific 39%, North America 31%, Europe 27%)", "https://www.persistencemarketresearch.com/market-research/home-decor-market.asp", "Aug 2026")
    R("mordor", "Mordor Intelligence, Home decor market (2026 US$716.5bn; North America 41.81% share in 2026)", "https://www.mordorintelligence.com/industry-reports/home-decor-market", "2026-10-22")
    R("statista_decor", "Statista Market Insights, Home decor worldwide (narrow segment, US$133.6bn in 2024; page blocked)", "https://www.statista.com/outlook/cmo/furniture/home-decor/worldwide", "2024", "s")
    R("fbi_light", "Fortune Business Insights, Smart lighting market (2025 US$27.98bn; North America 38%, Europe 29%, Asia Pacific 25%, rest of world 8%)", "https://www.fortunebusinessinsights.com/smart-lighting-market-117284", "9 Nov 2026")
    R("hh_world", "worldpopulationclock.net, about 2.2 billion households worldwide in 2025 (secondary site citing UN DESA; the UN file was not retrieved)", "https://worldpopulationclock.net/average-household-size-worldwide/", "accessed 2026-11-27", "s")
    R("itu_net", "ITU, Facts and Figures 2026: 6.3 billion people, 76% of the world, use the Internet", "https://www.itu.int/en/ITU-D/Statistics/Pages/facts/default.aspx", "2026-11")
    R("datareportal", "DataReportal, Digital Around the World: 56.2% of internet users aged 16+ buy something online every week (GWI data)", "https://datareportal.com/global-digital-overview?country=82", "2026", "s")
    R("ecb_fx", "ECB euro reference rate, US dollar: 1.0975 on 26 Nov 2026 (27 Nov not yet shown on the page)", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html", "2026-11-26")
    R("es_hh", "INE Spain, households on 1 Jan 2026 (19,746,638)", "https://ine.es/dyngs/Prensa/en/ECP4T25.htm?print=1", "2026-02-12")
    R("fr_hh", "INSEE, households (about 30.9M on 1 Jan 2022; no later figure found)", "https://www.insee.fr/fr/statistiques/8612510", "2025-11-18")
    R("de_hh", "Destatis, private households 2024 (41.8M)", "https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/11/PD26_386_122.html", "2026-11-05")
    R("eu_ecom", "Eurostat, individuals who bought online in the last 12 months, 2025 (isoc_ec_ib20: DE 81.4%, FR 80.2%, ES 70.8%)", "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ec_ib20?format=JSON&geo=ES&geo=FR&geo=DE&geo=EU27_2020&ind_type=IND_TOTAL&unit=PC_IND&sinceTimePeriod=2024", "2025")
    R("eu_19", "Eurostat news, 19% of EU individuals bought furniture, home accessories or garden items online in 3 months", "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250220-3", "2025-02-20")
    R("ine_epf", "INE Spain, household budget survey 2025: group 05 EUR 1,248 per household", "https://ine.es/dyngs/Prensa/en/EPF2025.htm", "2026-06-25")
    R("destatis_cons", "Destatis, consumption expenditure: interior decoration, appliances EUR 148 a month in 2024", "https://www.destatis.de/EN/Themes/Society-Environment/Income-Consumption-Living-Conditions/Consumption-Expenditure/Tables/liste-germany.html", "2024")
    R("bls_ces", "US BLS, Consumer Expenditures 2025: household furnishings and equipment US$2,355 per consumer unit (includes appliances)", "https://www.bls.gov/news.release/cesan.nr0.htm", "2026-10-29")
    # competition
    R("te", "allabolag.se, Teenage Engineering AB: revenue SEK 361.2M, EBITDA SEK 7.7M, FY2025", "https://allabolag.se/5567183719/teenage-engineering-ab", "FY2025")
    R("te_synth", "mezha.ua, Teenage Engineering to stop making synths (interview relay; year not on page; FY2024 revenue is a snippet)", "https://mezha.ua/news/teenage-engineering-to-stop-making-synths-315968/", "Oct (year not shown)", "s")
    R("nothing", "9to5Google, Nothing 2024 revenue over US$500M; TechCrunch, US$200M Series C", "https://9to5google.com/2025/01/16/nothing-expansion-funding-successful-2024-report/ ; https://techcrunch.com/2025/09/15/nothing-closes-200m-series-c-led-by-tiger-global-plans-ai-first-device-launch/", "2025-01-16; 2025-09-15")
    R("marshall", "Marshall Group, record-breaking 2023 (net sales MSEK 4,007; adjusted operating profit MSEK 757)", "https://group.marshall.com/2024/02/15/a-record-breaking-2023-and-a-new-era-for-marshall/", "2024-02-15")
    R("bo", "Bang & Olufsen, annual report 2024/25 (DKK 2,553M; gross margin 55.0%; EBIT 1.0%; 346 stores)", "https://www.inderes.dk/releases/annual-report-202425-bang-and-olufsen-reports-a-year-of-transition-achieving-record-high-gross-margin-positive-operating-profit-and-strengthened-branded-channel-performance", "2025-07-03")
    R("sonos", "Sonos, fourth quarter and fiscal 2025 results (revenue US$1,443.3M; GAAP gross margin 43.7%)", "https://investors.sonos.com/news-and-events/investor-news/latest-news/2025/Sonos-Reports-Fourth-Quarter-and-Fiscal-2025-Results/", "2025-11-05")
    R("nanoleaf", "inside.lighting and heise, Nanoleaf acquired by OneRobotics for about US$40.5M; 2025 revenue about US$30.9M", "https://inside.lighting/news/26-06/nanoleaf-acquired-40-million-deal ; https://www.heise.de/-11316733", "2026-06-03/04")
    R("muji", "Investing.com, Ryohin Keikaku FY Aug 2025 presentation (JPY 784.6B, operating profit JPY 73.8B, 1,412 stores)", "https://ng.investing.com/news/company-news/ryohin-keikaku-fy258-presentation-record-profits-as-china-sales-surge-93CH-2139136", "2025-10-10")
    R("lexon", "Lexon product page (Oblio, US$79.90) and VentureBeat on the BOW Group acquisition", "https://lexon-design.com/us/product/oblio/ ; https://venturebeat.com/business/lexon-writes-a-new-chapter-in-its-history-by-joining-bow-group", "accessed 2026-11-27; 2018", "s")
    R("hay", "SEC 10-Q (MillerKnoll stake in HAY) and Danish register for revenue DKK 1,219M FY May 2025 (register page returned 403)", "https://www.sec.gov/Archives/edgar/data/66382/000006638221000009/mlhr-20210227.htm ; https://companydata.dk/en/virksomhed/26799945-hay-aps", "2021; FY2025", "s")
    R("mdm", "L'Express Franchise, Maisons du Monde: EUR 406M loss in 2025 and rescue protocol", "https://lexpress-franchise.com/actualites/maisons-du-monde-annonce-perte-406-m-euros-en-2025-et-signature-protocole-sauvetage/", "2026-06-19")
    R("made", "TechCrunch, Next acquires Made.com's brand and IP as it enters administration", "https://techcrunch.com/2022/11/09/next-acquires-made-coms-brand-and-ip-as-the-online-furniture-retailer-enters-administration", "2022-11-09", "s")
    R("devialet", "Mac4Ever, Devialet revenue down about 20%, conciliation procedure", "https://mac4ever.com/audio/184613-devialet-va-mal-mais-a-quel-point", "2024-10-09")
    R("symfonisk", "TechRadar, Sonos and IKEA end the Symfonisk range", "https://techradar.com/audio/speakers/sonos-and-ikea-just-ended-their-unlikely-symfonisk-audio-duet-and-thats-a-real-shame", "2025-05-06", "s")
    R("price_v", "Retail pages read on 27 Nov 2026: Marshall Emberton III US$179.99; Samsung The Frame 43in US$899.99; Lexon Oblio US$79.90", "https://marshall.com/us/en/product/emberton-iii?pid=1009767 ; https://samsung.com/us/lifestyle-tvs/the-frame/43-inch-the-frame-qled-4k-tv-ls03fa-sku-qn43ls03fafxza ; https://lexon-design.com/us/product/oblio/", "2026-11-27")
    R("price_s", "Retail pages seen in snippets: HAY PC Portable, Alessi Anna G, Nanoleaf Shapes, Ember Mug 2, Muji clocks, Nothing Ear (3) and CMF Watch Pro 2, Teenage Engineering EP-133 and OB-4 (EUR)", "https://us.hay.com/lighting/pc-portable-lamp/2516116.html ; https://us.alessi.com/products/anna-g-corkscrew ; https://us-shop.nanoleaf.me/products/shapes-hexagon-smarter-kit-5pk ; https://target.com/p/ember-14oz-mug-2-white/-/A-81529010 ; https://muji.eu/products/railway-station-alarm-clock-5685 ; https://muji.eu/products/digital-clock-with-alarm-small-white-7756 ; https://galaxus.de/en/s1/product/nothing-ear-3-anc-550-h-wireless-headphones-62018402 ; https://be.nothing.tech/pages/cmf-store ; https://thomann.nl/teenage_engineering_ob_4_black_reviews.htm", "accessed 2026-11-27", "s")
    # problem and why now
    R("parks52", "Parks Associates, 52% of DIY smart home users report setup or connectivity issues", "https://www.parksassociates.com/blogs/pr-smart-home/parks-associates-52-of-diy-smart-home-users-report-setup-or-connectivity-issues", "2025-07-09")
    R("backmarket", "Back Market, unused tech survey (UK): 55% have 3 or more unused devices", "https://www.backmarket.co.uk/en-gb/c/technology/unused-tech-survey", "2025", "s")
    R("itu", "ITU, Global E-waste Monitor 2024: 62 million tonnes in 2022, 22.3% documented as recycled", "https://www.itu.int/en/mediacentre/pages/pr-2024-03-20-e-waste-recycling.aspx", "2024-03-20")
    R("futuresource", "Futuresource Consulting, what consumers want from the smart home (aesthetic design ranked last)", "https://www.futuresource-consulting.com/insights/what-consumers-want-from-the-smart-home-sophie-harding-s-post-survey-findings-2023", "2023-11-01")
    R("epoch", "Epoch AI, LLM inference price trends", "https://epoch.ai/data-insights/llm-inference-price-trends", "2025-03-12")
    R("a16z", "a16z, LLMflation", "https://a16z.com/llmflation-llm-inference-cost/", "2024-11-12")
    R("diy_online", "DIY International, e-commerce share of European DIY, home and garden (8.9% 2019, 13.7% 2022, 17% 2025)", "https://www.diyinternational.com/content/news/2026/03/24/plus/e-commerce-share-in-the-diy-sector-is-growing.html", "2026-03-24")
    R("lf_mcp", "Linux Foundation, Agentic AI Foundation formed; more than 10,000 published MCP servers", "https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation", "2025-12-09")
    R("gemma", "Google, Introducing Gemma 3n (2 to 3 GB memory footprint)", "https://developers.googleblog.com/en/introducing-gemma-3n/", "2025-05-20")
    R("espressif", "Espressif, Who we are: 1.5 billion+ IoT SoCs shipped", "https://www.espressif.com/en/company/about-us/who-we-are", "accessed 2026-11-27")
    R("peak", "Kickstarter, Peak Design raises US$13M (Roller Pro: US$12,940,078 from 23,461 backers)", "https://updates.kickstarter.com/peak-design-raises-13m-with-their-biggest-kickstarter-ever/", "2025-04-24")
    R("eu_duty", "European Commission, temporary flat duty of EUR 3 on low-value imports from 1 Jul 2026 (Regulation (EU) 2026/382)", "https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en", "2026-06-08")
    # business model
    R("rule3x", "Predictable Designs, Bolt, Sinovation: retail is 2x to 5x cost, ideally at least 3x", "https://predictabledesigns.com/how-to-price-your-new-electronic-hardware-product/ ; https://blog.bolt.io/?p=112 ; https://www.sinovationventures.com/blog/consumer-iot-start-up-advice", "undated", "s")
    R("peloton", "Peloton, Q4 FY2025 shareholder letter (connected fitness products gross margin 13.6%)", "https://www.sec.gov/Archives/edgar/data/0001639825/000163982525000132/q42025shareholderletter.htm", "2025-08-07")
    R("arhaus", "Arhaus, Form 10-K FY2025 (gross margin 38.9%)", "https://www.sec.gov/Archives/edgar/data/1875444/000187544426000010/arhs-20251231.htm", "FY2025")
    R("ws", "Williams-Sonoma, Q4 FY2025 results exhibit (gross margin 46.2%)", "https://www.sec.gov/Archives/edgar/data/719955/000071995526000030/exhibit991fy2025q4earnings.htm", "2026-03-18")
    R("tonies", "Tonies, record results 2025 (revenue EUR 630.3M, gross profit EUR 395.9M, figurines EUR 447.2M)", "https://www.mynewsdesk.com/uk/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442747", "2026-04-14")
    R("vat", "Your Europe, VAT rates (Spain 21%, France 20%, Germany 19%)", "https://www.europa.eu/youreurope/business/taxation/vat/vat-rules-rates", "checked 2026-07-13")
    R("keystone", "Faire, wholesale basics: keystone is retail at 2x wholesale", "https://faire.com/blog/selling/wholesale-basics-for-brands-makers-and-artists", "undated", "s")
    R("meta", "LocaliQ (WordStream), Facebook advertising benchmarks 2026 (traffic CPC US$0.60)", "https://localiq.com/blog/facebook-advertising-benchmarks/", "2026-09-23")
    R("cvr", "Shopify, ecommerce conversion rate (home and furniture 1.29%, Dynamic Yield)", "https://www.shopify.com/blog/ecommerce-conversion-rate", "2026-08-22")
    R("nrf", "NRF, consumers expected to return nearly US$850bn in 2025 (online return rate 19.3%)", "https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025", "2025-10-15")
    R("skylight", "Skylight support, calendar plans (Plus US$79 a year)", "https://skylight.zendesk.com/hc/en-us/articles/35984779668379-What-does-a-Skylight-Calendar-cost", "undated")
    R("remarkable", "reMarkable, Connect subscription (EUR 39.90 a year)", "https://remarkable.com/store/connect", "accessed 2026-11-27")
    R("mollick", "Mollick, The dynamics of crowdfunding (more than three quarters of projects ship late)", "https://papers.ssrn.com/abstract=2088298", "2014", "s")
    R("moq", "Cosmo Sourcing and ChinaImportal: ODM MOQ commonly 500 to 5,000 units", "https://www.cosmosourcing.com/blog/moq-meaning-minimum-order-quantity ; https://www.chinaimportal.com/?p=8724", "undated", "s")
    R("cert", "Predictable Designs, certification costs (CE, RED, FCC with a pre-certified module: US$3,000 to 8,000)", "https://predictabledesigns.com/certification-costs-what-it-really-takes/", "2026-01-17")
    R("freight", "Chemorbis, Asia to North Europe container rate about US$2,589 per 40ft (early May 2026); per-unit figure is our arithmetic", "https://www.chemorbis.com/en/premium-plastics-news/Asia-Europe-freight-rates-largely-erase-war-driven-gains-supporting-China-Europe-polymer-arbitrage/2026/05/07/971091", "2026-05-07", "s")
    # v4: the founder's saved X posts (slide 4 and the tie-ins). Handle, image and description from ../inspiration/README.md; not re-opened here.
    for p in POSTS:
        R("x_" + p["id"], f"X post by @{p['handle']}: {p['what']}", f"https://x.com/{p['handle']}/status/{p['id']}", f"posted {post_date(p['id'])}", "p")


def s_sources(start_num):
    tagname = {"v": "opened and read", "s": "unverified: search snippet or secondary page", "d": "derived", "p": "saved X post"}
    entries = []
    for i, key in enumerate(USED):
        label, url, date, tag = SRC[key]
        flag = "*" if tag == "s" else ""
        entries.append(f"<div><b>{i+1}{flag}</b>{esc(label)} <span class='muted'>({esc(date)}; {tagname[tag]})</span><br><span class='u'>{esc(url)}</span></div>")
    def est(key):
        label, url, date, tag = SRC[key]
        return 13.5 * (-(-(len(label) + len(date) + 40) // 105)) + 13.5 * (-(-len(url) // 112)) + 6
    pages, cur, h, cap = [], [], 0.0, 2 * 430 - 70
    for key, ent in zip(USED, entries):
        e = est(key)
        if cur and h + e > cap:
            pages.append(cur)
            cur, h, cap = [], 0.0, 2 * 430
        cur.append(ent)
        h += e
    if cur:
        pages.append(cur)
    out = []
    for pi, chunk in enumerate(pages):
        intro = (f'<p class="small" style="margin-bottom:8px">Every number on the slides carries one of these numbers. A star marks an unverified source: seen in a search snippet only, or a secondary page whose own source I could not open. Treat the figure as reported. Estimates and assumptions are labelled on the slides; the formulas are in <b>research.md</b>. Opinions are labelled. Placeholders are Oscar\'s inputs (brand name, renders and prices, unit cost and MOQ) or figures no source gave. Entries tagged "saved X post" come from the founder\'s saved-posts list with each post\'s first image; the posts were not re-opened for this build, and each date is decoded from the post id.</p>' if pi == 0 else "")
        body = f'{intro}<div class="src">{"".join(chunk)}</div>'
        out.append(slide(start_num + pi, "Appendix", f"Sources ({pi+1} of {len(pages)})", body, "Research of 27 Nov 2026: global market by region and funnel (v3), competition and business model, saved X posts (v4); problem and why-now evidence carried from v1."))
    return out


def main():
    register_sources()
    slides = [s_cover(), s_problem(), s_concept(), s_inspiration(), s_collection(), s_market_regions(), s_market_funnel(), s_competition(), s_business(), s_plan(), s_founder()]
    slides += s_sources(12)
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{esc(BRAND)}: gadgets pitch deck v4 (draft, 27 Nov 2026)</title>
<meta name="viewport" content="width=1280">
<style>{CSS}</style></head>
<body>
{"".join(slides)}
</body></html>'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"wrote {OUT} ({len(doc)//1024} KB, {len(slides)} slides, {len(USED)} sources)")


def s_plan():
    rows = [
        ("Idea and first calls (25 Nov)", 0.80, 0.87, "done"),
        ("Research and this deck v4 (27 Nov)", 0.87, 0.92, "done"),
        ("Collection: renders, prices (28 Nov)", 0.90, 0.97, "next"),
        ("Brand name and design language", 0.90, 1.6, "next"),
        ("Legal and admin groundwork (by 4 Dec)", 1.0, 1.15, "next"),
        ("First investor conversations", 1.0, 1.4, "next"),
        ("Pick launch objects for samples", 1.2, 1.8, "later"),
        ("Prototypes: dev boards, 3D prints", 1.6, 3.2, "later"),
        ("Gate: ads and pre-orders, when objects work", 3.2, 4.2, "gate"),
        ("ODM samples via a Shenzhen introduction", 3.6, 5.2, "later"),
        ("First drop to pre-order customers", 5.6, 7.0, "later"),
    ]
    gantt = chart_gantt(700, 400, rows, ["Nov 26", "Dec", "Jan 27", "Feb", "Mar", "Apr", "May", "Jun"],
                        "Plan (dark: done; red: next; grey: proposed, Oscar to confirm; dashed: Oscar's gate)", today_idx=0.87,
                        note="Dates after December are proposals for Oscar's edit, not commitments.")
    right = f'''
<div class="label">Where it stands, honestly</div>
<div class="steps" style="grid-template-columns:1fr;gap:10px">
  <div class="step"><div class="h">Done</div><div class="d">Idea and calls (25 Nov). Catalogue of nine objects drafted. Concept settled as one brand with a multi-category collection (27 Nov). Coffee prep. Research and this deck.</div></div>
  <div class="step"><div class="h">In hand</div><div class="d">The founder already runs a personal AI-agent setup with a data hub on the Model Context Protocol: the software layer for the smart objects exists in rough form.</div></div>
  <div class="step"><div class="h">Not yet</div><div class="d">A working unit. A sale. A brand name. An ODM quote. Final renders and prices (due 28 Nov).</div></div>
  <div class="step" style="border-color:{ACCENT}"><div class="h accent">Next milestone</div><div class="d">Two or three launch objects working in hand. Then a second meeting. Nothing public and no pre-orders until the objects work.</div></div>
</div>'''
    return slide(10, "Progress and plan", "Progress and plan: collection this week, working samples before anything else",
                 f'<div class="cols" style="grid-template-columns:700px 1fr;gap:32px"><div>{gantt}</div><div>{right}</div></div>',
                 "Plan dates beyond December 2026 are proposals for Oscar's edit.")


def s_founder():
    left = f'''
<div class="label">Founder</div>
<div style="display:grid;grid-template-columns:150px 1fr;gap:18px">
  <div class="card ph" style="height:180px;display:flex;align-items:center;justify-content:center;color:{MUTED};font-size:11px;text-align:center">photo<br>[placeholder]</div>
  <div>
    <p style="font-family:{SERIF};font-size:26px;margin:0 0 6px 0">Oscar <span class="ph">[surname placeholder]</span></p>
    <p class="small" style="margin-bottom:6px">Based in Catalonia. Builds this on his own time, solo.</p>
    <p class="small" style="margin-bottom:6px">Runs his own AI-agent setup daily since October 2026: a chief-of-staff agent, scheduled research runs and a personal data hub on the Model Context Protocol, the protocol the smart objects will use.</p>
    <p class="small" style="margin-bottom:6px">Method: research first and every number sourced; design-led; hardware sourced, brand and software owned.</p>
    <p class="small ph" style="margin:0">Education, languages, earlier projects: [placeholder for Oscar]</p>
  </div>
</div>
<div class="hr" style="margin:16px 0"></div>
<p class="small"><b>Team.</b> Solo founder today. First hires follow the first working objects: industrial design and firmware [placeholder for Oscar's plan].</p>'''
    right = f'''
<div class="label">The ask for this conversation</div>
<div class="steps" style="grid-template-columns:1fr;gap:12px">
  <div class="step"><div class="n">1</div><div class="h">Your read on the collection</div><div class="d">Of these nine objects, which would you buy at the printed price, and which never? That answer is worth more to me than a cheque today.</div></div>
  <div class="step"><div class="n">2</div><div class="h">One introduction in Shenzhen</div><div class="d">An ODM, sourcing agent or factory contact who could build a sample of a launch object next quarter.</div></div>
  <div class="step"><div class="n">3</div><div class="h">A second meeting, with a trigger</div><div class="d">When the first working object is in my hand, may I show it to you?</div></div>
</div>
<p class="small" style="margin-top:14px"><b>Not on the table today:</b> valuation, round size, equity. A working object first.</p>'''
    return slide(11, "Founder and ask", "Founder and ask",
                 f'<div class="cols c2"><div>{left}</div><div>{right}</div></div>',
                 "No valuation, round size or equity appears in this deck, by design.")


if __name__ == "__main__":
    main()

