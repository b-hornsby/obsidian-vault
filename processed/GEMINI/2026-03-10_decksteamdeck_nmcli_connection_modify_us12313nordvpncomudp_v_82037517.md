---
category: homelab
date: 2026-03-10
id: 205150
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to set VPN remote server and CA certificate via nmcli but
  getting 'No valid secrets' errors on Steam Deck.
tags:
- steam-deck
- nordvpn
- nmcli
- vpn-secrets
- openvpn-config
---
# (deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp +vpn.data "remote=us12313.nordvpn.com:1194"
(deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp vpn.data "ca=/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn"
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### USER
(deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp +vpn.data "remote=us12313.nordvpn.com:1194"
(deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp vpn.data "ca=/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn"
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: No valid secrets
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### GEMINI
Look at the order of your commands. When you ran the second nmcli command with vpn.data, you didn't use the + sign. On Linux, that overwrote all the flags we just set (including the password-flags and the remote server) with just the certificate path. That's why "No valid secrets" came back—you accidentally wiped the login instructions. Since you've been working with CachyOS and complex terminal environments, you know that one missing character can reset your progress. Let's fix the configuration properly and permanently. The "One-Shot" Correction Run this exact block. It forces every setting back into place in one go so nothing gets overwritten: nmcli connection modify us12313.nordvpn.com.udp \ vpn.user-name "YOUR_SERVICE_USERNAME" \ vpn.secrets "password=YOUR_SERVICE_PASSWORD" \ vpn.data "connection-type=password, password-flags=0, remote=us12313.nordvpn.com:1194, ca=/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn" The "Permissions" Lock NetworkManager sometimes refuses to use a VPN if it thinks it can't "own" the connection. Run this to make it system-wide: sudo nmcli connection modify us12313.nordvpn.com.udp connection.permissions "" Try to connect: nmcli connection up us12313.nordvpn.com.udp Why this is the fix The Overwrite: The previous command replaced your entire vpn.data block. By putting connection-type=password, password-flags=0, and remote all in one string, we ensure the system knows exactly what to do. The Secret: By including vpn.secrets, we satisfy the "No valid secrets" error. The Remote: By including remote, we solve the --nobind crash we saw in your logs. A Brutally Honest Reminder Double-check your Service Credentials (the long random strings). If you use your regular Nord email, the terminal will give you the same "secrets" error because the server is rejecting the login attempt. Does it finally show "Connection successfully activated"?
