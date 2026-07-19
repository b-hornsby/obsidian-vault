---
type: topic
status: active
priority: P1
first_seen: 2026-07-06
tags: [tech, it-tooling, it-work, endpoint-management]
aliases: [IT Tooling, Daily Tool Stack, Workplace IT]
---

# IT Tooling

> On-the-job tooling for IT equipment provisioning and endpoint management. These are the tools I use daily in the field.

## Ticketing / ITSM

- **Freshservice** — ticket intake, SLA tracking, asset lifecycle requests, user-facing request queue
- Patterns: ticket-first workflow, detail-rich notes, asset linking, SLA-aware timestamps

## Identity / Directory

- **Microsoft Entra ID** — user lifecycle (new hire / termination), group membership, device enrollment, MFA status
- Patterns: naming conventions, license assignment, guest vs member accounts, device compliance checks

## Documentation / KB

- **IT Glue** — documenting procedures, onboarding / offboarding runbooks, configuration baselines, vendor reference
- Patterns: flexible asset documentation, relationship mapping, network/credentials storage, maintaining documented state vs actual state

## RMM / Endpoint Management

- **NinjaOne** — RMM sweeps, patch status, endpoint health monitoring, remote assist sessions, scripts/deployment
- Patterns: monitoring-first approach, automation thresholds, patch testing before force-push, script deployment for common endpoint setups

## Provisioning Stack (Daily Work)

| Task | Tool used | Notes |
|------|-----------|-------|
| iPad setup for sales users | Freshservice + Entra + MDM | Enroll, configure mail/cal, app push, naming convention |
| Laptop setup for executives | Freshservice + Entra + NinjaOne | BitLocker, domain join, baseline apps, remote bootstrap |
| User offboarding | Freshservice + Entra | Disable accounts, remove devices, reclaim licenses, document in IT Glue |
| Asset lifecycle tracking | Freshservice + IT Glue | Serial numbers, procurement status, handoff documentation |
| Remote assist | NinjaOne | Screen share, command line, file transfer, script deployment |
| Patch / security status | NinjaOne | Patch gaps, AV status, compliance, escalation tickets |

## What I've Learned

- Freshservice ticket quality = downstream metrics. Vague tickets cause rework.
- Entra device management needs consistent naming conventions or inventory is unusable.
- IT Glue is only current if documentation is treated as part of the ticket, not a post-hoc chore.
- NinjaOne automation needs testing before force-pushing to exec endpoints.
- Runbook quality determines junior tech self-sufficiency.

## Related

- [[nodes/people/bryan.md|Bryan]]
- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/topics/tech/pc-security.md|PC Security]]
