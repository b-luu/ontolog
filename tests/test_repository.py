"""Exercise review boundaries, portable copies, and malformed contributions."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/ontolog-interview"
TEMPLATE = SKILL / "assets/knowledge-repository"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_module("repository_validator", TEMPLATE / "tools/validate.py")
initializer = load_module("repository_initializer", SKILL / "scripts/init_repository.py")


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "dataset"
        shutil.copytree(TEMPLATE / "examples/subscription-business", self.root)

    def change(self, rid, **updates):
        path = self.root / "records" / f"{rid}.md"
        old = path.read_text()
        r = validator.parse_record(path)
        r.update(updates)
        body = old.split("\n---\n", 1)[1]
        path.write_text("---\n" + yaml.safe_dump(r, sort_keys=False) + "---\n" + body)

    def errors(self):
        return validator.validate(self.root)[0]

    def assert_invalid(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_scoped_definitions_and_proposed_mapping_coexist(self):
        self.assertEqual(self.errors(), [])
        r = validator.parse_record(self.root / "records/assertion-active-close-match.md")
        self.assertEqual(r["status"], "proposed")

    def test_labels_do_not_define_identity(self):
        self.change("concept-product-active", title="Active customer")
        self.change("concept-finance-active", title="Active customer")
        self.assertEqual(self.errors(), [])

    def test_rename_does_not_break_id_references(self):
        path = self.root / "records/concept-product-active.md"
        path.rename(path.with_name("a-new-readable-name.md"))
        self.assertEqual(self.errors(), [])

    def test_confirmation_is_not_organizational_approval(self):
        self.change("concept-product-active", status="approved")
        self.assert_invalid("approved adoption decision")

    def test_confirmation_requires_evidence(self):
        self.change("concept-product-active", confirmation_source_ids=[])
        self.assert_invalid("Confirmed record needs confirmation_source_ids")

    def test_approval_cannot_be_extended_to_a_different_scope(self):
        self.change("metric-finance-active", scope_ids=["domain-finance", "domain-product"])
        self.assert_invalid("all its scopes")

    def approve_with_period(self, kind, **period):
        """Adopt each definition type with a bounded, explicitly retroactive decision."""
        self.change("assertion-active-close-match", status="proposed")
        rid = {"concept": "concept-finance-active", "assertion": "assertion-active-close-match",
               "metric": "metric-finance-active"}[kind]
        self.change("decision-finance-active", effective_from="2026-01-01",
                    effective_to="2026-07-01",
                    target_ids=["concept-finance-active", "metric-finance-active", rid]
                    if kind == "assertion" else ["concept-finance-active", "metric-finance-active"])
        for target in ("concept-finance-active", "metric-finance-active"):
            self.change(target, effective_from="2026-01-01", effective_to="2026-07-01")
        updates = dict(status="approved", decision_id="decision-finance-active", **period)
        if kind == "assertion":
            updates.update(scope_ids=["domain-finance"], evidence_kind="stated", unknowns=[])
        self.change(rid, **updates)
        return rid

    def test_approval_period_must_cover_each_definition_type(self):
        for kind in ("concept", "assertion", "metric"):
            for period in ({"effective_from": "2025-12-31", "effective_to": "2026-02-01"},
                           {"effective_from": "2026-06-01", "effective_to": "2026-07-02"},
                           {"effective_from": "2026-07-01", "effective_to": "2026-08-01"},
                           {"effective_from": "2026-08-01", "effective_to": "2026-09-01"}):
                with self.subTest(kind=kind, period=period):
                    self.approve_with_period(kind, **period)
                    self.assert_invalid("Adoption decision must cover this record's effective period")

    def test_contained_and_retroactive_approval_periods_are_valid(self):
        for kind in ("concept", "assertion", "metric"):
            for period in ({"effective_from": "2026-01-01", "effective_to": "2026-07-01"},
                           {"effective_from": "2026-02-01", "effective_to": "2026-06-01"}):
                with self.subTest(kind=kind, period=period):
                    self.approve_with_period(kind, **period)
                    self.assertEqual(self.errors(), [])

    def test_omitted_approved_bounds_inherit_decision_period(self):
        for kind in ("concept", "assertion", "metric"):
            for omitted in (("effective_from",), ("effective_to",),
                            ("effective_from", "effective_to")):
                with self.subTest(kind=kind, omitted=omitted):
                    rid = self.approve_with_period(kind, effective_from="2026-02-01",
                                                   effective_to="2026-06-01")
                    path = self.root / "records" / f"{rid}.md"
                    r = validator.parse_record(path)
                    for field in omitted:
                        del r[field]
                    body = path.read_text().split("\n---\n", 1)[1]
                    path.write_text("---\n" + yaml.safe_dump(r, sort_keys=False) + "---\n" + body)
                    self.assertEqual(self.errors(), [])

    def test_inherited_approval_bounds_cannot_make_an_empty_period(self):
        for period, omitted in (({"effective_from": "2026-07-01"}, "effective_to"),
                                ({"effective_to": "2026-01-01"}, "effective_from")):
            with self.subTest(period=period):
                rid = self.approve_with_period("concept", **period)
                path = self.root / "records" / f"{rid}.md"
                r = validator.parse_record(path)
                r.pop(omitted, None)
                body = path.read_text().split("\n---\n", 1)[1]
                path.write_text("---\n" + yaml.safe_dump(r, sort_keys=False) + "---\n" + body)
                self.assert_invalid("Adoption decision must cover this record's effective period")

    def test_approval_with_no_end_allows_later_periods(self):
        self.change("concept-finance-active", effective_from="2030-01-01",
                    effective_to="2031-01-01")
        self.assertEqual(self.errors(), [])

    def test_cross_scope_decision_needs_a_steward_for_each_scope(self):
        self.change("decision-finance-active", scope_ids=["domain-finance", "domain-product"])
        self.assert_invalid("No configured steward approved decision scope domain-product")

    def test_reporter_cannot_substitute_for_declared_steward(self):
        self.change("decision-finance-active", approver_ids=["contributor-sam"])
        self.assert_invalid("No configured steward")

    def test_authorized_rejection_does_not_adopt_target(self):
        self.change("decision-finance-active", outcome="reject")
        self.assert_invalid("approved adoption decision")

    def test_unchecked_inference_cannot_become_approved(self):
        self.change("assertion-active-close-match", status="approved", evidence_kind="inferred")
        self.assert_invalid("Unchecked inferred assertion")

    def test_unknown_parameters_block_metric_approval(self):
        self.change("metric-finance-active", unknowns=["Timezone still under discussion"])
        self.assert_invalid("unresolved unknowns")

    def test_boundary_examples_needed_for_metric_review(self):
        self.change("metric-finance-active", worked_examples=["One invoice -> one customer"])
        self.assert_invalid("at least three worked examples")

    def test_dangling_and_wrong_type_evidence_fail(self):
        self.change("concept-product-active", source_ids=["source-missing", "contributor-alex"])
        self.assert_invalid("missing or invalid target source-missing")
        self.assert_invalid("wrong target type for contributor-alex")

    def test_duplicate_ids_from_combined_contributions_fail(self):
        path = self.root / "records/concept-product-active.md"
        shutil.copyfile(path, path.with_name("concurrent-copy.md"))
        self.assert_invalid("Duplicate ID")

    def test_duplicate_yaml_fields_do_not_hide_evidence(self):
        path = self.root / "records/concept-product-active.md"
        path.write_text(path.read_text().replace("type: concept", "type: concept\nsource_ids: []"))
        self.assert_invalid("Duplicate YAML key")

    def test_malformed_shapes_fail_without_crashing(self):
        for value in (None, {}, [], 42):
            with self.subTest(value=value):
                self.change("concept-product-active", status=value, source_ids=value)
                self.assertTrue(self.errors())

    def test_typo_is_not_silently_accepted_as_extension(self):
        self.change("concept-product-active", decison_id="decision-finance-active")
        self.assert_invalid("Unknown field decison_id")

    def test_clean_initializer_has_no_fictional_business_records(self):
        destination = Path(self.temp.name) / "new-private-repository"
        initializer.initialize(destination)
        self.assertFalse((destination / "examples").exists())
        self.assertEqual(validator.validate(destination), ([], 0))
        result = subprocess.run([sys.executable, str(destination / "tools/validate.py"), str(destination)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_example_is_opt_in_and_independently_valid(self):
        destination = Path(self.temp.name) / "with-example"
        initializer.initialize(destination, with_example=True)
        self.assertEqual(validator.validate(destination), ([], 0))
        self.assertEqual(validator.validate(destination / "examples/subscription-business")[0], [])

    def test_initializer_refuses_to_overwrite_existing_work(self):
        marker = self.root / "keep.txt"
        marker.write_text("existing interview")
        with self.assertRaises(FileExistsError):
            initializer.initialize(self.root)
        self.assertEqual(marker.read_text(), "existing interview")

    def test_initializer_refuses_company_records_inside_public_checkout(self):
        with self.assertRaisesRegex(ValueError, "outside the kit checkout"):
            initializer.initialize(ROOT / "company-knowledge")
        self.assertFalse((ROOT / "company-knowledge").exists())

    def test_initializer_resolves_symlink_before_checking_checkout_boundary(self):
        alias = Path(self.temp.name) / "kit-alias"
        alias.symlink_to(ROOT, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "outside the kit checkout"):
            initializer.initialize(alias / "company-knowledge")

    def test_ejected_repository_has_no_upstream_git_metadata(self):
        destination = Path(self.temp.name) / "independent-instance"
        initializer.initialize(destination)
        self.assertFalse((destination / ".git").exists())

    def test_downloaded_kit_without_git_preserves_separation(self):
        download = Path(self.temp.name) / "downloaded-kit"
        shutil.copytree(ROOT, download, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        downloaded_initializer = load_module("downloaded_initializer", download / "skills/ontolog-interview/scripts/init_repository.py")
        with self.assertRaisesRegex(ValueError, "outside the kit checkout"):
            downloaded_initializer.initialize(download / "company-knowledge")

    def test_standalone_skill_is_self_contained(self):
        standalone = Path(self.temp.name) / "installed-skill"
        shutil.copytree(SKILL, standalone, ignore=shutil.ignore_patterns("__pycache__"))
        installed_initializer = load_module("installed_initializer", standalone / "scripts/init_repository.py")
        destination = Path(self.temp.name) / "company-instance"
        installed_initializer.initialize(destination)
        self.assertEqual(validator.validate(destination), ([], 0))
        with self.assertRaisesRegex(ValueError, "outside the kit checkout"):
            installed_initializer.initialize(standalone / "company-knowledge")


if __name__ == "__main__":
    unittest.main()
