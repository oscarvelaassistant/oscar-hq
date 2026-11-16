# Digest beta: the cut Paul and Pietro can open from a link

Written 2026-11-16 by the wake-3 run (task `queue/2026-11-16-003`), after the Digest beta decision (D-016): Oscar wants a link each partner opens to set up their own Digest and get a PDF by email, as a proof of concept the three of them discuss before anyone thinks about distribution. Status: plan only. Nothing here has been deployed, sent, created or signed up for.

This file cuts `spec.md` down. Where the two differ, this file governs the beta; `spec.md` stays the later full build. Limits and prices are not repeated here, they sit in `spec.md` sections 2 and 6 with their URLs. No estimates anywhere below.

What I read to write it: `plan.md`, `spec.md`, `/workspace/digest/README.md`, `daily.sh`, `DAILY-PROMPT.md` and AgentConfig `hub/registry.json`. I did not read the builders (`build_page3.py`, `lib/`) or the hub's `worker.js`; session 1 starts by reading the builders.

## 1. The cut

| In `spec.md` | In the beta | Why |
|---|---|---|
| Three readers invited by hand, nothing public (section 0) | Kept | It is the approved scope (the Phase 0 prototype decision, D-008). Oscar is reader 1 and tests every step on himself first. |
| Worker `digest-app` with 38 routes by my count, sessions, admin, device and cron (sections 1 and 4) | Replaced by a Worker `digest-beta` with six routes (section 2 below) | The beta needs a form that saves a profile and a way for the box to read it. |
| Invite codes, sessions, cookies, CSRF header (sections 4 and 8) | Faked: one secret link per person. The link is the login and, opened again, the settings page. | Three people who know each other. A lost link is replaced by Oscar with one command. |
| Email address in the profile, sign-up route | Dropped from the cloud. Oscar types each address into a file on the box. | The form cannot make Oscar's Gmail write to an address he did not enter, and no address sits in Cloudflare. |
| Data model with 17 key types (section 3) | Four: the profile, an index, a status line, the runner token | Everything else served screens the beta does not have. |
| Job queue, cron trigger, retry schedule (section 4) | Faked: a loop on the box with its state in local files | The box already decides when to run; a second scheduler in the cloud adds tests and no behaviour three readers would see. |
| Onboarding form (section 5, screen 3) | Kept, cut to six fields and one button | It is half of what the partners are asked to judge. |
| Landing page, sign-up, privacy and imprint pages, launch flag | Dropped. Two sentences on the form say what is stored and who reads it. | Nothing is public. |
| Reader with page and text views, archive, account page, export, self-service delete | Dropped. The inbox is the archive. Oscar deletes a profile on request with one command. | The email delivery decision (D-009: PDF by email from Oscar's Gmail) already makes the email the delivery. |
| Open and click events, feedback box, the `auto` profile block | Dropped. Feedback is a reply to the issue email, which lands in Oscar's inbox, and the review. | With three readers, asking is cheaper than tracking. |
| Device tokens and the e-ink pull | Dropped | Neither partner has a reading device. |
| `gather.py` with curated feed lists per topic | Replaced: the writing run searches the web itself, plus any URLs the partner gave | Free-text topics work on day one with no feed curation. `DAILY-PROMPT.md` already does this when the X exports are missing. |
| `write.sh` on Oscar's subscription, Opus, high effort (section 6, step 2) | Kept, with WebSearch added to its tools. The second `api` backend is not built. | The Phase 0 prototype decision (D-008) as Oscar answered it. One backend is less code; the swap is written when a spend decision asks for it. |
| `validate.py` | Kept, smaller: every story has a source, no em dash, the other readers' names do not appear, each cited URL is opened once | A dead link (DNS error, 404) fails the story. A block page (401, 403, 429) is logged as unchecked, since news sites often refuse scripts. |
| `render.py`, newspaper style, house page size | Kept as it is: one page from the page 3 template, the reader's name in the header | No template work. Page shape and length are review questions (section 5). |
| `upload.py`, PNG previews and issue JSON in KV | Dropped | No reader to show them in. |
| `send.py` through Gmail SMTP | Kept as specified (section 6, step 5), with two body lines changed | The email delivery decision (D-009). |
| Styles, lengths, languages, cadence | English, daily by 07:00, plus "make my issue now". Style is a tone choice in the prompt. Layout styles and lengths wait. | A tone is one prompt variable. A layout is template work. |
| Usage log per issue | Kept | `claude -p` returns it for free, and the cost-per-issue question comes back later. |
| Test matrix (sections 4 and 10) | Small: the six routes and `validate.py` | Proportionate to six routes. |
| Four weeks of measurement and the exit test | One week, then the review in section 5 | The Digest beta decision (D-016): the purpose is to agree what the product looks like. |

## 2. The smallest working path

| Step | What it is | Where it runs | Why there |
|---|---|---|---|
| Link | `https://digest-preview.projetrefonte.com/s/<key>`, one per person. The key is 32 random bytes; the Worker stores only its SHA-256. A wrong key shows one plain line. | Worker `digest-beta`, Cloudflare free plan, Oscar's existing account and zone, noindex on every answer | It has to open on a phone anywhere. Whether the box is reachable from outside, I don't know, and this way the plan does not depend on it. Oscar confirmed the hostname on 2026-11-12. |
| Setup form | One page at the link, prefilled on return. Fields: name on the masthead; city; topics as free text with tappable examples; "what you do, what you care about, what you never want to read" (up to 600 characters); tone (straight, analytical or light); up to 5 URLs of your own, optional. One checkbox pauses the daily issue. Button: "Save and make my issue now". A status line under it: being made, sent at HH:MM, or Oscar's late text. | The same Worker, as one static HTML file with a small script | No framework and no build step, as `spec.md` section 9 argues. Design per `playbooks/design.md`, fonts from the pipeline. |
| Profile stored | `profile:<sha256(key)>` plus one index key, so the box reads everything in one request. No email address. | KV namespace `DIGEST_BETA`, its own, never `OSCAR_DIGEST` | Product data stays apart from Oscar's personal data (`plan.md` section 4). |
| Run | `beta-runner.sh`, a loop in the style of `whoop-morning-watch.sh`, with a lock. Every 2 minutes it reads the profiles. It makes an issue when a profile was saved with the button (at most 3 such issues per person per day) and once a day from 04:30 Madrid, one reader after another. It starts nothing during a quiet window around the personal Digest's own 06:35 routine. State and logs stay in local files. | The box, `/workspace/digest-product/` | The writer is Oscar's Claude Code login, which only the box holds (`spec.md` section 1). 04:30 comes from the spec's cap of 25 minutes per writing run: three readers end by 05:45 when no run needs its retry. |
| PDF | `write.sh`: one fresh `claude -p --model opus --effort high` run per issue with Read, WebSearch and WebFetch only, returning the issue as structured output (4 to 6 stories, each with a source and a "why you" line built only from what the reader typed). Then `validate.py`, then the renderer forked from `build_page3.py`. On a refusal or an overflow the script hands the message back to Claude once. A second failure stops the issue. | The box | The renderer, fonts and checks exist there. The writing run gets no Bash, because it reads the open web on a machine that holds a Gmail credential. |
| Email | `send.py`: one message per reader from Oscar's Gmail through `smtp.gmail.com`, the PDF attached, three body lines (the masthead line, "Change your Digest: <your link>", "Reply to this email with what was wrong today"). A failed issue sends one message to Oscar's own address with the reason, and the form shows "Today's issue is running late. We're on it." | The box | The app password is an SMTP credential and stays in a chmod 600 file on the box (`spec.md` section 2). Addresses and links sit in `recipients.json`, chmod 600, never in a repo, a log or the Worker. |

The six routes: `GET /s/<key>` (the form), `PUT /s/<key>` (save), `GET /r/profiles`, `PUT /r/links/<id>` and `PUT /r/status/<id>` (runner token only), `GET /health`.

Oscar HUB as the work environment: not for this. The form is a page two outside people open, and putting it on the hub Worker would place a partner-facing route beside Oscar's notes and the WHOOP token, for no saving: a second small Worker uses the same account and the same deploy path. The hub's own home for this is the status tool in `plan.md` section 4, which waits for Phase 2. For Vela: `2026-11-16 | Digest beta: partner profiles in the beta Worker's KV and partner addresses in a chmod 600 file on the box, outside the hub, because they are product data | revisit 2026-12-12 | for Vela`.

What survives into the full build: the pipeline fork (the same folder as spec step 2), the write prompt, `send.py`, the form fields. What is thrown away: the beta Worker and the runner's local state. Undo: delete the Worker, the KV namespace and the hostname route, revoke the app password, delete the fork.

## 3. Build sessions, in order

Each is one Claude Code session on the box with Oscar (Opus, high effort or more, no permission-skipping flags).

1. A partner's issue on the box. Fork `/workspace/digest` into `/workspace/digest-product/` (the personal one is not touched). Make the reader's name and the PDF title parameters. `WRITE-PROMPT.md` is `DAILY-PROMPT.md` with the personal parts removed (WHOOP, vault, X exports, HQ, council, Vela's voice). Add `issue.schema.json`, `write.sh`, `validate.py` with its tests, `make_issue.sh <id>`, and two profile files typed by hand: Oscar's and a made-up one with different topics.
   Done when: `./make_issue.sh oscar` writes a one-page PDF with his name in the header and 4 to 6 stories, every source link opens, every "why you" line points to something in his profile file, the checks pass, the made-up profile gives a visibly different issue, and the log shows the run's duration and usage. Nothing deployed, nothing sent.
2. Email and the loop. Oscar creates the Gmail app password himself. Add `send.py` (tested against a local SMTP stub first), `recipients.json` holding only Oscar's address, `beta-runner.sh` reading the profile files, and the failure message to Oscar.
   Done when: Oscar edits one line of his profile file and, with no further command, the PDF arrives in his Gmail inbox and he has opened it on his phone; a deliberately broken profile produces the failure message to him and nothing else; the next morning his issue is in his inbox by 07:00 with nobody touching the box.
3. The link. Worker `digest-beta` with the six routes and the form, tests with a mock KV as `oscar-digest` has, `new_link.sh <id>`, the runner switched from profile files to `GET /r/profiles`. Then, on Oscar's typed yes, the deploy: KV namespace, Worker, hostname.
   Done when: the tests pass; Oscar opens his own link on his phone, fills the form, presses the button, sees "being made", receives the PDF and sees "sent at"; he changes his topics and the next issue differs; a wrong link shows the plain line; a fourth press on the same day is refused politely.
4. Handover (Oscar's own step, no build). He adds the two addresses to `recipients.json`, runs `new_link.sh` twice and gives each partner their link himself.
   Done when: both partners have told him their first issue arrived. The week starts that day.

Between the handover and the review, the only change allowed is fixing a delivery that failed. Everything else goes on a list for the review. This keeps the Pocket Factory mornings, and it keeps the week's issues comparable.

## 4. What Oscar does by hand, and every yes

By hand:
- Create the Gmail app password at myaccount.google.com (it needs 2-Step Verification, https://support.google.com/accounts/answer/185833) and paste it into `gmail.env` himself. No agent creates, reads aloud or copies it.
- If `wrangler` is the deploy path and the box has no Cloudflare API token (I don't know whether it has), create one in his dashboard for the existing account.
- Type Paul's and Pietro's addresses into `recipients.json`. They are never written in this repo.
- Hand over the two links, with whatever he wants to say about the test. A draft only if he asks for one.
- Read the replies in his own Gmail and bring them to the review.
- Approve the two sentences on the form before a partner sees them.

Yes needed:
- The deploy in session 3 (Worker, KV namespace and hostname on the existing account and zone, free plan, noindex): his typed yes in that session. It is the first moment anything is reachable from the internet.
- Issue emails to Paul and Pietro: covered by the email delivery decision (D-009). The first one leaves only after Oscar has entered an address and handed a link, so the handover is his yes in practice.
- Writing on his Claude subscription for other readers: his call of 2026-11-12, unchanged (`spec.md` section 12).
- Not in the beta and still gated: any API key or spend, a mail service, a domain, anything public, a fourth reader.

## 5. The review after the first week

Bring: each person's best issue and worst issue, printed or on screen; Oscar's replies folder; the runner log (issues due, sent, failed and why, usage per issue, how often each person pressed the button and changed their profile).

Decide, in this order:
1. Did it feel written for you? Which "why you" lines were right, which were wrong. If both partners say no, the next build is better inputs, and questions 2 to 4 wait.
2. The object: is it this page, and on what screen? The page is drawn at 8.25 by 6.19 inches for an e-ink tablet held landscape, and both partners read on a phone. One page or more.
3. The setup: which fields changed the issue, what was missing, and whether a form is enough or the product has to learn from what is read.
4. Rhythm: daily or weekly, and at what hour.
5. Who gets the next links, and who owns what. The Digest beta decision (D-016) left open what Paul and Pietro each own; each of them comes with the names of the first people they would hand a link to.
6. Go on, change it or stop. If go on: before anyone outside the three receives an issue, `plan.md` section 2 applies (an API key, which is a spend decision).

## 6. Claude's judgement (opinion, labelled)

Is this the most Pareto-efficient version? For what Oscar asked, I think yes. A smaller one exists: skip session 3, ask each partner five questions in a message and type their profiles by hand. It puts PDFs in their inboxes one session sooner and leaves out the part Oscar named, that they create their own. The setup is also the first thing a paying client would touch, so the three cannot agree on the product without having used it. The session order keeps the smaller version in reserve: if session 3 stalls, typed profiles start the week after session 2.

The one thing most likely to sink it: issues that read like topic news. Oscar's own Digest works because it reads his X likes, his vault and his HQ. A partner's issue has a form with a few lines. If Paul opens three issues and none tells him something a newsletter would not have, the layout will not carry it, and `plan.md` section 9 already calls the layout the part anyone can copy. What the cut does about it: the free text is the main input, every "why you" line has to point at something the reader wrote, and the button lets a partner rewrite the profile and see a different issue the same evening. What it does not do is learn from what they read. If question 1 of the review comes back no, that is the next thing to build, ahead of any reader or account page.

Second, and visible on day one: the phone. Session 2's done-when has Oscar open the PDF on his own phone before a partner does.

## Pointers

- The Digest beta decision (D-016): `ventures/_company/cofounder/decisions.md`. The task: `queue/2026-11-16-003`.
- The questions behind the form and their cut: `questions.md`. The form and the Worker as a draft for session 3: `beta/` (task `queue/2026-11-16-004`, 2026-11-16 evening).
- The full build this cuts down: `spec.md`. The product plan: `plan.md`.
- The pipeline it forks: `/workspace/digest/README.md`. The Worker pattern it borrows: `/home/box/projects/oscar-digest/README.md`.
- Oscar's standing feedback for any Digest build: `/home/box/AgentConfig/docs/OSCAR-FEEDBACK.md` (done means checked on the device).
