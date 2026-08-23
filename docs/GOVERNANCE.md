# Multi-Agent Governance

This document defines the operating model for AI-agent participation in QUANTINOVA INDUSTRIES
CORP repositories during the base-build phase. It supplements, and does not replace,
`STANDARDS.md`, `BRANCH_STRATEGY.md`, and `REPOSITORY_BASELINE.md`.

## 1. Roles

| Agent | Function | Write | Merge |
|---|---|---|---|
| Claude | Builder / curator — implements approved work on task branches | Yes | No automatic merge to protected `main` |
| Codex | Reviewer — inspects diffs, architecture, duplication, security | Review only, unless explicitly tasked otherwise | No |
| AGY | Read-only organization auditor | No | No |
| Sean's Agent | Future control-plane / operations-hub builder | Only once the control-plane build phase is opened | No automatic merge to protected `main` |

Full role detail is in `AGENT_POLICY.md`.

## 2. Execution order for base-build work

1. **Phase A** — GitHub `.github` governance base (this repository).
2. **Phase B** — Normalize labels, templates, and policies against Phase A.
3. **Phase C** — AGY read-only audit of the QIC GitHub organization.
4. **Phase D** — Claude discovery and a curated cherry-pick plan, built from Phase C's findings.
5. **Phase E** — Codex review of the cherry-pick plan.
6. **Phase F** — Claude implements approved curation.
7. **Phase G** — GitLab display/group identity normalization.
8. **Phase H** — Control-plane / operations-hub build, by Sean's Agent.

Phases D–F depend on Phase C being complete. Do not cherry-pick or ingest historical material
into any domain repository before AGY's audit has produced findings and Claude has reconciled
them into RETAIN / ADAPT / REFERENCE / ARCHIVE / REJECT calls, recorded in the relevant
repository's decision log.

## 3. Tooling is visibility, not authority

GitKraken and Kepler (repository/architecture visualization) may be used to inspect branch
state, commit history, and repository structure. They improve visibility only. The source of
truth remains Git and the GitHub/GitLab repository state itself — never a visualization tool's
cached or derived view.

## 4. Escalation

An agent that finds a phase blocked, a role conflict, a naming contradiction, or a decision
outside its authority must stop and report the specific blocker rather than proceeding on an
assumption. Silent scope expansion is not permitted.
