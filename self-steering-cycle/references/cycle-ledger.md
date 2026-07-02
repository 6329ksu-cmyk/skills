# Cycle Ledger

Use this file when the user says "continue", when the task spans multiple cycles, or when trust has been damaged and the next pass must show concrete progress.

## Internal Ledger

Keep a compact internal ledger while working. Do not dump it to the user unless it changes their decision.

```text
Objective hypothesis:
Latest steering signal:
Assumptions being used:
Blockers found:
Fixes attempted:
Validation run:
Residual risks:
Next best cycle:
```

## Continuation Rules

- On "continue", resume from unresolved blockers and residual risks first.
- On "wrong direction", rewrite the objective hypothesis before editing.
- On "harder" or "not enough", raise the verification level and add a skeptical refuter pass.
- On "usability first", convert abstract issues into user workflow failures.
- On "security only", drop unrelated polish and inspect exposure, authority, secrets, and abuse paths.

## When To Persist Notes

Persist a short note in the artifact only when it improves handoff: project state files, implementation plans, pending-work docs, test matrices, or skill references.

Do not create extra process files just to prove the cycle happened.
