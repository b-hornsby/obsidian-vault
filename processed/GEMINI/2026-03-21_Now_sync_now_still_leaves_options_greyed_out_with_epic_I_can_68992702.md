---
category: general
date: 2026-03-21
id: 461586
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing issues with Epic Launcher, specifically with account
  synchronization and 2FA, preventing him from accessing his account.
tags:
- epic-launcher
- 2fa-issues
- account-sync
- authentication-problems
---
# Now sync now still leaves options greyed out with epic I can’t even do email

### USER
Now sync now still leaves options greyed out with epic I can’t even do email

### GEMINI
If the "Sync now" button is spinning or the Epic options are greyed out, your new Tiny 11 install is likely hitting a Network/DNS Wall. Epic's login service is extremely sensitive to how your system talks to its authentication servers. As an operations professional, you know that if the "front gate" (2FA) isn't responding, it’s usually because the communication line is noisy. 1. The "DNS Flush" (The IT Specialist's Move) Sometimes a fresh install holds onto "dirty" network routes. Force a clean connection: Open Command Prompt (Admin). Type these one by one and hit Enter: ipconfig /flushdns netsh winsock reset Reboot the machine immediately. 2. The "Cloudflare" Fix (Bypassing ISP Lag) Your ISP's default DNS might be slow to update after your "Nuclear" wipe, causing Epic's 2FA request to time out before it even reaches you. Go to Settings > Network & Internet > Ethernet/Wi-Fi. Select Edit next to DNS server assignment. Change it from "Automatic" to Manual. Toggle IPv4 to On and enter: Preferred DNS: 1.1.1.1 Alternate DNS: 1.0.0.1 Save and try the Epic Launcher again. 3. The "Clock Reset" Mirror If the "Sync now" button was greyed out, your Time Zone might be set incorrectly for your physical location. Make sure the Time Zone is set to (UTC-05:00) Eastern Time (US & Canada). If it’s set to "London" or "UTC" by default, your 2FA code is technically 5 hours in the future or past, and Epic will reject it every single time. The Brutally Honest Reality You’ve spent all day fixing "low-level" infrastructure. Don't let a "high-level" software glitch like a 2FA code tilt you. This is just the final paperwork of the move. Once the time and DNS are synced, the "warehouse" is officially open. Did changing the DNS to 1.1.1.1 allow the Epic Launcher to finally "see" the 2FA request?
