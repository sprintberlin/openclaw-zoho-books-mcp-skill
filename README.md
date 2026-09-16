# Zoho Books MCP

Connect your agent to Zoho Books through the Model Context Protocol (MCP). This skill provides everything you need to list organizations, inspect contacts, invoices, expenses, bills, and items using `mcporter`.

This repository contains the public source for the ClawHub skill [`@sprintcx/zoho-books-mcp`](https://clawhub.ai/sprintcx/skills/zoho-books-mcp).

## What This Skill Includes

- Agent Skill instructions in `SKILL.md` (portable SKILL.md format)
- ClawHub release card metadata in `skill-card.md`
- Ready-to-use Python helpers for organizations and records (contacts, invoices, expenses, bills, items)
- Multi-account profile support for single-org and multi-tenant setups
- Security-conscious `mcporter` calls without shell expansion

## Requirements

| Requirement | Details |
|---|---|
| Zoho Books MCP Server | A configured endpoint from [mcp.zoho.eu](https://mcp.zoho.eu) |
| mcporter | MCP client CLI (bundled with OpenClaw; elsewhere `npm i -g mcporter`) |
| Endpoint selection | `ZOHO_BOOKS_MCP_URL` for one account; named profiles or `--mcp-url` for multiple accounts |
| Organization ID | `ZOHO_BOOKS_ORGANIZATION_ID` or profile `organization_id` for scoped calls |

### Single-account setup

For the common single-account case, set `ZOHO_BOOKS_MCP_URL` and `ZOHO_BOOKS_ORGANIZATION_ID`:

```bash
export ZOHO_BOOKS_MCP_URL="https://your-org-zoho-books-xxxxx.zohomcp.eu/mcp/YOUR_TOKEN/message"
export ZOHO_BOOKS_ORGANIZATION_ID="123456789"
```

To verify without printing credentials:

```bash
if [ -n "$ZOHO_BOOKS_MCP_URL" ]; then echo "ZOHO_BOOKS_MCP_URL is set"; else echo "ZOHO_BOOKS_MCP_URL is not set"; fi
```

### Multiple organizations and customer accounts

Use one shared profile file instead of changing global environment variables:

```json
{
  "version": 1,
  "profiles": {
    "acme": {
      "services": {
        "books": {
          "env": "ACME_BOOKS_MCP_URL",
          "organization_id": "123456789"
        }
      }
    }
  }
}
```

```bash
python3 scripts/list_records.py invoices --profile acme
```

The default file is `~/.config/zoho-mcp/profiles.json`. Full format: [`references/MULTI_ACCOUNT.md`](references/MULTI_ACCOUNT.md).

## Quick Start

### List available tools on your MCP server

```bash
mcporter list "$ZOHO_BOOKS_MCP_URL"
```

### List organizations

```bash
python3 scripts/list_organizations.py
```

### List invoices

```bash
python3 scripts/list_records.py invoices --limit 20
```

## Python Scripts

- `scripts/list_organizations.py`: List accessible Zoho Books organizations.
- `scripts/list_records.py`: Query contacts, invoices, expenses, bills, or items.
- `scripts/mcp_endpoint.py`: Shared endpoint and profile resolver.
- `tests/test_endpoint_resolution.py`: Credential-free resolver tests.

## Repository Files

- `SKILL.md`: Agent Skill instructions.
- `references/ACTION_PROFILES.md`: Least-privilege Books Action profiles.
- `references/COMMON_WORKFLOWS.md`: Verified workflows for frequent Books tasks.
- `references/ZOHO_BOOKS_MCP_ACTIONS.md`: Complete catalog of 1,090 known Books Actions.
- `references/MULTI_ACCOUNT.md`: Portable single-account and multi-account endpoint profiles.
- `scripts/list_organizations.py`: List accessible Books organizations.
- `scripts/list_records.py`: Paginated listing for contacts, invoices, expenses, bills, and items.
- `scripts/mcp_endpoint.py`: Shared endpoint, profile, and organization resolver.
- `scripts/mcp_client.py`: Shell-free `mcporter` client wrapper.
- `tests/`: Credential-free helper and resolver tests.

## Security Notes

The bundled scripts call `mcporter` directly through `subprocess.run([...])` without shell expansion. Accounting data is sensitive. Load only required records and never copy contents into chats, logs, or repositories.

## Publish

Publish under the SprintCX ClawHub organization:

```bash
clawhub skill publish . \
  --slug zoho-books-mcp \
  --name "Zoho Books MCP" \
  --owner sprintcx \
  --version 1.0.0 \
  --source-repo sprintberlin/openclaw-zoho-books-mcp-skill \
  --source-ref main \
  --source-path . \
  --changelog "Initial public Books MCP skill with portable account profiles"
```
