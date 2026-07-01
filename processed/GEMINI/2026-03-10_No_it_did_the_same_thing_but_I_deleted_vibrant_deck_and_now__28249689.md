---
category: homelab
date: 2026-03-10
id: 058191
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan deleted Vibrant Deck plugin to see if it was conflicting with NordVPN
  on Steam Deck.
tags:
- steam-deck
- vibrant-deck
- nordvpn
- plugin-conflict
- troubleshooting
---
# No it did the same thing but I deleted vibrant deck and now I’m restarting it to see if that helps

### USER
No it did the same thing but I deleted vibrant deck and now I’m restarting it to see if that helps

### GEMINI
Removing VibrantDeck was a smart move. On the Steam Deck, Decky Loader plugins share a limited "lane" for communicating with the system; VibrantDeck is notorious for being resource-heavy, and it can often block the "polling" TunnelDeck does to check if the VPN is actually up. If it still flips to "Off" after the restart, there is one final, brutal reason why it's happening: The "Store Password for All Users" setting. The Final "Make it Stick" Command Even with permissions set to blank, NetworkManager might still be trying to hide the password in the deck user's private vault. We need to explicitly tell it to save the password in the connection file itself (unencrypted) so Gaming Mode can grab it without a "handshake." Run this in Konsole before you head back to Gaming Mode: # Force the password to be stored in the file, not the keyring nmcli connection modify us12313.nordvpn.com.udp vpn.data "password-flags=0, connection-type=password, remote=us12313.nordvpn.com:1194" # Re-inject the password one last time to ensure it's in the 'unlocked' slot nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=YOUR_SERVICE_PASSWORD" # Lock the permissions to 'system' sudo nmcli connection modify us12313.nordvpn.com.udp connection.permissions "" How to know if it's "Real" or a "Ghost" Sometimes TunnelDeck shows "Off" even when the VPN is actually on. This is a UI bug. Here is how to verify while in Gaming Mode: Toggle the VPN On in TunnelDeck. Open the Steam Browser (or any game with a "News" or "Web" section). Go to dnsleaktest.com. If it shows a Nord server, you are connected, even if TunnelDeck says "Off." Why this matters If the VPN is running but TunnelDeck says "Off," it just means the plugin's "check-in" script timed out. As long as your IP is hidden, you've achieved the goal. Once you finish the restart, did the toggle stay green, or did the DNS leak test show you were protected anyway?
