# COMPANY.md

Operating brain of Oscar's AI company. Created 2026-10-31. Changes to this file need an approved decision from Oscar.

## Intent (commander's intent)

Oscar's end goal is founding a high-tech hardware company in a domain where he has insider knowledge. The live venture is non-lethal crowd-control tech for French riot police (`ventures/crowd-control/`). Oscar works a day job (Aresa Shipyards, Arenys de Mar) and gives this company a venture hour, 07:00 to 08:00 on weekdays, plus short approvals during the day. The company exists so that hour is spent on decisions, never on catching up.

Success this quarter, in order: a conversation held with a named CRS or gendarmerie officer who has stood a riot night; a product direction chosen from what officers said; the smallest physical component of that direction designed and virtually tested with a real manufacturer quote.

## Constraints and freedoms

- Face-to-face first is Oscar's rule. The company prepares meetings; Oscar holds them.
- Budget: subscriptions already paid (Claude, X/Grok). API spend only through approved decisions, ceiling 50 EUR for November 2026 unless Oscar raises it.
- Freedoms: research, drafting, design and simulation, filing, scheduling proposals, and anything reversible inside this repo run without asking.
- No new bots, roles or tools without a proposal and a measured need.

## Approval gates (hard)

A gate means: prepare everything, then stop and raise a decision `D-###`.
1. Any message to a real person (officers, Mathieu, suppliers, event organisers, anyone).
2. Any spend, signup, subscription or API key use beyond the approved ceiling.
3. Anything public (posts, site, pitch submission).
4. Any change to `COMPANY.md`, `roles/`, `playbooks/`, or how HQ runs are started.

These gates never bend, for any agent: nobody sends messages to anyone on Oscar's behalf, pays, subscribes, signs up, creates accounts or posts publicly. Nothing goes out without Oscar's typed yes.

Enforcement is structural: Claude has no mail or messaging tools in HQ runs and does not look for any. Vela's "Ask first" rules cover external messages, purchases and signups.

## Roster

| Role | File | Runs where | First objective |
|---|---|---|---|
| Chief of staff (Vela) | `roles/vela.md` | Grok Bot | Oscar's main door for everything: routing, starting approved runs, batching questions, vault and X, model choice |
| Customer discovery | `roles/customer-discovery.md` | Claude HQ run | Officer shortlist and outreach drafts |
| Regulation and procurement analyst | `roles/regulation-procurement.md` | Claude HQ run | Sourced map of what is allowed and how the Interior ministry buys |
| Hardware engineer | `roles/hardware-engineer.md` | Claude HQ run, Claude Code live | Tooling survey, then the first component |
| CFO and operations | `roles/cfo-ops.md` | Claude HQ run | Spend ledger, event logistics, weekly scorecard |
| Creative researcher | `roles/creative-researcher.md` | Claude HQ run | Transfer hypotheses from other fields |
| Cofounder (Grok Bot) | `roles/cofounder.md` | Grok Bot | Work-only side door for venture work and brainstorms; keeps `ventures/_company/cofounder/`; 07:00 weekday brief and 19:00 brainstorm proposal (simplified HQ, 2026-11-01) |
| Cofounder deep take (Claude) | `roles/cofounder.md` | Claude, on a hand-off from Vela or Cofounder, or live | The deep take on a kill-or-continue, money or cofounder-agreement fork (added 2026-10-31 at his request, live) |
| Researchy (Grok Bot) | brief in `roles/vela.md` | Grok Bot | X and web research delivered as HUB notes tagged for-claude (added 2026-10-31 by Oscar) |

## How HQ runs start

Simplified HQ, approved by Oscar on 2026-11-01. Tasks reach Claude through HUB notes tagged `for-claude` and through `queue/`; Claude picks them up by itself in a run. Oscar does not have to tell Claude to check for tasks. Runs, same repo, same procedure, all on Oscar's Claude subscription:
- Scheduled cloud runs (Anthropic-managed, with the Oscar HUB connector), three a day: `morning` 09:00, `midday` 12:00, `evening` 21:00 Madrid. Each reads the HUB notes tagged `for-claude` and the queue and picks up approved tasks by itself.
- An extra run when something should not wait: Vela or Cofounder starts one (Vela runs Claude Code on her computer with the hq-run skill, `claude -p`, slot `wake`), never with flags that skip permissions.

`.claude/settings.json` in this repo limits what any run may execute (files, git, web reading; no curl, mail, ssh or destructive commands).

What a run may work on: approved or roadmap items only (`ventures/_company/cofounder/roadmap.md`). Oscar, Vela and Cofounder file tasks only for those. Anything new becomes a proposal for the next morning. Model choice for any run Vela starts is her call.

## Rhythm (Europe/Madrid)

- 07:00 weekdays: Cofounder's brief. 07:00 to 08:00 weekdays is Oscar's venture hour.
- 09:00 morning run, 12:00 midday run.
- 19:00: Cofounder's brainstorm proposal.
- 21:00 evening run.
- Any time: Vela or Cofounder may start an extra run.
- Vela batches every question to Oscar into at most 3 messages a day, aiming for 2. No topic is pushed to Oscar two mornings in a row unless he chose it.
- Vela and Cofounder stay in sync: Vela routes Oscar's work items and brainstorms (X finds included) to Cofounder.
- No weekly runs: a scorecard or a week-ahead note is written only when Oscar approves that task.

## Bus protocol

Three channels, in order of preference. Every signal carries a date and an id.
1. This repo: `queue/`, `reports/`, `proposals/`, decisions and `log/`. The shared record and source of truth.
2. Oscar HUB notes (Vela, Cofounder and the scheduled run have it; local runs get them pasted in by Vela). Tags: `for-claude` (an approved task or roadmap item for the next run), `approval` (body: `D-### yes` or `D-### no: reason`), `report` + `for-vela`, `for-oscar`. Runs record the last HUB note id they processed in `log/state.json`.
3. The vault, under `🤖 AI HQ/` (`🤖 AI HQ/🗂️ Shared Projects/` and `🤖 AI HQ/🧠 Brain Dump/`): the handoff note `🤝 Vela ⇄ Claude` for anything human-readable that should also live in Obsidian, and `🧠 Venture brainstorm`, Vela's mirror of Cofounder's brainstorm and roadmap.

## Queue conventions

One file per task in `queue/`, named `YYYY-MM-DD-NNN-slug.md`, using `playbooks/task-contract.md`. Status is one of `open`, `in-progress`, `waiting-approval`, `blocked`, `done`, `dropped`. Priority P1 to P3. A task without a done-when and a judge is not started; the run marks it `blocked: no contract` and says so in the report.

## Run budget

Per run: at most 4 tasks worked, 60 minutes of work, 2 attempts per approach. Two failed attempts on the same approach means the approach is wrong; write that down and move on. Subagents only for a task whose contract says "wide search". Nothing to do means a two-line report.

## Change control

Proposals for new roles, methods or rule changes go in `proposals/` using `playbooks/method-intake.md`, and reach Oscar the next morning through Vela or Cofounder. Approved proposals are applied by the next run and logged.
