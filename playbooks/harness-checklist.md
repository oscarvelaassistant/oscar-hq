# Harness checklist

The test every task, role, routine and proposal passes before it runs unattended. Compiled from Oscar's vault captures: the seven jobs of a harness ("Harness Engineering: How to Build AI Agents That Don't Fall Apart", @0xwhrrari, https://x.com/0xwhrrari/status/2093685107534000560, and Annie Wang's course, https://x.com/anniewangtech/status/2116203053464363125), the grokbot-field-notes rules (MIT, https://github.com/unicodef1wn/grokbot-field-notes), and Anthropic's 2026 guidance as summarised in the vault note "Anthropic on subagents and agent architecture (X, 2025-2026)".

## Before it runs
- [ ] Contract: the request is a task file with a done-when and an outside judge.
- [ ] Small map: the agent is pointed at one role file and the named inputs, not the whole repo.
- [ ] Tools with failure states: each tool the task needs is listed, and what to do when it fails is written.
- [ ] Durable state outside the chat: outputs go to files in this repo, never only into a reply.
- [ ] Sensors before autonomy: a test, a validator, a second-agent falsification pass, or a human reply is named as the judge.
- [ ] Permissions outside the model: the gates the task will hit are listed; the tools that could cross them are not available to the run.
- [ ] Budget: attempts capped (two per approach), time capped, token fan-out only if the contract says wide search.

## After it runs
- [ ] Proof attached: the output links the source, the artifact, or the measurement that shows it is done.
- [ ] Traces: one log line per run, one line per failure in the task file.
- [ ] Failure becomes a fix: a recurring failure becomes a proposal to change a playbook, a tool or a rule, never a retry.
- [ ] Quiet on no-op: nothing important means a two-line report.

## Architecture rules (2026)
- One agent loop with skills loaded on demand is the default. Fan out to subagents only for breadth-heavy search where the extra tokens buy coverage (Anthropic's bug-hunt numbers: a single agent found 14, 15 and 27 of 70 planted bugs; a workflow found 66 each run, @ClaudeDevs 2026-10-09).
- Progressive disclosure: name and one-line description first, full file only when relevant. Keep role and playbook files short; most are too big.
- One owner per stage, handoffs for cross-role work, a human gate on messages, money, permissions and anything irreversible.
- Build a verification loop before building a second agent.
