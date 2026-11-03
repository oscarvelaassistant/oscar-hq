---
source: this repo, HUB notes 20261102111321456-992d70de (2026-11-02 midday) and 20261103110539606-4f947f63 (2026-11-03 midday)
author: Claude HQ run (evening, 2026-11-03)
date_seen: 2026-11-03
kind: tool
status: proposed
---

## Claim
The midday scheduled run (12:00 Madrid) cannot push to oscar-hq. On 2026-11-02 and again on 2026-11-03 its clone worked read-only and `git push` was refused twice with HTTP 403: "oscarvelaassistant/oscar-hq is not in this session's authorized repository set ... add the repository to the session's sources". The session had no add_repo tool to attach it. The morning and evening scheduled runs push without trouble (this evening session also had no add_repo tool, but the repository was already attached with push access). Each time, the midday run saved its report to the HUB and the evening run recreated its three edits by hand. Key line: "not in this session's authorized repository set".

## Which job of the harness it improves
Tools and state: the midday run would write to the shared record itself instead of leaving a recovery job for the evening run. Traces: `reports/` and `log/runs.md` would be complete at 12:00 instead of 21:00.

## Cost
No money, no new tool, no account. One change in how HQ runs are started (gate 4, Oscar's decision): the midday scheduled task's session sources get oscar-hq with push access, the same as the morning and evening tasks. Oscar or Vela makes the change in the task's settings; a run cannot change a scheduled task.

## Test
The next midday run pushes its own commit and its `log/runs.md` line says so; no "push refused" in a midday HUB note for a week. Scorecard line, when one is approved: runs that needed recovery by another run, which should go to zero.

## Recommendation
Adopt as written. Raised as D-006 in reports/2026-11-03-evening.md.
