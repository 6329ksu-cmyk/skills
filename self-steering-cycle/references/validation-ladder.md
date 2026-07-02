# Validation Ladder

Use the lowest level that gives honest confidence, then climb when the artifact is risky, user-visible, security-sensitive, or previously failed.

## Levels

1. **Shape**
   - Parse frontmatter, schema, JSON, Markdown links, filenames, or required sections.

2. **Static**
   - Run lint, typecheck, grep for forbidden patterns, secret scans, or structural consistency checks.

3. **Targeted Behavior**
   - Run the smallest test or reproduction that proves the changed behavior.

4. **Integration**
   - Run connected tests, migrations, build, import/export, API smoke checks, or document rendering.

5. **User-Visible**
   - Open the app, inspect screenshots, verify layout, try the workflow, check copy, empty states, errors, and responsive behavior.

6. **Adversarial**
   - Try malformed input, stale state, duplicated objects, missing credentials, permissions mismatch, rollback, restart, and handoff.

7. **Release/Handoff**
   - Confirm another agent or teammate can clone, pull, seed, run, verify, and understand what is intentionally local.

## Artifact Shortcuts

- **Skill**: run skill validator, inspect trigger description, read references, check no placeholder text, check concise progressive disclosure.
- **Code**: run targeted tests first, then build or broader suite if blast radius warrants it.
- **Frontend/UI**: use runtime smoke checks and screenshots when layout or interaction changed.
- **Docs/prompt**: test for ambiguity, missing acceptance criteria, unsafe instructions, and whether the next agent can act without the original conversation.
- **Security**: search for secrets, auth bypass, unsafe logging, dependency risk, and public/private boundary mistakes.

## Reporting

Report the checks actually run. Do not say "verified" when only inspected. If a check is skipped, name the remaining risk.
