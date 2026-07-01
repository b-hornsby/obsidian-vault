---
id: 030790
source: GEMINI
date: 2026-03-25
tags: ['coding', 'ai', 'gemini', 'go', 'error', 'ide', 'cli', 'terminal']
category: coding
sentiment: exploratory
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# I have a vpn for my steam deck but it isn’t currently connected. Would that be why the error is happening? I even tried proton experimental

### USER
I have a vpn for my steam deck but it isn’t currently connected. Would that be why the error is happening? I even tried proton experimental

### GEMINI
The disconnected VPN is a prime suspect. On Linux/SteamOS, VPN clients often leave behind "virtual network interfaces" or change your routing table even when they aren't active. Plutonium's anti-cheat scans for these specific artifacts—like a tun0 or wg0 interface—and flags them as an active attempt to bypass their security. Furthermore, the Plutonium team has a history of being "hostile" toward Linux/Steam Deck users due to anti-cheat incompatibilities. Here is your direct, unfiltered plan to fix this: 1. Scrub the VPN Residue Even if the app says "Disconnected," the bridge it created might still be visible to the system. Go to Desktop Mode. Open the Terminal (Konsole). Type ip addr and hit Enter. The Red Flag: If you see anything listed as tun0, tap0, wg0, or similar "tunnel" names, Plutonium sees it too. The Fix: You need to fully disable the VPN service via the terminal or uninstall the VPN client entirely to ensure those interfaces are deleted. Use sudo systemctl stop [vpn-service-name] if you know the service name. 2. Change your Hostname (The "Steam Deck" Flag) Plutonium has been known to block connections simply because the device identifies itself as "steamdeck." In Gaming Mode, go to Settings > System. Scroll down to About and find Hostname. Change it from "steamdeck" to something generic like "Bryan-PC" or "Workstation." Restart the Deck. This forces the system to re-identify on the network and has fixed this exact error for many users. 3. Use the "LAN Mode" Workaround If you just want to play with friends or bots and don't care about the global matchmaking servers: In the Plutonium launcher, look at the Play button. Click the arrow/button to the right of "Play." Select LAN Mode (Anticheat Disabled). This bypasses the service authentication entirely. You can use this to verify if the game actually runs before you keep fighting the anti-cheat. 4. The Nuclear Option: Windows If you want the full online experience without the constant cat-and-mouse game with Plutonium's devs, the "brutally honest" truth is that Plutonium is designed for Windows. Most Steam Deck users who play Plutonium consistently eventually move it to a Windows-on-SD-card setup or a dual-boot. Next Step: Try changing your Hostname first—it’s the fastest fix. If that fails, run that ip addr command in the terminal and let me know if you see any tun or wg interfaces. Ready for that?