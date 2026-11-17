"""Pixel art for the R-T-SAN 3-pager. Every drawing is built here, pixel by pixel.

Run through build.py. Each scene is an Art grid of palette keys; it exports PNG and SVG
(art/ folder) and raw RGB for the PDF. All drawings are concepts: nothing shown is built.
"""
import math
import zlib

PAL = {
    'K': '#1d1c1a',  # ink
    'D': '#4a4743',  # dark grey
    'M': '#8b867e',  # mid grey
    'L': '#c9c3b8',  # light grey
    'P': '#e9e4d8',  # pale
    'W': '#faf7f0',  # paper
    'O': '#e8590c',  # accent orange (the part being made, and R-T-SAN's lights)
    'o': '#f4a66a',  # light orange
    'd': '#a63d05',  # dark orange
    's': '#fbe3cf',  # orange tint
}


def rgb(hexc):
    return tuple(int(hexc[i:i + 2], 16) for i in (1, 3, 5))


class Art:
    def __init__(self, w, h, bg=None):
        self.w, self.h = w, h
        self.g = [[bg] * w for _ in range(h)]

    def px(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.g[y][x] = c

    def rect(self, x, y, w, h, c):
        for j in range(y, y + h):
            for i in range(x, x + w):
                self.px(i, j, c)

    def box(self, x, y, w, h, fill, edge='K'):
        self.rect(x, y, w, h, edge)
        if w > 2 and h > 2:
            self.rect(x + 1, y + 1, w - 2, h - 2, fill)

    def line(self, x0, y0, x1, y1, c, t=1):
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        o = t // 2
        while True:
            self.rect(x0 - o, y0 - o, t, t, c)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def limb(self, pts, t=5, fill='L', edge='K'):
        for (a, b) in zip(pts, pts[1:]):
            self.line(a[0], a[1], b[0], b[1], edge, t)
        for (a, b) in zip(pts, pts[1:]):
            self.line(a[0], a[1], b[0], b[1], fill, t - 2)

    def joint(self, x, y, r=3, fill='D', dot=None):
        n = 2 * r + 1
        self.rect(x - r, y - r + 1, n, n - 2, 'K')
        self.rect(x - r + 1, y - r, n - 2, n, 'K')
        self.rect(x - r + 1, y - r + 1, n - 2, n - 2, fill)
        if dot:
            self.px(x, y, dot)

    def disc(self, cx, cy, r, c):
        for j in range(-r, r + 1):
            for i in range(-r, r + 1):
                if i * i + j * j <= r * r + r * 0.6:
                    self.px(cx + i, cy + j, c)

    def sprite(self, x, y, rows):
        for j, row in enumerate(rows):
            for i, ch in enumerate(row):
                if ch != '.':
                    self.px(x + i, y + j, ch)

    def paste(self, x, y, other):
        for j in range(other.h):
            for i in range(other.w):
                c = other.g[j][i]
                if c is not None:
                    self.px(x + i, y + j, c)

    # ---- exports -------------------------------------------------------
    def has_alpha(self):
        return any(c is None for row in self.g for c in row)

    def raw(self, scale):
        """(rgb_bytes, alpha_bytes or None, width, height) upscaled by nearest neighbour."""
        alpha = self.has_alpha()
        rows, arows = [], []
        for row in self.g:
            line = b''.join(bytes(rgb(PAL[c]) if c else (255, 255, 255)) * scale for c in row)
            rows.extend([line] * scale)
            if alpha:
                al = b''.join((b'\xff' if c else b'\x00') * scale for c in row)
                arows.extend([al] * scale)
        return b''.join(rows), (b''.join(arows) if alpha else None), self.w * scale, self.h * scale

    def png(self, path, scale=8):
        from PIL import Image
        data, a, w, h = self.raw(scale)
        im = Image.frombytes('RGB', (w, h), data)
        if a:
            im.putalpha(Image.frombytes('L', (w, h), a))
        im.save(path, optimize=True)

    def svg(self, path):
        out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
               'shape-rendering="crispEdges">' % (self.w, self.h)]
        for y, row in enumerate(self.g):
            x = 0
            while x < self.w:
                c = row[x]
                x2 = x
                while x2 < self.w and row[x2] == c:
                    x2 += 1
                if c:
                    out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>'
                               % (x, y, x2 - x, PAL[c]))
                x = x2
        out.append('</svg>')
        with open(path, 'w') as f:
            f.write('\n'.join(out))


