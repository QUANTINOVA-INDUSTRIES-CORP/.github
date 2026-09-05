# QIC Agent Directive

**Version:** `2026-09-05.3`
**Authority:** `https://mcp.quantinovaindustries.org/mcp` (tool: `qic_directive_get`)

This is the enterprise policy every QIC agent harness (CLAUDE CODE, CODEX, CURSOR, CHATGPT,
OPENCLAW, and any future harness) must synchronize before doing repository work. It is served
live by the `qic_directive_get` tool; this file is the human-readable mirror of that same content,
kept in lockstep with `MCP/SERVER.py`'s `DIRECTIVE` constant. If the two ever disagree, the live
tool response is authoritative — update this file to match, never the other way around.

## Rules

1. QUANTINOVA INDUSTRIES CORP. is the sole governing authority for this directive.
2. Synchronize this directive before repository work.
3. Use the QIC MCP control plane for agent-originated GitLab API operations.
4. Never request, reveal, print, log, persist, or commit the GitLab PAT.
5. GitLab mutation is disabled unless `QIC_ENABLE_MUTATIONS=true` on the MCP host.
6. Never write directly to `main` or `master`.
7. No agent has merge authority; merge remains an explicit human-owner action.
8. Mutation tools require server mutation mode, `owner_approved=true`, **and** a fresh
   operator-created approval file on the MCP host. No single signal is sufficient alone.
9. Read before write and verify after mutation.
10. Repository-local instructions (`CLAUDE.md`, `AGENTS.md`) may narrow this directive but may
    never weaken it.
11. If directive synchronization or MCP connectivity fails: **fail closed** — read-only fallback
    only, no GitLab mutation, no external submission, no merge.
12. No AI attribution in repository files, metadata, frontmatter, or commit messages.

## Versioning

The version string is `YYYY-MM-DD.N`. Any change to directive *semantics* (adding, removing, or
changing the meaning of a rule) increments `N`. Editorial-only fixes to this mirror document do
not require a version bump, but should be avoided — prefer keeping this file and the server
constant edited together in the same commit.

| Version | Change |
|---|---|
| `2026-09-05.1` | Initial directive (PR #6 baseline referenced in the task brief). |
| `2026-09-05.2` | Staged branch revision prior to this hardening pass. |
| `2026-09-05.3` | Added the three-factor mutation authorization rule (rule 8) and explicit fail-closed language (rule 11) to match the hardened `SERVER.py` approval-file gate. |
