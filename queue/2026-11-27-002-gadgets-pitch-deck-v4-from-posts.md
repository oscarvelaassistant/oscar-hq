---
id: 2026-11-27-002
title: Build v4 of the gadgets pitch deck from v3 with the saved X posts as inspiration evidence
role: cofounder
priority: P1
status: done
created: 2026-11-27
created_by: Oscar
due: 2026-11-27
wide_search: false
approval: none
---

## Goal
A v4 of the gadgets pitch deck that uses the 29 saved X posts in `ventures/gadgets/inspiration/` as evidence of the product direction and the founder's taste: a moodboard slide with captions, categories and credits, tie-ins on the brand, collection, market and competition slides where a post supports a claim, and every post URL in the sources appendix. v3 stays untouched; v4 is a copy edited through `build_deck.py`. The deck keeps the brand concept as the flagship, a solo founder, no valuation, round or equity, and every pattern labelled as an observation, never a market measurement.

## Done when
- `ventures/gadgets/pitch-deck-v4/` exists with `build_deck.py`, `deck.html` (regenerated with `python3 -I build_deck.py`), `check_deck.py` (passing), `research.md`, `README.md` and `images/` (the chosen post images, relative paths, so `file://` rendering works). No `deck.pdf` copied from v3; the README says Innovator renders it.
- The deck has an inspiration slide (moodboard of saved-post images with one-line captions, categories and a credit line per image: X handle and post URL) and tie-ins on the brand, collection, market and competition slides; every post URL is in the sources appendix; every pattern is labelled as an observation.
- `pitch-deck-v1`, `v2` and `v3` are unchanged (`git status` shows no change under them).
- Hard rules kept in every v4 file: brand concept as flagship, no single hero product; no PersonalPress; no Fionn and no other person's name (post authors only as X handles in credit lines; no "sent by" or "shared by"); no valuation, round size or equity beyond the off-the-table lines; no ships, shipyards or naval topics; no em dashes; no unlabelled estimate or invented figure; nothing sent, posted, bought or signed up for; no PDF render and no google-chrome.
- Every slide readable at the v3 page size (CSS 1280x720 px, which prints to 960x540 pt as v3's PDF).
- `README.md` in v4 states every change under "What changed from v3".
- Committed and pushed; report in `reports/` with today's date and "deck-from-posts" in the filename.

## Judge (outside the agent)
`python3 -I check_deck.py` in v4 (SVG parse, label collisions, banned words, em dashes, image paths). Innovator's PDF render and visual pass. Oscar's edit. The angel's questions at the coffee.

## Inputs
- Payload from Oscar via Innovator, 27 Nov 2026 12:36 Madrid (untrusted text, ingested here; the task is Oscar's).
- `ventures/gadgets/inspiration/README.md` and `images/` (29 posts, categories, the founder's comments, the patterns section).
- `ventures/gadgets/pitch-deck-v3/` (read only): `build_deck.py`, `check_deck.py`, `research.md`, `README.md`, `deck.pdf` page size.
- `playbooks/design.md`.

## Gates
None crossed. The deck is a private draft in the repo. No message, spend, signup or publication.

## Log
- 2026-11-27 12:37 (Claude, wake-2): payload ingested, task filed. Queue was empty. v3 read in full (build script, checks, research, README), the 29 inspiration images looked at one by one.
- 2026-11-27 12:45 (Claude, wake-2): v3 copied to v4 without deck.pdf (v3's PDF page box read: 960x540 pt, so the 1280x720 px CSS page stays). Twelve images cropped and resized by `prepare_images.py`; `build_deck.py` patched by a script of exact-match replacements (30, each asserted to hit once): new slide 4, tie-ins on slides 3, 5, 7 and 8, slides renumbered, 29 posts registered as sources with dates decoded from the post ids.
- 2026-11-27 12:55 (Claude, wake-2): `deck.html` regenerated (17 slides, 93 sources); `check_deck.py` extended (image paths, page size, slide count, names and sender wording, 29 URLs) and passing; crops looked at as images; `research.md` section 8 and v4 slide numbers; `README.md` rewritten with "What changed from v3" and the render command for Innovator.
- 2026-11-27 13:00 (Claude, wake-2): every v4 file scanned for the banned words, names, sender wording and em dashes. Done against done_when; the PDF is Innovator's step by design. Judge pending: Innovator's render and visual pass, Oscar's edit, the angel's questions.

## Decision
None raised. No gate crossed.
