---
id: 950040
source: GEMINI
date: 2026-03-10
tags: ['nordvpn', 'vpn-configuration', 'network-manager', 'connection-profile']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is examining the configuration file for his NordVPN connection, likely to troubleshoot connection issues.
---
# f[connection]
id=us12313.nordvpn.com.udp
uuid=3304be90-7b07-4d8c-9038-fb23eed4f38a
type=vpn

[vpn]
connection-type=password
password-flags=0
service-type=org.freedesktop.NetworkManager.openvpn

### USER
f[connection]
id=us12313.nordvpn.com.udp
uuid=3304be90-7b07-4d8c-9038-fb23eed4f38a
type=vpn

[vpn]
connection-type=password
password-flags=0
service-type=org.freedesktop.NetworkManager.openvpn

### GEMINI
You've got the file open in nano, but you're missing the most critical part: the actual credentials and the secrets block. Without these, the system has no "secret" to use, which is why it keeps throwing that error. Since you're comfortable with CachyOS and terminal-heavy workflows, let's finish this config manually. This is the "brute force" method that skips the broken UI entirely. Step 1: Finish the Config File In that nano window, delete what you have and replace it with this exact structure. (Make sure you use your Nord Service Credentials from their dashboard, not your email): [connection] id=us12313.nordvpn.com.udp uuid=3304be90-7b07-4d8c-9038-fb23eed4f38a type=vpn permissions= [vpn] connection-type=password password-flags=0 service-type=org.freedesktop.NetworkManager.openvpn username=YOUR_SERVICE_USERNAME remote=us12313.nordvpn.com:1194 [vpn-secrets] password=YOUR_SERVICE_PASSWORD [ipv4] method=auto [ipv6] addr-gen-mode=stable-privacy method=auto Step 2: Save and Lock Down Save: Press Ctrl + O, then Enter. Exit: Press Ctrl + X. Permissions (Crucial): NetworkManager will ignore this file if the permissions are too loose. Run: sudo chmod 600 /etc/NetworkManager/system-connections/us12313.nordvpn.com.udp.nmconnection Step 3: Reload and Fire Now, tell the system to look at the changes and try to connect: sudo nmcli connection reload nmcli connection up us12313.nordvpn.com.udp Why this works By adding the [vpn-secrets] block and setting password-flags=0, you are telling the Steam Deck: "Don't look in the encrypted KDE Wallet for a password; it's written right here in this file." Setting the permissions to 600 ensures only the system (root) can see that password, satisfying the security check. Verification Once the terminal says "Connection successfully activated," you can jump back into Gaming Mode. Open TunnelDeck, and you’ll be able to toggle this on and off with a single tap. Did the terminal finally give you the "Success" message after you added the [vpn-secrets] block?
