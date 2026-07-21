# Naming Standard

Single source of truth for file and folder naming across all QUANTINOVA INDUSTRIES CORP
repositories. Repository-specific standards may add stricter rules but must not weaken these.

## 1. Folders

- Folders are `UPPERCASE`, using `UPPER_SNAKE_CASE` for multi-word names.
- Examples: `GOVERNANCE`, `DECISION_REGISTERS`, `WORKFLOW_TEMPLATES`.

## 2. Files

- Files are `UPPERCASE_NAME.lowercaseext` — uppercase base name, lowercase extension.
- Examples: `REPOSITORY_STANDARDS.md`, `BRANCH_STRATEGY.md`, `INTEGRATION_MAP.json`.

## 3. Lowercase exceptions (tool- or platform-mandated)

These keep their required lowercase or fixed form, because the toolchain or GitHub recognizes
them only by an exact name:

| Item | Reason |
|---|---|
| `readme.md` | Rendered as the repository/profile landing file |
| `claude.md`, `agents.md`, `codex.md` | AI agent instruction files read by name |
| `.github/`, `.git/` | Platform-recognized directories |
| `.gitignore`, `.gitattributes` | Git-recognized dotfiles |
| `LICENSE`, `CODEOWNERS` | GitHub-recognized fixed names |
| `.github/ISSUE_TEMPLATE/` and its `*.yml` forms | GitHub issue-form contract |
| Plugin skill / agent / command file and directory names | Loader requires lowercase names |

## 4. Branches and commits

- Branches: UPPERCASE `<TYPE>/<SUBJECT>` (see `BRANCH_STRATEGY.md`).
- Commits: lowercase Conventional Commits (see `COMMIT_CONVENTIONS.md`).
- The two conventions are intentionally different and must not be conflated.

## 5. Hygiene

- UTF-8 without BOM; LF line endings; no trailing whitespace.
- No AI attribution anywhere — in files, metadata, frontmatter, or commit messages.
