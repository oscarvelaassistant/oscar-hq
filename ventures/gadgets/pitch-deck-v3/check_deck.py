#!/usr/bin/env python3
"""No-browser checks for deck.html (run: python3 -I check_deck.py from this folder).

1. every inline SVG parses as XML;
2. no <text> in an SVG runs outside its viewBox, overlaps another <text>, or sits on a solid bar; no short vertical leader line crosses a label
   (width estimated from character count: 0.54 em regular, 0.58 em bold or serif);
3. no em dash anywhere in the file;
4. banned words are absent (PersonalPress, Fionn, ARESA, shipyard, valuation/round/equity only in the off-the-table lines).
Exit code 1 if anything fails. The estimate is conservative but is not a render: Vela's PDF render is the final visual check.
"""
import html
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "deck.html")
raw = open(SRC, encoding="utf-8").read()
problems = []

svgs = re.findall(r"<svg\b.*?</svg>", raw, flags=re.S)
print(f"{len(svgs)} inline SVGs")


def text_box(el, size, anchor, x, y, rot):
    s = "".join(el.itertext())
    bold = int(float(el.get("font-weight", "400"))) >= 600
    serif = "Georgia" in (el.get("font-family") or "")
    em = 0.58 if serif else (0.58 if bold else 0.54)
    w = len(s) * size * em
    if anchor == "middle":
        x0, x1 = x - w / 2, x + w / 2
    elif anchor == "end":
        x0, x1 = x - w, x
    else:
        x0, x1 = x, x + w
    y0, y1 = y - size * 0.80, y + size * 0.22
    if rot:  # rotate(-90 cx cy): the run goes up from (x, y) for "start", down for "end"
        L = x1 - x0
        if anchor == "end":
            return (x - size * 0.80, y, x + size * 0.22, y + L), s
        return (x - size * 0.80, y - L, x + size * 0.22, y), s
    return (x0, y0, x1, y1), s


for si, sv in enumerate(svgs):
    try:
        root = ET.fromstring(sv)
    except ET.ParseError as e:
        problems.append(f"svg {si}: does not parse: {e}")
        continue
    vb = [float(v) for v in root.get("viewBox").split()]
    W, H = vb[2], vb[3]
    boxes = []
    for el in root.iter("{http://www.w3.org/2000/svg}text"):
        try:
            x = float(el.get("x")); y = float(el.get("y")); size = float(el.get("font-size", "12"))
        except (TypeError, ValueError):
            continue
        anchor = el.get("text-anchor", "start")
        rot = "rotate" in (el.get("transform") or "")
        b, s = text_box(el, size, anchor, x, y, rot)
        boxes.append((b, s))
        if b[0] < -0.5 or b[1] < -0.5 or b[2] > W + 0.5 or b[3] > H + 0.5:
            problems.append(f"svg {si} ({int(W)}x{int(H)}): '{s[:40]}' runs outside: box {tuple(round(v) for v in b)}")
    # text over a solid bar (non-white text on a grey, red or dark bar), and short leader lines through text
    bars = []
    for r in root.iter("{http://www.w3.org/2000/svg}rect"):
        if r.get("fill") in ("#a8a398", "#b8371f", "#3a3630") and r.get("opacity") is None:
            bars.append((float(r.get("x")), float(r.get("y")), float(r.get("x")) + float(r.get("width")), float(r.get("y")) + float(r.get("height"))))
    for el in root.iter("{http://www.w3.org/2000/svg}text"):
        if el.get("fill") in ("#ffffff", "#f6f3ec", "#f3d9d2") or "<g transform" in sv:   # light text on dark shapes; scaled object groups
            continue
        try:
            x = float(el.get("x")); y = float(el.get("y")); size = float(el.get("font-size", "12"))
        except (TypeError, ValueError):
            continue
        b, s_ = text_box(el, size, el.get("text-anchor", "start"), x, y, "rotate" in (el.get("transform") or ""))
        for bar in bars:
            ox = min(b[2], bar[2]) - max(b[0], bar[0]); oy = min(b[3], bar[3]) - max(b[1], bar[1])
            if ox > 3 and oy > 3:
                problems.append(f"svg {si} ({int(W)}x{int(H)}): text '{s_[:34]}' sits on a bar ({ox:.0f}x{oy:.0f}px)")
    for ln in root.iter("{http://www.w3.org/2000/svg}line"):
        x1, y1, x2, y2 = (float(ln.get(k)) for k in ("x1", "y1", "x2", "y2"))
        if abs(x1 - x2) < 0.1 and 6 < abs(y2 - y1) < 40:   # a vertical leader
            for b, s_ in boxes:
                if b[0] + 1 < x1 < b[2] - 1 and min(y1, y2) + 1 < b[3] and max(y1, y2) - 1 > b[1]:
                    problems.append(f"svg {si} ({int(W)}x{int(H)}): leader line at x={x1:.0f} crosses '{s_[:34]}'")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, sa = boxes[i]; c, sc = boxes[j]
            ox = min(a[2], c[2]) - max(a[0], c[0])
            oy = min(a[3], c[3]) - max(a[1], c[1])
            if ox > 1.5 and oy > 1.5:
                problems.append(f"svg {si} ({int(W)}x{int(H)}): overlap '{sa[:32]}' x '{sc[:32]}' ({ox:.0f}x{oy:.0f}px)")

if chr(0x2014) in raw or "&mdash;" in raw or "&#8212;" in raw:
    problems.append("em dash found")
low = html.unescape(re.sub(r"<style.*?</style>", "", raw, flags=re.S)).lower()
for bad in ("personalpress", "fionn", "aresa", "shipyard", "naval"):
    if bad in low:
        problems.append(f"banned word: {bad}")
for w in ("valuation", "round size", "equity"):
    for m in re.finditer(w, low):
        ctx = low[max(0, m.start() - 60): m.end() + 70]
        if "not on the table" not in ctx and "by design" not in ctx and "no valuation" not in ctx:
            problems.append(f"'{w}' outside an off-the-table line: ...{ctx}...")

print("\n".join(problems) if problems else "all checks passed")
sys.exit(1 if problems else 0)
