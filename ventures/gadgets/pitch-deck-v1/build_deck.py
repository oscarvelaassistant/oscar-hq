#!/usr/bin/env python3
"""Builds deck.html (self-contained, 1280x720 slides, inline SVG charts) for the gadgets pitch deck v1.

Run: python3 -I build_deck.py   (writes deck.html next to this file)
All numbers live in the DATA section and in research.md with their sources. Placeholders are marked [placeholder].
No external assets: fonts are system fonts, charts are inline SVG, so the file prints to PDF with headless Chrome.
"""
import html
import math
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck.html")

# ---------------------------------------------------------------- style tokens
PAPER = "#f6f3ec"      # slide surface, warm paper (e-ink feel)
PANEL = "#fbf9f4"      # card surface
INK = "#17150f"        # primary ink
INK2 = "#5b5750"       # secondary ink
MUTED = "#8d8980"      # axis labels, footnotes
HAIR = "#d9d3c6"       # hairlines, grid
ACCENT = "#b8371f"     # lacquer red, the one accent (urushi lead)
GREY_MARK = "#a8a398"  # recessive marks for "others"
DARK_MARK = "#3a3630"  # second category mark
SERIF = "Georgia, 'Liberation Serif', 'DejaVu Serif', 'Times New Roman', serif"
SANS = "'Inter', 'Helvetica Neue', Helvetica, Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif"

BRAND = "[Brand name placeholder]"
DRAFT_LINE = "v1 draft for Oscar's edit, 27 Nov 2026. Private. Not for distribution."

# ---------------------------------------------------------------- DATA (filled from research.md; see sources there)
# Each entry that carries a number has a footnote id used on the slide and listed in SOURCES.
DATA = {}
SOURCES = []   # list of (id, label, url, date)


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


def circle(cx, cy, r, fill, stroke="none", sw=1):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


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


def box(x, y, w, h, title, sub=None, fill=PANEL, stroke=HAIR, accent=False, size=13, subsize=11, dashed=False, title_weight=600):
    """Rounded node with a title and optional sub-line, text wrapped to fit."""
    out = [rect(x, y, w, h, fill, rx=6, stroke=(ACCENT if accent else stroke), sw=(1.5 if accent else 1),
                extra=('stroke-dasharray="4 3"' if dashed else ""))]
    maxc = max(6, int(w / (size * 0.56)))
    tl = wrap(title, maxc)
    sl = wrap(sub, max(6, int(w / (subsize * 0.56)))) if sub else []
    total = len(tl) * (size + 3) + (len(sl) * (subsize + 3) + 4 if sl else 0)
    yy = y + h / 2 - total / 2 + size
    for t in tl:
        out.append(txt(x + w / 2, yy, t, size, ACCENT if accent else INK, "middle", title_weight))
        yy += size + 3
    if sl:
        yy += 4
        for t in sl:
            out.append(txt(x + w / 2, yy, t, subsize, INK2, "middle"))
            yy += subsize + 3
    return "".join(out)


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
    """series: list of dict(name, color, pts=[(x_float, y_float, label|None)]). Log y axis."""
    top, right, bottom, left = pad
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
        lab = f"${t:g}" if t >= 1 else f"${t:g}"
        out.append(txt(px0 - 6, Y(t) + 4, lab, 10, MUTED, "end"))
    for xv, lab in x_ticks:
        out.append(txt(X(xv), py1 + 14, lab, 10, MUTED, "middle"))
    out.append(line(px0, py1, px1, py1, "#c3bfb4", 1))
    out.append(txt(px0 - 6, py0 - 6, unit_label, 10, MUTED, "end"))
    for s in series:
        pts = sorted(s["pts"])
        d = " ".join(f"{'M' if i == 0 else 'L'} {X(x):.1f} {Y(y):.1f}" for i, (x, y, *_) in enumerate(pts))
        out.append(path(d, s["color"], width=2))
        for x, y, *lab in pts:
            out.append(circle(X(x), Y(y), 4, s["color"], PAPER, 2))
            if lab and lab[0]:
                out.append(txt(X(x) + 7, Y(y) - 7, lab[0], 10, INK2))
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
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
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
    return svg(w, h, "".join(out))


def chart_funnel(w, h, steps, title, note=None):
    """steps: list of (label, value, sublabel). Horizontal bars, widths proportional to log-ish scale for readability: use sqrt."""
    out = [txt(0, 12, title, 12, INK, weight=600)]
    n = len(steps)
    top = 26
    rowh = (h - top - (16 if note else 4)) / n
    vmax = steps[0][1]
    lab_w = 250
    bar_x0 = lab_w
    bar_wmax = w - lab_w - 90
    for i, (lab, v, sub) in enumerate(steps):
        y = top + i * rowh
        bw = max(6, bar_wmax * math.sqrt(v / vmax))
        col = ACCENT if i == n - 1 else (DARK_MARK if i == 0 else GREY_MARK)
        out.append(rect(bar_x0, y + 6, bw, rowh - 12, col, rx=3))
        out.append(txt(bar_x0 - 10, y + rowh / 2 - 2, lab, 12, INK, "end", 600))
        if sub:
            out.append(txt(bar_x0 - 10, y + rowh / 2 + 12, sub, 10, MUTED, "end"))
        out.append(txt(bar_x0 + bw + 8, y + rowh / 2 + 4, fmt_num(v), 12, INK2, "start", 600))
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
    return svg(w, h, "".join(out))


def chart_scatter_map(w, h, points, xlab, ylab, title, note=None):
    """points: list of dict(name, x 0..1, y 0..1, kind in {'ai','display','us'}, dx, dy)."""
    pad_l, pad_r, pad_t, pad_b = 36, 20, 26, 40
    px0, px1, py0, py1 = pad_l, w - pad_r, pad_t, h - pad_b
    out = [txt(0, 12, title, 12, INK, weight=600),
           rect(px0, py0, px1 - px0, py1 - py0, PANEL, rx=4, stroke=HAIR),
           line((px0 + px1) / 2, py0, (px0 + px1) / 2, py1, HAIR, 1),
           line(px0, (py0 + py1) / 2, px1, (py0 + py1) / 2, HAIR, 1)]
    out.append(txt(px0, py1 + 16, xlab[0], 10, MUTED, "start"))
    out.append(txt(px1, py1 + 16, xlab[1], 10, MUTED, "end"))
    out.append(txt(px0 - 6, py1 - 2, ylab[0], 10, MUTED, "end", extra=f'transform="rotate(-90 {px0-6} {py1-2})"'))
    out.append(txt(px0 - 6, py0 + 2, ylab[1], 10, MUTED, "start", extra=f'transform="rotate(-90 {px0-6} {py0+2})"'))
    for p in points:
        x = px0 + p["x"] * (px1 - px0)
        y = py1 - p["y"] * (py1 - py0)
        k = p["kind"]
        if k == "us":
            out.append(circle(x, y, 9, ACCENT, PAPER, 2))
            out.append(txt(x + p.get("dx", 12), y + p.get("dy", 4), p["name"], 12, ACCENT, "start", 700))
        elif k == "ai":
            out.append(circle(x, y, 6, GREY_MARK, PAPER, 2))
            out.append(txt(x + p.get("dx", 9), y + p.get("dy", 4), p["name"], 10, INK2, "start"))
        else:
            out.append(rect(x - 5.5, y - 5.5, 11, 11, DARK_MARK, rx=2, stroke=PAPER, sw=2))
            out.append(txt(x + p.get("dx", 9), y + p.get("dy", 4), p["name"], 10, INK2, "start"))
    # legend
    lx = px0 + 8
    ly = py0 + 14
    out.append(circle(lx, ly, 5, GREY_MARK)); out.append(txt(lx + 10, ly + 4, "AI hardware", 10, INK2))
    out.append(rect(lx + 90 - 4.5, ly - 4.5, 9, 9, DARK_MARK, rx=2)); out.append(txt(lx + 100, ly + 4, "Display and e-ink products", 10, INK2))
    out.append(circle(lx + 262, ly, 5, ACCENT)); out.append(txt(lx + 272, ly + 4, "This venture", 10, INK2))
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
    return svg(w, h, "".join(out))


