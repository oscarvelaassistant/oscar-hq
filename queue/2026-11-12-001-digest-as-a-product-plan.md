---
id: 2026-11-12-001
title: Plan Oscar's Digest as a product
role: cofounder
priority: P2
status: done
created: 2026-11-12
created_by: Oscar (HUB note 20261112130840286-c6cc2d47 via Vela, wake run)
wide_search: false
approval: "D-008 yes, modified (2026-11-12 14:55 Madrid, Oscar via Cofounder, relayed by Vela in the wake-2 payload): Phase 0 goes ahead, but the first tests write issues with Claude on Oscar's own subscription, no API key and no API spend for now. He was told that Anthropic's terms bar subscription use for issues made for other people and chose it anyway; recorded as his call. Cofounder logged it in ventures/_company/cofounder/decisions.md."
---

## Goal
A written plan for selling Oscar's Digest (the one-reader newspaper built in /workspace/digest and served by the oscar-digest Worker) as a product: personalised daily or weekly journal, the client picks length, style and topics. Oscar plus two friends, a third each, profits split three ways (Oscar's correction via Vela: a third each, not 30/30/30). Oscar builds. The plan covers: a new site and domain, a product account, automated digest creation, client onboarding (length, style, topics, daily or weekly), and how to build it.

## Done when
- `ventures/digest/plan.md` exists and covers the five areas Oscar listed, each with: what exists today, what to build, which gate it crosses, and a build order.
- Every cost in the plan is a quoted price with a URL, or marked unknown. No estimates.
- The deep take (cofounder shape, under 25 lines) is in the run report with one decision and one dated next action.
- Nothing is bought, registered, created or published by this task.

## Judge (outside the agent)
Oscar's answer to the decision in the report, and Cofounder recording it in decisions.md. A month on: did the next action happen on its date?

## Inputs
- HUB note 20261112130840286-c6cc2d47 (title "Plan Oscar's Digest as a product (Fable high)"), as relayed by Vela in the wake payload.
- ventures/_company/cofounder/brainstorm.md line of 2026-11-12.
- /workspace/digest/README.md (the current pipeline), /home/box/projects/oscar-digest/README.md (the Worker), /home/box/AgentConfig/hub/registry.json, /home/box/AgentConfig/docs/OSCAR-FEEDBACK.md.

## Gates
- Domain purchase: gate 2 (spend). Product account (Stripe or similar, email sender): gate 2 (signup). Public site: gate 3. API spend for generation beyond the 50 EUR ceiling: gate 2. The plan stops before all of them and names each as a later decision.

## Log
- 2026-11-12 14:13 (Claude, wake): filed from the wake payload, started.
- 2026-11-12 14:18 (Claude, wake): plan written at ventures/digest/plan.md (five areas, phases, gates, sourced prices, three open inputs). Done-when met except the judge, which is Oscar's answer. Stopped at gate 2 for the prototype's API spend: D-008 below.
- 2026-11-12 14:57 (Claude, wake-2): D-008 answered yes with a change (subscription, not API key, for the first tests). Judge met: Oscar answered and Cofounder recorded it. Task closed; the build spec is task 2026-11-12-002. The plan's section 2 now carries a pointer to the decision.

## Decision
### D-008 Start the Digest product prototype on an API key inside the November ceiling
- What: build Phase 0 of ventures/digest/plan.md: a fork of the pipeline that writes daily issues for three readers (Oscar and the two partners) on an Anthropic API key, spend inside the 50 EUR November ceiling, for four weeks. No site, no domain, nothing public, no other signup. If Oscar has no Console API key, this yes covers creating one.
- Why now: Anthropic's terms do not allow a subscription login to generate issues for other people (https://code.claude.com/docs/en/legal-and-compliance), so the test cannot run without a key; and the question the whole venture hangs on, whether two friends read it most mornings, is answered only by running it.
- Options: A) yes, Phase 0 for four weeks, measured; B) hold until the partners have written what each brings; C) no, plan stays on file.
- Recommendation: A. The cost is capped by the ceiling and four weeks of the venture hour; the result decides whether a domain is worth buying.
- Reversible: yes. The fork is deleted, the key is revoked, the personal Digest is untouched.
- Decide by: 2026-11-14 08:00. Default if silent: B, hold, no spend.
