#!/usr/bin/env python3
"""Eject an independent knowledge repository or install/export the Ontolog skill."""

import argparse
import importlib.util
from pathlib import Path
import shutil
import sys
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
SKILL_NAME = "ontolog-interview"
SKILL = ROOT / "skills" / SKILL_NAME
IGNORED = {".git", ".venv", "__pycache__", ".obsidian", ".DS_Store"}


def ignored(directory, names):
    return [name for name in names if name in IGNORED or name.endswith(".pyc")]


def check_bundle():
    """Do not distribute a template someone has populated with company records."""
    records = SKILL / "assets" / "knowledge-repository" / "records"
    if not (SKILL / "SKILL.md").is_file() or not records.is_dir():
        raise ValueError("Ontolog's skill/template bundle is missing.")
    if any(p.is_file() and p.name != ".gitkeep" for p in records.rglob("*")):
        raise ValueError("The bundled template contains records. Keep company data in an ejected repository before installing or exporting this bundle.")
    if any(p.is_symlink() for p in SKILL.rglob("*")):
        raise ValueError("The skill contains symlinks; use a clean source bundle for installation/export.")


def new_destination(path):
    path = path.expanduser().absolute()
    # Check before resolving, so a dangling symlink cannot redirect the write.
    if path.exists() or path.is_symlink():
        raise FileExistsError(f"Destination already exists: {path}")
    return path.resolve()


def install(agent, destination=None):
    check_bundle()
    if destination is None:
        locations = {
            "codex": Path.home() / ".agents" / "skills" / SKILL_NAME,
            "claude-code": Path.home() / ".claude" / "skills" / SKILL_NAME,
        }
        if agent not in locations:
            raise ValueError("For another local harness, provide --agent custom --dest /path/to/skills/ontolog-interview.")
        destination = locations[agent]
    destination = new_destination(Path(destination))
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError("Install outside the public Ontolog checkout.")
    if destination.name != SKILL_NAME:
        raise ValueError(f"The destination folder must be named {SKILL_NAME} to match SKILL.md.")
    shutil.copytree(SKILL, destination, ignore=ignored)
    return destination


def export_skill(destination):
    check_bundle()
    destination = new_destination(Path(destination))
    if destination == SKILL or SKILL in destination.parents:
        raise ValueError("Export outside the skill folder.")
    if destination.suffix.lower() != ".zip":
        raise ValueError("Export destination must end in .zip.")
    files = [p for p in SKILL.rglob("*") if p.is_file()
             and not any(part in IGNORED for part in p.relative_to(SKILL).parts)
             and p.suffix != ".pyc"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "x", compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, (Path(SKILL_NAME) / path.relative_to(SKILL)).as_posix())
    return destination


def eject(destination, with_example=False):
    check_bundle()
    path = SKILL / "scripts" / "init_repository.py"
    spec = importlib.util.spec_from_file_location("ontolog_initializer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    destination = new_destination(Path(destination))
    module.initialize(destination, with_example)
    return destination


def choose_agent():
    if not sys.stdin.isatty():
        raise ValueError("Non-interactive input: specify --agent codex, --agent claude-code, or --agent custom --dest PATH. Use export-skill for a ZIP.")
    print("Where will you use Ontolog?")
    print("1. Codex local (CLI, IDE, or local app workspace)")
    print("2. Claude Code local")
    print("3. Another local harness (provide its skill folder)")
    print("4. Claude web/Cowork or another app with skill ZIP import (export only)")
    choice = input("Choose 1-4: ").strip()
    agents = {"1": "codex", "2": "claude-code", "3": "custom", "4": "export"}
    if choice not in agents:
        raise ValueError("Choose a number from 1 to 4.")
    return agents[choice]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    repository = commands.add_parser("eject", help="Copy a clean knowledge template outside this checkout")
    repository.add_argument("destination", type=Path)
    repository.add_argument("--with-example", action="store_true", help="Include isolated fictional examples; records/ stays empty")
    installer = commands.add_parser("install", help="Choose a local agent or export an uploadable skill ZIP")
    installer.add_argument("--agent", choices=["codex", "claude-code", "custom"])
    installer.add_argument("--dest", type=Path, help="Exact skill directory, ending in ontolog-interview")
    exporter = commands.add_parser("export-skill", help="Produce a ZIP; does not upload or register it")
    exporter.add_argument("destination", nargs="?", type=Path, default=ROOT / "dist" / f"{SKILL_NAME}.zip")
    args = parser.parse_args(argv)
    try:
        if args.command == "eject":
            dest = eject(args.destination, args.with_example)
            print(f"Created {dest}. Company records are empty; examples {'included separately' if args.with_example else 'omitted'}.")
            print("No Git history, remote, or hosted privacy setting was created. See docs/setup.md in your new repository.")
        elif args.command == "export-skill":
            print(f"Exported {export_skill(args.destination)}. Import it through a supported app's skill settings; this is not an installation.")
        else:
            agent = args.agent or ("custom" if args.dest else choose_agent())
            if agent == "export":
                print(f"Exported {export_skill(ROOT / 'dist' / f'{SKILL_NAME}.zip')}. See docs/installation.md for app import instructions.")
            else:
                dest = args.dest
                if agent == "custom" and dest is None and sys.stdin.isatty():
                    response = input("Exact skill destination (ending in ontolog-interview): ").strip()
                    if not response:
                        raise ValueError("A destination is required.")
                    dest = Path(response)
                installed = install(agent, dest)
                print(f"Installed {installed}. Open a new session or refresh skills in your harness.")
                print("Point the agent at your separately ejected company repository. Installation does not grant access to it.")
    except (OSError, ValueError, shutil.Error) as exc:
        parser.exit(1, f"Ontolog: {exc}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
