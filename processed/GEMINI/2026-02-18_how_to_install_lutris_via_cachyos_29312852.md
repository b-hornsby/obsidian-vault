---
category: homelab
date: 2026-02-18
id: 113993
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for instructions on how to install Lutris on CachyOS, indicating
  he wants to use it for gaming.
tags:
- lutris
- game-launcher
- cachyos
- package-installation
- linux-gaming
---
# how to install lutris via cachyos

### USER
how to install lutris via cachyos

### GEMINI
Installing Lutris on CachyOS is straightforward, but because CachyOS is a performance-tuned gaming distro, you have two primary ways to do it: the "Cachy way" (recommended for dependencies) and the "Arch way." 1. The Recommended Way (CachyOS Hello) CachyOS provides a Gaming Meta Package that includes Lutris along with all the necessary dependencies (Wine, drivers, etc.) to ensure games actually launch. Open the CachyOS Hello app from your application menu. Navigate to Apps/Tweaks. Click on Install Gaming Packages. This will pull in Lutris, Steam, and essential libraries optimized for your CPU architecture (e.g., x86-64-v3/v4). 2. The Terminal Way (Pacman) If you just want the package itself without the full meta-package suite, run: sudo pacman -S lutris Note: If you use this method, I strongly recommend also installing the cachyos-gaming-applications package to avoid "missing library" errors common in Wine gaming: sudo pacman -S cachyos-gaming-applications 3. Essential Post-Install Steps (CachyOS Optimization) To get the most out of CachyOS's specific optimizations within Lutris: Install umu-launcher: CachyOS uses this to bridge Lutris with Proton more effectively. sudo pacman -S umu-launcher Set the Runner: In Lutris, go to Preferences -> Global Options. Enable Game Performance: Set your command prefix or environment variable to game-performance to trigger the CachyOS power profile when a game starts. Use proton-cachyos: In the Lutris "Runner Options" for your games, select proton-cachyos as the Wine version for the best performance. Strategy & Mirroring Since you're asking for the "how-to," here is the unfiltered truth: Don't just install the bare lutris package. The biggest "blind spot" for new CachyOS users is thinking it's just like standard Arch. If you manually install Lutris via pacman and skip the cachyos-gaming-applications meta-package, you are wasting the reason you chose this distro. You’ll end up hunting down lib32 dependencies and vulkan loaders manually. Use the CachyOS Hello tool—it's there so you can spend time playing, not troubleshooting. Would you like me to show you how to configure proton-cachyos specifically for a game like Battle.net or Epic Games inside Lutris?
