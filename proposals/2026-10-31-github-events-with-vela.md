---
source: https://docs.x.ai/grok-bot/skills-routines-and-automations and https://docs.x.ai/grok-bot/security
author: xAI docs (checked 2026-10-31)
date_seen: 2026-10-31
kind: bridge method
status: proposed
---

## Claim
Grok Bot routines can be started by external events, GitHub events among them, and by a webhook (POST with a bearer key). Grok Bot also has a built-in GitHub connected app that acts as the signed-in member. If both hold for Vela's account, the bus can be event-driven: an HQ run comments on a signal issue in `oscar-hq`, Vela's routine fires at once and relays the report; Vela files tasks and approvals as issues and comments, which HQ runs read. No clock, no Mac, no HUB polling.

## Which job of the harness it improves
State (one place for queue, approvals and reports) and traces (every signal is a GitHub event with a timestamp and an author).

## Cost
Vela's GitHub app connected to Oscar's account with access to the private repo; one routine on her side; `log/state.json` `signal_issue` set; run procedure step 6.3 already written. No money.

## Test
Decisions answered within one Vela check instead of up to three hours; measured on the scorecard as median hours to answer.

## Simpler variant: fire the HQ run by HTTP
Claude Code cloud scheduled tasks accept an API trigger: `POST https://api.anthropic.com/v1/claude_code/routines/<trig_id>/fire` with a subscription OAuth token from `claude setup-token`, beta header `experimental-cc-routine-2026-04-01`, body `{"text": "..."}`; the text arrives in the run as an untrusted payload that the saved prompt must opt in to act on (https://code.claude.com/docs/en/routines). The HQ run prompt opts in (run-procedure step 0). One secret in Vela's store, one curl, no GitHub app needed. The reverse direction (Claude waking Vela) still needs her webhook or GitHub-event routine.

## Recommendation
Adopt the HTTP fire first if Vela can run a script with a stored secret: it is one secret and one command. Adopt the GitHub bus once Vela confirms (a) she can read and comment on issues in a private repo as Oscar and (b) a routine of hers fires on a GitHub event. Until then, HUB notes remain the bus and the clock remains the trigger.
