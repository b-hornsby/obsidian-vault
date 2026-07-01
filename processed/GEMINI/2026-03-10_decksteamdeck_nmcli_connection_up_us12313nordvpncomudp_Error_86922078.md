---
category: homelab
date: 2026-03-10
id: 608374
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was repeatedly getting 'No valid secrets' errors when trying to connect
  to NordVPN via nmcli on Steam Deck.
tags:
- steam-deck
- nordvpn
- nmcli
- no-valid-secrets
- vpn-authentication
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
The "No valid secrets" loop is essentially a refusal by NetworkManager to look at the password you provided because it doesn't "trust" the storage method on an immutable system like the Steam Deck. Since you're used to the brutal honesty of Linux ricing and local LLM configurations, here is the unfiltered truth: the GUI and standard nmcli commands are failing because the KDE Wallet (the secret keeper) is likely dormant or disconnected. We are going to bypass the "secrets" system entirely by making the connection file file-based rather than keyring-based. The "Nuclear" Configuration Fix Run these commands in Konsole to force the connection to look at the file, not the vault. Open the configuration file: sudo nano /etc/NetworkManager/system-connections/us12313.nordvpn.com.udp.nmconnection Delete the existing [vpn] and [vpn-secrets] sections and replace them with this exact block (use your Nord Service Credentials, not your email): [vpn] connection-type=password password-flags=0 service-type=org.freedesktop.NetworkManager.openvpn username=YOUR_SERVICE_USERNAME [vpn-secrets] password=YOUR_SERVICE_PASSWORD Check the [connection] section at the top. Ensure it has this line: permissions= (If it says permissions=user:deck:;, delete everything after the equals sign so it's blank. This allows the system-level VPN service to read it). Save and Exit: Ctrl+O, Enter, Ctrl+X. Force a Reload and Permission Reset: sudo chmod 600 /etc/NetworkManager/system-connections/us12313.nordvpn.com.udp.nmconnection sudo nmcli connection reload The Ultimate Test: nmcli connection up us12313.nordvpn.com.udp Why this is the "Pro" way On CachyOS or SteamOS, the "Secrets" error usually means the gnome-keyring or kwallet isn't responding to the terminal. By setting password-flags=0 and putting the password in [vpn-secrets] inside a 600 permission file, you are telling Linux: "I am the vault. Use this string." What if it still fails? If it still says "No valid secrets," it means the networkmanager-openvpn plugin itself is crashing or missing a dependency on your specific CachyOS/SteamOS build. Does the terminal finally say "Connection successfully activated," or are we still hitting the "secrets" wall?
