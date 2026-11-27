# Gadgets pitch deck v1

Draft for Oscar's edit, written by the HQ wake run of 27 Nov 2026 (task 2026-11-27-001). Private. Nothing here has been sent or shown to anyone.

Files:
- `research.md`: every figure used in the deck with URL, date and a tag (verified, snippet only, my arithmetic, opinion, placeholder). Read this before the coffee; section 6 lists the placeholders and the snippet-only figures worth opening.
- `deck.html`: the ten slides (Oscar's nine plus a sources appendix), 1280x720, self-contained (system fonts, inline SVG charts). Opens in any browser; prints to PDF from the browser's print dialog at the page size set in the file.
- `build_deck.py`: generates `deck.html`. All copy, numbers and chart data live in this file. Regenerate with `python3 -I build_deck.py` from this folder. Editing `deck.html` directly also works, until the next regeneration overwrites it.
- `deck.pdf`: not produced by the run (headless Chrome needs an approval the run cannot give). To produce it on the box, from `~/oscar-hq`:

```
google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=ventures/gadgets/pitch-deck-v1/deck.pdf --virtual-time-budget=4000 file:///home/box/oscar-hq/ventures/gadgets/pitch-deck-v1/deck.html
```

Placeholders in the deck (marked `[placeholder]`): brand name, catalogue renders and target prices (due Sat 28 Nov), hero panel size and target price, hero unit cost and MOQ, founder surname, photo, education and languages, team plan. Dates after December 2026 on the plan slide are proposals.

Style: any style for now, Oscar redoes it later. Current choices: warm paper background, one accent (lacquer red, after the wood and lacquer lead), serif headings, system sans body, hairline grid.
