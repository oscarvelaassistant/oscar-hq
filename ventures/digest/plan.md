# Oscar's Digest as a product: the plan

Written 2026-11-12 by the wake run (task 2026-11-12-001, HUB note 20261112130840286-c6cc2d47 via Vela). Status: plan only. Nothing in here has been bought, registered, created or published. Every price is quoted from the URL next to it, in the currency the vendor shows; where a source is secondary it says so. No estimates.

Oscar's brief, in his words via Vela: sell Oscar's Digest as a personalised daily or weekly journal; the client picks length, style and topics; Oscar plus two friends, a third each, profits shared three ways; Oscar builds. He wants the plan to cover a new site and domain, a product account, automated digest creation, client onboarding, and how to build it.

## 1. What exists today (the asset)

- A working one-reader pipeline in `/workspace/digest`: Python builders for page 1 and page 3, an HTML and Playwright renderer to a PDF sized 1:1 for a BOOX Note Air2 Plus, procedural SVG art, a fit pass, an overflow probe, text rules (sources on every fact, no em dashes, decision codes in plain words), e-ink previews. Source: `/workspace/digest/README.md`.
- The writing step is one `claude -p --model opus` run per day with `DAILY-PROMPT.md`, on Oscar's Claude subscription, driven by Vela's 06:35 routine. Inputs are Oscar's own data: WHOOP through the hub, the vault's Brain Dump and health protocol, X exports, the HQ reports, Vela's research file.
- Delivery is a Cloudflare Worker, `oscar-digest`, on the free plan, with KV storage and bearer tokens for one device and one publisher. Source: `/home/box/projects/oscar-digest/README.md`.
- A design that Oscar likes (newspaper typography, engraved nature, four columns) and ten days of daily issues as samples.

