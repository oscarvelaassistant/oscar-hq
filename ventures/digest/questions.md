# DailyDigest setup: the questions, the cut, the final wording

Written 2026-11-16 by the evening run (task `queue/2026-11-16-004`), on top of `beta-plan.md` section 2. "DailyDigest" is Oscar's placeholder name and is used on the page. The page itself is `beta/form.html`; this file is the reasoning behind every field on it and every field left off it.

The one rule that decided everything: the page is opened once, on a phone, by someone who did not ask for it. Every field it asks for has to pay for itself in the first issue, or it goes. The writer (one `claude -p` run with web search, `beta-plan.md` section 2) can look things up; it cannot look up what the reader cares about. So the page asks only for what the writer cannot find, and infers or searches for the rest.

## 1. Everything that could improve an issue

Grouped by where it ends up. One line of why each.

### Asked on the page (first screen, required)

| Question | Why it is asked, and why first |
|---|---|
| Your first name, as it goes on the masthead | Drawn live into the masthead preview above the form. It is the reward for typing the first field, and the writer uses it nowhere else. |
| Where you wake up (city) | Timezone for "ready by 07:00", the weather line, and local stories the reader would not search for. One free field, no picker: open-meteo's geocoder resolves it on the box, so a typo costs nothing on the page. |
| Three things you would read about even on a busy morning | The main input. Free text, concrete prompt, tappable examples that append to the field. Three forces a choice; a reader who types eight is not refused. |

### Asked on the page (second screen, optional, with defaults)

| Question | Why it is asked, and why optional |
|---|---|
| What you do, what you are working on right now, what you never want to read | The "why you" lines are built only from this and the topics (`beta-plan.md` section 2). The "never" clause is the cheapest quality lever there is: one line removes a whole class of wrong stories. Up to 600 characters, with the count shown. |
| How it should read: straight, analytical or light, one sample sentence each | A tone is one prompt variable and changes how the issue feels more than any layout choice. Default: straight. |
| Links you already read (up to 5 URLs) | Public pages the writer can open: a newsletter archive, a blog, a site, a public profile. Optional, hidden behind "Add links", because a URL field on a phone is the slowest field there is. |

### Inferred, never asked

| Fact | From | Why not asked |
|---|---|---|
| Timezone, country, language of local sources | The city, through open-meteo's geocoder on the box | A timezone picker is the field most often filled in wrong. |
| Weather | City, open-meteo | Same. |
| Email address | Oscar types it into `recipients.json` on the box (`beta-plan.md` section 1) | The email field is where sign-up pages lose people, and the only field that makes a form worth attacking. The beta has neither. |
| Language of the issue | English, fixed by the email delivery decision (D-009) | Nothing to choose. |
| The reader's name in the greeting, the date, the issue number | The profile and the runner | Nothing to type. |
| Which story the reader opened | Not inferred: the beta has no reader page and no tracking (`beta-plan.md` section 1) | Asking is cheaper than tracking with three readers. |

### Asked later, not on the page

| Question | When | Why later |
|---|---|---|
| "Reply with the one story that was wrong for you, and the one thing you wanted and did not get" | The last line of every issue email | A reader can only answer it after reading an issue, and the reply lands in Oscar's inbox, where the review reads it. |
| Which of your three topics should get the most space | After the first week, in the review | The first issues show it better than the reader can predict it. |
| Daily or weekly, and at what hour | The review (`beta-plan.md` section 5, question 4) | Daily by 07:00 is fixed for the week so the issues stay comparable. |
| A second city, travel dates | When a reader asks | Nobody asks for it before the first issue. |
| X handle, Goodreads, Letterboxd and other profiles | After session 1 shows whether the writer can read them (see section 3) | An input the writer cannot open is a question that costs trust and returns nothing. |
| Pause the daily issue | Shown only on the return visit, prefilled, under the button | A new reader has nothing to pause. |

### Dropped

