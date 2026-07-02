# Recursive Artifacts

Use this file when improving a skill, prompt, workflow, agent instruction, checklist, or operating procedure.

## First-Pass Checks

- **Trigger accuracy**: Would the skill activate on the user's real words, including terse steering phrases?
- **Autonomy**: Does it let Codex proceed without turning the user into a manager?
- **Gap discovery**: Does it explicitly require finding issues beyond the user's examples?
- **Action bias**: Does it push Codex to fill gaps, not only report them?
- **Validation**: Does it tell Codex how to prove the result worked?
- **Briefing quality**: Does it keep final output useful and short?
- **Boundaries**: Does it pause before destructive, costly, public, credentialed, or production-risk actions?
- **Collision awareness**: If a similar skill exists, is this skill's distinct reason to trigger clear enough?
- **Continuation**: If the user says "continue", does the next agent know what to resume and what to drop?

## Self-Application Loop

1. Read the artifact as if a future agent will use it without this conversation.
2. Identify where that future agent could over-ask, under-test, over-explain, or follow the user's examples too literally.
3. Patch the artifact to reduce those failure modes.
4. Run available validators.
5. Produce a short evolution backlog for the next session.

## Common Fixes

- Move detailed examples into references so the main instruction stays lean.
- Add steering phrase interpretation for short corrective feedback.
- Add a refuter pass when trust or quality is low.
- Add explicit final status labels so the user can judge quickly.
- Add validation expectations for the artifact type.
- Add a "failed cycle" condition for agents that only execute the user's literal examples.
