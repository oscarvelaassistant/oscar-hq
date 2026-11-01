---
id: 2026-10-31-003
title: Virtual prototyping tooling survey and first-component candidates
role: hardware-engineer
priority: P2
status: waiting-approval
created: 2026-10-31
created_by: Claude
due: 2026-11-05
wide_search: true
approval: none
---

## Goal
Oscar has seen many tools on X for testing products virtually before sending them to a manufacturer. Turn that into a short list he can act on: which tools, what each can test, which are free, which run in a browser, and which he must install on the Mac. Then propose three candidate first components, one per promising product direction, each with the test that would prove it.

## Done when
- `ventures/crowd-control/engineering/tooling.md` covers at least the seeds in the role file plus the mainstream tools, each with: purpose, cost, browser or install, file formats, the test it enables, verdict (use now, later, skip) and the date checked.
- `ventures/crowd-control/engineering/first-component-candidates.md`: three candidates, each with the requirement it would satisfy (traced to the idea note until interviews exist), the tool that would test it, the test with numbers, and the manufacturer type that could make it. Ends with a decision `D-###` asking Oscar to pick one or wait for the first officer conversation; recommendation included.

## Judge (outside the agent)
Every tool entry links to the tool's own page showing the claimed capability and price. Every candidate's test has a number and the source of that number. Later: the chosen component's simulation result.

## Inputs
- `roles/hardware-engineer.md` (seeds).
- Oscar's vault captures of 22 Oct (Blueprint, electronics simulator), 23 Oct (Kimi K3.1 Pro, to compare only if free), 31 Oct (Schematik), and the Ideas note entries on HeyPCB Circuit World and the Tsung Xu VTOL build (summarised in `ventures/crowd-control/README.md`).

## Gates
Gate 2 for any paid tier or account with payment details.

## Log
- 2026-10-31 16:05 (Claude, setup): created.
- 2026-10-31 17:10 (Claude, evening): engineering/tooling.md written from two subagent passes, 21 tools with verdicts, prices and versions as pages state them, Mac install steps. Three vault claims corrected (Colorfigures is a figure skill, Schematik has no simulator, HeyPCB has 11,000+ boards and no free tier). Not done: first-component-candidates.md and its decision, out of run time after the P1 tasks. Next run writes the three candidates with sourced test numbers.
- 2026-10-31 20:15 (Claude, second evening run): engineering/first-component-candidates.md written (hardware-engineer subagent, reviewed): A, tethered drone's authorisation and perimeter log board (Wokwi, browser, test from L. 242-4 and L. 242-5: 600 fixes, alert at fix 401, seven-day erase at 604,800 s); B, spray vehicle's graduated valve driver with two-step confirm (KiCad ngspice; Bürkert 2873, IRLML6344, 1N5819 datasheets; pass limits 0.375 A, 24.6 V peak, 1.3 W); C, barrier exit-gate hinge (FreeCAD CalculiX; 3.0 kN/m at 1.1 m from a building code, S355J2 355 MPa). Nineteen sources fetched. Not sourced and said so: coil inductance, PWM frequency, jet flow and pressure at UGV scale, gate width, Green Guide and EN 13200-3 loads (paid). Done-when met; judge partly met (every sourced number has its page; the unsourced ones are listed). D-003 raised below; status waiting-approval until Oscar picks or the first interview lands.
- 2026-11-01 06:45 (Claude, morning): no answer to D-003 yet (decide by 2026-11-04 08:00). The interview question the memo adds either way is in discovery/interview-guide.md, placed before the closing and asked only if the officer has himself raised drones, water or street closures, to respect the guide's no-leading-questions rule. Nothing else touched.

## Decision

### D-003 First component: pick one or wait for the officer conversation
- What: whether to start designing one of the three candidates now (A, the drone's authorisation and perimeter log board, browser only; B, the spray vehicle's graduated valve driver with two-step confirm, KiCad install; C, the barrier exit-gate hinge, FreeCAD install) or to wait for the face-to-face with the Garde républicaine contact next week and the first conversation with someone who has stood a riot night.
- Why now: tooling is surveyed and every candidate has a numeric test written; the next engineering hour needs a target, and Oscar's premise (AI removes the need for an in-house engineer) is only tested by running one chain end to end.
- Options: A) start candidate A now, in Wokwi, as the chain test, and let the interviews redirect later; B) start B or C now; C) wait for the first officer conversation, as the role's standing rule says, and add the question "which of these three breaks or is missing on a riot night" to the interview guide.
- Recommendation: C by the rule, A if Oscar wants the chain exercised before the conversation; A's requirements come from L. 242-4 and L. 242-5, not from a guess about the street, and nothing is bought or installed.
- Reversible: yes; a design hour is lost at most.
- Decide by: 2026-11-04 08:00. Default if silent: C, wait; the interview question is added either way.
