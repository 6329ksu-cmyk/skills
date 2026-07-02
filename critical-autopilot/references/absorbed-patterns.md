# Absorbed Patterns

Use this file when merging adjacent skills, shaping a long autonomous pass, or deciding how Critical Autopilot should coordinate with specialist skills.

## Canonicalization

- Keep one active autonomous loop: `critical-autopilot`.
- Keep older names only as compatibility aliases when they preserve existing prompts.
- Alias skills should point back to the canonical loop and disable implicit invocation when possible.
- Do not let multiple near-identical skills compete for the same trigger space.

## Routing And Fallback

- Start with a quick capability check when tools, network, auth, runtime, or browser state matter.
- Use the right specialized skill or tool for domain work instead of forcing this loop to do everything.
- If a preferred path fails, use an explicit fallback chain and say what changed.

## Dark-Zone And Completeness Thinking

- Track what is known, assumed, missing, and conflicting.
- Audit completeness against the likely archetype, not just files that already exist.
- Use L1/L2/L3 checks:
  - L1: exists
  - L2: reachable or usable
  - L3: meaningful enough for the outcome
- Triage findings as fix-now, roadmap, intentional, or human decision.

## Goal Shape

Every cycle needs a working definition of done:

- outcome
- verification
- constraints
- iteration policy
- error handling

When producing follow-up work, make it self-contained: goal, files or scope, acceptance checks, constraints, and dependency notes.

## Fan-Out Worth-It Gate

Use parallel review or subagents only when breadth matters: many independent units, high-stakes decisions, or distinct expert lenses. Do not burn many agents for a simple one-file fix.

After broad review, bucket actions as:

- fix now
- queue
- defer or intentional
- human decision

## Fact Before Question

- Do not ask the user for facts the repo, docs, code, tests, artifacts, or runtime can reveal.
- Ask the user for judgment, priorities, authorization, or taste only when needed.
- If one question is necessary, make it the highest-leverage unresolved question.

## Compounding Loop

Prefer concrete next work in this order:

1. failed validation
2. blockers found in the current cycle
3. missing or thin regression coverage
4. validation tightening
5. stale docs, pending-work notes, drift, or dead code
6. feature suggestions derived from the inferred purpose

Measure before and after when feasible. Return the synthesis, not every intermediate observation.
