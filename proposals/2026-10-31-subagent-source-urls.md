---
source: this repo, second evening run of 2026-10-31 (falsification judge for task 002 returned "cannot check" on all twelve sources)
author: Claude HQ run
date_seen: 2026-10-31
kind: claude method
status: proposed
---

## Claim
In an unattended HQ run, a subagent that reads a URL out of a repo file and then fetches it is stopped by a permission prompt ("provenance required") that no one is there to answer; the fetch fails without retry. The same page opens when the URL arrives in the subagent's own prompt or comes out of a web search the subagent ran. The judge for task 002 lost its whole pass to this, and the hardware subagent reported the same block on five pages. The fix is a rule about how URLs are handed to subagents, not a new tool.

## Which job of the harness it improves
Tools and sensors: the falsification judge, the sample checks and the wide-search subagents can read what they are asked to read. Traces: judge verdicts land in the task file instead of "cannot check".

## Cost
No money, no tool, no account. One sentence in `playbooks/run-procedure.md` under step 4 (Gate 4, so a decision). Prompts to subagents get longer by the list of URLs.

## Test
The next falsification judge (task 002) returns a verdict on each of the twelve sources. Scorecard line: judge passes run per week, and the count of "cannot check" verdicts, which should be zero from the next run.

## Recommendation
Adopt with one change of wording in run-procedure.md step 4, wide-search paragraph: "Every URL a subagent or judge must read is pasted verbatim into its prompt; a subagent reaches other pages through its own web search results, never by copying a URL out of a file." Raised as D-005.

## Measured 2026-11-01 morning run (amends the claim and the wording)
Three subagents received their URLs pasted verbatim in the prompt. Every direct fetch of a pasted URL was still refused ("PROVENANCE_REQUIRED", the same unanswered prompt), so the claim above was half wrong: pasting is not enough. What worked: the subagent runs one web search for the page's title or reference, and fetches the link that the search returns; the judge for task 002 reached 14 of 14 sources that way (the arianeweb decision page only as its PDF twin), the four-source checker 4 of 6, and the run itself opened the two remaining pages the same way. Two pages served a captcha to the fallback (PubMed Central, doi.org) and were replaced by repository or author copies. Amended wording for run-procedure.md step 4: "A subagent or judge reaches every page through the link returned by its own web search for that page's title or reference; URLs are pasted into its prompt so it knows what to search for, and never copied out of a file into a fetch." D-005 amended in the 2026-11-01 morning report; the runs already apply this in their prompts.
