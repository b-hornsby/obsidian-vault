Wazuh + ntfy + Sysmon Project Checkpoint — 2026-06-23

## Goal
Autonomous PC security monitoring with plain-English ntfy alerts for:
- SSH / logon brute-force
- Suspicious process execution
- Unauthorized remote access
- Hardware abuse
- File integrity changes
Secondary: Enable autonomous management of both WSL manager and Windows agent without copy/paste (file-watcher command channel).

## Architecture (Current)
```
Windows (DESKTOP-5NE9JEA)
  → Wazuh Agent (ID 013) → 1514 TCP → WSL manager (172.28.184.10)
  → Sysmon64 → Microsoft-Windows-Sysmon/Operational → agent → manager
  → PowerShell Operational log → agent → manager (NEW)
  → systemd relay → ntfy.sh/toastedmel0n-pc-alerts → user phone
  → File watcher (C:\Users\toastedmel0n\wazuh-cmd\) → autonomous WSL→Windows command channel (NEW)
```

## What's Done
1. WSL Manager running — wazuh-manager active
2. Windows Agent installed — MSI, enrolled as ID 013, Active
3. Alerts flowing — Security → manager → phone confirmed end-to-end
4. ntfy relay working — formatted relay with retry/backoff/dedup (NEW: rewritten 2026-06-15)
5. Custom rules loaded — 871001–871004 in `/var/ossec/etc/rules/local_rules.xml`
6. Noise filtered — WER, System log events (61104/60702/60718) suppressed
7. Sysmon installed — process, file, DNS, network events flowing
8. Rule 92205 suppressed — PowerShell file creation noise eliminated (FIXED 2026-06-15)
9. PowerShell Operational log forwarding added (NEW 2026-06-15)
10. Relay running as systemd service with auto-restart (NEW 2026-06-15)
11. Relay health check timer — checks every 5 min, restarts if stuck (NEW 2026-06-15)
12. File-watcher command channel — WSL can run Windows commands autonomously (NEW 2026-06-15)
13. File watcher auto-starts on Windows logon via scheduled task (NEW 2026-06-15)
14. Config backup created at `~/wazuh-config-backup-2026-06-15/` (NEW 2026-06-15)
15. SSH from Windows to WSL attempted but abandoned — Microsoft account auth issues; file watcher is the command channel instead
16. Sysmon full telemetry enabled — applied level-0 rule overrides via Kevin Branch / BlueWolfNinja script (`/var/ossec/etc/rules/sysmon_level_0_overrides.xml`, 411 rules at level 3); manager restarted and confirmed active

## Credentials & Locations
| Item | Value |
|------|-------|
| Agent (013) | ID 013 / name: win-desktop / IP: 172.28.176.1 |
| WSL manager IP | 172.28.184.10 |
| ntfy topic | https://ntfy.sh/toastedmel0n-pc-alerts |
| File watcher dir | C:\Users\toastedmel0n\wazuh-cmd\ |
| Config backup | ~/wazuh-config-backup-2026-06-15/ |

## Key Files
- WSL manager config: `/var/ossec/etc/ossec.conf`
- Agent config: `C:\Program Files (x86)\ossec-agent\ossec.conf`
- Alerts: `/var/ossec/logs/alerts/alerts.json` and `alerts.log`
- Relay script: `~/wazuh-ntfy-formatted.py`
- Relay service: `/etc/systemd/system/wazuh-ntfy-relay.service`
- Health check: `/home/toastedmel0n/wazuh-relay-health.sh`
- Health timer: `/etc/systemd/system/wazuh-relay-health.timer`
- Custom rules: `/var/ossec/etc/rules/local_rules.xml`
- Sysmon config: `%TEMP%\sysmonconfig.xml`
- File watcher script: `C:\Users\toastedmel0n\wazuh-cmd\watcher.ps1`

## Custom Rules
|| Rule | Level | Status |
|------|-------|--------|
| 871001 | 10 | Loaded / Active |
| 871002 | 12 | Loaded / Active |
| 871003 | 8 | Loaded / Active |
| 871004 | 7 | Loaded / Active |
| 92200 | 0 | Suppressed (level 0 in ruleset) |
| 92205 | 0 | Suppressed (level 0 in ruleset) |
| 92216 | 0 | Suppressed (level 0 in ruleset) |
| sysmon_level_0_overrides.xml | 3 | Active — 411 level-0 rules overridden to level 3 for full Sysmon telemetry indexing (BlueWolfNinja script applied 2026-06-16) |

