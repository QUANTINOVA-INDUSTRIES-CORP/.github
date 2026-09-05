# QIC × ChatGPT Integration

This package prepares the QIC MCP control plane to be consumed by a custom ChatGPT connector,
using the **same** `https://mcp.quantinovaindustries.org/mcp` control plane, the **same**
directive (`qic_directive_get`), and the **same** underlying tool implementations that Claude Code
and every other harness use. There is no separate ChatGPT-specific policy engine, and ChatGPT never
receives the GitLab PAT.

```
CHATGPT
   │
   ▼
QIC MCP  (https://mcp.quantinovaindustries.org)
   │
   ▼
QIC DIRECTIVE  (qic_directive_get)
   │
   ▼
GITLAB CE
```

## Status

Scaffold and server-side support (an `/sse` mount alongside `/mcp`, matching current OpenAI
connector expectations) are in place. **End-to-end connector setup has not been completed** —
that requires an interactive step inside the CEO's own ChatGPT account (Settings → Connectors →
Developer Mode) that cannot be performed from this session. See `TEST-PLAN.md` for exactly what
was and wasn't verifiable here.

## Files

- `ARCHITECTURE.md` — how ChatGPT fits into the existing control-plane architecture.
- `SECURITY.md` — what ChatGPT can and cannot do, and why.
- `TOOL-MAPPING.md` — the exact tool subset exposed to ChatGPT initially.
- `AUTH.md` — the authentication design and the OpenAI-documentation basis for it.
- `TEST-PLAN.md` — what to verify, and what's already been checked.

## Current OpenAI integration surface (researched 2026-09-05)

OpenAI's Apps SDK is for publishing a reviewed, catalog-listed app with custom UI components —
not needed here, since this is a private, organization-internal integration with plain data tools
and no UI widget. The correct surface for this use case is **ChatGPT Developer Mode with a custom
remote MCP connector**: a user (the CEO) enables Developer Mode in ChatGPT settings and adds our
server's URL directly, without app-catalog review. This matches the brief's instruction to use
the currently-supported mechanism rather than the deprecated ChatGPT plugin architecture (retired).
See `AUTH.md` for the authentication details this implies.
