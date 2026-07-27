#!/usr/bin/env python3
"""Blog quality checker for monishas9011.github.io"""

import re
import sys
from pathlib import Path

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    VADER_AVAILABLE = True
except ImportError:
    VADER_AVAILABLE = False

# ── Configuration ──────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
POSTS_DIR = REPO_ROOT / "_posts"

REQUIRED_FRONT_MATTER = ["title", "date", "categories"]
STANDARD_HEADER_SIZE = (1200, 630)   # Change this if you settle on a different size
NEGATIVITY_THRESHOLD = -0.5

NON_DESCRIPTIVE_LINKS = {"click here", "here", "read more", "this", "link", "more", "learn more"}
FILLER_PHRASES = [
    "in order to",
    "it is important to note",
    "as mentioned earlier",
    "please note that",
    "it should be noted",
]

# ── Result collectors ──────────────────────────────────────────────────────────

issues = []    # Hard fails — block publish
warnings = []  # Soft flags — review recommended


def fail(filepath, check, message, line=None):
    loc = f"{Path(filepath).name}:{line}" if line else Path(filepath).name
    issues.append(f"  FAIL  [{check}] {loc}\n        {message}")


def warn(filepath, check, message, line=None):
    loc = f"{Path(filepath).name}:{line}" if line else Path(filepath).name
    warnings.append(f"  WARN  [{check}] {loc}\n        {message}")


# ── Front matter parser ────────────────────────────────────────────────────────

def parse_front_matter(content):
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end]
    body = content[end + 3:].strip()
    if YAML_AVAILABLE:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except yaml.YAMLError:
            fm = {}
    else:
        fm = {}
        for line in fm_text.split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
    return fm, body


# ── Individual checks ──────────────────────────────────────────────────────────

def check_filename(filepath):
    """Filename must match YYYY-MM-DD-title.md for Jekyll to build correctly."""
    if not re.match(r"^\d{4}-\d{2}-\d{2}-.+\.md$", filepath.name):
        fail(filepath, "Filename", f"Must be YYYY-MM-DD-title.md — got: {filepath.name}")


def check_front_matter_fields(filepath, fm):
    """Required front matter fields must be present."""
    for field in REQUIRED_FRONT_MATTER:
        if field not in fm:
            fail(filepath, "Front matter", f"Missing required field: '{field}'")


def check_em_dashes(filepath, lines):
    """Em dashes (—) should not appear in posts. Skips HTML tag lines (e.g. — Monisha signature)."""
    for i, line in enumerate(lines, 1):
        if "—" in line and not re.match(r"\s*<", line):
            fail(filepath, "Em dash", "Em dash (—) found — use a regular hyphen or reword", line=i)


def check_headings(filepath, lines):
    """Headings must use sentence case and follow correct hierarchy."""
    h1_count = 0
    prev_level = 0

    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.+)", line)
        if not m:
            continue

        hashes, text = m.groups()
        level = len(hashes)

        # Only one H1 allowed
        if level == 1:
            h1_count += 1
            if h1_count > 1:
                fail(filepath, "Multiple H1", "Only one H1 heading allowed per post", line=i)

        # No skipping heading levels (e.g. H2 → H4)
        if prev_level > 0 and level > prev_level + 1:
            fail(filepath, "Heading hierarchy", f"Jumped from H{prev_level} to H{level}", line=i)
        prev_level = level

        words = text.split()
        if not words:
            continue

        # First word must be capitalised (skip if starts with a number)
        first_char = words[0][0]
        if first_char.isalpha() and not first_char.isupper():
            fail(filepath, "Heading case", f"First word must be capitalised: '{text}'", line=i)

        # Remaining words should not be title-cased (sentence case only)
        title_cased = sum(
            1 for w in words[1:]
            if len(w) > 3 and w[0].isupper() and not w.isupper()
        )
        if title_cased > len(words) // 2 and len(words) > 2:
            warn(filepath, "Heading case", f"Looks like title case — use sentence case: '{text}'", line=i)


