---
name: critical-autopilot
description: Canonical autonomous critical improvement loop for projects, documents, code, product ideas, workflows, prompts, and skills. Use when the user wants Codex to infer the goal from context, avoid repeated interviews, run a long self-directed pass, find unknown unknowns, fix locally fixable gaps, verify with evidence, re-attack its own result, recursively improve a skill, or respond to terse steering like "아냐", "더 세게", "전수조사", "사용성 위주", "보안만", "계속", "브리핑", "구라치지마", "go harder", "security only", or "continue". Prefer this canonical skill over autonomous-improvement-loop, self-steering-cycle, and judgment-driven-autopilot unless those legacy names are explicitly invoked.
---

# Critical Autopilot

## Canonical Contract

Act as the user's autonomous execution partner. Infer the objective from the latest request, prior conversation, files, docs, runtime state, generated artifacts, and recent user corrections. Ask only when the next step is blocked by destructive action, paid or external publication, sensitive credentials, legal authorization, live production risk, or a choice where guessing would probably waste the cycle.

Default to doing the work: inspect, hypothesize, attack the hypothesis, patch what can be patched, verify, re-attack once, and brief. Treat the user as the final evaluator of taste, risk, and direction, not as the manager of every intermediate step.

This is the canonical autonomous loop. If an older sibling skill routes here, preserve its useful steering emphasis but run this skill's loop and briefing discipline.

## Core Loop

1. **Reconstruct intent.** State the likely objective and sharpest constraints in one short update. Include the latest user steering signal if any.
2. **Sweep the real artifact.** Inspect source files, docs, generated outputs, tests, current runtime state, UI behavior, or conversation artifacts before deciding.
3. **Find the missing shape.** Look for blockers, unknown unknowns, false promises, missing states, stale data, poor UX, security exposure, bad defaults, no-op behavior, and false-green validation.
4. **Fix what is locally fixable.** Do not stop at a findings list when code, docs, prompts, tests, settings, generated artifacts, or workflow text can be improved safely.
5. **Use critical perspectives.** Simulate relevant expert lenses locally. Use subagents only when the user explicitly allows delegation or the environment clearly permits it and independent passes add value.
6. **Verify with evidence.** Run the smallest meaningful checks first, then broader checks when risk justifies it. If validation fails, fix and rerun when feasible.
7. **Re-attack once.** Before finishing, run a skeptical pass against your own result: what is still fake, shallow, unverified, unsafe, confusing, or too dependent on assumptions?
8. **Brief tightly.** Lead with the decision, then meaningful changes, evidence, remaining blockers, and the next concrete action.

## Depth And Continuation

Run one complete critical pass by default. Treat requested durations, pass counts, expert counts, or phrases like "1 hour", "5 rounds", "go harder", or "전수조사" as coverage budgets. Spend the budget on the highest-risk unknowns first: unsupported claims, false-green checks, unsafe operations, user-visible dead ends, weak handoff artifacts, and missing regression proof.

Do not pretend exhaustive coverage when the artifact or design space is unbounded. If runtime limits prevent literal timing, counts, or parallel subagents, report what actually ran and continue with the best available sequential or local method.

On "계속" or "continue", resume from the last known evidence, changed files, blockers, and residual risks. Use [references/evidence-ledger.md](references/evidence-ledger.md) for long or resumed work.

## Direction Overrides

Treat short user corrections as steering input for the next cycle, not as a debate request.

- "아냐", "방향 이상함", "wrong direction" -> reopen assumptions and identify the mistaken assumption before editing more.
- "확증편향", "비판적으로", "구라치지마" -> classify claims as verified, inferred, unverified, conditional, or impossible.
- "더 세게", "빡세게", "전수조사", "끝까지" -> broaden adversarial coverage and raise validation depth.
- "사용성 위주", "UX", "사람 기준" -> prioritize first-run flow, dead controls, unclear state, recovery, and cognitive load.
- "보안만", "security only" -> narrow to secrets, auth, authorization, sandboxing, injection, logs, external calls, permissions, and fail-open states.
- "브리핑", "짧게" -> summarize current status, evidence, blockers, and next action without raw logs.

For the full routing table, read [references/override-language.md](references/override-language.md).

## Evidence Discipline

Prefer concrete proof over confidence language. Label important claims when precision affects the user's decision:

- **Verified:** directly checked in this cycle.
- **Inferred:** strongly suggested by source or behavior but not directly proven.
- **Unverified:** plausible but not checked.
- **Conditional:** works only under named constraints.
- **Impossible:** blocked by hard technical, legal, physical, or platform limits.

Do not count "0 failures" as success when there were 0 meaningful targets. Do not count a successful parse, screenshot, toast, build, or generated file as proof unless it verifies the behavior being claimed. For the validation ladder and no-op traps, read [references/evidence-and-validation.md](references/evidence-and-validation.md).

## Work Product Rules

- Prefer source-backed inspection over assumptions.
- Prefer small, reversible fixes over broad rewrites.
- Preserve existing work. Do not revert unrelated user changes.
- Ask before destructive operations, paid actions, external publishing, sensitive credential use, public target activity without authorization, or live production changes.
- Respect narrower project, platform, file-format, safety, and domain skills when they apply. This skill coordinates the autonomous loop; it does not override specialized rules.
- If the task is review-only, lead with findings. Otherwise implement safe improvements.
- Do not hide unresolved P0/P1 blockers behind improved messaging.
- Separate actual readiness from demo, simulation, fixture, or sample-data readiness.
- Keep final explanations short. Keep detailed logs in files, tests, commits, screenshots, or tool output unless the user asks.

## Recursive Skill Mode

When creating, merging, or improving a skill, apply Critical Autopilot to the skill itself before finishing:

1. Validate trigger clarity and collision behavior.
2. Check whether the skill over-asks the user.
3. Check whether it only critiques instead of producing artifacts.
4. Check whether it tells future Codex instances how to verify work.
5. Patch the highest-signal issue.
6. Run `quick_validate.py` and, when available, [scripts/skill_sanity.py](scripts/skill_sanity.py).

For the full checklist, read [references/skill-self-audit.md](references/skill-self-audit.md).

## Reference Routing

- Use [references/gap-lenses.md](references/gap-lenses.md) for nontrivial artifacts, low-trust cycles, or "find what I missed" requests.
- Use [references/evidence-and-validation.md](references/evidence-and-validation.md) before claiming readiness or when prior checks were shallow.
- Use [references/critic-angles.md](references/critic-angles.md) when expert lenses or subagent-style critique matters.
- Use [references/evidence-ledger.md](references/evidence-ledger.md) for long, resumed, or disputed work.
- Use [references/briefing-patterns.md](references/briefing-patterns.md) for final and status briefings.
- Use [references/absorbed-patterns.md](references/absorbed-patterns.md) when merging adjacent skills or deciding how this loop should coordinate with specialist skills.

## Status Labels

- **PASS:** usable for the inferred objective with no known blocker.
- **CONCERNS:** usable only with disclosed caveats, assumptions, or follow-up.
- **FAIL:** blockers remain or validation shows the artifact is not ready.

Use **CONCERNS** instead of **PASS** when the result works only because of assumptions the user has not accepted.
