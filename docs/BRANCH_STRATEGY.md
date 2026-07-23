# Branch Strategy

## 1. Model

QUANTINOVA INDUSTRIES CORP uses a protected-main, short-lived branch strategy based on GitHub Flow, with optional controlled release branches where a repository requires staged releases.

This approach is preferred over long-lived Git Flow branches for most repositories because it reduces divergence, integration risk, and unreviewed change accumulation.

> CI and workflow automation are **local-only** and are never committed to the organization.
> Where this document references "required status checks", validation is performed locally before
> review; org-side gating relies on pull-request review and code-owner approval, plus any status
> checks a repository configures independently.

## 2. Permanent branches

### `main`

`main` is the authoritative integration branch.

Requirements:

- always protected;
- no direct pushes;
- pull request required;
- required CI checks must pass;
- required reviewers and code owners must approve;
- conversations must be resolved;
- force pushes and deletion must be blocked;
- deployments must use a separate approved environment or release process.

The repository may define `main` as continuously deployable or release-ready. That decision must be documented.

### Release branches

Use `RELEASE/<VERSION_OR_PERIOD>` only when the repository must stabilize a release independently of ongoing development.

Examples:

```text
RELEASE/2.4.0
RELEASE/2026-07
```

Release branches must be temporary. Only release blockers, versioning, release notes, and approved stabilization changes may be added.

Every release-branch fix must also be merged or cherry-picked back to `main`.

## 3. Working branches

Format:

```text
<TYPE>/<SUBJECT>            or            <TYPE>/<ISSUE_ID>_<SUBJECT>
```

Branch names are UPPERCASE with underscores. `<TYPE>` is UPPERCASE; `<SUBJECT>` uses
`UPPER_SNAKE_CASE`. Include the issue or work-item id as the first subject segment when available.

Examples:

```text
FEAT/184_SUPPLIER_DUPLICATE_CHECK
FIX/231_MARGIN_ROUNDING
DOCS/GITHUB_STANDARDIZATION
SECURITY/302_RESTRICT_WORKFLOW_PERMISSIONS
```

Approved types:

| Prefix | Use |
|---|---|
| `FEAT/` | New user or business capability |
| `FIX/` | Defect correction |
| `DOCS/` | Documentation-only change |
| `REFACTOR/` | Behavior-preserving structural change |
| `TEST/` | Test-only change |
| `CHORE/` | Maintenance or tooling |
| `SECURITY/` | Approved security remediation |
| `HOTFIX/` | Urgent production correction |
| `RELEASE/` | Controlled release preparation |
| `EXPERIMENT/` | Time-boxed, non-production experiment |

Rules:

- use UPPERCASE `<TYPE>` and `UPPER_SNAKE_CASE` `<SUBJECT>`;
- include the issue or work-item identifier when available;
- keep the subject concise and meaningful;
- do not use personal names;
- do not reuse a merged branch name for unrelated work;
- do not store multiple unrelated work items in one branch.

> Note: branch names are UPPERCASE (`<TYPE>/<SUBJECT>`); **commit messages remain lowercase
> Conventional Commits** (`feat:`, `fix:`, `docs:`). The two conventions are intentionally different.

## 4. Standard workflow

```bash
git switch main
git pull --ff-only
git switch -c FEAT/184_SUPPLIER_DUPLICATE_CHECK

# Work in small, coherent commits.

git fetch origin
git rebase origin/main
git push --set-upstream origin FEAT/184_SUPPLIER_DUPLICATE_CHECK
```

Open a draft pull request when early feedback is useful. Mark it ready only after the author checklist and required validation are complete.

## 5. Keeping a branch current

Prefer rebasing a private working branch onto `origin/main` before review:

```bash
git fetch origin
git rebase origin/main
```

Do not rebase a shared branch without coordinating with all contributors.

After review has materially started, avoid unnecessary history rewriting. Use the repository's approved update method.

Never force-push protected branches. When a force-push to a personal working branch is necessary after rebase, use:

```bash
git push --force-with-lease
```

Do not use unrestricted `--force`.

## 6. Pull-request scope

A branch and pull request must represent one coherent change.

Split work when it contains:

- unrelated defects or features;
- independent migrations;
- broad formatting mixed with behavior changes;
- generated output unrelated to the approved change;
- infrastructure and application changes that require different approval paths.

Large changes should be decomposed into safe, reviewable increments while preserving compatibility.

## 7. Merge strategy

### Default: squash merge

Use squash merge when the pull request represents one logical change. The squash commit must follow Conventional Commits.

Advantages:

- clean default-branch history;
- easy reversion;
- one work item per commit;
- removal of intermediate fixup commits.

### Rebase merge

Use rebase merge only when each commit is independently meaningful, validated, and compliant.

### Merge commits

Use merge commits only when preserving branch topology has documented value, such as coordinated release integration. Avoid routine use.

Repositories must document their enabled merge methods.

## 8. Hotfixes

Use `HOTFIX/<ISSUE_ID>_<SUBJECT>` for an urgent correction to production.

Process:

1. Confirm incident or emergency authorization.
2. Branch from the exact production source, normally the release tag or `main`.
3. Make the smallest safe correction.
4. Add or update a regression test.
5. Perform expedited but real review and CI.
6. Deploy through the approved emergency process.
7. Merge the correction into every affected maintained branch.
8. document the incident, deployment, and follow-up work.

Urgency does not authorize bypassing security, audit, or approval controls.

## 9. Release tags

Use immutable annotated tags:

```text
vMAJOR.MINOR.PATCH
```

Example:

```text
v2.4.1
```

Create tags from an approved commit after required checks and approvals. Do not move or reuse a published release tag. Correct an error with a new version.

## 10. Branch protection baseline

Protect `main` and maintained release branches with:

- pull requests required;
- at least one approval, increased by repository risk;
- code-owner review where configured;
- dismissal of stale approvals after material changes;
- required status checks;
- conversation resolution;
- restricted direct pushes;
- blocked force pushes;
- blocked deletion;
- linear history where compatible with the merge policy;
- signed commits where required by repository policy.

Administrators should follow the same controls except during a documented emergency.

## 11. Branch lifecycle

- Delete merged working branches.
- Close and delete abandoned branches after preserving required work or decisions.
- Review stale branches regularly.
- Do not treat branches as backups.
- Do not retain confidential exports or generated artifacts in branches.

## 12. Experiments

`EXPERIMENT/` branches must be time-boxed and must not deploy to production. An experiment moving toward production requires an approved issue, normal branch type, production-quality tests, security review, and documentation.

## 13. Exceptions

Any long-lived branch or deviation must document purpose, owner, synchronization method, merge policy, protection rules, and review date.
