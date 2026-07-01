---
category: streaming
date: 2026-02-17
id: 301786
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to uninstall OBS Studio using both `pacman` and `flatpak`,
  but encountering errors, indicating a problem with package management.
tags:
- obs-studio
- package-removal
- pacman
- linux-applications
- flatpak
---
# ❯ sudo pacman -Rns obs-studio
[sudo] password for toastedmel0n:  
error: target not found: obs-studio

~
❯ flatpak uninstall com.obsproject.Studio
error: No installed refs found for ‘com.obsproject.Studio’

~
❯  

### USER
❯ sudo pacman -Rns obs-studio
[sudo] password for toastedmel0n:  
error: target not found: obs-studio

~
❯ flatpak uninstall com.obsproject.Studio
error: No installed refs found for ‘com.obsproject.Studio’

~
❯  

### GEMINI
You are looking for a ghost because you haven't identified what you actually installed. CachyOS often uses meta-packages or alternative versions (like the Git version or the browser-integrated version) that don't go by the standard name obs-studio. If pacman says it's not found, you're trying to delete a label that doesn't exist on your system. Stop guessing and find the actual package name. Step 1: Locate the target Run this command to see exactly what OBS-related packages are currently sitting on your drive: pacman -Qs obs Step 2: Kill the correct package Look at the output. You will likely see something like obs-studio-git, obs-studio-tytan652, or cachyos-obs-studio. Once you have the exact name from that list, run: sudo pacman -Rns [EXACT-NAME-FROM-LIST] The Reality Check If pacman -Qs obs returns nothing, then you didn't install it via the official repositories or Flatpak. You likely used an AppImage or a local binary. Check your home directory: ls ~/Applications or ls ~/Downloads Check for an AppImage: If you find a .AppImage file, just delete the file. That’s the "uninstallation." Run pacman -Qs obs and tell me what the output is—I'll tell you exactly which string to delete.
