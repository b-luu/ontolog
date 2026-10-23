#!/usr/bin/env python3
"""Copy the bundled private-repository starter without overwriting a destination."""

import argparse
from pathlib import Path
import shutil


def initialize(destination: Path, with_example: bool = False) -> None:
    skill = Path(__file__).resolve().parents[1]
    template = skill / "assets" / "knowledge-repository"
    if any(p.is_file() and p.name != ".gitkeep" for p in (template / "records").rglob("*")):
        raise ValueError("The bundled template contains company records; eject only a clean template.")
    if any(p.is_symlink() for p in template.rglob("*")):
        raise ValueError("The bundled template contains symlinks; eject only a clean template.")
    # Also works for an installed standalone skill, without depending on Git.
    source_root = skill
    packaged_root = skill.parent.parent
    if skill.parent.name == "skills" and (packaged_root / "docs" / "scope-and-integration.md").is_file():
        source_root = packaged_root
    for parent in skill.parents:
        if (parent / ".git").exists():
            source_root = parent
            break
    destination = destination.expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Destination already exists: {destination}")
    destination = destination.resolve()
    if destination == source_root or source_root in destination.parents:
        raise ValueError("Choose a destination outside the kit checkout or installed skill; keep organizational knowledge separate from the public template.")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Destination already exists: {destination}")
    # Exclude transient local state even if the template was opened in an editor.
    excluded = ["__pycache__", "*.pyc", ".venv", ".obsidian", ".git"]
    if not with_example:
        excluded.append("examples")
    shutil.copytree(template, destination, ignore=shutil.ignore_patterns(*excluded))
    for kind in ("domains", "contributors", "sources", "sessions", "concepts",
                 "assertions", "metrics", "questions", "decisions"):
        (destination / "records" / kind).mkdir(parents=True, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--with-example", action="store_true")
    args = parser.parse_args()
    try:
        initialize(args.destination.expanduser().absolute(), args.with_example)
    except (OSError, ValueError, shutil.Error) as exc:
        parser.exit(1, f"Cannot initialize repository: {exc}\n")
    print(f"Created {args.destination}. No Git history, remote, or hosted privacy setting was created. Read docs/setup.md and configure your organization's private storage before interviewing.")


if __name__ == "__main__":
    main()
