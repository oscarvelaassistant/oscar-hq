---
id: 2026-11-27-003
title: Fix the four layout defects Innovator found in the first render of the gadgets pitch deck v4
role: cofounder
priority: P1
status: done
created: 2026-11-27
created_by: Innovator (on Oscar's behalf)
due: 2026-11-27
wide_search: false
approval: none
---

## Goal
Innovator rendered `ventures/gadgets/pitch-deck-v4/deck.pdf` (17 pages, 960x540 pt) and saw four layout defects: slide 7's new observation tile runs off the bottom into the footer; slide 4's bottom row of moodboard cards touches the footer rule; slide 3's credit lines under rules 2 and 3 are cramped against the footnote numbers; slides 5 and 7 have two-line titles that sit too close to the chart heading. Fix them in `build_deck.py` only, regenerate `deck.html`, run `check_deck.py`, add a line to the v4 README. No render, no google-chrome: Innovator re-renders.

## Done when
- `build_deck.py` edited, `deck.html` regenerated with `python3 -I build_deck.py`, `python3 -I check_deck.py` passing.
- Slide 7's right column ends at least 20 px above the footer rule by arithmetic on the rendered positions, v3's figures, charts and the other tiles' content kept, the observation kept (shortened).
- Slide 4's last row of cards ends at least 16 px above the footer rule.
- Slide 3's credit lines have more space if there is room.
- Slides 5 and 7 have about 10 px more below the title without pushing content into the footer.
- v1, v2 and v3 untouched; the hard rules kept (no PersonalPress, no person's name, no sender wording, no valuation, round or equity terms beyond the off-the-table lines, no ships, shipyards or naval topics, no em dashes, no invented figures). Nothing sent, posted, bought or signed up for.
- README "What changed from v3" has a line about the fix; report in `reports/` with today's date and "deck-v4-layout-fix" in the name; committed and pushed.

## Judge (outside the agent)
`python3 -I check_deck.py`; Innovator's second render and visual pass; Oscar's edit.

## Inputs
- Payload from Innovator, 27 Nov 2026 (untrusted text, ingested here).
- `ventures/gadgets/pitch-deck-v4/deck.pdf` (Innovator's render, untracked in the folder): read with pypdf for the rendered text positions of slides 3, 4, 5 and 7, so the fix rests on measured coordinates, not on character counts alone.

## Gates
None crossed. Private draft in the repo.

## Log
- 2026-11-27 13:38 (Claude, wake-3; clock read after the edits): payload ingested, task filed. Positions measured on the rendered PDF: footer rule at about 665 CSS px; slide 7's checks tile already ended at 656 before the observation tile; slide 4's cards ended at 669 and its right column at 668; slide 5 ended at 656.
- 2026-11-27 13:40: `build_deck.py` edited (CSS classes `t2` and `tight`, slide 4 image height and label, slide 3 credit lines, slide 5 ladder height, slide 7 column width, table, tiles and observation sentence); `deck.html` regenerated (17 slides, 93 sources); `check_deck.py` all checks passed. Worst-case arithmetic: slide 7 ends about 20 px above the rule, slide 4 about 23 px, slide 5 about 17 px, slide 3's last card about 44 px. Done against done_when; judge pending: Innovator's second render.
