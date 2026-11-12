---
id: 2026-11-12-002
title: Write the Phase 0 build spec for the Digest product (front end, customer journey, cloud backend)
role: cofounder
priority: P2
status: done
created: 2026-11-12
created_by: Oscar (answer to D-008 via Cofounder, relayed by Vela in the wake-2 payload, 14:55 Madrid)
wide_search: false
approval: "D-008 yes, modified (2026-11-12 14:55, Oscar via Cofounder and Vela): Phase 0 approved; first tests on Oscar's own Claude subscription, no API key, no API spend. Told about Anthropic's terms, his call."
---

## Goal
A build spec, following ventures/digest/plan.md, that a Claude Code build session on the box can execute without new decisions, for (1) the front end and the whole customer journey (landing, sign-up and onboarding form, preferences, the issue reader and archive, the account) and (2) the cloud backend (Cloudflare Worker, KV, auth, the per-client pipeline, delivery). The per-client pipeline writes issues with Claude on Oscar's own account (subscription, `claude -p`), not an API key, as Oscar decided in D-008. Spec only: nothing public, no sign-ups, no spend, no deploys, no issues generated for anyone in this run.

## Done when
- `ventures/digest/spec.md` exists with: the customer journey screen by screen (landing, sign-up, onboarding form, preferences, reader, archive, account), the data model (every KV key, every profile field), every Worker route with method, auth and body, the auth model, the per-client pipeline stage by stage with the subscription-based writing step, delivery, the test plan, the build order with gates, and what each phase leaves out.
- Every limit or price in the spec is quoted with a URL or marked unknown. No estimates.
- The terms fact and Oscar's call are recorded in the spec and in plan.md, with the date and channel.
- Nothing is deployed, registered, created, sent or generated for anyone by this task.

## Judge (outside the agent)
The build session that follows this spec: it either builds Phase 0 from the spec without raising a new decision, or it lists the gaps. A month on: did the three readers get issues through the pipeline the spec describes?

## Inputs
- ventures/digest/plan.md (the plan this spec follows); ventures/_company/cofounder/decisions.md (D-008 line).
- /workspace/digest/README.md, daily.sh, DAILY-PROMPT.md, profile.md (the one-reader pipeline).
- /home/box/projects/oscar-digest/README.md and worker.js (the Worker: token model, KV layout, ETag handling).
- /home/box/AgentConfig/docs/OSCAR-FEEDBACK.md (standing design feedback); playbooks/design.md.
- /home/box/AgentConfig/hub/registry.json (hub rule, the oscar-digest service entry).

## Gates
- None crossed by this task. The spec names the gates the build will hit: domain purchase (gate 2), anything public (gate 3), Stripe and Resend sign-ups (gate 2), any API key or API spend (gate 2, the backend swap the spec keeps ready).

## Log
- 2026-11-12 14:57 (Claude, wake-2): filed from the wake-2 payload, started.
- 2026-11-12 15:20 (Claude, wake-2): spec written at ventures/digest/spec.md (13 sections: decision record, architecture, placement, KV data model with write counts, every Worker route, the customer journey screen by screen, the per-client pipeline with the subscription-based writer, delivery, auth, front-end, test plan, build order, risks, open inputs). Limits quoted from Cloudflare and Claude Code docs with URLs; Cloudflare Access free-plan user count marked unknown. plan.md sections 2 and 7 now point to D-008 and the spec. Done-when met except the judge (the build session). Nothing deployed, created, sent or generated.