def check_images(filepath, content, lines):
    """Images must exist, have alt text, and match the standard header size."""
    inline_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    for i, line in enumerate(lines, 1):
        for m in inline_re.finditer(line):
            alt, path = m.groups()

            # Skip external images
            if path.startswith("http"):
                continue

            if not alt.strip():
                fail(filepath, "Alt text", f"Image missing alt text: {path}", line=i)

            local = REPO_ROOT / path.lstrip("/")
            if not local.exists():
                fail(filepath, "Broken image", f"File not found: {path}", line=i)
            elif PIL_AVAILABLE:
                _check_dimensions(filepath, local, path, line)

    # Check front matter teaser image
    fm, _ = parse_front_matter(content)
    header = fm.get("header", {})
    if isinstance(header, dict):
        teaser = header.get("teaser", "")
        if teaser and not str(teaser).startswith("http"):
            local = REPO_ROOT / str(teaser).lstrip("/")
            if not local.exists():
                fail(filepath, "Broken image", f"Teaser image not found: {teaser}")
            elif PIL_AVAILABLE:
                _check_dimensions(filepath, local, str(teaser), None)


def _check_dimensions(filepath, local_path, ref, line):
    """Warn if image dimensions differ from the standard header size."""
    try:
        with Image.open(local_path) as img:
            w, h = img.size
            ew, eh = STANDARD_HEADER_SIZE
            if w != ew or h != eh:
                warn(
                    filepath, "Image size",
                    f"{Path(ref).name} is {w}x{h} — expected {ew}x{eh}",
                    line=line,
                )
    except Exception:
        pass


def check_links(filepath, lines):
    """Link text must be descriptive."""
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for i, line in enumerate(lines, 1):
        for m in link_re.finditer(line):
            text, _ = m.groups()
            if text.strip().lower() in NON_DESCRIPTIVE_LINKS:
                fail(filepath, "Link text", f"Non-descriptive link text: '[{text}]'", line=i)


def check_negativity(filepath, body):
    """Flag sentences with strongly negative sentiment."""
    if not VADER_AVAILABLE:
        warn(filepath, "Negativity check", "vaderSentiment not installed — skipping")
        return

    analyzer = SentimentIntensityAnalyzer()
    for sentence in re.split(r"(?<=[.!?])\s+", body):
        sentence = sentence.strip()
        if len(sentence) < 20:
            continue
        score = analyzer.polarity_scores(sentence)["compound"]
        if score < NEGATIVITY_THRESHOLD:
            preview = sentence[:90] + "..." if len(sentence) > 90 else sentence
            warn(filepath, "Negativity", f"Score {score:.2f}: \"{preview}\"")


def check_filler_phrases(filepath, lines):
    """Flag common filler phrases that weaken writing."""
    for i, line in enumerate(lines, 1):
        lower = line.lower()
        for phrase in FILLER_PHRASES:
            if phrase in lower:
                warn(filepath, "Filler phrase", f"Consider removing: '{phrase}'", line=i)


# ── Runner ─────────────────────────────────────────────────────────────────────

def run():
    posts = sorted(POSTS_DIR.glob("*.md"))

    if not posts:
        print("No posts found in _posts/ — nothing to check.")
        return

    print(f"\nChecking {len(posts)} post(s)...\n")

    for filepath in posts:
        content = filepath.read_text(encoding="utf-8")
        lines = content.splitlines()
        fm, body = parse_front_matter(content)
        body_lines = body.splitlines()

        check_filename(filepath)
        check_front_matter_fields(filepath, fm)
        check_em_dashes(filepath, lines)
        check_headings(filepath, body_lines)
        check_images(filepath, content, lines)
        check_links(filepath, body_lines)
        check_negativity(filepath, body)
        check_filler_phrases(filepath, body_lines)

    print("=" * 64)
    print("  QUALITY CHECK REPORT")
    print("=" * 64)

    if issues:
        print(f"\n  {len(issues)} issue(s) found — fix before publishing:\n")
        for issue in issues:
            print(issue)
            print()

    if warnings:
        print(f"\n  {len(warnings)} warning(s) — review recommended:\n")
        for w in warnings:
            print(w)
            print()

    if not issues and not warnings:
        print("\n  All checks passed. Good to go.\n")

    print("=" * 64 + "\n")

    if issues:
        sys.exit(1)


if __name__ == "__main__":
    run()
