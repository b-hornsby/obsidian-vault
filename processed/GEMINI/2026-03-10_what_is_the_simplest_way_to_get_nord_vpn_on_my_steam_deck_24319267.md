---
id: 990226
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'simple-setup', 'vpn-install', 'beginner']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking for the simplest method to get NordVPN running on his Steam Deck.
---
# what is the simplest way to get nord vpn on my steam deck?

### USER
what is the simplest way to get nord vpn on my steam deck?

### GEMINI
Getting NordVPN on a Steam Deck is slightly tricky because the official Linux app isn't a simple "install and click" affair on SteamOS. The simplest method—meaning the one with the least technical headache that won't break when your Steam Deck updates—is to use the built-in Network Manager in Desktop Mode. Method 1: The "Simple" Way (Importing a Config File) This uses SteamOS's native networking tools. It’s stable and doesn't require disabling system protections. Get your Credentials: Go to the NordVPN Account Dashboard on a browser. Look for Set up NordVPN manually to find your Service Credentials (these are different from your email/password). Download the Config: Visit the NordVPN Utility page and download the .ovpn file for the country/server you want to use. Enter Desktop Mode: Press the Steam Button > Power > Switch to Desktop. Import to Network Manager: Click the Wi-Fi/Network icon in the bottom right taskbar. Click the Settings (Configure Network Connections) icon. Click the + (plus) button to add a new connection. Scroll to the bottom and select Import VPN connection.... Select the .ovpn file you downloaded. Configure: In the "VPN" tab, enter the Service Username and Password you got in Step 1. Set the password storage to "Store password for all users (not encrypted)" so it connects easily. Connect: Click Apply, then toggle the VPN on from the network list. Method 2: The "Best for Gaming Mode" (Decky Loader) If you want a toggle that works while you are actually playing games (Gaming Mode), use TunnelDeck. Install Decky Loader: If you don't have it, go to decky.xyz in Desktop Mode and run the installer. Install TunnelDeck: Open the Decky menu (the ... button) in Gaming Mode, go to the Store (shopping bag icon), and find/install TunnelDeck. Usage: Once you have followed the "Import" steps in Method 1, those connections will automatically show up in the TunnelDeck menu. You can now toggle your VPN on and off without leaving your game. A Brutal Reality Check I’ll skip the fluff: avoid the "Native Linux App" (CLI) installation guides you see on Reddit unless you want a headache. SteamOS uses an immutable file system. If you use the sudo steamos-readonly disable command to install the official NordVPN app via pacman, it will be wiped every time SteamOS performs a system update. Stick to the Network Manager/TunnelDeck approach. It survives updates, requires no "hacks," and just works. Would you like me to walk you through setting up Decky Loader first if you don't have it yet?