# ---------------------------------------------------------------- sprites
CHECK_BADGE = [
    'KKKKKKKKK',
    'KOOOOOOOK',
    'KOOOOOWOK',
    'KOOOOWOOK',
    'KOWOWOOOK',
    'KOOWOOOOK',
    'KOOOOOOOK',
    'KKKKKKKKK',
]

CARTRIDGE = [
    'KKKKKKK',
    'KOOOOOK',
    'KOWWWOK',
    'KOOOOOK',
    'KOOOOOK',
    'KKOOOKK',
    '.KKKKK.',
]

CARTRIDGE_IN = [
    'MMMMMMM',
    'MoooooM',
    'MoWWWoM',
    'MoooooM',
    'MoooooM',
    'MMoooMM',
    '.MMMMM.',
]

ICONS = {
    'request': [
        '..KKKKKKKKK.....',
        '..KWWWWWWWKK....',
        '..KWWWWWWWKWK...',
        '..KWWWWWWWKKKK..',
        '..KWWWWWWWWWWK..',
        '..KWWOOOOOOWWK..',
        '..KWWOWWWWOWWK..',
        '..KWWOWOOWOWWK..',
        '..KWWOWOOWOWWK..',
        '..KWWOWWWWOWWK..',
        '..KWWOOOOOOWWK..',
        '..KWWWWWWWWWWK..',
        '..KWMMMMMMMWWK..',
        '..KWMMMMMWWWWK..',
        '..KWWWWWWWWWWK..',
        '..KKKKKKKKKKKK..',
    ],
    'pick': [
        '......KKKK......',
        '......KLLK......',
        '....KKKLLKKK....',
        '....KLLLLLLK....',
        '....KLKKKKLK....',
        '....KLKOOKLK....',
        '....KLKOOKLK....',
        '....KKKOOKKK....',
        '.......OO.......',
        '.......OO.......',
        '..MM.MMOOMM.MM..',
        '..MM.MMOOMM.MM..',
        '..MM.MMOOMM.MM..',
        '..MM.MMOOMM.MM..',
        '.KKKKKKKKKKKKKK.',
        '.KDDDDDDDDDDDDK.',
    ],
    'hold': [
        '................',
        '................',
        '......OOOO......',
        '......OOOO......',
        '..KKKKOOOOKKKK..',
        '..KLLKOOOOKLLK..',
        '..KLLKOOOOKLLKKK',
        '..KLLKOOOOKLLKDK',
        '..KLLKKKKKKLLKKK',
        '..KLLLLLLLLLLK..',
        '..KKKKKKKKKKKK..',
        '....KDDDDDDK....',
        '....KDDDDDDK....',
        '.KKKKKKKKKKKKKK.',
        '.KMMMMMMMMMMMMK.',
        '.KKKKKKKKKKKKKK.',
    ],
    'machine': [
        '.....KKKKKK.....',
        '.....KDDDDK.....',
        '.....KDDDDK.....',
        '.....KDDDDK.....',
        '.....KKKKKK.....',
        '......KLLK......',
        '.......LL.......',
        '.......LL...o...',
        '..o....LL..o....',
        '...o...LL.......',
        '.OOOOO.LL.OOOOO.',
        '.OOOOOOOOOOOOOO.',
        '.OOOOOOOOOOOOOO.',
        '.OOOOOOOOOOOOOO.',
        'KKKKKKKKKKKKKKKK',
        'KMMMMMMMMMMMMMMK',
    ],
    'finish': [
        '............KK..',
        '...........KLLK.',
        '..........KLLK..',
        '.........KLLK...',
        '........KLLK....',
        '.......KDDK.....',
        '......KDDK......',
        '.o....KKK.......',
        'ooo..OOOOOOOOO..',
        '.o..OOOOOOOOOOO.',
        '....OOOOOOOOOOO.',
        '....OOOOOOOOOOO.',
        '....OOOOOOOOOOO.',
        '.....OOOOOOOOO..',
        'KKKKKKKKKKKKKKKK',
        'KMMMMMMMMMMMMMMK',
    ],
    'check': [
        '....KKKKKKKK....',
        '....KDDDDDDK....',
        '....KDDKKDDK....',
        '....KDDKKDDK....',
        '....KKKKKKKK....',
        '......KooK......',
        '......ssss......',
        '.....ssssss.....',
        '....ssssssss....',
        '...ssssssssss...',
        '..sssOOOOOOsss..',
        '..sssOOOOOOsss..',
        '..sssOOOOOOsss..',
        '..sssOOOOOOsss..',
        'KKKKKKKKKKKKKKKK',
        'KMMMMMMMMMMMMMMK',
    ],
    'out': [
        '.......KKKKKKKKK',
        '.......KOOOOOOOK',
        '.......KOOOOOWOK',
        '.......KOOOOWOOK',
        '.......KOWOWOOOK',
        '.......KOOWOOOOK',
        '.......KOOOOOOOK',
        '.......KKKKKKKKK',
        '................',
        '....OOOOOO......',
        '...OOOOOOOO.....',
        '.K.OOOOOOOO...K.',
        '.K.OOOOOOOO...K.',
        '.KLLLLLLLLLLLLK.',
        '.KLLLLLLLLLLLLK.',
        '.KKKKKKKKKKKKKK.',
    ],
}


