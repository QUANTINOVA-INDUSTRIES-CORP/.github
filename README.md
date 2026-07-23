# QUANTINOVA INDUSTRIES CORP — Organization GitHub Standards

This repository is the organization-wide GitHub configuration repository for **QUANTINOVA INDUSTRIES CORP (QIC)**.

When this repository is named `.github`, is owned by the `QUANTINOVA-INDUSTRIES-CORP` organization, and is public, GitHub uses its supported community-health files, issue templates, pull-request template, and organization profile as defaults for organization repositories that do not provide repository-specific overrides.

> [!IMPORTANT]
> This repository contains public governance and engineering templates only. Do not commit credentials, client records, procurement data, pricing, internal architecture diagrams, personal information, or other confidential material.

## Repository purpose

This repository provides:

- organization profile content;
- default issue forms and pull-request guidance;
- default contribution, conduct, security, and support policies;
- reference naming, branching, commit, and coding standards;
- drop-in repository templates (`README.md`, `CLAUDE.md`, `AGENTS.md`, starter `.gitignore` files);
- a documented `CODEOWNERS` pattern.

Repository-specific requirements take precedence when a repository contains its own corresponding file.

> [!NOTE]
> QIC does not publish organization workflow templates. CI and workflow automation are local-only and are never committed — see `docs/REPOSITORY_BASELINE.md`, section 3.

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
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   ├── documentation_report.yml
│   │   └── feature_request.yml
│   └── pull_request_template.md
├── docs/
│   ├── BRANCH_STRATEGY.md
│   ├── COMMIT_CONVENTIONS.md
│   ├── NAMING_STANDARD.md
│   ├── REPOSITORY_BASELINE.md
│   └── STANDARDS.md
├── profile/
│   ├── assets/
│   │   ├── QIC_BANNER_DARK.png
│   │   └── QIC_BANNER_LIGHT.png
│   └── README.md
├── templates/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── NODE.gitignore
│   ├── PYTHON.gitignore
│   └── README.md
├── .gitattributes
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CODEOWNERS
├── CONTRIBUTING.md
├── README.md
├── SECURITY.md
└── SUPPORT.md
```

## How GitHub applies these files

### Organization profile

`profile/README.md` appears on the public organization profile.

### Default community-health files

Supported files in this repository act as defaults for organization repositories that do not contain their own equivalent file. A repository-level file overrides the organization default.

### Issue templates

The files in `.github/ISSUE_TEMPLATE/` are inherited only when a target repository does not define its own issue-template configuration. Labels referenced by inherited issue forms must already exist in the target repository; these templates therefore avoid mandatory label dependencies.

## Maintenance and change procedure

1. Make every change on an UPPERCASE working branch (see `docs/BRANCH_STRATEGY.md`) and submit it through a reviewed pull request. Never commit directly to `main`.
2. Replace bracketed placeholders such as `[SECURITY_CONTACT_EMAIL]` only with approved values.
3. Validate Markdown, YAML, links, and structure before requesting review.
4. Confirm referenced GitHub teams exist and have the required repository permissions before activating `CODEOWNERS` rules.
5. Test inheritance in a non-critical repository before organization-wide reliance.
6. Keep templates general; put repository-specific commands in the target repository.
7. Record breaking governance changes in the pull-request description.
8. Review this repository at least quarterly and after material GitHub platform changes.
9. Never weaken security controls.

## Placeholder policy

Placeholders in policy and template files use square brackets, for example:

- `[REPOSITORY_NAME]`
- `[ISSUE_ID]`
- `[SECURITY_CONTACT_EMAIL]`
- `[CODE_OF_CONDUCT_CONTACT]`
- `[SUPPORT_ESCALATION_CHANNEL]`

Drop-in files under `templates/` use `{{DOUBLE_BRACE}}` variables instead; replace every variable when adapting a template.

A placeholder must be replaced before the related instruction is treated as operational. Unresolved placeholders must not be interpreted as approved contacts, owners, service levels, or production settings.

## License and use

Unless a separate license file states otherwise, this repository and its contents are proprietary to **QUANTINOVA INDUSTRIES CORP**. External use, redistribution, or modification requires written authorization.
