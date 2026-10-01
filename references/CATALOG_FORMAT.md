# Action Catalog Format

This document describes how MCP Action knowledge is stored in this skill. The same layout is used by the other Zoho MCP skills (CRM, People, Books, Desk, WorkDrive, Social), so an agent learns the structure once and can then answer "which Actions do I need for this task" in any of them.

## Problem

A Zoho MCP app exposes hundreds of Actions. Books currently has 1,090. Written as prose Markdown, that catalog has three defects:

1. An agent must load thousands of lines into context to answer a small question.
2. Hand-written profile lists drift away from the real catalog, so Action names in a profile may no longer exist.
3. Zoho adds, renames, and removes Actions, and a prose file makes that invisible in review.

## Design

JSON is the only source of truth. There is no generated or hand-maintained Markdown catalog.

| File | Purpose |
|---|---|
| `references/actions.jsonl` | Every known Action, one JSON object per line |
| `references/profiles.json` | Role profiles and task recipes, referencing Action keys |
| `scripts/import_actions.py` | Rebuilds `actions.jsonl` from a Zoho MCP setup UI dump |
| `scripts/lookup_actions.py` | Answers profile, task, and search questions without loading the full catalog |

### Why JSONL for the catalog

One Action per line keeps Git diffs readable. When Zoho changes the catalog, review shows exactly which lines were added, changed, or marked removed, instead of one unreadable blob diff.

### Action record

```json
{"key":"list invoices","name":"list invoices","summary":"List all invoices with pagination.","description":"List all invoices with pagination. Supports query filtering by customer, status, and dates.","added":"2026-09-01"}
```

- `key`: unique identifier used by profiles and tasks. Equal to `name`.
- `name`: the Action name shown in the Zoho MCP setup UI.
- `summary`: shortened first line for fast scanning and list output.
- `description`: the untouched description text delivered by Zoho. It is the authoritative usage hint.
- `added`: date the Action first appeared in the catalog.
- `removed`: set when an Action disappears from a newer dump. The record is kept, so history stays visible.

Risk levels, module tags, and dependency graphs are deliberately not modelled. Zoho already states dependencies inside `description`, and any extra hand-maintained metadata would be the next thing to drift.

### Profiles

A profile is what an agent gets by default for a role. Books uses a single comprehensive operational profile:

```json
"bookkeeper": {
  "name": "Books Accountant",
  "description": "...",
  "actions": ["list organizations", "list invoices", "create bill"]
}
```

Profiles can compose through `extends` and `denied` if multiple roles are added in the future.

### Task recipes

A task recipe answers the practical question directly: which Actions must be enabled to complete one concrete job, such as matching a bank statement line. Recipes are flat, do not inherit, and may overlap freely.

## Usage

```bash
# Which profiles and task recipes exist
python3 scripts/lookup_actions.py --profiles
python3 scripts/lookup_actions.py --tasks

# Which Actions does a role need
python3 scripts/lookup_actions.py --profile bookkeeper

# Copy-ready list for the Zoho MCP setup UI
python3 scripts/lookup_actions.py --profile bookkeeper --names-only

# Find an Action by keyword
python3 scripts/lookup_actions.py --search "invoice"

# Read the full Zoho description of one Action
python3 scripts/lookup_actions.py --action "list invoices"
```

## Maintaining the catalog

1. Open the Zoho MCP setup UI for Zoho Books and copy the complete Action list into a text file.
2. Rebuild the catalog:

   ```bash
   python3 scripts/import_actions.py /tmp/books_actions_dump.txt --dry-run
   python3 scripts/import_actions.py /tmp/books_actions_dump.txt
   ```

3. Validate that profiles and tasks still reference existing Actions:

   ```bash
   python3 scripts/lookup_actions.py --validate
   ```

4. Fix any profile or task entry the validation rejects, then commit. The importer reports added, changed, and removed Actions so the change is visible in the commit message.

The catalog describes Actions that can exist for the app. It does not prove that an Action is enabled on a specific MCP server. Always confirm against the live server:

```bash
mcporter list "$ZOHO_BOOKS_MCP_URL"
```

Runtime tool names normally use the `ZohoBooks_` prefix with underscores (e.g. `ZohoBooks_list_invoices`).