def icon(name):
    a = Art(16, 16)
    rows = ICONS[name]
    assert len(rows) == 16 and all(len(r) == 16 for r in rows), name
    a.sprite(0, 0, rows)
    return a


def cartridge(name):
    """A skill cartridge: the loop-step icon inside a cartridge shell."""
    a = Art(22, 27)
    a.rect(0, 0, 19, 27, 'K')      # shell, with a cut corner top right
    a.rect(19, 3, 3, 24, 'K')
    a.rect(1, 1, 18, 25, 'D')
    a.rect(19, 4, 2, 22, 'D')
    a.rect(2, 2, 18, 18, 'K')      # window
    a.rect(3, 3, 16, 16, 'W')
    a.sprite(3, 3, ICONS[name])
    a.rect(4, 22, 14, 2, 'O')      # label strip
    return a


# --------------------------------------------------------------- R-T-SAN
def artisan_small(a, cx, by, left=None, right=None, lights='O'):
    """Small R-T-SAN standing on a surface whose top row is `by`.
    left / right: (elbow, wrist) points relative to (cx, by)."""
    a.rect(cx - 7, by - 2, 15, 2, 'K')            # base plate
    a.box(cx - 3, by - 12, 7, 10, 'L')            # torso
    a.px(cx, by - 8, lights)
    a.px(cx, by - 6, 'M')
    a.rect(cx - 8, by - 14, 17, 3, 'K')           # shoulder beam
    a.rect(cx - 1, by - 15, 3, 1, 'K')            # neck
    a.box(cx - 4, by - 22, 9, 7, 'L')             # head
    a.rect(cx - 3, by - 20, 7, 3, 'K')            # visor
    a.px(cx - 2, by - 19, lights)
    a.px(cx + 2, by - 19, lights)
    left = left or ((-14, -20), (-17, -9))
    right = right or ((14, -20), (17, -9))
    for side, (el, wr) in ((-1, left), (1, right)):
        sh = (cx + side * 8, by - 13)
        e = (cx + el[0], by + el[1])
        w = (cx + wr[0], by + wr[1])
        a.limb([sh, e, w], t=3, fill='L')
        a.rect(e[0] - 1, e[1] - 1, 3, 3, 'K')
        a.px(e[0], e[1], 'M')
        a.rect(w[0] - 2, w[1] + 1, 5, 1, 'K')     # gripper
        a.px(w[0] - 2, w[1] + 2, 'K')
        a.px(w[0] + 2, w[1] + 2, 'K')


def bench(a, x, by, w, legs=6):
    a.rect(x, by, w, 2, 'K')
    a.rect(x + 1, by + 2, 2, legs, 'K')
    a.rect(x + w - 3, by + 2, 2, legs, 'K')


def part(a, x, y):
    """The orange part, 5 x 3, bottom-left at (x, y)."""
    a.rect(x, y - 1, 5, 2, 'O')
    a.rect(x + 1, y - 2, 3, 1, 'O')
    a.px(x + 2, y - 1, 'd')


