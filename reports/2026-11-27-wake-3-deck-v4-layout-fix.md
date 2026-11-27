# HQ report 2026-11-27 wake-3

Extra run started by Innovator on Oscar's behalf (the layout defects in the first render of the gadgets pitch deck v4). Local run on the box, no HUB connector: HUB steps skipped, Vela saves this report. No decision raised; `state.next_decision` stays 19. Third wake run of the day; the filename carries "deck-v4-layout-fix" as the payload asked.

## Done since last report
- 2026-11-27-003 Gadgets pitch deck v4, layout fix in `ventures/gadgets/pitch-deck-v4/build_deck.py` only; `deck.html` regenerated, `check_deck.py` passes. Instead of estimating text widths from character counts, the run read the text positions of Innovator's `deck.pdf` with pypdf (slides 3, 4, 5, 7): the footer rule sits at about 665 CSS px, slide 7's column already ended at 656 before the observation tile, slide 4's bottom cards at 669, slide 5 at 656.
- Slide 7 (funnel): the funnel canvas is 740 px wide instead of 790 (its content reached 714 px; nothing in the chart moved), so the right column gains 54 px; the table keeps region names on one line, 2 px cell padding, 10 px font; the paragraph is 10.5 px; the three tiles have 6 px padding and 11 px text; the observation is one sentence, "Two readings from saved posts (slide 4): a wider market than tech people; cheap hardware plus an app sells.", still citing the two posts. Worst case (no line gained from the wider column), the column ends about 20 px above the rule. v3's figures, table and the beachhead and checks tiles keep their content.
- Slide 4 (inspiration): images 92 px tall instead of 100 (4 px cropped top and bottom), credit padding 4 px, the patterns label shortened to one line less (the save dates moved to the footer), list items 3 px apart. The card row ends about 23 px above the rule; the right column, which also touched the rule, ends about 22 px above it.
- Slide 3 (brand): credit lines under the rules get 5 px of space, line height 1.4, and break before the URL instead of inside the post id. The last card ends about 44 px above the rule.
- Slides 5 and 7: the body starts 10 px lower (class `t2`) because their titles wrap to two lines; slide 5 pays with a 176 px price ladder (was 192) and a 6 px gap, ending about 17 px above the rule; the ladder's label solver still finds a collision-free placement.
- Hard rules scanned by `check_deck.py` and by eye: no PersonalPress, no person's name, no sender wording, valuation, round and equity only in the off-the-table lines, no ships, shipyards or naval topics, no em dashes, no new figure. v1, v2 and v3 untouched (`git status`). Nothing sent, posted, bought or signed up for; no google-chrome, no render.
- README "What changed from v3": change 11 describes the fix; change 7 and the checks paragraph now say two v3 canvases are smaller and that a second render is the check.

## Blocked
- None. Innovator's second render is the judge; the command is unchanged in the v4 README.

## Spend
- API: 0.00 EUR this month (ceiling 50). Subscriptions: no change.

## Proposals
- Slides 6, 8 and 9 also have two-line titles with the same tight gap to their chart headings; not in the defect list, so unchanged. One line each in `build_deck.py` (class `t2`) after a look at their bottoms in the next render. Cost: minutes.
- A run cannot read a PDF with the pdfcraft tools or `pdftotext` (both need an approval it cannot give); pypdf in the user site works with an explicit `sys.path` line. If renders keep coming back as PDFs, a small `measure_pdf.py` next to `check_deck.py` would make the position check repeatable. Cost: an hour.

## Next step
- Innovator renders `deck.pdf` again and looks at slides 3, 4, 5 and 7. If a column still touches the footer, the next fix is the same lever: the measured positions, then `build_deck.py`.
