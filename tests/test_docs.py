"""Validate navigation failures and portability of the distributed docs."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


docs = load("docs_checker", ROOT / "tools/check_docs.py")
setup = load("setup_for_docs", ROOT / "ontolog.py")


class DocumentationTests(unittest.TestCase):
    def test_missing_targets_fragments_and_unreachable_guides_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Start\n[Missing](missing.md)\n[Heading](guide.md#missing)\n")
            (root / "guide.md").write_text("# Guide\n")
            (root / "orphan.md").write_text("# Orphan\n")
            errors, _, _ = docs.audit(root)
            self.assertTrue(any("missing target" in e for e in errors), errors)
            self.assertTrue(any("missing heading" in e for e in errors), errors)
            self.assertTrue(any("orphan.md: not reachable" in e for e in errors), errors)

    def test_links_in_code_are_ignored_and_duplicate_headings_resolve(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Start\n[Second](#section-1)\n## Section\n## Section\n```md\n[Example](nonexistent.md)\n```\n")
            self.assertEqual(docs.audit(root)[0], [])

    def test_repository_docs_are_reachable(self):
        self.assertEqual(docs.audit(ROOT)[0], [])

    def test_ejected_docs_work_without_public_checkout_or_examples(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = setup.eject(Path(tmp) / "company")
            self.assertFalse((destination / "examples").exists())
            self.assertEqual(docs.audit(destination)[0], [])

    def test_installed_skill_docs_are_self_contained(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = setup.install("custom", Path(tmp) / setup.SKILL_NAME)
            self.assertEqual(docs.audit(destination, "SKILL.md")[0], [])


if __name__ == "__main__":
    unittest.main()
