---
category: homelab
date: 2026-03-10
id: 905389
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered a file-not-found error when trying to import a NordVPN
  OVPN file on Steam Deck.
tags:
- steam-deck
- nordvpn
- ovpn-import
- file-not-found
- vpn-error
---
# Error: failed to import '/home/deck/Downloads/nord_server.ovpn': Failed to open file “/home/deck/Downl
oads/nord_server.ovpn”: No such file or directory.
(1)(deck@steamdeck ~)$ 

### USER
Error: failed to import '/home/deck/Downloads/nord_server.ovpn': Failed to open file “/home/deck/Downl
oads/nord_server.ovpn”: No such file or directory.
(1)(deck@steamdeck ~)$ 

### GEMINI
The error is literal: the terminal can't find that specific file because the filename isn't exactly nord_server.ovpn. NordVPN usually names their files something like us8232.nordvpn.com.udp.ovpn. Since you're on CachyOS (or SteamOS, which is also Arch-based), the terminal is your best friend here if the UI is glitching. Let's fix the pathing and get this imported. Step 1: Find the Actual Filename Run this command to see the exact name of the file you downloaded: ls ~/Downloads/*.ovpn Copy the full name that appears in the results (it will likely be a long string of letters and numbers). Step 2: Run the Import with the Correct Name Type sudo nmcli connection import type openvpn file and then drag and drop the .ovpn file from your file manager (Dolphin) directly into the terminal window. It will automatically paste the correct path for you. It should look something like this: sudo nmcli connection import type openvpn file /home/deck/Downloads/us9231.nordvpn.com.udp.ovpn Step 3: Add Your Credentials Once it says "Connection 'nord_server' successfully added", you need to give it your Service Credentials (not your email login). Run this: nmcli connection modify "NAME_OF_CONNECTION" vpn.user-name "YOUR_SERVICE_USERNAME" (Replace NAME_OF_CONNECTION with whatever the import called it—usually the filename without the .ovpn). If it still says "No such file or directory" Open your Downloads folder in the file manager. Right-click the .ovpn file and select Rename. Rename it to something simple like nord.ovpn. Run: sudo nmcli connection import type openvpn file ~/Downloads/nord.ovpn Why the UI is failing you Since you mentioned using CachyOS recently, keep in mind that if you are playing with KDE Plasma "ricing" or custom themes, it can sometimes break the Network Manager applet's ability to show VPN sub-menus. The nmcli (command line) method bypasses the broken UI entirely. Once that command says "Success," check TunnelDeck in Gaming Mode again. Does it show up in the list now?
