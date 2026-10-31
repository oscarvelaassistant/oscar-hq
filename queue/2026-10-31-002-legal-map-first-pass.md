---
id: 2026-10-31-002
title: Legal map and procurement path, first pass
role: regulation-procurement
priority: P1
status: in-progress
created: 2026-10-31
created_by: Claude
due: 2026-11-04
wide_search: false
approval: none
---

## Goal
Before any design work, know which of the five product directions in the idea (barrier vehicles, fire-suppression robots or drones, tethered overwatch drones, after-the-fact evidence capture, small water or foam unmanned vehicles) are legal as described in France and under the EU AI Act, and how the Interior ministry buys such equipment.

## Done when
- `ventures/crowd-control/regulation/legal-map.md`: for each of the five directions, a verdict (legal as described, needs a change, out) with the article or decision it rests on, URL and date consulted.
- The AI Act position on after-the-fact review of footage (the idea note's assumption) stated with the article number, and the applicability dates of the prohibitions.
- `ventures/crowd-control/regulation/procurement-path.md`: three procurement routes open to a new supplier, each with one real past tender reference (BOAMP, PLACE or TED id and URL).
- `ventures/crowd-control/regulation/constraints-for-design.md`: ten lines or fewer for the engineer.
- `open-questions.md` lists what primary sources did not settle and who could.

## Judge (outside the agent)
Falsification pass: a second agent (or the evening run) receives only the cited sources and tries to break each claim. Claims that fail are removed or rewritten before the report says "done".

## Inputs
- `roles/regulation-procurement.md` (starting points to verify).
- Légifrance, EUR-Lex consolidated AI Act, Conseil d'État decisions, Défenseur des droits reports, BOAMP and TED.

## Gates
None.

## Log
- 2026-10-31 16:05 (Claude, setup): created.
- 2026-10-31 17:10 (Claude, evening): first pass written, four files in regulation/. Five verdicts with sources (CE 444849, CE 468316, AN QE 16844, CNIL annex 4, CC 2021-834 DC consolidation, Commission AI Act page for Article 5). Not met: AI Act Articles 26 and 113 not fetched (Commission pages needed a permission the run could not grant; EUR-Lex next), Légifrance refused direct fetches, procurement route 1 has no notice by construction and no water-cannon notice was found; ten open questions filed. Judge (falsification by a second agent) not run. Next: fetch EUR-Lex and Légifrance texts, then run the falsification pass before saying done.
- 2026-10-31 20:15 (Claude, second evening run): falsification judge launched as a second agent with the two files; it could not open any of the twelve cited sources (URLs taken from a file trigger a permission prompt no one answers in an unattended run) and returned "cannot check" on every claim, plus two reading flags (CE 444849 point numbering, R. 2122-9-1 lot cap and the loi de finances 2024 sentence). The run fetched three sources itself through search-result links: CE 444849 re-read, dispositif and considérants 20 to 28 now stated precisely in legal-map.md; Article 26(10) read on the Commission service desk page; Article 113 as amended by Regulation (EU) 2026/1744 read in a secondary reproduction (the "two additional prohibitions" are Article 5(1)(ba) and (bb), from 2 December 2026; content not read). Q4 narrowed, Q11 added, the unsourced L. 2172-3 sentence flagged in procurement-path.md. Still not done: EUR-Lex consolidated text, Légifrance, the judge pass on the other nine sources. Proposal filed: proposals/2026-10-31-subagent-source-urls.md.
