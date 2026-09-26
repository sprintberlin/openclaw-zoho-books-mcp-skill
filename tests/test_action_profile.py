"""Checks that the documented Accountant profile uses real, unique catalog Actions."""

from __future__ import annotations

from pathlib import Path
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
PROFILE = REPOSITORY / "references" / "ACTION_PROFILES.md"
CATALOG = REPOSITORY / "references" / "ZOHO_BOOKS_MCP_ACTIONS.md"


def catalog_actions() -> set[str]:
    actions: set[str] = set()
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ") and not line.startswith(("| Aktion", "| :---")):
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if cells:
                actions.add(cells[0])
    return actions


def profile_actions() -> list[str]:
    actions: list[str] = []
    in_action_block = False
    for line in PROFILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "```text":
            in_action_block = True
            continue
        if stripped == "```" and in_action_block:
            in_action_block = False
            continue
        if in_action_block and stripped:
            actions.append(stripped)
    return actions


class ActionProfileTests(unittest.TestCase):
    def test_profile_actions_exist_in_catalog(self):
        catalog = catalog_actions()
        missing = sorted(set(profile_actions()) - catalog)
        self.assertEqual(missing, [])

    def test_profile_actions_are_unique(self):
        actions = profile_actions()
        self.assertEqual(len(actions), len(set(actions)))

    def test_profile_has_no_delete_or_bulk_mutations(self):
        forbidden = [
            action
            for action in profile_actions()
            if action.startswith("delete ") or action.startswith("bulk ")
        ]
        self.assertEqual(forbidden, [])

    def test_profile_covers_core_accounting_workflows(self):
        actions = set(profile_actions())
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


if __name__ == "__main__":
    unittest.main()
