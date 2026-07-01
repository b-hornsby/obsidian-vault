---
id: 335962
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'ovpn-file', 'vpn-setup']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was listing NordVPN OVPN files on his Steam Deck to begin VPN setup.
---
# (1)(deck@steamdeck ~)$ ls ~/Downloads/*.ovpn
/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn
(deck@steamdeck ~)$  

### USER
(1)(deck@steamdeck ~)$ ls ~/Downloads/*.ovpn
/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn
(deck@steamdeck ~)$  

### GEMINI
Perfect. Now that we have the exact path, we’re going to force the import. Since you've been "vibe coding" and working with local LLMs, you know the terminal doesn't care about missing UI buttons—it just executes. Let’s finish this. Step 1: Import the Connection Run this exact command (I've updated it with your specific filename): sudo nmcli connection import type openvpn file /home/deck/Downloads/us12313.nordvpn.com.udp.ovpn Step 2: Set Your Service Credentials After the import succeeds, you need to tell the system who you are. Crucial: Use your NordVPN Service Credentials (the long strings of characters from the Nord dashboard), not your email. Run these two commands: # Set the username nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "YOUR_SERVICE_USERNAME" # Set it to store the password so Gaming Mode doesn't hang nmcli connection modify us12313.nordvpn.com.udp vpn.data "password-flags=0" Step 3: Input the Password Now, try to bring the connection up. It will prompt you for the Service Password in the terminal: nmcli --ask connection up us12313.nordvpn.com.udp Why the UI was "invisible" On Arch-based systems like CachyOS or SteamOS, the KDE Plasma network applet often fails to show the "Add VPN" button if the networkmanager-openvpn plugin wasn't properly registered with the D-Bus service at startup. By using nmcli, we are talking directly to the NetworkManager backend, bypassing the broken UI entirely. Verification Once that command finishes, switch back to Gaming Mode: Open the Quick Access Menu (... button). Go to TunnelDeck. us12313.nordvpn.com.udp should now be sitting there, ready to be toggled on. Did the nmcli import give you a "Success" message this time, or did it throw a "plugin not found" error?