## ntfy Relay Features (Updated 2026-06-15)
- Minimum level filter: only sends alerts level 5+
- Deduplication: same rule+host within 5 min window is suppressed
- Retry with exponential backoff on HTTP 429 (rate limit)
- Runs as systemd service with auto-restart
- Health check timer monitors every 5 minutes
- Logs to journal: `journalctl -u wazuh-ntfy-relay.service`

## File Watcher Command Channel
- Drop `.cmd` files in `C:\Users\toastedmel0n\wazuh-cmd\`
- PowerShell watcher executes commands, writes output to `.out` files
- Auto-starts on Windows logon via scheduled task
- Enables autonomous Windows management from WSL without SSH/copy-paste

## Known Issues
- **ntfy HTTP 429**: Rate limit on ntfy.sh free tier. Relay handles with backoff. Don't spam test.
- **Agent IP**: Reports 172.28.176.1 (Hyper-V adapter), not actual host IP. Cosmetic only.
- **SSH abandoned**: Microsoft account + UAC made SSH key auth unreliable. File watcher is the command channel instead.

## Problems Fixed (2026-06-15)

### Rule 92205 still firing despite local_rules.xml override
**Symptom:** Rule 92205 (PowerShell creating .ps1 files in SystemTemp) fired 28+ times. local_rules.xml had `<disabled>yes</disabled>` but Wazuh ignored it — "Rule ID duplicated, only first occurrence considered."
**Root cause:** Default ruleset (0830-sysmon_id_11.xml) loads before local_rules.xml. Same ID = first one wins.
**Fix:** Changed level from 9 to 0 directly in `/var/ossec/ruleset/rules/0830-sysmon_id_11.xml`.
**Verification:** Triggered PowerShell file creation → no new 92205 alerts in alerts.json.

### ntfy relay hitting rate limits
**Symptom:** HTTP 429 errors, alerts not reaching phone.
**Root cause:** Relay sent ALL alerts including level 3 PAM/sudo events.
**Fix:** Rewrote relay with level 5+ filter, dedup window, retry backoff.
**Verification:** Dedup messages appearing in journal, no more 429 errors.

### No autonomous Windows command channel
**Symptom:** Every Windows fix required user to paste PowerShell commands.
**Fix:** Created file-watcher command channel — PowerShell script watches folder, executes .cmd files, writes .out results.
**Verification:** Successfully triggered Windows events and read results from WSL.

### Relay was fragile (background nohup process)
**Symptom:** If relay crashed, no alerts until manually restarted.
**Fix:** Converted to systemd service with `Restart=always` + health check timer.
**Verification:** `systemctl is-active wazuh-ntfy-relay.service` = active.

## Changelog
- 2026-06-09: Manager + agent commissioned (originally enrolled as ID 004)
- 2026-06-10: Checkpoint file created
- 2026-06-13: Fixed agent manager IP, verified full pipeline, filtered noise, installed Sysmon, repaired agent config
- 2026-06-15: Suppressed rule 92205, rewrote ntfy relay with retry/dedup/level filter, added PowerShell Operational log forwarding, created file-watcher command channel, set up relay systemd service + health check, config backup, Windows watcher auto-start task
- 2026-06-16: Added plain English to ntfy relay, lower level filter from 5 to 3, added Downloads and user creation rules (100002/100003), added Sysmon EIDs 27/28/29 overrides, fixed relay from failing user service to stable system-wide service, confirmed end-to-end Sent: 200

## What's Verified Working
1. Security events flow from Windows agent → manager
2. Failed logon alert (60122) reaches phone via ntfy
3. Sysmon events reach manager (process, file, DNS, network)
4. PowerShell Operational log forwarding active
5. Rule 92205 suppressed (no more PowerShell temp file spam)
6. ntfy relay: level 5+ filter, dedup, retry backoff all working
7. Relay auto-restarts via systemd
8. Health check timer running (every 5 min)
9. File-watcher command channel: WSL → Windows autonomous execution
10. File watcher auto-starts on Windows logon

## Final Sweep Results (2026-06-15 12:15 EDT)

| Component | Status | Notes |
|-----------|--------|-------|
| Wazuh manager | ✅ Active | No errors in log |
| Agent 013 (win-desktop) | ✅ Active | Connected, keepalive current |
| ntfy relay | ✅ Active | Retry/backoff working, hit rate limit during testing (expected) |
| Health check timer | ✅ Active | Checks every 5 min, auto-restarts relay if stuck |
| Rule 92205 | ✅ Suppressed | Level 0 in ruleset, no more PowerShell temp file spam |
| Custom rules 871001-004 | ✅ Loaded | In local_rules.xml |
| WazuhSvc (Windows) | ✅ Running | Auto-start enabled |
| Sysmon64 (Windows) | ✅ Running | Auto-start enabled |
| File watcher | ✅ Running | 1h 49m uptime at time of check |
| Config backup | ✅ Saved | `~/wazuh-config-backup-2026-06-15/` |
| ntfy integration blocks | ✅ Removed | Was causing "Invalid integration" errors in manager log |

## What's Missing / Deferred
1. **Wazuh Dashboard** — optional visual interface, not needed for single PC
2. **Prompt injection guardrails** — lower priority, can add later
3. **Agent IP reporting** — cosmetic, doesn't affect functionality

## Update 2026-06-22 — Detection Expansion & Rule Stabilization

### What Changed
1. **Alert 92213 false-positive fixed** in `/var/ossec/ruleset/rules/0830-sysmon_id_11.xml` using valid PCRE2 negation to exclude `__PSScriptPolicyTest_*.ps1` file drops from rule 92213 (`Executable file dropped in folder commonly used by malware`). Validated XML and restarted Wazuh manager.
2. **Suppressed alert 92148** noise.
3. **Added hardware-abuse detection rules** (`872001-872005`): USB insertion, boot device changes, suspicious mounts, CD-ROM writes, exe loaded from removable media.
4. **Added file-integrity rules** (`872006-872009`): new executable/script in `Temp`, `AppData`, `Startup`, and registry `Run` key modifications.
5. **Added unauthorized remote-access / account change rules** (`872010-872015`): new local user creation, RDP/SMB from non-private IPs, admin/privileged-group changes, unusual port listeners.
6. **Kept brute-force/suspicious-process rules in `custom_bruteforce_process_rules.xml`** (`871001-871008`). They remain active and untouched in their own file to avoid loader issues with `local_rules.xml`.
7. **Replaced `local_rules.xml`** with a clean flat rule file rooted in one `<group name="local,sysmon,">` container. `wazuh-analysisd -t` passes and rule warnings are now only harmless "overwrite target missing/duplicate" legacy warnings.
8. **GitHub backup**: pushed checkpoint commit `e4f40a2` to `origin/master`.

### Final Sweep Results (2026-06-22 19:59 EDT)

| Component | Status | Notes |
|-----------|--------|-------|
| Wazuh manager | ✅ Active | Rules loaded; `analysisd -t` passes |
| Agent 013 (win-desktop) | ✅ Active | 172.28.176.1 |
| ntfy relay | ✅ Active | Level-5 filter working |
| Rule 92213 | ✅ Suppressed | 0 new false-positive events after reload |
| Rules 872001-872015 | ✅ Loaded | Hardware, FIM, remote access, account changes |
| Custom rules 871001-871008 | ✅ Loaded | In separate file, not duplicated |
| WazuhSvc (Windows) | ✅ Running | Auto-start enabled |
| Sysmon64 (Windows) | ✅ Running | Auto-start enabled |
| File watcher | ✅ Running | WSL ↔ Windows command channel intact |
| Dashboard updater | ⏳ Pending | `update-data.py` patches ready; restart `pc-dashboard-updater.service` to activate |

### What's Missing / Deferred
1. **Dashboard deployed** — `pc-dashboard-updater.service` restarted with patched `update-data.py` (24h alert window, atomic `.tmp` + `replace` writes, PAM sudo throttling). `pc-dashboard.service` serving at `http://127.0.0.1:8080`.
2. **Relay upgraded** — Changed from level 5+ filter to level 3+ (`RELAYED_RULES` dict, 50+ rule IDs). Added `RULE_MAP` for plain-English descriptions with action guidance. Added `[TRUSTED]` tagging for rule 92201 (PowerShell script in Temp from built-in process).
3. **Relay is now system-level** — `/etc/systemd/system/wazuh-ntfy-relay.service` runs as root (replaced failing user-level service).
4. **Injection alert relay** — `injection-alert-relay.py` monitors Hermes prompt-injection audit log, posts HIGH-risk blocked/unapproved events to ntfy (every minute).
5. **Heartbeat watchdog** — `heartbeat-watchdog.service` + `.timer` (every 5 min) checks data.json freshness + relay status, posts to `ntfy.sh/pc-heartbeat` if stale.
6. **Dashboard HTML hand-edited** — served `index.html` was manually patched after generation (svc_wazuh_color, GPU power bars, comprehensive live JS). Diverges from `generate.py` output.

