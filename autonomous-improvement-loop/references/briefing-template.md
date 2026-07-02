# Briefing Template

Use concise briefing after a cycle. Do not dump all technical context.

## Standard Cycle Brief

```text
Verdict: PASS | CONCERNS | FAIL

Goal I optimized for:
...

What changed:
- ...

What got better:
- ...

Tradeoffs / what got less convenient:
- ...

Validation:
- ...

Remaining risk:
- ...

Recommended next cycle:
...
```

## When the User Wants "What Happened?"

```text
Before:
- ...

After:
- ...

Why it matters:
- ...

Cost/tradeoff:
- ...

Status:
- tests / commit / push / server / artifact path
```

## If Asking the User

Use at most three short questions. Prefer one.

```text
Need one decision:
...

Recommended: ...
Why: ...
```

## Anti-Dump Rule

Do not list the whole tech stack, file tree, dependency list, or every command unless the user asked for it. Summarize the decision-relevant part and keep detailed evidence in files, commits, tests, or logs.
