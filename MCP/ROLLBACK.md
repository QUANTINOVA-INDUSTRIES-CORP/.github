# QIC MCP — Rollback Procedure

Each step is independent — roll back only as much as needed.

## Stop the service (fastest full stop)

```bash
sudo systemctl stop qic-mcp.service
sudo systemctl disable qic-mcp.service
```

The MCP endpoint stops responding immediately; no GitLab credential is reachable from any agent
after this.

## Remove Cloudflare routing

- Delete the `mcp.quantinovaindustries.org` ingress rule from the `homelab-server` tunnel
  configuration (revert to just the `gitlab.quantinovaindustries.org` rule + 404 catch-all that
  existed before this work).
- Delete or disable the Cloudflare Access application protecting `mcp.quantinovaindustries.org`.
- Optionally revert/delete the `mcp.quantinovaindustries.org` DNS record entirely, or leave it
  pointed at the tunnel with no matching ingress rule (falls through to `http_status:404`, same
  as the pre-existing `odoo.quantinovaindustries.org` record does today).

## Remove the systemd unit

```bash
sudo systemctl disable --now qic-mcp.service
sudo rm /etc/systemd/system/qic-mcp.service
sudo systemctl daemon-reload
```

## Remove deployed files and credentials

```bash
sudo rm -rf /srv/qic-mcp
sudo rm -rf /etc/qic-mcp
sudo userdel qic-mcp
```

## Revoke credentials

- Revoke the GitLab PAT used by the service (GitLab → Preferences → Access Tokens).
- Revoke the Cloudflare Access service token from the Zero Trust dashboard.

## Revert Claude Code / other harness configuration

```bash
rm <project-root>/.mcp.json
unset QIC_CF_ACCESS_CLIENT_ID QIC_CF_ACCESS_CLIENT_SECRET
```

## Revert the branch

Nothing in this work touches `main`. To abandon the branch entirely:

```bash
git push origin --delete REFACTOR/MCP-CONTROL-PLANE   # only if PR #6 is also closed/abandoned first
```

PR #6 itself should be closed (not merged) via the GitHub UI/API if the whole effort is abandoned;
this procedure does not do that automatically since closing a PR is an explicit owner decision.