## Update 2026-06-23 — Dashboard Goes Live, Relay Upgraded

### What Changed
1. **Dashboard is now LIVE** — `pc-dashboard-updater.service` restarted with patched `update-data.py` (24h alert window, atomic `.tmp` + `replace` writes, PAM sudo throttling). `pc-dashboard.service` serving at `http://127.0.0.1:8080`. Browser reads `data.json` every 3s + `alerts.json` every 3s, updates DOM in-place.
2. **Data pipeline split cleanly** — `update-data.py` handles real-time metrics (CPU/RAM/Disk/GPU/services/alerts → data.json + alerts.json). `generate.py` is the static HTML generator (writes index.html + initial data.json). Two separate processes. `generate.py` is NOT running as a service.
3. **Relay upgraded** — Changed from level 5+ filter to level 3+ (`RELAYED_RULES` dict now maps 50+ rule IDs with `min_level: 3`). Added `RULE_MAP` for plain-English descriptions with action guidance. Added `[TRUSTED]` tagging for rule 92201 (PowerShell script in Temp from built-in `powershell.exe` process).
4. **Relay is now system-level service** — `/etc/systemd/system/wazuh-ntfy-relay.service` runs as root. Replaced failing user-level service. Uses `python3 -u` for unbuffered output.
5. **Injection alert relay** — `injection-alert-relay.py` monitors `/home/toastedmel0n/.hermes/audit/prompt-injection.log` for HIGH-risk blocked/unapproved events, posts to ntfy with title `Hermes Guardrail: {event_type}`. Runs every minute via systemd timer.
6. **Heartbeat watchdog** — `heartbeat-watchdog.service` + `.timer` (every 5 min) checks if `data.json` is ≤15 min old and if `wazuh-ntfy-relay.service` is active. If stale or down → posts to `ntfy.sh/pc-heartbeat`.
7. **Local user creation rules** — Added rule 60103 for Windows Event 4648 (logged-on user using explicit credentials) and rule 60104 for Event 4720 (new local user). Both at level 3, mapped to plain-English in relay.
8. **Rule 872010 fixed** — Had no `<if_sid>` (inherited from wrong parent). Added `<if_sid>100003</if_sid>` to inherit detection chain. Windows agent config already collects Security EventLog.
9. **Dashboard HTML hand-edited** — `index.html` was manually patched after generation to add `svc_wazuh_color`, `svc_sysmon_color`, GPU VRAM%/power bars, and more comprehensive live-updating JS. The served HTML now diverges from what `generate.py` produces. This is the current state; generator is the template, HTML is the live product.
10. **ntfy topic clarified** — Relay posts to `https://ntfy.sh/toastedmel0n-pc-alerts`. No API key. Urgent priority for external IPs, default for internal.
11. **Dashboard core purpose redefined** — Dashboard = service visibility (are wazuhsvc and sysmon running? what to do next?). Alerting = ntfy's job. Dashboard does not replace phone notifications.

