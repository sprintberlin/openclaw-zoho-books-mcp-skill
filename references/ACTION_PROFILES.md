# Zoho Books MCP Action Profiles

This document provides human-readable guidance for the least-privilege Books profile configured in this skill.

The machine-readable source of truth is [`references/profiles.json`](profiles.json), validated against [`references/actions.jsonl`](actions.jsonl). Use `scripts/lookup_actions.py` for automated inspection, token-efficient searches, and copy-ready lists.

## The 300-Action Server Limit

A Zoho MCP server accepts at most 300 selected Actions per connection. The recommended profile contains 156 Actions and fits on one connection.

| Profile | Actions | Fits one MCP server |
|---|---:|---|
| `bookkeeper` | 156 | yes |

Fewer Actions mean a smaller tool catalog and less context consumed per session. When a job needs an Action outside this profile, add it deliberately for that task instead of enabling the full catalog.

## Books Accountant

The single recommended operational profile covers master data, sales and purchase ledgers, banking, reconciliation, journals, financial reports, comments, and attachments. It excludes delete, bulk, and administrative configuration Actions. Void Actions are included only for explicitly requested corrections.

```bash
# List all profiles
python3 scripts/lookup_actions.py --profiles

# Inspect the complete profile with descriptions
python3 scripts/lookup_actions.py --profile bookkeeper

# Get all 156 Action names, one per line, ready for the Zoho MCP setup UI
python3 scripts/lookup_actions.py --profile bookkeeper --names-only
```

### Coverage

- Organizations, currencies, exchange rates, taxes, and tax groups
- Chart of accounts
- Customers, vendors, contacts, addresses, and contact persons
- Items
- Invoices, customer payments, credit notes, refunds, and sales receipts
- Bills, vendor payments, vendor credits, and expenses
- Bank accounts, transactions, matching, categorization, and reconciliation
- Journals and general-ledger transactions
- Profit and loss, balance sheet, cash flow, trial balance, general ledger, journal, aging, receivable, and payable reports
- Selected comments and attachments

### Safeguards

- All calls except `list organizations` require `organization_id`.
- Use `query_params` with `page` and `per_page` for pagination.
- Read existing records before updating them.
- Search for duplicates by reference number, contact, and amount before creating transactions.
- Verify tax IDs, gross/net amounts, currency, and exchange rate before creating transactions.
- Keep every `delete` and bulk mutation Action disabled by default.
- Use `mark invoice void`, `mark bill void`, `mark credit note void`, and `mark vendor credit void` only for explicitly requested corrections.
- Binary attachment support varies by server. Verify every uploaded file by reading it back and use a confirmed REST upload workflow when MCP cannot transfer it reliably.

## Developer or Administrator Actions

Do not create a reusable blanket administrator profile. Add high-impact Actions individually for the current task and remove them when the task is complete. This includes workflows, blueprints, custom functions, email alerts, webhooks, organization settings, user roles, and other administrative configuration.

## Explicitly Excluded

- Every delete, bulk delete, and permanent-delete Action
- Bulk mutations such as bulk update, approve, or mark
- Workflows, blueprints, custom functions, webhooks, and email alerts
- Organization settings, user roles, and administrative configuration
- Outbound email, SMS, reminders, and portal invitations unless explicitly authorized by the active approval policy

## Validation After Creating an MCP Server

1. Run `mcporter list "$ZOHO_BOOKS_MCP_URL"`.
2. Confirm at least `list invoices`, `create invoice`, `list bills`, `create bill`, `list expenses`, `create expense`, `list bank transactions`, `match bank transaction`, and `categorize bank transaction` are present.
3. Search the returned list for unintended `delete`, `bulk`, `workflow`, `blueprint`, `function`, and `webhook` Actions.
4. Remove unintended high-impact Actions in `mcp.zoho.eu` and reconnect if OAuth scopes changed.
5. Test one read first. Test writes only in the intended organization and verify the result afterward.

See [`references/CATALOG_FORMAT.md`](CATALOG_FORMAT.md) for the catalog architecture and maintenance workflow.
