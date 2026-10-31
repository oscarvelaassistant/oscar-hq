# Run procedure (the HQ run)

The runbook every scheduled Claude run follows. The scheduled task's prompt only points here, so changing this file changes the company's behaviour. Keep it under 80 lines.

## 0. Identify the run
Slot is `morning` (06:00), `midday` (12:00) or `evening` (20:00), from the clock in Europe/Madrid. Date `YYYY-MM-DD`. A test run is slot `test`.

## 1. Get the repo
Attach the repository `oscar-hq` (owner: Oscar's GitHub account) with push access and clone it. If this fails: write a HUB note titled `HQ run <date> <slot>: blocked, repo unreachable`, tags `report, for-vela, blocked`, and stop.

## 2. Read
`COMPANY.md`, `log/state.json`, every `queue/*.md` with status `open`, `in-progress` or `waiting-approval`. Nothing else yet.

## 3. Ingest signals
- HUB notes created after `state.last_hub_note` with tag `for-claude`: each becomes a queue file (status `open`, role chosen from the roster, P2 unless the note says otherwise). A note that is a question, not a task, is answered in the report.
- HUB notes tagged `approval`: apply `D-### yes` or `D-### no` to the matching task (`waiting-approval` becomes `in-progress` or `dropped`). Record the reason given.
- Queue files whose front matter `approval:` field changed since last run: same.
- Update `state.last_hub_note` only after the queue files are written.

## 4. Work
Order: P1 before P2 before P3; within a priority, oldest first. For each task, up to the run budget in `COMPANY.md`:
1. Read the task's role file fully. Read the venture folder files the task names. Nothing more.
2. Do the work. Write outputs where the role file says (never only in the report).
3. Check against the task's `done_when` and run its `judge` where it can be run now. State the result honestly; a missed target with real numbers is a good result, a faked one is not.
4. If the next step crosses a gate, stop there, set status `waiting-approval`, and write the decision memo (`playbooks/decision-memo.md`) inside the task file under `## Decision`.
5. Update the task's status and `log:` line.

Wide-search tasks (contract says so) may use parallel subagents, each with one narrow question and the role file; merge their results yourself and cite sources.

## 5. Report
Write `reports/<date>-<slot>.md` using the format in `reports/README.md`. Decisions first, numbered `D-###` continuing from `state.next_decision`. The morning report is the only one that may exceed 40 lines. Nothing to report means two lines.

## 6. Publish
1. `git add -A && git commit -m "HQ run <date> <slot>: <one line>"` and push. If the push is rejected, pull with rebase once and push again; if it fails twice, write the report to the HUB and stop.
2. Save a HUB note: title `HQ report <date> <slot>`, body = the report, tags `report, for-vela`. Add tag `decisions` when the report contains any `D-###`.
3. If GitHub issues are enabled for signalling (see `log/state.json` `signal_issue`), add a comment on that issue with the report's first 20 lines, so Vela's GitHub-event routine fires.

## 7. Log
Append one line to `log/runs.md`: `<date> <slot>: tasks worked N, done N, waiting N, blocked N, decisions D-### to D-###, duration`. Update `log/state.json`.

## Failure rules
- Two failed attempts on the same approach: stop that approach, record it in the task file, continue with the next task.
- A tool or source that is unreachable is reported as unreachable, never worked around by inventing content.
- Every failure that will recur becomes a line in `proposals/` (what to change in a playbook or tool), not a repeat.
