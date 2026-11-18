# DailyDigest: what the setup page asks, and what it leaves out

Part A of queue task 004 (2026-11-16), the box run's version. Builds on the cut in `beta-plan.md`. "DailyDigest" is a placeholder name.

This is the second of two designs written the same evening by two runs that did not see each other. The repo's current version is `questions.md` (evening cloud run, page in `beta/`). Not kept: Oscar answered the decision "Which DailyDigest setup page to keep (D-017)" in `queue/2026-11-16-004-dailydigest-test-page.md` on 18 Nov 2026 with "Keep A, the evening page", so `questions.md` and `beta/` are the version in force. This file and the page it describes (`/workspace/digest-product/worker/`) stay on disk as a record and are not built on.

Where the two differ:

| | `questions.md` (evening run) | This file (box run) |
|---|---|---|
| Required | Name, city, topics | Name, one topic |
| Topics | One free-text box | Three lines, eight tap-to-fill examples |
| What the reader does | Optional, behind the fold, shares a 600-character box with the never-list | Its own question on the first screen |
| Never-list | Part of that shared box | Its own optional question on the first screen |
| City | Typed, required | Guessed from the connection, editable, behind the fold |
| Sources | Up to 5 URLs | Up to 3 lines of plain text (a site, a newsletter, a name) |
| Masthead | "The <Name> Daily", drawn as SVG | "<Name>'s Digest" in the PDF's blackletter |
| Example name in the field | Paul (a beta reader's name) | Marta |

The page itself: `/workspace/digest-product/worker/form.html` (screenshots in `/workspace/digest-product/dev/shots/`).
The choices below are my judgement, not tested with readers. The beta is the test.

## 1. The final question list (wording as on the page)

First screen, four questions. Only the name and one topic are required.

| # | Question | Under it | Example in the field | Feeds |
|---|---|---|---|---|
| 1 | Whose paper is this? | Your first name. It goes on the masthead. | Marta | The masthead, live as they type: "Marta's Digest" in blackletter |
| 2 | Three things you'd read about even on a busy morning. | Be specific. "Formula 1 engineering" beats "sport". | Formula 1 engineering / New restaurants in Barcelona / AI tools for small companies. Eight tap-to-fill examples below (Startups and venture deals, Electric cars, FC Barcelona, Climate and energy, Space launches, Architecture and design, Wine, Chess) | What the writer searches for |
| 3 | What do you do all day? | One line. Each story comes with a note on why it matters to you, and this is where it comes from. | I run sales for a wine importer in Barcelona | The "why you" line under each story |
| 4 | Anything you never want to see? (optional) | | celebrity gossip, crypto prices | What the writer skips; the validator refuses a headline carrying it |

Behind one fold, "Make it sharper (optional)":

| # | Question | Under it | Example or default | Feeds |
|---|---|---|---|---|
| 5 | Where do you wake up? | For the dateline and for local stories. | Prefilled with Cloudflare's guess from the connection, marked as a guess, editable | Dateline, local angle |
| 6 | Who or what do you already trust? | A site, a newsletter, a writer. Public pages only: nothing to connect, no login. | ft.com / Stratechery / a writer you follow on X (up to three) | Where the writer looks first |
| 7 | How should it sound? | One line that changes with the choice | Straight (default), Analytical, Light | Tone of the copy |
| 8 | Pause my daily issue | Shown only after the first issue | Off | The morning run skips them |

Button: "Make my first issue" (afterwards "Save and make a new issue").
Status under the button: "Your issue is being made. You can close this page." then "Your issue was made at 21:09. It reaches you by email." or "Your issue was sent to your inbox at 21:10." If it fails: "Today's issue is running late. We're on it." No promise of how long it takes.
Small print, two sentences for Oscar to approve or rewrite: "This link is your login. There is no account and no password, so keep the link to yourself." and "What you type here is stored on Cloudflare and read by Oscar and by the language model that writes your paper (Claude, by Anthropic). It is used only to write your paper, and it is deleted when you ask Oscar."

## 2. The cut

Everything that could improve a reader's Digest, and where it went. One line of why each.

### Asked on the page
- First name: the masthead with their name is the product's first proof, and it costs one word.
- Three topics, free text: the one input the paper cannot be written without. Free text because "Formula 1 engineering" is a better brief than a ticked "Sport" box.
- What they do all day: the only honest source for a "why you" line. Without it those lines would be guesses about a person.
- Never-list (optional): one bad story on day one costs more trust than a missing good one.
- City (optional, guessed): the dateline looks made for them, and local stories need it.
- Trusted sources (optional): cheap to type, and it lets the paper open with names they already believe.
- Tone (optional, default Straight): three choices are enough to learn whether tone matters at all.
- Pause: the polite exit. A reader who cannot stop a daily email blames the sender.

### Inferred, never asked
- City: from Cloudflare's connection data, shown as a guess they can change.
- Time zone: from the phone, stored with the answers.
- Date and weekday: from the clock.
- Language: English for everyone in the beta.
- Email address: Oscar already has it. It stays on the box and never reaches the page or the cloud.
- Whether they came back and changed answers: the profile's timestamps say so.

### Asked later, by reply to an issue or in the first week
- "What was wrong with today's issue?": one question after a real issue beats five before it.
- Whether the "why you" lines were right: they can only judge that on a real page.
- Length, and daily or weekly: nobody knows before reading a few.
- Delivery hour: default morning until someone complains.
- More or less of a topic: the three topics can be edited on the page any time, so this is a reminder to do it.
- Language: when a reader asks for Spanish, Catalan or French.
- Reading device (phone, tablet, e-ink, print): matters for the page size, and worth asking once they have seen the PDF.
- Weather on the page: needs the city confirmed first, so it waits one round.

### Dropped for the beta
- Email field: it would put addresses in the cloud for no gain.
- Account, password, magic-link email: the link is the login.
- OAuth connects (X, Google, Pocket, Readwise, Spotify, calendar): the task rules them out, and each one is a consent screen before the first issue exists.
- X handle as a live feed: x.com answers the writer's fetches with a payment-required page (noted in the personal Digest's daily prompt), so a handle is treated as a name to search, typed in the trusted-sources field.
- Goodreads or Letterboxd import: a nice signal for a culture section the beta page does not have.
- Newsletter forwarding address: needs an inbox to receive mail, which is new infrastructure.
- Category checkboxes: they produce the generic paper this is meant to replace.
- Age, industry, job title, seniority: "What do you do all day?" gets more in one line and feels less like a form.
- Layout or style picker, delivery-time picker, language picker: decisions the reader should not have to make before seeing one issue.
- Consent checkbox: two plain sentences next to the button say what is stored and who reads it. Whether that is enough for a wider release is a legal question I have not checked.
- Free-text "anything else?": an open box invites instructions to the writer, and the four questions cover it.

