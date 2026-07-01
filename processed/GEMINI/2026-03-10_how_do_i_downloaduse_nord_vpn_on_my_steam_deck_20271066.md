---
category: homelab
date: 2026-03-10
id: 118085
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for instructions on how to download and use NordVPN on his
  Steam Deck.
tags:
- steam-deck
- nordvpn
- vpn-setup
- linux-vpn
---
# how do i download/use nord vpn on my steam deck

### USER
how do i download/use nord vpn on my steam deck

### GEMINI
Installing NordVPN on the Steam Deck is slightly different from Windows because SteamOS is an "immutable" system. While there is a native Linux app, it often breaks during SteamOS updates. The most reliable and "clean" method is to use the built-in Network Manager in Desktop Mode, then use a plugin to control it while gaming. Phase 1: Setup in Desktop Mode Set a Sudo Password: If you haven’t done this yet, open Konsole, type passwd, and follow the prompts to create a password. Get your Service Credentials: * Go to the Nord Account Dashboard. You need your Service Username and Service Password (these are different from your email login). Download Config Files: Visit the NordVPN Server Utility. Find a server you want and click Download Config. Choose the UDP file for better gaming speeds. Import the Connection: Click the Wi-Fi/Network icon in the bottom right tray. Click the Settings (gear icon) or "Configure Network Connections." Click the + (plus) button, scroll to the bottom, and select Import VPN connection... Select the .ovpn file you just downloaded. In the "VPN" tab, enter your Service Username/Password. Crucial: Change the "Password" dropdown setting to "Store password for all users (not encrypted)". This allows it to connect without asking for a password in Gaming Mode. Hit Apply. Phase 2: Use in Gaming Mode (TunnelDeck) To toggle the VPN on/off without leaving your game, you should use Decky Loader. Install Decky Loader: If you don't have it, run the installer from decky.xyz in Desktop Mode. Install TunnelDeck: * Switch back to Gaming Mode. Press the Quick Access Button (the ... button). Go to the Decky (plug icon) tab. Open the Store, search for TunnelDeck, and install it. Connect: Open TunnelDeck from the Decky menu. Toggle the switch for the NordVPN connection you just created. Critical Reminders Steam TOS: Technically, using a VPN to spoof your location to buy cheaper games is against Valve's Terms of Service and can get your account banned. It is generally safe for playing games or privacy, but never use it to purchase games. Updates: Because SteamOS is immutable, manual terminal-based installations of the NordVPN app usually get wiped after a system update. The Network Manager method above is more "update-proof." Would you like me to walk you through how to set up a specific "Kill Switch" so your internet cuts out if the VPN drops?
