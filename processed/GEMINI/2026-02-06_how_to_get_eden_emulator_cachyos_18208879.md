---
category: general
date: 2026-02-06
id: 903198
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to obtain and install the Eden emulator on CachyOS.
tags:
- eden-emulator
- cachyos
- software-installation
---
# how to get eden emulator cachyos

### USER
how to get eden emulator cachyos

### GEMINI
Getting the Eden Emulator (a high-performance Yuzu fork) on CachyOS is straightforward because CachyOS is Arch-based, though Eden isn't in the official main repos yet. You have two primary ways to get it: the "clean" way (AppImage) or the "Arch" way (AUR). 1. The Recommended Way: AppImage Most Eden users on CachyOS use the AppImage because it’s pre-compiled and includes all the specific optimizations the devs intended. Download: Go to the Eden Emulator Releases GitHub. Get the File: Download the latest .AppImage file. Make it Executable: Open your terminal in the download folder and run: chmod +x Eden-*.AppImage Run it: Double-click the file or run ./Eden-*.AppImage. Pro-Tip: If you want it to show up in your application menu, use Gear Lever (available in CachyOS package manager) to manage your AppImages. 2. The Arch Way: AUR (Arch User Repository) If you prefer a native install that updates with your system, check the AUR. Open your terminal and use paru (CachyOS’s default AUR helper): paru -S eden-emulator-bin (Note: If the specific bin package isn't there, search for eden-emu or eden-emulator-git.) Crucial CachyOS Optimizations Since you are on CachyOS, you should leverage the system's performance tools to make Eden run even better: GameMode: Ensure gamemode is installed. Run Eden by prefixing the command: gamemoderun ./Eden-*.AppImage. Ananicy-Rules: CachyOS uses ananicy-cpp for auto-prioritizing tasks. Eden was recently added to the ananicy-rules (as of late 2025), so ensure your system is updated: sudo pacman -Syu Keys and Firmware: Like any Switch emulator, Eden requires prod.keys and official firmware. Place these in ~/.local/share/eden/ (or wherever your config folder is mapped). Strategic Advice If you're doing this to squeeze out extra frames on a mid-range rig, don't just "install and play." Vulkan is mandatory: Don't even bother with OpenGL. Shader Cache: CachyOS’s kernel (specifically the linux-cachyos kernel) handles heavy I/O better than standard kernels. Ensure you are actually booted into it by running uname -r. If you aren't, you're wasting the main benefit of your OS. Would you like me to walk you through setting up the specific "Early Access" features or configuring the controller mapping for CachyOS?
