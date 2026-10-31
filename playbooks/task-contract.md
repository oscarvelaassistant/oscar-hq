# Task contract

Every queue file starts with this front matter and these sections. A task without `done_when` and `judge` is not started.

```markdown
---
id: 2026-10-31-001
title: Short imperative title
role: customer-discovery
priority: P1
status: open            # open | in-progress | waiting-approval | blocked | done | dropped
created: 2026-10-31
created_by: Oscar | Vela | Claude
due: 2026-11-03          # optional
wide_search: false       # true allows parallel subagents
approval: none           # none | D-012 yes | D-012 no: reason
---

## Goal
One paragraph: what should exist when this is done, and why it matters to the venture.

## Done when
Checkable statements. "A shortlist of 20 named officers with role, unit, years, source link, and a one-line hook each, saved at ventures/crowd-control/discovery/officers.md."

## Judge (outside the agent)
What, other than Claude or Oscar, shows the result is right. A reply from a real officer. A simulation that passes a stated test. A source document that says the thing. A second agent that tries to falsify the claims and fails.

## Inputs
Files, notes, links to start from. The rawest material available, not digests.

## Gates
Which approval gates this task will hit, and where it will stop to ask.

## Log
- YYYY-MM-DD HH:MM (Claude, slot): what happened, in one line.

## Decision
(Filled by the run when the task stops at a gate. Format in playbooks/decision-memo.md.)
```

Rules
- One task, one owner role, one outcome. Split anything with two outcomes.
- Prefer a hard, specific target over "do your best". Report honestly against it.
- Inputs name files and URLs, not "the usual sources".
