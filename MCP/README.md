# QIC MCP Control Plane

Canonical agent control plane for QUANTINOVA INDUSTRIES CORP.

## Endpoints

- MCP: `https://mcp.quantinovaindustries.org/mcp`
- GitLab upstream: `https://gitlab.quantinovaindustries.org/api/v4`

## Security model

Agent clients authenticate to the MCP edge. They do not receive the GitLab PAT.
The MCP process reads the PAT only from its server environment and sends it to GitLab using the
`PRIVATE-TOKEN` header. The PAT must never be stored in Git, `.mcp.json`, CLAUDE.md, AGENTS.md,
logs, prompts, or tool output.

Required server environment:

```bash
QIC_GITLAB_BASE_URL=https://gitlab.quantinovaindustries.org
QIC_GITLAB_PAT=<SERVER_SIDE_SECRET_ONLY>
QIC_ENABLE_MUTATIONS=false
```

`QIC_ENABLE_MUTATIONS` defaults to `false`. Read-only GitLab tools remain available, but branch,
file-write, and merge-request tools require **three independent factors** before they run:
`QIC_ENABLE_MUTATIONS=true` (restart-gated), the tool call carrying `owner_approved=true`, and a
fresh, single-use approval file created by the operator directly on the MCP host
(`/run/qic-mcp/approve` by default, TTL `QIC_MCP_APPROVAL_TTL_SECONDS`, default 300s). None of the
three is sufficient alone — see `SECURITY.md` for the full rationale and `OPERATIONS.md` for how to
grant a mutation window.

Recommended client/edge authentication is CLOUDFLARE ACCESS using per-device or per-agent service
tokens. The repository template expects these client-side environment variables:

```bash
QIC_CF_ACCESS_CLIENT_ID=<SERVICE_TOKEN_CLIENT_ID>
QIC_CF_ACCESS_CLIENT_SECRET=<SERVICE_TOKEN_CLIENT_SECRET>
```

These CLOUDFLARE credentials authenticate the client to the MCP edge. They are not GitLab
credentials and must be independently revocable.

## Run locally on the HomeLab server

```bash
cd MCP
uv sync
uv run python SERVER.py
```

This serves three routes on one listener (`QIC_MCP_HOST`:`QIC_MCP_PORT`, default
`127.0.0.1:8000`): Streamable HTTP at `/mcp` (Claude Code, Codex, Cursor), SSE at `/sse` (for
ChatGPT-style custom connectors), and a secret-free `/health` check. Keep the listener private and
publish it only through the existing CLOUDFLARE TUNNEL / ACCESS path. `python SERVER.py --stdio`
runs stdio transport instead, for local debugging only.

Example CLOUDFLARE TUNNEL ingress entry:

```yaml
- hostname: mcp.quantinovaindustries.org
  service: http://127.0.0.1:8000
```

Do not add a public router port-forward.

## Claude Code

Copy `templates/.mcp.json` into the project root, set the CLOUDFLARE ACCESS environment variables,
then verify:

```bash
claude mcp get qic-control-plane
```

Inside CLAUDE CODE, `/mcp` should show `qic-control-plane` connected. The first repository action
must call `qic_directive_get`.

## GitLab credential contract

The server-side PAT is the single upstream identity requested for agent GitLab operations. Use only
the scopes required by the enabled tools. The current server needs GitLab API access; do not grant
`sudo` or instance-administration scopes.

The server deliberately exposes no merge tool. Branch creation, file mutation, and merge-request
creation require both server mutation mode and `owner_approved=true`. Direct file mutation is blocked
on `main` and `master`.

## Exposed tools

- `qic_directive_get`
- `gitlab_whoami`
- `gitlab_project_search`
- `gitlab_project_get`
- `gitlab_file_read`
- `gitlab_branch_create`
- `gitlab_file_write`
- `gitlab_merge_request_create`

## Deployment gate

Before production routing:

1. Configure `QIC_GITLAB_PAT` only in the MCP service environment.
2. Keep `QIC_ENABLE_MUTATIONS=false` for initial deployment.
3. Verify `gitlab_whoami` returns the intended GitLab identity.
4. Create the CLOUDFLARE DNS/TUNNEL route for `mcp.quantinovaindustries.org`.
5. Protect the hostname with CLOUDFLARE ACCESS.
6. Test `qic_directive_get` from CLAUDE CODE.
7. Test read-only GitLab tools.
8. For a controlled mutation test: enable mutation mode, restart the MCP service, create the
   operator approval file immediately before each mutation call (`OPERATIONS.md`), use a
   disposable non-default branch, then disable mutation mode again.
9. Roll the `.mcp.json`, `CLAUDE.md`, and `AGENTS.md` templates into active repositories.

See `DEPLOYMENT.md` for the full HomeLab procedure, `OPERATIONS.md` for day-2 operations,
`SECURITY.md` for the complete threat model, `TESTING.md` for the test matrix, and `ROLLBACK.md`
to undo any part of this.
