# Digest beta: the Worker and the setup page (draft, not deployed)

Written 2026-11-16 by the HQ evening run for task `queue/2026-11-16-004`. This is the cloud half of `beta-plan.md` section 2 (build session 3), written ahead of the box sessions because the page was asked for now and the box is not reachable from a cloud run. Nothing here is deployed, bound to an account or reachable from the internet. The deploy waits for Oscar's typed yes in session 3.

| File | What it is |
|---|---|
| `public/form.html` | The setup page, one static file with its script. Fields and wording from `../questions.md` section 4. Fonts are expected under `public/fonts/` (copied from the pipeline's `fonts/` in session 3, not in this repo); Georgia and the system sans are the fallback and are what the screenshot below used. |
| `worker.js` | The six routes. KV namespace `DIGEST_BETA`, four key types (`index`, `profile:<hash>`, `status:<id>`, `runner:<hash>`). Security headers and a nonce CSP on the form. |
| `worker.test.mjs` | 28 checks with a mock KV. `node worker.test.mjs`, Node 18 or newer, no install. All pass as of this commit. |
| `wrangler.toml` | The binding names and the hostname, with the KV id left blank on purpose. |
| `new_link.sh` | Makes one secret link on the box, sends only its SHA-256 to the Worker, prints the link once. |

## What the box session still has to do (sessions 1 to 3 in `beta-plan.md`)

1. Session 1 and 2 are untouched by this folder: the fork of `/workspace/digest`, `WRITE-PROMPT.md`, `write.sh`, `validate.py`, `send.py`, `beta-runner.sh`.
2. In session 3, copy this folder into `/workspace/digest-product/worker/`, copy the four font files into `public/fonts/`, run the tests, open `public/form.html` locally with `{{PROFILE_JSON}}` set to `{}` and check it on a phone-width window, then on a phone.
3. Point `beta-runner.sh` at `GET /r/profiles` (bearer token) and at `PUT /r/status/<id>` after each issue: `being-made` when it starts, `sent` with `at_local` as `HH:MM` Madrid when `send.py` returns, `late` after a second failure, `saved` after a profile save with no issue due.
4. Create the runner token on the box (`openssl rand -base64 32 | tr '+/' '-_' | tr -d '='`), store its SHA-256 as `runner:<hash>` with value `1` in the namespace (`wrangler kv key put`), keep the token in a chmod 600 file.
5. Oscar's typed yes, then: KV namespace, `wrangler deploy`, the hostname route. Then `./new_link.sh oscar` and the done-when of session 3.

## What the form does

Saves every field to the phone at once and to the Worker one second after typing stops, so leaving the page loses nothing. The button is the only thing that asks for an issue (`make: true`), three a day per person; a fourth press gets the polite line with a 429. A returning visit opens the optional section, shows the pause checkbox and changes the button to "Make my issue now". A wrong or dead link gets one plain line and a 404.

## Checked

- `node worker.test.mjs`: 28 of 28.
- The page rendered at 390 px wide in headless Chromium with the fallback fonts, looked at as an image: masthead redraws from the name, three fields above the fold line, one button, no horizontal scroll.
- No em dash in either file (a test checks it).

Not checked, and honestly so: on a real phone, with the real fonts, against a real KV, on the real hostname. That is session 3's done-when.
