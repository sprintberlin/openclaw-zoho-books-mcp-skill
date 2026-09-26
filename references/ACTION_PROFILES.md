# Recommended Zoho Books MCP Action Profile

Zoho Books exposes roughly 1,090 MCP Actions. Do not enable the entire catalog for a normal agent. Use the single recommended **Books Accountant** profile for all day-to-day operational bookkeeping.

Names below match the Zoho MCP setup UI and the complete catalog in `ZOHO_BOOKS_MCP_ACTIONS.md`. Runtime tools usually appear with the `ZohoBooks_` prefix and underscores instead of spaces, for example `ZohoBooks_list_invoices`.

## Profile overview

1. **Books Accountant**: recommended operational profile. Covers master data, sales ledger, purchase ledger, banking, nominal ledger, attachments, and read-back verification. No delete, void, bulk, or administrative configuration actions.
2. **Books Developer or Administrator**: no blanket profile. Add configuration, blueprint, workflow, custom function, and administrative Actions individually for a defined task.

## Books Accountant

Select the following Actions in the Zoho MCP setup UI:

### Organization, Currencies, and Taxes

```text
list organizations
get organization
list currencies
get currency
list exchange rates
get exchange rate
create exchange rate
update exchange rate
list taxes
get tax
create tax
update tax
get tax group
create tax group
update tax group
```

### Chart of Accounts

```text
list chart of accounts
get chart of account
create chart of account
update chart of account
mark chart of account active
mark chart of account inactive
```

### Contacts and Vendors

```text
list contacts
get contact
create contact
update contact
list customers
list vendors
get contact by reference
get contact unused credits
get contact statement
list contact persons
get contact person
create contact person
update contact person
list contact addresses
get contact address
add contact address
update contact address
verify contact address
```

### Items

```text
list items
get item
create item
update item
list item details
mark item active
mark item inactive
```

### Sales and Accounts Receivable

```text
list invoices
get invoice
create invoice
update invoice
mark invoice sent
mark invoice draft
mark invoice void
get invoice by reference
list invoice payments
list customer payments
get customer payment
create customer payment
update customer payment
apply credits to invoice
list invoice credits applied
list credit notes
get credit note
create credit note
update credit note
mark credit note open
mark credit note void
apply credit note to invoice
list credit note refunds of all credit notes
get credit note refund
create credit note refund
update credit note refund
list sales receipts
get sales receipt
create sales receipt
update sales receipt
```

### Purchases and Accounts Payable

```text
list bills
get bill
create bill
update bill
mark bill open
mark bill void
list bill payments
list vendor payments
get vendor payment
create vendor payment
update vendor payment
apply credits to a bill
apply credits to bill
list bills credited
list vendor credits
get vendor credit
create vendor credit
update vendor credit
mark vendor credit open
mark vendor credit void
list expenses
get expense
create expense
update expense
```

### Banking and Reconciliation

```text
list bank accounts
get bank account
get bank account balance
get bank account balances
list bank transactions
list bank account transactions
get bank transaction
get matching bank transactions
match bank transaction
unmatch bank transaction
categorize bank transaction
categorize bank transaction as customer payment
categorize bank transaction as vendor payment
categorize bank transaction as expense
categorize bank transaction as payment refund
categorize as credit note refunds
categorize as vendor credit refunds
categorize as vendor payment refund
create bank reconciliation
list bank reconciliations
get bank reconciliation
```

### Journals and General Ledger

```text
list journals
get journal
create journal
update journal
list chart of account transactions
```

### Financial and Tax Reports (Read-Only)

```text
get profit and loss report
get balance sheet report
get cash flow report
get trial balance report
get general ledger report
get general ledger details report
get journal report
get account transactions report
get ar aging summary report
get ar aging details report
get ap aging summary report
get ap aging details report
get receivable summary report
get payable summary report
```

### Comments and Attachments

```text
add invoice comment
list invoice comments
add bill comment
get bill comments
add contact comment
list contact comments
list expense comments
add credit note comment
list credit note comments
add vendor credit comment
list vendor credit comments
add invoice document
upload invoice document
add contact attachment
add credit note attachment
add bank reconciliation attachment
```

Safeguards:

- All calls except `list organizations` require `organization_id`.
- Use `query_params` with `page` and `per_page` for pagination.
- Always read existing records before updating.
- Check for duplicates using reference number, contact, and amount before creating transactions.
- Verify tax IDs, gross/net amounts, and currency before creating transactions.
- Keep all `delete` and bulk mutation Actions disabled by default.
- Void actions (`mark invoice void`, `mark bill void`, `mark credit note void`, `mark vendor credit void`) are included for corrections but must only be used when explicitly requested.
- Binary attachment uploads for bills and expenses are not reliably supported by generic MCP Actions. Use a confirmed REST upload workflow or the `zoho-attachment-bridge` skill where available, and verify the upload by reading it back.

## Books Developer or Administrator

Do not create a reusable blanket profile. Add high-impact Actions individually for the current task and remove them again when the task is complete. This includes workflows, blueprints, custom functions, email alerts, webhooks, organization settings, user roles, and other administrative configuration.

## Explicitly excluded from normal profiles

- Every `delete*`, `bulk delete*`, and permanent-delete Action
- Bulk mutations (`bulk update*`, `bulk approve*`, `bulk mark*`)
- Workflows, blueprints, custom functions, webhooks, and email alerts
- Organization settings, user roles, and administrative configuration
- Outbound email, SMS, reminders, and portal invitations (unless explicitly authorized by the active approval policy)

## Validation after creating an MCP server

1. Run `mcporter list "$ZOHO_BOOKS_MCP_URL"`.
2. For Books Accountant, confirm at least `list invoices`, `create invoice`, `list bills`, `create bill`, `list expenses`, `create expense`, `list bank transactions`, `match bank transaction`, and `categorize bank transaction` are present.
3. Search the returned list for unintended `delete`, `bulk`, `workflow`, `blueprint`, `function`, and `webhook` Actions.
4. Remove unintended high-impact Actions in `mcp.zoho.eu` and reconnect if OAuth scopes changed.
5. Test one read first. Test writes only in the intended organization and verify the result afterward.
