# Gadgets pitch deck v2

Draft for Oscar's edit, rebuilt on 27 Nov 2026 after Oscar's correction: the flagship is the concept itself, one premium brand with a multi-category collection of decorations, gadgets and other objects for the home. PersonalPress and the personal digest are not in the collection and not in the deck (named here only to say so). Gadgets is Oscar's solo project, so no slide names anyone else. No valuation, round size or equity. Private. Nothing here has been sent, shared or made public.

Files:
- `research.md`: every figure with URL, date and a tag (verified, snippet only, my arithmetic, assumption, opinion, placeholder). Sections 1 (market), 2 (competition) and 3 (business model) are new for v2; sections 4 and 5 add to v1's. Section 6 lists placeholders, invented items and snippet-only figures worth opening before the coffee.
- `deck.html`: 13 slides at 1280x720, self-contained (system fonts, inline SVG charts, flat placeholder renders). Slides 1 to 9 are the pitch, 10 to 13 the numbered sources with URLs.
- `build_deck.py`: generates `deck.html`. All copy, numbers, chart data and the source registry (`register_sources`) live in this file. Footnote numbers are generated in order of first use; a star marks a source seen in a search snippet only. Regenerate with `python3 -I build_deck.py` from this folder.
- `deck.pdf`: see the status line below.

Slides: 1 cover; 2 problem and why now; 3 the brand (house diagram, customer loop, three draft brand rules); 4 the collection (nine objects in three families, placeholder renders and prices, ladder of comparable list prices); 5 market (top-down ladder and bottom-up funnel); 6 competition (map, table, the gap); 7 business model (flow, unit structure and margin benchmarks, direct versus wholesale, evidence); 8 plan; 9 founder and ask; 10 to 13 sources.

To render the PDF on the box, from `~/oscar-hq`:

```
google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=ventures/gadgets/pitch-deck-v2/deck.pdf --virtual-time-budget=4000 file:///home/box/oscar-hq/ventures/gadgets/pitch-deck-v2/deck.html
```

Checks run without a browser: every SVG parses; no chart label runs outside its SVG or overlaps another label (estimated from character widths); no em dashes; no mention of PersonalPress, Fionn, ARESA, shipyards or naval topics in deck.html; valuation, round size and equity appear only in the two lines saying they are off the table. A visual check of the rendered pages is still to do.

Placeholders (marked `[placeholder]`): brand name, object renders (flat drawings stand in), prices per object (due Sat 28 Nov), unit cost and MOQ, founder surname, photo, education and languages, team plan. Dates after December on the plan slide are proposals.

Invented for the deck and flagged on the slides: two decor objects (the other seven come from the 26 Nov catalogue decision), three brand rules, the plan rows after December, and three assumptions in the bottom-up funnel (10% premium share, 1% to 3% capture, EUR 120 a year per customer).

Style: any style for now, Oscar restyles later. Current choices: warm paper background, one accent (lacquer red), serif headings, system sans body, hairline grid, flat object drawings in wood tones.
