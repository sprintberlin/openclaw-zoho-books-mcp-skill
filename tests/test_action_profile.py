"""Checks that the machine-readable Books Accountant profile is valid and safe."""

from __future__ import annotations

import json
from pathlib import Path
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
CATALOG = REPOSITORY / "references" / "actions.jsonl"
PROFILES = REPOSITORY / "references" / "profiles.json"


def load_catalog_keys() -> set[str]:
    keys: set[str] = set()
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if line.strip():
            keys.add(json.loads(line)["key"])
    return keys


def load_profile_actions(profile_id: str = "bookkeeper") -> list[str]:
    data = json.loads(PROFILES.read_text(encoding="utf-8"))
    return data["profiles"][profile_id]["actions"]


class ActionProfileTests(unittest.TestCase):
    def test_profile_actions_exist_in_catalog(self):
        catalog = load_catalog_keys()
        missing = sorted(set(load_profile_actions()) - catalog)
        self.assertEqual(missing, [])

    def test_profile_actions_are_unique(self):
        actions = load_profile_actions()
        self.assertEqual(len(actions), len(set(actions)))

    def test_profile_has_no_delete_or_bulk_mutations(self):
        forbidden = [
            action
            for action in load_profile_actions()
            if action.startswith("delete ") or action.startswith("bulk ")
        ]
        self.assertEqual(forbidden, [])

    def test_profile_covers_core_accounting_workflows(self):
        actions = set(load_profile_actions())
        required = {
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
        self.assertEqual(sorted(required - actions), [])

    def test_profile_fits_single_connection(self):
        actions = load_profile_actions()
        self.assertEqual(len(actions), 156)
        self.assertLessEqual(len(actions), 300)


if __name__ == "__main__":
    unittest.main()
