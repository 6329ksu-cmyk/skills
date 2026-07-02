# Briefing Format

Use this shape for final answers after one cycle.

## Default

Keep it short:

```text
STATUS: PASS | CONCERNS | FAIL

What I changed:
- ...

Why it matters:
- ...

Validation:
- ...

Still worth improving:
- ...
```

## If the task was tiny

Use one or two short paragraphs plus a validation line.

## If the user is frustrated

Lead with the concrete correction, not process. Acknowledge only what affects the work. Avoid long apologies, defensiveness, and abstract reassurance.

## If validation failed

Use **FAIL** or **CONCERNS** and name the exact failing check. Include what was fixed, what remains, and the next command or cycle that should address it.

## Evidence

Prefer one concrete evidence line over a long log:

- validator or test result
- exact file changed
- reproduced failure and fixed behavior
- screenshot or runtime smoke result
- unresolved risk with the next verification step

Do not paste long command output unless the user asked for it.

## If the artifact is a skill

Include:

- skill name
- location
- core philosophy
- files created or changed
- validator result
- recursive self-application improvements
- remaining evolution backlog

Do not list every inspected file unless it changes the user's decision.
