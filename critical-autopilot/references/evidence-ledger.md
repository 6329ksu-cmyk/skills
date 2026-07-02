# Evidence Ledger

Use this only when the work is long, resumed, or likely to be challenged. Keep it compact. The ledger can live in the final brief, in memory, or in a temporary note when a multi-turn handoff needs it.

## Minimal Shape

```
Objective: ...
Current decision: handled / blocked / operator action needed
Latest user steering: ...
Verified:
- ...
Inferred:
- ...
Unverified:
- ...
Changed:
- ...
Highest-risk remaining:
- ...
Next action:
- ...
```

## Rules

- Keep verified, inferred, and unverified claims separate.
- Prefer evidence that can be rerun: commands, tests, validators, rendered screenshots, API responses, file paths, and exact failure messages.
- Do not write a ledger file for every small task. Use one when it prevents restarting, prevents stale claims, or helps the user judge progress.
- If the user says "계속", resume from this ledger and update only what changed.
