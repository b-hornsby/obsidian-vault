---
category: homelab
date: 2026-03-10
id: 361111
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was checking NetworkManager logs on Steam Deck to debug a NordVPN OpenVPN
  connection failure.
tags:
- steam-deck
- networkmanager
- nordvpn
- openvpn
- vpn-debugging
---
# (4)(deck@steamdeck ~)$ journalctl -u NetworkManager -n 30 --no-pager
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1842] device (wlan0): state change: ip-check -> secondaries (reason 'none', manage
d-type: 'full')
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1844] device (wlan0): state change: secondaries -> activated (reason 'none', manag
ed-type: 'full')
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1849] manager: NetworkManager state is now CONNECTED_SITE
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1852] device (wlan0): Activation: successful, device activated.
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.5372] manager: NetworkManager state is now CONNECTED_GLOBAL
Mar 10 11:06:44 steamdeck NetworkManager[9190]: <info>  [1773155204.6874] manager: startup complete
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0378] agent-manager: agent[61e30607d0267526,:1.202/nmcli-connect/1000]: agent regi
stered
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0442] vpn[0x563e84de9320,3304be90-7b07-4d8c-9038-fb23eed4f38a,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <error> [1773155215.0472] audit: failed to open auditd socket: Protocol not supported
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0472] audit: op="connection-activate" uuid="3304be90-7b07-4d8c-9038-fb23eed4f38a" 
name="us12313.nordvpn.com.udp" pid=9254 uid=1000 result="success"
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <warn>  [1773155215.0629] vpn[0x563e84de9320,3304be90-7b07-4d8c-9038-fb23eed4f38a,"us12313.nordvpn.com
.udp"]: connect: failed to connect interactively: 'GDBus.Error:org.freedesktop.NetworkManager.VPN.Error.BadArguments: property “psdl” invalid or not s
upported'
Mar 10 11:07:46 steamdeck NetworkManager[9190]: <info>  [1773155266.3682] audit: op="connection-delete" uuid="3304be90-7b07-4d8c-9038-fb23eed4f38a" na
me="us12313.nordvpn.com.udp" pid=9300 uid=1000 result="success"
Mar 10 11:08:03 steamdeck NetworkManager[9190]: <info>  [1773155283.7779] audit: op="connection-add" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" name=
"us12313.nordvpn.com.udp" pid=9326 uid=0 result="success"
Mar 10 11:09:08 steamdeck NetworkManager[9190]: <info>  [1773155348.1823] audit: op="connection-update" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" na
me="us12313.nordvpn.com.udp" args="vpn.user-name,vpn.data,vpn.secrets" pid=9359 uid=1000 result="success"
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9782] agent-manager: agent[4d7260e303f3c743,:1.208/nmcli-connect/1000]: agent regi
stered
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9848] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9853] audit: op="connection-activate" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" 
name="us12313.nordvpn.com.udp" pid=9370 uid=1000 result="success"
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Note: --cipher is not set. OpenVPN versions before 2.5 defaulted to BF-CBC as fallback when cipher negotia
tion failed in this case. If you need this fallback please add '--data-ciphers-fallback BF-CBC' to your configuration and/or add BF-CBC to --data-ciph
ers.
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Options error: --nobind doesn't make sense unless used with --remote
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Use --help for more information.
Mar 10 11:09:17 steamdeck NetworkManager[9190]: <warn>  [1773155357.0262] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:09:17 steamdeck NetworkManager[9190]: <warn>  [1773155357.0263] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:10:21 steamdeck NetworkManager[9190]: <info>  [1773155421.5810] audit: op="connection-update" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" na
me="us12313.nordvpn.com.udp" args="vpn.data" pid=9410 uid=1000 result="success"
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9547] agent-manager: agent[4d7260e303f3c743,:1.211/nmcli-connect/1000]: agent regi
stered
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9607] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9611] audit: op="connection-activate" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" 
name="us12313.nordvpn.com.udp" pid=9419 uid=1000 result="success"
Mar 10 11:10:25 steamdeck nm-openvpn[9433]: Options error: --nobind doesn't make sense unless used with --remote
Mar 10 11:10:25 steamdeck nm-openvpn[9433]: Use --help for more information.
Mar 10 11:10:26 steamdeck NetworkManager[9190]: <warn>  [1773155426.0016] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:10:26 steamdeck NetworkManager[9190]: <warn>  [1773155426.0017] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
(deck@steamdeck ~)$  

