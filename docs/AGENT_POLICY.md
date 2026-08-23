# Agent Policy

Rules for AI-agent participation in QUANTINOVA INDUSTRIES CORP repositories. See
`GOVERNANCE.md` for the operating model these roles sit inside, and `STANDARDS.md` §17 /
`BRANCH_STRATEGY.md` for the human review and branch controls every agent-authored change must
still pass.

## 1. Roles

### Claude — builder / curator / implementation owner

- May write to task branches following `BRANCH_STRATEGY.md`.
- May open pull requests.
- Must not merge to a protected branch automatically. A human, or an explicitly authorized
  review step, promotes the change.
- Owns provenance recording for any cherry-picked or imported material (`PROVENANCE_POLICY.md`).

### Codex — reviewer / verifier

- Reviews Claude's diffs for correctness, architecture fit, duplication, unsafe imports, naming
  violations, dead code, excessive dependencies, secrets, and policy violations.
- Does not become the primary builder during the base-build phase. Codex may write only when a
  task is explicitly assigned to it outside the reviewer role.

### AGY — organization auditor

- Read-only. Inspects repositories, structure, files, technology, staleness, duplication, and
  reusable assets across the QIC GitHub organization.
- Produces findings only — no edits, commits, pushes, pull requests, deletions, branch changes,
  CI/CD changes, issue/secret changes, GitHub setting changes, or migrations.
- Excludes MCP experimentation, harness prototypes, and temporary orchestration repositories
  from the canonicalization scope unless a non-MCP repository depends on one directly, in which
  case the dependency is noted, not removed.

### Sean's Agent — control-plane / operations-hub builder

- Consumes the stabilized canonical repositories and policies produced by Phases A–G.
- Does not build against unnormalized source repositories.
- Write access opens only when the control-plane build phase is explicitly opened.

## 2. Commit and change attribution

Every agent-generated change must carry, via labels on its issue or pull request:

- an `agent:` tag identifying which agent produced the change (`agent:claude`, `agent:codex`,
  `agent:agy`, `agent:sean`);
- a `source:` tag when the change contains imported or cherry-picked material;
- a `scope:` tag identifying the affected area;
- a `status:` tag reflecting current state.

See `LABEL_POLICY.md` for the full taxonomy. No anonymous agent-generated commits — every
change must be traceable to the agent and role that produced it.

Commit messages themselves follow `COMMIT_CONVENTIONS.md` and `NAMING_STANDARD.md` hygiene:
lowercase Conventional Commits, no AI attribution in the message body, metadata, or frontmatter.
Attribution lives in labels and pull-request metadata, not in the commit text.

## 3. No automatic merges

No agent — Claude, Codex, Sean's Agent, or any future agent — merges to `main` or another
protected branch automatically during the base-build phase. Promotion requires the review and
approval controls already defined in `BRANCH_STRATEGY.md` §10.
