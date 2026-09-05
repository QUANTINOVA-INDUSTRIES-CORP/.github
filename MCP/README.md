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
```

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

The MCP SDK serves Streamable HTTP at `/mcp` on its configured local listener. Keep the listener
private and publish it only through the existing CLOUDFLARE TUNNEL / ACCESS path.

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
creation require `owner_approved=true`, and file mutation is blocked on `main` and `master`.

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
2. Verify `gitlab_whoami` returns the intended GitLab identity.
3. Create the CLOUDFLARE DNS/TUNNEL route for `mcp.quantinovaindustries.org`.
4. Protect the hostname with CLOUDFLARE ACCESS.
5. Test `qic_directive_get` from CLAUDE CODE.
6. Test read-only GitLab tools.
7. Test mutation only on a disposable non-default branch with explicit owner approval.
8. Roll the `.mcp.json`, `CLAUDE.md`, and `AGENTS.md` templates into active repositories.
