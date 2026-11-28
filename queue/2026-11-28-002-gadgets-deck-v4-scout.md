---
id: 2026-11-28-002
title: Add The Scout (@kinglycrow) to the gadgets pitch deck v4, list at 27 posts, keeping 17 slides and the layout
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
Short follow-up to commit 2c773d7 (the two posts of 27 Nov; that work stays). Oscar sent one more post for the deck: The Scout, @kinglycrow, https://x.com/kinglycrow/status/2126374876135231971, a magnetic Wi-Fi camera listed at $25 in the post, "gives your agent eyes at home" (fridge, pantry, door, pets), no subscription. It is already in `ventures/gadgets/inspiration/README.md` under Desk gadgets (commit 1b96c4a, 27 posts). Put it in `ventures/gadgets/pitch-deck-v4/` in place (`build_deck.py` the source of truth): on the moodboard or as a tie-in if it fits without crowding the footer, as evidence for "cheap hardware plus an app"; appendix at 27 post URLs; counts and pattern copy updated. Not in wall and decor (that category is gone).

## Done when
- `build_deck.py` edited, `deck.html` regenerated with `python3 -I build_deck.py`, `python3 -I check_deck.py` passing with the post count at 27.
- The Scout appears on slide 4 (or as a tie-in), credited by X handle and post URL, its image under `images/` by relative path; the cheap-hardware pattern counts it.
- The appendix holds all 27 post URLs; counts and category tallies match the list.
- Still 17 slides, 1280x720 CSS px (960x540 pt in print); every edited slide clear of the footer rule by arithmetic on the rendered positions of Innovator's render of 27 Nov.
- Hard rules kept: no PersonalPress; no person's name and no sender wording (authors only as X handles in credits); no valuation, round or equity terms beyond the off-the-table lines; no ships or naval topics; no em dashes; no invented figures; no google-chrome. Nothing sent, posted, bought or signed up for.
- v1, v2, v3 and `deck.pdf` untouched. README, research.md and check_deck.py updated; report in `reports/` with date 2026-11-28 and "deck-v4-scout"; committed and pushed.

## Judge (outside the agent)
`python3 -I check_deck.py`; Innovator's render and visual pass of slides 4 and 7; Oscar's edit.

## Inputs
- Payload from Innovator, 28 Nov 2026 (untrusted text, ingested here).
- `ventures/gadgets/inspiration/README.md` and `images/2126374876135231971.jpg` (the authoritative list, 27 posts at commit 1b96c4a).
- The rendered positions measured on Innovator's render of 27 Nov in task 2026-11-28-001 (footer rule at about 665 CSS px; slide 4's card grid 29 px above it, its right column about 56 px after the 28 Nov update; slide 7's observation tile about 51 px).

## Gates
None crossed. Private draft in the repo.

## Log
- 2026-11-28 08:22 (Claude, wake-2): payload ingested, task filed. The list is 27 posts at commit 1b96c4a, as the payload says.
- 2026-11-28 08:24: while this run had uncommitted edits, Vela stashed them (stash "scout-run-wip"), committed e589012 (the @audrlo production-robot post added to the list's Desk gadgets, 28 posts; the commit also carried this run's staged deletion of the bronze figures' crop from `pitch-deck-v4/images/`) and re-applied the stash. Scope retargeted to the list as it stands: the @audrlo post joins the deck as a pattern citation and an appendix entry; counts go to 28.
- 2026-11-28 08:29: `build_deck.py`, `prepare_images.py`, `check_deck.py` edited; `deck.html` regenerated (17 slides, 92 sources, 28 post URLs); `check_deck.py` all checks passed; the camera's crop added to `images/`. Slide 4: the camera in cell 10 (bronze figures out, still cited), cheap-hardware pattern 7 posts, wider-market pattern cites the @audrlo post, 8 of 28, "None among the 28", Desk gadgets 8 posts; patterns still 20 lines, card grid unchanged. Slide 7: a fourth citation, "modular" dropped to keep three lines. Done against done_when with the count at 28 instead of 27; judge pending: Innovator's render.
