# Gap Map

Use this reference when the task requires more than a simple fix.

## Objective Fit

Ask internally:

- What outcome is the user probably buying with this request?
- What would make the result useful tomorrow, not just correct now?
- What would the user reject after one cycle as "not it"?
- What is the smallest result that proves progress?

## Gap Categories

Check these categories and classify each gap as blocker, concern, or polish.

- **Purpose gap**: unclear target user, missing definition of done, wrong success metric.
- **Artifact gap**: stale/generated/past sample data mixed into current output, wrong files included, missing provenance.
- **Correctness gap**: wrong logic, incomplete parsing, platform assumptions, edge cases.
- **Security gap**: auth bypass, secret handling, unsafe defaults, MITM, injection, overbroad external access.
- **Safety/legal gap**: destructive action, public target scanning, OT/production risk, unclear authorization.
- **Usability gap**: confusing UI, ambiguous status, hard-to-follow flow, unclear next action.
- **Validation gap**: no test for the behavior, tests hit real external systems, no smoke check, no artifact inspection.
- **Communication gap**: too much irrelevant technical detail, no tradeoff summary, no remaining-risk statement.
- **Evolution gap**: no way for the next cycle to improve from user rejection or new evidence.

## Filling Gaps

Prefer fixing the highest-risk gap directly. Use this order:

1. Blockers that can make the output wrong, unsafe, or misleading.
2. Confusing behavior that can cause user misuse.
3. Missing tests around changed or risky behavior.
4. Documentation or briefing improvements that reduce future ambiguity.
5. Polish only after the above.

## Assumption Ledger

Record assumptions internally while working. Brief only the assumptions that affect user judgment.

Useful format:

```text
Assumption: The goal is submission readiness, not fastest demo.
Impact: I used stricter safety gates and accepted some added friction.
```
