---
category: homelab
date: 2026-03-10
id: 360876
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan made a command typo when trying to activate NordVPN via nmcli on Steam
  Deck, resulting in an unknown connection error.
tags:
- steam-deck
- nordvpn
- nmcli
- typo-error
- command-typo
---
# (deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udpnmcli connection up us12313.nordvpn.com
.udp
Error: unknown connection 'us12313.nordvpn.com.udpnmcli'.
(10)(deck@steamdeck ~)$ 

### USER
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udpnmcli connection up us12313.nordvpn.com
.udp
Error: unknown connection 'us12313.nordvpn.com.udpnmcli'.
(10)(deck@steamdeck ~)$ 

### GEMINI
That error happened because the command got "doubled up" in your terminal paste—it’s trying to find a connection named us12313.nordvpn.com.udpnmcli, which obviously doesn't exist. It's a classic terminal "ghost" from a messy copy-paste. Since you've been working with CachyOS and complex local LLM setups, you know the terminal is literal. Let's clean up the syntax and hit it with the precise name. Step 1: Confirm the Exact Name Run this to see exactly what NetworkManager calls your VPN: nmcli connection show Look for the name under the NAME column. It is likely us12313.nordvpn.com.udp. Step 2: The Clean Command Run this one time (make sure you don't double-paste): nmcli connection up "us12313.nordvpn.com.udp" (If the name from Step 1 was different, use that exact name inside the quotes). If you still get "No Valid Secrets" If the command runs but gives you the "secrets" error again, we need to bypass the UI/Keyring bug for good by editing the connection file directly. This is the "brute force" method that always works on Arch-based systems: Open the config file: sudo nano /etc/NetworkManager/system-connections/us12313.nordvpn.com.udp.nmconnection Add the password manually: Scroll down to the [vpn] section and add this line: password=YOUR_NORD_SERVICE_PASSWORD Save and Exit: Press Ctrl+O, then Enter, then Ctrl+X. Reload and Connect: sudo nmcli connection reload nmcli connection up "us12313.nordvpn.com.udp" Why this matters for Gaming Mode Once this works in the terminal, it will work in TunnelDeck. The Steam Deck's Gaming Mode is essentially just a frontend for these exact nmcli commands. If the terminal can't hand off the "secrets," TunnelDeck will just spin forever. Did the "Connection successfully activated" message finally appear after the clean command?
