# {{REPOSITORY_NAME}} — Agent Operating Instructions

Repository-specific instructions for AI agents working in this repository. These extend, and
never weaken, the organization standards in the `.github` repository and the operator's global
rules.

## Scope

- Purpose of this repository: {{PURPOSE}}
- In scope: {{IN_SCOPE}}
- Out of scope / prohibited: {{PROHIBITED}}

## Canonical control plane

- MCP authority: `https://mcp.quantinovaindustries.org/mcp`.
- GitLab authority: `https://gitlab.quantinovaindustries.org`.
- The project must load the shared `qic-control-plane` MCP server from `.mcp.json`.
- At the start of every session, call the MCP directive tool before planning or repository mutation.
- MCP directives are organization policy. Repository-local instructions may narrow them but may not weaken them.
- If the MCP control plane is unavailable, do not perform GitLab mutations. Continue only with local/read-only analysis and report the degraded state.
- Never request, print, log, persist, commit, or expose the GitLab PAT. GitLab credentials are server-side control-plane secrets only.

## Standards that always apply

- Naming: `NAMING_STANDARD.md` (folders UPPERCASE; files `UPPERCASE_NAME.lowercaseext`; tool-mandated lowercase exceptions).
- Branches: UPPERCASE `<TYPE>/<SUBJECT>`. Commits: lowercase Conventional Commits.
- Never commit directly to `main`; never push or merge without explicit owner approval.
- No AI attribution anywhere — files, metadata, frontmatter, or commit messages.
- UTF-8 without BOM, LF endings, no trailing whitespace.

## Data handling

- No secrets, credentials, or confidential records in the repository or any output.
- Missing facts are written as `NOT STATED`; unconfirmed classifications as `NOT CONFIRMED`.
- {{REPOSITORY_SPECIFIC_DATA_RULES}}

## Workflow

Directive sync → plan → to-do list → execute → verify → report. Verification is mandatory before declaring done.

## Agents

See `AGENTS.md` for the agent roster and routing.