### USER
(4)(deck@steamdeck ~)$ journalctl -u NetworkManager -n 30 --no-pager
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1842] device (wlan0): state change: ip-check -> secondaries (reason 'none', manage
d-type: 'full')
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1844] device (wlan0): state change: secondaries -> activated (reason 'none', manag
ed-type: 'full')
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1849] manager: NetworkManager state is now CONNECTED_SITE
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.1852] device (wlan0): Activation: successful, device activated.
Mar 10 11:06:40 steamdeck NetworkManager[9190]: <info>  [1773155200.5372] manager: NetworkManager state is now CONNECTED_GLOBAL
Mar 10 11:06:44 steamdeck NetworkManager[9190]: <info>  [1773155204.6874] manager: startup complete
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0378] agent-manager: agent[61e30607d0267526,:1.202/nmcli-connect/1000]: agent regi
stered
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0442] vpn[0x563e84de9320,3304be90-7b07-4d8c-9038-fb23eed4f38a,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <error> [1773155215.0472] audit: failed to open auditd socket: Protocol not supported
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <info>  [1773155215.0472] audit: op="connection-activate" uuid="3304be90-7b07-4d8c-9038-fb23eed4f38a" 
name="us12313.nordvpn.com.udp" pid=9254 uid=1000 result="success"
Mar 10 11:06:55 steamdeck NetworkManager[9190]: <warn>  [1773155215.0629] vpn[0x563e84de9320,3304be90-7b07-4d8c-9038-fb23eed4f38a,"us12313.nordvpn.com
.udp"]: connect: failed to connect interactively: 'GDBus.Error:org.freedesktop.NetworkManager.VPN.Error.BadArguments: property “psdl” invalid or not s
upported'
Mar 10 11:07:46 steamdeck NetworkManager[9190]: <info>  [1773155266.3682] audit: op="connection-delete" uuid="3304be90-7b07-4d8c-9038-fb23eed4f38a" na
me="us12313.nordvpn.com.udp" pid=9300 uid=1000 result="success"
Mar 10 11:08:03 steamdeck NetworkManager[9190]: <info>  [1773155283.7779] audit: op="connection-add" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" name=
"us12313.nordvpn.com.udp" pid=9326 uid=0 result="success"
Mar 10 11:09:08 steamdeck NetworkManager[9190]: <info>  [1773155348.1823] audit: op="connection-update" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" na
me="us12313.nordvpn.com.udp" args="vpn.user-name,vpn.data,vpn.secrets" pid=9359 uid=1000 result="success"
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9782] agent-manager: agent[4d7260e303f3c743,:1.208/nmcli-connect/1000]: agent regi
stered
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9848] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:09:16 steamdeck NetworkManager[9190]: <info>  [1773155356.9853] audit: op="connection-activate" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" 
name="us12313.nordvpn.com.udp" pid=9370 uid=1000 result="success"
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Note: --cipher is not set. OpenVPN versions before 2.5 defaulted to BF-CBC as fallback when cipher negotia
tion failed in this case. If you need this fallback please add '--data-ciphers-fallback BF-CBC' to your configuration and/or add BF-CBC to --data-ciph
ers.
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Options error: --nobind doesn't make sense unless used with --remote
Mar 10 11:09:17 steamdeck nm-openvpn[9385]: Use --help for more information.
Mar 10 11:09:17 steamdeck NetworkManager[9190]: <warn>  [1773155357.0262] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:09:17 steamdeck NetworkManager[9190]: <warn>  [1773155357.0263] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:10:21 steamdeck NetworkManager[9190]: <info>  [1773155421.5810] audit: op="connection-update" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" na
me="us12313.nordvpn.com.udp" args="vpn.data" pid=9410 uid=1000 result="success"
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9547] agent-manager: agent[4d7260e303f3c743,:1.211/nmcli-connect/1000]: agent regi
stered
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9607] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: starting openvpn
Mar 10 11:10:25 steamdeck NetworkManager[9190]: <info>  [1773155425.9611] audit: op="connection-activate" uuid="fbdb7f00-8e87-4f84-9cf1-163b99a2164f" 
name="us12313.nordvpn.com.udp" pid=9419 uid=1000 result="success"
Mar 10 11:10:25 steamdeck nm-openvpn[9433]: Options error: --nobind doesn't make sense unless used with --remote
Mar 10 11:10:25 steamdeck nm-openvpn[9433]: Use --help for more information.
Mar 10 11:10:26 steamdeck NetworkManager[9190]: <warn>  [1773155426.0016] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
Mar 10 11:10:26 steamdeck NetworkManager[9190]: <warn>  [1773155426.0017] vpn[0x563e84de9320,fbdb7f00-8e87-4f84-9cf1-163b99a2164f,"us12313.nordvpn.com
.udp"]: dbus: failure: connect-failed (1)
(deck@steamdeck ~)$  

### GEMINI
The log finally gave us the answer: Options error: --nobind doesn't make sense unless used with --remote. This is a specific bug with the OpenVPN 2.6+ update on Arch-based systems like the Steam Deck. When you imported the NordVPN file, it stripped out the server address (remote), but kept the --nobind flag. OpenVPN then crashes because it has a "rule" with no "destination." Since you've been working with CachyOS, you'll appreciate the precision here—we need to manually re-add the server address to the connection. The Fix Run these commands to tell the VPN exactly where to connect: # 1. Add the missing remote server and port nmcli connection modify us12313.nordvpn.com.udp +vpn.data "remote=us12313.nordvpn.com:1194" # 2. Re-verify the CA certificate path (just in case the import lost it) nmcli connection modify us12313.nordvpn.com.udp vpn.data "ca=/home/deck/Downloads/us12313.nordvpn.com.udp.ovpn" # 3. Fire it up nmcli connection up us12313.nordvpn.com.udp Why this happened When you ran the "Clean Slate" import, the SteamOS network manager tried to be "smart" and parsed the .ovpn file into its own format, but it forgot to copy the remote line from the text file into the system database. OpenVPN saw a configuration that said "don't bind to a local port" (--nobind) but didn't see a server to talk to, so it aborted immediately. One Final "Advisor" Tip If the command above gives you a "Certificate" error, it's because it's looking for the certificate inside the .ovpn file in your Downloads. Do not delete that file! If you move or delete it, the VPN will break. Did adding the remote line finally get the terminal to say "Connection successfully activated"?
