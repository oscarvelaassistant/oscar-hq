# oscar-hq

Headquarters of Oscar Bonnefon's AI company. The company works on his ventures while he is at work; he makes the decisions in his venture hour (07:00 to 08:00 on weekdays) and during coffee breaks, through Vela, his Grok Bot chief of staff and main door. Innovator, a work-only Grok Bot, is the side door for venture work and brainstorms.

This repository is the company's shared state. Every agent that works here reads `COMPANY.md` first.

## Layout

| Path | What it holds | Who writes it |
|---|---|---|
| `COMPANY.md` | Intent, roster, rhythm, approval gates, bus protocol | Oscar (changes need his approval) |
| `roles/` | One file per role: mission, inputs, outputs, done-when, judge, gates | Proposed by Claude, approved by Oscar |
| `playbooks/` | How things are done: run procedure, task contract, decision memo, harness checklist, method intake | Same |
| `queue/` | Tasks as markdown files, one per task, status in the front matter | Vela, Innovator, Claude, Oscar |
| `reports/` | One report per run, newest first | Claude |
| `log/` | Run log and `state.json` (last processed signals) | Claude |
| `proposals/` | Proposed changes to the company itself (new role, new method, rule change), waiting for Oscar | Claude, Vela |
| `ventures/<name>/` | Work product per venture (research, interview notes, designs, BOMs) | Claude |
| `.claude/` | Claude Code subagents and settings so a Claude Code session on this repo can delegate by role | Claude |

## How a task moves

1. Oscar approves a task (to Vela, to Innovator, or from a morning brief or proposal): it lands in `queue/` or as a HUB note tagged `for-claude`.
2. The next Claude HQ run picks it up by itself, without Oscar asking: either Vela or Innovator starts an extra one right away (Claude Code on Vela's computer, `claude -p` with Oscar's subscription, hq-run skill), or the next scheduled run does (09:00, 12:00 and 21:00 Madrid). The run reads the role file, does the work, writes the output under `ventures/`, and sets the task status.
3. The run writes `reports/<date>-<slot>.md`. Anything that needs Oscar is a numbered decision (`D-###`); anything new Claude thought of is a proposal.
4. Vela batches decisions into her messages to Oscar (at most 3 a day, aiming for 2); he answers in chat; Vela records the answer (a HUB note tagged `approval`, or `queue/` front matter). The next run acts on it.

## Principles (short)

- One loop with role playbooks loaded on demand; parallel subagents only for wide searches. (Anthropic's 2026 guidance, summarised in Oscar's vault note "Anthropic on subagents and agent architecture".)
- Verification is the job: every task has a done-when and an outside judge before it starts. (grokbot-field-notes, MIT, and the harness checklist in `playbooks/harness-checklist.md`.)
- Gates are enforced by who holds the tools, not by prompts: Claude drafts, never sends; Vela asks first before anything external.
- Approved work only: agents work on approved or roadmap items; new ideas become proposals for the next morning.
- Quiet on no-op: a run that finds nothing to do writes a two-line report and stops.
- Adding a role or a method means adding one file. Nothing else changes.
