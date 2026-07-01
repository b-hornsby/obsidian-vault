---
category: general
date: 2026-03-09
id: 125925
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to install the Nexus Mods application on the CachyOS
  operating system.
tags:
- nexus-mods
- modding
- cachyos
- game-modding
- linux-gaming
---
# how do i install the nexus mods app in cachyos?

### USER
how do i install the nexus mods app in cachyos?

### GEMINI
As of March 2026, the situation with the Nexus Mods App (the native Linux/cross-platform one) has shifted significantly. Nexus Mods officially retired the standalone App in early January 2026 to consolidate their efforts back into Vortex, which is finally getting native Linux/SteamOS support. However, since you're on CachyOS, you can still install the existing version of the Nexus Mods App from the AUR. 1. The Fast Way (AUR) Since you're using CachyOS, you likely have an AUR helper like paru or yay ready to go. The binary version is the most stable bet. paru -S nexusmods-app-bin (Or use yay -S nexusmods-app-bin if that's your preference.) 2. Critical Configuration (Don't Skip) The app relies on XDG Desktop Portals to handle the "Log In" link from your browser. If clicking "Log In" does nothing, you need to ensure you have the portal for your desktop environment installed. For KDE Plasma: sudo pacman -S xdg-desktop-portal-kde For GNOME: sudo pacman -S xdg-desktop-portal-gnome For Hyprland/Sway: sudo pacman -S xdg-desktop-portal-hyprland (or -wlr) Pro Tip: There is a known bug in some AUR PKGBUILDs where the .desktop file has a broken TryExec line. If the app won't launch from your menu, edit /usr/share/applications/nexusmods-app.desktop and remove the TryExec line entirely. 3. The "Advisor" Reality Check You’re building a DeFi bot and troubleshooting obs-cmd connection refused errors, yet you're trying to use a deprecated mod manager. The Nexus Mods App was essentially an alpha project that they’ve now abandoned. It only has "full" support for a handful of games (like Cyberpunk 2077 and Stardew Valley). If you're trying to mod Bethesda games (Skyrim/Fallout) or anything complex, you are wasting your time with the native App. The Move: If the App doesn't support your specific game, don't fight with it. Use Mod Organizer 2 via the steam-tinker-launch script or the flatpak version. It’s mature, handles the virtual file system correctly on Linux, and doesn't suffer from the "identity crisis" Nexus is currently having with their software roadmap. 4. Troubleshooting the obs-cmd Error I noticed your terminal output earlier. Connection refused usually means the OBS WebSocket server isn't running or is on a different port/password than what obs-cmd expects. Go to OBS -> Tools -> WebSocket Server Settings. Ensure "Enable WebSocket Server" is checked. Check the port (default is 4455). Would you like me to help you debug that obs-cmd connection or verify if the Nexus App supports the specific game you're trying to mod?
