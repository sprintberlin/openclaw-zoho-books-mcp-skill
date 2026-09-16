# Zoho Books MCP Actions

**Stand:** 01.09.2026  
**Anzahl:** 1.090 Actions  
**Quelle:** Export der im Zoho-MCP-Konfigurator bekannten Books-Actions

> Dieser Katalog beschreibt grundsätzlich bekannte Actions. Welche Actions ein konkreter MCP-Server tatsächlich aktiviert hat, muss immer mit `mcporter list <MCP_URL>` geprüft werden.

| Aktion / Befehl | Beschreibung |
| :--- | :--- |
| activate blueprint | Activate a blueprint to enforce the defined workflow. |
| activate workflow | Mark an existing workflow as active. |
| active tag | Mark a reporting tag as active so that you can use it on entities which you allowed. A newly created tag will be in draft state. Use this to mark that tag as ready. |
| active tag option | Mark a reporting tag's option as active. |
| add bank reconciliation attachment | Attach a file to a bank reconciliation. |
| add bill comment | Add a comment for a bill. |
| add contact address | Add an additional address for a contact using the arguments below. |
| add contact attachment | Attach a file to a contact. |
| add contact bank account | Add a bank account for a contact to enable automatic payment collection through ACH or bank transfer. |
| add contact card | Add a credit or debit card for a contact to enable automatic payment collection. |
| add contact comment | Add a comment to a contact. |
| add contact tax info | Add a tax information record to a contact. |
| add credit note attachment | Attach a file to a credit note. |
| add credit note comment | Add a comment to an existing credit note. |
| add credit note digital signature | Send a credit note for digital signature. |
| add invoice comment | Add a comment for an invoice. |
| add invoice digital signature | Send an invoice for digital signature. |
| add invoice document | Attach a document to a specific document slot of an invoice. |
| add invoice online payment bank account | Associate a bank account with an invoice to receive online payments. Use this to configure the bank account into which online payments for the invoice are deposited. |
| add item to portal | Make an item available in the customer portal. |
| add items to portal | Make multiple items available in the customer portal in a single request. |
| add journal comment | Add a comment for a journal. |
| add project comment | Post comment to a project. |
| add project task | The project task has been added. |
| add project user | Assign a users to a project. |
| add purchase order comment | Add a comment for a purchase order. |
| add retainer invoice comment | Add a comment for a retainer invoice. |
| add sales order comment | Add a comment for a sales order. |
| add task | Add a task. |
| add task comment | Add comment to a task. |
| add vendor credit comment | Add a comment to an existing vendor credit. |
| all tag options | Get all options for a reporting tag. |
| apply credit note substatus | Apply a custom sub-status to a credit note. |
| apply credit note to invoice | Apply credit note to existing invoices. |
| apply credits to a bill | Apply vendor credit to existing bills. |
| apply credits to bill | Apply the vendor credits from excess vendor payments to a bill. Multiple credits can be applied at once. |
| apply credits to invoice | Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once. |
| apply invoice substatus | Apply a custom sub-status to an invoice. |
| apply journal credits to bills | Applies available journal credits to bills. |
| apply journal credits to invoices | Applies available journal credits to invoices. |
| apply pricebook to invoice | Apply a price book to an invoice so that the price book rates are used for the invoice line items. |
| apply retainer payments to invoices | Apply the advance payments collected against a retainer invoice to one or more invoices. |
| approve bill | Approve a bill. |
| approve contact bank account | Approve a bank account added for a contact. |
| approve credit note | Approve a credit note. |
| approve credit notes | Approve multiple credit notes in a single request. Use this to approve credit notes that are pending approval in bulk. |
| approve estimate | Approve an estimate. |
| approve invoice | Approve an invoice. |
| approve invoices | Approve multiple invoices in a single request. Use this to approve invoices that are pending approval in bulk. |
| approve journal | Approves a journal. |
| approve purchase order | Approve a purchase order. |
| approve retainer invoice | Approve a retainer invoice. |
| approve sales order | Approve a sales order. |
| approve vendor credit | Approve a Vendor credit. |
| assign contact owner | Assign a user as the owner of a specific contact. Use this when a contact must be associated with a particular user for ownership and access purposes. |
| assign owner to contacts | Assign a user as the owner of multiple contacts in a single request. Use this to bulk-assign ownership for a set of contacts. |
| associate recurring invoice bank account | Associate a bank account with a recurring invoice for auto-bill so that generated invoices are charged to this bank account. |
| associate recurring invoice card | Associate a card with a recurring invoice for auto-bill so that generated invoices are charged to this card. |
| autocomplete projects | Returns a paginated list of projects whose name contains <code>search_text</code>. Use each item's <code>id</code> as the project id when building report query parameters: <code>rule</code> JSON (group <code>project</code>, field <code>project_ids</code>) or <code>compare_entities</code> with group <code>project</code>. OAuth scope: <code>ZohoBooks.projects.READ</code>. |
| bulk approve journals | Approves multiple journals. |
| bulk delete bank account rules | Delete multiple bank rules in a single request. |
| bulk delete base currency adjustments | Deletes multiple base currency adjustments. |
| bulk delete chart of accounts | Deletes multiple accounts. |
| bulk delete customer payments | Delete multiple customer payments. |
| bulk delete journals | Deletes multiple journals. |
| bulk delete register transactions | Bulk delete selected transactions on the account register. |
| bulk delete vendor payments | Delete multiple vendor payments. |
| bulk execute custom functions | Manually re-execute multiple failed custom functions from history. |
| bulk export estimates as pdf | Maximum of 25 estimates can be exported in a single pdf. |
| bulk export invoices as pdf | Maximum of 25 invoices can be exported in a single pdf. |
| bulk export sales orders as pdf | Maximum of 25 sales orders can be exported in a single pdf. |
| bulk fetch fields | Fetch fields for one or more entities in a single request. Optionally filter by last modified time to get only updated fields. |
| bulk fetch pricebooks | Retrieve multiple price lists in bulk. Use the filter parameters to narrow the price lists returned. |
| bulk invoice reminder | Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once. |
| bulk mark chart of accounts active | Marks multiple accounts as active. |
| bulk mark chart of accounts inactive | Marks multiple accounts as inactive. |
| bulk print estimates | Export estimates as pdf and print them. Maximum of 25 estimates can be printed. |
| bulk print invoices | Export invoices as pdf and print them. Maximum of 25 invoices can be printed. |
| bulk print sales orders | Export sales orders as pdf and print them. Maximum of 25 sales orders can be printed. |
| bulk publish journals | Publishes multiple draft journals. |
| bulk resend webhooks | Resend multiple failed webhook executions at once. |
| bulk submit journals | Submits multiple journals for approval. |
| bulk update bank account rules | Update multiple bank rules in a single request. |
| bulk update custom module records | Update existing custom module records in bulk. |
| bulk update register transactions | Bulk update transactions on the account register (for example, change account, branch, or date on selected entities). |
| cancel credit note einvoice | Cancel the e-invoice of a credit note on the Invoice Registration Portal (IRP). |
| cancel credit notes einvoice | Cancel the e-invoices of multiple credit notes on the Invoice Registration Portal (IRP). |
| cancel einvoice credit note | Cancel the e-invoice generated for a credit note on the Invoice Registration Portal (IRP). |
| cancel einvoice invoice | Cancel the e-invoice generated for an invoice on the Invoice Registration Portal (IRP). |
| cancel invoice | Change the status of an invoice to cancelled. |
| cancel invoice einvoice | Cancel the e-invoice of an invoice on the Invoice Registration Portal (IRP). |
| cancel invoices einvoice | Cancel the e-invoices of multiple invoices on the Invoice Registration Portal (IRP). |
| cancel scheduled invoice email | Cancel a previously scheduled invoice email. |
| cancel write off invoice | Cancel the write off amount of an invoice. |
| cancel writeoff opening balance | Cancels a previously written-off opening balance. |
| categorize as credit note refunds | Categorize an Uncategorized transaction as a refund from a credit note. |
| categorize as vendor credit refunds | Categorize an uncategorized transaction as a refund from a vendor credit. |
| categorize as vendor payment refund | Categorizing bank transactions as Vendor Payment Refund. |
| categorize bank transaction | Categorize an uncategorized transaction by creating a new transaction. |
| categorize bank transaction as customer payment | Categorize an uncategorized transaction as Customer Payment. |
| categorize bank transaction as expense | Categorize an Uncategorized transaction as expense. |
| categorize bank transaction as payment refund | Categorizing bank transactions as Payment Refund. |
| categorize bank transaction as vendor payment | Categorize an uncategorized transaction as Vendor Payment. |
| check formula syntax | Validate the syntax of a formula field expression. |
| clone project | Cloning a project. |
| convert purchase order to bill | Create a bill for the selected purchase orders. Use this api to fetch the Bill payload by passing the purchaseorder_ids in the query parameters and then use the create bill api and pass the payload to create a bill <br> <a href=/books/api/v3/bills/#create-a-bill>Create bill API Endpoint</a>. |
| copy organization settings | Copy the specified settings to an organization. |
| create alert | Create a new email alert configuration for workflow automation. |
| create bank account | Create a bank account or a credit card account for your organization. |
| create bank account match filter | Create a match filter used to identify bank transactions for rules. |
| create bank account rule | Create a rule and apply it on deposit/withdrawal for bank accounts and on refund/charges for credit card accounts. |
| create bank reconciliation | Reconcile the transactions of a bank account for a statement period. |
| create bank transaction | Create a bank transaction based on the allowed transaction types. |
| create base currency adjustment | Creates a base currency adjustment for the given information. |
| create bill | Create a bill received from your vendor. |
| create blueprint | Create a new blueprint for a module. |
| create blueprint transition | Create a new transition for a blueprint. |
| create chart of account | Creates an account with the given account type. |
| create contact | Create a new contact with comprehensive business information. This operation allows you to create a customer or vendor by providing details such as contact name, company information, addresses, contact persons, payment terms, tax settings, and custom fields. The created contact can be used for generating invoices, bills, estimates, and other business transactions. The system automatically assigns a unique contact ID. |
| create contact person | Create a contact person for contact. |
| create credit note | Create a new credit note to record credits issued to customers for returned items, overpayments, or adjustments. Supports multi-currency transactions, custom line items, tax calculations, and workflows. |
| create credit note refund | Refund credit note amount. |
| create currency | Create a currency for transaction. |
| create custom action | Create a new custom action. |
| create custom button | Create a new custom button for a module. |
| create custom field | Create a new custom field for a specific entity. |
| create custom function | Create a new custom function for workflow automation. |
| create custom module | Create a new custom module configuration. Define the module name, fields, permissions, and other settings. |
| create custom module record | Create a new record in a custom module. |
| create custom notification | Create a custom notification for the selected feature. |
| create custom scheduler | Create a new custom scheduler to run custom functions at scheduled intervals. |
| create custom trigger | Create a new custom trigger that can be used to invoke workflows via API. |
| create custom view | Create a new custom view for a specific entity type. <br><strong>Note:</strong> Filter criteria fields must use the format <code>${entity.field_name}</code> (e.g., <code>${invoice.status}</code> for standard fields, <code>${invoice.cf_text_field}</code> for custom fields). Use <code>${PLACEHOLDER.EMPTY}</code> as the value to match empty/null fields. |
| create customer debit note | Create a customer debit note for additional charges or adjustments to be made to the original invoice. |
| create customer payment | Create a new payment. |
| create customer payment refund | Refund the excess amount paid by the customer. |
| create delivery challan | Create a new delivery challan for a customer. The customer ID is required. |
| create employee | Create an employee for an expense. |
| create estimate | Create an estimate for your customer. |
| create estimate comment | Add a comment for an estimate. |
| create exchange rate | Create an exchange rate for the specified currency. |
| create expense | Create billable or non-billable expense. |
| create field update | Create a new field update action for workflow automation. |
| create fixed asset | Create a fixed asset. |
| create fixed asset comment | Add a comment to the fixed asset. |
| create fixed asset type | Create a fixed asset type. |
| create invoice | Create an invoice for your customer. |
| create invoice asynchronous online payment | Collect an online payment for an invoice asynchronously through a payment gateway. |
| create invoice from salesorder | Create an instant invoice for all the confirmed sales orders you have selected. |
| create invoice synchronous online payment | Charge a card synchronously to collect an online payment for an invoice. |
| create invoices from estimates | Create one or more invoices from the selected estimates. |
| create invoices from projects | Create invoices from one or more projects. Use this to bill unbilled project time and expenses by generating invoices directly from the selected projects. |
| create item | Create a new item. |
| create journal | Create a journal. |
| create location | Create a location. |
| create new draft blueprint | Create a new draft version of an existing blueprint. |
| create opening balance | Creates opening balance with the given information. |
| create organization | Create an organization. |
| create organization address | Add an address for the organization. |
| create pricebook | create a new pricebook. |
| create project | Create a project. |
| create purchase order | Create a purchase order for your vendor. |
| create push notification | Create a new push notification action for workflow automation. |
| create recurring bill | Create a recurring bill. |
| create recurring expense | Create a recurring expense. |
| create recurring invoice | Creating a new recurring invoice. |
| create recurring journal | Creates a recurring journal. |
| create related list | Create a new related list for a module. |
| create retainer invoice | Create a retainer invoice for your customer. |
| create retainer invoice async online payment | Record an online payment for a retainer invoice and process it asynchronously. |
| create retry policy | Create a new retry policy for webhook or custom function actions. |
| create sales order | Create a sales order for your customer. |
| create sales receipt | Create a sales receipt for immediate payment transactions. |
| create tag | Create a reporting tag |
| create tax | Create a tax which can be associated with an item. Note: You have to enable Sales Tax in order to perform tax related operations. |
| create tax authority | Create a tax authority. Note: You have to enable Sales Tax in order to perform tax related operations. |
| create tax exemption | Create a tax exemption. Note: You have to enable Sales Tax in order to perform tax related operations. |
| create tax group | Create a tax group associating multiple taxes. Note: You have to enable Sales Tax in order to perform tax related operations. |
| create time entries | Logging time entries. |
| create user | Create a user for your organization. |
| create vendor credit | Create a new vendor credit to record credits issued by vendors for returned items, overpayments, or adjustments. Supports multi-currency transactions, custom line items, tax calculations, and workflows. |
| create vendor payment | Create a payment made to your vendor and you can also apply them to bills either partially or fully. |
| create web tab | Create a new web tab for the organization. |
| create webhook | Create a new webhook configuration for sending HTTP callbacks. |
| create workflow | Create a new workflow rule for automating actions based on triggers. |
| deactivate blueprint | Deactivate a blueprint to stop enforcing the defined workflow. |
| deactivate workflow | Mark an existing workflow as inactive. |
| decline contact bank account | Decline a bank account added for a contact. |
| delete alert | Delete an existing email alert configuration. |
| delete applied retainer payment | Delete a retainer invoice payment that was applied to an invoice. |
| delete bank account | Delete a bank account from your organization. |
| delete bank account match filter | Delete a match filter. |
| delete bank account rule | Delete a rule from your account and make it no longer applicable on the transactions. |
| delete bank reconciliation | Delete a bank reconciliation. |
| delete bank reconciliation document | Delete a document attached to a bank reconciliation. |
| delete bank transaction | Delete a transaction from an account by specifying the transaction_id. |
| delete base currency adjustment | Deletes the base currency adjustment. |
| delete bill | Delete an existing bill. Bills which have payments applied cannot be deleted. |
| delete bill comment | Delete a bill comment. |
| delete bill payment | Delete a payment made to a bill. |
| delete blueprint | Delete an existing blueprint. |
| delete blueprint transitions | Delete existing transitions from a blueprint. |
| delete chart of account | Deletes the given account. Accounts associated in any transaction/products could not be deleted. |
| delete chart of account transaction | Deletes the transaction. |
| delete contact | Delete an existing contact. |
| delete contact address | Delete the additional address of a contact. |
| delete contact bank account | Delete a bank account associated with a contact. |
| delete contact card | Delete a card associated with a contact. |
| delete contact comment | Delete a comment added to a contact. |
| delete contact document | Delete a document attached to a contact. |
| delete contact person | Delete an existing contact person. |
| delete contact tag | Remove a reporting tag from a contact. |
| delete contact tax info | Delete a tax information record of a contact. |
| delete contacts | Delete one or more contacts. |
| delete credit note | Delete an existing credit note. |
| delete credit note comment | Delete a credit note comment. |
| delete credit note document | Delete a document attached to a credit note. |
| delete credit note einvoice status | Delete the locally stored e-invoice status of a credit note. |
| delete credit note refund | Delete a credit note refund. |
| delete credit note substatus | Remove a custom sub-status applied to a credit note. |
| delete currency | Delete a currency. Currency that is associated to transactions cannot be deleted. |
| delete custom action | Delete an existing custom action. |
| delete custom button | Delete an existing custom button. |
| delete custom field | Delete an existing custom field. |
| delete custom function | Delete an existing custom function. |
| delete custom module | Delete an existing custom module configuration and all its records. |
| delete custom module record | Delete an individual record from a custom module. |
| delete custom module records | Delete records from a custom module. |
| delete custom notification | Delete an existing custom notification. |
| delete custom scheduler | Delete an existing custom scheduler. |
| delete custom trigger | Delete an existing custom trigger. |
| delete custom view | Delete an existing custom view. |
| delete customer debit note | Delete an existing customer debit note. Debit notes which have payment or credits note applied cannot be deleted. |
| delete customer payment | Delete an existing payment. |
| delete customer payment refund | Delete refund pertaining to an existing customer payment. |
| delete delivery challan | Delete an existing delivery challan. |
| delete delivery challan attachment | Delete an attachment. |
| delete employee | Delete an existing employee. |
| delete estimate | Delete an existing estimate. |
| delete estimate comment | Delete an estimate comment. |
| delete exchange rate | Delete an exchange rate for the specified currency. |
| delete expense | Delete an existing expense. |
| delete expense receipt | Delete the receipt attached to the expense. |
| delete field update | Delete an existing field update configuration. |
| delete fixed asset | Deletes the given fixed asset. |
| delete fixed asset comment | Delete the comment of the fixed asset. |
| delete fixed asset type | Deletes the given fixed asset type. |
| delete invoice | Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted. |
| delete invoice applied credit | Delete a particular credit applied to an invoice. |
| delete invoice comment | Delete an invoice comment. |
| delete invoice document | Delete a specific document attached to an invoice. This operation permanently removes the document from the invoice and cannot be undone. Only documents that are not system-generated can be deleted. |
| delete invoice einvoice status | Delete the locally stored e-invoice status of an invoice. |
| delete invoice expense receipt | Delete the expense receipts attached to an invoice which is raised from an expense. |
| delete invoice line item | Delete a specific line item from an invoice. |
| delete invoice of credit note | Delete the credits applied to an invoice. |
| delete invoice payment | Delete a payment made to an invoice. |
| delete invoice substatus | Remove a custom sub-status applied to an invoice. |
| delete invoices | Delete one or more invoices. Only invoices that are not part of a closed accounting period can be deleted. |
| delete item | Delete the item created.items that are part of transaction cannot be deleted. |
| delete journal | Deletes the given journal. |
| delete journal comment | Delete a jounral comment. |
| delete journal credits payables | Deletes applied journal credits from payables. |
| delete journal credits receivables | Deletes applied journal credits from receivables. |
| delete last imported bank statement | Delete the statement that was previously imported. |
| delete location | Delete a location. |
| delete opening balance | Delete the entered opening balance. |
| delete organization address | Delete an existing address of the organization. |
| delete pricebook | Delete the pricebook. |
| delete project | Deleting a existing project. |
| delete project comment | Deleting a comment. |
| delete project task | Delete a task added to a project. |
| delete project user | Remove user from a project. |
| delete purchase order | Delete an existing purchase order. |
| delete purchase order comment | Delete a purchase order comment. |
| delete push notification | Delete an existing push notification configuration. |
| delete recurring bill | Delete an existing recurring bill. |
| delete recurring expense | Deleting an existing recurring expense. |
| delete recurring invoice | Delete an existing recurring invoice. |
| delete recurring invoice bank account | Remove the bank account associated with a recurring invoice for auto-bill. |
| delete recurring invoice card | Remove the card associated with a recurring invoice for auto-bill. |
| delete recurring journal | Deletes a recurring journal. |
| delete related list | Delete an existing related list. |
| delete retainer invoice | Delete an existing retainer invoice. Invoices which have payment or credits note applied cannot be deleted. |
| delete retainer invoice attachment | Delete the file attached to the retainer invoice. |
| delete retainer invoice comment | Delete a retainer invoice comment. |
| delete retry policy | Delete an existing retry policy. |
| delete sales order | Delete an existing sales order. Invoiced sales order cannot be deleted. |
| delete sales order comment | Delete a sales order comment. |
| delete sales receipt | Delete an existing sales receipt. |
| delete tag | Delete a reporting tag. If there are any usages of the reporting tag in transactions, custom views or workflows, you will not be able to delete the tag. |
| delete task | Delete a tasks. |
| delete task comment | Delete a comment of a task. |
| delete task document | Delete a document of a task. |
| delete tasks | Delete tasks. |
| delete tax | Delete a simple or compound tax. Note: You have to enable Sales Tax in order to perform tax related operations. |
| delete tax authority | Delete a tax authority. Note: You have to enable Sales Tax in order to perform tax related operations. |
| delete tax exemption | Delete a tax exemption. Note: You have to enable Sales Tax in order to perform tax related operations. |
| delete tax group | Delete a tax group. Tax group that is associated to transactions cannot be deleted. Note: You have to enable Sales Tax in order to perform tax related operations. |
| delete time entries | Deleting time entries. |
| delete time entry | Deleting a logged time entry. |
| delete transaction lock | Delete a transaction lock entry. |
| delete user | Delete a user associated to the organization. |
| delete vendor credit | Delete a vendor credit. |
| delete vendor credit bill | Delete the credits applied to a bill. <code>Note: </code>You should pass the vendor_credit_bill_id from "Get vendor credits > bills credited > vendor_credit_bill_id" section |
| delete vendor credit comment | Delete a vendor credit comment. |
| delete vendor credit refund | Delete a vendor credit refund. |
| delete vendor payment | Delete an existing vendor payment. |
| delete vendor payment refund | Delete refund pertaining to an existing vendor payment. |
| delete web tab | Delete an existing web tab. |
| delete webhook | Delete an existing webhook configuration. |
| delete workflow | Delete an existing workflow rule. |
| deploy custom function | Deploy a cloud-based custom function (Node.js, Java, Python, or Go). |
| disable contact payment reminder | Disable automated payment reminders for a contact. |
| disable contact person sms | Disable SMS notifications for a contact person. |
| disable contact portal | Disable client portal access for a contact. |
| disable invoice payment reminder | Disable automated payment reminders for an invoice. |
| disable recurring invoice autobill | Disable auto-bill for a recurring invoice so that generated invoices are no longer charged automatically. |
| downgrade organization to invoice | Downgrade an organization from Zoho Books to Zoho Invoice. |
| download custom function | Download the code package (ZIP) for a cloud-based custom function. |
| email contact | Send email to contact. |
| email contact statement | Email statement to the contact. If JSONString is not inputted, mail will be sent with the default mail content. |
| email credit note | Email a credit note. |
| email estimate | Email an estimate to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content. |
| email invoice | Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content. |
| email invoices | Send invoices to your customers by email. Maximum of 10 invoices can be sent at once. |
| email multiple estimates | Send estimates to your customers by email. Maximum of 10 estimates can be sent at once. |
| email purchase order | Email a purchase order to the vendor. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content. |
| email retainer invoice | Email a retainer invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content. |
| email sales order | Email a sales order to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content. |
| email sales receipt | Email a sales receipt to the customer. |
| email vendor payment | Send a vendor payment receipt to the vendor via email. You can customize the email content, attach files, and control sender preferences. If the request body is empty, the email will be sent with default content based on the email template associated with the vendor or the default template. |
| enable contact payment reminder | Enable automated payment reminders for a contact. |
| enable contact person sms | Enable SMS notifications for a contact person. |
| enable contact portal | Enable portal access for a contact. |
| enable custom function integration | Enable a custom function integration type (DRE or Cloud). |
| enable invoice payment reminder | Enable automated payment reminders for an invoice. |
| enable locations | Enable Locations for an organisation. |
| enable recurring invoice autobill | Enable auto-bill for a recurring invoice so that generated invoices are charged automatically to the associated card or bank account. |
| exclude bank transaction | Exclude a transaction from your bank or credit card account. |
| exclude common transition from blueprint | Exclude an existing common transition from a blueprint. |
| execute custom function | Execute a custom function for a specific entity. |
| execute custom function manually | Manually re-execute a failed custom function from history. |
| execute custom trigger | Execute a custom trigger for a specific entity using OAuth or ZAPI key authentication. |
| fetch credit note einvoice | Fetch the latest e-invoice status of a credit note from the Invoice Registration Portal (IRP). |
| fetch invoice einvoice | Fetch the latest e-invoice status of an invoice from the Invoice Registration Portal (IRP). |
| finalize credit note approval | Give the final approval for a credit note in a multi-level approval flow. Use this when a credit note requires a final approval step after the initial approval. |
| finalize invoice approval | Give the final approval for an invoice in a multi-level approval flow. Use this when an invoice requires a final approval step after the initial approval. |
| force pay invoice | Charge a saved payment method to collect payment for an invoice immediately. |
| generate blueprint with platform ai | Generate a blueprint using Platform AI based on the provided requirements. |
| generate invoice payment link | This API generates a payment link for the invoice with an expiry date. |
| get account transactions report | Account Transactions for the selected filters and period. entity_type is account_transactions for this report. Call GET /reports/metadata with that entity_type before this report. |
| get account type summary report | Account Type Summary for the selected filters and period. entity_type is account_type_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get account type transactions report | Account Type Transactions for the selected filters and period. entity_type is account_type_transactions for this report. Call GET /reports/metadata with that entity_type before this report. |
| get accounting period transaction lock | Get transaction locking details for an accounting period. |
| get activity logs report | Activity Logs for the selected filters and period. entity_type is activity_logs for this report. Call GET /reports/metadata with that entity_type before this report. |
| get advance search fields | Get the available fields and operators for advanced search/filter criteria for a specific entity type. |
| get alert | Get the details of a specific email alert configuration. |
| get alert editpage | Get the data needed to render the alert edit page, including entities, templates, recipients, and attachments. |
| get alert history | Get the details of a specific email alert execution history entry. |
| get all tag options | Get the options and its criteria details of a reporting tag. For each page, you can retrieve only 200 options. |
| get ap aging details report | Accounts payable aging details report. entity_type is ap_aging_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get ap aging summary report | Accounts payable aging summary report. entity_type is ap_aging_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get ar aging details report | Accounts receivable aging detail report. entity_type is ar_aging_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get ar aging summary report | Accounts receivable aging summary. entity_type is ar_aging_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get balance sheet report | Balance sheet report for the selected period. entity_type is balance_sheet for this report. Call GET /reports/metadata with that entity_type before this report. |
| get bank account | Get a detailed look of the account specified. |
| get bank account balance | Retrieve the balance of a bank account. |
| get bank account balances | Retrieve the balance breakdown of a bank account. |
| get bank account insights | Retrieve cash-flow insights for a bank account. |
| get bank account overview | Retrieve an overview of a bank account. |
| get bank account preferences | Retrieve the preferences of a bank account. |
| get bank account rule | Get details of a specific rule. |
| get bank account statement summary | Retrieve the statement summary of a bank account. |
| get bank accounts overview | Retrieve an overview of all bank accounts. |
| get bank charges report | Bank charges report for receivables. entity_type is bank_charges for this report. Call GET /reports/metadata with that entity_type before this report. |
| get bank reconciliation | Retrieve the details of a bank reconciliation. |
| get bank reconciliation document | Retrieve a document attached to a bank reconciliation. |
| get bank statement import encryption key | Retrieve the public key used to encrypt bank statement files before import. |
| get bank transaction | Fetch the details of a transaction by specifying the transaction_id. |
| get base currency adjustment | Get the base currency adjustment details. |
| get bill | Get the details of a bill. |
| get bill comments | Get the complete history and comments of a bill. |
| get bill details report | Bill details report for payables. entity_type is bill_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get billable expense details report | Billable Expense Details for the selected filters and period. entity_type is billable_expense_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get blueprint | Get the details of a specific blueprint. |
| get blueprint edit page details | Get the details required for rendering the blueprint edit page. |
| get blueprint reports | Get reports related to blueprints. |
| get blueprint transitions for record | Get the available blueprint transitions for a specific record. |
| get budget vs actuals report | Budget Vs Actuals for the selected filters and period. entity_type is budget_vs_actuals for this report. Call GET /reports/metadata with that entity_type before this report. |
| get card expiry report | Card Expiry for the selected filters and period. entity_type is card_expiry for this report. Call GET /reports/metadata with that entity_type before this report. |
| get cash book summary report | Cash book summary report for the selected period. entity_type is cash_book_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get cash flow forecast report | Cash flow forecast report for the selected period. entity_type is cash_flow_forecast for this report. Call GET /reports/metadata with that entity_type before this report. |
| get cash flow report | Cash flow report for the selected period. entity_type is cash_flow for this report. Call GET /reports/metadata with that entity_type before this report. |
| get chart of account | Gets the details of an account. |
| get contact | Retrieve comprehensive details of a specific contact. This operation provides complete contact details such as basic information, addresses, contact persons, payment terms, tax settings, custom fields, and financial data including outstanding amounts, credit limits, and transaction history. |
| get contact address | Get addresses of a contact including its Shipping Address, Billing Address and other additional addresses. |
| get contact bank account | Retrieve the details of a bank account associated with a contact. |
| get contact by reference | Retrieve a contact using its reference ID from an external system. |
| get contact card | Retrieve the details of a card associated with a contact. |
| get contact card count | Retrieve the number of saved cards across contacts in the organization. |
| get contact client review email | Retrieve the email content for a contact client review. |
| get contact contact person | Retrieve a specific contact person of a contact. |
| get contact document | Retrieve a document attached to a contact. |
| get contact email content | Retrieve the default email content used when emailing a contact. |
| get contact income and expense | Retrieve the income and expense summary of a contact. |
| get contact inventory summary | Retrieve the inventory summary for a contact. |
| get contact opening balances | Retrieve the opening balances of a contact. |
| get contact payment method email | Retrieve the email content requesting a payment method from a contact. |
| get contact person | Get the contact person details. |
| get contact profit and loss | Retrieve the profit and loss summary of a contact. |
| get contact sms content | Retrieve the SMS content used when notifying a contact. |
| get contact statement | Retrieve the account statement of a contact. |
| get contact statement mail | Get the statement mail content. |
| get contact unused credits | Retrieve the unused customer credits available for a contact. |
| get contact vendor statement email | Retrieve the email content for a vendor statement. |
| get contacts sms content | Retrieve the SMS content used when notifying multiple contacts. |
| get credit note | Details of an existing creditnote. |
| get credit note custom fields | Retrieve the custom fields configured for a credit note. |
| get credit note einvoice | Retrieve the e-invoice JSON data generated for a credit note. |
| get credit note email | Get email content of a credit note. |
| get credit note email history | Get email history of a credit code. |
| get credit note mail content | Retrieve the default email content (subject and body) used when emailing a credit note. |
| get credit note refund | Get refund of a particular credit note. |
| get credit note refund by id | Retrieve the details of a specific credit note refund using its refund ID. |
| get credit note signature template | Retrieve the digital signature template details associated with a credit note. |
| get credit notes details report | Credit Notes Details for the selected filters and period. entity_type is credit_notes_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get currency | Get the details of a currency. |
| get current user | Get the details of the current user. |
| get custom action | Get the details of a specific custom action. |
| get custom button | Get the details of a specific custom button. |
| get custom button history | Get the details of a specific custom button execution history entry. |
| get custom function | Get the details of a specific custom function. |
| get custom function editpage | Get the data needed to render the custom function edit page, including entities, languages, parameters, and sample scripts. |
| get custom function history | Get the details of a specific custom function execution history entry. |
| get custom module | Get the configuration details of a specific custom module. |
| get custom module record | Get the details of an individual record in a custom module. |
| get custom notification editpage | Get the data needed to edit a custom notification. |
| get custom notification preference | Get the execution limit notification preferences. |
| get custom scheduler | Get the details of a specific custom scheduler. |
| get custom trigger editpage | Get the data needed to render the custom trigger edit page. |
| get custom trigger url | Get the ZAPI key URL for a custom trigger. |
| get custom view | Get the details of a specific custom view. |
| get customer balance details report | Per-customer balance detail report. entity_type is customer_balance_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get customer balance summary details report | Extended customer balance summary details. entity_type is customer_balance_summary_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get customer balance summary report | Customer balance summary report. entity_type is customer_balance_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get customer balances report | Customer balance listing for receivables. entity_type is customer_balances for this report. Call GET /reports/metadata with that entity_type before this report. |
| get customer debit note | Get the details of a customer debit note. |
| get customer payment | Details of an existing payment. |
| get customer payment refund | Obtain details of a particular refund of a customer payment. |
| get customer payments report | Customer Payments for the selected filters and period. entity_type is customer_payments for this report. Call GET /reports/metadata with that entity_type before this report. |
| get day book report | Day Book for the selected filters and period. entity_type is day_book for this report. Call GET /reports/metadata with that entity_type before this report. |
| get delivery challan | Retrieve the details of an existing delivery challan. |
| get deliverychallan details report | Delivery challan details for receivables. entity_type is deliverychallan_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get donations by donor report | Donations By Donor for the selected filters and period. entity_type is donations_by_donor for this report. Call GET /reports/metadata with that entity_type before this report. |
| get donations by fund report | Donations By Fund for the selected filters and period. entity_type is donations_by_fund for this report. Call GET /reports/metadata with that entity_type before this report. |
| get dunning child invoices report | Dunning Child Invoices for the selected filters and period. entity_type is dunning_child_invoices for this report. Call GET /reports/metadata with that entity_type before this report. |
| get ec sales list report | Ec Sales List for the selected filters and period. entity_type is ec_sales_list for this report. Call GET /reports/metadata with that entity_type before this report. |
| get elimination journal report | Elimination Journal Report for the selected filters and period. entity_type is elimination_journal_report for this report. Call GET /reports/metadata with that entity_type before this report. |
| get employee | Get the details of the employee. |
| get entity fields meta | Fetch the complete fields metadata for an entity, including system and custom fields. |
| get estimate | Get the details of an estimate. |
| get estimate details report | Customer estimate details report. entity_type is estimate_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get estimate email | Get the email content of an estimate. |
| get exception report | Exception Report for the selected filters and period. entity_type is exception_report for this report. Call GET /reports/metadata with that entity_type before this report. |
| get exchange rate | Get the details of an exchange rate that has been asscoiated to the currency. |
| get expense | Get the details of the Expense. |
| get expense details report | Expense Details for the selected filters and period. entity_type is expense_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get expenses by category report | Expenses By Category for the selected filters and period. entity_type is expenses_by_category for this report. Call GET /reports/metadata with that entity_type before this report. |
| get expenses by customer report | Expenses By Customer for the selected filters and period. entity_type is expenses_by_customer for this report. Call GET /reports/metadata with that entity_type before this report. |
| get expenses by employee report | Expenses By Employee for the selected filters and period. entity_type is expenses_by_employee for this report. Call GET /reports/metadata with that entity_type before this report. |
| get expenses by project report | Expenses By Project for the selected filters and period. entity_type is expenses_by_project for this report. Call GET /reports/metadata with that entity_type before this report. |
| get failed child invoices report | Failed Child Invoices for the selected filters and period. entity_type is failed_child_invoices for this report. Call GET /reports/metadata with that entity_type before this report. |
| get field update | Get the details of a specific field update configuration. |
| get field update editpage | Get the data needed to render the field update edit page, including entities, fields, and available field values. |
| get field usage | Get the usage details of a custom field in custom reports and other configurations. |
| get fields meta | Get field metadata for a specific entity type, including all available field types and configurations. |
| get fixed asset | Get the details of the fixed asset. |
| get fixed asset forecast | It displays a detailed summary of the asset's future depreciation rates. |
| get fixed asset history | It displays a detailed summary of the asset from acquisition till write off. |
| get fixed asset register report | Fixed Asset Register for the selected filters and period. entity_type is fixed_asset_register for this report. Call GET /reports/metadata with that entity_type before this report. |
| get fixed asset type list | fixed asset type list. |
| get general ledger details report | General Ledger Details for the selected filters and period. entity_type is general_ledger_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get general ledger report | General Ledger for the selected filters and period. entity_type is general_ledger for this report. Call GET /reports/metadata with that entity_type before this report. |
| get horizontal balance sheet report | Horizontal balance sheet report for the selected period. entity_type is horizontal_balance_sheet for this report. Call GET /reports/metadata with that entity_type before this report. |
| get horizontal profit and loss report | Horizontal layout profit and loss report. entity_type is horizontal_profit_and_loss for this report. Call GET /reports/metadata with that entity_type before this report. |
| get im credits usage report | Im Credits Usage for the selected filters and period. entity_type is im_credits_usage for this report. Call GET /reports/metadata with that entity_type before this report. |
| get in process payments report | Payments in process for receivables. entity_type is in_process_payments for this report. Call GET /reports/metadata with that entity_type before this report. |
| get inventory queue report | Inventory Queue for the selected filters and period. entity_type is inventory_queue for this report. Call GET /reports/metadata with that entity_type before this report. |
| get invoice | Get the details of an invoice. |
| get invoice advanced tracking details | Retrieve the advanced inventory tracking details (batches or serial numbers) of the line items in an invoice. |
| get invoice by reference | Retrieve an invoice using its reference ID from an external system. |
| get invoice custom fields | Retrieve the custom fields configured for an invoice. |
| get invoice dashboard | Retrieve the invoice dashboard with summary metrics for invoices. |
| get invoice delivery notes | Retrieve the delivery notes for one or more invoices. Use this to generate or print delivery notes for the specified invoices. |
| get invoice details report | Detailed invoice lines for receivables. entity_type is invoice_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get invoice einvoice | Retrieve the e-invoice JSON data generated for an invoice. |
| get invoice email | Get the email content of an invoice. |
| get invoice metadata | Retrieve a metadata value stored against an invoice. |
| get invoice packing slips | Retrieve the packing slips for one or more invoices. Use this to generate or print packing slips for the specified invoices. |
| get invoice payment qr | Retrieve the QR code that the customer can scan to pay an invoice online. |
| get invoice payment qr status | Retrieve the payment status of an invoice online payment QR code. |
| get invoice qr code | Retrieve the QR code generated for an invoice. |
| get invoice refunds details report | Customer invoice refunds detail report. entity_type is invoice_refunds_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get invoice signature template | Retrieve the digital signature template configured for an invoice. |
| get invoice sms | Retrieve the default SMS content used when sending an invoice notification by SMS. |
| get item | Details of an existing item. |
| get journal | Get the details of the journal. |
| get journal report | Journal Report for the selected filters and period. entity_type is journal_report for this report. Call GET /reports/metadata with that entity_type before this report. |
| get last imported bank statement | Get the details of previously imported statement for the account. |
| get matching bank transactions | Provide criteria to search for matching uncategorised transactions. The list of transactions can also include invoices/bills/credit-notes which will not be matched directly. Instead, a new (payment/refund) transaction is recorded and matched. |
| get mileage details report | Mileage Details for the selected filters and period. entity_type is mileage_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get mileage summary report | Mileage Summary for the selected filters and period. entity_type is mileage_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get module filters | Get the list of module filters available for workflow configuration. |
| get movement of equity report | Movement of equity report for the selected period. entity_type is movement_of_equity for this report. Call GET /reports/metadata with that entity_type before this report. |
| get network entity report | Network Entity for the selected filters and period. entity_type is network_entity for this report. Call GET /reports/metadata with that entity_type before this report. |
| get opening balance | Get opening balance. |
| get organization | Get the details of an organization. |
| get organization address | Retrieve the address of the organization. |
| get payable details report | Payable details report for vendors and bills. entity_type is payable_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get payable summary report | Payable summary report for accounts payable. entity_type is payable_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get payment reminder mail content for invoice | Get the mail content of the payment reminder. |
| get pb sms credits usage report | Pb Sms Credits Usage for the selected filters and period. entity_type is pb_sms_credits_usage for this report. Call GET /reports/metadata with that entity_type before this report. |
| get portal activities report | Portal Activities for the selected filters and period. entity_type is portal_activities for this report. Call GET /reports/metadata with that entity_type before this report. |
| get profit and loss report | Profit and loss report for the selected period. entity_type is profit_and_loss for this report. Call GET /reports/metadata with that entity_type before this report. |
| get progress invoice summary report | Progress billing invoice summary. entity_type is progress_invoice_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project | Get the details of a project. |
| get project cost summary report | Project Cost Summary for the selected filters and period. entity_type is project_cost_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project details report | Project Details for the selected filters and period. entity_type is project_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project performance summary report | Project Performance Summary for the selected filters and period. entity_type is project_performance_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project profitability summary report | Project Profitability Summary for the selected filters and period. entity_type is project_profitability_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project revenue details report | Project Revenue Details for the selected filters and period. entity_type is project_revenue_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project revenue summary report | Project Revenue Summary for the selected filters and period. entity_type is project_revenue_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project summary report | Project Summary for the selected filters and period. entity_type is project_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get project task | Get the details of a project task. |
| get project user | Get details of a user in project. |
| get purchase order | Get the details of a purchase order. |
| get purchase order email | Get the email content of a purchase order. |
| get purchase receive item report | Purchase Receive Item for the selected filters and period. entity_type is purchase_receive_item for this report. Call GET /reports/metadata with that entity_type before this report. |
| get purchaseorder details report | Purchase order details report for payables. entity_type is purchaseorder_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get purchaseorders by vendors report | Purchase orders grouped or listed by vendor. entity_type is purchaseorders_by_vendors for this report. Call GET /reports/metadata with that entity_type before this report. |
| get purchases by category report | Purchases By Category for the selected filters and period. entity_type is purchases_by_category for this report. Call GET /reports/metadata with that entity_type before this report. |
| get purchases by item report | Purchases By Item for the selected filters and period. entity_type is purchases_by_item for this report. Call GET /reports/metadata with that entity_type before this report. |
| get purchases by vendor report | Purchases By Vendor for the selected filters and period. entity_type is purchases_by_vendor for this report. Call GET /reports/metadata with that entity_type before this report. |
| get push notification | Get the details of a specific push notification configuration. |
| get push notification editpage | Get the data needed to render the push notification edit page, including entities, recipients, and placeholders. |
| get rating by customer report | Rating By Customer for the selected filters and period. entity_type is rating_by_customer for this report. Call GET /reports/metadata with that entity_type before this report. |
| get ratio analysis report | Financial ratio analysis report for the selected period. entity_type is ratio_analysis for this report. Call GET /reports/metadata with that entity_type before this report. |
| get realized gain or loss report | Realized Gain Or Loss for the selected filters and period. entity_type is realized_gain_or_loss for this report. Call GET /reports/metadata with that entity_type before this report. |
| get receivable details report | Receivable transaction detail report. entity_type is receivable_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get receivable summary report | Receivable summary report. entity_type is receivable_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get recurring bill | Get the details of a recurring bill. |
| get recurring expense | Get the details of the recurring expense. |
| get recurring invoice | Get the details of a recurring invoice. |
| get recurring invoice dashboard | Retrieve the dashboard summary for recurring invoices, including aggregated metrics for the recurring invoice profiles. |
| get recurring invoice details report | Recurring Invoice Details for the selected filters and period. entity_type is recurring_invoice_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get recurring journal | Gets the details of a recurring journal. |
| get refund history report | Refund History for the selected filters and period. entity_type is refund_history for this report. Call GET /reports/metadata with that entity_type before this report. |
| get register budget vs actuals | Retrieve budget versus actuals for an account register. When <code>budget_id</code> is provided, returns detailed period breakdown. |
| get register bulk action history | Retrieve details of a single bulk action on the account register, including affected transactions. |
| get register bulk update editpage | Returns metadata for fields supported when bulk updating transactions on an account register. |
| get related list | Get the details of a specific related list. |
| get report 1099 vendor payments report | Report 1099 Vendor Payments for the selected filters and period. entity_type is report_1099_vendor_payments for this report. Call GET /reports/metadata with that entity_type before this report. |
| get reports metadata | Returns metadata for a report: <code>entity_fields</code> for tabular params (<code>select_columns</code>, <code>group_by</code>, <code>rule</code>, <code>sort_column</code>, <code>date_filter</code>) and <code>report_details</code> for chart view, defaults, and export options. Use <code>entity_fields</code> flags per parameter; for <code>chart_view</code> true, use <code>report_details.chart_type[]</code> for <code>chart_type</code>, <code>x_axis</code>, and <code>y_axis</code> (not <code>entity_fields</code>). Example (<code>profit_and_loss</code>): <code>chart_type</code> lists <code>line_chart</code> and <code>bar_chart</code> with <code>x_axis[]</code> and <code>y_axis[]</code> field and group pairs. Do not send <code>rule</code> when <code>search_allowed</code> is false for that field. |
| get reports schedule history | Returns action history for a scheduled report. Report constant <code>reports_schedule_history</code>. Requires <code>schedule_id</code>. Each row includes <code>action_type</code>: <code>created</code>, <code>updated</code>, <code>inactivated</code>, <code>activated</code>, or <code>mail_sent</code>. |
| get retainer invoice | Get the details of a retainer invoice. |
| get retainer invoice email | Get the email content of a retainer invoice. |
| get retainerinvoice details report | Retainer invoice line details. entity_type is retainerinvoice_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get retry policy | Get the details of a specific retry policy. |
| get running timer | Get current running timer. |
| get sales by category report | Sales By Category for the selected filters and period. entity_type is sales_by_category for this report. Call GET /reports/metadata with that entity_type before this report. |
| get sales by customer report | Sales By Customer for the selected filters and period. entity_type is sales_by_customer for this report. Call GET /reports/metadata with that entity_type before this report. |
| get sales by item report | Sales By Item for the selected filters and period. entity_type is sales_by_item for this report. Call GET /reports/metadata with that entity_type before this report. |
| get sales by salesperson report | Sales By Salesperson for the selected filters and period. entity_type is sales_by_salesperson. Call GET /reports/metadata before this report. This operation does not list rule; metadata has no search_allowed fields. Example: filter Hari by running the report for the date range and returning the matching row from sales[], not by sending rule with salesperson_name. |
| get sales order | Get the details of a sales order. |
| get sales order email | Get the email content of a sales order. |
| get sales receipt | Get the details of a sales receipt. |
| get sales summary report | Sales Summary for the selected filters and period. entity_type is sales_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get saleschannel ecommerce summary report | Saleschannel Ecommerce Summary for the selected filters and period. entity_type is saleschannel_ecommerce_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get salesorder details report | Sales order details for receivables. entity_type is salesorder_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get schedule balance sheet report | Schedule view of the balance sheet report. entity_type is schedule_balance_sheet for this report. Call GET /reports/metadata with that entity_type before this report. |
| get schedule profit and loss report | Schedule view of the profit and loss report. entity_type is schedule_profit_and_loss for this report. Call GET /reports/metadata with that entity_type before this report. |
| get sms history report | Sms History for the selected filters and period. entity_type is sms_history for this report. Call GET /reports/metadata with that entity_type before this report. |
| get snail mail report | Snail Mail for the selected filters and period. entity_type is snail_mail for this report. Call GET /reports/metadata with that entity_type before this report. |
| get system mails report | System Mails for the selected filters and period. entity_type is system_mails for this report. Call GET /reports/metadata with that entity_type before this report. |
| get tags | Get a list of all reporting tags in the preferred order that you can set. |
| get task | Get a task. |
| get tax | Get the details of a simple or compound tax. Note: You have to enable Sales Tax in order to perform tax related operations. |
| get tax authority | Get the details of a tax authority. Note: You have to enable Sales Tax in order to perform tax related operations. |
| get tax exemption | Get the details of a tax exemption. Note: You have to enable Sales Tax in order to perform tax related operations. |
| get tax group | Get the details of a tax group. Note: You have to enable Sales Tax in order to perform tax related operations. |
| get time entry | Get details of a time entry. |
| get time to pay report | Time To Pay for the selected filters and period. entity_type is time_to_pay for this report. Call GET /reports/metadata with that entity_type before this report. |
| get timesheet details report | Timesheet Details for the selected filters and period. entity_type is timesheet_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get timesheet profitability details report | Timesheet Profitability Details for the selected filters and period. entity_type is timesheet_profitability_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get timesheet profitability summary report | Timesheet Profitability Summary for the selected filters and period. entity_type is timesheet_profitability_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get transaction journal view | Gets the journal view of a transaction. |
| get transaction lock | Get the details of financial transaction locking. |
| get trial balance report | Trial Balance for the selected filters and period. entity_type is trial_balance for this report. Call GET /reports/metadata with that entity_type before this report. |
| get unrealized gain or loss report | Unrealized Gain Or Loss for the selected filters and period. entity_type is unrealized_gain_or_loss for this report. Call GET /reports/metadata with that entity_type before this report. |
| get unused retainer payments | Retrieve information about unused retainer payments for a specific contact. This endpoint returns details of retainer payments that have been made but not yet applied to invoices, providing insight into available credit balances from retainer payments. |
| get upcoming actions report | Upcoming Actions for the selected filters and period. entity_type is upcoming_actions for this report. Call GET /reports/metadata with that entity_type before this report. |
| get upcoming workflows report | Upcoming Workflows for the selected filters and period. entity_type is upcoming_workflows for this report. Call GET /reports/metadata with that entity_type before this report. |
| get user | Get the details of a user. |
| get vendor balance summary report | Vendor balance summary report for accounts payable. entity_type is vendor_balance_summary for this report. Call GET /reports/metadata with that entity_type before this report. |
| get vendor credit | Get details of a vendor credit. |
| get vendor credit details report | Vendor credit details report. entity_type is vendor_credit_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get vendor credit refund | Get refund of a particular vendor credit. |
| get vendor payment | Get the details of a vendor payment. |
| get vendor payment email content | Retrieve the pre-populated email content for a vendor payment, including subject, body, recipient contacts, sender options, and attachment details. This endpoint provides all the necessary information to compose and send a vendor payment receipt email. |
| get vendor payment refund | Obtain details of a particular refund of a vendor payment. |
| get vendor payments report | Vendor payments report for accounts payable. entity_type is vendor_payments for this report. Call GET /reports/metadata with that entity_type before this report. |
| get vendor refund history report | Vendor refund history report. entity_type is vendor_refund_history for this report. Call GET /reports/metadata with that entity_type before this report. |
| get web tab | Get the details of a specific web tab. |
| get webhook | Get the details of a specific webhook configuration. |
| get webhook editpage | Get the data needed to render the webhook edit page, including entities, fields, and connection link names. |
| get webhook history | Get the details of a specific webhook execution history entry. |
| get whatsapp history report | Whatsapp History for the selected filters and period. entity_type is whatsapp_history for this report. Call GET /reports/metadata with that entity_type before this report. |
| get workflow | Get the details of a specific workflow rule. |
| get workflow editpage | Get the data needed to render the workflow edit page, including entities, fields, actions, and related configurations. |
| get workflow log details | Get the detailed execution log of a specific workflow run. |
| get workflow logs report | Workflow Logs for the selected filters and period. entity_type is workflow_logs for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom product purchases report | Zom Product Purchases for the selected filters and period. entity_type is zom_product_purchases for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom product sales report | Zom Product Sales for the selected filters and period. entity_type is zom_product_sales for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom purchase receive report | Zom Purchase Receive for the selected filters and period. entity_type is zom_purchase_receive for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom saleseturns report | Zom Saleseturns for the selected filters and period. entity_type is zom_saleseturns for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom sofulfillmentbyitem details report | Zom Sofulfillmentbyitem Details for the selected filters and period. entity_type is zom_sofulfillmentbyitem_details for this report. Call GET /reports/metadata with that entity_type before this report. |
| get zom sofulfillmentbyitem report | Zom Sofulfillmentbyitem for the selected filters and period. entity_type is zom_sofulfillmentbyitem for this report. Call GET /reports/metadata with that entity_type before this report. |
| import bank statements | Import your bank/credit card feeds into your account. |
| import customer using crm account id | Zoho Books must be integrated with Zoho CRM using Accounts and Contacts sync or using Accounts only sync to import a customer from CRM with its CRM account ID. <br> Note: You can get a contact by CRM account ID by using this <a href=/books/api/v3/contacts/#list-contacts/zcrm_account_id>API Endpoint</a> |
| import customer using crm contact id | Zoho Books must be integrated with Zoho CRM using <code>Contacts only sync</code> or <code>Accounts & their Contacts and Include contacts that are not associated to any accounts </code> sync type contacts that are not associated to any accounts in Zoho CRM to import a customer from CRM with its CRM contact ID. <br> Note: You can get a contact by CRM contact ID by using this <a href=/books/api/v3/contacts/#list-contacts/zcrm_contact_id>API Endpoint</a> |
| import item using crm product id | Zoho Books must be integrated with Zoho CRM using Products only sync to import an item from CRM with its CRM product ID. |
| import vendor using crm vendor id | Zoho Books must be integrated with Zoho CRM using Vendor only sync to import a vendor from CRM with its CRM vendor ID. |
| inactive tag | Mark a reporting tag as inactive. |
| inactive tag option | Mark a reporting tag's option as inactive. |
| include common transition in blueprint | Include an existing common transition in a blueprint. |
| invite contact person to portal | Send a client portal invitation to a contact person. |
| invite project user | Invite and user to the project. |
| invite user | Send invitation email to a user. |
| list alert histories | Get a list of email alert execution history records. |
| list alerts | Get a list of all email alert configurations in your organization. |
| list all contact bank accounts | List bank accounts across all contacts in the organization. |
| list all contact persons | List contact persons across all contacts in the organization. |
| list bank account balances | Retrieve the balances of all bank accounts. |
| list bank account match filters | List the match filters used to identify bank transactions for rules. |
| list bank account rules | Fetch all the rules created in the organization. |
| list bank account statements | List the imported statements of a bank account. |
| list bank account subaccounts | List the sub-accounts of a bank account. |
| list bank account transactions | List the transactions of a bank account. |
| list bank accounts | List all bank and credit card accounts for your organization. |
| list bank reconciliations | List the reconciliations of a bank account. |
| list bank transactions | Get all the transaction details involved in an account. |
| list base currency adjustment accounts | List of accounts having transaction with effect to the given exchange rate. |
| list base currency adjustment contacts | List contacts having transactions with effect to the given exchange rate for a specific account. |
| list base currency adjustments | Lists base currency adjustment. |
| list bill payments | Get the list of payments made for a bill. |
| list bills | List all bills with pagination. |
| list bills credited | List bills to which the vendor credit is applied. |
| list blueprints | List all the blueprints configured for the organization. |
| list chart of account transactions | List all involved transactions for the given account. |
| list chart of accounts | List all chart of accounts along with pagination. |
| list child expenses of recurring expense | List child expenses created from recurring expense. |
| list child journals | Lists all child journals created from a recurring journal. |
| list contact addresses | List addresses across contacts in the organization. |
| list contact autobill recurring invoices | Retrieve the recurring invoices set to be auto-billed against a specific card of a contact. Use this to review which recurring invoices are linked to a contact card for automatic payment. |
| list contact bank accounts | List all bank accounts associated with a contact. |
| list contact cards | List all cards associated with a contact. |
| list contact comments | List recent activities of a contact. |
| list contact credit note refunds | List the credit note refunds issued to a contact. |
| list contact payment refunds | List the payment refunds issued to a contact. |
| list contact persons | List all contacts with pagination. |
| list contact tax info | List the tax information records of a contact. |
| list contact unpaid invoices | List the unpaid invoices of a contact. |
| list contacts | Retrieve a comprehensive list of all contacts with advanced filters. This operation supports multiple search criteria including contact name, company name, address, email, phone, and general text search. You can filter contacts by status (active, inactive, duplicate, CRM) and sort by various fields. The response includes essential contact information, financial data including outstanding amounts and credit limits, and pagination details for efficient data retrieval. |
| list created views | List all the custom views created by the current user. |
| list credit note comments | Get history and comments of a credit note. |
| list credit note refunds of a credit note | List all refunds of an existing credit note. |
| list credit note refunds of all credit notes | List all refunds with pagination. |
| list credit note templates | Get all credit note pdf templates. |
| list credit notes | Retrieve a paginated list of credit notes with comprehensive filtering, sorting, and search capabilities. Use query parameters to filter by date, status, amount, customer details, items, taxes, and custom fields. |
| list credit notes einvoice | Retrieve the e-invoice details of credit notes. |
| list currencies | Get list of currencies configured. |
| list custom actions | List all the custom actions configured for the organization. |
| list custom buttons | List all the custom buttons configured for the organization. |
| list custom buttons meta | Get the meta information of custom buttons available for a specific entity and page view. This is used to render buttons on entity detail or list pages. |
| list custom fields | List all custom fields configured for a specific entity. |
| list custom fields simple | List all custom fields for a specific entity type in a simplified format. |
| list custom function histories | Get a list of custom function execution history records. |
| list custom functions | Get a list of all custom functions configured in your organization. |
| list custom module records | Get the list of records of a custom module. |
| list custom modules | List all custom module configurations in the organization. This returns the module definitions including field configurations, permissions, and portal settings. |
| list custom scheduler histories | List the execution histories of custom schedulers. |
| list custom schedulers | List all the custom schedulers configured for the organization. |
| list custom triggers | Get a list of all custom triggers configured in your organization. |
| list custom views | List all the custom views configured for the organization. You can filter by entity type. |
| list customer debit notes | Get a list of customer debit notes with helpful pagination, filtering, search, and sorting features. Perfect for viewing your debit note data in organized ways, whether you need to find specific debit notes or browse through your records. |
| list customer payment refunds | List all the refunds pertaining to an existing customer payment. |
| list customer payments | List all the payments made by your customer. |
| list customers | Retrieve only customers with filters and pagination. |
| list delivery challan templates | Retrieve a list of available templates for delivery challans. |
| list delivery challans | Retrieve a list of delivery challans with pagination. Filter by status, customer, date, and more. |
| list employees | List employees with pagination. |
| list estimate comments | Get the complete history and comments of an estimate. |
| list estimate templates | Get all estimate pdf templates. |
| list estimates | List all estimates with pagination. |
| list exchange rates | List of exchange rates configured for the currency. |
| list expense comments | Get history and comments of expense. |
| list expenses | List all the Expenses with pagination. |
| list field updates | Get a list of all field update configurations in your organization. |
| list fixed assets | fixed asset list. |
| list invoice comments | Get the complete history and comments of an invoice. |
| list invoice credits applied | Get the list of credits applied for an invoice. |
| list invoice payments | Get the list of payments made for an invoice. |
| list invoice templates | Get all invoice pdf templates. |
| list invoices | Get a list of invoices with helpful pagination, filtering, search, and sorting features. Perfect for viewing your invoice data in organized ways, whether you need to find specific invoices or browse through your records. |
| list invoices einvoice | Retrieve the e-invoice details of invoices. |
| list invoices of credit note | List invoices to which the credit note is applied. |
| list item details | Fetch item details for the mentioned item IDs |
| list items | Get the list of all active items with pagination. |
| list journal credits | Lists available credits of a journal. |
| list journals | Get journal list. |
| list locations | List all the available locations in your zoho inventory. |
| list lookup fields | List available lookup fields for a specific entity. |
| list opening balance details | Lists the opening balance details for a specific account. |
| list opening balance transactions | Lists the opening balance transactions for a specific account. |
| list organizations | Get the list of organizations. |
| list organizations for user | Retrieve the list of organizations accessible to a user. Use the query parameters to filter the organizations returned. |
| list pricebook items | Retrieve the items in a price list along with their pricing. Use the filter parameters to narrow the items returned. |
| list pricebooks | List all the available pricebooks in your zoho books organization. |
| list project comments | Get comments for a project. |
| list project invoices | Lists invoices created for this project. |
| list project tasks | Get list of tasks added to a project. |
| list project users | Get list of users associated with a project. |
| list projects | List all projects with pagination. |
| list purchase order comments | Get the complete history and comments of purchase order. |
| list purchase order templates | Get all purchase order pdf templates. |
| list purchase orders | List all purchase orders. |
| list push notifications | Get a list of all push notification configurations in your organization. |
| list recurring bill history | Get history and comments of a recurring bill. |
| list recurring bills | List all recurring bills with pagination. |
| list recurring expense history | Get history and comments of a recurring expense. |
| list recurring expenses | List all the Expenses with pagination. |
| list recurring invoice child invoices | Retrieve the list of invoices generated from a recurring invoice profile. Use the filter and search parameters to narrow the results. |
| list recurring invoice history | Get the complete history and comments of a recurring invoice. |
| list recurring invoices | List the details of all recurring invoice. |
| list recurring journals | Lists all recurring journals. |
| list register bulk action history | List bulk update and bulk delete history for the given account register. |
| list register transactions | Retrieve transactions for a chart of accounts register (account) as a report view with optional grouping, column selection, and print preferences. |
| list related lists | List all the related lists configured for a specific entity. |
| list retainer invoice | Get the complete history and comments of a retainer invoice. |
| list retainer invoice templates | Get all retainer invoice pdf templates. |
| list retainer invoices | List all retainer invoices with pagination. |
| list retry policies | Get a list of all retry policies configured in your organization. |
| list sales order comments | Get the complete history and comments of sales order. |
| list sales order templates | Get all sales order pdf templates. |
| list sales orders | List all sales orders. |
| list sales receipts | List all sales receipts. |
| list task comments | List comments of a task. |
| list tasks | List a task. |
| list tax authorities | List of tax authorities. Note: You have to enable Sales Tax in order to perform tax related operations. |
| list tax exemptions | List of tax exemptions. Note: You have to enable Sales Tax in order to perform tax related operations. |
| list taxes | List of simple and compound taxes with pagination. Note: You have to enable Sales Tax in order to perform tax related operations. |
| list time entries | List all time entries with pagination. |
| list transaction locks | List all transaction locks with pagination. |
| list unreviewed bank statements | List the unreviewed statement transactions of a bank account. |
| list upcoming actions | Get a report of upcoming time-based workflow action executions. |
| list upcoming workflows | Get a report of upcoming time-based workflow executions. |
| list users | Get the list of all users in the organization. |
| list vendor credit comments | Get history and comments of a vendor credit. |
| list vendor credit refunds of a vendor credit | List all refunds of an existing vendor credit. |
| list vendor credit refunds of all vendor credits | List all refunds with pagination. |
| list vendor credits | Retrieve a paginated list of vendor credits with comprehensive filtering, sorting, and search capabilities. Use query parameters to filter by date, status, amount, vendor details, items, taxes, and custom fields. |
| list vendor payment refunds | List all the refunds pertaining to an existing vendor payment. |
| list vendor payments | List all the payments made to your vendor. |
| list vendors | Retrieve only vendors with filters and pagination. |
| list web tabs | List all the web tabs configured for the organization. |
| list webhook histories | Get a list of webhook execution history records. |
| list webhooks | Get a list of all webhook configurations in your organization. |
| list workflow logs | Get a list of workflow execution logs. |
| list workflows | Get a list of all workflow rules configured in your organization. |
| mail invoice pdf | Email the PDF copy of an invoice to the customer. |
| map invoice with salesorder | Associate one or more existing invoices with a sales orders. |
| mark bank account active | Make an account active. |
| mark bank account inactive | Make an account inactive. |
| mark bill open | Mark a void bill as open. |
| mark bill void | Mark a bill status as void. |
| mark chart of account active | Updates the account status as active. |
| mark chart of account inactive | Updates the account status as inactive. |
| mark contact active | Mark a contact as active. |
| mark contact address as billing | Set a contact address as the billing address. |
| mark contact address as shipping | Set a contact address as the shipping address. |
| mark contact inactive | Mark a contact as inactive. |
| mark contact person primary | Mark a contact person as primary for the contact. |
| mark contacts for 1099 tracking | Enable 1099 tracking for multiple contacts in a single request. Applicable to organizations in the United States edition that report vendor payments for 1099 purposes. |
| mark credit note draft | Convert a voided credit note to Draft. |
| mark credit note einvoice cancelled | Record that a credit note e-invoice was cancelled on the Invoice Registration Portal (IRP) outside of Zoho Books. |
| mark credit note einvoice pushed | Record that a credit note e-invoice was pushed to the Invoice Registration Portal (IRP) outside of Zoho Books, by supplying the acknowledgement details. |
| mark credit note open | Convert a credit note in Draft status to Open. |
| mark credit note ready to push | Mark a credit note e-invoice as ready to be pushed to the Invoice Registration Portal (IRP). |
| mark credit note void | Mark the credit note as Void. |
| mark default option | Mark an option as the default option or clear default option for a reporting tag. |
| mark delivery challan as delivered | Change the status of a delivery challan to delivered. |
| mark delivery challan as open | Change the status of a delivery challan to open. |
| mark delivery challan as returned | Change the status of a delivery challan to returned. |
| mark delivery challan as undelivered | Change the status of a delivery challan to undelivered. |
| mark estimate accepted | Mark a sent estimate as accepted if the customer has accepted it. |
| mark estimate declined | Mark a sent estimate as declined if the customer has rejected it. |
| mark estimate sent | Mark a draft estimate as sent. |
| mark fixed asset active | Mark the fixed asset as active to start calculating depreciation for the asset. |
| mark fixed asset cancel | Cancel the fixed asset. |
| mark fixed asset draft | Mark the fixed asset as draft. |
| mark invoice draft | Mark a voided invoice as draft. |
| mark invoice einvoice cancelled | Record that an invoice e-invoice was cancelled on the Invoice Registration Portal (IRP) outside of Zoho Books. |
| mark invoice einvoice pushed | Record that an invoice e-invoice was pushed to the Invoice Registration Portal (IRP) outside of Zoho Books, by supplying the acknowledgement details. |
| mark invoice ready to push | Mark an invoice e-invoice as ready to be pushed to the Invoice Registration Portal (IRP). |
| mark invoice sent | Mark a draft invoice as sent. |
| mark invoice void | Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits. |
| mark invoices sent | Change the status of one or more invoices to sent. |
| mark invoices shipped | Mark one or more invoices as shipped. |
| mark item active | Mark an inactive item as active. |
| mark item inactive | Mark an active item as inactive. |
| mark journal published | Mark a draft journal as published. |
| mark location active | Mark location as Active. |
| mark location inactive | Mark location as Inactive. |
| mark location primary | Mark location as primary. |
| mark organization inactive | Mark an organization as inactive. |
| mark pricebook active | Mark the pricebook as Active. |
| mark pricebook inactive | Mark the pricebook as Inactive. |
| mark project active | Mark project as active. |
| mark project inactive | Marking a project as inactive. |
| mark purchase order billed | Mark a purchase order as billed. |
| mark purchase order cancelled | Mark a purchase order as cancelled. |
| mark purchase order open | Mark a draft purchase order as open. |
| mark retainer invoice draft | Mark a voided retainer invoice as draft. |
| mark retainer invoice sent | Mark a draft retainer invoice as sent. |
| mark retainer invoice void | Mark an invoice status as void. Upon voiding, the payments and credits associated with the retainer invoices will be unassociated and will be under customer credits. |
| mark sales order as open | Mark a draft sales order as open. |
| mark sales order as void | Mark a sales order as void. |
| mark task as completed | Mark a task as completed. |
| mark task as ongoing | Mark a task as ongoing. |
| mark task as open | Mark a task as open. |
| mark user active | Mark an inactive user as active. |
| mark user inactive | Mark an active user as inactive. |
| mark vendor credit open | Change an existing vendor credit status to open. |
| mark vendor credit void | Mark an existing vendor credit as void. |
| match bank transaction | Match an uncategorized transaction with an existing transaction in the account. |
| merge contact | Merge a duplicate contact into another contact. |
| overwrite blueprint | Overwrite an existing blueprint with new details. |
| poll custom function status | Check if a custom function integration type is enabled. |
| preview invoice coupons | Preview the effect of applying coupons to an invoice before it is created. |
| print credit notes | Export the selected credit notes as a single PDF file. Use this to print or download one or more credit notes together. |
| print invoice delivery note | Export the delivery note of an invoice as a PDF file. |
| print invoice packing slip | Export the packing slip of an invoice as a PDF file. |
| publish blueprint | Publish a blueprint to make it active. |
| push credit note einvoice | Push the e-invoice of a credit note to the Invoice Registration Portal (IRP). |
| push credit note refund einvoice | Push the e-invoice of a credit note refund to the Invoice Registration Portal (IRP). |
| push credit notes einvoice | Push the e-invoices of multiple credit notes to the Invoice Registration Portal (IRP). |
| push invoice einvoice | Push the e-invoice of an invoice to the Invoice Registration Portal (IRP). |
| push invoices einvoice | Push the e-invoices of multiple invoices to the Invoice Registration Portal (IRP). |
| recall credit note einvoice status | Revert the manually updated e-invoice status of a credit note. |
| recall invoice einvoice status | Revert the manually updated e-invoice status of an invoice. |
| reevaluate base currency adjustment | Reevaluates a base currency adjustment. |
| refund excess vendor payment | Refund the excess amount paid to the vendor. |
| refund vendor credit | Refund vendor credit amount. |
| regenerate custom trigger apikey | Regenerate the API key for a custom trigger. |
| reject credit note | Reject a credit note that is pending approval. Optionally provide a reason for the rejection. |
| reject invoice | Reject an invoice that is pending approval. Optionally provide a reason for the rejection. |
| reject journal | Rejects a journal. |
| reject purchase orders | Reject a purchase order. |
| remind customer for invoice payment | Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status. |
| remove item from portal | Remove an item from the customer portal so that it is no longer available there. |
| reorder bank account rules | Change the order in which bank rules are evaluated. |
| reorder custom fields | Reorder the display order of custom fields for a specific entity type. |
| reorder custom views | Reorder the custom views for a specific entity type. |
| reorder related lists | Reorder the display order of related lists for a specific entity. |
| reorder tags | Reorder the reporting tags in your organization. The order of tags will be followed in transactions and reports. |
| reorder web tabs | Reorder the display order of web tabs. |
| reorder workflows | Change the execution order of workflow rules. |
| resend contact person portal invite | Resend the client portal invitation to a contact person. |
| resend webhook | Resend a failed webhook execution. |
| restore bank transaction | Restore an excluded transaction in your account. |
| restore contact documents | Restore previously deleted contact documents. |
| resume recurring bill | Resume a stopped recurring bill. |
| resume recurring expense | Resume a stopped recurring expense. |
| resume recurring invoice | Resume a stopped recurring invoice. |
| resume recurring invoices | Resume multiple stopped recurring invoices in a single request. The recurring invoices resume generating child invoices on their schedule. |
| resume recurring journal | Resumes a stopped recurring journal. |
| return delivery challans | Partially return one or more delivery challans by specifying the line items and quantities to return. |
| reverse journal | Reverses a journal entry. |
| save bank reconciliation draft | Save the progress of a bank reconciliation as a draft. |
| schedule invoice email | Schedule an invoice to be emailed to the customer at a future date and time. |
| sell fixed asset | Sell the fixed asset. |
| send contact client review email | Send the client review email to a contact. |
| send contact payment method email | Send an email requesting a payment method from a contact. |
| send contact sms | Send an SMS notification to a contact. |
| send contact vendor statement email | Send the vendor statement email to a contact. |
| send contacts sms | Send an SMS notification to multiple contacts. |
| send custom notification | Create and send an execution limit or execution failure notification. |
| send invoice dunning notifications | Send dunning notifications to the customer for an overdue invoice. |
| send invoice retry sms | Resend the online payment SMS notification for an invoice. |
| send invoice sms | Send an invoice notification to the customer by SMS. |
| send invoice via snail mail | Send a physical copy of an invoice to the customer through snail mail. |
| skip suggested bank account rule | Dismiss a bank rule suggested by Zoho Books. |
| start entry timer | Start tracking time spent. |
| stop entry timer | Stop tracking time, say taking a break or leaving. |
| stop recurring bill | Stop an active recurring bill. |
| stop recurring expense | Stop an active recurring expense. |
| stop recurring invoice | Stop an active recurring invoice. |
| stop recurring invoices | Stop multiple active recurring invoices in a single request. The recurring invoices stop generating child invoices until they are resumed. |
| stop recurring journal | Stops an active recurring journal. |
| submit bill | Submit a bill for approval. |
| submit credit note | Submit an estimate for approval. |
| submit credit notes | Submit multiple credit notes for approval in a single request. Use this to send credit notes for approval in bulk. |
| submit estimate | Submit an estimate for approval. |
| submit invoice | Submit an invoice for approval. |
| submit invoices | Submit one or more invoices for approval. |
| submit journal for approval | Submits a journal for approval. |
| submit purchase order | Submit a purchase order for approval. |
| submit retainer invoice | Submit a retainer invoice for approval. |
| submit sales order | Submit a sales order for approval. |
| submit vendor credit | Submit a Vendor credit for approval. |
| track contact 1099 | Track a contact for 1099 reporting: (Note: This API is only available when the organization's country is U.S.A). |
| trigger workflow | Manually trigger a workflow for a specific entity. |
| trigger workflow action | Manually trigger time-based actions of a workflow for a specific entity. |
| uncategorize bank transaction | Revert a categorized transaction as uncategorized. |
| undo return delivery challans | Undo a previously applied return for one or more delivery challans. |
| unmap invoices from salesorders | Remove the mapping between invoices and their associated sales orders. |
| unmatch bank transaction | Unmatch a transaction that was previously matched and make it uncategorized. |
| unship invoices | Revert the shipped status of one or more invoices. |
| untrack contact 1099 | Use this API to stop tracking payments to a vendor for 1099 reporting. (Note: This API is only available when the organization's country is U.S.A). |
| update a task | Update a tasks. |
| update alert | Update an existing email alert configuration. |
| update bank account | Modify the account that was created. |
| update bank account match filter | Update a match filter used to identify bank transactions for rules. |
| update bank account preferences | Update the preferences of a bank account. |
| update bank account rule | Make changes to the rule, add or modify it and update. |
| update bank reconciliation | Update a bank reconciliation. |
| update bank transaction | Make changes in the applicable fields of a transaction and update it. |
| update bill | Update a bill. To delete a line item just remove it from the line_items list. |
| update bill billing address | Updates the billing address for this bill. |
| update bill using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a bill by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding bill will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing bills, a new bill will be created if the necessary payload details are available |
| update blueprint | Update an existing blueprint. |
| update blueprint process state | Update the state of a blueprint, such as activating or deactivating it. |
| update blueprint state | Update an existing state of a blueprint. |
| update blueprint transition | Update an existing transition of a blueprint. |
| update blueprint transitions for record | Update the available blueprint transitions for a specific record. |
| update chart of account | Updates the account information. |
| update contact | Update an existing contact with comprehensive business information. This operation allows you to modify all contact details including basic information, addresses, contact persons, payment terms, tax settings, and custom fields. For contact person, you can add new contact persons, update existing ones, or remove them by excluding them from the contact_persons list. |
| update contact address | Edit the additional address of a contact using the arguments below. |
| update contact bank account | Update the details of a bank account associated with a contact. |
| update contact card | Update the details of a card associated with a contact. |
| update contact document | Update a document attached to a contact. |
| update contact person | Update an existing contact person. |
| update contact tags | Update the reporting tags associated with a contact. |
| update contact tax info | Update a tax information record of a contact. |
| update contact trn status | Update the tax registration number (TRN) verification status of a contact. |
| update contact using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a contact by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding contact will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing contacts, a new contact will be created if the necessary payload details are available |
| update credit note | Details of an existing creditnote. |
| update credit note billing address | Updates the billing address for an existing credit note alone. |
| update credit note cfdi status | Update the CFDI (Comprobante Fiscal Digital por Internet) status of a credit note for the Mexico edition. |
| update credit note custom fields | Update the values of the custom fields associated with a credit note. |
| update credit note document | Update a document attached to a credit note. |
| update credit note refund | Update the refunded transaction. |
| update credit note shipping address | Updates the shipping address for an existing credit note alone. |
| update credit note template | Update the pdf template associated with the credit note. |
| update credit note using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a credit note by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding credit note will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing credit notes, a new credit note will be created if the necessary payload details are available |
| update currency | Update the details of a currency. |
| update custom action | Update an existing custom action. |
| update custom button | Update an existing custom button. |
| update custom field | Update an existing custom field. |
| update custom fields in bill | Update the value of the custom field in existing bills. |
| update custom fields in customer payment | Update the value of the custom field in existing customerpayments. |
| update custom fields in estimate | Update the value of the custom field in existing estimates. |
| update custom fields in invoice | Update the value of the custom field in existing invoices. |
| update custom fields in item | Update the value of the custom field in existing items. |
| update custom fields in purchase order | Update the value of the custom field in existing purchaseorders. |
| update custom function | Update an existing custom function. |
| update custom module | Update the configuration of an existing custom module. |
| update custom module record | Update an existing record in a custom module. |
| update custom notification preference | Update the custom notification preferences. |
| update custom scheduler | Update an existing custom scheduler. |
| update custom trigger | Update an existing custom trigger. |
| update custom view | Update an existing custom view. |
| update customer debit note | Update an existing customer debit note. To delete a line item just remove it from the line_items list. |
| update customer payment | Update an existing payment information. |
| update customer payment refund | Update the refunded transaction. |
| update customer payment using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a payment by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding payment will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing payments, a new payment will be created if the necessary payload details are available |
| update delivery challan | Update an existing delivery challan. |
| update delivery challan shipping address | Update the shipping address of an existing delivery challan. |
| update delivery challan template | Assign a different template to an existing delivery challan. |
| update estimate | Update an existing estimate. To delete a line item just remove it from the line_items list. |
| update estimate billing address | Updates the billing address for this estimate alone. |
| update estimate comment | Update an existing comment of an estimate. |
| update estimate shipping address | Updates the shipping address for an existing estimate alone. |
| update estimate template | Update the pdf template associated with the estimate. |
| update estimate using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an estimate by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding estimate will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing estimates, a new estimate will be created if the necessary payload details are available |
| update exchange rate | Update the details of exchange rate for a currency. |
| update expense | Update an existing Expense. |
| update expense using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a expense by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding bill expense be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing expenses, a new expense will be created if the necessary payload details are available |
| update field dropdown options | Add, update, or remove dropdown options for a custom field. |
| update field status | Activate or deactivate a custom field. |
| update field update | Update an existing field update configuration. |
| update fixed asset | Updates the fixed asset with given information. |
| update fixed asset type | Updates the fixed asset type with given information. |
| update invoice | Update an existing invoice. To delete a line item just remove it from the line_items list. |
| update invoice advanced tracking details | Update the advanced inventory tracking details (batches or serial numbers) of the line items in an invoice. |
| update invoice billing address | Updates the billing address for this invoice alone. |
| update invoice cfdi status | Update the CFDI (Comprobante Fiscal Digital por Internet) status of an invoice for the Mexico edition. |
| update invoice comment | Update an existing comment of an invoice. |
| update invoice einvoice payment status | Update the payment status of an invoice e-invoice on the Invoice Registration Portal (IRP). |
| update invoice metadata | Update a metadata value stored against an invoice. |
| update invoice shipping address | Updates the shipping address for this invoice alone. |
| update invoice template | Update the pdf template associated with the invoice. |
| update invoice using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an invoice by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding invoice will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing invoices, a new invoice will be created if the necessary payload details are available |
| update item | Update the details of an item. |
| update item using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an item by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding item will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing items, a new item will be created if the necessary payload details are available |
| update journal | Updates the journal with given information. |
| update location | Update location |
| update opening balance | Updates the existing opening balance information. |
| update organization | Update the details of an organization. |
| update organization address | Update an existing address of the organization. |
| update partial unlock | Update partial unlock settings for transaction locking. |
| update percentage task | Update completed percentage of a task. |
| update pricebook | update existing pricebook. |
| update project | Update details of a project. |
| update project task | Update the details of a project task. |
| update project user | Update details of a user. |
| update projects using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a project by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding project will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing projects, a new project will be created if the necessary payload details are available |
| update purchase order | Update an existing purchase order. |
| update purchase order billing address | Updates the billing address for this purchase order alone. |
| update purchase order comment | Update an existing comment of a purchase order. |
| update purchase order template | Update the pdf template associated with the purchase order. |
| update purchase order using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a purchase order by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding purchase order will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing purchase orders, a new purchase order will be created if the necessary payload details are available |
| update push notification | Update an existing push notification configuration. |
| update recurring bill | Update a recurring bill. To delete a line item just remove it from the line_items list. |
| update recurring bill using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a recurring bill by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding recurring bill will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing recurring bills, a new recurring bill will be created if the necessary payload details are available |
| update recurring expense | Update a recurring expense. |
| update recurring expense using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a recurring expense by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding recurring expense will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing recurring expenses, a new recurring expense will be created if the necessary payload details are available |
| update recurring invoice | Update the recurring invoice. |
| update recurring invoice template | Update the pdf template associated with the recurring invoice. |
| update recurring invoice using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a recurring invoice by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding recurring invoice will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing recurring invoices, a new recurring invoice will be created if the necessary payload details are available |
| update recurring journal | Updates an existing recurring journal. |
| update related list | Update an existing related list. |
| update related list status | Activate or deactivate a related list. |
| update retainer invoice | Update an existing invoice. |
| update retainer invoice billing address | Updates the billing address for this retainer invoice alone. |
| update retainer invoice comment | Update an existing comment of a retainer invoice. |
| update retainer invoice template | Update the pdf template associated with the retainer invoice. |
| update retry policy | Update an existing retry policy. |
| update sales order | Update an existing sales order. To delete a line item just remove it from the line_items list. |
| update sales order billing address | Updates the billing address for this sales order alone. |
| update sales order comment | Update existing comment of a sales order. |
| update sales order shipping address | Updates the shipping address for this sales order alone. |
| update sales order sub status | Update a sales order sub status. |
| update sales order template | Update the pdf template associated with the sales order. |
| update sales order using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a sales order by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding sales order will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing sales orders, a new sales order will be created if the necessary payload details are available |
| update sales receipt | Update an existing sales receipt. |
| update salesorder customfields | Update the value of the custom field in existing salesorders. |
| update tag | Update a reporting tag |
| update tag criteria | Update the visibility conditions (or filter in some places) of a reporting tag. You can set other tags or location as filters for a tag. Check our help document to know about the requirements of a tag to be associated as a filter to another tag. |
| update tag options | Create, update or delete the options of a reporting tag. Reorder and arrange them in an hierarchical structure as per your organization requirements. <br><b>NOTE:</b> <br><ol> <li>An option cannot be a child option beyond five hierarchical level.</li> <li>The overall children of an option cannot exceed 500 options.</li></ol> |
| update tasks | Update tasks. |
| update tax | Update the details of a simple or compound tax. Note: You have to enable Sales Tax in order to perform tax related operations. |
| update tax authority | Update the details of a tax authority. Note: You have to enable Sales Tax in order to perform tax related operations. |
| update tax exemption | Update the details of a tax exemption. Note: You have to enable Sales Tax in order to perform tax related operations. |
| update tax group | Update the details of the tax group. Note: You have to enable Sales Tax in order to perform tax related operations. |
| update time entry | Update logged time entry. |
| update transaction lock | Update transaction lock settings. |
| update user | Update the details of a user. |
| update vendor credit | Update an existing vendor credit. |
| update vendor credit refund | Update the refunded transaction. |
| update vendor payment | Update an existing vendor payment. You can also modify the amount applied to the bills. |
| update vendor payment refund | Update the refunded transaction. |
| update vendor payment using custom field | A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update a vendor payment by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding vendor payment will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing vendor payments, a new vendor payment will be created if the necessary payload details are available |
| update web tab | Update an existing web tab. |
| update web tab status | Activate or deactivate a web tab. |
| update webhook | Update an existing webhook configuration. |
| update workflow | Update an existing workflow rule. |
| upgrade organization to books | Upgrade an organization from Zoho Invoice to Zoho Books. |
| upload credit note digital signature | Upload the digitally signed copy of a credit note. |
| upload invoice digital signature | Upload the digitally signed copy of an invoice. |
| upload invoice document | Upload the file content for a document attached to an invoice. |
| verify contact address | Validate a contact address against the provided address fields. Use this before creating or updating a contact to confirm that the address is valid. |
| verify contact address by id | Verify a specific address of a contact. |
| verify contact bank account | Verify a contact bank account using the two micro-deposit amounts credited to the account. Provide the deposit amounts to confirm ownership of the bank account. |
| verify contact einvoice | Verify the e-invoice (GST) details of a contact. |
| void invoices | Mark multiple invoices as void in a single request. Voided invoices are retained for record-keeping but are excluded from receivables. |
| write off fixed asset | Write off the fixed asset. |
| write off invoice | Write off the invoice balance amount of an invoice. |
| write off invoices | Write off the balance amount of one or more invoices. |
| writeoff opening balance | Writes off an opening balance entry. |
