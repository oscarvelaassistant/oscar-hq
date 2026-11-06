---
source: this repo (COMPANY.md Rhythm, reports/README.md) and the evening scheduled task's stored prompt as delivered to the 2026-11-06 evening run
author: Claude HQ run (evening, 2026-11-06)
date_seen: 2026-11-06
kind: tool
status: proposed
---

## Claim
The evening scheduled task's prompt says: "on Fridays this run also writes the weekly scorecard as reports/README.md describes". COMPANY.md (Rhythm) says: "No weekly runs: a scorecard or a week-ahead note is written only when Oscar approves that task." reports/README.md says the same ("only when Oscar approves that task"), and roles/cfo-ops is the role that writes it when approved. No scorecard task is filed in queue/ and no for-claude note asks for one. The two texts disagree every Friday. The 2026-11-05 evening run noted it; this run did not write a scorecard, following COMPANY.md. Key line: "written only when Oscar approves that task".

## Which job of the harness it improves
Contract: one rule for the Friday evening run instead of two that disagree. Traces: a scorecard that exists because Oscar asked for it, or a prompt that no longer promises one.

## Cost
No money, no new tool, no account. One gate 4 change, Oscar's decision, either way: A) edit the Rhythm line in COMPANY.md and the weekly line in reports/README.md so the Friday evening run writes the scorecard without a task (applied by the next run after a yes, logged); or B) Oscar or Vela removes the Friday clause from the evening scheduled task's prompt (a run cannot change a scheduled task).

## Test
No Friday evening report mentions the conflict again. If A: a `reports/scorecard-YYYY-Www.md` exists by 21:30 Madrid every Friday, with counts taken from queue/ and log/, never from memory. If B: the evening prompt and COMPANY.md say the same thing and the scorecard appears only on an approved task.

## Recommendation
B, remove the clause from the prompt. The company has had no open task since 2026-11-02 and roadmap.md is still the placeholder, so a scorecard this week would be mostly zeros and a repeat of log/runs.md. When the roadmap fills, Oscar files a scorecard task once and the cfo-ops role writes it from the files, as COMPANY.md already allows. The tradeoff: with B, nothing reminds Oscar to ask for a scorecard; with A, he gets one every Friday whether or not the week had work. Raised as D-007 in reports/2026-11-06-evening.md.
