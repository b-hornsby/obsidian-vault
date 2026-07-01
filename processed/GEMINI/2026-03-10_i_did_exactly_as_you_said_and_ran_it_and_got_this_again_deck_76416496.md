---
category: homelab
date: 2026-03-10
id: 713389
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is encountering a 'No valid secrets' error when trying to connect to
  NordVPN on his Steam Deck, despite following instructions.
tags:
- steam-deck
- nordvpn
- vpn-troubleshooting
- nmcli
- no-valid-secrets
---
# i did exactly as you said and ran it and got this again: (deck@steamdeck ~)$ sudo nmcli connection reload
nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### USER
i did exactly as you said and ran it and got this again: (deck@steamdeck ~)$ sudo nmcli connection reload
nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### GEMINI
The "No valid secrets" loop is happening because your configuration file is likely still missing the connection-type=password field. On Arch-based systems like the Steam Deck, the OpenVPN plugin is extremely picky—if you don't explicitly tell it the connection type is "password," it assumes you're using a certificate/key and tells you it has "no secrets" for that method. Since we’ve been through the ringer with the manual file edits, let’s use the nmcli tool to inject the missing flags directly. This is safer than hand-editing the text file. Step 1: Inject the Missing "Connection Type" Run this exact command in Konsole. This is the specific fix for the "BadArguments: Invalid connection type" error we saw in your logs: nmcli connection modify us12313.nordvpn.com.udp +vpn.data "connection-type=password" Step 2: Re-verify the Credentials Just to be 100% sure the system has the right strings, run these two: nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "YOUR_SERVICE_USERNAME" nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=YOUR_SERVICE_PASSWORD" Step 3: Clear the Cache and Fire Sometimes the NetworkManager process hangs onto the old, broken config in memory. sudo systemctl restart NetworkManager # Wait 5 seconds for your Wi-Fi to reconnect nmcli connection up us12313.nordvpn.com.udp If it still fails (The "Vibe Coding" Reality Check) If you get "No valid secrets" again, there is a core issue with how the .ovpn file was parsed. Here is the Fastest Reset: Delete the connection: nmcli connection delete us12313.nordvpn.com.udp Import fresh: nmcli connection import type openvpn file ~/Downloads/us12313.nordvpn.com.udp.ovpn Run this ONE command immediately after: nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "YOUR_USER" vpn.secrets "password=YOUR_PASS" vpn.data "connection-type=password, password-flags=0" Try to connect. Why this is happening The Steam Deck's version of the OpenVPN plugin is essentially a "lite" version. It doesn't always know how to handle the advanced metadata NordVPN puts in their files. By manually forcing connection-type=password, you’re stripping away the complexity and telling it to just use the strings you provided. Did Step 1 (adding the connection-type) finally let the handshake go through?