## 3. Connects: now or later

| Connect | Beta | Why |
|---|---|---|
| City for the dateline and local stories | Now, optional, guessed | One field, no third party |
| A site or newsletter they trust | Now, optional, as plain text | The writer opens public pages only |
| X handle | Now only as a name in the trusted-sources field | No API, no login; x.com pages cannot be fetched |
| Weather | Later | Needs a confirmed city and a slot on the page |
| Goodreads, Letterboxd | Later | Public profile pages could be read without login, once there is a culture slot |
| Anything with OAuth or a third-party sign-up | Not in the beta | Ruled out by the task |

## 4. The friction rules, applied

| Rule | On the page |
|---|---|
| First screen asks the minimum | Four questions, two required. Everything else is behind one fold |
| No account, no password, the link is the login | The link key is 32 random bytes; the server keeps only its SHA-256. A wrong link gets one plain line |
| Progress saved on every field | Each keystroke is kept on the phone, and saved to the server a moment after typing stops and when a field is left. "Saved" shows top right |
| Mobile first | One column, text fields at 18 px (no zoom on iPhone), tap targets the width of the screen. Checked at 390 px and 320 px wide in headless Chrome, not yet on a real phone |
| Under two minutes on a phone | A target, not a measurement. Nobody has timed it |
| Sensible defaults | Tone Straight, city guessed, daily issue on |
| Examples in every field | Every field has one, and the topics have eight tap-to-fill examples |
| One clear button | "Make my first issue", full width, black |
| Masthead preview with their name | The top of the page is the masthead, set in the paper's blackletter, changing as they type |

## 5. Open points for Oscar

- The two small-print sentences are a draft. They name Cloudflare, Oscar and Claude by Anthropic.
- The status line says "It reaches you by email." That is only true once sending is switched on (after the Gmail app password). For his own test as reader 1 the PDF is on the box.
- The intro line reads "One page, every morning, written for one reader. Four questions and it is yours." Change freely.
- The example name is "Marta", chosen so that no beta reader sees his own name or the other's in the field.
