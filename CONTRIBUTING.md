# Contributing to openclaw-zoho-books-mcp-skill

Contributions from humans and agents are explicitly welcome. Issues and pull requests are both wanted. Prefer a pull request when you can implement and verify the fix.

## Issue

Use an issue for a reproducible defect, incomplete documentation, a live-schema mismatch, a broken helper or workflow, incorrect parameter guidance, or a missing Action in the profile.

1. Search open issues on GitHub first to link an existing match and avoid duplicates:
   ```bash
   gh issue list --repo sprintberlin/openclaw-zoho-books-mcp-skill --state open
   ```
2. If none exists, write a sanitized body file and create the issue with GitHub CLI (`gh`):
   ```bash
   cat > /tmp/zoho-books-issue.md <<'EOF'
   ### What happened
   ...

   ### Expected behavior
   ...

   ### Reproduction / Environment
   ...
   EOF
   gh issue create \
     --repo sprintberlin/openclaw-zoho-books-mcp-skill \
     --title "bug(schema): <short description>" \
     --body-file /tmp/zoho-books-issue.md
   ```
3. State expected and actual behavior plus minimal reproduction details.
4. Return the issue URL.

Do not file skill issues for endpoint, authentication or profile setup, rate limits, transient service failures, timeouts, organization-specific custom fields, or unsupported Zoho Books operations.

## Pull request

Use a pull request for a verified improvement or fix.

1. Branch from `main` and keep the change focused.
2. Add or update tests for behavior changes under `tests/`.
3. Run the test suite:
   ```bash
   python3 -m unittest discover -s tests
   ```
4. Verify that no credentials, tokens, or customer-specific data are included.
5. Write a sanitized PR body file, then open the pull request with `gh pr create` and link its issue when present:
   ```bash
   cat > /tmp/zoho-books-pr.md <<'EOF'
   Resolves #<issue-number>

   ### Summary
   ...
   EOF
   gh pr create \
     --repo sprintberlin/openclaw-zoho-books-mcp-skill \
     --title "feat(profiles): add bank transaction matching actions" \
     --body-file /tmp/zoho-books-pr.md
   ```

## Requirements

- Use an authenticated GitHub CLI (`gh`) with the required repository access.
- Never submit MCP URLs, tokens, live credentials, customer-specific identifiers, personal data, or accounting record content in issues, PRs, comments, or commits.
- Keep `SKILL.md` short, actionable, and imperative. Put reference material in `references/` and deterministic logic in `scripts/`.
- Preserve compatibility with `mcporter` and existing helper interfaces.
