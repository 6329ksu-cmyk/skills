#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def fail(message):
    print(f"FAIL: {message}")
    return 1


def read_text(path):
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    fields = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields, text[end + 5 :]


def local_markdown_links(markdown):
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for raw in pattern.findall(markdown):
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        yield raw.split("#", 1)[0]


def main():
    if len(sys.argv) != 2:
        return fail("usage: skill_sanity.py <skill-folder>")

    root = Path(sys.argv[1]).expanduser().resolve()
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        return fail("missing SKILL.md")

    errors = []
    text = read_text(skill_md)
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return fail(str(exc))

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        errors.append("frontmatter name must be 1-63 chars of lowercase letters, digits, or hyphens")
    if len(description.split()) < 12:
        errors.append("frontmatter description is too short for reliable discovery")

    for link in local_markdown_links(body):
        if link and not (root / link).exists():
            errors.append(f"broken SKILL.md link: {link}")

    openai_yaml = root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        openai_text = read_text(openai_yaml)
        if f"${name}" not in openai_text:
            errors.append(f"agents/openai.yaml default prompt should mention ${name}")

    markers = ["TO" + "DO", "FIX" + "ME", "T" + "BD", "PLACE" + "HOLDER", "[TO" + "DO"]
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml"}:
            path_text = read_text(path)
            for marker in markers:
                if marker in path_text:
                    errors.append(f"{path.relative_to(root)} contains placeholder marker {marker}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: {root.name} sanity checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
