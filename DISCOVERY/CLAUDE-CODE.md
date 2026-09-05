# Discovery — Claude Code integration

Date: 2026-09-05

- No `.mcp.json` currently configured for `qic-control-plane` in this Claude Code session/project.
- No `QIC_CF_ACCESS_CLIENT_ID` / `QIC_CF_ACCESS_CLIENT_SECRET` environment variables set locally yet — no Cloudflare Access service token has been minted for this yet (see `CLOUDFLARE.md`).
- Once the Access application + service token exist and the MCP server is deployed and routed, wiring this is: drop `templates/.mcp.json` into the target project, export the two env vars, then `claude mcp get qic-control-plane` and call `qic_directive_get`.
