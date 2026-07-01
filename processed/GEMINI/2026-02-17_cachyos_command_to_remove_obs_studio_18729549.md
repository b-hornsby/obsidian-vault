---
category: homelab
date: 2026-02-17
id: 947905
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wanted to know the correct CachyOS/pacman command to uninstall OBS
  Studio.
tags:
- obs-studio
- cachyos
- package-removal
- pacman
---
# cachyos command to remove obs studio

### USER
cachyos command to remove obs studio

### GEMINI
To remove OBS Studio on CachyOS, use the standard Arch-based package manager commands in your terminal. Depending on how much "junk" you want to leave behind, choose one of the following: 1. The Recommended (Clean) Method This removes the package and any of its dependencies that aren't being used by other programs. This is the best way to prevent your system from accumulating "orphan" files. sudo pacman -Rns obs-studio 2. The Basic Method This removes only the OBS Studio package. It will leave all its dependencies installed. sudo pacman -R obs-studio 3. If you installed via Flatpak If you installed OBS through the App Store or via Flatpak, use this instead: flatpak uninstall com.obsproject.Studio Important: Cleaning up User Data The commands above remove the software, but they do not touch your personal settings, scenes, or profiles. If you want to wipe everything and start completely fresh, you need to manually delete the configuration folder: For Pacman installations: rm -rf ~/.config/obs-studio For Flatpak installations: rm -rf ~/.var/app/com.obsproject.Studio [!WARNING] Only run the rm -rf commands if you are 100% sure you don't need your scenes or recording settings anymore. They are gone forever once you do. Would you like me to show you how to check if any other "orphan" packages are still cluttering your system after this removal?