### Data Flow Diagram

```
[Windows Host (DESKTOP-5NE9JEA)]
    │
    ├── Sysmon64 (EventID 1-15) ─┐
    │   └── File, network, process, USB, DNS, registry events
    │
    └── Wazuh Agent (ID 013) ─┐
           └── Sends events → Wazuh manager in WSL2
                               │
                               ▼
                    /var/ossec/logs/alerts/
                    ├── alerts.log       ──► [wazuh-ntfy-formatted.py] ──► ntfy.sh ──► phone
                    │   (plain text)         (tail, classify, dedup, plain-English)
                    │
                    └── alerts.json      ──► [update-data.py] ──► data.json
                            (JSON lines)           (every 1s)        │
                                                             ├── index.html ──► Browser (127.0.0.1:8080)
                                                             ├── data.json  ──► JS poll 3s (metrics)
                                                             └── alerts.json ─► JS poll 3s (recent alerts)
```

### Final Sweep Results (2026-06-23 12:00 UTC)

| Component | Status | Notes |
|-----------|--------|-------|
| Wazuh manager | ✅ Active | 50+ rules loaded, `analysisd -t` passes |
| Agent 013 (win-desktop) | ✅ Active | OK / DESKTOP-5NE9JEA |
| ntfy relay | ✅ Active | Level 3+ filter, 50+ rule IDs, [TRUSTED] tagging, dedup 300s |
| Dashboard (updater) | ✅ Active | `pc-dashboard-updater.service`, writes data.json + alerts.json every 1s |
| Dashboard (server) | ✅ Active | `pc-dashboard.service`, serving at 127.0.0.1:8080 |
| Dashboard HTML | ⚠️ Hand-edited | Served index.html diverges from generate.py output (svc_wazuh_color, GPU power bars added) |
| Heartbeat watchdog | ⚠️ Active but timer may be stale | Checks data.json age + relay status every 5 min |
| Relay health timer | ❌ Inactive/dead | `systemctl restart` fails in WSL due to interactive auth |
| Injection relay | ✅ Active | Runs every minute, posts HIGH-risk prompt-injection events |
| Sysmon | ✅ Running | Full telemetry (level 0 overrides applied) |
| WazuhSvc | ✅ Running | Auto-start enabled |
| File watcher | ⏳ Not verified recently | Was working 2026-06-22 |
| GPU (RTX 3070) | ✅ Active | nvidia-smi reports temp/util/VRAM/power |

