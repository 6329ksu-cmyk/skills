# Recursive Skill Audit

Apply this checklist before finishing a skill creation or skill update task.

## Trigger

- Does the frontmatter description explain both what the skill does and when to use it?
- Does it include likely terse user triggers?
- Is it broad enough for reuse but not so broad that it steals unrelated tasks?

## Behavior

- Does the skill tell Codex to infer intent and act instead of interviewing?
- Does it still protect destructive, paid, external, credentialed, or legal-risk actions?
- Does it say how to handle short steering like "continue", "wrong direction", or "security only"?
- Does it tell Codex to fill fixable gaps, not merely list them?
- Does it explain how to treat requested durations, pass counts, or expert counts without pretending fake exhaustive coverage?

## Verification

- Does the skill require meaningful evidence?
- Does it warn against no-op and false-green validation?
- Does it define what to do if validation cannot run?

## Briefing

- Is the final answer short and judgment-oriented?
- Does it avoid dumping long logs, stacks, and file inventories?
- Does it separate handled, blocked, conditional, and next-cycle items?

## Progressive Disclosure

- Is `SKILL.md` concise?
- Are detailed maps in one-level `references/` files?
- Are there no README/changelog/extra docs that add clutter?

Patch the skill after this audit and rerun the validator.