What a product cannot reuse as is: the writing step (see section 2), the personal inputs (WHOOP, vault, X exports are Oscar's and stay behind the hub), and Vela (a Grok Bot cannot be the orchestrator for N clients).

## 2. The fact that shapes the whole build: generation must move to the API

Decision record, 2026-11-12 14:55 Madrid (Oscar via Cofounder, relayed by Vela; D-008 yes, modified): for the first tests the issues are written with Claude on Oscar's own subscription through Claude Code, not with an API key, so no API spend for now. He was told the terms below bar this for issues made for other people and chose it anyway; recorded as his call. This section's consequences therefore apply from the moment Oscar moves to an API key, not to Phase 0. The build spec is `ventures/digest/spec.md`.

Anthropic's Claude Code legal page says OAuth sign-in is "intended exclusively for purchasers of Claude Free, Pro, Max, Ultra, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code", that developers building products "should use API key authentication", and that Anthropic "does not permit third-party developers ... to route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users". Customers "may not pay for, resell, or intermediate Claude usage on their end users' behalf". Source: https://code.claude.com/docs/en/legal-and-compliance

Consequences:
- Client issues are generated with an Anthropic API key under the Commercial Terms, billed to the product. Oscar's own issue can stay on his subscription.
- API spend is a gate 2 item (COMPANY.md: ceiling 50 EUR for November 2026, approved decision required). Phase 0 below asks for that decision.
- Cost per issue is unknown until measured. The prototype logs input and output tokens per issue and per model; the first scorecard reports cost per issue against the price.

Current API list prices, USD per million tokens, base input / output (source: https://platform.claude.com/docs/en/about-claude/pricing):

| Model | Input | Output | Cache hit |
|---|---|---|---|
| Claude Opus 5.5 | 4 | 20 | 0.20 |
| Claude Sonnet 5.5 | 2 | 10 | 0.10 |
| Claude Haiku 5.5 (prompts up to 100k tokens) | 0.10 | 0.50 | 0.01 |

The same page says models from Claude 4.7 on tokenize about 30% more tokens for the same text.

## 3. Site and domain

What to build: one static marketing site (what it is, three sample issues as PDFs and PNGs, a sign-up form, a privacy page, an imprint) plus the client web app at a subdomain (`app.`). Both run on Cloudflare on the free plan: Pages or a Worker for the static site, a Worker for the app. The existing Worker code (token model, KV layout, ETag handling, signed uploads) is the starting point; the product gets its own Worker and its own KV namespace, never the personal `OSCAR_DIGEST` one.

Domain: Cloudflare Registrar sells at cost ("Registration, transfer, and renewal prices are always at or below what registries and ICANN charge us", https://www.cloudflare.com/products/registrar/). Cloudflare does not print the .com price on that page; secondary sources quote about USD 10.44 a year for a .com (registry fee plus ICANN fee), for example https://dev.to/techsifted/best-domain-registrars-in-2026-where-to-actually-buy-your-domain-1h47. Verify in the Cloudflare dashboard before buying. Name candidates (availability not checked, no registrar queried): the product needs a name that is not "Oscar's Digest" (a client's issue carries the client's name on the masthead). Oscar and the two partners pick the name; the plan does not.

Gates: buying the domain is gate 2 (spend); putting the site up is gate 3 (public). Both are Phase 1 decisions, raised only if Phase 0 passes.

## 4. Product account

"Product account" here means the client-facing account system plus the two external accounts the product needs.

Client accounts (built, no third party): email plus magic-link login (no passwords to store), one KV record per client holding the preferences in section 6, delivery history, and the issue archive (`issue:<client>:<date>` PDF with a 30-day TTL, same pattern as `pdf:<date>` today). The device-token model from the current Worker carries over for e-ink readers that pull `/latest.pdf`.

Billing: Stripe. Spain pricing: standard EEA cards 1.5% plus EUR 0.25 per transaction; international cards 3.15% plus EUR 0.25, plus 2% for currency conversion; Stripe Billing (subscriptions) 0.7% of billing volume on pay-as-you-go. Source: https://stripe.com/es/pricing. Opening a Stripe account is gate 2 (signup) and needs the legal entity in section 8.

Email delivery: D-009 (2026-11-12 15:11 Madrid, Oscar via Cofounder, logged by Vela): the MVP delivers each issue as a PDF by email, sent from Oscar's own Gmail account to the three readers, with no mail service sign-up; all issues in English. A mail service of the product's own (Resend, Postmark, Mailgun, Mailjet, Amazon SES, Cloudflare Email Sending, Proton SMTP) is a gate 2 decision for Phase 2; the options with quoted prices and URLs are in `ventures/digest/spec.md` section 7a. Cloudflare's own sending needs the Workers Paid plan for arbitrary recipients (https://developers.cloudflare.com/email-service/); on the free plan it sends only to verified addresses.

Hub rule: client data is the product's data, not Oscar's personal data, so it lives in the product's own Worker and KV, outside the personal hub. The hub gets one read tool, `digest_product_status` (clients, issues sent, failures, token spend), so the dashboard and Oscar's own Digest can show it. For Vela line: `2026-11-12 | product client data lives in the product Worker's KV, outside the personal hub; only a status read tool goes behind the hub | revisit 2026-12-12 | for Vela`.

## 5. Automated digest creation

Three stages per issue, each a separate program so a failure is visible and retryable:

1. Gather, per client profile: public sources only. For each topic a fixed list of RSS feeds and news pages (the client can add feeds or URLs), fetched by the Worker (Cloudflare free plan: 100,000 requests a day, 5 cron triggers per account, 15 minutes wall time per scheduled run; sources: https://developers.cloudflare.com/workers/platform/pricing/ and https://developers.cloudflare.com/workers/platform/limits/). Weather and sunrise for the client's city from open-meteo as today. Nothing from X for clients (the exports are Oscar's connector data). Output: `data/<client>/<date>/sources.json`.
2. Write, with the API: Haiku 5.5 ranks and deduplicates candidates against the profile; Sonnet 5.5 writes the issue in the client's language and style within the copy budget the renderer enforces; Opus 5.5 only for a weekly long edition if the quality gap shows in the prototype. Every story keeps its source URL; a story without one is dropped by the build as today. The prompt is the generalised `DAILY-PROMPT.md` with the personal parts removed (no WHOOP, no vault, no council unless a client opts into a health section with their own data).
3. Render and deliver: the existing Python and Playwright renderer, parameterised by length and style (section 6), produces the PDF and a PNG preview; delivery is the PDF by email from Oscar's Gmail (D-009), plus the web link and, for Oscar, the device pull. Each run writes `status-<client>-<date>.json` like today.

Where it runs: Phase 0 on the box (Python already works there; the box has no cron, so a timer loop like `whoop-morning-watch.sh`, or a systemd user timer). Phase 2 moves gather and delivery into the Worker cron and keeps rendering on the box or on a small always-on machine; Playwright does not run in a Worker. A Worker-only pipeline would need an HTML-to-PDF service, which is a new account and a later decision.

Quality rules kept from the personal Digest: sourced facts, no em dashes, overflow probe, fit pass, no invented numbers, previews looked at by the pipeline before publishing. New: a per-issue check that no personal data of another client leaks (one profile per process, no shared context).

## 6. Client onboarding

One form, under five minutes, stored as the client's profile JSON:

- Name as it should print on the masthead; email; city and timezone (weather, sunrise, delivery time).
- Language: English, Spanish, Catalan, French (the pipeline already writes English; the other three are a prompt change plus a proof-read of the first issues by a partner who speaks the language). Phase 0 is English only (D-009); Paul reads French and Spanish and can proof-read those.
- Cadence: daily or weekly, with the delivery time (daily: ready by 07:00 local; weekly: pick the day).
- Length: short (one page), standard (two pages), long (three pages, weekly only). The renderer's page templates give these for free.
- Style: newspaper (today's design), letter (one column, a personal note first), brief (headline and three lines per story). Newspaper ships first; letter and brief are template work.
- Topics: a pick list seeded from the feeds we already know work (defence and naval, AI and robotics, hardware, art and history, birds and nature, local news for the city) plus free text and the client's own feeds or URLs. The profile grows the way `profile.md` does, from what the client reads: the web app records which stories were opened.
- Delivery: email (PDF attached and a web link; the default, and the MVP's channel per D-009), web link only, or e-ink pull with a device token.
- Data: the profile and 30 days of issues; deleted on cancellation; no sharing with anyone; the privacy page says this plainly (clients will be in the EU).

First issue within 24 hours of sign-up, free; the second month is paid. Pricing is a partners' decision, not set here. Public anchors for comparable products, as quoted by secondary pages on 2026-11-12: Readless Pro USD 4.90 a month and Max USD 9 a month (https://www.readless.app/solutions/daily-news-digest), i-digest USD 5.9 self-managed and USD 12.9 managed daily digest (https://i-digest.com/), Feedly's AI tier about USD 12 a month (https://summry.io/en/blog/ai-news-digest-tools-compared). Those products deliver summaries in an app or an email; none that I found delivers a laid-out newspaper made for one reader, which is the thing to price.

## 7. How to build it: phases and gates

Phase 0, prototype for three readers (Oscar, Paul and Pietro), no site, nothing public. D-008 answered yes on 2026-11-12 with the change recorded in section 2: the writing step runs on Oscar's subscription for the first tests. D-009 the same day: each issue is delivered as a PDF by email from Oscar's own Gmail, no mail service sign-up, English only. Spec: `ventures/digest/spec.md`.
- Fork the pipeline into `/workspace/digest-product` (the personal one stays untouched). Profile JSON, generic gather stage, writing stage behind one interface (`claude-code` on the subscription in Phase 0, `api` ready for a later gate 2 decision) with usage logging, renderer parameterised by length. Oscar builds with Claude Code on the box (Opus, effort high, as the rules say).
- Run it daily for four weeks for the three readers. Measure: issues delivered on time, tokens and USD per issue per model, how many issues each partner opened (the web link logs it), and what each one asked to change.
- Exit test: both partners read it on most days of week four, and cost per issue is known. Otherwise stop; the cost was four weeks of Oscar's venture hour and under 50 EUR of API.

Phase 1, name, domain, site with sign-up and samples. Decisions: domain purchase (gate 2), site goes live (gate 3). Builds on the Phase 0 issues as samples.

Phase 2, accounts, billing, a product mail service, archive. Decisions: Stripe account (gate 2, needs the entity), the mail service (gate 2; options and prices in the spec, section 7a). The hub status tool and the For Vela line close here.

Phase 3, first paying clients from the partners' own circles; weekly scorecard line: clients, churn, cost per issue against price, failures. Opus for the weekly edition only if the prototype shows the gap.

What Oscar builds versus what the partners do: Oscar builds and runs the pipeline. The partners' contribution is not stated in the brief; a third each with one builder needs it written down (section 8).

## 8. The three-way split

A third each, profits shared three ways (Oscar's correction of 2026-11-12). Two things need writing before any money moves:
- What each partner puts in (clients, languages, money, design, operations) and what happens if one stops contributing. One page, signed by the three, before Phase 2.
- The vehicle. Spanish law has allowed a sociedad limitada with EUR 1 of share capital since Ley 18/2022 (BOE-A-2022-15818, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-15818), with a legal reserve of 20% of profits while capital is under EUR 3,000, per secondary summaries such as https://www.garrigues.com/es_ES/noticia/publicada-boe-reforma-reduce-3000-euros-1-euro-capital-minimo-constituir-sociedad. Whether to incorporate before the first client, or run Phase 3 on a written agreement and one partner's invoice, is a partners' decision; a Stripe account needs one of the two. Costs of incorporation (notary, registry): unknown, source pending.

## 9. What I would say as cofounder (opinion, labelled)

The role file records why Oscar's earlier ventures were closed: software too easy to copy, work that bored him, missing insider knowledge. This is software, and the design can be copied in a weekend by anyone with the same tools. What cannot be copied fast is ten days of a working pipeline, a reader who already likes it, and three people who will read a daily issue and say what is wrong. So the honest test is Phase 0, not the site: if two friends do not read a free issue most mornings, no domain will fix that. Build Phase 0, measure, then decide on the domain. Said once; Oscar's call after that.

## Open inputs from Oscar (Vela folds them into a batch)
- What each partner brings (section 8): still open. Who they are is answered (2026-11-12 15:09): Paul and Pietro, both in Barcelona; details in the spec, section 13.
- Which language the first clients read: answered, English for all three in Phase 0 (D-009).
- Whether he has an Anthropic Console API key already: no longer needed for Phase 0 (D-008 as answered); it returns when the `api` backend is switched on.
- The spec's own open inputs: all answered on 2026-11-12 (`ventures/digest/spec.md` section 13).
