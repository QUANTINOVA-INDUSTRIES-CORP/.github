# QIC MCP — Deployment Procedure (HomeLab)

Target host: `homelab-lan` (Ubuntu, reachable via SSH; see `DISCOVERY/ENVIRONMENT.md`).
Deployment root: `/srv/qic-mcp`. Service account: `qic-mcp` (dedicated, non-root, no shell needed
beyond running the service).

## 1. Service account and directories

```bash
sudo useradd --system --home-dir /srv/qic-mcp --shell /usr/sbin/nologin qic-mcp
sudo mkdir -p /srv/qic-mcp /etc/qic-mcp
sudo chown -R qic-mcp:qic-mcp /srv/qic-mcp
sudo chown root:root /etc/qic-mcp
sudo chmod 750 /etc/qic-mcp
```

## 2. Ship the code

Deploy via `git`, not a hand-copied tree, so `git log`/`git status` on the host always shows what
is actually running:

```bash
sudo -u qic-mcp git clone --branch REFACTOR/MCP-CONTROL-PLANE --single-branch \
  https://github.com/QUANTINOVA-INDUSTRIES-CORP/.github.git /srv/qic-mcp/repo
sudo -u qic-mcp ln -s /srv/qic-mcp/repo/MCP /srv/qic-mcp/MCP
```

## 3. Python runtime

`uv` is not installed on the host yet (confirmed in discovery). Install it for the service account,
then sync the pinned dependencies:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo -u qic-mcp env UV_INSTALL_DIR=/srv/qic-mcp/.local/bin sh
sudo -u qic-mcp bash -lc 'cd /srv/qic-mcp/repo/MCP && /srv/qic-mcp/.local/bin/uv venv /srv/qic-mcp/.venv && /srv/qic-mcp/.local/bin/uv pip install --python /srv/qic-mcp/.venv/bin/python .'
```

(`ExecStart` in `systemd/qic-mcp.service` points at `/srv/qic-mcp/.venv/bin/python` directly, so the
service does not depend on `uv` being on `PATH` at runtime — only at build/update time.)

## 4. Environment file

`/etc/qic-mcp/qic-mcp.env`, owner `root:root`, mode `0600`, **never committed**:

```bash
QIC_GITLAB_BASE_URL=https://gitlab.quantinovaindustries.org
QIC_GITLAB_PAT=<value piped in directly from the operator's own credential store, never typed or displayed>
QIC_ENABLE_MUTATIONS=false
QIC_MCP_HOST=127.0.0.1
QIC_MCP_PORT=8000
QIC_MCP_APPROVAL_FILE=/run/qic-mcp/approve
QIC_MCP_APPROVAL_TTL_SECONDS=300
```

The PAT value must reach this file without ever being echoed to a terminal, a log, or an agent's
own transcript — pipe it directly (`... | ssh homelab-lan "sudo tee /etc/qic-mcp/qic-mcp.env >/dev/null"`)
from wherever it's already held (e.g. the operator's existing credential-manager-backed CLI), never
via a shell variable that gets printed or a command whose argv includes the literal secret.

## 5. systemd unit

```bash
sudo cp /srv/qic-mcp/repo/MCP/systemd/qic-mcp.service /etc/systemd/system/qic-mcp.service
sudo systemctl daemon-reload
sudo systemctl enable --now qic-mcp.service
sudo systemctl status qic-mcp.service --no-pager
curl -s http://127.0.0.1:8000/health
```

## 6. Cloudflare routing (already-existing tunnel, no new inbound ports)

The homelab box already runs `cloudflared` against the live `homelab-server` tunnel
(`5acc2f31-3607-4cb2-99de-c20b4b656827`), remotely managed (`config_src: cloudflare`), currently
routing only `gitlab.quantinovaindustries.org`. See `DISCOVERY/CLOUDFLARE.md` for the full picture,
including the pre-existing dangling `mcp.quantinovaindustries.org` DNS record left over from an
earlier, abandoned tunnel named `QIC_MCP` — that record gets repointed, not left in place.

1. Update the `mcp.quantinovaindustries.org` CNAME to target
   `5acc2f31-3607-4cb2-99de-c20b4b656827.cfargotunnel.com` (the live tunnel), replacing the
   dangling reference to the deleted `QIC_MCP` tunnel.
2. Add an ingress rule to the `homelab-server` tunnel's remote configuration, ahead of the
   `http_status:404` catch-all:
   ```json
   { "hostname": "mcp.quantinovaindustries.org", "service": "http://127.0.0.1:8000" }
   ```
3. Create a Cloudflare Access application protecting `mcp.quantinovaindustries.org`, following the
   existing `QIC SSH` application as precedent, with a Service Auth policy backed by a Cloudflare
   Access Service Token (not the GitLab PAT — a separate, independently-revocable credential).
4. Distribute the resulting `CF-Access-Client-Id` / `CF-Access-Client-Secret` to each authorized
   operator machine as environment variables — never committed, never placed in `.mcp.json` itself.

Both API steps (1) and (2) were performed via the Cloudflare API available to this session; see
the final report for the exact tunnel/zone IDs touched.

## 7. Claude Code

```bash
cp templates/.mcp.json <project-root>/.mcp.json
export QIC_CF_ACCESS_CLIENT_ID=...
export QIC_CF_ACCESS_CLIENT_SECRET=...
claude mcp get qic-control-plane
```

Inside Claude Code: `/mcp` should show `qic-control-plane` connected; call `qic_directive_get`
first, then the read tools.
