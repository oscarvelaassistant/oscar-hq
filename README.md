# oscar-hq

Headquarters of Oscar Bonnefon's AI company. The company works on his ventures while he is at work; he makes the decisions in a one-hour morning window and during coffee breaks, through one chat (Vela, his Grok Bot chief of staff).

This repository is the company's shared state. Every agent that works here reads `COMPANY.md` first.

## Layout

| Path | What it holds | Who writes it |
|---|---|---|
| `COMPANY.md` | Intent, roster, rhythm, approval gates, bus protocol | Oscar (changes need his approval) |
| `roles/` | One file per role: mission, inputs, outputs, done-when, judge, gates | Proposed by Claude, approved by Oscar |
| `playbooks/` | How things are done: run procedure, task contract, decision memo, harness checklist, method intake | Same |
| `queue/` | Tasks as markdown files, one per task, status in the front matter | Vela, Claude, Oscar |
| `reports/` | One report per run, newest first; the morning one is the one Oscar reads | Claude |
| `log/` | Run log and `state.json` (last processed signals) | Claude |
| `proposals/` | Proposed changes to the company itself (new role, new method, rule change), waiting for Oscar | Claude, Vela |
| `ventures/<name>/` | Work product per venture (research, interview notes, designs, BOMs) | Claude |
| `.claude/` | Claude Code subagents and settings so a Claude Code session on this repo can delegate by role | Claude |

## How a task moves

1. Oscar tells Vela, or writes it himself: a task file lands in `queue/` (or a HUB note tagged `for-claude`, which the next run imports).
2. A scheduled Claude run picks it up, reads the role file, does the work, writes the output under `ventures/` or `research/`, and sets the task status.
3. The run writes `reports/<date>-<slot>.md`. Anything that needs Oscar is a numbered decision (`D-###`) in that report.
4. Vela relays decisions to Oscar's phone; he answers in chat; Vela records the answer (`queue/` front matter or a HUB note tagged `approval`). The next run acts on it.

## Principles (short)

- One loop with role playbooks loaded on demand; parallel subagents only for wide searches. (Anthropic's 2026 guidance, summarised in Oscar's vault note "Anthropic on subagents and agent architecture".)
- Verification is the job: every task has a done-when and an outside judge before it starts. (grokbot-field-notes, MIT, and the harness checklist in `playbooks/harness-checklist.md`.)
- Gates are enforced by who holds the tools, not by prompts: Claude drafts, never sends; Vela asks first before anything external.
- Quiet on no-op: a run that finds nothing to do writes a two-line report and stops.
- Adding a role or a method means adding one file. Nothing else changes.
