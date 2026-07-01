---
category: homelab
date: 2026-03-10
id: 776980
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan was configuring NordVPN connection settings via nmcli on Steam Deck
  and getting connection activation failures.
tags:
- steam-deck
- nordvpn
- nmcli
- openvpn
- vpn-configuration
---
# (deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp +vpn.data "cipher=AES-256-GCM, dev-type=tun, remote-cert-tls=server"
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ 

### USER
(deck@steamdeck ~)$ nmcli connection modify us12313.nordvpn.com.udp +vpn.data "cipher=AES-256-GCM, dev-type=tun, remote-cert-tls=server"
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ 

### GEMINI
"Unknown reason" is the terminal's way of saying the connection started, but the server kicked you back out. Since we've verified the plugin is there and the config file is clean, we are down to the two most common "silent killers" on the Steam Deck: incorrect service credentials or a broken certificate path. Let's look at the actual handshake logs to stop the guessing game. Run this: journalctl -u NetworkManager -n 30 --no-pager What to look for in that output: AUTH_FAILED: This is the #1 culprit. It means the long strings you got from the Nord website aren't being accepted. (Make sure there are no accidental spaces at the end of the username or password). TLS Error / Certificate verify failed: This means the CA certificate we tried to bake into the file isn't working. The "Safe Bet" Reset If the logs are messy, let's try the most robust way to handle the credentials. We'll use the interactive editor to ensure the strings are "pure" and not being messed up by the command line's formatting: Enter the editor: nmcli connection edit us12313.nordvpn.com.udp Clear and set the username: set vpn.user-name YOUR_LONG_SERVICE_USERNAME Clear and set the password: set vpn.secrets password=YOUR_LONG_SERVICE_PASSWORD Save and exit: save then quit Try once more: nmcli connection up us12313.nordvpn.com.udp One Brutally Honest Check Since you've been working on CachyOS lately: is your Steam Deck's system time and date correct? If your clock is even a few minutes off, the security certificates will fail to validate, and the VPN will give you an "Unknown reason" error every single time. What do those last 30 lines of journalctl say? (Specifically, look for any lines containing nm-openvpn or AUTH).
