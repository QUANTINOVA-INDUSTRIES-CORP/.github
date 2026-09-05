# Test Plan — ChatGPT Integration

## What can be verified without a live ChatGPT account (done in this session)

- [x] `/sse` mount exists on the same listener as `/mcp`, serving the same tool set, verified
      against the pinned MCP Python SDK's actual `FastMCP.sse_app()` implementation (not assumed).
- [x] The five read-only tools ChatGPT would call are the same, already-tested tools Claude Code
      uses — no separate/duplicate implementation to diverge or drift.
- [x] The GitLab PAT boundary is enforced by `SERVER.py` itself (see `MCP/SECURITY.md`), so it
      holds regardless of how ChatGPT authenticates or is configured.

## What requires a live ChatGPT account (not performed in this session)

- [ ] Enable Developer Mode in the CEO's ChatGPT account (Settings → Connectors → Developer Mode).
- [ ] Add `https://mcp.quantinovaindustries.org/sse` (confirm exact path/trailing-slash requirement
      against current OpenAI documentation at the time this is attempted) as a custom connector.
- [ ] Complete whichever OAuth flow Cloudflare Access (or the fallback in `AUTH.md`) presents.
- [ ] Confirm ChatGPT lists exactly the five read-only tools and no others.
- [ ] Call `qic_directive_get` from ChatGPT and confirm the directive text matches
      `MCP/DIRECTIVE.md`.
- [ ] Call `gitlab_whoami`, `gitlab_project_search`, `gitlab_project_get`, `gitlab_file_read` from
      ChatGPT and confirm correct results.
- [ ] Confirm ChatGPT cannot see or call any mutation tool.
- [ ] Confirm no PAT, Cloudflare token, or other secret ever appears in ChatGPT's visible tool
      output or the conversation.

## Owner action required

Everything in the second list requires the CEO's own interactive ChatGPT session and cannot be
completed by an agent. This is the "genuinely inaccessible from this machine" step referenced in
the final report.
