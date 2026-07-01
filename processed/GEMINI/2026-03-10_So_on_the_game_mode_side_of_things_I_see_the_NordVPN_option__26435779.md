---
id: 288028
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'game-mode', 'vpn-connection', 'connection-verification']
category: homelab
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to verify he's actually connected to NordVPN through the Steam Deck game mode interface.
---
# So on the game mode side of things I see the NordVPN option but it’s just loading forever and not showing anything but now it is? (It took a while) How do I ensure that I’m connected to the actual vpn service

### USER
So on the game mode side of things I see the NordVPN option but it’s just loading forever and not showing anything but now it is? (It took a while) How do I ensure that I’m connected to the actual vpn service

### GEMINI
The "loading forever" was likely TunnelDeck struggling to parse the new configuration while the connection was already active. Since it’s finally showing up, you've cleared the biggest hurdle. To ensure you are actually connected and your traffic is encrypted, use these three verification methods: 1. The "Kill Switch" Check (Desktop Mode) Run this in the terminal. It’s the most definitive proof: nmcli device status What to look for: You should see a device named tun0 (or similar) with the state connected. If tun0 exists, your traffic is being routed through the VPN tunnel. 2. The IP Verification (Quick & Easy) Open the browser in Desktop Mode or run this in Konsole: curl https://am.i.mullvad.net/json (Even though you're using Nord, this tool gives a very clean summary). * Look for: "mullvad_exit_node": false (this is fine), but more importantly, check the city and country. If it shows a NordVPN server location instead of your house, you’re good. 3. The Gaming Mode "Visual Cue" In Gaming Mode, once you toggle the VPN on in TunnelDeck: Look at the top right header (next to the clock and Wi-Fi icon). On recent SteamOS versions, a small padlock icon or a VPN badge usually appears briefly or stays in the quick settings menu to indicate an active tunnel. Pro-Tip for Stability If TunnelDeck feels "laggy" or takes a long time to show the status: Open the TunnelDeck settings (the gear icon in the plugin). Ensure "Check connection status" is set to a reasonable interval (like 5 or 10 seconds). If it hangs, it's usually just the UI waiting for nmcli to respond. Does the curl command show an IP address that matches the Nord server location you chose?
