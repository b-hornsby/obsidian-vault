---
title: PC Security
type: concept
tags: [security, wazuh, monitoring, homelab]
---

# PC Security

Hub page for all things security monitoring on the Windows PC.

## What's Running

| Component | Role | Status |
|-----------|------|--------|
| [[wazuh-ntfy-checkpoint-2026-06-15|Wazuh Manager]] | Event analysis, rules, alerting | ✅ Active |
| Wazuh Agent (ID 013) | Windows endpoint monitoring | ✅ Active |
| Sysmon64 | Process/file/network telemetry | ✅ Active |
| ntfy relay | Phone alerts for level 5+ events | ✅ Active |
| Dashboard | `http://127.0.0.1:8080` — local only | ✅ Active |

## Architecture

```
Windows PC → Wazuh Agent → WSL Manager (172.28.184.10:1514)
                ↓                      ↓
            Sysmon64              ntfy relay → phone alerts
            PowerShell OpLog      health timer
            Security log          dashboard generator
```

## Key Documents
- [[wazuh-ntfy-checkpoint-2026-06-15|Wazuh + ntfy Project Checkpoint]] — full technical reference
- [[hermes-memories/2026-06-15|Session notes — June 15, 2026]]

## Access Methods
- **Terminal:** Hermes in WSL2 terminal (full access)
- **Phone (away):** Termius + tmux → same session
- **Watch (future):** Telegram bot (not set up yet)
- **Dashboard:** `http://127.0.0.1:8080` via Termius port forwarding

## Alert Rules (Level 5+)
- Failed logons (brute force) — rule 60122
- SSH brute force — rules 871001, 871002
- Prompt injection attempts — rule 871003
- Hardware anomalies — rule 871004
- Suspicious process activity — various Sysmon rules

## Suppressed Rules (Noise)
- 92205: PowerShell creating .ps1 in SystemTemp
- 92200: Scripting files in Temp/User folders

## Related
- [[nodes/projects/homelab-stack|Homelab]] — the PC being monitored
- [[nodes/projects/second-brain-vault|Second Brain Vault]] — knowledge infrastructure
