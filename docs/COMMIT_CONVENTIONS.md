# Commit Conventions

## 1. Standard

QUANTINOVA INDUSTRIES CORP uses Conventional Commits 1.0.0 for human-readable history, automated release tooling, changelog generation, and traceability.

Format:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

Example:

```text
feat(costing): add configurable withholding basis

Support goods and services classifications without inferring a rate.

Closes #184
```

## 2. Required rules

- Use lowercase type and scope.
- Use an imperative, concise description.
- Do not end the subject with a period.
- Keep the subject focused on one logical change.
- Explain why and material consequences in the body.
- Reference issues, incidents, decisions, or migrations in footers.
- Mark breaking changes explicitly.
- Do not include secrets, personal data, client records, or confidential details.

## 3. Types

| Type | Meaning |
|---|---|
| `feat` | New user-visible or business capability |
| `fix` | Defect correction |
| `docs` | Documentation-only change |
| `refactor` | Code restructuring without intended behavior change |
| `perf` | Performance improvement |
| `test` | Test addition or correction |
| `build` | Build system or external dependency change |
| `ci` | CI/CD workflow or configuration change |
| `chore` | Maintenance not covered by another type |
| `revert` | Reversion of a previous commit |
| `security` | Security control or vulnerability remediation |
| `data` | Data model, seed, transformation, or migration change |
| `style` | Formatting-only change with no behavior impact |

Use the most specific type. Do not use `chore` as a catch-all for features or fixes.

## 4. Scope

The optional scope identifies the affected domain, package, service, or component.

Examples:

```text
feat(supplier): add accreditation expiry tracking
fix(api): reject invalid pagination cursors
docs(runbook): add database restore verification
ci(node): test Node.js 24
security(auth): rotate session after privilege change
```

Use stable domain terminology. Avoid names of individuals, temporary sprint labels, or vague scopes such as `misc`.

## 5. Description

Good descriptions:

```text
fix(costing): preserve decimal precision in bid margin
feat(rfq): export submission checklist as PDF
security(actions): restrict token permissions to read-only
```

Poor descriptions:

```text
update files
fix bug
changes
WIP
final
misc fixes
```

## 6. Body

Use the body when the subject cannot explain context, constraints, behavior, risk, or migration.

The body should answer relevant questions:

- Why was the change required?
- What behavior changed?
- What alternatives were rejected?
- What operational or compatibility impact exists?
- How was risk controlled?
- Is follow-up work required?

Wrap prose at a reasonable width when practical. Use bullets for distinct facts.

## 7. Footers

Common footers:

```text
Closes #184
Fixes #231
Refs #77
Incident: INC-2026-014
Decision: ADR-0008
Migration: MIG-0021
```

Use GitHub closing keywords only when the commit or merged pull request fully resolves the issue.

## 8. Breaking changes

Use either `!` after the type or scope, or a `BREAKING CHANGE:` footer. For clarity, use both for material changes.

```text
feat(api)!: require idempotency keys for order creation

BREAKING CHANGE: POST /orders now rejects requests without an
Idempotency-Key header. Clients must generate and retain a unique key
for each logical order.
```

A breaking-change commit must include migration guidance, compatibility impact, and release coordination.

## 9. Reverts

Use:

```text
revert: feat(costing): add configurable withholding basis

This reverts commit 0123456789abcdef.

Reason: The production configuration does not yet provide the required
transaction classification.
```

Do not manually reverse a material change without identifying the reverted commit and reason.

## 10. Merge and squash commits

When squash merging, edit the generated message to a compliant Conventional Commit subject and useful body.

Preferred:

```text
feat(supplier): add duplicate-registration validation (#184)
```

Avoid:

```text
Merge pull request #184 from feature-branch
```

A repository using automated semantic versioning must define which types trigger major, minor, and patch releases.

## 11. Commit composition

A good commit is:

- atomic;
- buildable where practical;
- testable;
- understandable without private chat context;
- free of unrelated formatting or generated changes;
- safe to revert independently.

Use fixup commits during development when useful, then squash them before merge unless the repository preserves reviewed commit history.

## 12. Dependency commits

State the package and version.

```text
build(deps): update fastapi from 0.115.0 to 0.116.1
build(deps-dev): update ruff from 0.11.0 to 0.12.2
```

The pull request must still document security, compatibility, license, and lockfile impact.

## 13. Data and migration commits

Use `data` and identify the affected model or migration.

```text
data(suppliers): add accreditation expiry column
data(costing)!: convert amount fields to fixed-precision decimals
```

Destructive or irreversible changes require an approved migration and rollback plan.

## 14. Security commits

Do not reveal exploitable detail in a public commit before coordinated disclosure.

Examples:

```text
security(auth): enforce server-side role validation
security(actions): remove write permission from pull-request workflow
```

For embargoed vulnerabilities, follow the private security-advisory process.

## 15. Examples

```text
feat(profile): publish organization engineering principles
fix(workflow): skip CodeQL when no supported language is detected
docs(branching): define hotfix synchronization procedure
refactor(parser): isolate supplier-record normalization
perf(search): add indexed status filter
test(costing): cover zero-cost margin validation
ci(python): add Python 3.14 test job
security(secrets): block production environment files
data(projects): backfill normalized reference numbers
```

## 16. Validation

Repositories may enforce this convention with commitlint, release tooling, pull-request title checks, or squash-merge controls. Automation supplements review; it does not replace accurate classification or meaningful descriptions.
