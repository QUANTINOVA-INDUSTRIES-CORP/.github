# Contributing to QUANTINOVA INDUSTRIES CORP Repositories

Thank you for contributing. This document defines the default contribution process for repositories owned by QUANTINOVA INDUSTRIES CORP. A repository-specific `CONTRIBUTING.md` or stricter policy takes precedence.

## 1. Before contributing

1. Read the repository `README.md`, security policy, license, and local development instructions.
2. Search open and closed issues and pull requests.
3. Open or obtain an approved issue before substantial, breaking, security-sensitive, or architectural work.
4. Confirm that the repository accepts the proposed contribution. Some repositories are private, restricted, archived, generated, or maintained only through an internal process.
5. Never place credentials, client records, personal data, procurement-sensitive information, production exports, or other confidential material in an issue, branch, commit, pull request, log, or test fixture.

Security vulnerabilities must be reported under `SECURITY.md`, not through public issues.

## 2. Development setup

Use the repository's documented toolchain and lockfiles. Do not change runtime versions, package managers, formatting systems, or build tools unless the approved work requires it.

A typical setup is:

```bash
git clone https://github.com/QUANTINOVA-INDUSTRIES-CORP/[REPOSITORY_NAME].git
cd [REPOSITORY_NAME]
git switch main
git pull --ff-only
git switch -c FEAT/[ISSUE_ID]_SHORT_SUBJECT
```

Repository documentation must replace `[REPOSITORY_NAME]`, `[ISSUE_ID]`, and any other placeholder with approved values.

## 3. Branches

Follow `docs/BRANCH_STRATEGY.md`.

Default branch categories:

- `FEAT/` — new capability;
- `FIX/` — defect correction;
- `DOCS/` — documentation only;
- `REFACTOR/` — behavior-preserving code change;
- `TEST/` — test-only change;
- `CHORE/` — maintenance;
- `SECURITY/` — approved security remediation;
- `HOTFIX/` — urgent production correction;
- `RELEASE/` — controlled release preparation where used;
- `EXPERIMENT/` — time-boxed, non-production experiment.

Keep branches short-lived and focused. Do not commit directly to protected branches.

## 4. Code and documentation standards

Follow:

- `docs/STANDARDS.md`;
- `docs/COMMIT_CONVENTIONS.md`;
- repository-specific linters, formatters, type checkers, tests, and architecture rules.

Required principles include:

- least privilege and secure defaults;
- explicit validation and failure handling;
- no embedded secrets;
- deterministic builds and committed lockfiles;
- tests for changed behavior;
- backward compatibility or an approved migration;
- documentation for user-visible, operational, configuration, schema, and API changes;
- comments that explain decisions and constraints rather than restating syntax.

## 5. Testing

Run the complete repository-defined validation suite before opening a pull request.

Examples:

```bash
# Node.js / TypeScript
npm ci
npm run lint --if-present
npm run typecheck --if-present
npm test --if-present
npm run build --if-present

# Python
python -m pip install -r requirements-dev.txt
ruff check .
pytest -q
python -m build
```

These examples do not override repository-specific commands.

Tests must cover:

- intended success behavior;
- relevant failure behavior;
- authorization and validation boundaries;
- regressions fixed by the change;
- migration and rollback behavior when applicable.

Do not weaken, skip, or delete a test merely to obtain a passing build unless the test is demonstrably invalid and the pull request documents the reason.

## 6. Commits

Use Conventional Commits as defined in `docs/COMMIT_CONVENTIONS.md`.

Examples:

```text
feat(supplier): add duplicate-registration validation
fix(costing): preserve decimal precision in margin calculation
docs(security): clarify vulnerability reporting process
```

Commits must be understandable, scoped, and free of unrelated generated files or formatting changes.

## 7. Pull requests

Open a pull request against the repository's approved target branch and complete every applicable section of the pull-request template.

A reviewable pull request must:

- explain the problem and solution;
- link the approved issue or work item;
- identify risk, data impact, security impact, and compatibility;
- include test evidence;
- document deployment and rollback where applicable;
- disclose breaking changes and migrations;
- contain no unresolved placeholders, debugging code, or confidential material;
- remain within the approved scope.

Draft pull requests may be used for early design feedback. They must be marked ready only when the author checklist is complete.

## 8. Review and approval

Authors must not approve their own pull requests.

Reviewers evaluate:

- correctness and requirement fit;
- security, privacy, and access control;
- architecture and maintainability;
- tests and evidence;
- operational readiness;
- documentation and migration quality;
- scope discipline.

All required checks, code-owner approvals, and conversations must be resolved before merge. Approval may be revoked when material changes are pushed after review.

## 9. Merge and release

Use the repository's approved merge method. Squash merge is preferred for repositories that require one Conventional Commit per pull request. Preserve separate commits only when their history has independent operational value.

Delete merged feature branches unless retention is explicitly required.

A merged pull request is not automatically authorization to deploy. Follow the repository's release, change-management, and production-approval process.

## 10. Dependencies and third-party code

Dependency changes require review of:

- necessity and maintenance health;
- source and publisher authenticity;
- known vulnerabilities;
- license compatibility;
- transitive dependency impact;
- lockfile changes;
- runtime and deployment impact.

Do not add copied code, media, data, or documentation without confirmed rights and attribution.

## 11. AI-assisted contributions

AI-assisted work is permitted only when consistent with repository and corporate policy.

The contributor remains accountable for:

- factual and technical correctness;
- license and provenance;
- security and confidentiality;
- tests and documentation;
- disclosure when required by the repository;
- removing fabricated APIs, citations, packages, or behavior.

Do not submit confidential information to unapproved external AI services.

## 12. Conduct

Participation is subject to `CODE_OF_CONDUCT.md`.

## 13. Questions

Use the channels described in `SUPPORT.md`. Do not use support channels to disclose vulnerabilities.
