# Decision memo

How anything that needs Oscar is presented. One screen on a phone. Vela reads these aloud or pastes them; Oscar answers "D-012 yes", "D-012 no", or "D-012 option B".

```markdown
### D-012 Send outreach to the first five officers
- What: send the five French LinkedIn messages in ventures/crowd-control/discovery/outreach-batch-1.md from Oscar's account.
- Why now: calls are wanted before Euronaval (3 to 6 Nov); replies take days.
- Options: A) send all five; B) send two, wait for tone feedback; C) hold.
- Recommendation: A. Each message is under 80 words, names a specific unit or event, asks for 20 minutes, no product pitch.
- Reversible: yes, except that a message once sent is sent.
- Decide by: 2026-11-02 08:00. Default if silent: hold.
```

Rules
- Numbering `D-###` is global across all reports; the next number is in `log/state.json`.
- One decision per memo. A memo with "and" in the title is two memos.
- The recommendation is a real one, with the tradeoff stated. No balanced non-recommendations.
- "Default if silent" is always the safe side of the gate (hold, do not send, do not spend).
- The answer is recorded in the task file's `approval:` field with date and channel (chat via Vela, HUB note, repo edit).
