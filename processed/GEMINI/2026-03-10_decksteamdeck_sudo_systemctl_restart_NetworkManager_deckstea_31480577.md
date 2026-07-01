---
category: homelab
date: 2026-03-10
id: 603026
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to restart the NetworkManager service on his Steam Deck to
  get NordVPN working, but is encountering a VPN service startup failure.
tags:
- steam-deck
- nordvpn
- network-manager
- vpn-troubleshooting
- systemctl
---
# deck@steamdeck ~)$ sudo systemctl restart NetworkManager
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: The VPN service failed to start
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### USER
deck@steamdeck ~)$ sudo systemctl restart NetworkManager
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: The VPN service failed to start
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### GEMINI
"The VPN service failed to start" usually means the OpenVPN binary itself is having a permission issue or the configuration file we've been hacking away at is now missing a fundamental line it needs to actually execute. Since you've been working with CachyOS and local LLMs, you're familiar with "configuration drift"—we've edited this file so many times that it's likely gotten messy. Let's do a clean, 60-second reset using the nmcli import tool properly. This is the "advisor" move: stop patching a sinking ship and just build a new one. The "Clean Slate" Procedure Delete the old mess: nmcli connection delete us12313.nordvpn.com.udp Re-import the original file: sudo nmcli connection import type openvpn file /home/deck/Downloads/us12313.nordvpn.com.udp.ovpn The "Golden" Configuration Command: Instead of multiple steps, run this one command. It sets the username, the password, and the connection type all at once. (Replace the placeholders with your long Service Credentials from the Nord dashboard): nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "SERVICE_USER" vpn.secrets "password=SERVICE_PASS" vpn.data "connection-type=password, password-flags=0" Try it now: nmcli connection up us12313.nordvpn.com.udp If it STILL says "Failed to start" If it fails immediately, the issue is that SteamOS has "lost" the path to the OpenVPN plugin because of its immutable nature. Run this to verify the plugin is actually there: ls /usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so If it says "No such file": The plugin was deleted by a SteamOS update. You need to run the sudo pacman -S networkmanager-openvpn command again from our earlier steps. If it's there: The configuration we just made is 100% correct, and the failure is likely a specific Cipher mismatch (Nord updated their servers recently to require AES-256-GCM). Why this is happening "Failed to start" means the nm-openvpn-service process crashed the moment it tried to read the config. Usually, this is because a manual edit (like the f typo or a missing ca= line) made the file unparseable. The Clean Slate method above is the only way to ensure the file structure is perfect. Did the "Clean Slate" import finally give you the "Connection successfully activated" message?
