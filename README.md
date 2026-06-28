# QUANTINOVA INDUSTRIES CORP — Organization GitHub Standards

This repository is the organization-wide GitHub configuration repository for **QUANTINOVA INDUSTRIES CORP**.

When this repository is named `.github`, is owned by the `QUANTINOVA-INDUSTRIES-CORP` organization, and is public, GitHub can use its supported community-health files, issue templates, pull-request template, workflow templates, and organization profile across repositories that do not provide repository-specific overrides.

> [!IMPORTANT]
> This repository contains public governance and engineering templates only. Do not commit credentials, client records, procurement data, pricing, internal architecture diagrams, personal information, or other confidential material.

## Repository purpose

This repository provides:

- organization profile content;
- default issue forms and pull-request guidance;
- default contribution, conduct, security, and support policies;
- organization workflow templates for Node.js/TypeScript, Python, and security scanning;
- reference coding, branching, and commit standards;
- starter `.gitignore` templates;
- a documented `CODEOWNERS` pattern.

Repository-specific requirements take precedence when a repository contains its own corresponding file.

## Required repository settings

Configure the repository as follows:

| Setting | Required value |
|---|---|
| Owner | `QUANTINOVA-INDUSTRIES-CORP` |
| Repository name | `.github` |
| Visibility | **Public** |
| Default branch | `main` |
| Direct pushes to `main` | Blocked |
| Pull-request reviews | Required |
| Conversation resolution | Required |
| Force pushes and branch deletion | Blocked |
| Secret scanning and push protection | Enabled where available |
| Dependency graph and Dependabot alerts | Enabled where available |

## Structure

```text
.
├── README.md
├── profile/
│   └── README.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── config.yml
│   └── pull_request_template.md
├── workflow-templates/
│   ├── ci-node.yml
│   ├── ci-node.properties.json
│   ├── ci-python.yml
│   ├── ci-python.properties.json
│   ├── security-scan.yml
│   └── security-scan.properties.json
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── SUPPORT.md
├── CODEOWNERS
├── .gitignore-node
├── .gitignore-python
└── docs/
    ├── STANDARDS.md
    ├── BRANCH_STRATEGY.md
    └── COMMIT_CONVENTIONS.md
```

> [!NOTE]
> Organization workflow templates must be stored in the root-level `workflow-templates/` directory. They must not be placed under `.github/workflow-templates/`.

## How GitHub applies these files

### Organization profile

`profile/README.md` appears on the public organization profile.

### Default community-health files

Supported files in this repository act as defaults for organization repositories that do not contain their own equivalent file. A repository-level file overrides the organization default.

### Issue templates

The files in `.github/ISSUE_TEMPLATE/` are inherited only when a target repository does not define its own issue-template configuration. Labels referenced by inherited issue forms must already exist in the target repository; these templates therefore avoid mandatory label dependencies.

### Workflow templates

The files in `workflow-templates/` appear in the Actions workflow template chooser for organization repositories. The `$default-branch` token is replaced by GitHub when a template is adopted.

Workflow templates are starters, not centrally executed reusable workflows. After adding a template to a repository, maintainers must review runtime versions, dependency-manager assumptions, permissions, secrets, and repository-specific commands.

## Adoption procedure

1. Create the public `QUANTINOVA-INDUSTRIES-CORP/.github` repository.
2. Add this file set on a feature branch.
3. Replace approved placeholders such as `[PROJECT_NAME]` and `[SECURITY_CONTACT_EMAIL]`.
4. Validate Markdown, YAML, JSON, and workflow syntax.
5. Confirm referenced GitHub teams exist and have the required repository permissions before activating `CODEOWNERS` rules.
6. Open a pull request and require review.
7. Merge only after security and governance approval.
8. Test inheritance in a non-critical repository before organization-wide reliance.

## Maintenance

- Review action major versions and supported runtime versions at least quarterly.
- Review this repository after material GitHub platform changes.
- Use pull requests for every change.
- Record breaking governance changes in the pull-request description.
- Keep templates general. Put repository-specific commands in the target repository.
- Never weaken security controls solely to make a workflow pass.

## Placeholder policy

Placeholders use square brackets, for example:

- `[PROJECT_NAME]`
- `[REPOSITORY_NAME]`
- `[DESCRIPTION]`
- `[SECURITY_CONTACT_EMAIL]`
- `[SUPPORT_CHANNEL]`

A placeholder must be replaced before the related instruction is treated as operational. Unresolved placeholders must not be interpreted as approved contacts, owners, service levels, or production settings.

## License and use

Unless a separate license file states otherwise, this repository and its contents are proprietary to **QUANTINOVA INDUSTRIES CORP**. External use, redistribution, or modification requires written authorization.
