#!/usr/bin/env python3
"""Copies the saved-post images the deck uses into ./images/, cropped to the moodboard cell and resized.

Run once from this folder: python3 -I prepare_images.py
Source: ../inspiration/images/<post id>.jpg (the inspiration list is ../inspiration/README.md).
Output: images/<post id>.jpg, 384x200 px (the 192x100 cell at 2x), JPEG quality 86.
Each crop is a horizontal band of the source image at the ratio of the cell; AY says where the band sits
(0 = top of the source, 0.5 = middle, 1 = bottom) so that the object stays in frame. Nothing else is changed.
The images belong to their authors; they are here as private reference, not for publication.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "inspiration", "images"))
OUT = os.path.join(HERE, "images")
CELL_W, CELL_H, SCALE = 192, 100, 2
RATIO = CELL_W / CELL_H

# post id: vertical anchor of the band (AY). The 12 featured posts of slide 4 (three of them reused on slide 3).
CROPS = {
    "2125588103276720393": 0.45,   # @modem_works, bookcase
    "2125257053341966427": 0.50,   # @inanimate_tech, five promptable devices
    "2125609297895903294": 0.50,   # @hturan, e-ink simulation (portrait)
    "2113274039297028534": 0.13,   # @luusssso, transparent cassette player (portrait, upper device)
    "2123010578616659969": 0.35,   # @SciFiArchives, headphone concept (portrait)
    "2125946257852285039": 0.40,   # @andreintg, open-frame PC case (portrait)
    "2123854155856880066": 0.45,   # @pmamtraveller, ceramic ashtray
    "2125649169138528553": 0.40,   # @kieranklaassen, thermal-printer slips (portrait)
    "2117773168807166443": 0.50,   # @RaemondBW, AirPlay board (portrait)
    "2121458552803914203": 0.42,   # @MaxLobovsky, resin water gun in the printer (portrait)
    "2122938259906994637": 0.40,   # @pmamtraveller, bronze figures
    "2111851254091776122": 0.35,   # @_GVNTHER_, red and white illustration (portrait)
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for pid, ay in CROPS.items():
        im = Image.open(os.path.join(SRC, pid + ".jpg")).convert("RGB")
        w, h = im.size
        if w / h >= RATIO:          # wider than the cell: full height, centred horizontally
            bh = h
            bw = int(round(h * RATIO))
            x0 = (w - bw) // 2
            y0 = 0
        else:                       # taller than the cell: full width, band placed by AY
            bw = w
            bh = int(round(w / RATIO))
            x0 = 0
            y0 = int(round((h - bh) * ay))
        band = im.crop((x0, y0, x0 + bw, y0 + bh)).resize((CELL_W * SCALE, CELL_H * SCALE), Image.LANCZOS)
        band.save(os.path.join(OUT, pid + ".jpg"), "JPEG", quality=86, optimize=True)
        print(f"{pid}: {w}x{h} -> band {bw}x{bh} at ({x0},{y0}) -> {CELL_W*SCALE}x{CELL_H*SCALE}")


if __name__ == "__main__":
    main()
