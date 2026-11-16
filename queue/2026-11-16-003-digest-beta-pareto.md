---
id: 2026-11-16-003
title: Digest beta: the most Pareto-efficient build so Paul and Pietro can make their own Digest from a link
role: cofounder
priority: P1
status: open
created: 2026-11-16
created_by: Oscar (19:03 in Innovator chat), filed by Innovator
effort: Fable high
approval: none for the plan; any deploy, account or spend stays a gate as in spec.md
---

## Goal
Oscar, in his words (19:03 Madrid, 16 Nov): "I want to continue forward with the Daily Digest with Paul and Pietro ... find out what is the most Pareto efficient thing that I can build right now, use Oscar Hub as a work environment if needed, so that I can basically have a product that I can send them the link, and they can create their own Daily Digest that will create a PDF that will send to their email to start with, just so we can have a proof of concept and discuss the actual product. Agree on what it looks like, and then once we're okay with that, we can go and worry about the distribution and getting clients."

So the beta is: one link, a partner sets up their own Digest (topics, style), and gets a PDF by email. Its purpose is a proof of concept the three of them discuss to agree what the product looks like. Distribution and clients come after.

## Context
- The Digest product has a plan (`ventures/digest/plan.md`) and a full Phase 0 spec (`ventures/digest/spec.md`, 6 build steps). Nothing is built yet: `/workspace/digest-product/` does not exist.
- Standing decisions: the Phase 0 prototype is approved with Claude on Oscar's own account as the writer, no API spend (D-008); PDFs go by email from Oscar's own Gmail, English only (D-009). Oscar was told once about Anthropic's terms for subscription use for other people; his call.
- Pocket Factory is still a venture; Oscar chose on 16 Nov to run the Digest alongside it.
- Oscar says building it won't take him long.

## Done when
`ventures/digest/beta-plan.md` exists with:
1. The cut: which parts of spec.md the beta keeps, which it drops or fakes (for example invite codes, the archive, the reader views, the polished app), and why, in one table.
2. The smallest working path: link, setup form, profile stored, nightly or on-demand run, PDF, email. Name where each piece runs (box, Cloudflare Worker on `digest-preview.projetrefonte.com`, Oscar HUB if it is the better work environment) and why.
3. Build sessions in order, each with a done-when Oscar can check, sized in sessions, not estimated hours.
4. What Oscar has to do by hand (Gmail app password, entering the partners' addresses, handing the link) and every gate that needs his yes.
5. What the three of them should look at and decide in the review after the first week of PDFs.
6. One Fable judgement, labelled as Claude's opinion: is this the most Pareto-efficient version, and what is the one thing most likely to sink it.
No em dashes. Decisions named by title, not bare codes. No estimates unless labelled.

## Judge (outside the agent)
Oscar reads it and can start build session 1 the same day.

## Gates
Plan only. Nothing deployed, bought, signed up for, sent or published in this task.
