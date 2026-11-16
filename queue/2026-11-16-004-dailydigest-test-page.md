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
approval: Oscar asked for the page to be built now ("yes go do that now")
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
