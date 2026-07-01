---
category: homelab
date: 2026-03-10
id: 193456
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is unable to find the option to add a VPN connection on his Steam Deck.
tags:
- steam-deck
- nordvpn
- vpn-setup
- network-manager
---
# i dont see even the option to add a vpn connection

### USER
i dont see even the option to add a vpn connection

### GEMINI
This is a common issue with the Steam Deck’s custom OS. The "Add VPN" option is missing because Valve didn't include the necessary OpenVPN plugin by default. Since the system is "read-only," you can't just install it like a normal app. You have two ways to fix this: the Manual Terminal Fix (reliable but technical) or the TunnelDeck Fix (easier if you use Decky Loader). Option 1: The TunnelDeck Fix (Recommended) If you already have Decky Loader installed, this is the most painless way. In Gaming Mode, go to the Decky Store (plug icon). Install the TunnelDeck plugin. Once installed, open TunnelDeck in the Decky menu. Look for a setting that says "Enable OpenVPN" or "Install OpenVPN". Toggle it. Restart your Steam Deck. The "VPN" option should now appear in Desktop Mode under Network Settings. Option 2: The Manual Terminal Fix If you aren't using Decky Loader, you’ll need to manually inject the plugin into the system. Go to Desktop Mode and open Konsole. Type the following commands one by one (it will ask for your sudo password): # Unlock the filesystem sudo steamos-readonly disable # Initialize the package manager keys sudo pacman-key --init sudo pacman-key --populate archlinux # Install the missing VPN plugin sudo pacman -S networkmanager-openvpn # Re-lock the filesystem for safety sudo steamos-readonly enable Restart the Steam Deck. Why is this happening? The Steam Deck uses SteamOS, which is an immutable (read-only) version of Arch Linux. Valve keeps it locked down so system updates don't break your console. Because of this, even after you fix it, a major SteamOS update will likely delete this plugin again. If you notice the VPN option disappears after an update, you will need to run the commands in Option 2 again (or just toggle it back on in TunnelDeck). Did you run into any "key" or "signature" errors while trying the terminal commands?
