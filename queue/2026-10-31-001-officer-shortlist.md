---
id: 2026-10-31-001
title: Officer shortlist and first outreach batch (objective 1)
role: customer-discovery
priority: P1
status: done
created: 2026-10-31
created_by: Claude
due: 2026-11-02
wide_search: true
approval: D-001 yes (option C, hold all five); D-002 yes (option B, ask the warm contact for two names)
---

## Goal
Give Oscar, in his Sunday or Monday morning window, a named list of people who have stood riot nights and a first batch of French messages ready to send, so objective 1 (one conversation held with a named CRS or gendarmerie officer) gets a name and a date this week. The council's 2026-10-29 recommendation was a conversation by 1 November through his reserve chain or a KUBE contact; that date has passed with no name filled in, so this task produces the names.

## Done when
- `ventures/crowd-control/discovery/officers.md` lists at least 20 named people (serving or retired CRS, gendarmerie mobile, BRAV-M, BSPP, trainers), each with unit, role, years, how reachable with a URL or a lead name, warm or cold, a one-line hook, status `not contacted`.
- `ventures/crowd-control/discovery/outreach/2026-11-01-batch-1.md` holds five French messages under 80 words each, one per person, chosen warm first, asking for 20 minutes, with no product pitch.
- `ventures/crowd-control/discovery/interview-guide.md` exists: ten questions ordered to get the last riot night as a story before any opinion.
- A decision `D-###` asks Oscar which five to send and from which account; default hold.
- A second decision asks Oscar for two names from his own channels (reserve chain, IHEDN, Mathieu, KUBE) to put at the top of the list; the run cannot know these.

## Judge (outside the agent)
A real reply. Until then the report says "drafts ready, zero contact". The shortlist's URLs resolve to real profiles or articles (the run checks each one).

## Inputs
- `roles/customer-discovery.md`.
- Oscar's idea file: `~/Claude Projects/InnovationHub/ideas/crowd-control.md` (not in this repo; its content is summarised in `ventures/crowd-control/README.md`).
- Vela's shared note `🤖 AI HQ/🗂️ Shared Projects/Crowd-control tech.md` in the vault: on 2026-10-24 the plan was to message ten retired maintien-de-l'ordre officers on LinkedIn and text Mathieu; status unknown, ask Oscar in the decision whether any of that happened.

## Gates
Gate 1 at sending. The run stops at drafts.

## Log
- 2026-10-31 16:05 (Claude, setup): created.
- 2026-10-31 16:45 (Claude, live with Oscar): Oscar named a warm contact, a friend of his father, former gendarme (Garde républicaine, motorbike escort); he will see him face to face next week. Message drafted (three versions) at discovery/outreach/2026-10-31-garde-republicaine-contact.md and the interview prep at discovery/interviews/2026-11-prep-garde-republicaine-contact.md. This contact is the first candidate for objective 1. The broader shortlist stays useful as the pipeline behind him; the run should rank warm introductions obtained through him above cold LinkedIn messages, and D-001 becomes "which cold messages, if any, to send before his introductions arrive".
- 2026-10-31 17:10 (Claude, evening): read Oscar's 16:45 live note after the fact (it landed on the remote during the run); D-001 reframed as he asked. Three mapping subagents (CRS; gendarmerie mobile and CNEFG; BRAV-M, BSPP, unions). 29 named people with fetched URLs in discovery/officers.md, all cold; five French drafts (77, 72, 77, 75, 75 words) in discovery/outreach/2026-11-01-batch-1.md; discovery/interview-guide.md written. Done-when met except warmth (no warm name exists yet). Judge: drafts ready, zero contact. Not found: a serving captain named after a 2023 riot night, a CRS trainer, any BRAV-M officer below director level. Stopped at Gate 1; D-001 and D-002 raised.
- 2026-11-02 09:25 (Claude, morning): Oscar answered through Vela (HUB note 20261102080611432-848eb74b, typed 09:04 Madrid): D-001 "Hold all five cold messages" (option C), D-002 "Ask my warm contact for two names at the face-to-face" (option B). Applied: batch-1 stays in discovery/outreach as drafts, nothing sent; the two-names ask is already the guide's closing question, and Vela added the Innov'Achats closing question on his yes (commit b9cecae). Task done at its drafts stage; judge still "drafts ready, zero contact". Objective 1 now rests on Oscar's face-to-face next week; the next discovery task opens when he reports the names he gets.

## Decision

### D-001 Cold messages before the warm introductions arrive
- What: whether to send any of the five cold French messages in ventures/crowd-control/discovery/outreach/2026-11-01-batch-1.md (Davoine, CRS 83; Verfaillie, ex-gendarme mobile; Cavallero, Alliance CRS; Le Louette, GendXXI; Cavallier, ex-CNEFG) before Oscar's warm contact (former gendarme, Garde républicaine, face to face next week) has had the chance to introduce him onward.
- Why now: objective 1 now has a first warm candidate but still no date with someone who has stood a riot night; cold replies take days; the role rule is warm before cold.
- Options: A) send all five now in parallel; B) send only Cavallier and Cavallero now (a retired general and a union delegate, no hierarchy leave needed) and hold the three others; C) hold all five until the face-to-face has happened and its introductions are known.
- Recommendation: C. The warm list is not exhausted, so the role rule says no cold messages yet; the batch stays ready and goes out the day the warm route stalls.
- Reversible: no once sent.
- Decide by: 2026-11-03 08:00. Default if silent: hold.

### D-002 A second warm name from Oscar's channels
- What: beyond the Garde républicaine contact, one more person from the reserve chain, IHEDN, Mathieu or KUBE who has stood a riot night (CRS, gendarmerie mobile, BRAV-M) or can introduce someone who has; and whether the 24 October plan (ten retired officers on LinkedIn, a text to Mathieu) happened.
- Why now: a Garde républicaine escort rider may not have stood a riot night himself; objective 1 needs someone who has, and all 29 names found this run are cold.
- Options: A) one name now, by HUB note or to Vela; B) no name, but ask the warm contact for two at the face-to-face (the interview guide's closing question); C) none, proceed cold under D-001.
- Recommendation: B, and A if a name comes to mind.
- Reversible: yes.
- Decide by: 2026-11-03 08:00. Default if silent: the morning run keeps the cold batch on hold and continues mapping.
