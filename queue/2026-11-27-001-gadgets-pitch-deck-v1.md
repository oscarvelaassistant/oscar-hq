---
id: 2026-11-27-001
title: Research and build v1 of the gadgets pitch deck for the Shenzhen angel coffee
role: cofounder
priority: P1
status: done
created: 2026-11-27
created_by: Oscar
due: 2026-11-27
wide_search: true
approval: none
---

## Goal
A first version of the gadgets pitch deck (promptable AI gadgets under one premium brand: cheap hardware sourced from Shenzhen, premium design, AI software the owner customises by talking to it; hero: a promptable e-ink display) that Oscar edits before the coffee with a possible angel from Shenzhen next week. Research first, with every number sourced by URL and date, so the market, competition and business-model slides survive a VC-style question. Oscar owns the style and the final cut.

## Done when
- `ventures/gadgets/pitch-deck-v1/research.md` exists: TAM/SAM/SOM for AI consumer devices, e-ink displays and smart home décor with the method shown; competition table (AI hardware and e-ink/display products: pricing, funding, outcomes); business-model benchmarks (hardware margin, subscription tiers, pre-orders, Shenzhen ODM cost and MOQ benchmarks); problem and why-now evidence (LLM cost curves, e-ink price trends, MCP/agents). Every number has a URL and a date; unsourced items are marked [placeholder]; opinions are labelled.
- `ventures/gadgets/pitch-deck-v1/deck.html` exists: self-contained slides (no external assets) in Oscar's structure: cover, problem and why now, hero, catalogue, market, competition, business model, progress and plan, founder and ask; with charts, a flowchart and diagrams drawn from the research.
- `ventures/gadgets/pitch-deck-v1/deck.pdf` rendered with headless Chrome if the tool is available on the box; if not, the report says so.
- Placeholders only where Oscar allowed them: catalogue renders and prices (due Sat 28 Nov), brand name, hero unit cost and MOQ, and any figure that could not be sourced.
- Hard rules kept: gadgets is Oscar's solo project (no team slide or mention of anyone else as team); no valuation, round size or equity; no ships, shipyards or naval angle; nothing sent, shared or public; no sign-ups, no spend.
- Committed and pushed; report in `reports/2026-11-27-wake.md`.

## Judge (outside the agent)
The angel's questions at the coffee: which market and competition figures she challenges, and whether any number in the deck fails a source check when she asks "where is that from". Before the coffee: Oscar's edit pass, and a spot check by Innovator of five random figures against their URLs.

## Inputs
- Payload from Oscar via Vela, 27 Nov 2026 07:44 Madrid (untrusted text, ingested here; Oscar approved the task).
- `ventures/gadgets/angel-coffee-prep.md` (discovery coffee, five questions, not-yet list).
- Vault note `🤖 AI HQ/🗂️ Shared Projects/🛠️ Gadgets startup.md` (idea list, status, solo-project correction of 27 Nov).
- `ventures/_company/cofounder/decisions.md` (the gadgets pivot and the gadget catalogue decision, 26 Nov), `morning-brief.md` (27 Nov).
- Oscar's slide structure in the payload. The "existing 9-slide outline" was searched for in the repo (only Pocket Factory deck notes found) and could not be searched in the vault from this run (shell search outside the repo is blocked); the payload structure is used.
- Web research through WebSearch and WebFetch, primary sources preferred.

## Gates
None crossed. The deck is a draft in the repo; showing or sending it is Oscar's act (gate 3 if it ever goes public). No spend, no sign-up, no message to anyone.

## Log
- 2026-11-27 07:50 (Claude, wake): payload ingested, task filed, research started with five parallel subagents (market sizing; AI hardware competitors; e-ink and display competitors; business model and ODM benchmarks; problem and why now).
- 2026-11-27 08:35 (Claude, wake): all five subagents back (about 270 web calls); `research.md` written with verified / snippet-only tags on every figure.
- 2026-11-27 09:00 (Claude, wake): `build_deck.py` and `deck.html` written (10 slides incl. a sources appendix, 11 inline SVG charts and diagrams); SVG parsed well-formed; scanned for forbidden words (no shipyard, naval, ARESA, team names; valuation, round size and equity appear only in the two lines saying they are off the table).
- 2026-11-27 09:05 (Claude, wake): `deck.pdf` NOT rendered: `google-chrome` needs an approval this `claude -p` run cannot give (tried chained and bare, two attempts, stopped per the failure rule). Visual check of the slides therefore not done; layout checked by arithmetic on box sizes only. Vela: the one-line command is in `ventures/gadgets/pitch-deck-v1/README.md`.
- 2026-11-27 09:05 (Claude, wake): done against done_when except the conditional PDF line, which the report states. Judge pending: Oscar's edit, Innovator's spot check of five figures, the angel's questions.

## Decision
None raised. No gate crossed.
