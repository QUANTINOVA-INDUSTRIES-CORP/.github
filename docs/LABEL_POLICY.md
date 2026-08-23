# Label Policy

Canonical label taxonomy for QUANTINOVA INDUSTRIES CORP repositories during the base-build
phase. Label names are short and machine-parseable (`category:value`) so they can be filtered
and scripted against. One hex color family is assigned per category; every label within a
category uses a shade from that family. Do not assign colors ad hoc, per repository.

Colors are not applied automatically — GitHub's default labels (`bug`, `documentation`,
`enhancement`, etc.) already exist on organization repositories and are left in place. This
taxonomy is additive.

## 1. Type

Hue: blue.

| Label | Hex |
|---|---|
| `type:bug` | `#1B4F9C` |
| `type:feature` | `#2C6FD1` |
| `type:refactor` | `#4A8EE0` |
| `type:docs` | `#6BA6E8` |
| `type:security` | `#123B73` |
| `type:infra` | `#3D7BC7` |
| `type:data` | `#5B99DA` |
| `type:research` | `#7FB2E8` |
| `type:audit` | `#234F91` |

## 2. Status

Hue: amber.

| Label | Hex |
|---|---|
| `status:triage` | `#FFF3B0` |
| `status:ready` | `#FFD43B` |
| `status:blocked` | `#B8860B` |
| `status:in-progress` | `#FFC107` |
| `status:review` | `#E8A317` |
| `status:approved` | `#D4A017` |
| `status:deferred` | `#C9B037` |

## 3. Priority

Hue: red.

| Label | Hex |
|---|---|
| `priority:critical` | `#7F1D1D` |
| `priority:high` | `#B91C1C` |
| `priority:medium` | `#EF4444` |
| `priority:low` | `#FCA5A5` |

## 4. Scope

Hue: teal.

| Label | Hex |
|---|---|
| `scope:frontend` | `#0F766E` |
| `scope:backend` | `#14907A` |
| `scope:database` | `#1AA88A` |
| `scope:devops` | `#21C29A` |
| `scope:gitlab` | `#2ADBAB` |
| `scope:github` | `#34E6B8` |
| `scope:control-plane` | `#0B5E56` |
| `scope:operations-hub` | `#128577` |
| `scope:agents` | `#17A08D` |
| `scope:governance` | `#0A4A44` |

## 5. Risk

Hue: orange.

| Label | Hex |
|---|---|
| `risk:breaking` | `#C2410C` |
| `risk:security` | `#EA580C` |
| `risk:data` | `#F97316` |
| `risk:infra` | `#FDBA74` |

## 6. Source

Hue: purple. See `PROVENANCE_POLICY.md` for what each source value means and what it requires.

| Label | Hex |
|---|---|
| `source:native` | `#5B21B6` |
| `source:cherry-picked` | `#7C3AED` |
| `source:migrated` | `#9061F9` |
| `source:reference` | `#C4B5FD` |

## 7. Review

Hue: slate.

| Label | Hex |
|---|---|
| `review:claude` | `#475569` |
| `review:codex` | `#64748B` |
| `review:agy` | `#94A3B8` |
| `review:human` | `#1E293B` |

## 8. Agent

Hue: magenta. Required on every agent-generated change per `AGENT_POLICY.md` §2.

| Label | Hex |
|---|---|
| `agent:claude` | `#BE185D` |
| `agent:codex` | `#DB2777` |
| `agent:agy` | `#EC4899` |
| `agent:sean` | `#F472B6` |

## 9. Application

Apply labels at the issue or pull-request level, not by editing file content. A pull request
importing cherry-picked material carries at minimum one `type:`, one `scope:`, one `status:`,
one `source:`, and one `agent:` label. Reviewer labels (`review:`) are added by whoever performs
that review, not by the change's author.
