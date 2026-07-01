---
id: 357947
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'clean-setup', 'vpn-troubleshooting', 'fresh-start']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan decided to wipe his NordVPN setup and start from scratch on Steam Deck.
---
# Okay let’s back all this up and start from getting the old setup deleted and start from scratch with this vpn setup

### USER
Okay let’s back all this up and start from getting the old setup deleted and start from scratch with this vpn setup

### GEMINI
Since you want a clean start with a setup that actually works in Gaming Mode, we’re going to perform a complete sweep of the old OpenVPN junk and move to WireGuard (NordLynx). WireGuard is the "gold standard" for the Steam Deck in 2026. It doesn't need a password after the first setup, it's faster, and it doesn't "break" when you switch to Gaming Mode. Phase 1: The Total Purge Let's wipe the slate clean so old settings don't conflict with the new ones. Open Konsole in Desktop Mode: # 1. Delete the broken connection nmcli connection delete us12313.nordvpn.com.udp # 2. Stop any hanging OpenVPN processes sudo killall openvpn # 3. Clean the NetworkManager cache sudo systemctl restart NetworkManager Phase 2: Get your WireGuard "Key" (The Modern Way) We need a Private Key. Nord doesn't just hand these out, so we use a quick tool to generate it. Go to this site in your Steam Deck browser: https://nord-configs.selfhoster.nl/ Note: This is a community-trusted tool for 2026 that converts your Nord "Access Token" into a WireGuard file. Get an Access Token: Log in to your Nord Account Dashboard. Go to NordVPN -> Manual Setup -> Generate Token. Generate the File: Paste that token into the website. Select a server (e.g., United States). Click Generate/Download. You will get a .conf file (like us1234.conf). Phase 3: The "Bulletproof" Import Now we put that file into the system in a way that Gaming Mode can't mess up. Go to System Settings > Connections (the Wi-Fi icon in the taskbar). Click the + (Plus) button at the bottom left. Scroll to the very bottom and select Import VPN connection... Pick the .conf file you just downloaded. THE MOST IMPORTANT PART: Click on your new connection (e.g., us1234). Go to the General Configuration tab. Check the box: "All users may connect to this network." Check the box: "Automatically connect to VPN when using this connection" (Optional, if you want it always on). Click Apply. Phase 4: Enable in Gaming Mode Switch back to Gaming Mode. Open TunnelDeck in the Decky menu. You will see your new WireGuard connection listed. Toggle it ON. Why this is the "Last Setup You'll Ever Need" Zero Handshake: Unlike OpenVPN, WireGuard doesn't "log in" every time. It just starts sending packets. No more "No valid secrets" errors. Battery Life: WireGuard is much lighter on the Steam Deck's CPU than OpenVPN. Sticky: Because you checked "All users may connect," the SteamOS background service has full permission to keep that tunnel alive. Once you import that .conf file and check the "All users" box, does the toggle finally stay green in Gaming Mode?
