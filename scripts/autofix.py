#!/usr/bin/env python3
"""Auto-fixer for blog quality issues. Runs before the quality check in CI."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
POSTS_DIR = REPO_ROOT / "_posts"


def fix_em_dashes(body):
    """
    Replace em dashes based on context:
      - After a closing quote  →  colon  (e.g. "Title" — subtitle  →  "Title": subtitle)
      - Trailing at end of line  →  comma
      - Everything else  →  comma
    Skips HTML tag lines (e.g. — Monisha signature in a <p> tag).
    """
    lines = body.split("\n")
    fixed = []

    for line in lines:
        # Leave HTML lines alone — em dashes there are intentional (e.g. — Monisha)
        if re.match(r"\s*<", line):
            fixed.append(line)
            continue

        # After a closing quote, em dash introduces a subtitle → colon
        line = re.sub(r'(["’”])\s*—\s*', r'\1: ', line)

        # Trailing em dash at end of line → comma
        line = re.sub(r'\s*—\s*$', ',', line)

        # Everything else → comma with single space either side
        line = re.sub(r'\s*—\s*', ', ', line)

        fixed.append(line)

    return "\n".join(fixed)


def fix_trailing_whitespace(content):
    """Remove trailing spaces from every line."""
    lines = content.split("\n")
    return "\n".join(line.rstrip() for line in lines)


def parse_front_matter(content):
    """Return (front_matter_text, body_text, has_front_matter)."""
    if not content.startswith("---"):
        return "", content, False
    end = content.find("---", 3)
    if end == -1:
        return "", content, False
    fm = content[:end + 3]
    body = content[end + 3:]
    return fm, body, True


def fix_file(filepath):
    original = filepath.read_text(encoding="utf-8")
    fm, body, has_fm = parse_front_matter(original)

    # Only fix em dashes in the body — front matter titles are a manual call
    body = fix_em_dashes(body)

    # Trailing whitespace across the whole file (safe everywhere)
    content = fm + body if has_fm else body
    content = fix_trailing_whitespace(content)

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return True
    return False


def run():
    posts = sorted(POSTS_DIR.glob("*.md"))
    fixed_files = []

    for filepath in posts:
        if fix_file(filepath):
            fixed_files.append(filepath.name)

    if fixed_files:
        print(f"  Auto-fixed {len(fixed_files)} file(s):")
        for name in fixed_files:
            print(f"    - {name}")
    else:
        print("  Nothing to fix.")

    return len(fixed_files)


if __name__ == "__main__":
    changed = run()
    sys.exit(0)
