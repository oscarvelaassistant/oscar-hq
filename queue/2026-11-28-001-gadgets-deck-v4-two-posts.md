---
id: 2026-11-28-001
title: Add the two posts Oscar sent on 27 Nov to the gadgets pitch deck v4, keeping 17 slides and the layout
role: cofounder
priority: P1
status: done
created: 2026-11-28
created_by: Innovator (on Oscar's behalf)
due: 2026-11-28
wide_search: false
approval: none
---

## Goal
Oscar sent two posts on the evening of 27 Nov (the large e-ink tablet read in a cafe, @huntie; the ESP-Mosaico ESP32-S31 modular AMOLED board, @ahm3dhub). They are already in `ventures/gadgets/inspiration/README.md` (commit 7876f9a, Displays and e-ink). Put them in the pitch deck v4 (`ventures/gadgets/pitch-deck-v4/`, `build_deck.py` as the source of truth): on the moodboard if they fit without crowding the footer, or as evidence tie-ins on the brand, collection or market slides; all post URLs in the appendix; counts, tallies and pattern copy updated, patterns labelled observation. No new slide, same page size, the 27 Nov layout fix kept. Innovator renders `deck.pdf` afterwards.

## Done when
- `build_deck.py` edited, `deck.html` regenerated with `python3 -I build_deck.py`, `python3 -I check_deck.py` passing with the post-count check raised to the list's count.
- The two posts appear on slide 4 (or as tie-ins), credited by X handle and post URL, images copied into `images/` by relative path.
- The appendix holds every post URL on the inspiration list; counts and category tallies match the list.
- Every edited slide stays at least 16 px clear of the footer rule by arithmetic on the rendered positions of Innovator's last render; slide count 17; 960x540 pt page.
- Hard rules kept: the flagship is the brand concept, no single hero product; no PersonalPress; no person's name and no sender wording; no valuation, round size or equity beyond the off-the-table lines; no ships, shipyards or naval topics; no em dashes; no invented figures. Nothing sent, posted, bought or signed up for; no google-chrome, no render.
- v1, v2 and v3 untouched; `deck.pdf` not copied or overwritten. README, research.md and check_deck.py updated; report in `reports/` with today's date and "deck-v4-two-posts"; committed and pushed.

## Judge (outside the agent)
`python3 -I check_deck.py`; Innovator's render and visual pass of slides 4, 5 and 7; Oscar's edit.

## Inputs
- Payload from Innovator, 28 Nov 2026 (untrusted text, ingested here).
- `ventures/gadgets/inspiration/README.md` and `images/` (the authoritative list). At 08:03 Madrid, during this run, Vela removed the five Wall and decor posts from it at Oscar's request (commits c653f43 and 84ec477): the list is 26 posts, not the 31 the payload named.
- `ventures/gadgets/pitch-deck-v4/deck.pdf` (Innovator's render of 27 Nov, commit 02c6a67), read with pypdf for the rendered text positions of slides 3, 4, 5 and 7.

## Gates
None crossed. Private draft in the repo.

## Log
- 2026-11-28 07:57 (Claude, wake): payload ingested, task filed. Positions measured on Innovator's render: footer rule at about 665 CSS px; slide 4's card grid ended 29 px above it and its right column 21 px; slide 5 19 px; slide 7's observation tile 65 px; slide 3's last card 44 px.
- 2026-11-28 08:03: Vela's two commits landed in this working tree (Wall and decor posts removed, list at 26). Scope retargeted to the list as it stands: the five posts, their images and their category leave the deck too.
- 2026-11-28 08:09: `build_deck.py`, `prepare_images.py`, `check_deck.py` edited; `deck.html` regenerated (17 slides, 90 sources, 26 post URLs); `check_deck.py` all checks passed; two crops added to `images/`, two removed (`git rm`). Slide 4: moodboard cells 4 and 8 are the new posts, the water gun moved to cell 11; patterns 20 lines (21 before), count chart six rows. Slide 5: "saved posts" on the e-ink display. Slide 7: a third reading and citation. Worst-case arithmetic: slide 4's right column ends about 56 px above the rule, its cards 29 px, slide 5 about 19 px, slide 7 about 51 px. Done against done_when; judge pending: Innovator's render.
