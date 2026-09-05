# Repository Baseline

Every active QUANTINOVA INDUSTRIES CORP repository must contain, or inherit from this
`.github` repository, the files below. This baseline exists so consolidated repositories
share one predictable structure.

## 1. Required files

| File | Purpose | Inherit or local |
|---|---|---|
| `README.md` | What the repository is, how to use it, ownership | Local (per repo) |
| `CLAUDE.md` | AI agent operating instructions for this repository | Local (from template) |
| `AGENTS.md` | Agent roster and routing for this repository | Local (from template) |
| `.mcp.json` | Canonical `qic-control-plane` MCP bootstrap | Local (from template) |
| `SECURITY.md` | Vulnerability reporting and handling | Inherit from `.github` |
| `CONTRIBUTING.md` | Contribution and review process | Inherit from `.github` |
| `SUPPORT.md` | Where to get help | Inherit from `.github` |
| `CODEOWNERS` | Review ownership | Local (per repo paths) |
| `LICENSE` | License or proprietary notice | Local (per repo) |
| `.gitignore` | Ignore rules, including local-only automation | Local |
| `.gitattributes` | Enforce LF line endings and text handling | Local |

## 2. Templates

Drop-in starting points live in this repository under `templates/`:
`templates/README.md`, `templates/CLAUDE.md`, `templates/AGENTS.md`, `templates/.mcp.json`, plus
starter ignore rules in `templates/NODE.gitignore` and `templates/PYTHON.gitignore` (copy the
relevant one to `.gitignore`). Copy into a new repository and adapt; do not weaken governance or
security clauses.

`templates/.mcp.json` is organization-controlled. It must continue to point the shared
`qic-control-plane` server at `https://mcp.quantinovaindustries.org/mcp`. It must never contain the
GitLab PAT. Client authentication values are supplied at runtime through environment expansion.

## 3. Canonical MCP control plane

All agent harnesses must synchronize organization directives through `qic-control-plane` before
repository mutation. Agent-originated GitLab API operations route through the MCP control plane to
`https://gitlab.quantinovaindustries.org`; the GitLab PAT exists only in the MCP server environment.
If the control plane is unavailable, GitLab mutation is blocked for that agent session.

The reference server and deployment contract live under `MCP/` in this repository.

## 4. Automation is local-only

CI and workflow automation are never committed to the organization. Keep them in a local,
gitignored folder (for example `_LOCAL_CI/`). See `BRANCH_STRATEGY.md` for how validation
and review gating work without org-hosted workflows.

## 5. Conventions

- Naming per `NAMING_STANDARD.md`.
- Branches per `BRANCH_STRATEGY.md`; commits per `COMMIT_CONVENTIONS.md`.
- UTF-8 without BOM, LF endings, no trailing whitespace, no AI attribution.