| Question | Why |
|---|---|
| Email address and password, "create an account", confirm your email | The link is the login (`beta-plan.md` section 1). |
| Topic checkboxes (politics, tech, sport, ...) | Categories give category news. A checkbox cannot say "the Ligue 1 relegation fight, not the Champions League". |
| Length, number of pages, layout style | Template work; the beta ships one page from the page 3 template, and page shape is review question 2. |
| Interests ranked 1 to 5, sliders, importance scores | Nobody can rank interests they have not seen written up. The reply line does this after the fact. |
| Age, job title, company, industry picklists | "What you do" in the reader's own words carries more than three picklists, and nobody enjoys a job-title field. |
| Sources to exclude (a list of sites) | The "never want to read" clause covers it in words. |
| Reading time available, "how long do you have in the morning" | Length is fixed in the beta. |
| Privacy consent checkbox | Nothing is public and the three know each other; two sentences on the form say what is stored and who reads it. Oscar approves them before a partner sees the page (`beta-plan.md` section 4). |
| Notification channel, phone number, WhatsApp | Email only (D-009). |
| Referral, "how did you hear about us" | Oscar handed them the link. |

## 2. Friction rules, applied

Each rule from the task, and where it lands on the page.

| Rule | On `beta/form.html` |
|---|---|
| First screen asks the minimum | Three fields above the button: name, city, topics. Everything else sits under one "More about you (optional)" line and is folded shut on first visit, open on return. |
| No account, no password | The URL is the identity. No email field, no sign-in, nothing to confirm. |
| The link is the login | `GET /s/<key>` returns the form with the saved profile already in it. The email says "Change your Digest: <your link>". |
| Progress saved on every field | Each field saves to the browser at once and to the Worker one second after typing stops (`PUT /s/<key>`). A "Saved" word appears next to the field; leaving the page or losing signal loses nothing. The button does not save, it only asks for an issue. |
| Mobile first | One column, 16 px gutter, 18 px body text, inputs 48 px tall, the examples are tappable chips, the keyboard type matches the field (`inputmode`, `autocapitalize`). Drawn for a phone first and checked at 390 px. |
| Under two minutes on a phone | A target, not a measurement. Three required fields, one of them a name. The target is checked in session 3 by Oscar with a stopwatch. |
| Sensible defaults | Tone: straight. Links: none. Pause: off. Everything optional is prefilled with a working value, so pressing the button with only the three fields filled makes a full issue. |
| Examples in every field | A placeholder in each field, and for topics three tappable examples that are real topics, not categories. |
| One clear button | "Save and make my first issue" (on return: "Make my issue now"). Nothing else looks like a button. |
| A preview of the masthead with their name | An SVG masthead at the top of the page: "The <Name> Daily", today's date, the issue number. It redraws on every keystroke in the name field. |
| Nothing lost in sign-in | There is no sign-in. The remaining risk is the wrong link or a dead one, which shows one plain line with Oscar's first name in it: "This link is not one of ours. Ask Oscar for a new one." |

## 3. Connects: which links are worth asking for at beta stage

"Connects" are optional links the reader gives for context. No OAuth and no third-party sign-up in the beta, so only public URLs the writer can open with `WebFetch`.

| Connect | Beta | Why |
|---|---|---|
| City | Asked, required | Weather and local stories for one field. |
| Newsletters, blogs and sites the reader already reads (public URLs) | Asked, optional, up to 5 | A newsletter archive page tells the writer the reader's level and taste better than any question. Public, fetchable, no account needed. |
| X handle | Not on the beta page | Whether `WebFetch` on the box can read an x.com profile or a user's posts without a login, I don't know; in my experience public x.com pages return an empty shell to scripts. Session 1 tests it once with Oscar's own handle. If it reads, the field is added as a sixth optional link; if not, it stays off, because an input the writer silently ignores is worse than no input. |
| Goodreads, Letterboxd | Not on the beta page | Public profile pages exist and are readable, but neither partner has said they use one, and a books-and-films line is a nice touch, not a reason to open the issue. Asked when a reader mentions it. |
| Spotify, Strava, YouTube, podcasts | Not in the beta | Need OAuth or a login, out by the task's rule. |
| RSS feed URLs | Covered by the links field | A feed URL is a URL; the writer opens it. No separate field. |
| Calendar, email, notes | Not in the beta | Personal data, OAuth, and a different product. The personal Digest reads Oscar's vault because it is his. |

