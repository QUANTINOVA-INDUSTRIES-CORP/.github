# Identity Naming Policy

This document governs the human-facing **display name** versus the **technical path/slug** for
the QIC organization, groups, subgroups, and projects/repositories — on both GitHub and the
self-hosted GitLab CE instance. It is a distinct concern from `NAMING_STANDARD.md`, which
governs file, folder, branch, and commit naming *inside* a repository. Do not conflate the two.

## 1. Principle

Display name and technical slug are different concerns and change independently. A display-name
change must never cascade into a path, URL, or remote change "to make it pretty."

## 2. Top level

| | Value |
|---|---|
| Branded / human-facing name | QIC |
| Technical path | `qic` |

The technical path `qic` does not change.

## 3. GitLab — current state

| | Value |
|---|---|
| Group display name | QIC |
| Group path | `qic` |

Both confirmed current as of this policy's introduction.

## 4. GitLab — subgroup naming rule (target, not yet applied)

When subgroups are introduced under the `qic` group, the rule is:

| | Convention | Example |
|---|---|---|
| Subgroup display name | Title Case | Data Platform |
| Subgroup path | lowercase, kebab-case | `data-platform` |

**This rule is not yet applied.** The current GitLab state has nine domain skeletons as flat
projects directly under the `qic` group (for example `qic/qic-data-platform`), not as subgroups
(`qic/data-platform`). Converting to subgroups would require creating each subgroup and
transferring the corresponding project into it, which changes that project's `full_path` and
therefore every clone URL and configured remote pointing at it. That is a migration, not a
cosmetic rename, and is out of scope for base-build governance normalization. It requires an
explicit, separately authorized migration plan before execution.

## 5. Project / repository paths

Lowercase, kebab-case, unless a verified existing canonical path must be preserved for
compatibility. Do not cascade-rename an existing project's path, URL, or Git remote solely for
naming consistency — only as part of an explicit, authorized migration.

## 6. GitHub

| | Value |
|---|---|
| Organization display name | QUANTINOVA INDUSTRIES CORP |
| Organization slug | `QUANTINOVA-INDUSTRIES-CORP` |

Repository slugs follow the pattern already established across the organization
(`qic-<domain>` or `qic_<domain>`, per repository). Do not rename an existing repository slug to
enforce consistency; apply the lowercase kebab-case convention to new repositories going
forward.
