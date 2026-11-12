# Digest product, Phase 0 build spec: front end, customer journey, cloud backend

Written 2026-11-12 by the wake-2 run (task 2026-11-12-002), following `ventures/digest/plan.md`; updated the same day by the wake-3 run (task 2026-11-12-003) with Oscar's answers to section 13 and the change to PDF-by-email delivery (D-009). Status: spec only. Nothing in here has been deployed, registered, created, sent or generated for anyone. Every limit and price is quoted from the URL next to it or marked unknown. No estimates, except where a number is labelled as Claude Code's own client-side estimate.

The spec is written so a Claude Code build session on the box (Opus, effort high, as the rules say) can build Phase 0 from it without raising a new decision. Where it cannot, section 12 says so.

## 0. Decision record and scope

- D-008, answered by Oscar on 2026-11-12 at 14:55 Madrid through Cofounder, relayed by Vela: yes to Phase 0, with one change. For the first tests the issues are written with Claude on Oscar's own Claude subscription, through Claude Code, not with an API key, so there is no API spend for now. He was told once that Anthropic's Claude Code legal page bars subscription credentials for issues made for other people (https://code.claude.com/docs/en/legal-and-compliance), and chose it anyway. Recorded as his call here, in `queue/2026-11-12-001`, and by Cofounder in `ventures/_company/cofounder/decisions.md`.
- What this changes against the plan: plan section 2 ("generation must move to the API") is superseded for Phase 0. The writing step is built behind one interface with two backends, `claude-code` (subscription, Phase 0) and `api` (Anthropic API key, needs a gate 2 decision). Swapping is a configuration change, not a rebuild.
- D-009, 2026-11-12 at 15:11 Madrid, Oscar via Cofounder, logged by Vela in `ventures/_company/cofounder/decisions.md`: the MVP delivers each issue as a PDF by email. The test PDFs are emailed from Oscar's own Gmail account to Oscar, Paul and Pietro, with no mail service sign-up. All issues are in English. Choosing and signing up for an email provider is not approved; it stays a gate 2 decision for later, prepared in section 7a.
- Oscar's answers to the wake-2 open inputs, 2026-11-12 at 15:09 Madrid via Cofounder, relayed by Vela: the Phase 0 hostname `digest-preview.projetrefonte.com` is fine; Oscar is client 1; the text clients see when an issue fails is "Today's issue is running late. We're on it."; the partners are Paul (reads French, Spanish and English, lives in Barcelona, no reading device) and Pietro (reads English, lives in Barcelona, no reading device). Both partners therefore read on a phone or laptop, in the `Europe/Madrid` timezone, and the email with the PDF is their delivery.
- Scope of Phase 0: three readers (Oscar and the two partners), invited by hand, nothing public. The code is the product's code, not a throwaway: the landing page, sign-up and the public parts are built but held behind a launch flag until the Phase 1 decisions (domain, gate 2; site live, gate 3).
- Out of scope here: product name, pricing, legal vehicle (partners' decisions), billing (Phase 2, Stripe sign-up is gate 2), a mail service of the product's own (Phase 2, gate 2, section 7a), the hub status tool (Phase 2, plan section 4), languages other than English (D-009; build step 6).

## 1. Architecture

Three parts, one trust boundary.

- A. The cloud: one Cloudflare Worker, `digest-app`, on the free plan, with its own KV namespace `DIGEST_PRODUCT`. It serves the landing page and the client web app as static assets, exposes the JSON API, holds client profiles, issues and jobs, and runs one cron trigger that decides which issues are due. It never calls Claude.
- B. The box: `/workspace/digest-product/`, a fork of the one-reader pipeline. A runner loop pulls due jobs from the Worker, gathers public sources, writes the issue with `claude -p` on Oscar's Claude Code login, renders the PDF and previews with the existing Playwright renderer, validates, uploads the result to the Worker, and then emails the PDF to the client from Oscar's Gmail account through `smtp.gmail.com` (D-009). It never serves clients.
- C. Clients: their email inbox (the PDF attached, plus a link to the reader), a browser (phone or laptop) with a session cookie, or an e-ink device with a per-client device token that pulls the latest PDF.

Why the email is sent from the box and not from the Worker: the sender is Oscar's Gmail account with an app password, which is an SMTP credential; the box already holds Oscar's secrets in chmod 600 files, the Worker holds none (section 8), and the PDF is already on the box when the issue is done. A Worker could open an SMTP connection, but that would put a Gmail credential in a Cloudflare secret for no gain at three readers. When a product mail service is approved (section 7a), sending moves to the Worker.

Why the writer lives on the box and not in the Worker: the subscription login is Claude Code's OAuth login on the box (`claude auth login`). A Worker cannot hold it. Claude Code's documentation says bare mode "doesn't use your subscription login" and "never reads OAuth credentials" (https://code.claude.com/docs/en/headless), so the runner calls plain `claude -p`, the way `/workspace/digest/daily.sh` does today, never `--bare`.

Nothing of the personal Digest is shared: `/workspace/digest`, the Worker `oscar-digest` and the KV namespace `OSCAR_DIGEST` stay untouched (plan section 3). Oscar's personal inputs (WHOOP, vault, X exports, the hub) are never read by the product pipeline.

## 2. Placement and names

| What | Where |
|---|---|
| Worker source, static site, tests | `/home/box/projects/digest-product/` (new git repo on the box; `worker.js`, `public/`, `test/`, `wrangler.toml`) |
| Pipeline fork | `/workspace/digest-product/` (new; copies `lib/`, `fonts/`, the renderer and the page templates from `/workspace/digest`, then diverges) |
| Phase 0 hostname | `digest-preview.projetrefonte.com`, a custom domain on the Worker in the zone Oscar already owns (no spend). The product's own name and domain are Phase 1 decisions; the Worker moves hostname then. |
| KV namespace | `DIGEST_PRODUCT`, binding `DP`, created in the same Cloudflare account, free plan |
| Tokens on the box | `/home/box/.config/digest-product/runner.env` and `admin.env`, chmod 600, same pattern as `/home/box/.config/oscar-digest/`; moved to the Proton Pass vault "Agents" when the vault exists (AgentConfig secrets rule) |
| Gmail credential on the box | `/home/box/.config/digest-product/gmail.env`, chmod 600: Oscar's Gmail address and a Google app password that Oscar creates himself at myaccount.google.com (app passwords need 2-Step Verification on the account, https://support.google.com/accounts/answer/185833). No agent creates, reads aloud or copies it; Oscar revokes it from the same page whenever he wants. Moves to the vault with the other secrets. |
| Deploy path | As `oscar-digest` today: the Worker uploaded through Vela's Cloudflare connector, or `wrangler deploy` from the box with a Cloudflare API token for the existing account (not a new account, not a spend). The build session uses whichever exists; no permission-skipping flags. |

Limits the design respects, Workers Free plan (https://developers.cloudflare.com/workers/platform/limits/): 100,000 requests a day resetting at midnight UTC; 10 ms CPU per request and per cron invocation; 5 cron triggers per account; 15 minutes wall time per scheduled invocation; 50 subrequests per invocation; 100 Workers per account; static assets 20,000 files per version, 25 MiB per file. Static asset requests "are free and unlimited" (https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/), so the landing page and the app shell cost nothing against the request cap; only `/api/*`, `/i/*`, `/d/*`, `/r/*`, `/a/*` and the cron count.

Workers KV, free plan (https://developers.cloudflare.com/kv/platform/limits/): 100,000 reads a day; 1,000 writes a day to different keys; 1 write per second to the same key; 1 GB storage; keys 512 bytes; metadata 1,024 bytes; values 25 MiB. The daily write cap is the binding limit: section 3 counts writes per client per day.

## 3. Data model (KV namespace `DIGEST_PRODUCT`)

Identifiers: a client id `cid` is 10 random base32 characters, never derived from the email. Every secret (invite code, session id, token) is stored as its SHA-256 hex, never in clear, as `oscar-digest` does today.

| Key | Value | TTL |
|---|---|---|
| `client:<cid>` | profile JSON (fields below) | none |
| `email:<sha256(lowercased email)>` | `cid` (login and duplicate check) | none |
| `clients:index` | JSON array of `{cid, status, tz, cadence, weekly_day, ready_by}` for the cron (one read instead of a list) | none |
| `session:<sha256(sid)>` | `{cid, created, expires, ua}` | 90 days |
| `invite:<sha256(code)>` | `{cid, created, expires, used_at, note}` | 7 days |
| `token:<sha256(token)>` | `{role: "runner" or "admin" or "device", cid (device only), name, created, revoked}` | none |
| `issue:<cid>:<date>` | PDF bytes; metadata `{date, etag, size, pages, updated, style, length, lang}` | 30 days |
| `issue:<cid>:<date>:p<N>` | PNG preview of page N (1872 x 1404); metadata `{sha256, size}` | 30 days |
| `issue:<cid>:<date>:json` | the issue content (stories, sources, why-you lines, the masthead line) for the text view | 30 days |
| `issues:<cid>` | JSON index, newest first, at most 60 entries: `{date, pages, size, etag, published, emailed_at, opened_at}` | none |
| `latest:<cid>` | `{date, etag}` for the device pull | none |
| `job:<cid>:<date>` | `{state: "due" or "running" or "done" or "failed", due_at, claimed_at, finished_at, attempts, late, reason, usage: {input_tokens, output_tokens, cache_read_input_tokens}, cost_estimate_usd, duration_ms, num_turns, model, email: {sent_at, message_id, attempts, error}}` | 60 days |
| `jobs:open` | JSON array of `{cid, date, state, due_at, attempts}` for jobs not yet done or failed twice (the runner reads this, never lists) | none |
| `events:<cid>:<date>` | `{opened_at, views: ["page", "text"], clicked: [urls], feedback: "one line from the client"}` | 90 days |
| `feeds:<topic>` | curated feed list for a topic: `[{url, title, lang}]`, seeded from the repo, uploaded by admin | none |
| `config:launched` | `"0"` or `"1"`: the launch flag (gate 3). Absent means `"0"`. | none |
| `stats:<date>` | `{issues_due, done, failed, late, opened}` aggregated by the cron at the end of the day, for the Phase 2 hub status tool | 400 days |

Profile fields in `client:<cid>` (plan section 6, made exact):

- `cid`, `email`, `status` (`invited`, `active`, `paused`, `cancelled`), `created`, `last_login`.
- `masthead_name`: the name printed on the masthead, 2 to 40 characters.
- `lang`: `en`, `es`, `ca` or `fr`. UI language and issue language, one value. Phase 0 accepts only `en` (D-009: all issues in English); the other three stay in the schema and are switched on in build step 6, after a partner who speaks the language has proof-read a test issue. Paul reads French and Spanish as well as English; his issue is in English until then.
- `city`, `country`, `lat`, `lon`, `tz` (IANA name). The Worker resolves city to coordinates and timezone at onboarding with the open-meteo geocoding API, no key needed (https://open-meteo.com/en/docs/geocoding-api); the client confirms the match.
- `cadence`: `daily` or `weekly`; `weekly_day` (`mon` to `sun`, weekly only); `ready_by`: local time `HH:MM`, default `07:00`.
- `length`: `short` (1 page), `standard` (2 pages), `long` (3 pages, weekly only). `style`: `newspaper`, `letter`, `brief`. Phase 0 ships `newspaper` and `standard`; the other values are accepted and shown as "coming" in the form until the templates exist (build order step 6).
- `topics`: 1 to 8 ids from the pick list (`defence-naval`, `ai-robotics`, `hardware`, `art-history`, `birds-nature`, `local-news`, `business`, `science`); `feeds`: up to 10 client URLs (RSS, Atom or a news page), each checked once at save time by the Worker (fetches the head, must answer 200 and parse, 1 subrequest each); `notes`: free text up to 600 characters ("what I care about, what I never want to read").
- `delivery`: `{email: bool, web: true, device: bool}`. `email` defaults to `true` (D-009: the MVP delivers the PDF by email) and goes to the address in `email`; the client can switch it off in the form and read on the web only. `device` is for an e-ink reader (Oscar only in Phase 0; neither partner has one).
- `consent`: `{privacy_version, accepted_at}`.
- `health_section`: always `false` in Phase 0 (plan section 5: no health block unless a client opts in with their own data, which needs its own design).
- `auto`: rewritten by the pipeline from the client's reading, never by the client: `{topic_weights, clicked_domains_14d, last_rewritten}`. This is the product's version of `profile.md`'s auto block.

Writes per client per issue day, counted: cron creates the job (1, plus 1 on `jobs:open`), runner claims (1), uploads PDF (1), previews (2 or 3), JSON (1), index (1), latest (1), job done (1, plus 1 on `jobs:open`), emailed (1 on the job, 1 on the index), reader events (1 to 3). At most 17. Three clients: 51 writes a day against the 1,000 cap. The arithmetic ceiling on the free plan is 58 daily clients at 17 writes each; a bigger Phase 3 needs the Workers Paid plan ("a minimum charge of $5 USD per month for an account", https://developers.cloudflare.com/workers/platform/pricing/). Every PUT writes only when the bytes changed (same-hash short-circuit, as `oscar-digest` does for plates).

## 4. Worker routes

Conventions: JSON bodies, `cache-control: no-store` on every API answer, `x-robots-tag: noindex, nofollow` on everything while `config:launched` is `0`, and on `/app`, `/i`, `/d`, `/r`, `/a` always. Unknown paths answer 404. Every POST and PUT from the browser must carry `x-requested-with: digest` (CSRF, together with `SameSite=Lax`). Methods not listed answer 405.

Public, no auth:
- `GET /`: when launched, the landing page (static). Before launch, the private-preview page: one sentence and the invite code field, nothing else about the product.
- `GET /privacy`, `GET /imprint`: static, same gating.
- `GET /i/<code>`: invite link. Valid, unexpired, unused code: marks it used, creates a session, sets the cookie, redirects to `/app/onboarding` (profile incomplete) or `/app` (complete). Anything else: a plain page "This invite link is not valid any more. Ask the person who invited you for a new one."
- `POST /i`: `{code}` from the preview page's field, same effect as the link.
- `POST /signup` (launched only): `{email, lang}`. Creates `client:<cid>` with status `invited` and the email key; no welcome email is sent in Phase 1 (a product mail service is Phase 2, section 7a). Oscar sees the request in `GET /a/clients` and hands out an invite himself. Answer: "Thanks, you will hear from us."
- `GET /health`: `{ok, version}`.

Session (cookie `__Host-sid`, HttpOnly, Secure, SameSite=Lax, 90 days; the Worker looks up `session:<sha256(sid)>`, refuses if expired or the client is `cancelled`):
- `GET /app` and `GET /app/*`: the app shell (static, one HTML file; routes are client-side).
- `GET /api/me`: the profile without `auto`'s internals, plus `{has_device_token, issues_count, next_issue_due}`.
- `PUT /api/me`: the editable profile fields, validated (lang in the set, tz a known IANA name, times `HH:MM`, topics ids in the list, feeds checked, `masthead_name` length). Saves and updates `clients:index`. Returns the saved profile. Setting `status: "paused"` or `"active"` goes through here too.
- `GET /api/issues`: `issues:<cid>`.
- `GET /api/issues/<date>.pdf`, `GET /api/issues/<date>/p<N>.png`, `GET /api/issues/<date>.json`: the issue, this client's only. ETag and 304 as `oscar-digest` does.
- `POST /api/issues/<date>/events`: `{opened, view, clicked, feedback}`, merged into `events:<cid>:<date>`; sets `opened_at` on the index entry once.
- `POST /api/device-token`: creates a device token bound to `cid` (role `device`), returns it once in clear with the pull instructions; a second call revokes the old one. `DELETE /api/device-token`: revokes.
- `GET /api/export`: the profile, index and events as one JSON file (data portability).
- `POST /api/account/delete`: `{confirm: "delete"}`. Sets `cancelled`, deletes the session, the email key, device tokens, `issues:<cid>`, `latest:<cid>` and every `issue:<cid>:*` and `events:<cid>:*` key it can reach from the index (the TTLs catch anything missed), and removes the client from `clients:index`. Answer: a plain goodbye page.
- `POST /api/logout`.

Device (bearer token, role `device`, bound to one `cid`):
- `GET` or `HEAD /d/latest.pdf`, `GET /d/latest.json`: identical semantics to `oscar-digest`'s `/latest.pdf` and `/latest.json` (ETag is the PDF's SHA-256 prefix, `last-modified`, 304 on `if-none-match` or `if-modified-since`), scoped to the token's client.

Runner (bearer token, role `runner`, the box):
- `GET /r/jobs`: `jobs:open` with each job's profile attached (one read per job).
- `POST /r/jobs/<cid>/<date>/claim`: `due` becomes `running` with `claimed_at`; 409 if already running and claimed less than 60 minutes ago (a crashed run is reclaimable after that).
- `PUT /r/issues/<cid>/<date>.pdf` (body PDF, 1 KB to 20 MB, must start with `%PDF-`), `PUT /r/issues/<cid>/<date>/p<N>.png` (PNG signature, 5 KB to 3 MB), `PUT /r/issues/<cid>/<date>.json` (validated against the issue schema). Same bytes again answer `unchanged` without a write.
- `POST /r/jobs/<cid>/<date>/done`: `{pages, usage, cost_estimate_usd, duration_ms, num_turns, model}`. Requires the PDF, the previews for every page and the JSON to be present (409 otherwise). Updates the index, `latest:<cid>`, the job and `jobs:open`.
- `POST /r/jobs/<cid>/<date>/failed`: `{reason}`. `attempts` increments; below 2 the job returns to `due` at once. At 2 it becomes `failed` with `late: true`, and the reader shows Oscar's text, "Today's issue is running late. We're on it." (section 5). The cron puts a `failed` job back to `due` once an hour until 4 further attempts have been used or the client's local 18:00 has passed, whichever is first, so the text stays true; after that the job stays `failed`, leaves `jobs:open`, and the text stays on the reader until the next issue replaces it. No email is sent for an issue that never finished.
- `POST /r/jobs/<cid>/<date>/emailed`: `{sent_at, message_id}` or `{error, attempts}`. Records the email result on the job and `emailed_at` on the index entry. The Worker refuses it before `done`.
- `PUT /r/clients/<cid>/auto`: the rewritten `auto` block.

Admin (bearer token, role `admin`, box CLI only, never a browser):
- `POST /a/clients`: `{email, lang, note}` creates an `invited` client and returns an invite link. `POST /a/clients/<cid>/invite`: a fresh invite link for an existing client (new device, lost session). `GET /a/clients`: the list with status, last login, issues delivered, last emailed, last open. `POST /a/clients/<cid>/pause`. `PUT /a/feeds/<topic>`. `PUT /a/config/launched` (`{value: "1"}`): this call is gate 3 and is made only after a D-### yes. `GET /a/status`: the aggregate the Phase 2 hub tool will expose.

Cron, one trigger (`*/15 * * * *`, 1 of the account's 5; the build session checks in the dashboard how many the hub Worker and `oscar-digest` already use): reads `clients:index`; for every `active` client computes the local date and time with `Intl.DateTimeFormat` in the client's `tz` (DST-safe, as `madridDate` does today); an issue is due when the local time is within `lead` minutes before `ready_by` on an issue day (every day for `daily`; `weekly_day` for `weekly`) and no `job:<cid>:<local date>` exists. `lead` is a Worker variable, 180 minutes at first: the runner's longest run is capped at 25 minutes per client (section 6) and the three clients run one after another. Creates the job `due` and appends to `jobs:open`. A fresh `active` client with no issue yet gets a job for the next local date at once, so the first issue arrives within one runner cycle after onboarding, whatever the hour. At 23:50 UTC the same cron writes `stats:<date>`.

Rate limiting: invite codes and session ids are 32 random bytes, so guessing is impractical; Phase 0 adds no counter (each counter hit would cost a KV write). Whether a free-plan WAF rate-limiting rule is available for `/i` and `/signup`: I don't know; the build session checks the dashboard and adds one if it is free.

Tests (`node --test test/`, mock KV, no network, as today): every route's auth paths (no token, wrong role, revoked, other client's session); invite single use and expiry; session expiry and cancelled client; profile validation (bad `tz`, bad `lang`, `lang` other than `en` refused in Phase 0, 11 feeds, 41-character name); upload size and signature checks; ETag 304 on all three device and session PDF routes; `done` refused without previews; `emailed` refused before `done`; the late-issue schedule (back to `due` at once below 2 attempts, hourly after, stop after 4 further attempts or local 18:00); cron due computation at `ready_by` 07:00 for `Europe/Madrid` (all three Phase 0 readers), `Europe/London`, `America/New_York` across the DST change dates of 2026 and for weekly on the chosen day only; no duplicate job on a second cron tick; the write count per client per issue day asserted at or under 17; a cancelled client's keys gone.

## 5. The customer journey, screen by screen

Design rules: `playbooks/design.md` and the `frontend-design` skill in the build session. Typography carries it, taken from the newspaper itself: Playfair Display for heads, Source Serif Pro for text, IBM Plex Sans Condensed for labels, self-hosted from the pipeline's `fonts/`. Black, white, four greys and one accent. A real grid, generous white space, no gradients, no glows, no stock art. Real copy and the real sample pages from the Phase 0 issues (the plan's ten personal issues are not used as samples: they are Oscar's data). Mobile first for the reader, since the partners read on phones (Paul and Pietro, Barcelona, no reading device). The email with the PDF is what the partners open first; the reader is where they come back for the archive, the settings and the feedback line. Every screen is in English in Phase 0 (D-009); the string files for `es`, `ca` and `fr` are build step 6, proof-read by Paul for French and Spanish before a partner sees them. Oscar's standing feedback applies (`/home/box/AgentConfig/docs/OSCAR-FEEDBACK.md`): no em dashes, no estimates, nothing shown as done that was not checked on a real device.

1. Landing (`/`, static; Phase 1 public, Phase 0 replaced by the private-preview page). Above the fold: the masthead of a real sample issue with a client's first name on it, one sentence saying what it is (a newspaper laid out for one reader, from the topics they choose, every morning), and two actions: "Request an invite" (email field, `POST /signup`) and "I have an invite" (code field). Below: three sample issues as pages (PNG) and PDF, "How it works" in three short steps (tell us what you read, we make your paper overnight, it is ready by seven), what it costs ("Free for the first month; the price is announced before anything is charged", until the partners set the price), the privacy promise in two sentences with a link, and the imprint. Nothing about AI models by name; the page says the issues are written by a language model and checked by rules, in one sentence, because clients will ask.
2. Invite (`/i/<code>`). No screen of its own on success; the client lands in onboarding already signed in. Failure page as in section 4.
3. Onboarding (`/app/onboarding`, one page, one column, under five minutes, saved with one `PUT /api/me`). Order and defaults:
   - Your name on the masthead (live preview of the masthead with today's date, drawn as SVG from the name, so the client sees their paper before anything else).
   - Language: English in Phase 0, shown as the single value with "Spanish, Catalan and French coming" (D-009). When the other three are switched on, four choices and the UI switches at once.
   - City (text; the Worker suggests matches from open-meteo; the client confirms one; shows the resolved timezone in words: "Your paper will be ready at 07:00 Paris time").
   - Cadence and time: daily or weekly (day picker); ready by (default 07:00).
   - Length and style: three lengths, three styles, each with a thumbnail; the ones not built yet are shown greyed with "coming", not hidden, so the choice set stays what the plan promised.
   - Topics: the eight pick-list tiles; "Add a feed or site" field (checked on save; a bad URL is reported inline, not silently dropped); the free-text "What I care about, what I never want to read".
   - Delivery: email, on by default, to the address shown ("Your issue arrives as a PDF, from Oscar's address, by 07:00"); web (always on); e-ink device (explained in one line, set up later from the account page).
   - Privacy consent: one checkbox with the two sentences and the link; required.
   - Submit: "Your first issue is being made. It will be in your inbox in a couple of hours, or by 07:00 tomorrow." The runner's cycle decides which; the reader shows the live state.
4. Reader (`/app`, opens the newest issue). Page view: the PNG pages one under the other, fit to width, pinch-zoom, a "Download PDF" link, page dots. Text view (toggle, remembered): one column built from the issue JSON: masthead line, then each story as headline, body, the source link, the "why you" line; this is the phone-friendly reading mode and the first form of the `letter` style. Every click on a source link and every open sends `POST /api/issues/<date>/events`. Under the issue: "What was wrong today?" one-line box (saved as `feedback`), which is how the plan's "what each one asked to change" gets measured. States: "Being made" (job `running` or `due` before any failure), "Today's issue is running late. We're on it." (job `failed` or re-queued after two failed attempts; Oscar's text, 2026-11-12; the technical reason stays in the job record and in `GET /a/clients`, never on the reader), "Paused".
5. Archive (`/app/archive`): the last 30 days as a list (date, pages, emailed or not, opened or not), tap to open. Older issues are gone and the page says so ("Issues are kept for 30 days").
6. Preferences (`/app/settings`): the onboarding form, prefilled, same validation; "Changes apply from your next issue"; pause and resume.
7. Account (`/app/account`): email (read-only in Phase 0, with "to change it, ask the person who invited you"; the issue email goes here while delivery by email is on); e-ink device: "Create a device token" shows the token once with the exact pull URL and the BOOX steps, "Revoke"; "Download my data" (`GET /api/export`); "Sign out"; "Delete my account" (type "delete", explains that the profile and issues go at once, and that nothing is kept); link to the privacy page. Signing in on another device in Phase 0: the page says plainly "Ask Oscar for a new invite link"; Phase 2 replaces this with a magic link by email.

## 6. The per-client pipeline (the box, `/workspace/digest-product/`)

Entry point `runner.sh`, a loop in the style of `/workspace/digest/whoop-morning-watch.sh` (the box has no cron): every 10 minutes, `GET /r/jobs`, one job at a time, oldest `due_at` first, a lock file so a second start exits, `--status` and `--stop`, log `logs/runner-<date>.log`. For each job, five programs, each separately runnable by hand with `<cid> <date>` so a failure is visible and retryable:

1. `gather.py`. Fetches the profile from the Worker (the only input about the person). For each topic, the curated feeds from `feeds/<topic>.json` in the repo plus the client's own feeds; entries from the last 48 hours; deduplicated by URL and by near-identical title; capped at 60 candidates with title, URL, published time, feed title, the first 400 characters of the entry text, language if the feed says. Weather and sunrise for `lat, lon` from open-meteo (no key, as today), the moon phase from `lib/`. Writes `work/<cid>/<date>/sources.json` and `profile.json`. Public sources only; nothing from the hub, the vault or any X export; nothing from another client's directory.
2. `write.sh`. One Claude Code run on Oscar's login:
   ```
   timeout 25m claude -p "$(render_prompt WRITE-PROMPT.md)" \
     --model opus --effort high \
     --output-format json --json-schema issue.schema.json \
     --tools "Read,WebFetch" --allowedTools "Read,WebFetch" \
     --permission-mode dontAsk --permission-prompts none \
     --max-turns 40 \
     --append-system-prompt-file HOUSE-RULES.md > "logs/claude-$CID-$DATE.json"
   ```
   The working directory is `work/<cid>/<date>/`, so `Read` sees only this client's files. No `--bare` (it would not use the subscription login; see section 1). No `--continue` or `--resume`: every issue is a fresh session, so nothing of one client's run reaches another. Model and effort follow the house rule (every Claude Code call at least high effort; Opus for builds). `--json-schema` makes Claude Code return the issue as `structured_output` validated against `issue.schema.json` (https://code.claude.com/docs/en/headless, "Get structured output"); if the field is absent the run counts as failed. The result JSON's `usage`, `total_cost_usd` (Claude Code's client-side estimate of what the run would cost on the API, labelled as such; on the subscription the money is zero, but it is the number the later cost-per-issue question needs), `duration_ms` and `num_turns` go into the job's `done` call. The prompt `WRITE-PROMPT.md` is the generalised `DAILY-PROMPT.md`: pick 4 to 6 stories (standard) from `sources.json` only, write in `lang`, within the copy budget the renderer enforces for the length, one "why you" line per story built only from the profile's topics and notes, never a guess about the person; cite only URLs that are in `sources.json`; `WebFetch` only to open a cited URL once and check it resolves; no em dashes; no invented numbers; no estimates. `HOUSE-RULES.md` repeats the text rules and the gates (never send, post, sign up, pay, contact anyone).
3. `validate.py`. Refuses the issue when: any story source is not in `sources.json`; any em dash; copy over the budget for the length; a story without a source; any other client's `masthead_name` or email appears in the text (the runner holds no admin token, so the Worker's `GET /r/jobs` answer carries the list of all masthead names and email local parts for this check and nothing else about the other clients); the language check fails (the run's own `lang` field in the structured output must equal the profile's). On the first refusal the runner re-runs `write.sh` once with the validator's message appended to the prompt; on the second it reports `failed` with the reason.
4. `render.py` and `upload.py`. `render.py` is `build_page3.py` and `lib/render.py` generalised: masthead with the client's name, the client's language strings, the newspaper template at the house page size (8.2467 x 6.1850 in, 1872 x 1404 px at 227 dpi, so the e-ink pull is 1:1 and the PNGs are the reader's pages), fit pass, overflow probe, `pdfcraft-cli check`, em dash check, previews (PNG; the e-ink previews are not needed for clients). Then `upload.py` PUTs the PDF, the previews and the JSON, and POSTs `done`; on any failure before `done`, POSTs `failed` with the reason. Writes `work/<cid>/<date>/status.json` like `out/status-<day>.json` today.

5. `send.py`. Runs only after `done` was accepted and only when the profile's `delivery.email` is `true`. Builds one message per client, never several recipients on one message: `From` Oscar's Gmail address, `To` the client's address, subject "Your issue, <weekday> <day> <month> <year>" (the product has no name yet; the subject changes with the Phase 1 name), a plain-text body of three lines (the masthead line, "Open the reader: <link to /app>", "Reply to this email with what was wrong today"), and the PDF attached as `issue-<date>.pdf`. Sends through `smtp.gmail.com`, port 587 with STARTTLS, authenticated with the address and the app password from `gmail.env` (Google's SMTP page: "Port 25, 465, or 587", app password required, "The sending limit is 2,000 messages per day" for Workspace accounts, https://knowledge.workspace.google.com/admin/gmail/send-email-from-a-printer-scanner-or-app; for a personal Gmail account the limit is 500 emails a day, https://support.google.com/mail/answer/22839). Attachment ceiling for personal Gmail: "the limit is 25 MB" (https://support.google.com/mail/answer/6584); the personal Digest's two-page PDFs measured on the box today are between 145 KB and 279 KB, so the product's PDFs fit with room. On an SMTP error the script retries three times, ten minutes apart, then POSTs `emailed` with the error; the issue stays readable on the web and the reader shows nothing about the email. Three readers means three messages a day, against a 500-a-day limit. The script writes nothing but the job record and `logs/send-<date>.log` (date, cid, message id or error; never the address, never the body).

Then, once a day after the last job, `profile_auto.py` rewrites each client's `auto` block from the last 14 days of events (`GET` through the runner's job answers; the Worker includes the client's events in the job payload) and PUTs it to `/r/clients/<cid>/auto`. Topic weights only; no text of what was read is kept outside the events keys.

Oscar as client 1 (confirmed 2026-11-12): he is onboarded through the real journey like the partners, so he reads what they read, and his own product issue arrives in his Gmail inbox from his Gmail address. His personal Digest keeps running separately on `/workspace/digest`.

Subscription behaviour, measured not assumed: the runner records, per run, duration, usage, `num_turns` and any `api_retry` event with error `rate_limit` from the transcript (field names from https://code.claude.com/docs/en/headless, "Handle API retries"). On a rate limit the job goes back to `due` without counting an attempt and the runner sleeps 30 minutes. The limits of Oscar's plan are not known to me; four weeks of these numbers answer whether three daily issues fit beside the personal Digest and the HQ runs on the same login.

Logs and transcripts: `logs/claude-<cid>-<date>.json` holds a client's content; kept 30 days, chmod 600, never copied into the repo or a note. Tokens are logged to the job record only, never printed to a chat.

## 7. Delivery

- Email, the MVP's delivery (D-009): the PDF attached plus the reader link, one message per client, sent by `send.py` on the box from Oscar's own Gmail account after `done` (section 6, step 5). The only emails the system sends are issue emails to clients who have `delivery.email` on; no welcome mail, no "your issue is ready" without the issue, no invite mail. Oscar hands the invite links to the partners himself, in person or from his own account. Replies to an issue email land in Oscar's own inbox, which is where the partners' "what was wrong" will arrive in practice.
- Web: the reader (section 5). The issue is "delivered" when `done` lands; the reader polls `GET /api/issues` every 60 seconds while it shows "Being made" or the late text.
- E-ink pull: `GET /d/latest.pdf` with the client's device token, the same contract the BOOX app already implements for Oscar (`DigestSync.kt` reads a URL and a token). In Phase 0 only Oscar has such a device (Paul and Pietro have none); the account page's instructions are written for the BOOX app and say that other readers can open the PDF in any PDF app.

## 7a. A mail service of the product's own: the later decision, prepared

Not approved and not needed for Phase 0 (D-009: no mail service sign-up). It becomes a decision when one of these is true: the issues should come from a product address instead of Oscar's; the Gmail route is restricted or its 500-a-day limit is in sight; or Phase 1 puts the site live and sign-ups need a welcome mail. Prices quoted on 2026-11-12 from the vendor pages, in the currency shown; the sign-up is gate 2 in every case.

| Option | Free allowance | First paid tier | Attachment limit | Source |
|---|---|---|---|---|
| Resend | 3,000 emails a month, 100 a day, 3 domains | USD 20 a month for 50,000 | 40 MB per email after base64 | https://resend.com/pricing and https://resend.com/docs/api-reference/emails/send-email |
| Postmark | 100 emails a month, no overages | Basic, USD 15 a month, 10,000 emails | 10 MB total message | https://postmarkapp.com/pricing and https://postmarkapp.com/developer/user-guide/send-email-with-api |
| Mailgun | 100 emails a day | Basic, USD 15 a month, 10,000 emails | not quoted on the pricing page | https://www.mailgun.com/pricing/ |
| Mailjet | 6,000 a month, 200 a day | Starter, USD 9 a month, 8,000 emails, no daily cap | not quoted on the pricing page | https://www.mailjet.com/pricing/ |
| Amazon SES | up to USD 200 of AWS Free Tier credits for a new account, usable for 6 months | USD 0.10 per 1,000 emails à la carte, plus USD 0.12 per GB of attachments; sandbox accounts send 200 a day to verified addresses only until approved | 40 MB per message (v2 API or SMTP) | https://aws.amazon.com/ses/pricing/ and https://docs.aws.amazon.com/ses/latest/dg/quotas.html |
| Cloudflare Email Sending (beta) | none on Workers Free: "Sending to arbitrary recipients requires the Workers Paid plan" | Workers Paid, minimum USD 5 a month, 3,000 emails a month included, USD 0.35 per 1,000 after | 25 MiB total message, 32 attachments | https://developers.cloudflare.com/email-service/, https://developers.cloudflare.com/email-service/platform/pricing/, https://developers.cloudflare.com/email-routing/email-workers/send-email-workers/ |
| Proton Workspace (SMTP access for external tools) | none | Standard USD 8.99 a user a month on the yearly rate (USD 14.99 standard price); Premium USD 14.99 (USD 24.99) | not quoted | https://proton.me/business/plans |
| Gmail, Oscar's own account (the D-009 route) | 500 emails a day, 25 MB per message | none, already paid for | 25 MB | https://support.google.com/mail/answer/22839 and https://support.google.com/mail/answer/6584 |

Not fetched this run: Brevo (the pricing page returned no body text) and Twilio SendGrid (the pricing URL redirects in a loop); both would need a second look before the memo. My recommendation for that memo, as cofounder (opinion): Cloudflare Email Sending if it has left beta by then, because the Worker already lives there and USD 5 a month covers the Workers Paid plan the KV write cap will need anyway; otherwise Resend's free tier, which covers 100 a day. Either way the sender becomes a product domain with SPF and DKIM set in the same Cloudflare zone.

## 8. Auth and security

- Invite codes and session ids: 32 random bytes (`crypto.getRandomValues`), base64url, stored as SHA-256; invites expire after 7 days and are single use; a used invite creates a new session and never reopens.
- Cookie `__Host-sid`: HttpOnly, Secure, SameSite=Lax, Path `/`, 90 days; refreshed on use once a day (one write) rather than on every request.
- CSRF: SameSite=Lax plus the `x-requested-with: digest` header on every state-changing browser call; the Worker rejects a state change without it.
- Tokens for runner, admin and device: random, hashed, role-scoped, revocable by flag, created by `tokens.sh new <role> [cid]` on the box (writes the hashed record through the admin route for device tokens, or straight into KV for runner and admin at setup). The runner token can read jobs and write issues; it cannot read `client:*` directly, create invites, or flip the launch flag. The admin token never leaves the box.
- Isolation: a session reaches only its own `cid`'s keys (every key is prefixed with the `cid` from the session, never from the URL alone); the validator's cross-client name check; per-client work directories; fresh Claude sessions.
- Headers: `content-security-policy` (self only, no inline scripts; fonts and images from self), `referrer-policy: no-referrer`, `x-content-type-options: nosniff`, `x-robots-tag` as in section 4.
- Data: email, city and the profile are the only personal data; issues and events carry 30 and 90 day TTLs; deletion is immediate and complete on the account page, with one stated exception: issue emails already sent sit in the Sent folder of Oscar's Gmail account and in the client's own inbox, and the privacy page says so. The privacy page names the processor (Oscar, until the entity exists) and the sub-processors (Cloudflare for hosting, Anthropic for the writing model, open-meteo for weather, Google for email delivery while issues are sent from Oscar's Gmail).
- The Gmail app password: it grants an app access to Oscar's Google account, not only to sending, so it is treated like the admin token: chmod 600 on the box, never printed, never in a repo, revocable by Oscar at any moment at myaccount.google.com (https://support.google.com/accounts/answer/185833). `send.py` uses it for SMTP only and never opens IMAP. Clients are in the EU (plan section 6); whether a data-processing agreement with Anthropic is needed for a subscription-based product is a question for the regulation role, parked, not a Phase 0 blocker for three friends who know what they are testing.
- Secrets: none bound to the Worker; the box keeps the tokens in chmod 600 files until the vault exists; nothing is ever printed; gitleaks on the product repo as on this one.

## 9. Front-end technology

Static files served as Worker static assets (free, unlimited requests): `public/index.html` (landing), `public/preview.html` (private preview), `public/privacy.html`, `public/imprint.html`, `public/app.html` (the shell), `public/app.js`, `public/app.css`, `public/i18n/<lang>.json`, `public/fonts/`. No framework, no build step: the shell is one HTML file with a small client-side router and `fetch` calls to `/api/*`. Why: the free plan caps Worker invocations at 100,000 a day and nothing else, so everything that can be a file is a file; and a build-free app is what a Claude Code session on the box can change and redeploy in minutes. The masthead preview in onboarding reuses `lib/art.py`'s masthead rules ported to a small SVG function in `app.js` (name, date, the olive sprig), so the client sees the real design.

Accessibility: keyboard reachable, labels on every field, the reader's page images carry the headline list as alt text, text view is plain HTML, contrast at the newspaper's black on paper.

## 10. Test plan

- Worker: the unit tests in section 4, run before every deploy (`node --test test/`).
- Pipeline: `validate.py` tests (foreign URL refused, em dash refused, another client's name refused, over-budget copy refused, missing `lang` refused); `render.py` overflow probe on a long, a short and a standard issue from fixture JSON; one golden run of `write.sh` on Oscar's own profile from a fixture `sources.json`, checked by `validate.py`, before any partner exists (so even the test runs write only for Oscar); `send.py` tested against a local SMTP stub (one recipient per message, PDF attached, size under 25 MB, three retries), and then once for real from Oscar's Gmail to Oscar's own address, with Oscar present, before any partner is onboarded.
- End to end, Oscar as client 1, on the preview hostname: admin creates the client and the invite; Oscar opens it on his phone; onboarding under five minutes (timed); the cron creates the first job; the runner builds, uploads and emails; the PDF arrives in Oscar's inbox and opens on the phone; the reader shows the pages and the text view on the phone; the BOOX pulls `/d/latest.pdf` with a device token (checked on the device, per Oscar's feedback rule); feedback line saved; account export and delete tested on a throwaway second client of Oscar's own.
- Phase 0 measures, reported in the HQ report's Done section each week (a scorecard line only if Oscar approves a scorecard task): issues due, delivered by `ready_by`, late and why; emails sent, SMTP errors, bounces seen in Oscar's inbox; usage and Claude Code's cost estimate per issue (labelled estimate); opens per partner per week; feedback lines; rate-limit incidents; runner uptime (the box being off is the first failure mode, and the reader's late text is the mitigation).
- Exit test (plan section 7): both partners open the issue on most days of week four, and the per-issue usage numbers are known. Otherwise stop; the fork is deleted, the Worker and namespace are deleted (fully reversible, as `oscar-digest` documents), the preview hostname removed.

## 11. Build order

Sessions of Claude Code on the box with Oscar (Opus, effort high or more; no permission-skipping flags), each with a done-when. Nothing in steps 1 to 5 is public, costs money, or creates an account.

1. Worker skeleton: `wrangler.toml`, `worker.js` with the data model, every route in section 4, the cron, the static asset routing, the tests. Done when the tests pass locally. No deploy.
2. Pipeline fork: `/workspace/digest-product/` with `gather.py`, `write.sh` and `WRITE-PROMPT.md`, `issue.schema.json`, `validate.py`, `render.py` (newspaper, standard), `upload.py`, `send.py`, `runner.sh`, `feeds/*.json` seeded from the feeds the personal Digest already uses. Done when the golden run on Oscar's own profile produces a PDF that passes every check, locally, nothing uploaded, and `send.py` passes against the SMTP stub, nothing sent.
3. Private deploy: KV namespace, Worker, custom domain `digest-preview.projetrefonte.com` (confirmed by Oscar 2026-11-12) with `config:launched` absent (preview page only, noindex), runner and admin tokens, Oscar's Gmail app password created by Oscar himself and saved in `gmail.env`, one real test email from his Gmail to his own address with him present, then the runner loop started. Done when `/health` answers and Oscar's own end-to-end run in section 10 passes in his inbox, on his phone and on the BOOX.
4. The app, polished: onboarding, reader with both views, archive, settings, account, feedback, the English string file, the privacy and imprint pages (text to be approved by Oscar before any partner sees them; drafts only). Done when Oscar has used every screen on his phone and listed what to change, and that list is done.
5. Partners: Oscar creates the two clients with Paul's and Pietro's addresses (entered by him, never written in this repo) and hands the two invite links himself. The runner serves three clients; three issue emails a day leave his Gmail. Four weeks of measurement. Done when week four's exit test is read.
6. During the four weeks, if time allows and never ahead of a partner's request: the `letter` and `brief` styles, the `short` and `long` lengths, Spanish, Catalan and French (Paul proof-reads French and Spanish; Catalan waits for a reader who speaks it), the `api` writer backend written but not configured (so the swap is ready if Oscar changes his mind or the subscription route stops working; using it is a gate 2 decision).

Decisions this build will raise later, not now: Phase 1 domain purchase (gate 2) and launch flag to `1` (gate 3); a mail service of the product's own (gate 2, section 7a) and Stripe (gate 2) in Phase 2, and the hub status tool; any API key use (gate 2).

## 12. Risks and unknowns, stated once

- Terms. The subscription route is the one Anthropic's Claude Code legal page says is not permitted for third parties' use (https://code.claude.com/docs/en/legal-and-compliance). Oscar chose it knowing that. Two consequences the build must live with: if Anthropic restricts the account, Phase 0 stops and the `api` backend plus a spend decision is the way back; and the same login runs Oscar's personal Digest and the HQ runs, so a restriction would hit those too. I do not know how or whether Anthropic enforces this. Said once; his call.
- Subscription limits are not published in a form I could cite for Oscar's plan; the runner measures them.
- The box is a single point of failure for the pipeline and has no cron; the loop pattern already runs the WHOOP watch, and the reader's honest "no issue today" line is the fallback. Moving the pipeline to an always-on machine is a Phase 2 question.
- KV writes: 1,000 a day on the free plan caps the product at 66 daily clients by arithmetic; Phase 3 needs the paid plan.
- Cloudflare Access as an extra layer on the preview hostname: the free plan's user allowance is not stated on the pages I read (https://www.cloudflare.com/plans/zero-trust-services/ and https://www.cloudflare.com/plans/free/), so the spec does not depend on it; the app's own invite and session model is the gate.
- Gmail as the sender: Oscar's personal address is the product's face for three friends, which is fine for a test and wrong for a stranger; the 500-a-day limit is far away at three readers; Google can ask for a new app password or block automated sending without notice, and I do not know how Google treats a personal account that sends the same automated message daily. If Gmail stops, the issue is still on the web and the reader says nothing wrong; the fix is the section 7a decision. Deliverability to Paul's and Pietro's providers is unknown until the first week; a message landing in spam is the first thing to check with them.
- All three readers are in `Europe/Madrid`, so the DST and timezone tests in section 4 are the only place other zones are exercised until a client elsewhere exists.
- Proof-reading of the non-English issues depends on a partner who speaks the language; Phase 0 is English only (D-009), and Paul covers French and Spanish in build step 6.
- A data-processing agreement question for EU clients is parked for the regulation role before Phase 3.

## 13. Inputs from Oscar: answered 2026-11-12, 15:09 Madrid, via Cofounder, relayed by Vela

- The two partners: Paul (French, Spanish and English; Barcelona; no reading device) and Pietro (English; Barcelona; no reading device). Their email addresses are entered by Oscar when he creates the clients and never written here.
- Hostname: `digest-preview.projetrefonte.com` is fine.
- Oscar reads a product issue of his own as client 1: yes.
- The text clients see when an issue fails: "Today's issue is running late. We're on it." (applied in sections 4 and 5, with the retry schedule that keeps it true).
- Added the same day (D-009, 15:11): delivery is a PDF by email from Oscar's own Gmail, no mail service sign-up, all issues in English.

No input is open. The next thing the build needs from Oscar is a live session on the box for step 1.

## Pointers (one home per fact)

- The plan this follows: `ventures/digest/plan.md`. The decisions: `ventures/_company/cofounder/decisions.md` (D-008 and D-009 lines) and `queue/2026-11-12-001`. The tasks for this spec: `queue/2026-11-12-002` (first version) and `queue/2026-11-12-003` (Oscar's answers and email delivery).
- The one-reader pipeline this forks: `/workspace/digest/README.md`. The Worker this reuses: `/home/box/projects/oscar-digest/README.md`.
- Hub rule: client data lives in the product Worker's KV, outside the personal hub; the For Vela line is in plan section 4.
