# Recommended Zoho Books MCP Action Profiles

Zoho Books exposes roughly 1,090 MCP Actions. Do not enable the entire catalog for a normal agent. Start with the smallest profile that covers the role and add individual Actions only after a real requirement appears.

Names below match the Zoho MCP setup UI and the complete catalog in `ZOHO_BOOKS_MCP_ACTIONS.md`. Runtime tools usually appear with the `ZohoBooks_` prefix and underscores instead of spaces, for example `ZohoBooks_list_invoices`.

## Profile overview

1. **Books Read-only Analyst**: inspect organizations, contacts, invoices, expenses, bills, items, and taxes without write permissions.
2. **Books Staff / Operator, read/write without delete**: recommended operational profile. Create and update contacts, invoices, expenses, bills, and items. No delete, void, refund, or direct banking operations.
3. **Books Developer or Administrator**: no blanket profile. Add configuration, blueprint, and administrative Actions individually for a defined task.

## Books Read-only Analyst

```text
list organizations
get organization
list contacts
get contact
list invoices
get invoice
list expenses
get expense
list bills
get bill
list items
get item
list taxes
list currencies
```

Safeguards:

- All calls except `list organizations` require `organization_id`.
- Use `query_params` with `page` and `per_page` for pagination.

## Books Staff / Operator, read/write without delete

Select every Action from **Books Read-only Analyst**, then add:

### Document and transaction creation / updates

```text
create contact
update contact
create invoice
update invoice
mark invoice sent
create expense
update expense
create bill
update bill
create item
update item
add invoice comment
add bill comment
```

Safeguards:

- Always read existing records before updating.
- Check for duplicates using reference number, contact, and amount.
- Verify tax IDs, gross/net amounts, and currency before creating transactions.
- Keep `delete` and `mark ... void` Actions disabled by default.
