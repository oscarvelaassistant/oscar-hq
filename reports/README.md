# Reports

One file per run: `YYYY-MM-DD-<slot>.md` (`morning`, `midday`, `evening`, `test`). Weekly: `scorecard-YYYY-Www.md`. The morning report is the one Oscar reads in his window; keep it under 40 lines unless decisions need the room.

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

## Next run
- What the 12:00 run will do if the decisions above come back.
```

Nothing to report: two lines, "Nothing new. Next run <slot>."

## Weekly scorecard (Friday evening run)
- Tasks: opened, done, dropped, blocked, median hours from open to done.
- Decisions: raised, answered, median hours to answer, defaults applied in silence.
- Venture: objective 1 status (officer named? date set? conversation held?), product direction status, component status.
- Spend: API EUR, subscriptions.
- Methods adopted in the last four weeks and their measured effect.
- Postmortem lines: one per failed task (what failed, what changed so it will not repeat).
