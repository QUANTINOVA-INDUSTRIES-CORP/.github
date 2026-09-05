# QIC MCP — Day-2 Operations

## Service management

```bash
sudo systemctl status qic-mcp.service --no-pager
sudo systemctl restart qic-mcp.service
sudo journalctl -u qic-mcp.service -f
```

## Health check

```bash
curl -s http://127.0.0.1:8000/health | jq .
```

Returns `status`, `directive_version`, `build_version`, `gitlab_host`, `mutations_enabled`. Never
returns secrets — safe to check from anywhere on the LAN, and safe to leave world-readable behind
Cloudflare Access if ever needed for uptime monitoring.

## Reading audit events

Every tool call emits one JSON line to stdout, captured by `journald`:

```bash
sudo journalctl -u qic-mcp.service -o cat | grep '"tool"'
sudo journalctl -u qic-mcp.service -o cat | jq -c 'select(.operation_class=="mutation")'
```

Each event: `ts`, `tool`, `operation_class` (`read`/`mutation`), `success`, `project`, `branch`,
`directive_version`, and `error` (truncated, present only on failure). No PAT, no headers, no file
content.

## Enabling a controlled mutation (the three-factor gate)

Mutations require all three factors from `MCP/SECURITY.md`. To perform one deliberately:

```bash
# 1. Flip the global switch and restart (only needed once per mutation "window")
sudo sed -i 's/QIC_ENABLE_MUTATIONS=false/QIC_ENABLE_MUTATIONS=true/' /etc/qic-mcp/qic-mcp.env
sudo systemctl restart qic-mcp.service

# 2. Immediately before EACH mutation call, create the single-use approval file
sudo install -d -m 0750 -o qic-mcp -g qic-mcp /run/qic-mcp
sudo -u qic-mcp touch /run/qic-mcp/approve

# 3. Have the agent make the call with owner_approved=true within QIC_MCP_APPROVAL_TTL_SECONDS (default 300s)

# 4. When the mutation window is done, flip the switch back off and restart
sudo sed -i 's/QIC_ENABLE_MUTATIONS=true/QIC_ENABLE_MUTATIONS=false/' /etc/qic-mcp/qic-mcp.env
sudo systemctl restart qic-mcp.service
```

`/run` is tmpfs, so the approval file also disappears on reboot — nothing to clean up if the
service or host restarts mid-window.

## Rotating credentials

- **GitLab PAT**: generate the replacement in GitLab first, pipe the new value into
  `/etc/qic-mcp/qic-mcp.env` the same way as initial deployment (never through a variable that gets
  echoed), then `sudo systemctl restart qic-mcp.service` and re-run `gitlab_whoami` to confirm.
  Revoke the old token in GitLab only after the new one is confirmed working.
- **Cloudflare Access service token**: rotate from the Cloudflare Zero Trust dashboard/API; update
  the operator machine's `QIC_CF_ACCESS_CLIENT_ID`/`QIC_CF_ACCESS_CLIENT_SECRET` env vars. This never
  touches the MCP host or the GitLab credential.

## Updating the deployed code

```bash
sudo -u qic-mcp git -C /srv/qic-mcp/repo fetch origin REFACTOR/MCP-CONTROL-PLANE
sudo -u qic-mcp git -C /srv/qic-mcp/repo checkout REFACTOR/MCP-CONTROL-PLANE
sudo -u qic-mcp git -C /srv/qic-mcp/repo reset --hard origin/REFACTOR/MCP-CONTROL-PLANE
sudo -u qic-mcp /srv/qic-mcp/.local/bin/uv pip install --python /srv/qic-mcp/.venv/bin/python /srv/qic-mcp/repo/MCP
sudo systemctl restart qic-mcp.service
curl -s http://127.0.0.1:8000/health
```
