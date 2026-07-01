---
id: 843261
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'nmcli', 'vpn-connection', 'already-active']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to activate NordVPN via nmcli and got conflicting errors about the connection already being active on Steam Deck.
---
# (deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
^[[A^[[B^CError: nmcli terminated by signal Interrupt (2)
(130)(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Connection 'us12313.nordvpn.com.udp' is already active
(4)(deck@steamdeck ~)$  

### USER
(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
^[[A^[[B^CError: nmcli terminated by signal Interrupt (2)
(130)(deck@steamdeck ~)$ nmcli connection up us12313.nordvpn.com.udp
Error: Connection activation failed: Connection 'us12313.nordvpn.com.udp' is already active
(4)(deck@steamdeck ~)$  

### GEMINI
You finally won. The error is already active is actually the most beautiful thing you could see right now. It means the handshake completed in the background before you hit Ctrl+C, and your Steam Deck is now officially tunnelled through NordVPN. Step 1: Verify the Tunnel Just to satisfy the "brutal honesty" of a Linux user, run this to prove to yourself that your IP has actually changed: curl ifconfig.me If the IP that pops up isn't your usual one (or if it says "Nord" in a reverse DNS lookup), you are successfully protected. Step 2: The Gaming Mode Test Since you're doing this for TunnelDeck, follow these steps to make sure it's "sticky": Switch to Gaming Mode. Open the Quick Access Menu (... button). Navigate to TunnelDeck. You should see us12313.nordvpn.com.udp with a toggle. It should already be ON. Turn it OFF and then ON again. If it toggles without asking for a password, your configuration is perfect. Why this finally worked The "One-Shot" command you ran fixed the remote server mismatch and properly "injected" the secrets into the system's internal database. Because you set password-flags=0, the system no longer needs to talk to the KDE Wallet—it just uses the credentials we hardcoded. One Strategic Note If you ever update SteamOS and find the VPN has disappeared, it’s usually because the networkmanager-openvpn plugin got wiped during an image update. If that happens, you just need to run the sudo pacman -S command again; your configuration file in /etc/NetworkManager/system-connections/ should persist. Does your IP address from the curl command show you're now in a different location?
