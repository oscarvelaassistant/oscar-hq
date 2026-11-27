# HQ report 2026-11-27 wake-2

Extra run started by Innovator at 12:36 Madrid with Oscar's payload (the gadgets pitch deck v4 built from the saved X posts). Local run on the box, no HUB connector: HUB steps skipped, Vela saves this report. No decision raised; `state.next_decision` stays 19. The filename carries "deck-from-posts" as the payload asked; this is the second wake run of the day.

## Done since last report
- 2026-11-27-002 Gadgets pitch deck v4, in `ventures/gadgets/pitch-deck-v4/` (v3 copied; v1, v2 and v3 untouched; v3's deck.pdf not copied). What changed: one new slide, slide 4 "Inspiration", a moodboard of twelve of the 29 saved posts with category, one-line caption and a credit line per image (X handle, post date, post URL, appendix number), the patterns as observations with every one of the 29 posts cited, a count by category, and the lighting gap stated as a gap in the saved material, not demand. Changed slides: 3 (brand: a thumbnail and credit beside each of the three rules), 5 (collection, v3's 4: "(saved post: slide 4)" on the e-ink display, the desk display and the aquarium; footer says no saved post shows lighting), 7 (funnel, v3's 6: one tile with the founder's two readings, labelled observation, assumptions unchanged), 8 (competition, v3's 7: one row and one sentence for the five-device promptable studio seen in one post, not researched). The appendix is slides 12 to 17 with 93 sources, the 29 post URLs among them, tagged "saved X post". v3's slides 4 to 10 are now 5 to 11; no v3 number, chart or layout fix changed.
- Files: `build_deck.py` (source of truth, new POSTS block; `python3 -I build_deck.py` regenerates), `deck.html` (17 slides at 1280x720 px, which print to 960x540 pt like v3's PDF), `prepare_images.py` and `images/` (twelve crops, relative paths, so `file://` rendering works), `check_deck.py` (extended: image paths, page size, slide count, names and sender wording, 29 URLs; all checks pass), `research.md` (section 8: method, the twelve posts, the patterns, the tie-ins, tags; v4 slide numbers), `README.md` ("What changed from v3", the render command for Innovator).
- Hard rules kept and scanned in every v4 file: the brand concept is the flagship; the digest product is not named; no Fionn, no "sent by" or "shared by", no artist or maker names (captions describe the object, post authors appear only as X handles in credit lines); valuation, round size and equity only in the off-the-table lines; no ships, shipyards or naval topics; no em dashes; every pattern labelled observation, never a measurement; post dates decoded from the post ids. Nothing sent, posted, bought or signed up for; no PDF rendered, no google-chrome run.
- Judge pending: Innovator's PDF render and visual pass (slides 3, 4, 5, 7, 8 and the six source pages are the ones v4 touched), Oscar's edit, the angel's questions.

## Blocked
- None. The PDF render is Innovator's step by design; the one-line command is in `ventures/gadgets/pitch-deck-v4/README.md`.

## Spend
- API: 0.00 EUR this month (ceiling 50). Subscriptions: no change.

## Proposals
- The 29 posts were not re-opened (x.com is not fetchable from a run); no figure from a post sits on a slide, so nothing depends on it. If one ever does, a for-claude task should re-open that post with Vela's X tooling first. Cost: minutes per post.
- No run can check HTML text overflow (moodboard cells, rule cards, tables) without a render; the `Bash(google-chrome:*)` allow-list proposal from this morning's wake report stands (gate 4, needs an approved decision).

## Next step
- Innovator renders `deck.pdf`, looks at slides 3, 4, 5, 7, 8 and the source pages, and files defects as a for-claude note; Oscar edits `build_deck.py` or `deck.html`. The next run does nothing on gadgets until a for-claude note or queue file.
