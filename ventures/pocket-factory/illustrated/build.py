"""Builds pocket-factory-3pager.pdf (A4, 3 pages), the art/ folder and preview/.

    python3 ventures/pocket-factory/illustrated/build.py

Source of truth for the document: this file (layout and copy) and art.py (pixel art).
Needs Python 3 with fontTools and Pillow. Fonts: IBM Plex Serif, IBM Plex Mono and
Press Start 2P (all SIL Open Font License), read from FONT_DIR.
Each page is drawn as a 336 dpi raster (so it looks the same in every viewer) with an
invisible text layer on top, so the text can be selected and searched and the links work.
preview/page-N.png are the exact page images inside the PDF.
"""
import io
import os
import zlib

from fontTools import subset
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

import art

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'pocket-factory-3pager.pdf')
FONT_DIR = '/usr/share/fonts/truetype/sand-box/google/'
FONT_FILES = {
    'px': 'Press Start 2P/PressStart2P-Regular.ttf',
    'serif': 'IBM Plex Serif/IBMPlexSerif-Regular.ttf',
    'serifm': 'IBM Plex Serif/IBMPlexSerif-Medium.ttf',
    'serifi': 'IBM Plex Serif/IBMPlexSerif-Italic.ttf',
    'mono': 'IBM Plex Mono/IBMPlexMono-Regular.ttf',
    'monob': 'IBM Plex Mono/IBMPlexMono-SemiBold.ttf',
}

MM = 72 / 25.4
PW, PH = 210 * MM, 297 * MM
INK, GREY, RULE, PAPER = '#1d1c1a', '#6a655d', '#c9c3b8', '#faf7f0'
ACC, TINT, WHITE, DGREY = '#e8590c', '#fbe3cf', '#ffffff', '#4a4743'
LEFT, RIGHT = 18.0, 192.0
CW = RIGHT - LEFT
S = 2304 / 174.0          # raster pixels per mm (336 dpi): 12 pixels per hero art pixel
SS = 2                    # supersampling while drawing
PXW, PXH = int(round(210 * S)), int(round(297 * S))

SRC1 = ('[1] Seeed reBot-DevArm, open hardware under CERN-OHL-W 2.0, "effective May 11, 2026": ',
        'github.com/Seeed-Projects/reBot-DevArm', 'https://github.com/Seeed-Projects/reBot-DevArm')
SRC2 = ('[2] Powerhouse Residency, 10 weeks in Shenzhen from 1 March 2027: ',
        'powerhouse.engineering/residency', 'https://powerhouse.engineering/residency')


def P(v):
    """mm to supersampled pixels, snapped to the final pixel grid."""
    return int(round(v * S)) * SS


def LW(pt):
    """Line width in points to supersampled pixels."""
    return max(1, int(round(pt / MM * S))) * SS


class Font:
    def __init__(self, key, path):
        self.key, self.path = key, path
        self.tt = TTFont(path)
        self.cmap = self.tt.getBestCmap()
        self.upem = self.tt['head'].unitsPerEm
        self.hmtx = self.tt['hmtx']
        self.used = set(' ')
        self.cache = {}

    def pil(self, size):
        """PIL face for a size in points, at the supersampled page resolution."""
        if size not in self.cache:
            self.cache[size] = ImageFont.truetype(self.path, size / MM * S * SS)
        return self.cache[size]


