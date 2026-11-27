# Gadgets pitch deck v3

Draft for Oscar's edit, built on 27 Nov 2026 from v2 (`../pitch-deck-v2/`, untouched). The flagship is the concept itself: one premium brand with a multi-category collection of decorations, gadgets and other objects for the home. PersonalPress and the personal digest are not in the collection and not in the deck (named here only to say so). Gadgets is Oscar's solo project, so no slide names anyone else. No valuation, round size or equity. Private. Nothing here has been sent, shared or made public.

## What changed from v2

Oscar's ask: "in the market, get claude to research for the whole world, give me a market size by region overall, then break up the total market like you did in the bottom up".

1. **Slide 5, market by region (new, replaces half of the v2 market slide).** Bar chart of the world market by region (North America, Europe, Asia-Pacific, Latin America, Middle East and Africa; China and Japan split out from Asia-Pacific). Each region shows the reported decor market including furniture (GMI, 2025) with a range whisker to Fortune Business Insights, and the brand's scope: decor without furniture plus adjacent gadgets. World brand scope: about US$315bn. A table shows how four publishers split the world differently, and the range for decor without furniture (US$134bn to 441bn).
2. **Slide 6, market funnel (new, replaces the other half).** Households, online buyers, buyers of home items online, premium buyers, customers and revenue, for the world and for Spain, France and Germany (the v2 bottom-up, now the beachhead inside the funnel). Every narrowing step is labelled SOURCED or ASSUMPTION on the slide. A regional table runs the same funnel in dollars. The world customer figure is a ceiling, not a plan.
3. **Layout fixes.** Slide 4: the price-ladder labels are now placed by a search that rejects overlaps and leader lines through labels (the build fails if no clean placement exists). Slide 7 (competition): the map caption no longer collides with the axis labels (the plot reserves room for the caption). Slide 2: the token-cost chart caption has a clear gap below the tick labels. Slide 8 (business model): a leader line in the gross-margin strip crossed the Williams-Sonoma label; fixed the same way as the ladder.
4. **Sources appendix** is now slides 11 to 14, 64 numbered sources. The v2 spend-per-household tiles (INE, Destatis, BLS) are off the slides and stay in `research.md` 1.4.
5. Cover, footers, plan row and file headers say v3.

## Files

- `research.md`: every figure with URL, date and a tag (verified, snippet only, my arithmetic, assumption, opinion, placeholder). Sections 1 to 6 are v2's (slide numbers updated). **Section 7 is new**: regional inputs from five publishers, the scope arithmetic by region, the worldwide funnel with each step's label, FX, checks, what was not found.
- `deck.html`: 14 slides at 1280x720, self-contained (system fonts, inline SVG charts, flat placeholder renders). Slides 1 to 10 are the pitch, 11 to 14 the numbered sources.
- `build_deck.py`: generates `deck.html`. All copy, numbers, chart data and the source registry live here. The block "v3 market data" holds every input and formula behind slides 5 and 6. Footnote numbers are generated in order of first use; a star marks an unverified source (search snippet only, or a secondary page whose source could not be opened). Regenerate with `python3 -I build_deck.py` from this folder.
- `check_deck.py`: the no-browser checks (below). Run with `python3 -I check_deck.py` from this folder.
- `deck.pdf`: not yet. Vela renders it (command below).

Slides: 1 cover; 2 problem and why now; 3 the brand; 4 the collection (nine objects, price ladder); 5 market by region; 6 market funnel; 7 competition; 8 business model; 9 plan; 10 founder and ask; 11 to 14 sources.

## Render the PDF

On the box, from `~/oscar-hq`:

```
google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=ventures/gadgets/pitch-deck-v3/deck.pdf --virtual-time-budget=4000 file:///home/box/oscar-hq/ventures/gadgets/pitch-deck-v3/deck.html
```

## Checks run without a browser

`python3 -I check_deck.py`: every SVG parses; no chart label runs outside its SVG, overlaps another label, or sits on a solid bar (widths estimated from character counts: 0.54 em regular, 0.58 em bold or serif); no short vertical leader line crosses a label; no em dash; no mention of PersonalPress, Fionn, ARESA, shipyards or naval topics; valuation, round size and equity appear only in the lines saying they are off the table. All passed on the last build. Not covered: text overflow in the HTML blocks (tiles, tables, footers) and the real rendered widths. **A visual check of the rendered PDF is still to do**, especially slide 5 (right column height), slide 6 (funnel sub-labels and right column) and the sources pages (pagination is estimated).

## Placeholders and assumptions

Placeholders (marked `[placeholder]`): brand name, object renders, prices per object (due Sat 28 Nov), unit cost and MOQ, founder surname, photo, education and languages, team plan. Dates after December on the plan slide are proposals.

Invented for the deck and flagged on the slides: two decor objects, three brand rules, the plan rows after December; the funnel's 10% premium share, 1% to 3% capture and EUR 120 a year per customer; and in v3 the regional assumptions: GMI's 42.5% non-furniture share, 41.5% online share and 29.2% premium share applied to every region, the gadget regional splits, and the 19% EU home-item rate applied to the world.

Unverified (starred): Statista's narrow US$133.6bn segment, DataReportal's 56.2% weekly online buyers, the 2.2 billion world households (secondary page citing UN DESA; the UN file could not be fetched), and v2's snippet-only items.

Style: any style for now, Oscar restyles later. Warm paper background, one accent (lacquer red), serif headings, system sans body, hairline grid, flat object drawings in wood tones.
