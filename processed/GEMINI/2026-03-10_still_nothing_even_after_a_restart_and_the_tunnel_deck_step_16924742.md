---
category: homelab
date: 2026-03-10
id: 599918
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is still experiencing issues with NordVPN on his Steam Deck, even after
  restarting and following the 'tunnel deck' step.
tags:
- steam-deck
- nordvpn
- vpn-troubleshooting
- tunnel-deck
---
# still nothing even after a restart and the tunnel deck step

### USER
still nothing even after a restart and the tunnel deck step

### GEMINI
Since the "Manual Terminal Fix" didn't immediately reveal the VPN option, it’s likely because the NetworkManager service hasn't refreshed its available plugins, or the specific UI package for KDE (the Steam Deck's desktop) is missing. Because you are on a Steam Deck, we have to be aggressive with the manual commands. Let's force the installation of the GUI components and restart the network service specifically. Step 1: Force Install GUI Plugins Open Konsole in Desktop Mode and run these commands. I've added the gnome and libnm packages which are often the "missing link" for the UI to actually show the buttons: # Unlock the system sudo steamos-readonly disable # Refresh keys (skip if you did this already, but it doesn't hurt) sudo pacman-key --init sudo pacman-key --populate archlinux # Install the OpenVPN plugin AND the required network manager libraries sudo pacman -S networkmanager-openvpn nm-connection-editor libnm Step 2: Restart the Network Service Instead of a full reboot (which sometimes fails to "catch" new plugins on SteamOS), try restarting the network stack directly while in Desktop Mode. Run this in Konsole: sudo systemctl restart NetworkManager Step 3: Check the "Hidden" Menu Sometimes the option is there, but the KDE Settings menu is being stubborn. Try opening the connection editor directly via command: In Konsole, type: nm-connection-editor A small window should pop up. Click the + (Plus) icon at the bottom. Scroll to the very bottom. Do you see "Import a saved VPN configuration..." or "OpenVPN" here? The "Nuclear" Option (If the above fails) If SteamOS 3.5+ is refusing to show the menu, you can bypass the GUI entirely and import your NordVPN file via the terminal. This works even when the buttons are invisible: Make sure you have your .ovpn file from NordVPN saved (e.g., in your Downloads folder). Run this command (replace the path with your actual file path): sudo nmcli connection import type openvpn file /home/deck/Downloads/nord_server.ovpn If it says "Success", the connection is now in your system. You can then go to TunnelDeck in Gaming Mode, and it should see it there. When you ran the pacman -S command in Step 1, did it finish with "Total Installed Size..." or did it give you an error about "Target not found"?
