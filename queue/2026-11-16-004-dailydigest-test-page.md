---
id: 2026-11-16-004
title: DailyDigest test page: the setup form on Oscar's own Digest backend, plus the question design
role: cofounder
priority: P1
status: in-progress
created: 2026-11-16
created_by: Oscar (19:12 in Innovator chat), filed by Innovator
effort: Fable 5.2 high
depends_on: 2026-11-16-003 (beta-plan.md); build on its cut, do not redo it
approval: Oscar asked for the page to be built now ("yes go do that now"). Setup page pick (D-017) answered by Oscar on 18 Nov 2026 at 10:18 Madrid, "Keep A, the evening page" (relayed by Vela in the wake run's payload)
---

## Goal
Oscar, in his words (19:12 Madrid, 16 Nov): "create a new page to test the DailyDigest (new name i coined as a placeholder), and make it so it reuses the same or similar backend structure i used for my own digest, and have claude think of the questions and the connects we can ask from the clients to make the best possible digest for them (which for now will be a pdf we send them), it's also important that it's as intuitive, frictionless, and that filling in the form doesn't lose the customers during the sign in process, be ruthless about that, whilst also asking questions in the best pointed way so that we are able to get them their best possible digest."

"DailyDigest" is a placeholder name; use it on the page.

## Two parts

### A. Question design (`ventures/digest/questions.md`)
- Every question or connection that could improve a reader's Digest, then the ruthless cut: what is asked on the page, what is inferred, what is asked later (from a reply to the first issue, or in the first week), and what is dropped. One line of why for each.
- "Connects" means optional links the reader can give for better context (for example an X handle, a newsletter or site they read, a Goodreads or Letterboxd, a city for weather). Say which ones are worth it at beta stage and which wait. No OAuth or third-party account sign-up in the beta.
- Friction rules, applied: the first screen asks the minimum, no account, no password, the link is the login, progress saved on every field, mobile first, done in under two minutes on a phone (a target, not a measurement), sensible defaults, examples in every field, one clear "make my first issue" button, and a preview of the masthead with their name.
- Questions phrased the pointed way: concrete prompts ("Three things you'd read about even on a busy morning") rather than category checkboxes. Show the final wording.

### B. The page and its backend
- Build the setup page and the profile store from `beta-plan.md` section 2, reusing the personal Digest's structure in `/workspace/digest` (builders, `lib/`, renderer, text rules, fonts) through a fork in `/workspace/digest-product/`. The personal Digest stays untouched.
- Page: same typography and design rules as `spec.md` section 5 and `playbooks/design.md`.
- Done when Oscar can open the page on his phone, fill it in as reader 1, press the button, and a PDF built from his answers is produced on the box and passes the validator. Sending the email is the step after he has created the Gmail app password himself; until then `send.py` runs against the stub only.
- A private deploy to `digest-preview.projetrefonte.com` (noindex, secret per-person links, no public landing) is in scope once the local version passes, because Oscar asked for a page he can send. Stop before any account sign-up, purchase or spend, and report it as a gate.

## Gates
- Nothing is sent to Paul or Pietro. Oscar hands out the links himself.
- No new accounts, no spend, no API key.
- No em dashes. Decisions named by title. No estimates unless labelled.

## Report back
Page URL (or local path), the final question list, the cut list, what Oscar must do by hand next, and any gate reached.

## Log
- 2026-11-16 21:06 (Claude, evening, cloud run): started. The box (`/workspace/digest`, `/workspace/digest-product/`) is not reachable from a cloud run, so part B's fork, runner and PDF cannot be done here; the cloud half (the page and the Worker) can.
- 2026-11-16 21:13 (Claude, evening): part A done: `ventures/digest/questions.md` (everything that could be asked, the cut into asked now, inferred, asked later and dropped, the connects worth it at beta stage, the friction rules applied one by one, the final wording, the profile the writer receives). Part B, cloud half done as a draft: `ventures/digest/beta/` with `public/form.html` (the setup page, three fields above the button, autosave on every field, masthead preview from the name, one button, status line), `worker.js` (the six routes, nonce CSP, noindex, runner token), `worker.test.mjs` (28 checks with a mock KV, all pass), `wrangler.toml` (KV id blank), `new_link.sh`. Page rendered at 390 px in headless Chromium and looked at. No em dash (checked by a test). Nothing deployed, no account, no spend, nothing sent.
- Status stays `in-progress`: the done-when (Oscar fills it in on his phone, presses the button, a PDF is produced on the box and passes the validator) needs sessions 1 to 3 on the box. Next: a Claude Code session on the box with Oscar, starting with session 1 of `beta-plan.md`; session 3 takes this folder as its starting point.
- 2026-11-16 21:30 (Claude, wake-4, local run on the box, started 19:13 by Vela): this run and the evening cloud run worked this task at the same time without seeing each other, because the task still read `open` in the repo until this run committed at its end. Result: two question designs, two pages and two Workers. Nothing of the evening run was changed. This run's question design is kept beside it as `ventures/digest/questions-box-run.md`; its code is on the box in `/workspace/digest-product/`. The choice between them is the decision below. This run also went over the 60-minute budget (about two hours by the clock) and stopped building when it saw that.
- 2026-11-18 09:10 (Claude, morning, cloud run): the decide-by time for "which DailyDigest setup page to keep" (D-017) passed with no approval note in the HUB and no change to this file's `approval:` field. The written default holds: A (`ventures/digest/questions.md`, `ventures/digest/beta/`) stays the repo's version, the box fork waits, nothing is deployed. Oscar can still pick B or C; the memo stands below. Status stays `in-progress`; the remaining done-when needs a box session.
- 2026-11-18 10:19 (Claude, wake, local run on the box, started by Vela): Oscar's answer to "which DailyDigest setup page to keep" (D-017) arrived in the run's payload: "Keep A, the evening page" (18 Nov 10:18 Madrid). Recorded in `approval:`. A was already the applied default, so no file moved; `questions-box-run.md` is marked not kept and the box fork's `worker/` is left on disk, unused. Work done on the box fork, in the order of the list below: the validator and the renderer now read A's profile shape (the never-list is read out of the `about` box, "why you" may rest on topics, about, city or urls) and print the masthead "The <Name> Daily"; the copy budgets are measured per slot and all 12 full-page test cases fit (item 3, done); schema, fixture and tests follow (16 tests pass, fixture passes offline and with `--pdf`, preview looked at). Not done: anything that needs node, the claude CLI or a deploy (none allowed in this run). Two open points for Oscar are in the report and the fork README (name length 40 on the page against 24 in the masthead; masthead typeface differs between page preview and PDF). Status stays `in-progress`.

## State of the box half after the wake run of 2026-11-18
Code lives in `/workspace/digest-product/` (outside this repo, no git there). Its `README.md` lists every file, what was checked and what is not built, in order.

Done
- `validate.py` and `render_issue.py` on the kept page's profile shape, masthead "The <Name> Daily". 16 unit tests pass; the placeholder fixture passes offline and with `--pdf`.
- Copy budgets measured on the page (`dev/calibrate_budgets.py verify`: every slot at its limit, 4, 5 and 6 stories, four fillers, 12 of 12 fit, nothing dropped). In characters: lead headline 56, dek 110, body 300, why you 95, 2 sources; a short slot 45, 180, 50, 1 source; the tall column 60, 560, 90, 3 sources. The tightest case leaves 4 px, and the filler is made-up prose, so the renderer's overflow refusal stays the last check. The numbers live in `validate.BUDGET`; `issue.schema.json` repeats them for the writer and a test keeps the two equal.
- From wake-4, not kept: part A's second version (`ventures/digest/questions-box-run.md`) and its page in the fork's `worker/`.

Not done (the next run picks up here, in this order)
1. Run the kept Worker's tests on the box (`node worker.test.mjs` in a copy of `ventures/digest/beta/`; 28 of 28 in the cloud run, never run on the box: no box run has been allowed to start node).
2. `beta_runner.py`, `write.sh` and `WRITE-PROMPT.md` (designs in the fork README, on the kept Worker's status contract in `ventures/digest/beta/README.md`).
3. One real issue from Oscar's answers through the writer, validated with links opened.
4. `send.py` against the stub.

Not met from the done-when: Oscar opening the page on his phone, and a PDF built from his answers. Both need a box session with node, the claude CLI and, for the page on his phone, the deploy with his typed yes.

## Decision

Answered 18 Nov 2026 10:18 Madrid by Oscar: A ("Keep A, the evening page"). The memo below is kept as written.

### D-017 Which DailyDigest setup page to keep
- What: two runs built the page the same evening without seeing each other's work. Pick the question set; the code follows the pick.
- Why now: the next box session should build on one page, and the validator and PDF renderer on the box are written for one profile shape.
- Options:
  - A) The evening run's page (`ventures/digest/questions.md`, `ventures/digest/beta/`). Three required fields: name, city, one box for topics. Work and the never-list share one optional 600-character box behind a fold. Masthead "The <Name> Daily". Its Worker passes 28 tests.
  - B) The box run's page (`ventures/digest/questions-box-run.md`, `/workspace/digest-product/`). Four questions on the first screen: name, three topic lines, "What do you do all day?", an optional never-list. City is guessed and optional. Masthead "<Name>'s Digest" in the paper's own blackletter, fonts embedded. Its Worker has never run.
  - C) B's questions and look, on A's tested Worker.
- Recommendation: C (my opinion, and I wrote B, so weigh that). "What do you do all day?" is the only source for the "why you" lines, so it belongs where every reader answers it, and the masthead on the page should match the PDF they receive. A's Worker is the one with passing tests. Tradeoff: one merging step before anything can be deployed, and one more field on the first screen than A.
- Reversible: yes. Nothing is deployed and both versions stay on disk.
- Decide by: 2026-11-18 09:00. Default if silent: A stays the repo's version, the box fork waits, nothing is deployed.

The deploy itself is unchanged: Oscar's typed yes in the session that does it, as `beta-plan.md` section 4 says.
