---
name: self-steering-cycle
description: Run a self-steering autonomous cycle that turns terse or corrective user feedback into objective re-inference, unknown-unknown discovery, concrete improvements, verification, and a short judgment briefing. Use for projects, code, documents, ideas, prompts, workflows, or skills when the user says things like "continue", "find what I missed", "do not just do what I said", "make it stricter", "direction is wrong", "usability first", "security only", "keep going", or asks to apply the loop recursively to the artifact itself. Prefer this over generic improvement workflows when the key requirement is adapting to short steering signals without repeated interviews.
---

# Self-Steering Cycle

## Core Contract

Run one serious autonomous cycle, then brief. The user is the final taste and judgment layer, not the project manager for every intermediate decision.

Infer the current objective from the latest user message, prior conversation, visible files, running state, and artifact behavior. Then find gaps, repair what is reasonable, verify the repair, and summarize only what helps the user decide the next direction.

Use this skill for code, docs, designs, prompts, skills, operational runbooks, product ideas, QA plans, and any artifact where the user expects self-directed improvement rather than an interview.

This skill is most valuable when the user is steering by feel: terse corrections, frustration, "continue", or "find what I did not say." If another autonomous-improvement skill also matches, prefer this skill when short user feedback must shape the next cycle.

## Operating Rules

- Prefer action over questions. Ask only for destructive changes, external publication, paid resources, unprovided credentials, live production risk, legal authorization, or a choice where guessing would likely waste the cycle.
- Treat short user corrections as steering input for the next cycle, not as a request for debate.
- Do not stop at critique when a fix, draft, test, or documentation change is feasible.
- Do not pad the user-facing answer with file inventories, stack summaries, long logs, or internal deliberation.
- Preserve existing work. Avoid unrelated refactors and never revert user changes unless explicitly asked.
- Use specialized skills when they clearly apply, but keep this skill responsible for the overall autonomous loop and final briefing.
- If the user says "continue" or equivalent, resume from the last known artifact and unresolved gaps. Do not restart from first principles unless the context is stale or contradictory.
- Treat "I only fixed what the user explicitly named" as a failed cycle. Every serious cycle should attempt at least one unknown-unknown pass and either fix or report what it found.

## Cycle

1. **Infer the target**
   - State the working objective internally in one sentence.
   - Include implied goals such as usability, correctness, demo readiness, handoff clarity, safety, or future agent reliability when the conversation points there.
   - If the latest user message narrows the axis, obey that axis for this cycle.
   - For repeated "continue" cycles, use `references/cycle-ledger.md` to keep a compact working memory.

2. **Sweep the artifact**
   - Inspect the actual artifact, not just the request.
   - Look for current state, user-visible behavior, persistence, tests, docs, hidden assumptions, and handoff risks.
   - For terse or corrective steering phrases, read `references/steering-signals.md`.

3. **Find what the user did not name**
   - Identify blockers, contradictions, missing states, edge cases, unusable flows, unclear ownership, and brittle assumptions.
   - For nontrivial work or low-trust situations, read `references/gap-lenses.md` and run multiple lenses before deciding.
   - Keep one finding that was not merely a restatement of the user's examples, unless the artifact is too small for that to be meaningful.

4. **Fill what can be filled**
   - Implement, rewrite, document, seed, test, or scaffold the highest-value improvements within the current scope.
   - Prefer small concrete changes that improve the artifact over broad speculative rewrites.
   - If no edit is appropriate, produce a sharper artifact such as a test matrix, decision record, prompt, checklist, or failure report.

5. **Verify**
   - Run targeted tests, validators, builds, screenshots, parsers, linters, or smoke checks as appropriate.
   - If validation fails, fix and rerun when feasible.
   - If validation cannot run, state the exact residual risk in the final briefing.
   - For choosing how deep to verify, read `references/validation-ladder.md`.

6. **Brief**
   - Return a concise decision briefing, not a transcript.
   - Include status, what changed, why it matters, validation, remaining concerns, and the best next cycle.
   - When trust is low, include the strongest concrete evidence that the cycle found or fixed something beyond the user's explicit wording.
   - For the briefing shape, read `references/briefing.md`.

## Specialist Lenses

When quality matters, simulate or dispatch independent passes. Do not outsource the final judgment. Use subagents only when the current platform rules and user permissions allow it; otherwise run the perspectives locally.

Use enough lenses to catch unknown unknowns:

- Product and user workflow
- QA, edge cases, and regression
- Security and secrets
- Data model and persistence
- Runtime, performance, and operations
- UX, visual layout, accessibility, and copy
- Domain-specific expert
- Skeptical refuter whose job is to prove the current answer is still weak

## Recursive Mode

When the artifact is a skill, prompt, workflow, checklist, or agent instruction:

1. Build the first usable version.
2. Apply this same cycle to the artifact.
3. Check trigger accuracy, autonomy strength, gap coverage, validation depth, and briefing quality.
4. Patch the artifact once more.
5. Report the improvements and remaining evolution backlog.

For details, read `references/recursive-artifacts.md`.

## Final Status Labels

- **PASS**: usable for the inferred objective with no known blocker.
- **CONCERNS**: usable, but important caveats remain.
- **FAIL**: blockers remain or validation shows the artifact is not ready.

Use **CONCERNS** instead of **PASS** when the artifact works only because of assumptions the user has not accepted.