# ------------------------------------------------------------------ hero
def hero():
    W, H = 192, 104
    a = Art(W, H, 'W')
    B = 68                                        # bench top row

    # floor
    a.rect(0, 97, W, 7, 'P')
    a.rect(0, 96, W, 1, 'L')

    # pegboard with tools R-T-SAN can pick up
    a.box(18, 4, 56, 20, 'P', 'L')
    for y in range(7, 22, 3):
        for x in range(21, 72, 3):
            a.px(x, y, 'L')
    # gripper
    a.rect(26, 7, 1, 3, 'K'); a.rect(23, 10, 7, 2, 'K')
    a.rect(23, 12, 2, 6, 'K'); a.rect(28, 12, 2, 6, 'K')
    # end mill
    a.rect(35, 7, 4, 6, 'D'); a.rect(36, 13, 2, 2, 'K'); a.rect(36, 15, 1, 6, 'K'); a.px(37, 16, 'M'); a.px(37, 18, 'M')
    # soldering iron
    a.rect(44, 7, 3, 8, 'D'); a.rect(44, 9, 3, 1, 'M'); a.rect(45, 15, 1, 5, 'K'); a.px(45, 20, 'O')
    # saw disc
    a.disc(55, 13, 4, 'K'); a.disc(55, 13, 3, 'M'); a.px(55, 13, 'K')
    # screwdriver
    a.rect(63, 7, 3, 6, 'D'); a.rect(64, 13, 1, 8, 'K')
    # probe
    a.rect(69, 7, 2, 4, 'K'); a.rect(69, 11, 1, 7, 'M'); a.px(69, 18, 'K')

    # request screen
    a.box(152, 4, 32, 21, 'D')
    a.rect(154, 6, 28, 17, 'K')
    a.rect(159, 9, 18, 1, 'O'); a.rect(159, 19, 18, 1, 'O')
    a.rect(159, 9, 1, 11, 'O'); a.rect(176, 9, 1, 11, 'O')
    a.rect(165, 12, 6, 5, 'o'); a.rect(167, 13, 2, 3, 'K')
    a.px(156, 8, 'M'); a.px(156, 10, 'M'); a.px(156, 12, 'M')
    a.rect(167, 25, 2, 3, 'K')

    # workbench
    a.rect(12, B, 176, 4, 'K')
    a.rect(14, B + 4, 172, 3, 'D')
    a.rect(16, B + 7, 5, 21, 'K'); a.rect(183, B + 7, 5, 21, 'K')
    a.rect(21, B + 18, 162, 2, 'D')
    # material under the bench
    a.box(34, B + 9, 16, 9, 'L'); a.rect(36, B + 12, 12, 1, 'M')
    a.box(52, B + 11, 11, 7, 'M')
    for i, x in enumerate(range(120, 150, 4)):
        a.rect(x, B + 14 - (i % 2), 3, 4 + (i % 2), 'M' if i % 3 else 'L')
    a.rect(118, B + 16, 34, 2, 'K')

    # stock rack on the bench
    a.rect(18, B - 4, 26, 4, 'K'); a.rect(19, B - 3, 24, 2, 'D')
    tops = [44, 48, 46, 50, 45, 49, 47]
    for i, t in enumerate(tops):
        x = 20 + i * 3
        a.rect(x, t, 2, B - 4 - t, 'M' if i % 2 else 'L')
        a.px(x, t, 'K'); a.px(x + 1, t, 'K')
    a.rect(18, 54, 26, 1, 'K')

    # R-T-SAN
    cx = 92
    a.box(cx - 17, B - 5, 34, 5, 'D')             # base
    a.box(cx - 7, 40, 15, B - 45, 'L')            # torso
    a.rect(cx - 3, 45, 7, 2, 'O')
    for y in (51, 54, 57):
        a.rect(cx - 4, y, 9, 1, 'M')
    a.box(cx - 20, 35, 41, 6, 'D')                # shoulder beam
    a.rect(cx - 2, 31, 5, 4, 'K')                 # neck
    a.box(cx - 10, 17, 21, 14, 'L')               # head
    a.rect(cx - 8, 21, 17, 6, 'K')                # visor
    a.rect(cx - 5, 23, 3, 2, 'O'); a.rect(cx + 3, 23, 3, 2, 'O')
    a.rect(cx + 6, 12, 1, 5, 'K'); a.px(cx + 6, 11, 'O')

    # left arm: lifting a bar out of the rack
    sh, el, wr = (cx - 20, 38), (56, 29), (49, 43)
    a.rect(47, 40, 3, 22, 'O'); a.rect(47, 40, 3, 1, 'd')        # the bar
    a.limb([sh, el, wr], 5)
    a.joint(*sh, 3, 'M', 'K'); a.joint(*el, 3, 'M', 'K')
    a.box(44, 44, 9, 4, 'D')
    a.rect(44, 48, 2, 4, 'K'); a.rect(51, 48, 2, 4, 'K')

    # right arm: tool over the machining station
    sh, el, wr = (cx + 20, 38), (124, 27), (133, 41)
    a.limb([sh, el, wr], 5)
    a.joint(*sh, 3, 'M', 'K'); a.joint(*el, 3, 'M', 'K')
    a.box(129, 42, 9, 9, 'D'); a.rect(131, 44, 5, 1, 'M')
    a.rect(132, 51, 3, 2, 'K'); a.rect(133, 53, 1, 4, 'M')

    # machining station: vise holding the part
    a.box(120, B - 6, 28, 6, 'D')
    a.box(121, B - 12, 6, 7, 'M'); a.box(141, B - 12, 6, 7, 'M')
    a.rect(127, B - 13, 14, 7, 'O')
    a.rect(132, B - 13, 3, 2, 'W'); a.rect(133, B - 12, 1, 2, 'M')
    for (x, y) in ((126, 50), (124, 53), (139, 49), (142, 52), (137, 53), (128, 47)):
        a.px(x, y, 'o')

    # inspection camera
    a.rect(151, 32, 2, B - 32, 'K'); a.rect(151, 32, 12, 2, 'K')
    a.box(156, 34, 11, 7, 'D'); a.rect(160, 41, 3, 2, 'K'); a.px(165, 36, 'O')
    for i, y in enumerate(range(43, B - 3)):
        hw = 1 + i // 4
        a.rect(161 - hw, y, 2 * hw + 1, 1, 's')
    a.rect(154, B - 3, 15, 3, 'D')
    part(a, 159, B - 4)

    # output tray with the accepted part
    a.rect(172, B - 5, 1, 5, 'K'); a.rect(186, B - 5, 1, 5, 'K'); a.rect(172, B - 2, 15, 2, 'K')
    a.rect(175, B - 6, 9, 4, 'O'); a.rect(177, B - 8, 5, 2, 'O'); a.rect(178, B - 5, 3, 2, 'd')
    a.rect(179, B - 13, 1, 5, 'K')
    a.sprite(175, B - 21, CHECK_BADGE)

    # the container this all sits in, cut away: corrugated roof beam, corrugated posts, corner castings
    for x in range(W):
        a.px(x, 0, 'K'); a.px(x, 3, 'K')
        a.px(x, 1, 'D' if (x // 2) % 2 == 0 else 'M')
        a.px(x, 2, 'M' if (x // 2) % 2 == 0 else 'D')
    for x0 in (0, W - 4):
        for y in range(4, 96):
            a.px(x0, y, 'K'); a.px(x0 + 3, y, 'K')
            a.px(x0 + 1, y, 'D' if (y // 2) % 2 == 0 else 'M')
            a.px(x0 + 2, y, 'M' if (y // 2) % 2 == 0 else 'D')
    for x0 in (0, W - 6):
        a.box(x0, 0, 6, 6, 'O')
        a.box(x0, 98, 6, 6, 'O')
    return a


# ------------------------------------------------------------ town panel
def town():
    W, H = 92, 60
    a = Art(W, H, 'W')
    # hills
    for x in range(W):
        y0 = 31 + int(round(3 * math.sin(x / 10.0) + 2 * math.sin(x / 4.3 + 1)))
        a.rect(x, y0, 1, 46 - y0, 'P')
    # sun
    a.disc(79, 9, 5, 'O')
    # distant houses
    for (x, w) in ((58, 7), (67, 5), (74, 8), (84, 6)):
        a.rect(x, 36, w, 6, 'L'); a.rect(x - 1, 35, w + 2, 1, 'M'); a.px(x + 2, 38, 'M')
    # ground
    a.rect(0, 42, W, 18, 'L')
    a.rect(0, 42, W, 1, 'M')
    for (x, y) in ((4, 55), (20, 57), (57, 56), (66, 50), (88, 57), (75, 58), (52, 47), (90, 46)):
        a.rect(x, y, 2, 1, 'M')
    # open workshop
    a.rect(6, 17, 44, 35, 'W')                    # interior
    a.rect(6, 17, 2, 35, 'K'); a.rect(48, 17, 2, 35, 'K')
    a.rect(8, 17, 40, 1, 'P')
    a.rect(2, 12, 52, 5, 'D'); a.rect(2, 11, 52, 1, 'K'); a.rect(2, 16, 52, 1, 'K')
    for x in range(4, 53, 4):
        a.rect(x, 12, 1, 4, 'M')
    a.rect(6, 52, 44, 1, 'M')
    bench(a, 11, 45, 35, 6)
    artisan_small(a, 28, 45, left=((-13, -19), (-13, -8)), right=((14, -20), (15, -7)))
    for i, x in enumerate((12, 14, 16)):          # stock on the bench
        a.rect(x, 39 + i, 1, 6 - i, 'M')
    a.rect(14, 33, 2, 5, 'O')                     # bar in the left gripper
    part(a, 40, 44)
    # solar panel
    a.rect(62, 44, 1, 8, 'K')
    a.box(55, 38, 15, 7, 'D'); a.rect(59, 39, 1, 5, 'M'); a.rect(64, 39, 1, 5, 'M'); a.rect(56, 41, 13, 1, 'M')
    # crate of raw material
    a.box(72, 47, 9, 7, 'M'); a.rect(74, 44, 1, 3, 'K'); a.rect(77, 43, 1, 4, 'K'); a.rect(79, 45, 1, 2, 'K')
    # someone collecting a part
    a.rect(85, 40, 3, 3, 'D'); a.rect(84, 43, 5, 7, 'K'); a.rect(84, 50, 2, 5, 'K'); a.rect(87, 50, 2, 5, 'K')
    a.rect(82, 45, 2, 1, 'K'); a.rect(80, 44, 3, 2, 'O')
    return a


# ------------------------------------------------------------ dome panel
def dome():
    W, H = 92, 60
    a = Art(W, H, 'K')
    stars = [(5, 4), (14, 11), (22, 3), (31, 8), (47, 4), (58, 9), (66, 3), (85, 6), (89, 17), (3, 22),
             (9, 16), (79, 24), (71, 13), (38, 13), (87, 30), (2, 33)]
    for i, (x, y) in enumerate(stars):
        a.px(x, y, 'P' if i % 3 else 'M')
    a.px(31, 7, 'P'); a.px(31, 9, 'P'); a.px(30, 8, 'P'); a.px(32, 8, 'P')
    # a distant world
    a.disc(78, 10, 4, 'o'); a.rect(75, 11, 6, 1, 'O'); a.rect(76, 13, 4, 1, 'O')
    # ridge and ground
    for x in range(W):
        y0 = 43 + int(round(2 * math.sin(x / 6.0 + 1) + 1.5 * math.sin(x / 2.7)))
        a.rect(x, y0, 1, 50 - y0, 'd')
    a.rect(0, 50, W, 10, 'O')
    for (x, y, w) in ((4, 55, 9), (58, 57, 12), (80, 53, 7), (30, 58, 8)):
        a.rect(x, y, w, 1, 'd'); a.rect(x + 1, y + 1, w - 2, 1, 'o')
    # dome
    cxd, cyd, r = 38, 50, 29
    for y in range(cyd - r, cyd):
        hw = int(math.sqrt(r * r - (cyd - y) ** 2))
        a.rect(cxd - hw, y, 2 * hw + 1, 1, 'W')
        a.rect(cxd - hw, y, 2, 1, 'L'); a.rect(cxd + hw - 1, y, 2, 1, 'L')
    a.rect(cxd - 3, cyd - r, 7, 1, 'L')
    for y in range(cyd - r + 1, cyd):             # glazing bars
        hw = int(math.sqrt(r * r - (cyd - y) ** 2))
        if hw > 15:
            a.px(cxd - 15, y, 'P'); a.px(cxd + 15, y, 'P')
    a.rect(cxd - r - 1, cyd, 2 * r + 3, 3, 'K'); a.rect(cxd - r, cyd + 1, 2 * r + 1, 1, 'M')
    bench(a, 21, 45, 35, 3)
    artisan_small(a, 38, 45, left=((-13, -20), (-15, -9)), right=((13, -19), (13, -8)))
    a.rect(22, 43, 2, 2, 'd'); a.rect(24, 42, 3, 3, 'd'); a.px(25, 41, 'd')   # raw material
    a.rect(50, 34, 2, 4, 'O')                     # piece in the right gripper
    part(a, 49, 44)
    # airlock and mast
    a.box(71, 40, 13, 13, 'L'); a.rect(75, 44, 5, 9, 'D'); a.px(76, 48, 'O')
    a.rect(67, 45, 4, 5, 'M')
    a.rect(86, 30, 1, 23, 'L'); a.rect(84, 30, 5, 1, 'L'); a.px(86, 28, 'O')
    return a


# ----------------------------------------------------------- share panel
def share():
    W, H = 192, 58
    a = Art(W, H, 'W')
    xs = [22, 59, 96, 133, 170]
    by = 46
    poses = [
        (((-13, -19), (-13, -8)), ((14, -20), (15, -7))),
        (((-14, -20), (-15, -8)), ((13, -19), (12, -8))),
        (((-13, -20), (-12, -8)), ((13, -20), (12, -8))),
        (((-13, -19), (-12, -8)), ((14, -20), (15, -8))),
        (((-14, -20), (-15, -7)), ((13, -19), (13, -8))),
    ]
    learner = 2
    # the link between them
    for x in range(xs[0], xs[-1] + 1):
        if x % 2 == 0:
            a.px(x, 5, 'O')
    for i, cx in enumerate(xs):
        for y in range(5, 22):
            if y % 2 == 1:
                a.px(cx, y, 'O')
    for i, cx in enumerate(xs):
        ground = ['P', 'L', 'P', 'O', 'L'][i]
        a.rect(cx - 17, by + 8, 35, 2, ground)
        bench(a, cx - 15, by, 31, 6)
        l, r_ = poses[i]
        artisan_small(a, cx, by, left=l, right=r_)
        if i == learner:
            a.sprite(cx - 3, 9, CARTRIDGE)
            for (dx, dy) in ((-6, 9), (6, 9), (-7, 13), (7, 13), (-5, 17), (5, 17)):
                a.px(cx + dx, dy, 'O')
            part(a, cx + 9, by - 1)
        else:
            a.sprite(cx - 3, 9, CARTRIDGE_IN)
            # arrow head pointing down into the head
            a.px(cx - 1, 19, 'O'); a.px(cx + 1, 19, 'O'); a.px(cx, 20, 'O'); a.px(cx - 2, 18, 'O'); a.px(cx + 2, 18, 'O')
            part(a, cx + 9, by - 1)
    return a


def arm_icon():
    """One open arm, for the 'bought' layer."""
    a = Art(30, 24)
    a.box(3, 20, 14, 4, 'D')
    a.box(7, 10, 6, 10, 'L')
    a.limb([(10, 10), (18, 4), (25, 12)], 3, 'L')
    a.rect(9, 9, 3, 3, 'K'); a.px(10, 10, 'M')
    a.rect(17, 3, 3, 3, 'K'); a.px(18, 4, 'M')
    a.rect(23, 13, 5, 1, 'K'); a.rect(23, 14, 1, 3, 'K'); a.rect(27, 14, 1, 3, 'K')
    return a


def all_art():
    arts = {'hero': hero(), 'town': town(), 'dome': dome(), 'share': share(), 'arm': arm_icon()}
    for n in ICONS:
        arts['icon-' + n] = icon(n)
    for n in ('pick', 'hold', 'machine', 'finish', 'check'):
        arts['skill-' + n] = cartridge(n)
    return arts


if __name__ == '__main__':
    import os
    import sys
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'art')
    os.makedirs(out, exist_ok=True)
    for name, a in all_art().items():
        a.png(os.path.join(out, name + '.png'), 8 if a.w < 100 else 6)
        a.svg(os.path.join(out, name + '.svg'))
    print('wrote', len(all_art()), 'drawings to', out)
