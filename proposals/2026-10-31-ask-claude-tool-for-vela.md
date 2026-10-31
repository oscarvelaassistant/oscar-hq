---
source: https://docs.x.ai/grok-bot/vault and https://docs.x.ai/grok-bot/computer-and-apps
author: xAI docs (checked 2026-10-31)
date_seen: 2026-10-31
kind: bridge method
status: proposed
---

## Claim
Grok Bot stores API keys in a masked secret card the model never sees, and bots can add MCP servers by URL or by a command run on the shared cloud computer. If a script on that computer can read a stored key as an environment variable (not documented as of 2026-10-31), Vela can call the Anthropic API directly for an instant Claude-quality draft or answer inside Oscar's chat, without waiting for an HQ run.

## Which job of the harness it improves
None of the seven directly; it improves Oscar's chat experience (quality of quick answers) and removes some tasks from the queue. That is why it stays optional and capped.

## Cost
Oscar's Anthropic API key placed in Vela's secret store; API spend against the 50 EUR November ceiling; one more place a key lives (Grok docs state separate bots are not a security boundary and the computer is shared across bots).

## Test
Spend stays under the ceiling; Oscar reports whether the drafts are good enough that fewer quick tasks reach the queue (count of `for-claude` notes that are quick questions, before and after).

## Recommendation
Adopt only if Vela confirms a script can consume a stored secret, and only with a monthly spend limit set on the Anthropic console. Otherwise reject without regret: the HQ runs already use Claude on the subscription.
