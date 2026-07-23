# Naming Standard

Single source of truth for file and folder naming across all QUANTINOVA INDUSTRIES CORP
repositories. Repository-specific standards may add stricter rules but must not weaken these.

## 1. Folders

- Folders are `lowercase`, using `lower_snake_case` for multi-word names.
- Examples: `docs`, `templates`, `profile`.
- Platform-fixed directories keep their required exact form (for example `.github/` and
  `.github/ISSUE_TEMPLATE/`).

## 2. Files

- Files are `UPPERCASE_NAME.lowercaseext` — uppercase base name, lowercase extension.
- Examples: `REPOSITORY_STANDARDS.md`, `BRANCH_STRATEGY.md`, `INTEGRATION_MAP.json`.

## 3. Fixed-name exceptions (tool- or platform-mandated)

These keep their required exact form, because the toolchain or GitHub recognizes them only by
that name:

| Item | Reason |
|---|---|
| `.github/`, `.git/` | Platform-recognized directories |
| `.gitignore`, `.gitattributes` | Git-recognized dotfiles |
| `LICENSE`, `CODEOWNERS` | GitHub-recognized fixed names (no extension) |
| `.github/ISSUE_TEMPLATE/` and its `*.yml` forms | GitHub issue-form contract (lowercase filenames) |
| Plugin skill / agent / command file and directory names | Loader requires lowercase names |

`README.md`, `CLAUDE.md`, and `AGENTS.md` follow the standard file rule in section 2 and match
the exact names GitHub and AI tooling read; they are not exceptions.

## 4. Branches and commits

- Branches: UPPERCASE `<TYPE>/<SUBJECT>` (see `BRANCH_STRATEGY.md`).
- Commits: lowercase Conventional Commits (see `COMMIT_CONVENTIONS.md`).
- The two conventions are intentionally different and must not be conflated.

## 5. Hygiene

- UTF-8 without BOM; LF line endings; no trailing whitespace.
- No AI attribution anywhere — in files, metadata, frontmatter, or commit messages.
