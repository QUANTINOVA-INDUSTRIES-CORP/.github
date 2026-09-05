# Authentication Design — ChatGPT Connector

## What OpenAI's current documentation says (researched 2026-09-05)

- ChatGPT connects to custom MCP servers over a remote (HTTPS) transport; local `stdio` servers
  are not supported.
- The documented custom-connector authentication options are **OAuth using a Client ID Metadata
  Document (CIMD)** (OpenAI's stated preference where the authorization server supports it) or
  **OAuth dynamic client registration**. This is a live, per-user authorization-code handshake —
  not a static header pair.
- Developer Mode lets a user add a private/internal connector directly by URL, without app-catalog
  review — this is the correct path for an organization-internal tool like this one.
- This is a fast-moving beta surface. **Re-check `developers.openai.com/api/docs/mcp` and the
  ChatGPT Help Center Developer Mode article at connector-setup time** before wiring anything —
  do not assume this document is still current by the time it's acted on.

## Why this differs from the Claude Code approach

Claude Code's `.mcp.json` sends a static `CF-Access-Client-Id` / `CF-Access-Client-Secret` header
pair — simple, because Claude Code is configured once by the operator on a machine the operator
controls. ChatGPT's documented flow instead expects the *server* (or the identity layer in front
of it) to speak OAuth: redirect the user to authenticate, issue a token, and validate that token on
each MCP request. A static header pair is not what ChatGPT's connector setup is built around.

## Recommended approach: Cloudflare Access as the OAuth/OIDC provider

Rather than building and maintaining a bespoke OAuth authorization server inside `SERVER.py`, the
lowest-new-code path is a **second Cloudflare Access application**, in front of the same
`mcp.quantinovaindustries.org` hostname (or a dedicated path/subdomain if Access requires separate
apps not to overlap), configured for **Access for SaaS** (Cloudflare's OIDC-provider mode for
third-party apps) instead of the Service Auth (service-token) mode used for Claude Code. In this
mode:

1. The CEO adds the connector URL in ChatGPT Developer Mode.
2. ChatGPT initiates OAuth; the CEO authenticates through Cloudflare Access's own login (whatever
   identity provider is already configured for the `QIC SSH` / `Warp Login App` Access
   applications).
3. Cloudflare issues an OIDC token to ChatGPT; ChatGPT presents it on each MCP request.
4. Cloudflare Access validates the token at the edge, same as it validates the service token for
   Claude Code today — `SERVER.py` itself does not need to know or care which auth mode fronted the
   request.

**This has not been built or tested in this session** — it requires confirming Cloudflare's current
Access-for-SaaS configuration supports CIMD/dynamic client registration in the exact shape ChatGPT
expects, which needs hands-on testing against a live ChatGPT Developer Mode connector attempt.

## Fallback if Access-for-SaaS doesn't fit

If Cloudflare's OIDC provider mode doesn't satisfy ChatGPT's exact CIMD/dynamic-registration
expectations, the fallback is a minimal OAuth 2.0 authorization-code endpoint added directly to
the `SERVER.py` Starlette app (a `/authorize` and `/token` route implementing just enough of RFC
7591 dynamic client registration for ChatGPT to complete its handshake), issuing short-lived
bearer tokens that gate access to the `/sse` mount only. This is more code to own and was not
built in this session — only recommended as the documented fallback if the Cloudflare-native path
doesn't pan out.

## What never changes regardless of which auth path is chosen

The GitLab PAT stays exactly where it already is — the MCP server's own process environment. Both
auth designs above only gate *reaching the MCP edge at all*; they have no interaction with the
GitLab credential or the mutation gate, which are enforced identically for every harness.
