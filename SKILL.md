---
name: "zoho-books-mcp"
description: "Zoho Books MCP endpoint setup, multi-account routing, organization selection, action profiles, helper CLIs, and safe accounting workflows."
---

# Zoho Books MCP

Use Zoho Books through an MCP endpoint from `mcp.zoho.eu`. This skill is the canonical home for Books-specific action documentation, least-privilege profiles, portable account routing, and helper CLIs.

Source: [sprintberlin/openclaw-zoho-books-mcp-skill](https://github.com/sprintberlin/openclaw-zoho-books-mcp-skill)

## Requirements

- A Zoho Books MCP endpoint from `mcp.zoho.eu`
- `mcporter`
- Endpoint configuration via `ZOHO_BOOKS_MCP_URL`, `--profile`, or `--mcp-url`
- A Zoho Books organization ID for organization-scoped calls

Treat the endpoint as a credential. Never print it, commit it, or copy it into tickets, prompts, or chats.

## First setup

1. Create or open a Zoho Books connection at `mcp.zoho.eu`.
2. Select only required Actions. Start with [references/ACTION_PROFILES.md](references/ACTION_PROFILES.md).
3. Configure one endpoint with `ZOHO_BOOKS_MCP_URL`, or named accounts using [references/MULTI_ACCOUNT.md](references/MULTI_ACCOUNT.md).
4. Configure the organization ID with `ZOHO_BOOKS_ORGANIZATION_ID` or the selected profile's `organization_id`.
5. Inspect the selected live server with `mcporter list "$ZOHO_BOOKS_MCP_URL"`; finish only after the required Actions are present.

The catalog describes possible Actions, not what one MCP server has enabled. Runtime names normally use `ZohoBooks_` plus the setup Action name with spaces converted to underscores, for example `ZohoBooks_list_invoices`.

## Endpoint and organization selection

For one account, set `ZOHO_BOOKS_MCP_URL` and `ZOHO_BOOKS_ORGANIZATION_ID`. For multiple accounts, pass `--profile NAME` to a bundled helper. Profiles default to `~/.config/zoho-mcp/profiles.json` and can reference an environment variable, a local URL file, or a direct URL.

Endpoint resolution order:

1. `--mcp-url`
2. `--profile`, `ZOHO_BOOKS_MCP_PROFILE`, or `ZOHO_MCP_PROFILE`
3. `ZOHO_BOOKS_MCP_URL`

Organization resolution order:

1. `--organization-id`
2. selected profile's `organization_id`
3. `ZOHO_BOOKS_ORGANIZATION_ID`
4. `ZOHO_ORGANIZATION_ID`

One-off `--mcp-url` can expose the credential in shell history or process listings. Prefer a profile backed by an injected environment variable or `url_file`.

## Safe workflow

1. Resolve the exact account and organization before reading data. Never reuse an endpoint or organization ID from another customer.
2. Inspect the live Actions and the selected Action schema before the first call.
3. Read the target contact, document, payment, account, or setting before changing it.
4. Use the organization ID returned by `list organizations`; never infer it from names or transfer one between profiles.
5. Send only intended fields, then read the affected record back and compare IDs, amounts, currency, tax, status, and contact.
6. Keep delete, void, refund, payment, bank matching, reconciliation, workflow, tax, and administrative Actions disabled unless the task explicitly requires them.
7. Treat email, SMS, reminders, payment collection, and portal invitations as external communication requiring the active approval policy.

## Bundled helpers

List organizations without requiring an organization ID:

```bash
python3 scripts/list_organizations.py --profile acme
```

List organization-scoped records:

```bash
python3 scripts/list_records.py contacts --profile acme --limit 20
python3 scripts/list_records.py invoices --profile acme --query status=unpaid --json
python3 scripts/list_records.py expenses --profile acme --query vendor_id=123456789 --json
```

Supported resources are `contacts`, `invoices`, `expenses`, `bills`, and `items`. `--query KEY=VALUE` can be repeated and must match the live Action schema. Pagination is automatic.

All helpers accept `--mcp-url`, `--profile`, `--profiles-file`, and `--timeout`. Organization-scoped helpers also accept `--organization-id`. Run `--help` without credentials. Unknown or incomplete options exit with status 2.

## Direct mcporter calls

For direct calls, include `organization_id` for organization-scoped Actions:

```bash
cat > /tmp/books_invoices.json <<'JSON'
{
  "query_params": {
    "organization_id": "<ORGANIZATION_ID>",
    "page": 1,
    "per_page": 100
  }
}
JSON
mcporter call "$ZOHO_BOOKS_MCP_URL.ZohoBooks_list_invoices" --args "$(< /tmp/books_invoices.json)"
```

Use the schema shown by the live MCP server when it differs. Write nested arguments to a temporary JSON file instead of fragile shell quoting.

## Accounting safeguards

- Confirm gross amount, net amount, tax, currency, exchange rate, date, contact, reference number, and account before creating or updating a transaction.
- Search for duplicates using reference number plus contact and amount before creating a document or payment.
- Never fabricate contact IDs, account IDs, tax IDs, item IDs, payment IDs, document IDs, or organization IDs.
- Creating a payment, refund, bank match, reconciliation, credit application, or write-off changes accounting state. Require an explicit task and verify the resulting ledger state.
- `mark ... void`, delete, and cancellation Actions are destructive. Keep them out of normal profiles.
- Binary attachment Actions vary by server and may be unavailable or unreliable. Verify the transferred file by reading it back; use a confirmed REST upload workflow when MCP does not support the binary operation.

## References

- [Action profiles](references/ACTION_PROFILES.md): least-privilege starting sets
- [Common workflows](references/COMMON_WORKFLOWS.md): ordered procedures for frequent Books tasks
- [Complete Books Actions catalog](references/ZOHO_BOOKS_MCP_ACTIONS.md): all known Books Actions and descriptions
- [Multi-account profiles](references/MULTI_ACCOUNT.md): portable routing for CRM, People, and Books

Load the profile reference while configuring a connection. Load a workflow while performing that task. Load the full catalog only when the profiles do not contain a required Action.

## Troubleshooting

- **No endpoint configured**: set `ZOHO_BOOKS_MCP_URL`, select `--profile`, or pass `--mcp-url`; never print the value.
- **No organization ID configured**: use `--organization-id`, profile `organization_id`, or `ZOHO_BOOKS_ORGANIZATION_ID`.
- **Profile not found or wrong app**: verify `--profiles-file`, profile name, and `services.books`.
- **Action missing**: inspect the live server; enabling an Action in documentation does not enable it remotely.
- **OAuth scope error**: reconnect the affected Books connection. Never switch to another customer's endpoint.
- **Unexpected tax or amount**: stop, read the saved record, and compare organization currency, tax mode, line items, and rounding before another write.
