# Architecture

ChatGPT is added as a fourth (fifth, counting future harnesses) consumer of the one existing
control plane — it does not get its own server, its own directive, or its own copy of the GitLab
integration logic.

```
                 CLAUDE CODE ──┐
                 CODEX ────────┤
                 CURSOR ───────┼──▶  mcp.quantinovaindustries.org  ──▶  QIC DIRECTIVE  ──▶  GitLab CE
                 CHATGPT ──────┤        (Cloudflare Tunnel + Access)
                 future ───────┘
```

## What's shared

- The same `MCP/SERVER.py` process, the same tool implementations, the same `DIRECTIVE` constant,
  the same audit log, the same GitLab PAT (never leaves the server).
- The same fail-closed contract: if directive sync fails, ChatGPT — like every other harness — must
  fall back to read-only/local-only behavior. This is enforced by policy (the directive text) since
  ChatGPT (unlike Claude Code) doesn't read a `CLAUDE.md`/`AGENTS.md` bootstrap file automatically;
  the equivalent instruction has to live in the connector's own system-prompt-equivalent
  configuration inside ChatGPT (see `AUTH.md`/`TEST-PLAN.md` for where that's set).

## What's different

- **Transport**: ChatGPT's documented custom-connector path expects an SSE interface
  (conventionally at a path ending `/sse/`), distinct from the Streamable HTTP path
  (`/mcp`) that Claude Code, Codex, and Cursor use. `SERVER.py` now mounts both on the same
  listener (`/mcp` and `/sse`) so one process serves every harness — see `MCP/SERVER.py`'s
  `build_app()`.
- **Authentication**: Claude Code authenticates with a static Cloudflare Access service-token
  header pair set once in an environment variable. ChatGPT's documented connector flow instead
  expects the server to support OAuth (Client ID Metadata Documents or dynamic client
  registration) — a live, per-user authorization handshake, not a static header. See `AUTH.md`.
- **Tool subset**: ChatGPT is initially limited to the five read-only tools (`TOOL-MAPPING.md`).
  Mutation tools exist on the server but are not part of the initial ChatGPT-facing contract; the
  server's own three-factor mutation gate (`MCP/SECURITY.md`) still applies regardless of which
  harness calls them, so this is a belt-and-braces restriction, not the only one.
