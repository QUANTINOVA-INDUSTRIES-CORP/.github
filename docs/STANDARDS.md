# Engineering Standards

## 1. Purpose

These are the default engineering standards for repositories owned by QUANTINOVA INDUSTRIES CORP. Repository-specific standards may add stricter requirements but must not silently weaken security, review, testing, or traceability controls.

## 2. Priority order

When requirements conflict, apply the following order:

1. applicable law, regulation, contract, and authorized security directive;
2. approved corporate governance and data-classification policy;
3. repository-specific architecture and operational requirements;
4. this organization standard;
5. language or framework convention;
6. individual preference.

Escalate unresolved conflicts. Do not guess.

## 3. Core principles

All production-relevant work must be:

- **Correct** — satisfies explicit requirements and handles failure states.
- **Secure** — uses least privilege, secure defaults, and validated boundaries.
- **Traceable** — links changes to approved work and preserves review evidence.
- **Maintainable** — clear ownership, modular design, tests, and documentation.
- **Observable** — failures can be detected, diagnosed, and acted upon.
- **Reproducible** — dependencies, builds, and deployment inputs are controlled.
- **Reversible** — material changes have a tested rollback or recovery path.
- **Data-conscious** — collection, access, retention, and logging are minimized.

## 4. Repository baseline

Each active repository should contain or inherit:

- `README.md`;
- `CONTRIBUTING.md`;
- `SECURITY.md`;
- `SUPPORT.md`;
- issue and pull-request templates;
- `CODEOWNERS`;
- an approved license or proprietary notice;
- automated CI;
- dependency lockfiles where supported;
- documented configuration and environment variables;
- a release, deployment, and rollback process when production-relevant.

Archived repositories must be marked archived, identify their successor when one exists, and must not appear active.

## 5. Architecture and design

### 5.1 Boundaries

- Separate presentation, domain logic, persistence, and external integrations where complexity warrants.
- Keep business rules out of transport and UI layers.
- Define interfaces for external systems and unstable dependencies.
- Avoid circular dependencies and hidden global state.
- Prefer explicit data flow and dependency injection over implicit coupling.

### 5.2 Decision records

Create an architecture decision record for material decisions involving:

- system boundaries;
- data model or storage technology;
- authentication and authorization;
- external platforms or strategic dependencies;
- irreversible migrations;
- material cost, security, or operational tradeoffs.

A decision record must state context, decision, alternatives, consequences, owner, and date.

### 5.3 Simplicity

Use the simplest design that satisfies verified requirements. Do not add abstraction, distributed infrastructure, frameworks, or dependencies for speculative future needs.

## 6. Coding standards

### 6.1 General

- Use descriptive names and consistent terminology.
- Keep functions and modules focused.
- Prefer explicit error handling.
- Eliminate dead code and commented-out implementations.
- Avoid duplicated business rules.
- Use immutable data where practical.
- Represent money with decimal or integer minor units, never binary floating point.
- Represent timestamps in ISO 8601 and store timezone-aware values.
- Validate external data at trust boundaries.
- Use structured types or schemas for material records.

### 6.2 Comments

Comments must explain:

- why a non-obvious decision exists;
- security or compliance constraints;
- invariants and edge cases;
- external-system behavior;
- temporary limitations with a linked issue.

Do not use comments to restate obvious syntax or preserve obsolete code.

### 6.3 Error handling

- Fail closed for authorization and security controls.
- Return actionable errors without exposing secrets or internals.
- Preserve the original cause for diagnostics.
- Do not catch broad exceptions without a documented reason.
- Define retry, timeout, idempotency, and circuit-breaking behavior for network operations.
- Distinguish user error, validation error, transient failure, dependency failure, and internal defect.

## 7. Language baselines

### 7.1 Node.js and TypeScript

- Use a supported Node.js LTS release.
- Commit the package-manager lockfile.
- Enable TypeScript strict mode for new TypeScript projects.
- Use ESLint or an approved equivalent.
- Avoid `any`; document unavoidable uses.
- Validate runtime input because TypeScript types do not exist at runtime.
- Use `npm ci` or the package manager's frozen-lockfile equivalent in CI.
- Review lifecycle scripts and dependency provenance.
- Do not use dynamic code execution such as `eval` for untrusted data.

Recommended `tsconfig.json` controls include:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "useUnknownInCatchVariables": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

### 7.2 Python

- Use a supported CPython release.
- Use `pyproject.toml` for new packages.
- Use Ruff or approved equivalents for linting and formatting.
- Use type annotations for public interfaces and material domain logic.
- Use `pytest` or an approved test framework.
- Pin or lock production dependencies through an approved tool.
- Do not use mutable default arguments.
- Avoid `pickle` or unsafe deserialization for untrusted data.
- Use `Decimal` for monetary arithmetic.

## 8. Security

### 8.1 Secrets

