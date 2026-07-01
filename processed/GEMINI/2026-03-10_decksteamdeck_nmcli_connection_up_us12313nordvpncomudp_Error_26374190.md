---
category: homelab
date: 2026-03-10
id: 414327
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was getting 'No valid secrets' errors when trying to activate NordVPN
  via nmcli on Steam Deck.
tags:
- steam-deck
- nordvpn
- nmcli
- no-valid-secrets
- vpn-auth
---
# (deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ 

### USER
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ 

### GEMINI
The "No valid secrets" error is the classic NetworkManager headache on Arch/SteamOS. It means the system is trying to pull your password from a "keyring" (like a digital vault) that isn't unlocked or doesn't exist in the terminal environment. Since you're used to "vibe coding" and manual Linux ricing, we’re going to bypass the vault entirely and bake the credentials directly into the connection file so it stops asking for "secrets" it can't find. Step 1: Force the Password into the Config Run these three commands in Konsole. This tells NetworkManager: "Don't look in the vault, the password is right here." # 1. Tell it to use its own internal storage for the password nmcli connection modify us12313.nordvpn.com.udp vpn.data "password-flags=0" # 2. Hard-code the Service Password (from your Nord Dashboard) nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=YOUR_SERVICE_PASSWORD" # 3. Ensure the VPN service knows to look for a 'password' variable nmcli connection modify us12313.nordvpn.com.udp vpn.data "password-flags=0, username=YOUR_SERVICE_USERNAME" Step 2: The "Owner" Fix Sometimes the connection fails because it’s restricted to the "deck" user, but the system service runs as "root." Let's make it available to everyone: sudo nmcli connection modify us12313.nordvpn.com.udp connection.permissions "" Step 3: Test the Handshake Now, try to bring it up again: nmcli connection up us12313.nordvpn.com.udp If it STILL says "No valid secrets" This is a known bug where the OpenVPN plugin ignores the nmcli secrets. If it fails again, we do it the "Brute Force" way: Open Konsole and type: sudo nano /etc/NetworkManager/system-connections/us12313.nordvpn.com.udp.nmconnection Look for a section called [vpn]. Add this line under the [vpn] section: password=YOUR_SERVICE_PASSWORD Press CTRL+O, Enter, then CTRL+X to save. Reload the connections: sudo nmcli connection reload Try nmcli connection up us12313.nordvpn.com.udp one last time. Did that finally give you the "Connection successfully activated" message?
