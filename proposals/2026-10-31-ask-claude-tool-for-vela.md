---
source: Oscar, 2026-10-31 ("Vela has access to my Claude account, I logged into it from her Linux laptop"); https://docs.x.ai/grok-bot/computer-and-apps
author: Oscar; xAI docs (checked 2026-10-31)
date_seen: 2026-10-31
kind: bridge method
status: proposed
---

## Claim
Claude Code is logged in with Oscar's subscription on Vela's cloud computer. So Vela can run full HQ runs (`claude -p` inside a clone of this repo) and answer quick questions with Claude quality, with no API key and no API spend. This supersedes the earlier idea of an HTTP "ask Claude" tool with an API key.

## Which job of the harness it improves
Permissions: the run executes under this repo's `.claude/settings.json` allow and deny lists, enforced by Claude Code, not by the prompt. Traces: every run commits to the repo. State: same repo as the cloud runs.

## Cost
No money. A GitHub clone on Vela's computer with push access (Oscar sets up GitHub there once). Oscar's Claude login lives on a machine shared by all his bots (xAI docs: separate bots are not a security boundary); usage counts against his weekly pool.

## Test
A task given to Vela in chat produces a commit in `oscar-hq` and a report she relays, within the same conversation. Scorecard: median hours from task to first result.

## Recommendation
Adopt now, with three safeguards: keep `.claude/settings.json` as the only permission source (no skip-permissions flags), keep Oscar's Claude login off every other bot's tasks (Vela only), and review the weekly usage pool on the Friday scorecard. Reject the API-key variant unless the subscription pool runs out.
