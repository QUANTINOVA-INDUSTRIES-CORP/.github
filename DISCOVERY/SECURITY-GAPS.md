# Discovery — Security Gaps to Close

Date: 2026-09-05

1. **Owner-approval boundary** (brief §7) — `owner_approved: bool` client argument plus a global `QIC_ENABLE_MUTATIONS` env flag is the only gate today. Needs a real server-side approval mechanism (nonce, approval file, or equivalent) so a compromised or careless client can't self-authorize a mutation just by passing `true`. Decision needed from operator — asked in-conversation.
2. **GitLab credential identity** — no dedicated service-account PAT exists; only the CEO's personal, full-privilege token is available. Decision needed — asked in-conversation.
3. **Dangling DNS** — `mcp.quantinovaindustries.org` points at a deleted tunnel today, so until fixed the hostname is not just "not deployed," it actively resolves to a non-functional target. Low risk (no service behind it) but should be corrected as part of this work, not left dangling.
4. **No Cloudflare Access application yet protects `mcp.quantinovaindustries.org`** — until one is created, any ingress rule added for that hostname would be reachable without Access enforcement while it exists. Sequencing matters: create the Access app and policy *before* or in the same change as the ingress rule, not after.
5. **No audit logging yet** — mutation calls today would succeed/fail with no durable, secret-redacted record.
6. **`uv` not installed on homelab** — needs installing (or the service needs to be run a different way) before the documented `uv sync && uv run python SERVER.py` deployment path works.
