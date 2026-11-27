# Gadgets pitch deck v1

Draft for Oscar's edit, written by the HQ wake run of 27 Nov 2026 (task 2026-11-27-001). Private. Nothing here has been sent or shown to anyone.

Files:
- `research.md`: every figure used in the deck with URL, date and a tag (verified, snippet only, my arithmetic, opinion, placeholder). Read this before the coffee; section 6 lists the placeholders and the snippet-only figures worth opening.
- `deck.html`: the ten slides (Oscar's nine plus a sources appendix), 1280x720, self-contained (system fonts, inline SVG charts). Opens in any browser; prints to PDF from the browser's print dialog at the page size set in the file.
- `build_deck.py`: generates `deck.html`. All copy, numbers and chart data live in this file. Regenerate with `python3 -I build_deck.py` from this folder. Editing `deck.html` directly also works, until the next regeneration overwrites it.
- `deck.pdf`: ten pages at 1280x720 px, rendered by the morning run of 27 Nov 2026 with the cloud run's Chromium (Playwright `page.pdf`). Regenerate after editing: in a cloud run, any Chromium works; on the box, from `~/oscar-hq`:

```
google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=ventures/gadgets/pitch-deck-v1/deck.pdf --virtual-time-budget=4000 file:///home/box/oscar-hq/ventures/gadgets/pitch-deck-v1/deck.html
```

Layout fixes of 27 Nov morning (seen on screenshots of every slide): the comparables ladder on slide 5 now scales to its largest bar (v1 scaled to the smallest, so five of six bars overflowed); funnel and Gantt label columns widened; chart notes wrap; the unit-economics bar on slide 7 carries its labels in a legend below the bar and the margin benchmarks are staggered; the competition table fits its column; the hero tiles and the "Also in place" box no longer overflow; axis labels on the competition map read upward.

Placeholders in the deck (marked `[placeholder]`): brand name, catalogue renders and target prices (due Sat 28 Nov), hero panel size and target price, hero unit cost and MOQ, founder surname, photo, education and languages, team plan. Dates after December 2026 on the plan slide are proposals.

Style: any style for now, Oscar redoes it later. Current choices: warm paper background, one accent (lacquer red, after the wood and lacquer lead), serif headings, system sans body, hairline grid.