class Page:
    """One A4 page: a raster the reader sees, plus an invisible text layer and links."""

    def __init__(self, doc):
        self.doc, self.ops, self.links = doc, [], []
        self.im = Image.new('RGB', (PXW * SS, PXH * SS), PAPER)
        self.d = ImageDraw.Draw(self.im)

    def fill(self, x, y, w, h, c):
        self.d.rectangle([P(x), P(y), P(x + w) - 1, P(y + h) - 1], fill=c)

    def stroke(self, x, y, w, h, c, lw=0.6):
        t = LW(lw)
        o = t // 2
        self.d.rectangle([P(x) - o, P(y) - o, P(x + w) - 1 + o, P(y + h) - 1 + o], outline=c, width=t)

    def line(self, pts, c, lw=0.6):
        self.d.line([(P(x), P(y)) for x, y in pts], fill=c, width=LW(lw), joint='curve')

    def poly(self, pts, fill=None, strokec=None, lw=0.6):
        q = [(x * S * SS, y * S * SS) for x, y in pts]
        if fill:
            self.d.polygon(q, fill=fill)
        if strokec:
            self.d.line(q + [q[0], q[1]], fill=strokec, width=LW(lw), joint='curve')

    def arrow(self, pts, c=INK, lw=0.9, head=2.0):
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        bx, by = x1 - ux * head, y1 - uy * head
        self.line(pts[:-1] + [(bx, by)], c, lw)
        self.poly([(x1, y1), (bx - uy * head * 0.55, by + ux * head * 0.55),
                   (bx + uy * head * 0.55, by - ux * head * 0.55)], fill=c)

    def measure(self, s, font, size, track=0.0):
        """Width in mm."""
        f = self.doc.fonts[font].pil(size)
        if track:
            return (sum(f.getlength(ch) for ch in s) / (S * SS)) + track / MM * len(s)
        return f.getlength(s) / (S * SS)

    def text(self, x, y, s, font, size, c=INK, track=0.0, align='l'):
        fo = self.doc.fonts[font]
        for ch in s:
            if ord(ch) not in fo.cmap:
                raise ValueError('%s has no glyph for %r' % (font, ch))
        fo.used.update(s)
        f = fo.pil(size)
        w = self.measure(s, font, size, track)
        vis = w - (track / MM if track else 0)
        if align == 'r':
            x -= vis
        elif align == 'c':
            x -= vis / 2
        px, py = x * S * SS, round(y * S * SS)
        if track:
            for ch in s:
                self.d.text((px, py), ch, font=f, fill=c, anchor='ls')
                px += f.getlength(ch) + track / MM * S * SS
        else:
            self.d.text((px, py), s, font=f, fill=c, anchor='ls')
        # invisible copy for selection and search, stretched to the drawn width
        nat = sum(fo.hmtx[fo.cmap[ord(ch)]][0] for ch in s) * size / fo.upem
        tz = 100.0 * (vis * MM) / nat if nat else 100.0
        self.ops.append('BT 3 Tr /%s %.2f Tf %.2f Tz %.2f %.2f Td <%s> Tj ET'
                        % (font, size, tz, x * MM, PH - y * MM, s.encode('cp1252').hex()))
        return w

    def para(self, x, y, w, s, font, size, lead, c=INK):
        """Wrapped text. y is the first baseline; lead in mm. Returns the next baseline."""
        for block in s.split('\n'):
            line = ''
            for word in block.split(' '):
                trial = (line + ' ' + word) if line else word
                if self.measure(trial, font, size) > w and line:
                    self.text(x, y, line, font, size, c)
                    y += lead
                    line = word
                else:
                    line = trial
            if line:
                self.text(x, y, line, font, size, c)
                y += lead
        return y

    def imsize(self, name, w):
        """Size in mm an art piece gets when asked for width w: whole pixels per art pixel."""
        a = self.doc.arts[name]
        n = max(1, int(round(w * S / a.w)))
        return a.w * n / S, a.h * n / S

    def image(self, name, x, y, w):
        a = self.doc.arts[name]
        n = max(1, int(round(w * S / a.w)))
        data, alpha, pw, ph = a.raw(n * SS)
        im = Image.frombytes('RGB', (pw, ph), data)
        mask = Image.frombytes('L', (pw, ph), alpha) if alpha else None
        self.im.paste(im, (P(x), P(y)), mask)
        return a.w * n / S, a.h * n / S

    def link(self, x, y, w, h, url):
        self.links.append((x * MM, PH - (y + h) * MM, (x + w) * MM, PH - y * MM, url))

    def final(self):
        """The page as it ships: downsampled, then reduced to a 256-colour palette."""
        im = self.im.reduce(SS)
        return im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


