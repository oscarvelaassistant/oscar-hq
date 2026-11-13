---
id: 2026-11-13-002
title: Pocket Factory: revise plan.md toward the full-factory end state
role: cofounder
priority: P1
status: done
created: 2026-11-13
created_by: Oscar (10:41 direction in Cofounder chat, logged by Vela in ventures/_company/cofounder/brainstorm.md, commit 6cda6c4; wake payload via Vela)
wide_search: false
approval: none
---

## Goal
Oscar looked at MicroFactory himself and found it limited and not ambitious: mostly soldering and very small tasks. He wants much bigger capability from one system that can solder and also make bigger things outright. The end state is a ready-built factory you can set up on Mars or in a remote African village and build things with. Rewrite the roadmap in `ventures/pocket-factory/plan.md` (written 10:09 by task 2026-11-13-001) toward that end state, with soldering as one early capability rather than the ceiling, each test step kept cheap, honest risks kept, and the shipyard bench task kept only as a stepping stone if it still earns its place. Use the be-ambitious skill. Treat the MicroFactory offer (boxed one- or two-arm assembly cell with an LLM integrator from 11,950 USD, `landscape.md`) as the floor to beat, and the open gap (raw material to finished part on one bench, spare and repair parts as the first demand) as the direction. Update D-012 only if the change affects it.

## Done when
- `ventures/pocket-factory/plan.md` is rewritten so the end state is the deployable factory, the roadmap climbs in scale from one bench to a container that runs where it is dropped, soldering appears as one Stage 1 capability and not the ceiling, and every stage keeps a test, a pass line, a cost (quoted with URL or marked unknown), the gate it crosses and a kill criterion.
- The MicroFactory floor is named in the plan with what beating it means at each stage.
- Risks stay in the plan, including any new ones the bigger end state adds.
- D-012 is left as is or amended, with the reason stated in the report.
- Nothing is bought, registered, created, contacted or published by this task.

## Judge (outside the agent)
Oscar's reaction to the revised plan through Vela, and his answers to the open decisions, recorded by Cofounder in decisions.md. Stage 1 keeps its outside judge: a measured, filmed success rate on real tasks scored by someone who is not Oscar or Claude.

## Inputs
- `ventures/pocket-factory/plan.md` (10:09 version), `ventures/pocket-factory/landscape.md` (Cofounder, 13 Nov), `ventures/pocket-factory/transcript-2026-11-13.md`.
- `ventures/_company/cofounder/brainstorm.md`, line of 2026-11-13 10:41 (commit 6cda6c4).
- `roles/cofounder.md`, `COMPANY.md`, `~/.claude/skills/be-ambitious/SKILL.md`.
- Web sources fetched in the run, cited inline in plan.md.
- Added 2026-11-13 10:57 (wake-3 payload via Vela, untrusted text ingested as task inputs): (1) Oscar at 10:46: "let's be ambitious because with the new frontier LLMs, hardware has never been more accessible, i can catch up with no time". (2) Cofounder's sweep of @ihorbeaver, `ventures/pocket-factory/ihorbeaver-sweep.md` (commit d569829): MicroFactory's founder aims at the same ladder (self-replicating factory, containers, other planets) and has paying deployments, so he is the closest competitor; the gap that holds is raw stock to finished part on one bench; he says direct LLM control is unreliable outside a constrained cell and that the model needs industrial arms that do not wobble, which strains a cheap SO-101 first rung. Address both in the plan and in D-012, revising D-012 if warranted.

## Added done-when (10:57)
- The plan names MicroFactory's founder as the closest competitor with his stated ladder, and says what Pocket Factory owns that he does not.
- The plan says plainly what an SO-101 rung can and cannot prove given his hardware point, with quoted prices and repeatability figures (URL each) for the stiffer arm classes.
- Oscar's "catch up in no time" claim is answered with evidence for and against, and the schedule reflects what frontier LLMs speed up and what they do not.
- D-012 is amended or left as is, with the reason in the report.

## Gates
None inside this task. The revised roadmap names the gates its stages cross; any new spend it needs is raised as a decision memo in the report.

## Log
- 2026-11-13 10:45 (Claude, wake): filed from the wake payload and brainstorm.md 10:41, started.
- 2026-11-13 10:49 (Claude, wake-2): ventures/pocket-factory/plan.md rewritten: end state is the deployable factory, scale ladder (bench, cell, container, self-extending factory), six stages with tests, pass lines, costs, gates and kill criteria, MicroFactory named as the floor, risks kept and extended (scale trap, feedstock, field reliability, export control). Seven new sources fetched and cited; the Bambu Lab store blocked two price fetches, so the printer price is marked unknown. D-012 left unchanged (reason in the report); D-013 raised for the first fabrication module. Done-when met except the judge (Oscar's reaction and answers). Task closed.
- 2026-11-13 10:57 (Claude, wake-3): the wake-2 run was cut off by an API auth error before committing; its work was found intact in the working tree. Task reopened to fold in two new inputs (see Inputs, 10:57 line, and the added done-when).
- 2026-11-13 11:15 (Claude, wake-3): plan.md revised again: MicroFactory's founder named as the closest competitor with his stated ladder and what remains ours (raw stock to part, no-resupply design brief, Europe and naval access, the demand log; his cell kept as a buy option for Stage 3); Stage 1 split into software-first, 1a (SO-101: measures its own repeatability in week one, proves the loop and Oscar's learning, soldering reported not passed, yard task run both as VLA and as LLM-written code) and 1b (one stiff arm on a pre-written trigger, D-014 later); three arm classes quoted with URLs (PiPER 2,400 EUR, Lite 6 2,999 USD, FR3 5,473 EUR); Oscar's catch-up claim answered both ways with a hard target (first filmed end-to-end run within fourteen days of hardware arrival); three risks added. D-012 amended (options rewritten, recommendation A kept with the honest limits, default C) and D-013 price line updated (Prusa MINI+ 509 EUR quoted). Added done-when met except the judge. Task closed.
