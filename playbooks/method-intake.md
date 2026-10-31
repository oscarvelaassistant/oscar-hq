# Method intake

How a method Oscar finds on X (or anywhere) becomes part of the company, without Oscar editing files.

## Flow
1. Oscar sends the post to Vela, or bookmarks it on X. Vela files it in the vault brain dump as she does now, and adds a HUB note tagged `for-claude` and `method` with the link and one line on what it claims.
2. The next HQ run writes `proposals/<date>-<slug>.md` with the form below and raises a decision `D-###` only if it recommends adoption. Rejections are listed in the report in one line each.
3. On `yes`, the following run applies the change (a new or edited playbook, role file, routine text for Vela, or scheduled-run prompt), logs it, and names the measurement that will show whether it helped.
4. The Friday scorecard reports the measurement for every method adopted in the last four weeks. A method with no effect is reverted by proposal.

## Form
```markdown
---
source: https://x.com/...
author: @handle (and who they are, if verifiable)
date_seen: 2026-10-31
kind: grok-bot method | claude method | bridge method | tool
status: proposed | adopted | rejected | reverted
---

## Claim
What the source says works, in one paragraph, with the verbatim key line (under 15 words).

## Which job of the harness it improves
Contract, map, tools, state, sensors, permissions, budget, traces, or none (then reject).

## Cost
Setup steps, money, new tool or account, new attack surface.

## Test
How we will know it helped: the scorecard line it should move, and by when.

## Recommendation
Adopt as written | adopt with changes (say which) | reject (say why). One real recommendation.
```

## Standing rejections
- Anything that adds a bot, a dashboard or a tool without a named failure it fixes.
- Anything that moves a gate from "ask first" to "allow" for messages, money, permissions or publishing.
- Role play dressed as method: new vocabulary without a new instrument or a new check.