class Doc:
    def __init__(self):
        self.fonts = {k: Font(k, FONT_DIR + v) for k, v in FONT_FILES.items()}
        self.arts = art.all_art()
        self.pages = []

    def page(self):
        p = Page(self)
        self.pages.append(p)
        return p

    def save(self, path, preview_dir=None):
        objs = {}
        counter = [2]

        def new():
            counter[0] += 1
            return counter[0]

        def stream(d, data):
            data = zlib.compress(data, 9)
            return (('<< %s /Filter /FlateDecode /Length %d >>\nstream\n' % (d, len(data))).encode('latin-1')
                    + data + b'\nendstream')

        font_refs = {}
        for i, (key, f) in enumerate(self.fonts.items()):
            tt = f.tt
            head, hhea, os2 = tt['head'], tt['hhea'], tt['OS/2']
            k = 1000.0 / f.upem
            widths = []
            for code in range(32, 256):
                try:
                    g = f.cmap.get(ord(bytes([code]).decode('cp1252')))
                    widths.append(int(round(f.hmtx[g][0] * k)) if g else 0)
                except UnicodeDecodeError:
                    widths.append(0)
            psname = tt['name'].getDebugName(6) or key
            base = 'PF%s+%s' % ('ABCDEF'[i] * 4, psname.replace(' ', ''))
            flags = 32 | (1 if key in ('mono', 'monob', 'px') else 0) | (64 if key == 'serifi' else 0)
            bbox = [int(round(v * k)) for v in (head.xMin, head.yMin, head.xMax, head.yMax)]
            cap = getattr(os2, 'sCapHeight', 0) or hhea.ascent
            opts = subset.Options()
            opts.notdef_outline = True
            opts.layout_features = []
            opts.hinting = False
            opts.name_IDs = [1, 2, 6]
            opts.drop_tables += ['meta']
            sub = TTFont(f.path)
            s = subset.Subsetter(opts)
            s.populate(text=''.join(sorted(f.used)))
            s.subset(sub)
            buf = io.BytesIO()
            sub.save(buf)
            data = buf.getvalue()
            nfile, ndesc, nfont = new(), new(), new()
            objs[nfile] = stream('/Length1 %d' % len(data), data)
            objs[ndesc] = ('<< /Type /FontDescriptor /FontName /%s /Flags %d /FontBBox [%d %d %d %d] '
                           '/ItalicAngle %s /Ascent %d /Descent %d /CapHeight %d /StemV 80 /FontFile2 %d 0 R >>'
                           % (base, flags, bbox[0], bbox[1], bbox[2], bbox[3], tt['post'].italicAngle,
                              round(hhea.ascent * k), round(hhea.descent * k), round(cap * k), nfile)).encode()
            objs[nfont] = ('<< /Type /Font /Subtype /TrueType /BaseFont /%s /FirstChar 32 /LastChar 255 '
                           '/Widths [%s] /Encoding /WinAnsiEncoding /FontDescriptor %d 0 R >>'
                           % (base, ' '.join(str(w) for w in widths), ndesc)).encode()
            font_refs[key] = nfont
        fres = ' '.join('/%s %d 0 R' % (k, n) for k, n in font_refs.items())

        kids = []
        for i, p in enumerate(self.pages):
            q = p.final()
            if preview_dir:
                q.convert('RGB').save(os.path.join(preview_dir, 'page-%d.png' % (i + 1)), optimize=True)
            pal = bytes(q.getpalette()[:768]).ljust(768, b'\0')
            nim, nc, npg = new(), new(), new()
            objs[nim] = stream('/Type /XObject /Subtype /Image /Width %d /Height %d /BitsPerComponent 8 '
                               '/ColorSpace [/Indexed /DeviceRGB 255 <%s>]' % (q.width, q.height, pal.hex()),
                               q.tobytes())
            content = 'q %.2f 0 0 %.2f 0 0 cm /Pg Do Q\n' % (PW, PH) + '\n'.join(p.ops)
            objs[nc] = stream('', content.encode('latin-1'))
            annots = ''
            if p.links:
                annots = ' /Annots [%s]' % ' '.join(
                    '<< /Type /Annot /Subtype /Link /Rect [%.2f %.2f %.2f %.2f] /Border [0 0 0] '
                    '/A << /S /URI /URI (%s) >> >>' % l for l in p.links)
            objs[npg] = ('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.2f %.2f] /Resources << /Font << %s >> '
                         '/XObject << /Pg %d 0 R >> >> /Contents %d 0 R%s >>'
                         % (PW, PH, fres, nim, nc, annots)).encode()
            kids.append(npg)
        objs[1] = b'<< /Type /Catalog /Pages 2 0 R /Lang (en) >>'
        objs[2] = ('<< /Type /Pages /Kids [%s] /Count %d >>'
                   % (' '.join('%d 0 R' % k for k in kids), len(kids))).encode()
        ninfo = new()
        objs[ninfo] = (b'<< /Title (R-T-SAN: concept) /Author (Oscar Bonnefon) '
                       b'/Subject (Three-page illustrated concept, November 2026) >>')

        out = io.BytesIO()
        out.write(b'%PDF-1.5\n%\xe2\xe3\xcf\xd3\n')
        offs = {}
        for n in sorted(objs):
            offs[n] = out.tell()
            out.write(('%d 0 obj\n' % n).encode() + objs[n] + b'\nendobj\n')
        xref = out.tell()
        total = max(objs) + 1
        out.write(('xref\n0 %d\n0000000000 65535 f \n' % total).encode())
        for n in range(1, total):
            out.write(('%010d 00000 n \n' % offs[n]).encode())
        out.write(('trailer\n<< /Size %d /Root 1 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n'
                   % (total, ninfo, xref)).encode())
        with open(path, 'wb') as fh:
            fh.write(out.getvalue())


