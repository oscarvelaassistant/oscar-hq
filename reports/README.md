# Reports

One file per run: `YYYY-MM-DD-<slot>.md` (`morning` 08:00, `midday` 12:00, `evening` 21:00, `wake` for an extra run Vela or Cofounder starts, `test`). A second run on the same day and slot adds `-2`, `-3`. Weekly: `scorecard-YYYY-Www.md`, only when Oscar approves that task. Oscar does not read reports directly: Vela batches their decisions to him. Keep a report under 40 lines unless decisions need the room.

## Format

```markdown
# HQ report 2026-11-01 morning

## Decisions needed
### D-001 ...
(decision memos, playbooks/decision-memo.md; omit the section when there are none)

## Done since last report
- 2026-10-31-001 Officer shortlist: 18 named, 12 with LinkedIn, saved at ventures/crowd-control/discovery/officers.md. Judge pending: first reply.

## In progress
- ...

## Blocked
- ... (what is missing, who can unblock)

## Spend
- API: 0.00 EUR this month (ceiling 50). Subscriptions: no change.

## Proposals
- Anything new this run thought of, one line each (file in `proposals/` when it needs more). Not worked until Oscar approves.

## Next step
- What the next run will do if the decisions above come back.
```

Nothing to report: two lines, "Nothing new. Waiting on <what>."

## Weekly scorecard (when Oscar approves a scorecard task)
- Tasks: opened, done, dropped, blocked, median hours from open to done.
- Decisions: raised, answered, median hours to answer, defaults applied in silence.
- Venture: objective 1 status (officer named? date set? conversation held?), product direction status, component status.
- Spend: API EUR, subscriptions.
- Methods adopted in the last four weeks and their measured effect.
- Postmortem lines: one per failed task (what failed, what changed so it will not repeat).
