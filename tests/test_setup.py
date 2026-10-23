"""Exercise independent instances, safe local installation, and upload packaging."""

import contextlib
import importlib.util
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ontolog_setup", ROOT / "ontolog.py")
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def test_local_install_is_complete_and_independent(self):
        destination = self.directory / setup.SKILL_NAME
        setup.install("custom", destination)
        self.assertTrue((destination / "SKILL.md").is_file())
        self.assertTrue((destination / "references/interview-method.md").is_file())
        self.assertTrue((destination / "scripts/init_repository.py").is_file())
        result = subprocess.run([sys.executable, str(destination / "scripts/init_repository.py"), str(self.directory / "private")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(list((self.directory / "private/records").rglob("*.md")))

    def test_no_existing_skill_is_overwritten(self):
        destination = setup.install("custom", self.directory / setup.SKILL_NAME)
        note = destination / "local.txt"
        note.write_text("Local customization")
        with self.assertRaises(FileExistsError):
            setup.install("custom", destination)
        self.assertEqual(note.read_text(), "Local customization")

    def test_dangling_symlink_is_not_followed(self):
        destination = self.directory / setup.SKILL_NAME
        missing = self.directory / "missing"
        destination.symlink_to(missing, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            setup.install("custom", destination)
        self.assertFalse(missing.exists())

    def test_codex_and_claude_install_to_their_own_locations(self):
        with patch.object(setup.Path, "home", return_value=self.directory):
            codex = setup.install("codex")
            claude = setup.install("claude-code")
        self.assertEqual(codex, self.directory / ".agents/skills" / setup.SKILL_NAME)
        self.assertEqual(claude, self.directory / ".claude/skills" / setup.SKILL_NAME)
        self.assertTrue((codex / "SKILL.md").exists())
        self.assertTrue((claude / "SKILL.md").exists())

    def test_zip_contains_skill_folder_and_no_runtime_state(self):
        archive = setup.export_skill(self.directory / "skill.zip")
        with ZipFile(archive) as zipped:
            names = zipped.namelist()
            self.assertIn(f"{setup.SKILL_NAME}/SKILL.md", names)
            self.assertIn(f"{setup.SKILL_NAME}/LICENSE", names)
            self.assertTrue(all(name.startswith(setup.SKILL_NAME + "/") for name in names))
            self.assertFalse(any("__pycache__" in name or "/.git/" in name for name in names))
            self.assertTrue(all(name.endswith(".gitkeep") for name in names if "/knowledge-repository/records/" in name))
        with self.assertRaises(FileExistsError):
            setup.export_skill(archive)

    def test_ejection_is_empty_by_default_and_examples_are_isolated(self):
        empty = setup.eject(self.directory / "empty")
        example = setup.eject(self.directory / "demo", with_example=True)
        self.assertFalse((empty / "examples").exists())
        self.assertFalse(list((empty / "records").rglob("*.md")))
        self.assertFalse(list((example / "records").rglob("*.md")))
        self.assertTrue(list((example / "examples").rglob("*.md")))
        self.assertFalse((empty / ".git").exists())

    def test_noninteractive_install_requires_an_explicit_choice(self):
        result = subprocess.run([sys.executable, str(ROOT / "ontolog.py"), "install"], input="", capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("specify --agent", result.stderr)

    def test_interactive_custom_choice_installs_in_selected_folder(self):
        destination = self.directory / setup.SKILL_NAME
        with patch.object(setup.sys.stdin, "isatty", return_value=True), patch("builtins.input", side_effect=["3", str(destination)]), contextlib.redirect_stdout(io.StringIO()):
            result = setup.main(["install"])
        self.assertEqual(result, 0)
        self.assertTrue((destination / "SKILL.md").exists())

    def test_company_data_in_template_blocks_distribution(self):
        source = self.directory / "source" / setup.SKILL_NAME
        shutil.copytree(setup.SKILL, source)
        (source / "assets/knowledge-repository/records/private.md").write_text("Company data")
        with patch.object(setup, "SKILL", source):
            for operation in (lambda: setup.export_skill(self.directory / "leak.zip"),
                              lambda: setup.install("custom", self.directory / "installed" / setup.SKILL_NAME),
                              lambda: setup.eject(self.directory / "ejected")):
                with self.assertRaisesRegex(ValueError, "contains records"):
                    operation()
        self.assertFalse((self.directory / "leak.zip").exists())

    def test_installation_refuses_public_checkout(self):
        with self.assertRaisesRegex(ValueError, "outside the public"):
            setup.install("custom", ROOT / ".agents/skills" / setup.SKILL_NAME)


if __name__ == "__main__":
    unittest.main()
