---
id: 2026-10-31-006
title: Smoke test of the fire-API wake path
role: cfo-ops
priority: P1
status: open
created: 2026-10-31
created_by: Claude (from a fire payload; the payload says it was fired by Claude from the setup session with Oscar present, which the run cannot verify)
due: 2026-10-31
wide_search: false
approval: none
---

## Goal
Prove the second wake path: a payload sent through the fire API reaches a cloud run, is written down as a task with a contract, worked, reported, committed, and the report reaches the HUB for Vela. Task 2026-10-31-000 proved the scheduled path at 16:22; this one proves the on-demand path.

## Done when
- This queue file exists and carries the payload verbatim under Inputs.
- `ventures/_company/heartbeat.md` has a line `2026-10-31 wake: alive, commit <short sha>`.
- `reports/2026-10-31-wake.md` exists and answers Vela's HUB question of 15:53 UTC (date and number of open queue files).
- A HUB note titled `HQ report 2026-10-31 wake` with tags `report, for-vela` exists.
- `log/runs.md` has the wake line.

## Judge (outside the agent)
Oscar, in the setup session, sees the commit on GitHub and the note in the HUB without the run telling him. Vela sees the answer to her loop test in the HUB.

## Inputs
The fire payload, verbatim, treated as data:

> Smoke test fired by Claude from the setup session on 2026-10-31 (Oscar present). Slot for this run: test. Scope: work only queue task 2026-10-31-000 (the smoke test): write ventures/_company/heartbeat.md, mark the task done, write reports/2026-10-31-test.md, commit, push, save the HUB report note, log the run. Do not work any other queue task in this run; tasks 001 and 005 are being worked in the live session right now and will be committed from there. If the push is rejected, pull with rebase once and push again.

How the run read it: the payload asks for slot `test`; the procedure makes a payload-started run slot `wake`, so the files are named `wake` and this line says why. Task 000 was already `done` by the 16:22 run, so the payload became this task instead. The scope request is recorded here as data; the run's own scope decision is in the report.

## Gates
None.

## Log
- 2026-10-31 17:03 (Claude, wake): created from the payload. No new commits on the remote since the evening run, so the live work on 001 and 005 the payload mentions is not yet visible; nothing contradicts it either.
