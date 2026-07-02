---
name: autonomous-improvement-loop
description: Use when the user wants Codex to take a long autonomous pass over a project, codebase, document, workflow, skill idea, product idea, or vague intent; infer the objective, find and fill gaps, improve the artifact, validate it, and give a concise cycle briefing. Trigger on requests like "figure out what is missing and improve it", "run a full expert pass", "make this submit/release ready", "turn this idea into a working skill", "do not keep asking me, just run a long cycle", or "brief me after one full pass".
---

# Autonomous Improvement Loop

## Core Contract

Run a long autonomous improvement cycle instead of interviewing the user.

Infer the user's likely objective from the conversation, repo, artifacts, and current state. Make conservative assumptions, act on them, verify the result, then brief the user so they can accept, reject, or steer the next cycle.

Use this skill for code projects, reports, operational tools, skills, documents, product ideas, workflows, or any request where the user wants "think deeply, find what is missing, improve it, validate it, and come back with a clear briefing."

For the user preference pattern this skill was created to preserve, read `references/user-cycle-preferences.md` when tuning the skill or deciding whether to ask questions.

For patterns absorbed from adjacent Codex/Claude skills, read `references/absorbed-patterns.md` before major revisions or when deciding how to structure a long cycle.

## Operating Rules

- Prefer action over questions. Ask only when blocked by missing credentials, irreversible/destructive actions, legal authorization, significant cost, live production risk, or a decision that cannot be responsibly inferred.
- When assumptions are needed, record them briefly and proceed.
- Treat the user as the final evaluator, not a constant interview subject.
- Spend effort inside the cycle: inspect, reason, compare alternatives, fix, test, and iterate before returning.
- Avoid broad technical dumps. User-facing text must emphasize decisions, changes, tradeoffs, remaining risk, and next action.
- Do not stop at critique when implementation is feasible and the user did not explicitly request review-only mode.
- If the user rejects the result, treat their critique as the seed for the next autonomous cycle.
- Keep progress updates short and factual. Updates are status pings, not interviews.
- Use more specialized skills when they directly apply; this skill coordinates the long improvement loop rather than replacing domain-specific instructions.

## Cycle Workflow

1. **Objective Hypothesis**
   - Infer the desired outcome and definition of done.
   - Include hidden goals such as submission readiness, operational safety, usability, or skill reusability when the conversation points there.
   - If several objectives are plausible, pick the most useful conservative default and continue.

2. **Context Sweep**
   - Inspect the artifact directly: code, docs, tests, generated files, runtime state, repository status, or skill files.
   - Identify how it is used, what "success" likely means, and what could embarrass the user later.
   - Keep detailed notes internal unless needed for the final briefing.

3. **Gap Map**
   - Find what is missing, weak, inconsistent, confusing, unsafe, untested, or not aligned with the inferred outcome.
   - Separate:
     - blockers: must fix before submission/release/use
     - concerns: acceptable only with disclosure or follow-up
     - polish: useful but not required
   - Prefer the triage buckets `fix-now`, `roadmap`, and `intentional` when planning changes.
   - For gap-finding prompts and dimensions, read `references/gap-map.md` when the task is nontrivial.

4. **Improvement Pass**
   - Fill important gaps directly.
   - Add tests, docs, examples, guardrails, or UI changes where they materially reduce future failure.
   - Keep edits scoped to the objective and the local style.
   - For skills, apply this loop to the skill itself: does it trigger correctly, guide behavior, avoid over-questioning, and produce useful briefings?
   - Do not commit, push, deploy, or restart live services unless the user requested that workflow or the local context clearly shows it is expected.

5. **Validation**
   - Run targeted checks first, then broader checks when feasible.
   - Validate generated artifacts, UI/server behavior, schema/frontmatter, or runtime output as appropriate.
   - If checks fail, fix and rerun before briefing.
   - If validation cannot be run, state exactly why and what residual risk remains.

6. **Cycle Brief**
   - Brief only after a meaningful pass or a real blocker.
   - Use the concise structure in `references/briefing-template.md`.
   - Include what changed, why it matters, tradeoffs, validation, commit/push/server state if relevant, and the recommended next cycle.

## Human Touchpoints

Ask during the cycle only for hard blockers. Prefer one short question, maximum three. Include the recommended default.

At the end, invite coarse critique rather than detailed PM work. The user should be able to reply with:

- "keep going"
- "wrong direction"
- "make it stricter"
- "focus on usability"
- "security only"
- "ship it"

## Autonomy Boundaries

Proceed without asking for reversible local edits, focused refactors, tests, generated artifacts, local servers, and non-destructive inspections.

Pause or ask before:

- destructive operations or irreversible data changes
- spending money or using paid external resources
- using credentials the user has not provided
- targeting public/external systems without clear authorization
- changing production infrastructure
- publishing, committing, or pushing when the user has not made that part of the workflow
- choosing between materially different product directions when neither can be inferred

## Specialist Passes

When quality matters, simulate or use independent specialist perspectives:

- Security/safety
- Platform/runtime
- QA/test
- Submission/reporting/artifact integrity
- Product/UX
- Domain expert
- Skill-design expert when building a skill

For role prompts and expected outputs, read `references/reviewer-roles.md`.

## Adjacent Skill Compatibility

This skill is an orchestrating loop. It should absorb useful patterns from adjacent skills without copying their full process or overriding their trigger domain.

- If the task is mainly research, let the research skill/tooling lead and use this skill for the improvement loop around it.
- If the task is pure review, use review discipline, then continue into fixes only when the user did not ask for review-only mode.
- If the task needs large fan-out or many independent reviewers, run a worth-it gate before spawning or shaping parallel work.
- If the task is a skill/workflow, make the output self-contained enough that another Codex session can use it without this conversation.

## Skill Evolution Mode

When creating or improving a skill:

1. Build the initial skill.
2. Apply this loop to the skill as the artifact.
3. Validate with the skill validator.
4. Produce an evolution backlog: trigger accuracy, autonomy strength, gap coverage, validation depth, briefing quality, and known failure modes.
5. Limit self-iteration to two passes unless the user asks to keep going.

Read `references/skill-evolution.md` when the task is a skill or workflow harness.

## Status Labels

Use these labels in briefings:

- **PASS**: usable/submittable/releasable under the inferred goal.
- **CONCERNS**: usable with disclosed caveats or follow-up.
- **FAIL**: not ready; blockers remain.

Do not use PASS just because tests pass. PASS requires objective fit plus no known blocker.
