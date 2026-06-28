# Security Policy

QUANTINOVA INDUSTRIES CORP takes the security of its software, automation, infrastructure, and documentation seriously.

## Supported versions

Each repository must maintain a repository-specific support table when its release model differs from the default below.

| Version or branch | Security support |
|---|---|
| Latest production release | Supported |
| Default branch | Supported for development; not necessarily production-ready |
| Previous production release | Supported only during an announced transition window |
| Older, archived, or end-of-life versions | Not supported |
| `[PROJECT_SPECIFIC_VERSION]` | NOT STATED — replace or remove |

## Reporting a vulnerability

Do **not** open a public issue, discussion, pull request, or support ticket for a suspected vulnerability.

Use the following order:

1. Open the affected repository.
2. Select the **Security** tab.
3. Select **Report a vulnerability** to create a private security advisory report.
4. If private vulnerability reporting is unavailable, contact `[SECURITY_CONTACT_EMAIL]` with the subject:
   `SECURITY REPORT — [REPOSITORY_NAME] — [SHORT DESCRIPTION]`.

If neither method is available, contact an authorized QUANTINOVA INDUSTRIES CORP repository administrator through an established private corporate channel and request a secure reporting method. Do not send exploit details through an unapproved channel.

## Information to include

Provide as much of the following as safely possible:

- affected repository, component, version, branch, or commit;
- vulnerability class and affected security property;
- prerequisites and attack scenario;
- minimal reproduction steps or proof of concept;
- observed and potential impact;
- affected configurations or environments;
- known mitigations or workarounds;
- whether the issue is known to be actively exploited;
- reporter contact information and disclosure expectations.

Sanitize logs and evidence. Do not include unrelated credentials, personal data, client data, procurement records, production database exports, or proprietary information.

## Handling targets

The following are target service levels, not guarantees:

| Stage | Target |
|---|---|
| Acknowledge receipt | Within 2 business days |
| Initial severity assessment | Within 5 business days |
| Status update for confirmed material issues | At least every 10 business days |
| Remediation timeline | Based on severity, exploitability, affected systems, and release risk |

Critical reports involving active exploitation, credential exposure, material data loss, or broad unauthorized access should be clearly marked **CRITICAL**.

## Coordinated disclosure

Reporters are requested to:

- provide reasonable time for investigation and remediation;
- avoid accessing, modifying, retaining, or destroying data beyond what is necessary to demonstrate the issue;
- avoid privacy violations, service disruption, social engineering, extortion, and destructive testing;
- keep vulnerability details confidential until an agreed disclosure date;
- comply with applicable law and authorized testing scope.

QUANTINOVA INDUSTRIES CORP will coordinate disclosure when appropriate. Public credit is provided only with the reporter's consent and subject to legal, contractual, and security constraints.

## Scope

Unless a repository states otherwise, security reports may cover:

- source code and application logic;
- authentication and authorization;
- secrets and credential handling;
- dependency and supply-chain risk;
- CI/CD workflows;
- cloud and infrastructure configuration stored in the repository;
- APIs, integrations, and automation;
- data validation, exposure, and retention behavior.

The following are generally out of scope unless they demonstrate a concrete security impact:

- reports based only on automated scanner output without validation;
- missing security headers with no practical exploit;
- denial-of-service testing without written authorization;
- social engineering or physical security testing;
- attacks requiring compromised administrator access without an additional control failure;
- vulnerabilities in unsupported or materially modified versions;
- findings that depend on disclosure of a user's own credentials.

## Safe-harbor statement

No authorization is granted for testing outside systems and accounts owned or explicitly approved by QUANTINOVA INDUSTRIES CORP. Testing must stop immediately if it risks harm, disruption, unauthorized data access, or violation of law or contract.

Good-faith research that follows this policy will be considered in the handling of the report. This statement is not legal advice, does not waive legal rights, and does not authorize activity prohibited by law or third-party terms.

## Security requirements for contributors

Contributors must:

- keep secrets out of source control and history;
- use least-privilege permissions;
- validate untrusted input and encode output appropriately;
- avoid unsafe deserialization, injection, path traversal, and insecure temporary-file patterns;
- review dependency provenance and lockfile changes;
- use approved cryptographic libraries and protocols;
- avoid logging sensitive values;
- document security assumptions and residual risks;
- request security review for material changes.

## Policy maintenance

Review this policy at least annually and after material changes to reporting channels, ownership, supported products, or GitHub security features.
