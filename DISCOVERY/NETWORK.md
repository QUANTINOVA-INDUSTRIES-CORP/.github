# Discovery — Network

Date: 2026-09-05

- Homelab reachable over LAN/mDNS via SSH alias `homelab-lan` → `homelab-server.local`. The alternate alias `homelab` (static IP `192.168.137.2`) timed out during this session — that IP may be stale (DHCP change) or the box may not be on that subnet right now. `homelab-lan` is the working path; no change made to SSH config since a working alias already exists.
- No inbound router ports are in use or proposed — all public exposure for `mcp.quantinovaindustries.org` goes through the existing `homelab-server` Cloudflare Tunnel, consistent with the brief's requirement not to open a new public port.
- Tunnel egress-only architecture confirmed: `cloudflared` on the homelab box maintains outbound connections to Cloudflare edge colos (observed connections to `mnl04` and `sin13`/`sin22`); Cloudflare terminates public traffic and forwards over the tunnel to `127.0.0.1`-bound services on the box.
