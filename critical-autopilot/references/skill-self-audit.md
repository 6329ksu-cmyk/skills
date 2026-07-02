# Skill Self-Audit

When creating or improving a Codex skill, apply Critical Autopilot to the skill before finishing.

## Audit Steps

1. **Trigger fit:** The YAML description names real situations where the skill should be used, and it is not project-specific.
2. **Operating stance:** The skill tells Codex how to act, not just what topic it covers.
3. **Progressive disclosure:** `SKILL.md` stays short enough to load every time, while references hold optional detail.
4. **No dead placeholders:** Remove placeholder markers, broken links, missing references, and generated boilerplate.
5. **Interface check:** `agents/openai.yaml`, if present, has a useful `display_name`, `short_description`, and `default_prompt` that names the skill correctly.
6. **Safety boundaries:** The skill asks before destructive operations, paid actions, external publishing, or sensitive credential use.
7. **Validation:** Run the available validator. If this skill's bundled `scripts/skill_sanity.py` is available, run it against the skill folder too.
8. **Recursive patch:** Fix the highest-signal issue found by this audit, then validate again.
9. **Evidence hygiene:** The final brief separates verified results from inferred or unverified claims.

## Common Failure Modes

- The skill becomes a rigid checklist instead of a reusable operating mode.
- The description is too vague for automatic discovery.
- The skill says "use experts" without defining when subagents are allowed.
- It rewards long reports instead of verified improvements.
- It treats simulation, demo data, or empty tests as production readiness.
- It hides Korean or short-command trigger language only in the body, where automatic discovery cannot see it.