def chart_gantt(w, h, rows, months, title, today_idx=None, note=None):
    """rows: list of (label, start_month_idx(float), end_month_idx(float), state in {'done','next','later','gate'})."""
    lab_w = 230
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
    # legend
    lx = px0
    ly = h - 6
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
    return svg(w, h, "".join(out))


def chart_stacked_hbar(w, h, title, total_label, segments, benchmarks=None, note=None):
    """One retail-price bar split into segments (label, share 0..1, color, placeholder bool). benchmarks: list of (label, share) marks on a margin scale."""
    out = [txt(0, 12, title, 12, INK, weight=600)]
    bx0, bx1 = 10, w - 10
    by, bh = 40, 46
    x = bx0
    for lab, share, col, ph in segments:
        sw = (bx1 - bx0) * share
        out.append(rect(x + 1, by, sw - 2, bh, col, rx=3, extra=('stroke-dasharray="4 3"' if ph else ""), stroke=(INK2 if ph else "none")))
        if sw > 60:
            out.append(txt(x + sw / 2, by + bh / 2 + 4, lab, 11, "#ffffff" if col in (ACCENT, DARK_MARK) else INK, "middle", 600))
        else:
            out.append(txt(x + sw / 2, by + bh + 14, lab, 10, INK2, "middle"))
        x += sw
    out.append(txt(bx0, by - 8, total_label, 11, INK2))
    if benchmarks:
        yb = by + bh + 44
        out.append(txt(bx0, yb - 8, "Gross margin benchmarks, premium consumer hardware (latest fiscal year):", 11, INK2))
        out.append(line(bx0, yb + 10, bx1, yb + 10, "#c3bfb4", 1))
        for lab, share in benchmarks:
            xx = bx0 + (bx1 - bx0) * share
            out.append(circle(xx, yb + 10, 5, DARK_MARK, PAPER, 2))
            out.append(txt(xx, yb + 30, lab, 10, INK2, "middle"))
            out.append(txt(xx, yb + 42, f"{share*100:.0f}%", 10, MUTED, "middle"))
        for t in (0, 0.25, 0.5, 0.75):
            xx = bx0 + (bx1 - bx0) * t
            out.append(txt(xx, yb - 20, f"{t*100:.0f}%", 9, MUTED, "middle"))
    if note:
        out.append(txt(0, h - 4, note, 10, MUTED))
    return svg(w, h, "".join(out))


