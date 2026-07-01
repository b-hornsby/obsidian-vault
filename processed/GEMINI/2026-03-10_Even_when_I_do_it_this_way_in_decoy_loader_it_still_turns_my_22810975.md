---
category: homelab
date: 2026-03-10
id: 676399
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was frustrated that NordVPN keeps turning off when exiting and re-entering
  the menu in Decoy Loader on Steam Deck.
tags:
- steam-deck
- nordvpn
- decoy-loader
- vpn-toggle
- game-mode
---
# Even when I do it this way in decoy loader it still turns my vpn right off when I exit the menu and re enter it

### USER
Even when I do it this way in decoy loader it still turns my vpn right off when I exit the menu and re enter it

### GEMINI
That "toggle back to off" loop is a classic symptom of a failed handshake. If the system can't verify the connection within a second or two, it just kills the process and resets the switch. Since you've already tried the standard setup, here is why it’s failing and the "brutally honest" fix you need to apply: 1. The Most Likely Culprit: Missing OpenVPN Binaries By default, SteamOS is missing the specific "glue" (the networkmanager-openvpn package) that allows the system to actually talk to OpenVPN files. Without it, you can import the file all day, but the system doesn't know how to execute it. The Fix: Go to Desktop Mode. Open Konsole (the terminal). Set a password if you haven't (type passwd and follow prompts). Run these commands exactly: sudo steamos-readonly disable (Unlocks the system) sudo pacman -S networkmanager-openvpn (Installs the missing link) sudo steamos-readonly enable (Relocks the system) 2. The Authentication Loop If you used your email and account password in the VPN settings, it will fail every single time. The Fix: You must use your Manual Service Credentials. Go to your Nord Account Dashboard, scroll to "NordVPN" > "Manual Setup," and get the specific username/password found there. Update your connection in Desktop Mode with these credentials. 3. The IPv6 Conflict SteamOS sometimes struggles with IPv6 when a VPN is trying to tunnel. The Fix: While still in Desktop Mode, go to your Wi-Fi settings, find your current connection, and under the IPv6 tab, change the method to Disabled. 4. Protocol Mismatch If you downloaded a "NordLynx" or "WireGuard" config, TunnelDeck/Network Manager will likely choke on it. The Fix: Ensure the file you downloaded ends in .ovpn. If you want the most stable connection for the Deck, use the UDP version of the file, not TCP. The Brutal Truth: If you do these four things and it still toggles off, your .ovpn file is likely for a server that is currently under load or blocked by your local network. Download a fresh config for a completely different country to test. Do you want me to help you generate the specific terminal commands for the package install if you get a "PGP signature" error? (That's the next common hurdle).
