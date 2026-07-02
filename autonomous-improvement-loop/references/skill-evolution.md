# Skill Evolution

Use this reference when the artifact being improved is a skill, workflow, prompt harness, or reusable operating procedure.

## Self-Application Pass

Treat the skill as the project.

Check:

- **Trigger accuracy**: Will Codex know when to use it from the description alone?
- **Autonomy strength**: Does it tell Codex not to over-interview the user?
- **Gap coverage**: Does it cover missing requirements, improvements, validation, and briefing?
- **Cycle control**: Does it avoid infinite self-review?
- **Reference hygiene**: Are details split into references without hiding critical instructions?
- **Briefing quality**: Does it force concise human-readable output?
- **Failure handling**: Does it say when to ask, stop, or report blocked?

## Evolution Backlog Template

```text
Skill status: PASS | CONCERNS | FAIL

Current strengths:
- ...

Weak spots:
- ...

Next upgrades:
1. ...
2. ...
3. ...

Forward-test prompts:
- ...
```

## Forward-Test Prompts

Use realistic prompts. Do not leak expected fixes.

Examples:

```text
Use $autonomous-improvement-loop on this repo and make it release-ready. Do not ask unless blocked; brief after one full cycle.
```

```text
Use $autonomous-improvement-loop to turn this rough skill idea into a reusable Codex skill. Create the files, validate them, and brief me.
```

```text
Use $autonomous-improvement-loop to improve this report generator so the generated artifacts are submission-safe.
```

## Iteration Limit

Run at most two self-application passes unless the user asks for more. Record remaining improvement ideas in the backlog instead of looping forever.
