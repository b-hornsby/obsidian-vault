---
category: homelab
date: 2026-03-10
id: 812925
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan got a VPN secrets format error when trying to modify NordVPN credentials
  via nmcli on Steam Deck.
tags:
- steam-deck
- nordvpn
- nmcli
- vpn-secrets
- configuration-error
---
# when i ran the second one i got an error: Error: failed to modify vpn.secrets: (my secret) is not valid; use <option>=<value>.

### USER
when i ran the second one i got an error: Error: failed to modify vpn.secrets: (my secret) is not valid; use <option>=<value>.

### GEMINI
The error happened because the terminal interpreted your password as a command instead of a value. Since you're used to the precision of CachyOS and local LLM configurations, you know that special characters in a password (like $ or !) can break a command if they aren't properly "wrapped." The syntax vpn.secrets "password=YOUR_PASSWORD" is very specific. You need the word password= inside the quotes with your actual secret. The Correct Syntax Run this exact command, making sure your password is inside the quotes and starts with password=: nmcli connection modify us12313.nordvpn.com.udp vpn.secrets "password=PASTE_YOUR_ACTUAL_SECRET_HERE" Why it failed If your Nord service password contains a special character and you didn't use the password= prefix inside the quotes, nmcli doesn't know what to do with the string. It's looking for a "Key=Value" pair. If that still gives an error: We'll use the interactive mode, which is much safer for passwords with weird characters: Type: nmcli connection edit us12313.nordvpn.com.udp You will see a nmcli> prompt. Type: goto vpn Type: set secrets password=YOUR_ACTUAL_SERVICE_PASSWORD Type: save Type: quit The Final Test Once you've saved it using either method above, fire it up: nmcli connection up us12313.nordvpn.com.udp Once you see "Connection successfully activated," you can finally close the terminal and jump back into Gaming Mode. Does it connect now?
