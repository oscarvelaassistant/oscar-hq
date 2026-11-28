# HQ report 2026-11-28 wake-2

Extra run started by Innovator on Oscar's behalf (The Scout post for the gadgets pitch deck v4). Local run on the box, no HUB connector: HUB steps skipped, Vela saves this report. No decision raised; `state.next_decision` stays 19. Filename carries "deck-v4-scout" as the payload asked. Commit 2c773d7 (the two posts of 27 Nov) is kept whole.

## Done since last report
- 2026-11-28-002 Gadgets pitch deck v4: The Scout (@kinglycrow, the magnetic Wi-Fi camera listed at $25 in the post) is on the moodboard (slide 4, cell 10) with its caption "Magnetic Wi-Fi camera at $25: an AI agent's eyes at home", category Desk gadgets, handle, post date and URL. It took the cell from the bronze figures, which stay cited in the hand-made pattern and in the appendix; Art objects keeps the ceramic ashtray, so every category and every pattern still has a cell. "Cheap hardware plus an app" counts 7 posts and names the camera in its citations; slide 7's observation tile cites it as a fourth post on "cheap hardware plus an app sells". Still 17 slides, 1280x720 CSS px, `build_deck.py` the source, `deck.html` regenerated, `check_deck.py` all passed, `deck.pdf` untouched, v1 to v3 untouched.
- The list changed under the task again. At 08:24, during this run, Vela committed a second post Oscar sent, the @audrlo production-robot post (3D-printed robot-head prototypes grown into a production home device), to the list's Desk gadgets (commit e589012), so the authoritative list is 28 posts, not the 27 the payload named. The deck follows the list: that post is cited in the wider-market pattern on slide 4 (where the inspiration README places it) and has its appendix URL; it is not on the moodboard. Appendix: 92 sources (90 before). `check_deck.py` expects 28 post URLs and the four posts added today.
- To make that commit, Vela stashed this run's uncommitted edits (stash "scout-run-wip") and re-applied them afterwards; her commit also carried this run's staged deletion of the bronze figures' crop from `pitch-deck-v4/images/`. Nothing was lost; the edits were checked file by file before continuing. The stash entry is still in the stash list and can be dropped.
- Copy and layout, by arithmetic on Innovator's render of 27 Nov (footer rule at about 665 CSS px): the three count lines on slide 4 keep their character counts, the wider-market line grows from 103 to 109 characters and stays at two lines, so the pattern list keeps its 20 lines (about 56 px above the rule) and the card grid its size (29 px). Slide 7's tile keeps three lines: the fourth footnote number was paid for by dropping "modular" from the third reading (the appendix entry still says modular), about 51 px kept. The footer's date range now ends 2026-11-28. No figure changed or invented; the $25 is the post's own figure and sign, not checked against a shop page.
- Hard rules scanned by `check_deck.py` and by eye: no PersonalPress; no person's name and no sender wording (authors only as X handles in credit lines); valuation, round and equity only in the off-the-table lines; no ships or naval topics; no em dashes. Nothing sent, posted, bought or signed up for; no google-chrome, no render.
- Written: `pitch-deck-v4/README.md` (new top section for this update), `research.md` section 8 (counts, 8.2 row 10, 8.3, 8.4, new 8.8), `check_deck.py`, `prepare_images.py`, task file `queue/2026-11-28-002-gadgets-deck-v4-scout.md`.

## Blocked
- None. Innovator's render is the judge for slides 4 and 7; the command in the v4 README is unchanged.

## Spend
- API: 0.00 EUR this month (ceiling 50). Subscriptions: no change.

## Proposals
- Same as the last report, now with a second occurrence in one morning: Vela and the HQ run edit the same checkout on the box. This time her commit needed a stash of the run's work and swept one of the run's staged deletions into her commit. One line in `playbooks/run-procedure.md` or the hq-run skill (a wake run works in its own `git worktree`, or Vela waits for the run's push before committing) would end it. Cost: minutes.
- The payload's count (27) was stale again by the time the run had read the repo; the run procedure's "read the repo first" caught it, and the deck follows the list. A line in the hq-run skill ("state the list's commit, not its count") would make the payload robust. Cost: one line.

## Next step
- Innovator renders `deck.pdf` and looks at slides 4 and 7. If anything touches the footer, the same lever applies: the measured positions, then `build_deck.py`.
