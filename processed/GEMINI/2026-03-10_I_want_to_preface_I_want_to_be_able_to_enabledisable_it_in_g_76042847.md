---
id: 227394
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'game-mode', 'vpn-toggle', 'steam-deck-ui']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified that he wants to be able to enable/disable NordVPN in Steam Deck's game mode primarily.
---
# I want to preface I want to be able to enable/disable it in game mode primarily

### USER
I want to preface I want to be able to enable/disable it in game mode primarily

### GEMINI
Since you want a reliable Gaming Mode toggle, we need to stop using the OpenVPN method. OpenVPN on the Steam Deck is notoriously buggy with passwords in Gaming Mode—that’s why it keeps disabling itself. The easiest and most modern way as of 2026 is to use WireGuard (NordLynx). It doesn't use a username or password; it uses a "Secret Key" that is baked into the file, meaning it will stay connected without the Decky plugin crashing or asking for credentials. Step 1: Get your NordLynx Private Key Nord doesn't give you these files directly, so we have to "leak" it from their official Linux tool. In Desktop Mode, open Konsole and run: sh <(wget -qO - https://downloads.nordcdn.com/apps/linux/install.sh) sudo usermod -aG nordvpn $USER Restart your Deck. Open Konsole again and type: nordvpn login nordvpn set technology nordlynx nordvpn connect The Secret Step: Once connected, run this to see your private key: sudo wg show nordlynx private-key Copy that long string of characters. Step 2: Create the WireGuard Config Create a new text file on your desktop named NordVPN.conf. Paste this inside, replacing the placeholders with your info (you can find the Endpoint IP for any Nord server here): [Interface] PrivateKey = PASTE_YOUR_PRIVATE_KEY_HERE Address = 10.5.0.2/32 DNS = 103.86.96.100, 103.86.99.100 [Peer] PublicKey = PASTE_SERVER_PUBLIC_KEY_HERE Endpoint = SERVER_IP_ADDRESS:51820 AllowedIPs = 0.0.0.0/0 (Tip: Most people find it easier to just use a "NordVPN WireGuard Config Generator" website to grab a pre-made file using their Private Key). Step 3: Import into the Deck Go to System Settings > Connections. Click the + button -> Import VPN connection. Select your NordVPN.conf file. Crucial: Right-click the new connection, go to General Configuration, and check "All users may connect to this network." Step 4: The Gaming Mode Win Back in Gaming Mode, open TunnelDeck. You will see "NordVPN" listed as a WireGuard connection. Toggle it ON. Why this is the "2026" solution: No Passwords: WireGuard uses keys. TunnelDeck will never ask you for a "Secret" again. Speed: It is roughly 2x faster than the OpenVPN method you were using. Stability: It connects in less than 1 second, so the "loading forever" bug disappears. Would you like me to help you find the specific Server IP and Public Key for a specific location (like USA or UK) to finish the file?
