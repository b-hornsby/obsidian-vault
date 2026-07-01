---
id: 647728
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'desktop-mode', 'game-mode', 'nordvpn', 'mode-difference']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan noted that NordVPN worked fine in desktop mode but not in game mode on his Steam Deck.
---
# It worked perfectly fine in desktop mode that’s the thing

### USER
It worked perfectly fine in desktop mode that’s the thing

### GEMINI
If it works in Desktop Mode but fails in Gaming Mode/TunnelDeck, the problem isn't your credentials or the server—it's a permission and persistence conflict between the two environments. Here is the brutal reality: Desktop Mode uses a dedicated session manager (KDE Plasma) to handle your "secrets" (passwords). Gaming Mode does not. When you flip that switch in TunnelDeck, the system asks, "Where is the password?" and because it can't find the KDE keyring in Gaming Mode, it just gives up and toggles off. The "No-Nonsense" Fixes 1. The "All Users" Password Hack (Most Likely Fix) In Desktop Mode, your password is likely stored in your private "KWallet." Gaming Mode can't talk to KWallet. Go back to Desktop Mode > Network Settings. Select your VPN connection and go to the VPN (OpenVPN) tab. Look for the Password field. Click the small icon inside the text box (it usually looks like a person or a floppy disk). Select "Store password for all users (not encrypted)". Click Apply. Why this works: This moves the password from your encrypted vault into a plain-text file that Gaming Mode is actually allowed to read. 2. The IPv6 "Killer" Gaming Mode and Desktop Mode handle network handshakes differently. If IPv6 is enabled, Gaming Mode often tries to route traffic through it simultaneously, causing the VPN tunnel to collapse. In Desktop Mode > Network Settings, find your active Wi-Fi connection (not the VPN). Go to the IPv6 tab. Set "Method" to Disabled. Click Apply. 3. TunnelDeck "Sync" Issue Sometimes TunnelDeck holds onto a "ghost" version of your configuration. Go to Gaming Mode. Open the Decky Menu > TunnelDeck. If your VPN is listed, remove it or hit the refresh icon if available. Restart your Steam Deck (don't just sleep/wake). A full reboot forces the system to re-scan the Network Manager files you edited in Step 1. The Reality Check If you’ve done the "Store password for all users" step and it still fails, you are likely hitting a DNS leak protection loop. SteamOS’s Gaming Mode is notoriously aggressive about maintaining its own DNS. Check this: When you are in Desktop Mode with the VPN ON, go to dnsleaktest.com. If it shows your real ISP's location anywhere, the VPN isn't actually "working perfectly"—it's leaking, and Gaming Mode is smart enough to see that as a broken connection and kill it. Would you like me to show you how to hard-code Nord's DNS into your Wi-Fi settings to stop that loop?
