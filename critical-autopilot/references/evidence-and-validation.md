# Evidence And Validation

Use the lowest validation level that can honestly support the claim; climb when the artifact is risky, user-visible, security-sensitive, previously failed, or being submitted, shipped, or handed off.

## Validation Ladder

1. **Static Read**
   - Inspect files, schemas, docs, configs, generated artifacts, and source-backed facts.

2. **Syntax Or Schema**
   - Run parsers, frontmatter validators, JSON/YAML/schema validation, link checks, or required-section checks.

3. **Unit Or Local Behavior**
   - Run focused tests, reducers, small scripts, or direct reproductions for the changed behavior.

4. **Integration Smoke**
   - Run builds, app launch, route/API flow, migration, import/export round trip, service startup, or document rendering.

5. **User-Visible Proof**
   - Use screenshots, rendered output, browser interaction, CLI workflow, report inspection, or visible UI state checks.

6. **Adversarial And Regression**
   - Try malformed input, stale state, duplicated objects, missing credentials, permissions mismatch, rollback, restart, and handoff.

7. **Operational Proof**
   - Confirm retries, persistence, restart/resume behavior, clear failure states, clone/pull/setup handoff, and intentionally local data boundaries.

## No-Op Traps

Do not count these as success by themselves:

- a toast says "applied" but the target did not change
- a screenshot is nonblank but the intended region did not render or update
- a test reports 0 failures because it found 0 targets
- a generated file parses but does not contain the required data
- a recommendation exists without score, provenance, or compatibility data
- a preview works but commit, undo, export, restart, or handoff does not
- a broad suite passes while the specific failure mode has no targeted check
- a report looks current but includes stale sample data or a different run's artifacts

## Claim Labels

Use these labels when precision matters:

- **Verified:** directly checked in this cycle.
- **Inferred:** strongly suggested by source or behavior but not directly proven.
- **Unverified:** plausible but not checked.
- **Conditional:** works only under named constraints.
- **Impossible:** blocked by hard technical, legal, physical, or platform limits.

## Failure Handling

If validation fails, choose one of these explicitly:

- fix and rerun
- narrow the claim
- mark the cycle blocked
- create a focused follow-up gate

Never hide a failed validator behind unrelated passing checks.
