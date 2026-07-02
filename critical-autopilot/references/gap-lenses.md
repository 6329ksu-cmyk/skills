# Gap Lenses

Use this file for nontrivial artifacts, low-trust cycles, broad "find what I missed" requests, or any cycle that could otherwise only fix what the user explicitly named.

## Core Lenses

Run the relevant lenses quickly, then act on the highest-value findings.

1. **Goal Fit**
   - Is the artifact solving the real implied problem, or only a convenient substitute?
   - What would make the user say "this still misses the point"?
   - Are success criteria observable?

2. **User Workflow**
   - Can a real user start, continue, recover, and finish without hidden knowledge?
   - Are empty states, errors, permissions, loading states, and handoffs handled?
   - Does the flow reduce work or just move work elsewhere?

3. **State And Ownership**
   - Where is truth stored?
   - Are duplicated, mirrored, derived, cached, or generated objects synchronized safely?
   - What happens when state is stale, partial, duplicated, reordered, or migrated?

4. **Correctness And Edge Cases**
   - What invariant should never break?
   - Try missing data, malformed input, duplicated data, stale data, partial saves, permissions mismatch, restart, rollback, and handoff.
   - For visual artifacts, check overflow, text wrapping, scaling, occlusion, layer order, and viewport changes.

5. **Security And Privacy**
   - Are secrets, credentials, tokens, personal data, internal URLs, source links, logs, or exports exposed?
   - Are auth and authorization boundaries clear?
   - Could demos, fixtures, generated reports, or docs leak something that should not be committed?

6. **Operations And Handoff**
   - Can the next agent or teammate reproduce, run, seed, verify, retry, recover, and inspect the work?
   - Are local-only assets, ignored data, environment variables, and manual steps documented?
   - Does the final state survive pull, clone, restart, deploy, import, export, and reuse?

7. **Regression Proof**
   - Is there a test, validator, prompt guard, fixture, or checklist that makes the fixed issue harder to reintroduce?
   - Are broad checks masking a missing specific check?

8. **Skeptical Refuter**
   - Assume the current plan is attractive but wrong.
   - Find the smallest realistic scenario that breaks it.
   - Convert that scenario into a fix, test, or explicit caveat.

## Coverage Challenge

Before leaving the gap phase, answer internally:

- What did the user not mention that would still make the result feel broken?
- What hidden dependency would fail after pull, restart, deploy, import, handoff, or reuse?
- What visible behavior would embarrass the artifact even if the core logic is correct?
- What assumption did this cycle make because it was convenient?

If the answer exposes a cheap fix, make it. If it exposes a real but larger issue, report it as a concern with the next concrete verification step.

## Ranking

Classify findings:

- **Blocker:** prevents real use, correctness, safety, or handoff.
- **Concern:** acceptable only if disclosed or scheduled.
- **Polish:** improves confidence or experience but does not block the current goal.

Fix blockers first. Fix concerns when cheap or high-leverage. Do not spend the cycle polishing while blockers remain.
