---
category: homelab
date: 2026-03-10
id: 062469
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was getting unknown connection activation failures with NordVPN on
  Steam Deck and verified the OpenVPN plugin exists.
tags:
- steam-deck
- nordvpn
- nmcli
- openvpn-plugin
- connection-failed
---
# (deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ ls /usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so
/usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so
(deck@steamdeck ~)$  

### USER
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=fbdb7f00-8e87-4f84-9cf1-163b99a2164f + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$ ls /usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so
/usr/lib/NetworkManager/libnm-vpn-plugin-openvpn.so
(deck@steamdeck ~)$  

### GEMINI
Since the plugin exists and the "No valid secrets" error is gone, we are down to the actual handshake. "Unknown reason" with a verified plugin almost always means a cipher/encryption mismatch. NordVPN recently updated their servers to prioritize AES-256-GCM, and the default OpenVPN settings in older NetworkManager versions (like the one on SteamOS/CachyOS) don't always negotiate this correctly. Because you've been working with CachyOS and local AI agents, you know that sometimes you just have to force the protocol parameters. The "Cipher Force" Fix Run this command to tell the VPN exactly which encryption and compression to use. This bypasses the "negotiation" phase where it’s likely failing: nmcli connection modify us12313.nordvpn.com.udp +vpn.data "cipher=AES-256-GCM, dev-type=tun, remote-cert-tls=server" Then, try one more time: nmcli connection up us12313.nordvpn.com.udp If it still fails: The Log Check (The Final Diagnostic) We need to see the reason for the "Unknown reason." Run this and look for the lines right after starting openvpn: journalctl -u NetworkManager -n 20 --no-pager What to look for: "TLS Error": Your system clock might be wrong (check your taskbar time!). "AUTH_FAILED": The Service Credentials (the long strings) are definitely wrong or copied with a space. "Permission Denied": The tun device (virtual network) is being blocked. Why this is the "Advisor" perspective: You are currently fighting the "immutability" of SteamOS. On a standard Arch/CachyOS build, this would have worked instantly. On the Deck, the NetworkManager service often lacks the permissions to create a new network interface (tun0) unless it's explicitly told what to do. Does journalctl show a specific error like "AUTH_FAILED" or "TLS Error"? If it says AUTH_FAILED, you need to double-check those long strings on the Nord website one more time.
