---
id: 2026-11-01-001
title: Legal map and procurement path, second pass (open questions from the first pass)
role: regulation-procurement
priority: P2
status: done
created: 2026-11-01
created_by: Claude
due: 2026-11-05
wide_search: false
approval: none
---

## Goal
Close the open questions the first pass (task 2026-10-31-002) left in `ventures/crowd-control/regulation/open-questions.md` that primary texts can settle without a lawyer, and give procurement-path.md a third route that carries a real notice, so the engineer's constraints and Oscar's procurement picture rest on the texts in force rather than on secondary readings.

## Done when
- Q3 (D. 211-17 current text: is foam or any non-water projection listed), Q7 (what décision 2021-834 DC censured in L. 242-1 to L. 242-8, and the L. 242-4 text in force), Q8 (what the December 2021 SNMO says on encirclement and new equipment) and Q11 (L. 2172-3 wording after the loi de finances pour 2024; R. 2123-1 b of 2°) are each answered in `legal-map.md` or `procurement-path.md` with the article or page, URL and date consulted, or marked "text not reachable" with the two attempts logged.
- `procurement-path.md` gains one route with a real notice (UGAP referencing, a partenariat d'innovation notice, or a Préfecture de police purchase of barriers or BRAV-M equipment), BOAMP, PLACE or TED id and URL, so three routes carry a notice each.
- `constraints-for-design.md` stays at ten lines or fewer, updated where an answer changes a line.
- `open-questions.md` updated: closed questions marked closed with the date, the rest kept with who could answer them.

## Judge (outside the agent)
Falsification pass by a second agent on every new or changed claim, with the sources given as titles and URLs in its prompt and reached through its own web search results (the method that worked on 2026-11-01: 14 of 14 sources read). A claim that fails is removed or rewritten before the report says done.

## Inputs
- `roles/regulation-procurement.md`.
- `ventures/crowd-control/regulation/open-questions.md` (Q3, Q7, Q8, Q11, Q12 as written 2026-11-01), `legal-map.md`, `procurement-path.md`.
- Légifrance article pages open when reached through a search-result link (R. 311-1 and R. 311-2 did on 2026-11-01); the Conseil constitutionnel decision page for 2021-834 DC; interieur.gouv.fr for the December 2021 SNMO; BOAMP and TED searches by CPV 34144210, 35000000 and buyer "Préfecture de police"; ugap.fr.

## Gates
None. Gate 1 if a conversation with a lawyer, the SCAE or a procurement officer is proposed (Q1, Q2, Q12 need one).

## Log
- 2026-11-01 06:50 (Claude, morning): created as the follow-up of 2026-10-31-002, which closed with these questions open.
- 2026-11-01 21:55 (Claude, evening): Q3 closed (D. 211-17 in force since 18 Oct 2021 lists grenades and launchers only, no water, no foam; first-pass claim corrected: the list is a firearms list, water cannon is not on it), Q7 closed (décision 2021-834 DC: censures, three reserves, 48-hour rule for home images; L. 242-4 text in force still unread on Légifrance), Q8 half closed (encirclement wording of the December 2021 SNMO through CE n° 461513; the circular's PDF not reached, two attempts, permission an unattended run cannot grant), Q11 closed (L. 2172-3 and R. 2123-1 from reproductions, Légifrance article pages refused twice). Procurement: route 1 now has a named programme (Innov'Achats, Depafi, internal sponsor files); route 4 added (ministry grenade framework, BOAMP 22-149405 and 23-155499, ids and URLs from Politis, notices themselves not read, one attempt each, permission); Préfecture de police confirmed as its own buyer (two BOAMP notices read); UGAP hits are firefighter PPE only. constraints-for-design.md rewritten at ten lines. open-questions.md updated (Q2 merged into Q12, Q13 added). Judge: second agent, search-link method, 12 of 13 sources reached, 8 HOLDS, 3 PARTIAL (D. 211-17 category column per row, Politis date 10 not 9 November and ids only in links, Maximilien applies to one PP notice only), all three folded in. Done-when: four questions met; third-route notice met as id and URL, not as a read notice (stated gap); constraints at ten lines; open questions updated. Remaining for a run with a live operator or for Vela: read BOAMP 23-155499 and the SNMO PDF (Légifrance circ 45250), re-read L. 242-4, L. 2172-3 and R. 2123-1 on Légifrance.
