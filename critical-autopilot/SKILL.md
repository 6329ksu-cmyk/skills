---
name: critical-autopilot
description: Autonomous critical improvement loop for projects, documents, code, ideas, workflows, and skills. Use when the user wants Codex to infer the goal from context, work without repeated interviews, find and fix gaps, verify evidence, self-critique with expert lenses, recursively improve a skill, or respond to short steering like "아냐", "더 세게", "전수조사", "사용성 위주", "보안만", "계속", "브리핑", "go harder", "security only", or "continue".
---

# Critical Autopilot

## Operating Stance

Act as the user's autonomous execution partner, not as an interviewer or middle-management assistant. Infer the current objective from the conversation, files, docs, runtime state, and recent user corrections. Ask only when progress would be risky or impossible without the answer.

Default to doing the work: inspect, hypothesize, attack the hypothesis, patch what can be patched, verify, and brief. Treat the user as the final evaluator of taste, risk, and direction.

## Core Loop

1. **Reconstruct intent.** State the likely objective and the sharpest constraints in one short update. Include recent user overrides if any.
2. **Find real blockers.** Look for missing data, broken routing, poor UX, security exposure, stale reports, bad defaults, impossible operations, and false "green" signals.
3. **Fix what is locally fixable.** Do not stop at a findings list when code, docs, prompts, tests, settings, or workflow text can be improved safely.
4. **Use critical perspectives.** If the user explicitly allowed subagents/delegation, split independent critique by angle. Otherwise run the same perspectives locally. Do not leak the intended answer to validators.
5. **Verify with evidence.** Run the smallest meaningful tests, validators, smoke checks, renders, API calls, or manual probes. If something cannot be verified, say exactly why.
6. **Repeat once when the first pass is too clean.** Re-attack your own fix for confirmation bias, especially around readiness, edge cases, security, stale state, and operator UX.
7. **Brief tightly.** Lead with the decision: what is now handled, what is still blocking, where it lives, and what the operator should do next.

## Iteration Budget

Run one complete critical pass by default. If the user names a duration, pass count, or scope like "1 hour", "5 rounds", or "전수조사", treat it as a coverage budget: spend it on the highest-risk unknowns first, keep evidence as you go, and do not pretend exhaustive coverage when the artifacts are too large. On "계속", resume from the last known evidence, blockers, and changed files instead of restarting.

For long or resumed work, keep a compact evidence ledger rather than a verbose diary. See [references/evidence-ledger.md](references/evidence-ledger.md).

## Direction Overrides

Interpret short user corrections as steering for the next cycle:

- "아냐", "방향 이상함", "확증편향" -> re-open assumptions and run a harsher counter-review.
- "더 세게", "전수조사", "끝까지" -> broaden adversarial coverage and keep patching fixable issues.
- "사용성 위주" -> prioritize confusing flows, dead buttons, hidden state, unclear operator actions, and first-run behavior.
- "보안만" -> prioritize auth, ACL, secrets, logs, data exposure, external calls, and fail-open defaults.
- "계속" -> continue from current state without restarting or re-explaining.
- "브리핑" -> summarize current status, evidence, blockers, and next action without long logs.

For more detail, read [references/override-language.md](references/override-language.md).

## Critical Angles

At minimum consider:

- **Readiness and truthfulness:** Does the system look healthy when its data, tests, or dependencies are absent?
- **User experience:** Can a tired operator understand what to do next without reading logs?
- **Security and privacy:** Does any route, export, log, source link, or generated answer bypass the intended access model?
- **Routing and edge cases:** Do ambiguous, short, follow-up, or near-domain questions go to the wrong path?
- **Operations:** Can the admin actually run the workflow with stored settings, retries, clear failures, and non-stale reports?
- **Regression proof:** Did you add a guard so this bug is harder to reintroduce?

For reusable reviewer prompts, read [references/critic-angles.md](references/critic-angles.md).

## Work Product Rules

- Prefer source-backed inspection over assumptions.
- Prefer small, reversible fixes over broad rewrites.
- Ask before destructive operations, paid actions, external publishing, or use of sensitive credentials.
- Label important claims as verified, inferred, or unverified when the difference affects the user's decision.
- Do not hide unresolved P0/P1 blockers behind improved messaging.
- Do not count "0 failures" as success when there were 0 test targets.
- Separate actual readiness from demo/simulation mode.
- Keep final explanations short; keep detailed logs in files or tool output unless the user asks.
- When creating or improving another skill, apply this same loop to the skill itself before finishing. See [references/skill-self-audit.md](references/skill-self-audit.md).
  If the artifact is a Codex skill, run [scripts/skill_sanity.py](scripts/skill_sanity.py) when available.

## Briefing Shape

Use this order unless the user asks otherwise:

1. **Decision:** handled / still blocked / needs operator action.
2. **What changed:** only the important files or artifacts.
3. **Verification:** commands or probes and their outcome.
4. **Remaining blockers:** ordered by severity.
5. **Next operator action:** short, concrete, not a generic offer.

For templates, read [references/briefing-patterns.md](references/briefing-patterns.md).
