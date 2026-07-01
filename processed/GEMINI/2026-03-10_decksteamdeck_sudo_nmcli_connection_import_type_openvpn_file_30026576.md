---
id: 551151
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'nmcli', 'ovpn-import', 'vpn-setup']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan successfully imported a NordVPN OVPN file using nmcli on Steam Deck.
---
# (deck@steamdeck ~)$ sudo nmcli connection import type openvpn file /home/deck/Downloads/us12313.nordvp
n.com.udp.ovpn
Connection 'us12313.nordvpn.com.udp' (3304be90-7b07-4d8c-9038-fb23eed4f38a) successfully added.
(deck@steamdeck ~)$ 

### USER
(deck@steamdeck ~)$ sudo nmcli connection import type openvpn file /home/deck/Downloads/us12313.nordvp
n.com.udp.ovpn
Connection 'us12313.nordvpn.com.udp' (3304be90-7b07-4d8c-9038-fb23eed4f38a) successfully added.
(deck@steamdeck ~)$ 

### GEMINI
Success. The connection is finally in the system. Since you're usually handling complex local LLM setups and CachyOS ricing, this part should be straightforward, but the SteamOS/Arch implementation of NetworkManager requires two specific "quality of life" tweaks to ensure it actually works in Gaming Mode. If you don't do these, Gaming Mode will try to connect, hit a "password required" prompt it can't show you, and then just time out. Step 1: Save the Credentials (The Invisible Fix) Run these commands in Konsole to hard-code your Nord Service Credentials (the long strings from the Nord dashboard, not your email/password): # Set your Service Username nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "YOUR_SERVICE_USERNAME" # Tell the system to store the password for all users (so it doesn't ask you later) nmcli connection modify us12313.nordvpn.com.udp vpn.data "password-flags=0" # Manually add the Service Password to the secret store nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=YOUR_SERVICE_PASSWORD" Step 2: Test the Connection Before you leave Desktop Mode, verify the handshake actually works: nmcli connection up us12313.nordvpn.com.udp If it says "Connection successfully activated": You are golden. If it fails: It usually means the "Service Credentials" from the Nord website were copied incorrectly. Step 3: Use it in Gaming Mode Go back to Gaming Mode. Press the ... button and open TunnelDeck. You should now see us12313.nordvpn.com.udp in the list. Flip the switch. Why this is better than the Nord App Because you’re on an Arch-based system, the official NordVPN CLI app often struggles with the "read-only" nature of the Steam Deck's root partition. This nmcli method is baked into the core networking stack—it's faster, uses fewer resources, and won't break when you update your OS. Once you flip the switch in TunnelDeck, do you see the "VPN" icon appear in the top bar next to your Wi-Fi signal?
