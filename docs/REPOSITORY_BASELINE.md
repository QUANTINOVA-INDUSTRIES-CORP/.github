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
| `SECURITY.md` | Vulnerability reporting and handling | Inherit from `.github` |
| `CONTRIBUTING.md` | Contribution and review process | Inherit from `.github` |
| `SUPPORT.md` | Where to get help | Inherit from `.github` |
| `CODEOWNERS` | Review ownership | Local (per repo paths) |
| `LICENSE` | License or proprietary notice | Local (per repo) |
| `.gitignore` | Ignore rules, including local-only automation | Local |
| `.gitattributes` | Enforce LF line endings and text handling | Local |

## 2. Templates

Drop-in starting points live in this repository under `templates/`:
`templates/README.md`, `templates/CLAUDE.md`, `templates/AGENTS.md`, plus starter ignore rules
in `templates/NODE.gitignore` and `templates/PYTHON.gitignore` (copy the relevant one to
`.gitignore`). Copy into a new repository and adapt; do not weaken governance or security clauses.

## 3. Automation is local-only

CI and workflow automation are never committed to the organization. Keep them in a local,
gitignored folder (for example `_LOCAL_CI/`). See `BRANCH_STRATEGY.md` for how validation
and review gating work without org-hosted workflows.

## 4. Conventions

- Naming per `NAMING_STANDARD.md`.
- Branches per `BRANCH_STRATEGY.md`; commits per `COMMIT_CONVENTIONS.md`.
- UTF-8 without BOM, LF endings, no trailing whitespace, no AI attribution.
