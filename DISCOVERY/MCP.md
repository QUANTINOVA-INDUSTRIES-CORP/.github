# Discovery — Staged MCP Control Plane (branch REFACTOR/MCP-CONTROL-PLANE, PR #6)

Date: 2026-09-05

PR #6 (`QUANTINOVA-INDUSTRIES-CORP/.github#6`, DRAFT, author `ceobetch`) is real, open, and contains genuine prior work — not a stub. Inspected every file named in the task brief:

- `MCP/SERVER.py` — a working FastMCP (`mcp[cli]`) Streamable-HTTP server. Already implements: `qic_directive_get`, `gitlab_whoami`, `gitlab_project_search`, `gitlab_project_get`, `gitlab_file_read` (read tools), and `gitlab_branch_create`, `gitlab_file_write`, `gitlab_merge_request_create` (mutation tools). Mutation gate: `QIC_ENABLE_MUTATIONS` env var + protected-branch check (`main`/`master`) + client-supplied `owner_approved: bool` argument. No merge tool, no admin/sudo tools, no credential-exposing tools — matches the brief's prohibitions.
- `MCP/README.md` — accurately documents the security model, deployment gate, and exposed tools; already forbids PAT exposure in any client-visible surface.
- `MCP/pyproject.toml` — pins `httpx` and `mcp[cli]`, Python `>=3.11`, uses `uv`.
- `templates/.mcp.json` — points at `https://mcp.quantinovaindustries.org/mcp` with `CF-Access-Client-Id`/`CF-Access-Client-Secret` header env expansion; contains no secrets.
- `templates/CLAUDE.md`, `templates/AGENTS.md` — already model-independent (harness-agnostic), already require directive sync before repository mutation, already forbid AI attribution and PAT exposure, already gate merge/mutation on explicit owner approval.
- `docs/REPOSITORY_BASELINE.md` — already lists `.mcp.json` as a required per-repo baseline file inherited from this template.

**Conclusion: this is a legitimate, carefully-written first draft. Nothing here needs redesigning.** The gaps against the fuller task brief are additive, not corrective:

1. **Owner-approval model (brief §7):** the brief explicitly calls out that a client-supplied `owner_approved: bool` is not, by itself, sufficient authorization — exactly what `SERVER.py` currently relies on for its second gate (on top of the server-side `QIC_ENABLE_MUTATIONS` env flag). Needs a real server-side approval boundary. See in-conversation question.
2. Missing operational files the brief asks for: `MCP/CAPABILITIES.json`, `MCP/DIRECTIVE.md`, `MCP/SECURITY.md`, `MCP/DEPLOYMENT.md`, `MCP/OPERATIONS.md`, `MCP/TESTING.md`, `MCP/ROLLBACK.md`, `MCP/systemd/qic-mcp.service`.
3. No health endpoint yet (needs a `/health`-style route on the same ASGI app, excluding secrets).
4. No structured audit logging yet.
5. `CHATGPT/` integration package does not exist yet — needs research into the current (2026) OpenAI-supported integration surface before scaffolding.
6. Not yet deployed anywhere — homelab has no `/srv/qic-mcp`, no systemd unit, no env file.
7. `mcp.quantinovaindustries.org` DNS/tunnel routing is currently broken (dangling — see `CLOUDFLARE.md`).

Directive version in the staged code is already `2026-09-05.2` (the brief's example was `2026-09-05.1` — the staged code already incremented past the brief's example, consistent with this being active, evolving work rather than a fresh scaffold).
