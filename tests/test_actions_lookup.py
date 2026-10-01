"""Tests for the Books actions catalog, profiles, and lookup CLI."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPOSITORY / "references" / "actions.jsonl"
PROFILES_PATH = REPOSITORY / "references" / "profiles.json"
LOOKUP_SCRIPT = REPOSITORY / "scripts" / "lookup_actions.py"

sys.path.insert(0, str(REPOSITORY / "scripts"))
import lookup_actions  # noqa: E402
import import_actions  # noqa: E402


class ActionsCatalogAndLookupTests(unittest.TestCase):
    def test_catalog_file_is_valid_jsonl(self):
        self.assertTrue(CATALOG_PATH.exists(), f"missing {CATALOG_PATH}")
        lines = [
            line.strip()
            for line in CATALOG_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertGreaterEqual(len(lines), 1090)
        keys = set()
        for idx, line in enumerate(lines, start=1):
            data = json.loads(line)
            for required in ("key", "name", "summary", "description"):
                self.assertIn(required, data)
                self.assertTrue(str(data[required]).strip())
            self.assertNotIn(data["key"], keys, f"duplicate key {data['key']} at line {idx}")
            keys.add(data["key"])

    def test_profiles_file_is_valid_and_consistent(self):
        self.assertTrue(PROFILES_PATH.exists(), f"missing {PROFILES_PATH}")
        data = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data.get("version"), 1)
        self.assertEqual(data.get("service"), "books")
        self.assertIn("profiles", data)
        self.assertIn("tasks", data)

        result = subprocess.run(
            [sys.executable, str(LOOKUP_SCRIPT), "--validate"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode, 0, f"validation failed:\n{result.stdout}\n{result.stderr}"
        )
        self.assertIn("Validation OK", result.stdout)

    def test_lookup_cli_profiles_listing(self):
        result = subprocess.run(
            [sys.executable, str(LOOKUP_SCRIPT), "--profiles"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("bookkeeper", result.stdout)
        self.assertIn("Books Accountant", result.stdout)

    def test_lookup_cli_profile_inspection(self):
        result = subprocess.run(
            [sys.executable, str(LOOKUP_SCRIPT), "--profile", "bookkeeper", "--names-only"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("list invoices", result.stdout)
        self.assertIn("create bill", result.stdout)
        self.assertIn("categorize bank transaction", result.stdout)

    def test_lookup_cli_search_names_only(self):
        result = subprocess.run(
            [sys.executable, str(LOOKUP_SCRIPT), "--search", "invoice", "--names-only"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("list invoices", result.stdout)
        self.assertIn("create invoice", result.stdout)

    def test_lookup_cli_action_inspection(self):
        result = subprocess.run(
            [sys.executable, str(LOOKUP_SCRIPT), "--action", "list invoices", "--json"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        self.assertEqual(data.get("key"), "list invoices")
        self.assertIn("invoices", data.get("description", "").lower())

    def test_bookkeeper_profile_fits_within_300_action_limit(self):
        data = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
        profiles = data["profiles"]
        actions = lookup_actions.resolve_profile_actions("bookkeeper", profiles)
        self.assertLessEqual(len(actions), 200, f"bookkeeper exceeded target: {len(actions)}")
        self.assertLessEqual(len(actions), 300, f"bookkeeper exceeded 300 limit: {len(actions)}")
        self.assertEqual(len(actions), 156)

    def test_bookkeeper_profile_contains_core_accounting_actions(self):
        data = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
        profiles = data["profiles"]
        actions = set(lookup_actions.resolve_profile_actions("bookkeeper", profiles))
        required = {
            "list organizations",
            "list chart of accounts",
            "create invoice",
            "create customer payment",
            "create bill",
            "create vendor payment",
            "create expense",
            "match bank transaction",
            "categorize bank transaction",
            "create bank reconciliation",
            "create journal",
            "get profit and loss report",
            "get balance sheet report",
        }
        self.assertTrue(required.issubset(actions), f"missing: {required - actions}")

    def test_bookkeeper_profile_excludes_delete_and_bulk_actions(self):
        data = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
        profiles = data["profiles"]
        actions = lookup_actions.resolve_profile_actions("bookkeeper", profiles)
        for act in actions:
            self.assertFalse(act.startswith("delete "), f"delete action in profile: {act}")
            self.assertFalse(act.startswith("bulk "), f"bulk action in profile: {act}")

    def test_importer_parses_dump_with_known_names(self):
        known_names = ["list invoices", "create invoice"]
        sample_dump = (
            "Authorize On Demand\n"
            "Group view\n"
            "All Tools\n"
            "Tools Name\n"
            "list invoices List all invoices with pagination.\n"
            "create invoice Create an invoice for a customer.\n"
            "new capitalized action Creates a brand new thing.\n"
        )
        parsed = import_actions.parse_dump(sample_dump, known_names)
        keys = {entry["key"]: entry for entry in parsed}
        self.assertIn("list invoices", keys)
        self.assertIn("create invoice", keys)
        self.assertIn("new capitalized action", keys)
        self.assertEqual(keys["list invoices"]["summary"], "List all invoices with pagination.")

    def test_importer_merges_additions_and_marks_removals(self):
        known = {
            "oldAction": {
                "key": "oldAction",
                "name": "oldAction",
                "summary": "Old",
                "description": "Old action",
                "added": "2026-08-01",
            }
        }
        current_entries = [
            {
                "key": "newAction",
                "name": "newAction",
                "summary": "New",
                "description": "New action",
            }
        ]
        merged = import_actions.merge(current_entries, known, today="2026-09-18")
        by_key = {item["key"]: item for item in merged}
        self.assertEqual(by_key["newAction"]["added"], "2026-09-18")
        self.assertNotIn("removed", by_key["newAction"])
        self.assertEqual(by_key["oldAction"]["removed"], "2026-09-18")


if __name__ == "__main__":
    unittest.main()
