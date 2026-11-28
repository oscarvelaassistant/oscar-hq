# HQ report 2026-11-28 wake

Extra run started by Innovator on Oscar's behalf (the two posts Oscar sent on the evening of 27 Nov, for the gadgets pitch deck v4). Local run on the box, no HUB connector: HUB steps skipped, Vela saves this report. No decision raised; `state.next_decision` stays 19. Filename carries "deck-v4-two-posts" as the payload asked.

## Done since last report
- 2026-11-28-001 Gadgets pitch deck v4: the e-ink tablet post (@huntie) and the ESP32 AMOLED board post (@ahm3dhub) are on the moodboard (slide 4, cells 4 and 8) with captions, category, handle, date and URL; slide 4's patterns, count chart and footer updated; slide 5's e-ink display says "saved posts"; slide 7's observation tile has a third reading and citation; all post URLs in the appendix. Edited slides: 4, 5, 7 and the appendix (12 to 17). Still 17 slides, 960x540 pt, `build_deck.py` the source, `deck.html` regenerated, `check_deck.py` all passed, `deck.pdf` not touched, v1 to v3 untouched.
- The list changed under the task. At 08:03, during this run, Vela committed Oscar's request to remove the five Wall and decor posts from `ventures/gadgets/inspiration/` (commits c653f43 and 84ec477), so the authoritative list is 26 posts in six categories, not the 31 the payload named. The deck follows the list: those five posts, their images and their category are gone from it, and `check_deck.py` now fails if any of their ids or the words "Wall and decor" reappear. The appendix has 90 sources (93 before: 2 in, 5 out).
- Moodboard swap: the two new posts replace the AirPlay board (still cited in two patterns and the appendix; the least legible image at 92 px) and the illustration that left with the Wall and decor posts; the water gun moved from cell 8 to cell 11. `images/` holds exactly the twelve crops shown (two made by `prepare_images.py`, two removed with `git rm`).
- Copy: "Cheap hardware plus an app" counts 6 posts; "E-ink and calm screens" counts 2 and no longer says "a thin signal"; "Ceramics and hand-made objects" is 8 of 26; the lighting gap says "None among the 26" and lost its second sentence (slide 5's footer still says the light family rests on the 26 Nov catalogue decision). Slide 7's third reading: a modular AMOLED board with voice sells off the shelf from China. All labelled observations, never a market measurement; no figure changed or invented.
- Layout, by arithmetic on the text positions of Innovator's render of 27 Nov (pypdf; footer rule at about 665 CSS px): slide 4's pattern list is 20 lines (21 before) and the count chart one row shorter, so the right column ends about 56 px above the rule (21 px before) and the card grid is unchanged at 29 px; slide 7's tile takes a third line from a 65 px margin, about 51 px left; slide 5 adds one character to a short second line, 19 px kept. The 27 Nov fix on slides 3, 4, 5 and 7 is untouched.
- Hard rules scanned by `check_deck.py` and by eye: the flagship is the brand concept; no PersonalPress; no person's name and no sender wording (authors only as X handles in credit lines); valuation, round and equity only in the off-the-table lines; no ships, shipyards or naval topics; no em dashes. Nothing sent, posted, bought or signed up for; no google-chrome, no render.
- Written: `pitch-deck-v4/README.md` (new section "Update of 28 Nov 2026: two posts added, five removed"), `research.md` section 8 (counts, 8.2 grid, 8.3 patterns, 8.4 tie-ins, new 8.7), `check_deck.py`, `prepare_images.py`, task file `queue/2026-11-28-001-gadgets-deck-v4-two-posts.md`.

## Blocked
- None. Innovator's render is the judge for slides 4, 5 and 7; the command in the v4 README is unchanged.

## Spend
- API: 0.00 EUR this month (ceiling 50). Subscriptions: no change.

## Proposals
- Vela and the HQ run edit the same checkout on the box (`~/oscar-hq`): her two commits landed while this run had uncommitted edits in another folder. It worked this time because the folders differed. One line in `playbooks/run-procedure.md` or the hq-run skill (a wake run works in its own `git worktree`, or Vela waits for the run's push before committing) would remove the risk of one actor committing the other's half-done files. Cost: minutes.
- A payload that states a count from the repo (here "31 posts") can be stale by the time the run starts; the run procedure already says to read the repo first, which is what caught it. No change needed, noted for the record.

## Next step
- Innovator renders `deck.pdf` and looks at slides 4, 5 and 7. If anything touches the footer, the same lever applies: the measured positions, then `build_deck.py`.
