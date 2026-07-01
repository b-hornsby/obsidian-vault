---
tags: [security, wazuh, sysmon, ntfy, audit]
created: 2026-06-19 09:50
status: checked-in
---

# Security Stack Audit — June 19, 2026

## Status: Mostly Healthy — data flowing, several subsystems have issues

---

## 1. Wazuh Manager — ✅ RUNNING

All 10 core processes active on port 55000:
- `wazuh-apid` (x5) — API daemon
- `wazuh-authd` — Agent enrollment
- `wazuh-analysisd` — Alert analysis
- `wazuh-execd` — Active responses
- `wazuh-logcollector` — Journald collection
- `wazuh-monitord` — Log rotation
- `wazuh-remoted` — Agent comms
- `wazuh-syscheckd` — File integrity
- `wazuh-modulesd` — Module dispatch
- `wazuh-db` — SQLite engine

Manager stats API works for WUI client but curl/requests get connection drops (WSL TCP quirk).

---

## 2. Wazuh Indexer (OpenSearch) — ⚠️ RUNNING BUT AUTH FAILING

- Ports 9200/9300 listening on 127.0.0.1
- All external auth returns "Unauthorized"
- `wazuh-logs-*` index exists with data
- **Indexer-connector**: Agent 013 fails to sync — `WARNING: Failed to sync agent '013': No available server`

---

## 3. Agent Connectivity — ⚠️ PARTIAL

- Agent 000 (local): ✅ Running
- Agent 013 (Windows DESKTOP-5NE9JEA): Registered but indexer sync broken
- Windows agent IS sending alerts (Sysmon, PowerShell, service changes all visible in alerts.log)
- Indexer connection is the bottleneck

---

## 4. Alerts Flow — ✅ FLOWING

- Total alerts: 74,632 lines in alerts.log
- Dashboard alerts.json: 500 latest, 77KB, updating every 30s
- Recent alerts (June 19 ~09:42 AM, all from DESKTOP-5NE9JEA):
  - Rule 61104 (L3): Service startup type changed
  - Rule 61603 (L3): Sysmon Event 1 process creation (taskhostw, Steam, WinSecHealthHost)
  - Rule 61615 (L3): Sysmon Event 13 registry set value
  - Rule 92028 (L3): PowerShell executed script
  - Rule 92205 (L3): PowerShell created executable in Windows root folder
  - Rule 40704 (L5): Systemd service failure
  - Rule 60642 (L3): Software protection scheduled
- Alert volume: Normal noise, no blast patterns

---

## 5. ntfy Relay — ⚠️ RUNNING BUT HEALTH CHECK FAILING

- Process PID 2993, running wazuh-ntfy-formatted.py
- Systemd: wazuh-ntfy-relay.service — **active (running)** ✅
- Health check: wazuh-relay-health.service — **FAILED** ❌
  - Cause: Can't run systemctl restart without interactive auth in WSL
  - Impact: Relay itself is fine, health monitor keeps failing
- Dedup state: 1 stale entry (DNS rule from old run)
- 15 rules mapped with plain English titles + action guidance
- Reads alerts.log, pushes to ntfy.sh/toastedmel0n-pc-alerts

---

## 6. Dashboard — ✅ WORKING

- HTTP server python3 -m http.server 8080 — serving 200 OK
- data.json updated 09:45: CPU 50%, RAM 65% (18.4/28GB), Disk 6%, GPU 46% util @51°C
- alerts.json: 500 alerts, updating every 30s via update-data.py
- index.html: Dark theme, responsive, 900px max-width
- recent-alerts.html: Scrollable full alert list

---

## 7. Sysmon Config — ⚠️ CAN'T LOCATE

- Windows side: `%TEMP%\sysmonconfig.xml` (C:\Users\toastedmel0n\AppData\Local\Temp\)
- Sysmon IS working — Events 1 (process) and 13 (registry) flowing through Wazuh

---

## 8. Active Responses — ❌ NOT FIRING

- active-responses.log is 0 bytes — no active responses have fired
- execd process running, infrastructure present

---

## Issues to Fix (Priority Order)

### 1. Agent 013 Indexer Sync Failure — MEDIUM
Agent 013 (Windows) sends to Wazuh manager but can't sync with indexer. Indexer API auth can't be verified externally.

### 2. ntfy Health Check Failing — LOW
wazuh-relay-health.service fails trying to systemctl restart. Fix: disable health check OR add NOPASSWD sudoers entry for systemctl restart wazuh-ntfy-relay.service.

### 3. API curl Access — LOW
External curl/requests get connection drops despite API working for WUI. Likely WSL2 TCP stack or API connection handling.

---

## What's Working Well

- Data pipeline: Windows agent → Wazuh manager → alerts.log → update-data.py → dashboard → HTTP server
- Real-time monitoring: Dashboard every 30s with live metrics
- ntfy relay running, deduplicating, ready to push
- Sysmon integration: Process creation, registry, PowerShell all captured
- Alert volume healthy, mostly normal Windows noise

---

## File Paths

- Wazuh logs: /var/ossec/logs/
- Alerts log: /var/ossec/logs/alerts/alerts.log
- Dashboard: /home/toastedmel0n/pc-dashboard/
- ntfy relay: /home/toastedmel0n/wazuh-ntfy-formatted.py
- Relay state: /home/toastedmel0n/.ntfy-relay-state.json
- Dashboard data: /home/toastedmel0n/pc-dashboard/data.json
- Dashboard alerts: /home/toastedmel0n/pc-dashboard/alerts.json
- Sysmon config: %TEMP%\sysmonconfig.xml (Windows)
- ntfy systemd: /etc/systemd/system/wazuh-ntfy-relay.service
- Health check: /etc/systemd/system/wazuh-relay-health.service
- Health script: /home/toastedmel0n/wazuh-relay-health.sh

---

## Next Actions

1. Fix agent 013 indexer sync — check indexer logs and agent connection
2. Disable or fix ntfy health check service
3. If API curl works, investigate connection drop issue
