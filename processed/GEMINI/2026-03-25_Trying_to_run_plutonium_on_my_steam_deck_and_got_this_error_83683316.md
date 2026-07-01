---
category: general
date: 2026-03-25
id: 680970
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to run Plutonium (a Call of Duty mod/server tool) on his
  Steam Deck and encountered an error he needed help with.
tags:
- steam-deck
- plutonium
- gaming
- error-troubleshooting
---
# Trying to run plutonium on my steam deck and got this error? 

### USER
Trying to run plutonium on my steam deck and got this error? 

### GEMINI
This error message on Plutonium is a specific flag indicating that your connection is being routed through a "banned service"—most commonly a VPN, Proxy, or a Cloud Gaming relay. Plutonium’s anti-cheat and security measures automatically block these services to prevent ban evasion and malicious traffic. Since you are on a Steam Deck, the most likely culprits are how your network is configured or a specific privacy tool you have running in the background. Why this is happening Active VPN: If you have a VPN installed via Desktop Mode (or a Decky Loader plugin), Plutonium will detect the server IP and block the connection. Custom DNS/Cloudflare Warp: Sometimes specialized DNS services that mask your identity are flagged as proxies. Public/Shared WiFi: If you are on a university or corporate network, the entire outbound IP might be flagged as a "service" rather than a residential connection. iCloud Private Relay (if applicable): If you've bridged settings from an Apple device or are using similar relay services, this triggers the block. The Reality Check & Fixes If you want to play, you have to stop trying to mask your connection. Here is the prioritized plan to fix this: Kill the VPN: Go into Desktop Mode and ensure no VPN clients (WireGuard, OpenVPN, Mullvad, etc.) are active. This is the cause 90% of the time. Disable Decky Plugins: If you use "TunnelDeck" or similar networking plugins, turn them off entirely. Check your DNS: Reset your Steam Deck’s connection to use default ISP DNS or Google DNS ($8.8.8.8$). If you’ve set up a system-wide proxy to bypass regional restrictions, Plutonium won't let you in. Test on a Mobile Hotspot: To rule out your home network being the "banned service," connect your Deck to your phone's data. If it works, your home ISP or router configuration is the issue. The Bottom Line: You are being blocked because your traffic looks anonymous or automated. Provide a "clean" residential IP connection, and the error will vanish. Would you like me to walk you through how to reset the network configuration in SteamOS Desktop Mode?