- Never commit secrets, credentials, tokens, private keys, or production `.env` files.
- Use approved secret stores and short-lived credentials where possible.
- Rotate a secret immediately if exposed; deleting it from the latest commit is insufficient.
- Restrict GitHub Actions permissions explicitly.
- Pin third-party actions to an approved major version or immutable commit under the repository's supply-chain policy.
- Review workflows that can execute code from forks or untrusted pull requests.

### 8.2 Access control

- Apply least privilege.
- Enforce authorization server-side.
- Deny by default.
- Separate authentication from authorization.
- Check object-level authorization for every protected resource.
- Log material access and administrative actions without logging sensitive values.

### 8.3 Input and output

- Validate type, length, format, range, and allowed values.
- Use parameterized database queries.
- Encode output for the destination context.
- Restrict file paths and archive extraction.
- Enforce upload size, content type, and storage controls.
- Protect against server-side request forgery by allowlisting destinations where feasible.

### 8.4 Cryptography

Use current, reviewed libraries and platform primitives. Do not design custom cryptographic algorithms. Encryption keys must be managed separately from encrypted data.

## 9. Data and privacy

- Classify data before storage or integration.
- Collect only required fields.
- Define owner, purpose, retention, and deletion behavior.
- Avoid production data in development and tests.
- Mask or synthesize test data.
- Encrypt sensitive data in transit and at rest.
- Review data exports, analytics, logs, and backups for unintended disclosure.
- Document migrations and reconciliation checks.

## 10. Dependencies and supply chain

Before adding or materially upgrading a dependency, assess:

- necessity;
- publisher and repository authenticity;
- maintenance activity;
- vulnerability history;
- license;
- transitive dependencies;
- release integrity;
- runtime and bundle impact;
- replacement and removal cost.

Automated update pull requests require the same review and testing as human-authored changes.

## 11. Testing

Use a risk-based test strategy.

Required categories where applicable:

- unit tests for business rules;
- integration tests for databases and external boundaries;
- contract tests for APIs and events;
- end-to-end tests for critical user workflows;
- regression tests for corrected defects;
- authorization and validation tests;
- migration and rollback tests;
- resilience tests for timeouts, retries, and dependency failures.

Tests must be deterministic, isolated, readable, and safe to run. Flaky tests must be corrected or quarantined with an owner and expiry.

Coverage percentage is an indicator, not proof of quality. Critical logic requires direct assertions regardless of aggregate coverage.

## 12. Observability

Production services must define:

- structured logs;
- stable event and correlation identifiers;
- health and readiness behavior;
- relevant metrics and service-level indicators;
- alert ownership and runbooks;
- retention and access controls.

Logs must not contain passwords, tokens, private keys, full payment data, or unnecessary personal or confidential information.

## 13. Performance and reliability

- Establish measurable requirements before optimization.
- Measure representative workloads.
- Avoid unbounded queries, queues, recursion, retries, and memory growth.
- Set timeouts for external operations.
- Design retries with backoff, jitter, idempotency, and limits.
- Document capacity assumptions and failure behavior.
- Prefer graceful degradation over silent corruption.

## 14. APIs and compatibility

- Use consistent resource and error models.
- Validate requests and responses.
- Document authentication, authorization, limits, pagination, and idempotency.
- Do not make breaking changes without an approved versioning and migration plan.
- Deprecations require notice, replacement guidance, and a defined removal date.

## 15. Documentation

Update documentation in the same pull request as the change.

Document:

- purpose and scope;
- setup and prerequisites;
- configuration and secrets interface;
- architecture and dependencies;
- normal operation;
- failure modes and troubleshooting;
- deployment and rollback;
- ownership and support;
- data and security considerations.

Commands must be tested. Examples must not contain real secrets or confidential records.

## 16. CI/CD

CI must:

- run on pull requests to protected branches;
- use minimal `GITHUB_TOKEN` permissions;
- use reproducible dependency installation;
- run linting, tests, and build validation;
- prevent deployment from unreviewed pull-request code;
- separate build and deployment authorization;
- retain only necessary artifacts;
- avoid printing secrets;
- fail clearly and actionably.

Production deployment must use approved environments, reviewers, and rollback controls where available.

## 17. Reviews

Pull requests require review appropriate to risk.

Reviewers must examine:

- requirement fit;
- correctness and edge cases;
- security and data handling;
- tests;
- architecture and maintainability;
- operational readiness;
- migration and rollback;
- documentation;
- dependency and license impact.

High-risk changes require relevant domain, security, data, or operations review.

## 18. Prohibited practices

Unless explicitly approved and documented:

- direct pushes to protected branches;
- shared personal credentials;
- secrets in code or CI variables visible to untrusted jobs;
- disabling security controls to pass CI;
- unreviewed production changes;
- force-pushing shared protected branches;
- hidden data collection;
- production data in public or developer test fixtures;
- binary floating-point monetary calculations;
- silent exception suppression;
- undocumented destructive migrations;
- dependencies with unknown source or incompatible license.

## 19. Exceptions

An exception must include:

- requirement being waived;
- reason;
- risk;
- compensating controls;
- owner;
- approver;
- start date;
- expiry or review date;
- linked issue or decision record.

Expired exceptions are invalid.
