#!/usr/bin/env python3
"""Check local inline Markdown links, heading fragments, and guide reachability.

This checks the link style used by Ontolog, not every Markdown dialect. It does
not fetch external URLs. Release URL placeholders are allowed only in release
drafts. Knowledge records are checked for broken links but are excluded from
navigation coverage because their primary references are structured IDs.
"""

import argparse
from collections import deque
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

SKIP = {".git", ".venv", "__pycache__", "dist"}
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)")


def prose(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)
    output, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)


def headings(text):
    result, used = set(), set()
    for line in prose(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = LINK.sub(lambda m: m.group(0).split("](", 1)[0].lstrip("[!"), match.group(1))
        title = re.sub(r"<[^>]*>", "", title).lower()
        base = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        slug, suffix = base, 0
        while slug in used:
            suffix += 1
            slug = f"{base}-{suffix}"
        used.add(slug)
        result.add(slug)
    return result


def audit(root, entry="README.md"):
    root = Path(root).resolve()
    pages = {p.resolve(): p.read_text(encoding="utf-8") for p in root.rglob("*.md")
             if not any(part in SKIP for part in p.relative_to(root).parts)}
    errors, graph = [], {p: set() for p in pages}
    for path, text in pages.items():
        relative = path.relative_to(root)
        for match in LINK.finditer(prose(text)):
            raw = match.group(1).strip()
            target = raw[1:-1] if raw.startswith("<") else raw.split()[0]
            if re.fullmatch(r"\{[A-Z_]+\}", target) and "release" in relative.parts:
                continue
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(root):
                errors.append(f"{relative}: link escapes this artifact: {target}")
                continue
            if destination.is_dir():
                destination /= "README.md"
            if not destination.is_file():
                errors.append(f"{relative}: missing target: {target}")
                continue
            if destination in pages:
                graph[path].add(destination)
                if url.fragment and unquote(url.fragment) not in headings(pages[destination]):
                    errors.append(f"{relative}: missing heading: {target}")
    start = (root / entry).resolve()
    if start not in pages:
        errors.append(f"Missing Markdown entry point: {entry}")
    reached, queue = set(), deque([start])
    while queue:
        page = queue.popleft()
        if page in reached:
            continue
        reached.add(page)
        queue.extend(graph.get(page, set()) - reached)
    required = {p for p in pages if "records" not in p.relative_to(root).parts}
    for page in sorted(required - reached):
        errors.append(f"{page.relative_to(root)}: not reachable from {entry}")
    return errors, len(pages), len(required)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--entry", default="README.md")
    args = parser.parse_args()
    errors, pages, guides = audit(args.root, args.entry)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {pages} Markdown files; all {guides} guides reachable from {args.entry}. Local targets and heading fragments resolve. External URLs not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
