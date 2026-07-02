# Gap Lenses

Use this file for nontrivial artifacts, low-trust cycles, or requests to find what the user did not explicitly name.

## Core Lenses

Run the relevant lenses quickly, then act on the highest-value findings.

1. **Goal Fit**
   - Is the artifact solving the real implied problem?
   - What would make the user say "this still misses the point"?
   - Are success criteria observable?

2. **User Workflow**
   - Can a real user start, continue, recover, and finish without hidden knowledge?
   - Are empty states, errors, permissions, loading states, and handoffs handled?
   - Does the flow reduce work or just move work elsewhere?

3. **State and Ownership**
   - Where is truth stored?
   - Are duplicated, mirrored, derived, or cached objects synchronized safely?
   - What happens when an object appears in multiple contexts?

4. **Edge Cases**
   - Try missing data, duplicated data, stale data, partial saves, reordered steps, undo/redo, concurrent edits, and migration from older versions.
   - For visual artifacts, check overflow, text wrapping, scaling, occlusion, layer order, and viewport changes.

5. **Correctness and Tests**
   - What invariant should never break?
   - Is there a targeted test for the failure mode?
   - Are broad checks masking a missing specific check?

6. **Security and Privacy**
   - Are secrets, credentials, tokens, personal data, or internal URLs exposed?
   - Are authz boundaries clear?
   - Could logs, demos, fixtures, or docs leak something that should not be committed?

7. **Operations and Handoff**
   - Can the next agent or teammate reproduce, run, seed, verify, and recover the work?
   - Are local-only assets, ignored data, environment variables, and manual steps documented?
   - Does the final state survive pull, clone, restart, and deploy?

8. **Skeptical Refuter**
   - Assume the current plan is attractive but wrong.
   - Find the smallest realistic scenario that breaks it.
   - Convert that scenario into a fix, test, or explicit caveat.

## Coverage Challenge

Before leaving the gap phase, ask:

- What did the user not mention that would still make the result feel broken?
- What hidden dependency would fail after pull, restart, deploy, import, handoff, or reuse?
- What visible behavior would embarrass the artifact even if the core logic is correct?
- What assumption did this cycle make because it was convenient?

If the answer exposes a cheap fix, make it. If it exposes a real but larger issue, report it as a concern with the next concrete verification step.

## Ranking

Classify findings:

- **Blocker**: prevents real use, correctness, safety, or handoff.
- **Concern**: acceptable only if disclosed or scheduled.
- **Polish**: improves confidence or experience but does not block the current goal.

Fix blockers first. Fix concerns when cheap or high-leverage. Do not spend the cycle polishing while blockers remain.