### Known Issues
- **Relay health timer fails**: `systemctl restart` triggers interactive auth prompt in WSL. Service relies on `Restart=always` (10s retry) only.
- **Two relay processes**: PID 98182 and 190361 — likely a restart race. Only one should be active.
- **Dashboard HTML drift**: Served `index.html` was hand-edited after generation. `generate.py` output doesn't match. Patch `generate.py` then regenerate if a full rebuild is needed.
- **`alert_count_24h()` scans full alerts.json**: Every 1-second cycle parses the entire file (~65K+ lines). Slow and CPU-heavy.
- **`alert_count_l3plus`**: Extra field in `data.json` not from either generator or updater — added dynamically at some point.
- **No auth on dashboard**: `python3 -m http.server` has no authentication. Bounded to 127.0.0.1 only.
- **No TLS**: ntfy.sh endpoint is unauthenticated HTTP. Anyone with the topic ID can post to it.

### What's Verified Working
1. Security events flow: Windows → Wazuh manager → alerts.log + alerts.json
2. ntfy relay: level 3+, 50+ rules, dedup 300s, plain-English, [TRUSTED] tagging
3. Dashboard: live metrics (CPU/RAM/Disk/GPU/services/alerts) updated every 1s
4. Browser: polls data.json + alerts.json every 3s, updates DOM in-place, no page reloads
5. Injection relay: monitors Hermes audit log, posts HIGH-risk events
6. Heartbeat watchdog: checks data freshness + relay health every 5 min
7. Rule 92213: false-positive filtered via PCRE2 negation
8. Rules 872001-872015: hardware, FIM, remote access, account changes — loaded and active
9. Custom rules 871001-871008: brute-force/suspicious-process — loaded, separate file
10. Sysmon full telemetry: 411 level-0 rules overridden to level 3

### What's Missing / Deferred
1. **End-to-end phone alert test for new rule IDs** — queue after relay stabilizes
2. **Relay health timer fix** — NOPASSWD sudoers entry for systemctl or disable timer
3. **Dashboard HTML regeneration** — align served index.html with generate.py output
4. **alert_count_24h performance** — cache or index instead of full file scan
5. **Wazuh Dashboard** — optional visual interface, not needed for single PC
6. **Multi-host support** — currently monitors only this single Windows host
7. **Agent IP reporting** — cosmetic (172.28.176.1 vs actual host IP)


## Related
- [[MOC.md|Map of Content]]
- [[nodes/topics/tech/pc-security.md|PC Security]]