# ------------------------------------------------------------ page parts
def header(p, n):
    p.text(LEFT, 13, 'R-T-SAN', 'monob', 7, INK, 1.4)
    p.text(RIGHT, 13, 'CONCEPT, NOVEMBER 2026    %d/3' % n, 'mono', 7, GREY, 1.0, 'r')
    p.line([(LEFT, 16), (RIGHT, 16)], RULE, 0.5)


def footer(p, sources):
    p.line([(LEFT, 277), (RIGHT, 277)], RULE, 0.5)
    y = 281.5
    for (label, shown, url) in sources:
        w = p.text(LEFT, y, label, 'mono', 6.2, GREY)
        w2 = p.text(LEFT + w, y, shown, 'mono', 6.2, INK)
        p.link(LEFT + w, y - 2.2, w2, 3, url)
        y += 3.4
    p.text(RIGHT, 284.9, 'Oscar Bonnefon', 'mono', 6.2, GREY, 0, 'r')


def kicker(p, y, s, c=ACC, x=LEFT):
    p.text(x, y, s, 'monob', 7.5, c, 1.2)


def badge(p, x, y, n, size=4.2):
    p.fill(x, y, size, size, INK)
    p.text(x + size / 2, y + size - 1.2, str(n), 'monob', 7, WHITE, 0, 'c')


