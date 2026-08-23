# Review Policy

Agent-specific review requirements on top of the human review baseline already defined in
`STANDARDS.md` §17 and the protected-branch controls in `BRANCH_STRATEGY.md` §10. Those two
documents remain the general review standard; this document adds only what changes when an
agent, rather than a human, authors the change.

## 1. Requirement

A change authored by Claude is reviewed by Codex, or by a human, before promotion to `main`.
Claude does not self-approve or self-merge its own pull requests.

## 2. What Codex checks

Per `AGENT_POLICY.md` §1: correctness against the stated scope, architecture fit, duplication,
unsafe imports, naming-policy compliance (`NAMING_STANDARD.md`, `IDENTITY_NAMING_POLICY.md`),
dead code, excessive dependencies, exposed secrets, and provenance/license compliance for any
cherry-picked material.

## 3. Labeling the review state

Use `status:` and `review:` labels (`LABEL_POLICY.md` §2, §7) to make review state visible
without relying on chat history: `status:review` while Codex or a human is reviewing,
`status:approved` once cleared, `review:codex` or `review:human` identifying who performed it.

## 4. No auto-merge

No agent merges to a protected branch automatically during the base-build phase
(`AGENT_POLICY.md` §3). A pull request without an explicit human or Codex approval stays open.

## 5. Scope discipline

A reviewed change must have a clear, single scope; agent attribution (`agent:` label); a
provenance entry when it imports material; no exposed secrets; and no unrelated file churn.
Reject or request a split for changes that fail this, per `BRANCH_STRATEGY.md` §6.
