# Support

This document defines the default support path for repositories owned by QUANTINOVA INDUSTRIES CORP. Repository-specific support instructions take precedence.

## Choose the correct channel

| Need | Correct channel |
|---|---|
| Reproducible defect | Bug report issue form |
| New capability or enhancement | Feature request issue form |
| Usage or configuration question | Repository discussions, documented support channel, or issue tracker when enabled |
| Internal operational incident | `[INTERNAL_INCIDENT_CHANNEL]` |
| Access request | `[ACCESS_REQUEST_SYSTEM]` |
| Security vulnerability | Private process in `SECURITY.md` |
| Code-of-conduct concern | Private contact in `CODE_OF_CONDUCT.md` |
| Commercial, procurement, or contractual matter | Approved corporate business channel; not a GitHub issue |

Do not disclose credentials, personal data, client data, pricing, procurement-sensitive records, internal incident details, or vulnerabilities in a public issue.

## Before requesting support

1. Read the repository `README.md`, runbooks, and troubleshooting documentation.
2. Search open and closed issues and discussions.
3. Confirm that you are using a supported version and approved configuration.
4. Reproduce the issue with the smallest safe example.
5. Collect sanitized logs, timestamps, versions, and exact error messages.
6. State the operational impact and any safe workaround.

## Support request contents

Include:

- repository and component;
- version, branch, or commit;
- environment and relevant runtime versions;
- expected and observed behavior;
- reproduction steps;
- sanitized evidence;
- impact, urgency, and deadline;
- workaround attempted;
- related issue, pull request, deployment, or change record.

Use `NOT STATED` for information that is genuinely unavailable. Do not guess.

## Response expectations

Unless a repository or contract states otherwise:

- support is provided on a reasonable-effort basis;
- issue priority is determined by verified severity, affected users, operational impact, security risk, and available capacity;
- opening an issue does not create a contractual service-level agreement;
- incomplete, duplicate, unsupported, or out-of-scope requests may be closed with guidance;
- maintainers may request a minimal reproduction before investigation;
- production deployment and emergency response follow separate change and incident-management procedures.

## Severity guide

| Severity | Typical condition |
|---|---|
| S1 — Critical | Material production outage, active security event, data-loss risk, or business-critical process blocked with no safe workaround |
| S2 — High | Major function unavailable or materially incorrect; significant users or operations affected |
| S3 — Medium | Degraded behavior or limited operational impact; workaround exists |
| S4 — Low | Minor defect, documentation issue, cosmetic problem, or general question |

A requested severity may be reclassified after triage.

## Maintainer triage

Maintainers should:

1. confirm scope and remove any exposed sensitive information;
2. classify type, severity, and affected component;
3. reproduce or request missing evidence;
4. identify owner and next action;
5. link duplicates and dependencies;
6. communicate status and closure reason;
7. convert security issues to the private process immediately.

## Escalation

Escalate through `[SUPPORT_ESCALATION_CHANNEL]` only when:

- an S1 or S2 condition is verified;
- a committed business deadline is at risk;
- ownership is unresolved;
- a support request has a material security, legal, privacy, or compliance dimension;
- the normal support path is unavailable.

## Unsupported requests

The following are not handled through public repository support:

- requests for credentials or elevated access;
- disclosure of vulnerabilities;
- confidential business negotiations;
- procurement submissions or supplier quotations;
- custom development commitments without approval;
- legal conclusions;
- recovery of data not covered by an approved backup or retention policy;
- support for unapproved forks, modified deployments, or end-of-life versions.
