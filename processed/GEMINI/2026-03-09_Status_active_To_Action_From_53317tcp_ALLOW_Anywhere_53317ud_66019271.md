---
id: 756195
source: GEMINI
date: 2026-03-09
tags: ['firewall-rules', 'port-configuration', 'network-security', 'ufw']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is showing the status of firewall rules, specifically allowing traffic on port 53317.
---
# Status: active

To                         Action      From
--                         -
---
--      -
---
53317/tcp                  ALLOW       Anywhere                   
53317/udp                  ALLOW       Anywhere                   
53317/tcp (v6)             ALLOW       Anywhere (v6)              
53317/udp (v6)             ALLOW       Anywhere (v6)              


~
❯ 

### USER
Status: active

To                         Action      From
--                         -
---
--      -
---
53317/tcp                  ALLOW       Anywhere                   
53317/udp                  ALLOW       Anywhere                   
53317/tcp (v6)             ALLOW       Anywhere (v6)              
53317/udp (v6)             ALLOW       Anywhere (v6)              


~
❯ 

### GEMINI
There is your culprit. Your firewall is active and it isn't currently letting anything through on port 4455. On a performance-tuned distro like CachyOS, the security defaults are often tighter than you'd expect. Even though it's "local" traffic, ufw can still block the handshake if it isn't explicitly told to allow it. The Fix Run this to open the door for OBS: sudo ufw allow 4455/tcp The "Advisor" Moment: Strategy vs. Speed You’re currently playing "Whack-A-Mole" with your settings. You want to get back to gaming and building your DeFi bot, not auditing firewall rules. Here is the objective truth: If you're going to use CachyOS as a workstation for streaming and development, you need to decide if you want to keep ufw active at all. If you're behind a standard home router, the router's firewall is already doing the heavy lifting. A software firewall on your local machine is often just a source of friction for things like OBS WebSockets, KDE Connect, or local LLM APIs. If you want to keep it on for security, run the allow command above. If you want to stop troubleshooting network ports for local apps, you can disable it: sudo ufw disable Final Verification Once you've allowed the port or disabled the firewall, run the "naked" command again: obs-cmd replay save If it works, you are officially ready to bind this to your system hotkey. Open System Settings -> Shortcuts -> Commands. Set the command to obs-cmd replay save. Pick your keybind. Profit. (And get back to Apex). Would you like me to show you how to set up a "Replay Buffer Toggle" script so you can turn the recording feature on and off with one button?