def device_illustration(w, h, headline="Your morning paper, written for you", lines_col=3, frame_color=DARK_MARK, label=None, masthead="THE DAILY"):
    """A framed e-ink display, flat and geometric."""
    fw, fh = w - 20, h - 20
    fx, fy = 10, 10
    out = [rect(fx, fy, fw, fh, frame_color, rx=14)]
    ix, iy, iw, ih = fx + 22, fy + 22, fw - 44, fh - 44
    out.append(rect(ix, iy, iw, ih, "#f9f7f0", rx=3))
    mx = ix + 18
    my = iy + 30
    out.append(txt(ix + iw / 2, my, masthead, 15, INK, "middle", 700, SERIF, extra='letter-spacing="3"'))
    out.append(line(ix + 18, my + 10, ix + iw - 18, my + 10, INK, 1.2))
    out.append(txt(ix + 18, my + 24, "Friday 27 November 2026", 8, INK2))
    out.append(txt(ix + iw - 18, my + 24, "Arenys de Mar, 11 C, clear", 8, INK2, "end"))
    out.append(line(ix + 18, my + 32, ix + iw - 18, my + 32, HAIR, 1))
    hy = my + 56
    for i, t in enumerate(wrap(headline, 30)):
        out.append(txt(ix + 18, hy + i * 19, t, 15, INK, "start", 700, SERIF))
    cols = lines_col
    cw = (iw - 36 - (cols - 1) * 12) / cols
    y0 = hy + 19 * len(wrap(headline, 30)) + 10
    for c in range(cols):
        cx = ix + 18 + c * (cw + 12)
        yy = y0
        while yy < iy + ih - 20:
            out.append(rect(cx, yy, cw * (0.95 if (int(yy) // 7) % 3 else 0.7), 2.2, "#b9b4a8", rx=1))
            yy += 7
    out.append(rect(ix + 18, iy + ih - 34, 54, 16, ACCENT, rx=2))
    out.append(txt(ix + 45, iy + ih - 22, "ASK ME", 8, "#ffffff", "middle", 700))
    if label:
        out.append(txt(w / 2, h - 2, label, 10, MUTED, "middle"))
    return svg(w, h, "".join(out))


# ---------------------------------------------------------------- slide shell
def slide(num, kicker, title, body_html, foot_sources="", extra_class=""):
    return f'''
<section class="slide {extra_class}" id="s{num}">
  <header class="top">
    <div class="kicker">{num:02d} <span class="dot">&middot;</span> {esc(kicker)}</div>
  </header>
  <h1>{title}</h1>
  <div class="body">{body_html}</div>
  <footer class="foot">
    <div class="left">{esc(BRAND)} <span class="dot">&middot;</span> {esc(DRAFT_LINE)}</div>
    <div class="mid">{foot_sources}</div>
    <div class="right">{num}</div>
  </footer>
</section>'''


def fn(*ids):
    """Footnote marker string."""
    return '<sup class="fn">' + ", ".join(str(i) for i in ids) + "</sup>"


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
h1 {{ font-family: {SERIF}; font-weight: 400; font-size: 36px; line-height: 1.12; margin: 10px 0 0 0; letter-spacing: -.01em; max-width: 1100px; }}
h1 em {{ font-style: italic; color: {ACCENT}; }}
.body {{ position: absolute; left: 60px; right: 60px; top: 162px; bottom: 56px; }}
.foot {{ position: absolute; left: 60px; right: 60px; bottom: 22px; display: flex; justify-content: space-between; align-items: baseline;
        font-size: 10.5px; color: {MUTED}; border-top: 1px solid {HAIR}; padding-top: 8px; }}
.foot .mid {{ flex: 1; margin: 0 24px; color: {MUTED}; }}
.foot .right {{ font-variant-numeric: tabular-nums; }}
p, li {{ font-size: 16px; line-height: 1.42; margin: 0 0 10px 0; color: {INK}; }}
ul {{ padding-left: 18px; margin: 0; }}
.small {{ font-size: 13px; color: {INK2}; line-height: 1.4; }}
.muted {{ color: {MUTED}; }}
.accent {{ color: {ACCENT}; }}
sup.fn {{ font-size: 9px; color: {ACCENT}; font-weight: 600; vertical-align: super; line-height: 0; margin-left: 1px; }}
.cols {{ display: grid; gap: 36px; height: 100%; }}
.c2 {{ grid-template-columns: 1fr 1fr; }}
.c21 {{ grid-template-columns: 1.15fr 1fr; }}
.c12 {{ grid-template-columns: 1fr 1.25fr; }}
.c3 {{ grid-template-columns: 1fr 1fr 1fr; }}
.label {{ font-size: 11.5px; letter-spacing: .12em; text-transform: uppercase; color: {MUTED}; font-weight: 600; margin: 0 0 8px 0; }}
.card {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 14px 16px; }}
.card.ph {{ border-style: dashed; }}
.tile {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 14px 16px 12px 16px; }}
.tile .v {{ font-size: 34px; line-height: 1; margin: 2px 0 6px 0; letter-spacing: -.02em; color: {INK}; }}
.tile .v.ph {{ color: {MUTED}; font-size: 22px; }}
.tile .k {{ font-size: 11.5px; letter-spacing: .1em; text-transform: uppercase; color: {MUTED}; font-weight: 600; }}
.tile .m {{ font-size: 12px; color: {INK2}; line-height: 1.4; }}
table.t {{ border-collapse: collapse; width: 100%; font-size: 11px; line-height: 1.3; }}
table.t th {{ text-align: left; font-weight: 600; color: {MUTED}; font-size: 10px; letter-spacing: .08em; text-transform: uppercase; padding: 3px 8px 5px 0; border-bottom: 1px solid {HAIR}; }}
table.t td {{ padding: 4px 8px 4px 0; border-bottom: 1px solid {HAIR}; vertical-align: top; color: {INK}; }}
table.t td.n {{ font-variant-numeric: tabular-nums; white-space: nowrap; }}
table.t tr.us td {{ color: {ACCENT}; font-weight: 600; }}
.ph {{ color: {MUTED}; }}
.badge {{ display: inline-block; font-size: 10px; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; color: {ACCENT};
         border: 1px solid {ACCENT}; border-radius: 3px; padding: 2px 6px; vertical-align: middle; margin-left: 6px; }}
.catgrid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: 1fr 1fr; gap: 14px; height: 100%; }}
.cat {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 12px 14px; display: flex; flex-direction: column; }}
.cat.hero {{ border-color: {ACCENT}; border-width: 1.5px; }}
.cat .render {{ flex: 1; border: 1px dashed {HAIR}; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: {MUTED}; font-size: 11px; margin-bottom: 10px; min-height: 60px; text-align: center; padding: 6px; }}
.cat .name {{ font-family: {SERIF}; font-size: 17px; margin: 0 0 3px 0; }}
.cat .one {{ font-size: 12px; color: {INK2}; line-height: 1.35; margin: 0 0 6px 0; }}
.cat .price {{ font-size: 11.5px; color: {MUTED}; margin-top: auto; }}
.cover {{ padding: 0; }}
.cover .body {{ top: 0; bottom: 0; left: 0; right: 0; }}
.cover .wordmark {{ position: absolute; left: 80px; top: 92px; font-family: {SERIF}; font-size: 54px; line-height: 1.05; max-width: 560px; letter-spacing: -.01em; }}
.cover .sub {{ position: absolute; left: 80px; top: 300px; font-size: 20px; line-height: 1.45; max-width: 520px; color: {INK2}; }}
.cover .meta {{ position: absolute; left: 80px; bottom: 56px; font-size: 13px; color: {MUTED}; line-height: 1.6; }}
.cover .illus {{ position: absolute; right: 70px; top: 90px; }}
.cover .rule {{ position: absolute; left: 80px; top: 270px; width: 72px; height: 3px; background: {ACCENT}; }}
.quote {{ font-family: {SERIF}; font-size: 20px; line-height: 1.35; color: {INK}; border-left: 3px solid {ACCENT}; padding-left: 16px; margin: 0 0 14px 0; }}
.legend {{ font-size: 11px; color: {INK2}; }}
.legend i {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin: 0 5px 0 12px; vertical-align: -1px; }}
.steps {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }}
.step {{ background: {PANEL}; border: 1px solid {HAIR}; border-radius: 8px; padding: 12px 14px; }}
.step .n {{ font-family: {SERIF}; font-size: 26px; color: {ACCENT}; line-height: 1; margin-bottom: 6px; }}
.step .h {{ font-weight: 600; font-size: 14px; margin-bottom: 4px; }}
.step .d {{ font-size: 12.5px; color: {INK2}; line-height: 1.4; }}
.src {{ font-size: 10.5px; color: {INK2}; line-height: 1.45; column-count: 2; column-gap: 36px; }}
.src div {{ break-inside: avoid; margin-bottom: 4px; }}
.src b {{ color: {ACCENT}; font-weight: 700; margin-right: 4px; }}
.hr {{ height: 1px; background: {HAIR}; margin: 10px 0; }}
"""

# ---------------------------------------------------------------- sources (numbered as cited on the slides; full tables in research.md)
SOURCES = [
    (1, "ABI Research, Smart home hardware market outlook, 4Q 2025", "abiresearch.com"),
    (2, "Omdia, Smart speaker market overview 2H25 and 1H26 (snippet only)", "omdia.tech.informa.com"),
    (3, "IMARC, E-paper display market, updated 2026-02-26", "imarcgroup.com"),
    (4, "Technavio via PR Newswire, Digital photo frame market 2025 to 2029, 2025-01-28", "prnewswire.com"),
    (5, "Eurostat, EU households 2025, news 2026-05-13", "ec.europa.eu/eurostat"),
    (6, "US Census via FRED, Total households (TTLHH), updated 2026-11-17", "fred.stlouisfed.org"),
    (7, "Parks Associates, Smart home growth continues, 2026-04-23", "parksassociates.com"),
    (8, "Eurostat, Internet of things use 2024 (snippet only)", "ec.europa.eu/eurostat"),
    (9, "Bank of America Institute via KOMO News, 3% of households pay for AI, 2026-03-31", "komonews.com"),
    (10, "Attest, Gen AI the only subscription category still growing, updated 2026-11-09", "askattest.com"),
    (11, "TRMNL blog, On X: 14,500 orders, 2026-11-11", "trmnl.com"),
    (12, "Modal, Tidbyt is joining Modal, 2024-11-07", "modal.com"),
    (13, "9to5Google, Rabbit: 5,000 daily users on 100,000 sold, 2024-09-26", "9to5google.com"),
    (14, "reMarkable 2024 annual report via Wikipedia (snippet only)", "en.wikipedia.org"),
    (15, "36Kr, Plaud 2M devices and US$100M ARR, 2026-08-30", "eu.36kr.com"),
    (16, "Kicktraq, Fraimic Smart E Ink Canvas (snippet only), 2025", "kicktraq.com"),
    (17, "TechCrunch, Humane's Ai Pin is dead, HP buys assets for $116M, 2025-02-18", "techcrunch.com"),
    (18, "Fortune, Who is Avi Schiffmann (Friend), 2025-10-01", "fortune.com"),
    (19, "TechCrunch, Plaud launches the $179 Note Pro, 2025-08-27", "techcrunch.com"),
    (20, "TechCrunch, Meta acquires Limitless, 2025-12-05", "techcrunch.com"),
    (21, "TechCrunch, Amazon acquires Bee, 2025-07-22", "techcrunch.com"),
    (22, "UploadVR, 7 million Meta smart glasses sold in 2025, 2026-02-11", "uploadvr.com"),
    (23, "TechCrunch, Aura introduces a $499 e-ink frame, 2025-10-21", "techcrunch.com"),
    (24, "Skylight press release via Finviz, credit facility to $75M, 2026-09-30", "finviz.com"),
    (25, "reMarkable, Connect subscription page, accessed 2026-11-27", "remarkable.com"),
    (26, "Apple, Form 10-K FY2025, Products gross margin", "sec.gov"),
    (27, "Sonos, Q4 and fiscal 2025 results, 2025-11-05", "investors.sonos.com"),
    (28, "Peloton, Q4 FY2025 shareholder letter, 2025-08-07", "sec.gov"),
    (29, "Garmin, FY2024 results, Feb 2025 (snippet only)", "garmin.com"),
    (30, "reMarkable, Q1 2025 interim report (snippet only)", "live.euronext.com"),
    (31, "Predictable Designs, Certification costs, 2026-01-17", "predictabledesigns.com"),
    (32, "Cosmo Sourcing and ChinaImportal, MOQ guides (snippet only)", "cosmosourcing.com"),
    (33, "China sourcing agents on dev.to and Hackster, tooling costs (snippet only)", "dev.to, hackster.io"),
    (34, "Good Display store, GDEY075T7 7.5in panel, accessed 2026-11-27", "buy-lcd.com"),
    (35, "Waveshare, 13.3inch e-Paper HAT (K), accessed 2026-11-27", "waveshare.com"),
    (36, "LCSC and Digi-Key, ESP32-S3-WROOM-1 pricing (snippet only)", "lcsc.com"),
    (37, "Predictable Designs, Bolt, Sinovation: COGS-to-retail multiples (snippet only)", "predictabledesigns.com, bolt.io"),
    (38, "TechCrunch, Pebble founder: 25,000 pre-orders, five staff, 2026-01-12", "techcrunch.com"),
    (39, "LocaliQ (WordStream), Facebook advertising benchmarks, updated 2026-09-23", "localiq.com"),
    (40, "Parks Associates, 52% of DIY smart home users report setup issues, 2025-07-09", "parksassociates.com"),
    (41, "TechCrunch citing WSJ, Alexa at 10: $25bn lost 2017 to 2021, 2024-08-10", "techcrunch.com"),
    (42, "Amazon, Alexa+ announcement, 2025-02-26", "aboutamazon.com"),
    (43, "eMarketer citing CNET/YouGov, half will not pay for AI features, 2025 (snippet only)", "emarketer.com"),
    (44, "DataReportal, Digital 2025 global overview (GWI), Feb 2025", "datareportal.com"),
    (45, "E Ink, Benefits of ePaper (manufacturer claims), accessed 2026-11-27", "eink.com"),
    (46, "Epoch AI, LLM inference price trends, 2025-03-12", "epoch.ai"),
    (47, "a16z, LLMflation, 2024-11-12", "a16z.com"),
    (48, "Google, Introducing Gemma 3n, 2025-05-20", "developers.googleblog.com"),
    (49, "Anthropic, Introducing the Model Context Protocol, 2024-11-25", "anthropic.com"),
    (50, "Linux Foundation, Agentic AI Foundation formed, 2025-12-09", "linuxfoundation.org"),
    (51, "Espressif, Who we are: 1.5 billion+ SoCs shipped, accessed 2026-11-27", "espressif.com"),
    (52, "TechNews Taiwan, E Ink Holdings 2024 results, 2025-03-05", "finance.technews.tw"),
    (53, "Quartr, E Ink Holdings Q4 2025 earnings, 2026-04-13", "quartr.com"),
    (54, "StockAnalysis, E Ink Holdings (8069) revenue history, updated 2026-11-11", "stockanalysis.com"),
    (55, "European Commission, 150 EUR customs exemption to be removed in 2026, 2025-11-13", "taxation-customs.ec.europa.eu"),
    (56, "OpenAI, Google and Anthropic official API pricing pages, accessed 2026-11-27", "developers.openai.com, aistudio.google.com, platform.claude.com"),
    (57, "InkPoster (PocketBook), product pages, accessed 2026-11-27", "inkposter.com"),
    (58, "Yanko Design, Jitrainno colour e-ink art frame, 2026-09-11", "yankodesign.com"),
    (59, "Global Market Insights, E-paper display market, Sept 2026", "gminsights.com"),
    (60, "Counterpoint, Smart glasses shipments +139% in H2 2025, 2026-02-27", "counterpointresearch.com"),
    (61, "Deloitte, 2025 Connected Consumer survey, 2025-09-25", "deloitte.com"),
    (62, "Oura, Membership page, accessed 2026-11-27", "ouraring.com"),
    (63, "Skylight, Plus plan page, accessed 2026-11-27", "myskylight.com"),
]


# ---------------------------------------------------------------- slide builders
def s_cover():
    body = f'''
<div class="wordmark">{esc(BRAND)}<br><span style="font-size:30px;color:{INK2}">Objects you talk to.</span></div>
<div class="rule"></div>
<div class="sub">Promptable AI gadgets under one premium brand. Hardware sourced in Shenzhen, design from Europe, software the owner shapes by describing what they want.</div>
<div class="illus">{device_illustration(560, 420, headline="Your morning paper, composed for you")}</div>
<div class="meta">Pitch deck, version 1 draft &middot; 27 November 2026 &middot; Oscar [surname placeholder]<br>Private. Not for distribution. Every figure inside carries a numbered source (slide 10, research.md).</div>'''
    return f'''
<section class="slide cover" id="s1">
  <div class="body">{body}</div>
</section>'''


def s_problem():
    llm = chart_line_log(
        562, 215,
        [dict(name="GPT-4-class capability", color=ACCENT, pts=[
            (2023.20, 37.5, "GPT-4, $37.50"), (2023.85, 15.0, "GPT-4 Turbo, $15"),
            (2024.37, 7.5, "GPT-4o, $7.50"), (2025.10, 0.18, "Gemini 2.0 Flash, $0.18")])],
        y_ticks=[0.1, 1, 10, 100], x_ticks=[(2023.2, "Mar 2023"), (2024.0, "2024"), (2025.1, "Feb 2025")],
        title="Cheapest price to run a GPT-4-class model, USD per million tokens (log scale)",
        unit_label="USD / 1M tokens",
        note="Epoch AI series [46]; about 208x cheaper in two years (our arithmetic). a16z: cost falls about 10x a year at equal capability [47].")
    eink = chart_bars(270, 190, ["2023", "2024", "2025"], [27.1, 32.2, 36.1],
                      title="E Ink Holdings revenue, NT$ bn", unit="NT$ bn", highlight_last=True,
                      value_fmt=lambda v: f"{v:.1f}", ymax=42,
                      note="2024 +19%, 2025 +12%, record profit [52, 53, 54]")
    facts = f'''
<div class="tile" style="height:190px">
  <div class="k">Also in place</div>
  <p class="small" style="margin:8px 0 6px 0"><b>Open tool standard.</b> The Model Context Protocol, launched Nov 2024, now has more than 10,000 public servers and Linux Foundation governance with Anthropic, OpenAI, Google and Microsoft at the table.{fn(49, 50)}</p>
  <p class="small" style="margin:0 0 6px 0"><b>Models that fit in an object.</b> Gemma 3n runs in 2 to 3 GB of memory on phone-class hardware.{fn(48)}</p>
  <p class="small" style="margin:0"><b>Commodity radios.</b> Espressif has shipped more than 1.5 billion Wi-Fi SoCs.{fn(51)}</p>
</div>'''
    left = f'''
<div class="label">The problem</div>
<p class="quote">Every connected object does what its maker's app allows. The owner cannot reshape it.</p>
<ul>
  <li>52% of do-it-yourself smart home users report setup or connectivity problems.{fn(40)}</li>
  <li>The biggest home assistant lost $25bn in five years and became, in a former insider's words, "a smart timer". Its AI upgrade now costs $19.99 a month.{fn(41, 42)}</li>
  <li>The first AI gadgets were phones in disguise. Humane shipped about 10,000 units on more than $230M and is dead; Rabbit sold 100,000 and keeps 5,000 daily users; Friend sold 3,000.{fn(17, 13, 18)}</li>
  <li>Half of US smartphone owners will not pay extra for bolt-on AI features (reported survey).{fn(43)}</li>
</ul>
<p class="small" style="margin-top:14px"><span class="accent"><b>Our reading (opinion).</b></span> AI sells when it is the product inside a calm, single-purpose object that the owner can reshape by talking to it. Not another screen with a feature tax.</p>'''
    right = f'''
<div class="label">Why now</div>
{llm}
<div style="display:flex;gap:22px;margin-top:10px">{eink}{facts}</div>'''
    return slide(2, "Problem and why now", "The problem, and why the answer is possible now",
                 f'<div class="cols c2">{left and f"<div>{left}</div>"}<div>{right}</div></div>',
                 "Sources by number on slide 10 and in research.md. Figures marked \"reported\" come from search snippets, not opened pages.")


def s_hero():
    flow_w, flow_h = 598, 150
    d = [arrow_defs()]
    nodes = [
        (0, "You say it", "\"My day, the weather in Arenys, three headlines on e-ink research, in Catalan.\""),
        (1, "AI agent", "a language model plans the page"),
        (2, "Tools via MCP", "calendar, news, weather, home, PersonalPress (separate project)"),
        (3, "Page composed", "typeset like a newspaper"),
        (4, "E-ink refresh", "once a morning, weeks on a charge"),
    ]
    bw, gap = 106, 17
    for i, t, s in nodes:
        x = i * (bw + gap)
        d.append(box(x, 10, bw, 120, t, s, accent=(i == 0 or i == 4), size=12.5, subsize=10))
        if i < 4:
            d.append(arrow(x + bw + 2, 70, x + bw + gap - 2, 70))
    flow = svg(flow_w, flow_h, "".join(d))
    specs = f'''
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px;margin-top:14px">
  <div class="tile"><div class="k">Panel</div><div class="v ph">[placeholder]</div><div class="m">7.5in to 13.3in e-paper, mono or Spectra 6 colour</div></div>
  <div class="tile"><div class="k">Target price</div><div class="v ph">[placeholder]</div><div class="m">due Sat 28 Nov</div></div>
  <div class="tile"><div class="k">Unit cost at MOQ</div><div class="v ph">[placeholder]</div><div class="m">first ODM quote pending</div></div>
  <div class="tile"><div class="k">MOQ</div><div class="v ph">[placeholder]</div><div class="m">typical ODM range 500 to 5,000 units (reported){fn(32)}</div></div>
</div>
<p class="small" style="margin-top:14px"><b>Price points already paid in this category.</b> Aura Ink 13.3in e-paper frame $499{fn(23)}; InkPoster 13.3in $449{fn(57)}; TRMNL X 10.3in dashboard $229{fn(11)}; Fraimic AI art frame $399 list{fn(16)}.</p>
<p class="small" style="margin:6px 0 0 0"><b>Sourced component references (retail, single units).</b> 13.3in panel with driver board $142 to $145{fn(35)}; 7.5in panel $28.64{fn(34)}; ESP32-S3 Wi-Fi module $3.35 to $4.93{fn(36)}.</p>'''
    left = f'''
{device_illustration(500, 372, headline="Divendres. El teu dia, el temps i tres titulars.", label="Render placeholder: final industrial design due Sat 28 Nov. Style lead under discussion: wood and lacquer.")}
<p class="small" style="margin-top:10px">No app to learn, no menus, no vendor roadmap. The owner says "add my train times and drop the sport", and the next edition has it. The display is paper-like, has no backlight and holds its image with no power.{fn(45)}</p>'''
    right = f'''
<div class="label">How it works</div>
{flow}
{specs}'''
    return slide(3, "Hero", "Hero: a promptable e-ink display. Describe the page, and it becomes that page.",
                 f'<div class="cols c12" style="gap:28px"><div>{left}</div><div>{right}</div></div>',
                 "Panel and module prices are retail single-unit listings, not ODM quotes. The hero's unit cost and MOQ are placeholders by Oscar's instruction.")


def s_catalogue():
    items = [
        ("hero", "Promptable e-ink display", "Your daily paper, composed for you, on paper-like e-ink. The hero.", "[price placeholder]"),
        ("", "Desk AI display", "Where your assistant lives on the desk: a face, a voice, a glanceable screen.", "[price placeholder]"),
        ("", "Solar AI keychain", "Talk to your AI from a keyring. Charges in daylight.", "[price placeholder]"),
        ("", "Digital wall aquarium", "A living wall tank whose rare fish appear only sometimes.", "[price placeholder]"),
        ("", "10,000-lumen light with e-ink", "A work light with an e-ink face that says what it is lighting, and why.", "[price placeholder]"),
        ("", "Wi-Fi plug for fairy lights", "Lights that know your calendar: on for guests, off when you leave.", "[price placeholder]"),
        ("", "Interior oddities", "A fish-shaped lock and other hyper-specific objects in the Japanese specialist-store tradition.", "[price placeholder]"),
    ]
    cards = []
    for cls, name, one, price in items:
        cards.append(f'''<div class="cat {cls}"><div class="render">render due Sat 28 Nov</div><div class="name">{esc(name)}{'<span class="badge">hero</span>' if cls else ''}</div><div class="one">{esc(one)}</div><div class="price">{esc(price)}</div></div>''')
    cards.append(f'''<div class="cat" style="background:{INK};color:{PAPER};border-color:{INK}"><div class="name" style="color:{PAPER}">One layer under every object</div><div class="one" style="color:#d8d3c7">Each object runs the same promptable layer: the owner describes a change and it happens. One brand, one account, one voice. Hardware is commodity; the design and the software layer are what is ours.</div><div class="price" style="color:#b9b4a8">Draft one-liners for Oscar's edit</div></div>''')
    return slide(4, "Catalogue", "Catalogue: one software layer, seven objects. Renders and prices arrive Saturday 28 November.",
                 f'<div class="catgrid">{"".join(cards)}</div>',
                 "Catalogue renders and target prices are placeholders by Oscar's instruction (due Sat 28 Nov).")


def s_market():
    funnel = chart_funnel(562, 215, [
        ("Households, EU27 plus US", 337.9e6, "203.1M Eurostat 2025 [5] + 134.8M Census 2025 [6]"),
        ("With a connected home device", 104.6e6, "US 49% of internet households [7]; EU 19% smart speaker use, individuals (reported) [8]"),
        ("Already paying for an AI subscription", 3.1e6, "3% by bank account data [9]; surveys say 19.5%, which gives 20.4M [10]"),
    ], title="Bottom-up ceiling: who could buy a promptable object today", note="Bar length on a square-root scale. Our arithmetic from the sourced shares; multiplying shares is conservative when the traits overlap (opinion).")
    ladder = chart_funnel(562, 300, [
        ("Fraimic AI art frame", 1825, "Kickstarter backers, 2025 (reported) [16]"),
        ("TRMNL X dashboard", 14500, "orders in 16 months to Nov 2026 [11]"),
        ("Tidbyt ambient display", 100000, "devices shipped, lifetime to 2024 [12]"),
        ("Rabbit r1", 100000, "sold by Sept 2024; 5,000 daily users [13]"),
        ("reMarkable paper tablets", 791000, "devices sold in 2024 alone (reported) [14]"),
        ("Plaud AI recorders", 2000000, "devices, cumulative to June 2026; US$100M+ software ARR [15]"),
    ], title="What one product line has actually reached (units)", note="Square-root scale. Aura reports \"single-digit millions\" of frames, cumulative, profitable [23].")
    left = f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
  <div class="tile"><div class="k">TAM: smart home hardware, global</div><div class="v">US$66.5bn</div><div class="m">2025, to US$82.6bn in 2030 (CAGR 4.4%). ABI Research.{fn(1)} Every object in the catalogue is a connected home object.</div></div>
  <div class="tile"><div class="k">SAM: ambient displays and AI speakers</div><div class="v">about US$10bn</div><div class="m">Smart speakers US$6.2bn (54.7M units x ASP, 12 months to mid-2026, our arithmetic on reported Omdia figures){fn(2)} + e-paper displays US$3.4bn{fn(3)} + digital frames about US$0.7bn{fn(4)}.</div></div>
</div>
<p class="small" style="margin:10px 0 8px 0"><b>Method.</b> TAM is one verified analyst figure for the container market. SAM adds the three segments the catalogue competes in; the e-paper figure counts panels for e-readers and shelf labels too, so the sum is an upper bound. SOM is not a capture guess: a bottom-up ceiling (below) and the ladder of what single products have really sold (right).</p>
{funnel}'''
    right = f'''
{ladder}
<p class="small" style="margin-top:10px"><b>Growth signals, 2025 to 2026.</b> E-paper displays growing 11.5% to 17% a year{fn(3, 59)}; E Ink Holdings revenue +19% in 2024 and +12% in 2025{fn(52, 53)}; smart glasses shipments +139% in H2 2025{fn(60)}; US households spent US$896 on connected devices in 2025, up from US$764{fn(61)}.</p>'''
    return slide(5, "Market", "Market: a US$66bn container, a US$10bn arena, and what one product has actually reached",
                 f'<div class="cols c2">{f"<div>{left}</div>"}<div>{right}</div></div>',
                 "All inputs and the arithmetic are in research.md section 1. \"Reported\" marks figures seen in search snippets only.")


def s_competition():
    pts = [
        dict(name="Humane Ai Pin (dead)", x=0.55, y=0.74, kind="ai"),
        dict(name="Rabbit r1", x=0.50, y=0.34, kind="ai"),
        dict(name="Friend", x=0.60, y=0.46, kind="ai"),
        dict(name="Plaud", x=0.34, y=0.52, kind="ai"),
        dict(name="Limitless (to Meta)", x=0.42, y=0.40, kind="ai", dy=14),
        dict(name="Bee (to Amazon)", x=0.36, y=0.20, kind="ai"),
        dict(name="Meta Ray-Ban", x=0.46, y=0.86, kind="ai"),
        dict(name="TRMNL", x=0.30, y=0.30, kind="display", dy=14),
        dict(name="Aura", x=0.10, y=0.70, kind="display"),
        dict(name="Skylight", x=0.20, y=0.50, kind="display"),
        dict(name="reMarkable", x=0.16, y=0.86, kind="display"),
        dict(name="Meural (ended)", x=0.10, y=0.60, kind="display"),
        dict(name="Tidbyt (no new units)", x=0.25, y=0.40, kind="display"),
        dict(name="Nixplay", x=0.08, y=0.30, kind="display"),
        dict(name="InkPoster", x=0.05, y=0.80, kind="display"),
        dict(name="Inkplate, DIY boards", x=0.30, y=0.10, kind="display"),
        dict(name="Fraimic, Jitrainno (prompt to picture)", x=0.70, y=0.56, kind="display"),
        dict(name="This venture", x=0.88, y=0.86, kind="us", dx=-120, dy=24),
    ]
    scatter = chart_scatter_map(600, 450, pts, ("Fixed function", "Shaped by talking to it"), ("Utility object", "Premium design object"),
                                "Where the products sit (positions are our reading of each product's marketing: opinion)")
    rows = [
        ("Humane Ai Pin", "$699 + $24/mo", "$230M+ raised", "Dead Feb 2025; HP paid $116M for assets", fn(17)),
        ("Rabbit r1", "about $199", "$30M (reported)", "100k sold, 5k daily users; alive on software", fn(13)),
        ("Friend", "$129, now $249 + $9.99/mo", "about $7M", "3,000 sold by Oct 2025; $1M subway ads", fn(18)),
        ("Plaud", "$179 + $99.99/yr Pro", "self-funded (reported)", "2M+ devices, US$100M+ ARR; half upgrade", fn(19, 15)),
        ("Limitless", "$99", "$33M+", "Acquired by Meta Dec 2025; hardware stopped", fn(20)),
        ("Bee", "$49.99 + $19/mo", "$7M", "Acquired by Amazon Jul 2025", fn(21)),
        ("Meta Ray-Ban", "Display $799", "public", "7M+ glasses sold in 2025", fn(22)),
        ("TRMNL", "$139 to $229, no sub", "undisclosed", "14,500 X orders in 16 months; 1,000+ plugins", fn(11)),
        ("Aura", "$139 to $499, no sub", "$60M growth capital 2025", "Millions of frames; profitable; e-paper Ink Oct 2025", fn(23)),
        ("Skylight", "$320 + $79/yr", "bootstrapped, $75M credit", "12M customers; 1.7M Calendar households", fn(24)),
        ("reMarkable", "649 EUR + 3.99 EUR/mo", "profitable", "791k devices and 568k subscribers in 2024 (reported)", fn(25, 14)),
        ("Tidbyt", "$199, no sub", "acquired", "100k devices; no new hardware since Modal deal", fn(12)),
    ]
    trs = "".join(f"<tr><td><b>{esc(a)}</b></td><td class='n'>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}{e}</td></tr>" for a, b, c, d, e in rows)
    table = f'''<table class="t"><thead><tr><th>Product</th><th>Price</th><th>Money</th><th>Outcome, Nov 2026</th></tr></thead><tbody>{trs}</tbody></table>
<p class="small" style="margin-top:10px"><b>The gap, from the record.</b> The only products configured in plain language are AI art frames (prompt to picture){fn(16, 58)}. TRMNL owners configure by writing code with an LLM. Nobody ships an object a non-technical owner can reshape by describing it (fact as found; whether a premium brand can fill the gap is unproven).</p>'''
    return slide(6, "Competition", "Competition: many objects, and none that the owner can reshape by talking to it",
                 f'<div class="cols" style="grid-template-columns:600px 1fr;gap:28px"><div>{scatter}</div><div>{table}</div></div>',
                 "Prices and outcomes as published at the dates in research.md section 2. \"Reported\" marks figures seen in search snippets only.")


def s_business():
    d = [arrow_defs()]
    nodes = [
        ("Design in Europe", "wood, lacquer, typography; the part that is ours"),
        ("Ads and pre-orders", "only once models work (Oscar's gate); orders fund the batch"),
        ("ODM build in Shenzhen", "MOQ, tooling, certification; commodity inside"),
        ("Ship from an EU warehouse", "duty and VAT paid once, not per parcel"),
        ("Software tiers", "free, plus, hackable; the margin that compounds"),
        ("What owners ask for", "every prompt is a product-research note"),
    ]
    bw, gap, y0 = 172, 25.6, 8
    for i, (t, s) in enumerate(nodes):
        x = i * (bw + gap)
        d.append(box(x, y0, bw, 96, t, s, accent=(i in (0, 4)), size=12.5, subsize=10))
        if i < 5:
            d.append(arrow(x + bw + 2, y0 + 48, x + bw + gap - 2, y0 + 48))
    # return arrow from last node to first, below
    d.append(path(f"M {5*(bw+gap)+bw/2:.1f} {y0+98} L {5*(bw+gap)+bw/2:.1f} {y0+124} L {bw/2:.1f} {y0+124} L {bw/2:.1f} {y0+104}", INK2, width=1.5, extra='marker-end="url(#arr)"'))
    d.append(txt(1160 / 2, y0 + 120, "the loop: what owners ask for shapes the next object", 10, MUTED, "middle"))
    flow = svg(1160, 140, "".join(d))
    unit = chart_stacked_hbar(
        362, 215, "Where a retail euro goes (structure, not a forecast)", "Retail price = 100%. Unit cost [placeholder] until the first ODM quote.",
        [("Unit cost: 1/3 at the 3x rule", 0.333, DARK_MARK, False), ("Freight, duty, VAT, payments, returns [placeholder]", 0.27, PAPER, True), ("Gross margin, to compare below", 0.397, PAPER, True)],
        benchmarks=[("Peloton hw", 0.136), ("Apple", 0.368), ("Sonos", 0.437), ("reMarkable", 0.434), ("Garmin", 0.587)],
        note="3x rule [37]. Margins: Apple FY25 [26], Sonos FY25 [27], Peloton FY25 [28], reMarkable Q1 25 [30], Garmin FY24 [29].")
    tiers = f'''
<div class="label">Software tiers (draft, Oscar's pricing call)</div>
<div class="card" style="padding:10px 12px;margin-bottom:8px"><b>Free.</b> <span class="small">On-device layouts, local refresh, no cloud AI. The object is complete without paying.</span></div>
<div class="card" style="padding:10px 12px;margin-bottom:8px;border-color:{ACCENT}"><b>Plus.</b> <span class="small">Cloud AI editions, more sources, voice. Price [placeholder]; the category pays 3.99 EUR to $8.95 a month.{fn(25, 62)}</span></div>
<div class="card" style="padding:10px 12px;margin-bottom:10px"><b>Hackable.</b> <span class="small">MCP access, bring your own model, API. For the TRMNL crowd.</span></div>
<p class="small" style="margin:0"><b>Attach signals.</b> About half of Plaud buyers upgrade to the paid plan{fn(19)}; reMarkable reported 568k paying subscribers against 791k devices sold in 2024 (reported){fn(14)}; Skylight charges $39 to $79 a year on a $320 device{fn(63)}.</p>'''
    odm = f'''
<div class="label">Pre-orders and the Shenzhen build</div>
<ul class="small" style="padding-left:16px">
  <li>Pebble's founder took 25,000 pre-orders with five staff and no inventory built ahead of sales.{fn(38)}</li>
  <li>TRMNL took 14,500 orders for one device in 16 months without funding.{fn(11)}</li>
  <li>Meta ads, all industries 2026: CTR 1.93%, CPC $0.60 for traffic campaigns.{fn(39)}</li>
  <li>ODM MOQ commonly 500 to 5,000 units (reported){fn(32)}; injection tooling $2,000 to $15,000 (reported){fn(33)}; a wood or lacquer frame may avoid the mould (opinion).</li>
  <li>CE, RED and FCC with a pre-certified Wi-Fi module: $3,000 to $8,000.{fn(31)}</li>
  <li>The EU 150 EUR duty exemption ends in 2026, so bulk import to an EU warehouse, not drop-shipping.{fn(55)}</li>
</ul>'''
    return slide(7, "Business model", "Business model: hardware at a premium-brand margin, software tiers on top, pre-orders before the build",
                 f'{flow}<div class="cols c3" style="margin-top:12px;height:auto">{f"<div>{unit}</div>"}<div>{tiers}</div><div>{odm}</div></div>',
                 "The unit-cost bar shows structure under a published rule of thumb, not a forecast. Hero unit cost and MOQ are placeholders by Oscar's instruction.")


def s_plan():
    rows = [
        ("Idea and first calls (25 Nov)", 0.80, 0.87, "done"),
        ("Research and this deck v1 (27 Nov)", 0.87, 0.92, "done"),
        ("Catalogue: renders, prices (28 Nov)", 0.90, 0.97, "next"),
        ("Brand name, style (wood and lacquer lead)", 0.90, 1.6, "next"),
        ("Legal and admin groundwork (by 4 Dec)", 1.0, 1.15, "next"),
        ("First investor conversations", 1.0, 1.4, "next"),
        ("Hero software v0: prompt to page", 1.2, 2.6, "later"),
        ("Hero hardware prototype (dev panel)", 1.6, 3.2, "later"),
        ("Gate: ads and pre-orders, when models work", 3.2, 4.2, "gate"),
        ("ODM sample via a Shenzhen introduction", 3.6, 5.2, "later"),
        ("First batch to pre-order customers", 5.6, 7.0, "later"),
    ]
    gantt = chart_gantt(700, 400, rows, ["Nov 26", "Dec", "Jan 27", "Feb", "Mar", "Apr", "May", "Jun"],
                        "Plan (dark: done; red: next; grey: proposed, Oscar to confirm; dashed: Oscar's gate)", today_idx=0.87,
                        note="Dates after December are proposals for Oscar's edit, not commitments.")
    right = f'''
<div class="label">Where it stands, honestly</div>
<div class="steps" style="grid-template-columns:1fr;gap:10px">
  <div class="step"><div class="h">Done</div><div class="d">Idea and calls (25 Nov). Catalogue decided, hero picked (26 Nov). Coffee prep. This research and deck (27 Nov).</div></div>
  <div class="step"><div class="h">In hand</div><div class="d">The founder already runs a personal AI-agent operation with a data hub on the Model Context Protocol that composes daily briefs: the hero's software path exists in rough form. A separate project, PersonalPress, is a candidate first content source.</div></div>
  <div class="step"><div class="h">Not yet</div><div class="d">A working unit. A sale. A brand name. An ODM quote.</div></div>
  <div class="step" style="border-color:{ACCENT}"><div class="h accent">Next milestone</div><div class="d">The hero unit working in hand. Then a second meeting. Nothing public and no pre-orders until the models work.</div></div>
</div>'''
    return slide(8, "Progress and plan", "Progress and plan: catalogue this week, a working hero unit before anything else",
                 f'<div class="cols" style="grid-template-columns:700px 1fr;gap:32px"><div>{gantt}</div><div>{right}</div></div>',
                 "Plan dates beyond December 2026 are proposals for Oscar's edit.")


def s_founder():
    left = f'''
<div class="label">Founder</div>
<div style="display:grid;grid-template-columns:150px 1fr;gap:18px">
  <div class="card ph" style="height:180px;display:flex;align-items:center;justify-content:center;color:{MUTED};font-size:11px;text-align:center">photo<br>[placeholder]</div>
  <div>
    <p style="font-family:{SERIF};font-size:26px;margin:0 0 6px 0">Oscar <span class="ph">[surname placeholder]</span></p>
    <p class="small" style="margin-bottom:6px">Based in Catalonia. Day job in commercial strategy and market analysis; builds this on his own time, solo.</p>
    <p class="small" style="margin-bottom:6px">Runs his own AI-agent operation daily since October 2026: a chief-of-staff agent, scheduled research runs and a personal data hub on the Model Context Protocol, the same protocol the hero display will use.</p>
    <p class="small" style="margin-bottom:6px">Method: research first and every number sourced; design-led; hardware sourced, software owned.</p>
    <p class="small ph" style="margin:0">Education, languages, earlier projects: [placeholder for Oscar]</p>
  </div>
</div>
<div class="hr" style="margin:16px 0"></div>
<p class="small"><b>Team.</b> Solo founder today. First hires follow the hero unit: industrial design and firmware [placeholder for Oscar's plan].</p>'''
    right = f'''
<div class="label">The ask for this conversation</div>
<div class="steps" style="grid-template-columns:1fr;gap:12px">
  <div class="step"><div class="n">1</div><div class="h">Your read on the catalogue</div><div class="d">Of these seven, which would you buy at the printed price, and which never? That answer is worth more to me than a cheque today.</div></div>
  <div class="step"><div class="n">2</div><div class="h">One introduction in Shenzhen</div><div class="d">An ODM, sourcing agent or factory contact who could build a sample of the hero display next quarter.</div></div>
  <div class="step"><div class="n">3</div><div class="h">A second meeting, with a trigger</div><div class="d">When the hero unit works in my hand, may I show it to you?</div></div>
</div>
<p class="small" style="margin-top:14px"><b>Not on the table today:</b> valuation, round size, equity. A unit first.</p>'''
    return slide(9, "Founder and ask", "Founder and ask",
                 f'<div class="cols c2">{f"<div>{left}</div>"}<div>{right}</div></div>',
                 "No valuation, round size or equity appears in this deck, by design.")


def s_sources():
    items = "".join(f"<div><b>{n}</b>{esc(label)} <span class='muted'>({esc(dom)})</span></div>" for n, label, dom in SOURCES)
    body = f'''
<p class="small" style="margin-bottom:10px">Every number on the slides carries one of these source numbers. Full URLs, dates and the verification tag for each figure (opened page, or search snippet only) are in <b>research.md</b> next to this deck. Opinions are labelled on the slide where they appear. Placeholders are Oscar's inputs (catalogue renders and prices, brand name, hero unit cost and MOQ) or figures no source gave.</p>
<div class="src" style="column-count:4;column-gap:22px;font-size:9px;line-height:1.3">{items}</div>'''
    return slide(10, "Appendix", "Sources and method", body, "Research by the HQ run of 27 Nov 2026, about 270 web calls, primary sources preferred.")


def main():
    slides = [s_cover(), s_problem(), s_hero(), s_catalogue(), s_market(), s_competition(), s_business(), s_plan(), s_founder(), s_sources()]
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{esc(BRAND)}: gadgets pitch deck v1 (draft, 27 Nov 2026)</title>
<meta name="viewport" content="width=1280">
<style>{CSS}</style></head>
<body>
{"".join(slides)}
</body></html>'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"wrote {OUT} ({len(doc)//1024} KB, {len(slides)} slides)")


if __name__ == "__main__":
    main()
