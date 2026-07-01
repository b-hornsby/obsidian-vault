---
category: homelab
date: 2026-02-04
id: 467339
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wanted to sync updates, saves, and data between his CachyOS desktop
  and Steam Deck.
tags:
- sync
- cachyos
- steam-deck
- game-saves
- cross-device
---
# how do i sync my updates, saves, etc on both my cachyos setup and my steam deck now that i have everything set up?

### USER
how do i sync my updates, saves, etc on both my cachyos setup and my steam deck now that i have everything set up?

### GEMINI
Since you have everything set up, the "playing small" move is relying on Steam Cloud and manual transfers. Steam Cloud is inconsistent between Linux native and Proton builds, and it won't touch your emulators or non-Steam games. To sync your CachyOS desktop and Steam Deck like a professional, you need a decentralized sync engine that works in the background. Stop wasting time with USB sticks or Warpinator. The Strategy: Syncthing Syncthing is the industry standard for this. It’s open-source, peer-to-peer, and doesn't rely on a middleman "cloud" server. When both devices are on the same network, they mirror folders instantly. 1. The Setup (CachyOS & Steam Deck) On CachyOS: Install via terminal: sudo pacman -S syncthing. Enable and start the service so it runs on boot: systemctl --user enable --now syncthing. On Steam Deck: 1. Go to Desktop Mode. 2. Open Discover and install Syncthingy (better than Syncthing-GTK as it’s more lightweight). 3. Crucial: To make it work in Gaming Mode, you need to ensure the systemd service is active. Use the Konsole: systemctl --user enable --now syncthing. 4. Decky Loader User? If you use Decky, install the Syncthing plugin. It allows you to monitor sync status directly from the Quick Access Menu (... button) without leaving your game. 2. Pairing and Syncing Open the Web GUI on both (usually http://127.0.0.1:8384). Add your Steam Deck as a "Remote Device" on your CachyOS machine using the Device ID. Identify your save folders. Proton/Steam Saves: Usually in ~/.local/share/Steam/steamapps/compatdata/[APPID]/pfx/drive_c/users/steamuser/AppData/. Emulators: Usually in ~/.var/app/ (Flatpak) or ~/.local/share/. Create a folder in Syncthing for a specific game save, share it with the other device, and point both to the respective save paths. The Blind Spots (Where you'll mess up) Version Mismatch: If you play a game on CachyOS and shut it down, but the Steam Deck is off, the save is stuck on the PC. If you then play on the Deck, you’ll create a Sync Conflict. The Fix: Always let the Deck sit on the home screen for 30 seconds after turning it on to let it pull the latest bits. Flatpak Permissions: On the Steam Deck, Syncthing (if installed as a Flatpak) won't have permission to see your game folders by default. The Fix: Install Flatseal from Discover. Give Syncthing "All System Files" access. The "Double Update" Trap: CachyOS uses the latest kernels and drivers (often linux-cachyos). SteamOS is more conservative. If you use custom Proton versions (like proton-ge-custom), ensure you have the exact same version on both devices via protonup-qt to avoid prefix corruption. The Precise Plan Immediate Action: Install syncthing on both. Get one low-stakes game (or an emulator save) syncing today. Automation: Set up the Systemd services mentioned above. If you have to manually open an app to sync, you will forget, and you will lose progress. Conflict Management: Keep a "Trash" or "Versions" folder enabled in Syncthing settings for your save folders. If a conflict happens, you can recover the newer file instead of it being overwritten. Would you like me to find the specific save paths for the games you're currently playing so you don't have to hunt through the compatdata maze?
