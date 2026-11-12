---
id: 2026-11-12-003
title: Fold Oscar's answers into the Digest Phase 0 spec and switch the MVP delivery to PDF by email
role: cofounder
priority: P2
status: done
created: 2026-11-12
created_by: Oscar (answers to spec section 13 via Cofounder, relayed by Vela in the wake-3 payload, 15:09 Madrid)
wide_search: false
approval: "D-009 (2026-11-12 15:11 Madrid, Oscar via Cofounder, logged by Vela in ventures/_company/cofounder/decisions.md, commit 749fd61): test PDFs are emailed from Oscar's own Gmail to Oscar, Paul and Pietro, no mail service sign-up; all issues in English. The payload (15:09) asked this run to raise the provider decision; the log line two minutes later answers it, so it is applied and not raised again."
---

## Goal
`ventures/digest/spec.md` carries Oscar's four answers (hostname, client 1, the failure text, the two partners) and the scope change: the MVP delivers each issue as a PDF by email, from Oscar's own Gmail account, with no mail service sign-up (D-009). `plan.md` says the same where it said "no email". The spec still contains, for the later Phase 2 decision, the email providers with quoted prices and URLs, so the next decision memo can be written from it without new research. Spec only: nothing public, no sign-ups, no spend, no deploys, no emails sent.

## Done when
- Spec section 13's four open inputs are replaced by the answers, with date and channel.
- Every "no email in Phase 0" statement in spec.md and plan.md is replaced by PDF-by-email delivery, and the data model, routes, pipeline, journey, privacy, tests, build order and risks reflect it.
- A provider table with quoted prices and URLs exists in the spec for the Phase 2 decision; sources that could not be fetched are marked so.
- Nothing sent, deployed, registered or created.

## Judge (outside the agent)
The build session: it builds the email step from the spec without a new decision. Oscar: the first test issue arrives in his own inbox as a PDF from his Gmail.

## Inputs
- The wake-3 payload (Oscar's answers via Cofounder, relayed by Vela, 15:09).
- ventures/_company/cofounder/decisions.md (D-008 and D-009 lines).
- ventures/digest/spec.md, ventures/digest/plan.md.
- Price and limit pages fetched this run (URLs in spec section 7).

## Gates
- None crossed. The email step sends only when the runner is started by Oscar in build step 3, from his own account, to the three readers he named: his decision D-009. Any mail service sign-up stays gate 2 (Phase 2).

## Log
- 2026-11-12 15:11 (Claude, wake-3): filed from the wake-3 payload, started. D-009 found already logged (commit 749fd61, 15:11), applied as the approval.
- 2026-11-12 15:17 (Claude, wake-3): spec.md updated (sections 0 to 13: D-009 record, Gmail delivery from the box, profile and job fields, `emailed` route, late-issue retry schedule with Oscar's text, English only, provider table with prices for Phase 2, risks, answers in place of open inputs). plan.md sections 4, 6, 7 and open inputs updated. Done-when met except the judge. Nothing sent or deployed.
