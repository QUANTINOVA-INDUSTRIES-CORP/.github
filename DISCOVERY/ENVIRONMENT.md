# Discovery — Environment

Date: 2026-09-05

## Operator machine (this session)

- Windows 11, working from `V:\` (QUANTINOVA DEV DRIVE).
- `gh` CLI 2.99.0, authenticated as `ceobetch` (scopes: gist, read:org, repo).
- `glab` CLI 1.116.0, authenticated to `gitlab.quantinovaindustries.org` as `ceobetch` (President/Chairman/CEO account, `can_create_project: true`, `projects_limit: 100000`). Token stored in OS keyring, never displayed.
- Cloudflare API access is available in-session via the `cloudflare-api` MCP plugin, scoped to account `ce9dc31214526c1e01e65da0ea3069fc` ("Devoperationsquantinova@gmail.com's Account"). This gave read/write access to zones, DNS, Cloudflare Tunnel config, and Access apps without needing a separately supplied API token.

## Homelab server (`homelab-lan` / `homelab-server.local`)

- Reachable via SSH alias `homelab-lan` (mDNS). The `homelab` alias (static LAN IP `192.168.137.2`) timed out — likely a stale/wrong IP; use `homelab-lan`.
- OS: Ubuntu, kernel `7.0.0-30-generic`, hostname `homelab-server`.
- User `ceobetch` (uid 1000) has **passwordless sudo**.
- Python 3.14.4 present system-wide at `/usr/bin/python3`. `uv` is **not installed** — needs installing before `MCP/pyproject.toml` can be used as documented.
- `/srv` exists and is empty (root:root, 755) — clean target for `/srv/qic-mcp`.
- `/opt` has `gitlab/` (Omnibus GitLab CE) and `containerd/`.
- Disk: 233G volume, 205G free.

## Existing services on homelab

- `cloudflared.service` — active, running (see `DISCOVERY/CLOUDFLARE.md`).
- `gitlab-runsvdir.service` — active, running (GitLab CE Omnibus, via runit supervision).
- No existing `qic-mcp` service, no `/etc/qic-mcp`.