# ----------------------------------------------------------------- page 1
def page1(doc):
    p = doc.page()
    header(p, 1)
    kicker(p, 26, 'THE R-T-SAN MACHINE')
    p.text(LEFT - 0.6, 43, 'R-T-SAN', 'px', 40, INK)
    p.para(LEFT, 52.5, 174, 'A container you can drop anywhere in the world, one day on other planets. Two robot '
           'arms do what a team of highly skilled artisans would, 24/7.', 'serif', 14, 6.6)

    hy = 68.0
    k = CW / 192.0
    _, hh = p.image('hero', LEFT, hy, CW)
    p.stroke(LEFT, hy, CW, hh, INK, 0.7)
    marks = [(1, 145, 5), (2, 11, 5), (3, 24, 34), (4, 108, 19), (5, 113, 57), (6, 169, 33), (7, 177, 38)]
    for n, ax, ay in marks:
        badge(p, LEFT + ax * k, hy + ay * k, n)

    legend = ['Request: file or photo', 'Tools it can pick up', 'Raw stock', 'Two robot arms, run by AI',
              'Machining station', 'Inspection camera', 'Checked, accepted part']
    ly = hy + hh + 4.0
    cwid = CW / 4
    for i, s in enumerate(legend):
        x = LEFT + (i % 4) * cwid
        y = ly + (i // 4) * 6.2
        badge(p, x, y, i + 1, 3.8)
        p.text(x + 5.4, y + 2.9, s, 'mono', 7, INK)
    p.text(RIGHT, ly + 6.2 + 2.9, 'Concept drawing. Nothing here is built yet.', 'serifi', 7, GREY, 0, 'r')

    y0 = ly + 22
    p.line([(LEFT, y0 - 6.5), (RIGHT, y0 - 6.5)], RULE, 0.5)
    cw2 = 81.0
    x2 = RIGHT - cw2
    kicker(p, y0, 'WHAT IT IS')
    p.para(LEFT, y0 + 7, cw2,
           'R-T-SAN is a container you can drop anywhere in the world, however remote, and one day on other '
           'planets. Inside, two robot arms, run by AI, use a panoply of tools to cut, solder, machine, assemble '
           'and check, 24/7. Raw material goes in. A checked, accepted part comes out.', 'serif', 11, 5.6)
    kicker(p, y0, 'FIRST USE', x=x2)
    p.para(x2, y0 + 7, cw2,
           "Unlike today's specialized robots, R-T-SAN is general: it makes parts without skilled hands. The arms "
           'are off the shelf and open now [1]. The skills are not. It starts narrow: one material, one process, '
           'one family of parts. Each skill it learns widens what it can make.', 'serif', 11, 5.6)

    qy = y0 + 64
    p.fill(LEFT, qy - 7, 1.2, 13.5, ACC)
    p.text(LEFT + 6, qy, '“A Shenzhen factory in a pocket.”', 'serifi', 21, INK)
#    p.text(LEFT + 6, qy + 6, 'OSCAR BONNEFON, FIRST VOICE MEMO ON THE IDEA, 13 NOVEMBER 2026', 'mono', 6.2, GREY, 0.8)
    footer(p, [SRC1])


# ----------------------------------------------------------------- page 2
def page2(doc):
    p = doc.page()
    header(p, 2)
    kicker(p, 26, 'HOW IT WORKS')
    p.text(LEFT, 38, 'One loop, with nobody in between.', 'serifm', 23, INK)
    p.para(LEFT, 46.5, 174, 'Two robot arms, a panoply of tools, 24/7: a request goes in and a checked part comes '
           'out. If the check fails, R-T-SAN scraps the part and goes again.', 'serif', 11, 5.4)

    bw, bh, gap = 38.0, 36.0, (CW - 4 * 38.0) / 3
    xs = [LEFT + i * (bw + gap) for i in range(4)]
    r1, r2 = 64.0, 114.0

    def step(x, y, n, ic, label, desc):
        p.fill(x, y, bw, bh, WHITE)
        p.stroke(x, y, bw, bh, INK, 0.7)
        p.image('icon-' + ic, x + 3, y + 3, 14.4)
        p.text(x + bw - 3, y + 8.6, str(n), 'px', 11, ACC, 0, 'r')
        p.text(x + 3, y + 23.4, label, 'monob', 8, INK, 0.6)
        p.para(x + 3, y + 28.2, bw - 5, desc, 'serif', 8.5, 3.9, DGREY)

    step(xs[0], r1, 1, 'request', 'REQUEST IN', 'A file, or a photo of a broken part.')
    step(xs[1], r1, 2, 'pick', 'PICK STOCK', 'An arm takes a bar from the rack.')
    step(xs[2], r1, 3, 'hold', 'HOLD', 'The bar is clamped.')
    step(xs[3], r1, 4, 'machine', 'MACHINE', 'The right tool cuts the shape.')
    step(xs[3], r2, 5, 'finish', 'FINISH', 'Edges are cleaned up.')
    step(xs[2], r2, 6, 'check', 'CHECK', 'A camera inspects the part.')
    step(xs[0], r2, 7, 'out', 'PART OUT', 'Checked and handed over.')

    my1, my2 = r1 + bh / 2, r2 + bh / 2
    for i in range(3):
        p.arrow([(xs[i] + bw + 1, my1), (xs[i + 1] - 1, my1)])
    cx3 = xs[3] + bw / 2
    p.arrow([(cx3, r1 + bh + 1), (cx3, r2 - 1)])
    p.arrow([(xs[3] - 1, my2), (xs[2] + bw + 1, my2)])
    # decision
    cx1 = xs[1] + bw / 2
    hw, hhh = 19.0, 13.0
    p.arrow([(xs[2] - 1, my2), (cx1 + hw + 0.8, my2)])
    p.poly([(cx1 - hw, my2), (cx1, my2 - hhh), (cx1 + hw, my2), (cx1, my2 + hhh)], fill=WHITE, strokec=ACC, lw=1.2)
    p.text(cx1, my2 + 1.1, 'ACCEPTED?', 'monob', 8, INK, 0.6, 'c')
    p.arrow([(cx1 - hw - 0.8, my2), (xs[0] + bw + 1, my2)])
    p.text((cx1 - hw + xs[0] + bw) / 2, my2 - 1.6, 'YES', 'monob', 6.5, INK, 0.6, 'c')
    p.arrow([(cx1, my2 - hhh - 0.8), (cx1, r1 + bh + 1)], ACC, 1.1)
    p.text(cx1 + 2.4, (my2 - hhh + r1 + bh) / 2 + 0.2, 'NO: SCRAP IT,', 'monob', 6.5, ACC, 0.6)
    p.text(cx1 + 2.4, (my2 - hhh + r1 + bh) / 2 + 3.2, 'GO AGAIN', 'monob', 6.5, ACC, 0.6)

    # the layer that is ours
    sy = 163.0
    kicker(p, sy, 'WHAT IS BOUGHT, WHAT IS OURS')
    oy, oh = sy + 5, 61.0
    p.fill(LEFT, oy, CW, oh, TINT)
    p.stroke(LEFT, oy, CW, oh, ACC, 1.2)
    p.text(LEFT + 5, oy + 8.5, 'OURS', 'px', 9, ACC)
    lx = LEFT + 5
    p.text(lx, oy + 17, 'THE SKILL LIBRARY', 'monob', 8, INK, 0.6)
    names = ['pick', 'hold', 'machine', 'finish', 'check']
    cwid, _ = p.imsize('skill-pick', 13.6)
    for i, n in enumerate(names):
        x = lx + i * 16.4
        p.image('skill-' + n, x, oy + 20.5, cwid)
        p.text(x + cwid * 9.5 / 22, oy + 41.6, n.upper(), 'mono', 5.6, DGREY, 0.3, 'c')
    p.para(lx, oy + 47.5, 80, 'Each step of the loop is a learned skill, kept like a cartridge. Every skill one '
           'R-T-SAN learns, every R-T-SAN gets.', 'serif', 9.5, 4.5)

    rx = LEFT + 98
    p.text(rx, oy + 17, 'THE FACTORY PROCESS', 'monob', 8, INK, 0.6)
    isz, _ = p.imsize('icon-pick', 9.6)
    igap = 5.2
    seq = ['pick', 'hold', 'machine', 'check', 'out']
    iy = oy + 22
    for i, n in enumerate(seq):
        x = rx + i * (isz + igap)
        p.image('icon-' + n, x, iy, isz)
        if i < len(seq) - 1:
            p.arrow([(x + isz + 0.7, iy + isz / 2), (x + isz + igap - 0.7, iy + isz / 2)], INK, 0.7, 1.5)
    xa = rx + 3 * (isz + igap) + isz / 2
    xb = rx + isz / 2
    p.arrow([(xa, iy + isz + 1), (xa, iy + isz + 4.6), (xb, iy + isz + 4.6), (xb, iy + isz + 1)], ACC, 0.8, 1.5)
    p.text((xa + xb) / 2, iy + isz + 8, 'CHECK FAILED: ROUND AGAIN', 'mono', 5.6, ACC, 0.4, 'c')
    p.para(rx, oy + 47.5, 70, 'It chains the skills into one job and checks the result. A failed check sends '
           'it round again.', 'serif', 9.5, 4.5)

    by = oy + oh + 3
    bh2 = 27.0
    p.fill(LEFT, by, CW, bh2, WHITE)
    p.stroke(LEFT, by, CW, bh2, DGREY, 0.7)
    p.text(LEFT + 5, by + 8.5, 'BOUGHT', 'px', 9, GREY)
    p.image('arm', LEFT + 6, by + 11.5, 16.5)
    tx = LEFT + 40
    p.text(tx, by + 8.2, 'OPEN ARMS, OFF THE SHELF', 'monob', 8, INK, 0.6)
    p.para(tx, by + 14.2, 128, "Seeed's reBot-DevArm went open hardware in May 2026 [1]. Its B601 arms "
           'carry 1.5 kg (DM) or 2.5 kg (RS), with a maximum reach of 767 mm or 754 mm [1]. That bounds the stock '
           'R-T-SAN can lift.',
           'serif', 9.5, 4.5)
    footer(p, [SRC1])


# ----------------------------------------------------------------- page 3
def page3(doc):
    p = doc.page()
    header(p, 3)
    kicker(p, 26, 'WHERE IT GOES')
    p.text(LEFT, 37, 'Every skill one R-T-SAN learns,', 'serifm', 23, INK)
    p.text(LEFT, 46.5, 'every R-T-SAN gets.', 'serifm', 23, INK)

    y = 53.5
    pw, h = p.imsize('town', 84.0)
    x2 = RIGHT - pw
    p.image('town', LEFT, y, pw)
    p.stroke(LEFT, y, pw, h, INK, 0.7)
    p.image('dome', x2, y, pw)
    p.stroke(x2, y, pw, h, INK, 0.7)
    cy = y + h + 5
    p.text(LEFT, cy, 'ANYWHERE IN THE WORLD, HOWEVER REMOTE', 'monob', 7.5, INK, 0.8)
    p.para(LEFT, cy + 4.8, pw, 'Far from any factory. Raw material in, parts out.', 'serif', 9.5, 4.5, DGREY)
    p.text(x2, cy, 'ON ANOTHER PLANET, ONE DAY', 'monob', 7.5, INK, 0.8)
    p.para(x2, cy + 4.8, pw, 'The same R-T-SAN, the same skills, far from Earth.', 'serif', 9.5, 4.5, DGREY)

    y = cy + 11.5
    _, h = p.image('share', LEFT, y, CW)
    p.stroke(LEFT, y, CW, h, INK, 0.7)
    cy = y + h + 5
    p.text(LEFT, cy, 'MANY R-T-SANS, ONE SKILL LIBRARY', 'monob', 7.5, INK, 0.8)
    p.text(RIGHT, cy, 'CONCEPT DRAWINGS', 'mono', 6.2, GREY, 0.8, 'r')
    p.para(LEFT, cy + 4.8, CW, 'A skill learned in one place reaches every R-T-SAN, the way a phone gets updates. '
           'The end goal: give it raw material and a request, and it does what a team of highly skilled artisans '
           'would, 24/7. One skill at a time.', 'serif', 9.5, 4.5, DGREY)

    ty = cy + 15.5
    p.line([(LEFT, ty), (RIGHT, ty)], RULE, 0.5)
    kicker(p, ty + 6.5, 'THE TEN WEEKS: POWERHOUSE RESIDENCY, SHENZHEN, FROM 1 MARCH 2027 [2]')
    by = ty + 10
    g = 2.0
    bw = (CW - 9 * g) / 10
    for i in range(10):
        x = LEFT + i * (bw + g)
        last = i == 9
        p.fill(x, by, bw, 6.6, ACC if last else WHITE)
        p.stroke(x, by, bw, 6.6, ACC if last else INK, 0.6)
        p.text(x + bw / 2, by + 4.5, 'W%d' % (i + 1), 'monob' if last else 'mono', 6.5, WHITE if last else GREY, 0, 'c')
    p.text(LEFT, by + 10.6, 'DEMO DAYS EVERY TWO WEEKS [2]', 'mono', 6.2, GREY, 0.8)
    p.text(RIGHT, by + 10.6, 'ONE LOOP WORKING AND FILMED', 'monob', 6.2, ACC, 0.8, 'r')

    gy = by + 17.5
    cw2 = 82.0
    xr = RIGHT - cw2
    p.text(LEFT, gy, 'THE GOAL', 'monob', 7.5, INK, 1.2)
    p.para(LEFT, gy + 5.6, cw2, 'One loop working and filmed for Demo Day: bar stock in, accepted part out. '
           'One material, one process, one family of parts, on open arms sourced in Shenzhen. If the whole '
           'loop does not fit, an agreed subsystem of it.', 'serif', 9.5, 4.5)
    p.text(xr, gy, 'WHAT POWERHOUSE ADDS [2]', 'monob', 7.5, INK, 1.2)
    p.para(xr, gy + 5.6, cw2, "USD 5,000 of prototyping parts, sourced and bought by Powerhouse, and 40 hours of "
           "its engineers' time. The package is in exchange for equity. It is not cash. That sourcing and those "
           'hours turn a plan into a part on the table.', 'serif', 9.5, 4.5)

    sy = gy + 28.0
    p.stroke(LEFT, sy, CW, 20.5, INK, 0.7)
    p.text(LEFT + 4, sy + 5.9, 'WHERE THIS STANDS', 'monob', 7.5, ACC, 1.0)
    p.text(LEFT + 45, sy + 5.9, 'Step 1: the idea is being refined. Nothing is built yet. Every drawing here is a concept.',
           'serif', 8.6, INK)
    p.line([(LEFT, sy + 9.2), (RIGHT, sy + 9.2)], RULE, 0.5)
    p.text(LEFT + 4, sy + 14.6, 'THE FOUNDER', 'monob', 7.5, ACC, 1.0)
    p.para(LEFT + 45, sy + 14.6, 128, 'French, in Barcelona. Three years in industry as salesperson, business '
           "developer and AI guy. Not an engineer: Shenzhen's engineers and suppliers would help make it real.",
           'serif', 8.6, 4.0)
    footer(p, [SRC1, SRC2])


def main():
    out = os.path.join(HERE, 'art')
    prev = os.path.join(HERE, 'preview')
    os.makedirs(out, exist_ok=True)
    os.makedirs(prev, exist_ok=True)
    doc = Doc()
    for name, a in doc.arts.items():
        a.png(os.path.join(out, name + '.png'), 8 if a.w < 100 else 6)
        a.svg(os.path.join(out, name + '.svg'))
    page1(doc)
    page2(doc)
    page3(doc)
    doc.save(OUT, prev)
    print('wrote', OUT, os.path.getsize(OUT), 'bytes')


if __name__ == '__main__':
    main()
