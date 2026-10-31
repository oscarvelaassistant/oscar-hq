# COMPANY.md

Operating brain of Oscar's AI company. Created 2026-10-31. Changes to this file need an approved decision from Oscar.

## Intent (commander's intent)

Oscar's end goal is founding a high-tech hardware company in a domain where he has insider knowledge. The live venture is non-lethal crowd-control tech for French riot police (`ventures/crowd-control/`). Oscar works a day job (Aresa Shipyards, Arenys de Mar) and can give this company one hour in the morning plus short approvals during the day. The company exists so that hour is spent on decisions, never on catching up.

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
4. Any change to `COMPANY.md`, `roles/`, `playbooks/`, or the scheduled runs themselves.

Enforcement is structural: Claude has no mail or messaging tools in HQ runs and does not look for any. Vela's "Ask first" rules cover external messages, purchases and signups.

## Roster

| Role | File | Runs where | First objective |
|---|---|---|---|
| Chief of staff (Vela) | `roles/vela.md` | Grok Bot | Front door, routing, relaying decisions, vault and X |
| Customer discovery | `roles/customer-discovery.md` | Claude HQ run | Officer shortlist and outreach drafts |
| Regulation and procurement analyst | `roles/regulation-procurement.md` | Claude HQ run | Sourced map of what is allowed and how the Interior ministry buys |
| Hardware engineer | `roles/hardware-engineer.md` | Claude HQ run, Claude Code live | Tooling survey, then the first component |
| CFO and operations | `roles/cfo-ops.md` | Claude HQ run | Spend ledger, event logistics, weekly scorecard |
| Creative researcher | `roles/creative-researcher.md` | Claude HQ run | Transfer hypotheses from other fields |
| Cofounder (sparring partner) | `roles/cofounder.md` | Claude, on demand via Vela, live, and Sunday evening run | Turn Oscar's braindumps into one decision with a date (added 2026-10-31 at his request, live) |
| Researchy (Grok Bot) | brief in `roles/vela.md` | Grok Bot | X and web research delivered as HUB notes tagged for-claude (added 2026-10-31 by Oscar) |

## Where HQ runs happen

Two places, same repo, same procedure, both on Oscar's Claude subscription:
- Cloud scheduled runs (Anthropic-managed, no dependence on any machine): the fixed rhythm below. They have the Oscar HUB connector.
- Vela's computer, on demand: Claude Code is logged in there with Oscar's account. When Oscar gives Vela a task, she pulls the repo and runs `claude -p` with the HQ run prompt (slot `wake`), then relays the report from the output. `.claude/settings.json` in this repo limits what any run may execute (files, git, web reading; no curl, mail, ssh or destructive commands).

## Rhythm (Europe/Madrid)

- 06:00 cloud run: overnight work closed out, morning report written. This is the report Oscar reads.
- During the day: Vela runs Claude on demand for new tasks and approvals (replaces a fixed midday run).
- 20:00 cloud run: day closed out, queue set for the night.
- Vela: relays each report's decisions to Oscar; records his answers. Her schedule is in `roles/vela.md`.
- Sunday 20:00 run also writes the cofounder's `week-ahead.md`: the one decision for the week.
- Friday 20:00 run also writes the weekly scorecard (`reports/scorecard-<week>.md`) and a postmortem line per failed task.

## Bus protocol

Three channels, in order of preference. Every signal carries a date and an id.
1. This repo: `queue/` files and `reports/`. Source of truth.
2. Oscar HUB notes (both agents have it). Tags: `for-claude` (a task or message for the next run), `approval` (body: `D-### yes` or `D-### no: reason`), `report` + `for-vela` (a run's report for Vela to relay), `for-oscar` (Vela's own notes to Oscar). Runs record the last HUB note id they processed in `log/state.json`.
3. The vault handoff note `🤝 Vela ⇄ Claude` for anything human-readable that should also live in Obsidian. Vela mirrors Status and Next steps of `💡 InnovationHub` from each morning report.

## Queue conventions

One file per task in `queue/`, named `YYYY-MM-DD-NNN-slug.md`, using `playbooks/task-contract.md`. Status is one of `open`, `in-progress`, `waiting-approval`, `blocked`, `done`, `dropped`. Priority P1 to P3. A task without a done-when and a judge is not started; the run marks it `blocked: no contract` and says so in the report.

## Run budget

Per run: at most 4 tasks worked, 60 minutes of work, 2 attempts per approach. Two failed attempts on the same approach means the approach is wrong; write that down and move on. Subagents only for a task whose contract says "wide search". Nothing to do means a two-line report.

## Change control

Proposals for new roles, methods or rule changes go in `proposals/` using `playbooks/method-intake.md`, and appear as a decision in the next report. Approved proposals are applied by the next run and logged.
