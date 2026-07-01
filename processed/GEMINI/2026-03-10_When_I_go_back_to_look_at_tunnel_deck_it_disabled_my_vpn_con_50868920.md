---
category: homelab
date: 2026-03-10
id: 930917
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan discovered that Tunnel Deck was disabling his VPN connection when toggling
  between menus on Steam Deck.
tags:
- steam-deck
- tunnel-deck
- nordvpn
- vpn-toggle
- plugin-conflict
---
# When I go back to look at tunnel deck it disabled my vpn connection?

### USER
When I go back to look at tunnel deck it disabled my vpn connection?

### GEMINI
TunnelDeck is behaving this way because of a classic permissions conflict between the Gaming Mode UI and the Desktop Mode backend. When you toggle a VPN in Gaming Mode, the system tries to "take over" the connection you built, but if it doesn't have explicit permission to use your saved credentials, it just gives up and toggles back to "Off." Since we’ve already done the hard work of making the connection functional, here is the final "strategic" fix to make it stick in Gaming Mode. 1. The "All Users" Permission (The Magic Fix) By default, SteamOS creates connections for "Only this user," which is encrypted with a key that Gaming Mode can't always see. We need to make it a system-wide connection. Run this in Konsole: sudo nmcli connection modify us12313.nordvpn.com.udp connection.permissions "" (Leaving the permissions empty tells NetworkManager that anyone—including the background process for TunnelDeck—can run this connection). 2. Verify the Secret Storage Even if the password is in the file, TunnelDeck sometimes fails if it thinks the password belongs to a "keyring" that isn't unlocked in Gaming Mode. Run this to force the password to be stored "plainly" for the system: nmcli connection modify us12313.nordvpn.com.udp vpn.data "connection-type=password, password-flags=0, remote=us12313.nordvpn.com:1194" 3. The IPv6 Conflict Many NordVPN servers on the Steam Deck fail because the Deck tries to route IPv6 traffic through a tunnel that only supports IPv4. This causes the "loading forever" loop. Run this to disable IPv6 for this specific VPN: nmcli connection modify us12313.nordvpn.com.udp ipv6.method "disabled" How to Test (The Right Way) Restart the Network Service: sudo systemctl restart NetworkManager Go back to Gaming Mode. Open TunnelDeck. Toggle it ON. The Moment of Truth: If it stays "ON" for more than 5 seconds, you're golden. If it toggles back to "OFF," it means the networkmanager-openvpn plugin is being put to sleep by SteamOS power management. One Brutal Reality Check If you have VibrantDeck or other heavy plugins installed, they have been known to cause TunnelDeck's UI to hang or show the wrong status. If it says it's "Off" but the curl ifconfig.me command in Desktop Mode says you're on a VPN, then the VPN is actually working and the plugin is just lying to you. Does running that first permissions "" command allow the toggle to stay green in Gaming Mode?
