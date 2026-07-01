---
category: homelab
date: 2026-03-10
id: 117466
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to reload the network connection on his Steam Deck to get
  NordVPN working, but is encountering an unknown error.
tags:
- steam-deck
- nordvpn
- network-manager
- vpn-troubleshooting
- nmcli
---
# (deck@steamdeck ~)$ sudo nmcli connection reload
nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### USER
(deck@steamdeck ~)$ sudo nmcli connection reload
nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Unknown reason
Hint: use 'journalctl -xe NM_CONNECTION=3304be90-7b07-4d8c-9038-fb23eed4f38a + NM_DEVICE=wlan0' to get more details.
(4)(deck@steamdeck ~)$  

### GEMINI
"Unknown reason" usually means the connection settings are now correct, but the OpenVPN handshake itself is failing. This often happens on the Steam Deck because the .ovpn file you imported is missing its CA certificate or the specific encryption settings Nord expects. Since you're comfortable with the terminal and "vibe coding" your way through CachyOS, let's look at the actual error log to stop guessing. Step 1: See the Real Error Run this command to see the last 50 lines of the network log. This will tell us exactly why the handshake failed (e.g., "TLS Error," "Cipher mismatch," or "Auth Failure"): journalctl -u NetworkManager -n 50 --no-pager Step 2: The Most Likely Fix (The Certificate) When you import an .ovpn file via nmcli, it sometimes fails to embed the CA Certificate. Without it, the VPN can't verify the server. Check your Downloads folder for the .ovpn file you used. Open that .ovpn file in KWrite (the text editor). Look for the <ca> section. It looks like a big block of random letters between <ca> and </ca>. If that block is missing or looks corrupted, that's your "Unknown reason." Step 3: Try the "Clean Slate" Import Sometimes the manual edits we did to fix the "Secrets" error messed up the internal routing of the connection. Let's try to import it one more time, but completely fresh: # Delete the broken one sudo nmcli connection delete us12313.nordvpn.com.udp # Re-import it (make sure you use the full path to your .ovpn) sudo nmcli connection import type openvpn file /home/deck/Downloads/us12313.nordvpn.com.udp.ovpn # Set ONLY the credentials this time using the direct 'vpn.data' method nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "YOUR_SERVICE_USERNAME" vpn.data "password-flags=0" nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=YOUR_SERVICE_PASSWORD" A Brutally Honest Pivot If journalctl shows a "TLS Error" or "Missing Plugin," it means the version of networkmanager-openvpn on your current SteamOS/CachyOS build is incompatible with the specific encryption Nord is using in that .ovpn file. Run the journalctl command from Step 1 and paste the last few lines here. I'll be able to tell you instantly if it's a certificate issue or a protocol mismatch.