Oscar's own Digest reads his X likes and his vault; a partner's issue has a form. The links field is the one connect that narrows that gap on day one, which is why it is on the page even though it is the slowest field to fill.

## 4. The final wording

What the page says, top to bottom. Labels in bold, help text in plain type, placeholders in quotes.

Masthead preview: "The <Name> Daily" (before a name is typed: "The Daily"), today's date, "No. 1".

Intro, one line: "Your own one-page paper, written overnight from what you tell us here. Three fields and a button."

**What should the masthead say?**
Your first name, or whatever you want on top of your paper.
Placeholder: "Paul"

**Where do you wake up?**
We use it for the weather line, your 07:00, and stories near you.
Placeholder: "Barcelona"

**Three things you would read about even on a busy morning**
Be as specific as you like. "Hardware startups in Europe" beats "technology"; "the Ligue 1 relegation fight" beats "football".
Placeholder: "Battery supply chains, Catalan politics, what the Fed does next"
Tappable examples: "Robotics startups in Europe", "The Barcelona housing market", "Long-form interviews with founders"

Fold: **More about you (optional, but it is what makes the paper yours)**

**What do you do, what are you working on right now, and what do you never want to read?**
The paper uses this to say why each story is for you. The last part is the most useful.
Placeholder: "I run a small design studio in Gracia, we are hiring our first engineer, never show me crypto prices or celebrity news."
Counter: "0 / 600"

**How should it read?**
Straight: "Three facts, one source, no adjectives."
Analytical: "What happened, why it happened, and what it probably means for you."
Light: "The same facts, told the way a well-read friend would over coffee."

**Links you already read (optional, up to 5)**
A newsletter, a blog, a site, a public profile. We read them to learn your taste; we do not quote them without saying so.
Placeholder: "https://"

Two sentences under the button (Oscar approves them before a partner sees them): "What you type here is stored under your private link and read by the person who sent it to you and by the program that writes your paper. Nothing is public, and asking him deletes it."

Button, first visit: **Save and make my first issue**
Button, return visit: **Make my issue now**

Status line under the button, one of: "Saved. Your first issue is being made; it arrives by email." / "Being made." / "Sent at 06:52." / "Today's issue is running late. We're on it." (Oscar's text) / "Three issues a day is the limit. Tomorrow's is on its way at 07:00." / "Saved. Your next issue is tomorrow by 07:00."

Return visit only: **Pause my daily issue** (checkbox) "Your link keeps working; press the button whenever you want one."

Wrong or dead link, the whole page: "This link is not one of ours. Ask Oscar for a new one."

## 5. What the writer receives

The profile the Worker stores and the runner reads (`beta-plan.md` section 2, four key types):

```json
{
  "name": "Paul",
  "city": "Barcelona",
  "topics": "Battery supply chains, Catalan politics, what the Fed does next",
  "about": "I run a small design studio ...",
  "tone": "straight",
  "urls": ["https://..."],
  "paused": false,
  "updated_at": "2026-11-17T06:40:12Z",
  "requests": ["2026-11-17T06:40:30Z"]
}
```

`requests` holds the button presses of the current Madrid day; the Worker refuses the fourth. The writer's prompt (`WRITE-PROMPT.md`, session 1) gets `name`, `city`, `topics`, `about`, `tone` and `urls`, and the rule that every "why you" line points at a phrase in `topics` or `about`.

## 6. Open questions for the box session

- X handle: test once in session 1 whether the writer can read a public x.com page from the box. Decides one optional field.
- Fonts: the page expects `fonts/` next to it (Playfair Display, Source Serif Pro, IBM Plex Sans Condensed, `spec.md` section 5) and falls back to Georgia and system sans when they are missing. Copy them from the pipeline in session 3.
- The two privacy sentences: Oscar's wording wins over mine.
