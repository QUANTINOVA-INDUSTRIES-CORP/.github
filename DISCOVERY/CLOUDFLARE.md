# Discovery — Cloudflare

Date: 2026-09-05

## Zone

- `quantinovaindustries.org`, zone id `e4e9ed9c89efea7c7cf00bd3d2e36434`, active, on account `ce9dc31214526c1e01e65da0ea3069fc`.

## Tunnel

- Live tunnel: **`homelab-server`** (id `5acc2f31-3607-4cb2-99de-c20b4b656827`), status `healthy`, 4 active connections from the homelab box, `remote_config: true` (config is managed via the Cloudflare API/dashboard, not a local `config.yml` — confirmed no `/etc/cloudflared/config.yml` on the box, only a tunnel token file).
- Current ingress (from `GET /accounts/{account}/cfd_tunnel/{id}/configurations`):
  ```json
  { "ingress": [
      { "hostname": "gitlab.quantinovaindustries.org", "service": "http://localhost:80" },
      { "service": "http_status:404" }
  ]}
  ```
- **Finding:** a *second*, unrelated tunnel named `QIC_MCP` (id `5a69badf-...`) exists but was **deleted on 2026-09-02** and never had an active connection (`remote_config: false`, i.e. it used a local config file and was never actually run). This looks like leftover scaffolding from an earlier, abandoned attempt at this same project.

## DNS (zone `quantinovaindustries.org`)

| Name | Type | Target | Proxied |
|---|---|---|---|
| `gitlab.quantinovaindustries.org` | CNAME | `5acc2f31-...cfargotunnel.com` (homelab-server tunnel) | yes |
| `mcp.quantinovaindustries.org` | CNAME | `5a69badf-...cfargotunnel.com` (**the deleted `QIC_MCP` tunnel**) | yes |
| `odoo.quantinovaindustries.org` | CNAME | `5acc2f31-...cfargotunnel.com` (homelab-server tunnel) | yes |
| `ssh.quantinovaindustries.org` | CNAME | `ca209e6b-...cfargotunnel.com` (separate SSH tunnel) | yes |

**`mcp.quantinovaindustries.org` is a dangling record** — it points at a deleted tunnel and currently resolves to nothing useful. It needs to be repointed at the live `homelab-server` tunnel (`5acc2f31-...cfargotunnel.com`), and an ingress rule for `mcp.quantinovaindustries.org → http://127.0.0.1:<port>` needs to be added to that tunnel's config, ahead of the `http_status:404` catch-all.

(Note, not in scope: `odoo.quantinovaindustries.org` also has a DNS record on the same tunnel but no matching ingress rule exists yet, so it currently 404s. Left untouched — not part of this task.)

## Cloudflare Access

Two existing Access applications on this account:
- `Warp Login App` (`qic-dev0ps-team.cloudflareaccess.com/warp`)
- `QIC SSH` (protecting `ssh.quantinovaindustries.org`)

No Access application yet protects `mcp.quantinovaindustries.org`. Following the `QIC SSH` precedent, a new Access app + service-token policy for `mcp.quantinovaindustries.org` is the natural pattern to reuse.
