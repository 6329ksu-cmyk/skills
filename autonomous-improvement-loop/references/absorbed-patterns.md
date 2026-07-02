# Absorbed Patterns

This skill should absorb patterns, not duplicate entire skills. Use these as design influences when improving a project, idea, document, or skill.

## Routing And Fallback

From agent-reach and workflow-style skills:

- Start with a quick capability/preflight check when tools, network, auth, or runtime matter.
- Use a route table mindset: choose the right specialized skill or tool for the task instead of forcing this loop to do everything.
- If a preferred path fails, use an explicit fallback chain and say what changed.

## Dark-Zone And Completeness Thinking

From idea-to-spec and audit-existing-project:

- Track what is bright/known, gray/assumed, dark/missing, and conflicting.
- Audit completeness against the likely archetype, not just the files that already exist.
- Use L1/L2/L3 checks:
  - L1: exists
  - L2: reachable/usable
  - L3: meaningful/complete enough for the outcome
- Triage findings as `fix-now`, `roadmap`, or `intentional`.

## Goal Shape

From goal and goal-decomposer:

- Every cycle needs a working definition of done:
  - outcome
  - verification
  - constraints
  - iteration policy
  - error handling
- When producing follow-up tasks, make them self-contained: include goal, files/scope, acceptance checks, constraints, and dependency notes.
- Do not hide unresolved design decisions inside implementation tasks. Either infer conservatively or mark them as remaining risk.

## Fan-Out Worth-It Gate

From workflow-shaper, council, and full-team review:

- Use parallel or multi-review only when breadth matters: many independent units, high-stakes decisions, or distinct expert lenses.
- Do not burn many agents for a simple one-file fix.
- Use action buckets after broad review:
  - ship/fix now
  - queue/roadmap
  - defer/intentional
  - human decision

## Fact Before Question

From deep-interview:

- Do not ask the user for facts the repo, docs, code, tests, or artifacts can reveal.
- Ask the user for judgment, priorities, authorization, or taste only when needed.
- If one question is necessary, make it the highest-leverage unresolved question.
- Use scenario-based edge cases internally when boundaries are fuzzy.

## Validation Discipline

From validate, review, pre-mortem, and rpi:

- Avoid self-grading. Prove claims with tests, artifact inspection, runtime smoke checks, or concrete diffs.
- Run a pre-mortem before declaring readiness: how could this still fail after the apparent fix?
- Check whether verification proves the claimed behavior or only proves the code builds.
- Preserve a next-work list when the cycle stops with concerns.

## Compounding Loop

From evolve, goals, and rpi:

- Prefer concrete next work in this order:
  1. failing tests or failed validation
  2. blockers found in the current cycle
  3. missing/thin regression coverage
  4. validation tightening
  5. stale docs, pending-work notes, drift, dead code
  6. feature suggestions derived from the inferred purpose
- Measure before and after when feasible.
- Keep context dense: return only the synthesis, not every intermediate observation.

## Skill-Specific Absorption

When this loop is used to create or improve a skill:

- Make trigger descriptions strong because frontmatter determines whether the skill is used.
- Keep SKILL.md short and move detailed dimensions into references.
- Include validation steps.
- Forward-test with realistic prompts when the skill is complex.
- Add an evolution backlog instead of endlessly self-reviewing.
