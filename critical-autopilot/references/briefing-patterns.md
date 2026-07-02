# Briefing Patterns

The user wants decision-grade compression, not a diary. Include only what changes the operator's next move.

## Final Brief

- **Decision:** handled, still blocked, or needs operator action.
- **Where:** the important files, URLs, reports, or commands.
- **What changed:** one to five high-signal changes.
- **Verification:** the meaningful checks and their result.
- **Remaining:** the few blockers or development directions that still matter.

Use evidence labels when risk matters:

- **Verified:** directly tested, rendered, executed, or inspected from source.
- **Inferred:** likely from code or context, but not directly executed.
- **Unverified:** blocked by missing access, missing data, time, cost, external service, or unsafe action.

## Status Brief

Use when interrupted or asked "브리핑":

```
현재 판단: ...
확인한 증거: ...
막힌 것: ...
다음 행동: ...
```

## Avoid

- Full directory inventories.
- Long dependency or framework explanations unless they affect the decision.
- Raw logs when a summarized failure is enough.
- "All good" claims when no meaningful target was tested.
- Generic offers as the final line.
