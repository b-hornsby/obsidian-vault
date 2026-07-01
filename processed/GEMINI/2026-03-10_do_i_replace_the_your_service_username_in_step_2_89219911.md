---
category: homelab
date: 2026-03-10
id: 916802
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is seeking clarification on a step in the NordVPN setup process, specifically
  whether to replace a placeholder username.
tags:
- nordvpn
- vpn-configuration
- steam-deck
---
# do i replace the your service username in step 2?

### USER
do i replace the your service username in step 2?

### GEMINI
Yes, absolutely. You must replace those placeholders. Your standard email and password used for the NordVPN website will not work here. Since June 2023, NordVPN requires "Service Credentials" for all manual OpenVPN setups. Where to get them: Log in to your Nord Account Dashboard. On the left, click NordVPN. Scroll down to the Manual setup section and click Set up NordVPN manually. You'll get a verification code in your email. Enter it. You will see a Username and Password (long strings of random characters). These are what you paste into Step 2. The Precise Commands Once you have those strings from the website, run these in Konsole (Desktop Mode): # 1. Set the Service Username nmcli connection modify us12313.nordvpn.com.udp vpn.user-name "PASTE_THE_LONG_USER_STRING_HERE" # 2. Set the Service Password nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=PASTE_THE_LONG_PASS_STRING_HERE" # 3. Final Attempt to connect nmcli connection up us12313.nordvpn.com.udp Why this matters The "No valid secrets" error you kept getting was likely because the system was trying to use your regular email address as the username, which the NordVPN server rejects immediately. By using these generated strings, the handshake should finally complete. Once you get "Connection successfully activated" in the terminal, you can go back to Gaming Mode and use the TunnelDeck toggle. Do you have those strings ready to paste?
