# R-T-SAN: illustrated 3-pager

Task 2026-11-17-004. Concept document for Oscar's Powerhouse application. Design only: nothing sent.

| File | What it is |
|---|---|
| `pocket-factory-3pager.pdf` | The document. A4, 3 pages. Page 1 what it is, page 2 how it works, page 3 where it goes and the ten weeks. |
| `build.py` | Source of the layout and all the copy. Writes the PDF, `art/` and `preview/`. |
| `art.py` | Source of every drawing, as pixel grids drawn in code. No stock images, no generated images. |
| `art/` | Each drawing as PNG and SVG: hero, town, dome, share, arm, seven loop icons, five skill cartridges. |
| `preview/page-N.png` | The exact page images inside the PDF, for checking by eye. |

Rebuild: `python3 ventures/pocket-factory/illustrated/build.py` (needs Pillow and fontTools; fonts IBM Plex Serif, IBM Plex Mono and Press Start 2P, all SIL Open Font License, read from the path in `FONT_DIR`).

How the PDF is made: each page is a 336 dpi image with an invisible text layer on top, so the text can be selected and searched and the two source links can be clicked. The source is Python, not HTML: the run that made it could not start Chrome (blocked by `.claude/settings.json`), so nothing depends on a browser.

Sources on the pages:
- [1] Seeed reBot-DevArm, open hardware under CERN-OHL-W 2.0, "effective May 11, 2026": https://github.com/Seeed-Projects/reBot-DevArm
- [2] Powerhouse Residency: https://powerhouse.engineering/residency
- Payload and reach on page 2 are checked against the Seeed reBot-DevArm README "Hardware Specifications" table [1]: B601-DM 1.5 kg payload and 767 mm max reach, B601-RS 2.5 kg and 754 mm (checked 17 Nov 2026). The earlier "about 760 mm" figure was unverified and is gone.
- Text matches Oscar's final Powerhouse intro video (transcript: /workspace/video/intro-transcript.md, 17 Nov 2026): a container dropped anywhere, two robot arms, a panoply of tools, 24/7, a team of highly skilled artisans, unlike today's specialized robots, not an engineer, Shenzhen.
- The pull quote line carries no attribution.
