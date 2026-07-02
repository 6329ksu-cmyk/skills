# Evidence And Validation

## Validation Ladder

Use the lowest rung that can honestly support the claim; climb when risk is higher.

1. **Static read:** inspect files, schemas, docs, configs.
2. **Syntax/schema:** parser, frontmatter validator, JSON/YAML/schema validation.
3. **Unit/local behavior:** focused tests, reducers, small scripts.
4. **Integration smoke:** build, app launch, route/API flow, import/export round trip.
5. **User-visible proof:** screenshot, render, browser interaction, document/PDF render.
6. **Regression proof:** before/after diff, no-op detection, target-only change proof.
7. **Operational proof:** retries, permissions, persistence, restart/resume, failure states.

## No-Op Traps

Do not count these as success by themselves:

- a toast says "applied" but the target did not change
- a screenshot is nonblank but the intended region did not change
- a test reports 0 failures because it found 0 targets
- a generated file parses but does not contain the required data
- a recommendation exists without score, provenance, or compatibility data
- a preview works but commit/undo/export does not

## Claim Labels

Use these labels when precision matters:

- **Verified:** directly checked in this cycle.
- **Inferred:** strongly suggested by source or behavior but not directly proven.
- **Unverified:** plausible but not checked.
- **Conditional:** works only under named constraints.
- **Impossible:** blocked by hard technical, legal, physical, or platform limits.

## Failure Handling

If validation fails, decide:

- fix and rerun
- narrow the claim
- mark as blocked
- create a focused follow-up gate

Never hide a failed validator behind unrelated passing checks.
