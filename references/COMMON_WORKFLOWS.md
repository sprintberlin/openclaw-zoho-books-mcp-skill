# Verified Zoho Books MCP Workflows

Step-by-step procedures for frequent Books tasks. All operations assume `mcporter` and a configured `ZOHO_BOOKS_MCP_URL` plus `organization_id`.

## 1. Organization discovery and verification

```text
list organizations -> get organization
```

1. Run `list organizations` to discover accessible organizations.
2. Record the target `organization_id`.
3. Verify currency, time zone, and country settings with `get organization`.
4. Always pass `organization_id` in subsequent calls.

## 2. Contact and vendor lookup

```text
list contacts -> get contact
```

1. Query contacts: `list contacts` with filters (e.g. `contact_type=vendor` or `search_text`).
2. Inspect full details: `get contact` with `contact_id`.
3. Check currency, payment terms, and existing balance before creating transactions.

## 3. Invoice inspection and status verification

```text
list invoices -> get invoice
```

1. List invoices: `list invoices` with status filter (`Status.Unpaid`, `Status.Overdue`, etc.).
2. Inspect line items, tax details, and payments: `get invoice` with `invoice_id`.
3. Verify payment status before sending reminders.

## 4. Expense tracking and verification

```text
list expenses -> get expense -> create expense
```

1. Check for existing expense: `list expenses` with date and reference number to prevent duplicates.
2. Inspect category and tax rules: `get expense` on a similar past entry.
3. Create expense: `create expense` with verified account ID, amount, and tax ID.
4. Read back the created expense with `get expense` to verify tax and total amounts.
