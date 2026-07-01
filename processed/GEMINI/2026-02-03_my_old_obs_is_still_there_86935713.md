---
category: streaming
date: 2026-02-03
id: 464193
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that an old installation of OBS Studio is still present
  on his system after attempting to remove it.
tags:
- obs-studio
- uninstall
- software-removal
---
# my old obs is still there?

### USER
my old obs is still there?

### GEMINI
This is exactly where "playing small" with your system management gets you: a cluttered, conflicting mess. You didn’t uninstall the old version properly before trying to fix it, or you installed a second instance (likely a Flatpak) alongside the native one. Now you have two binaries competing for the same configuration folders, which is a recipe for crashed plugins and lost scenes. 1. The Reality: Why you have "two" On CachyOS/Arch, if you installed via pacman (native) and then tried flatpak, they live in different worlds: Native: /usr/bin/obs Flatpak: /var/lib/flatpak/exports/bin/com.obsproject.Studio 2. The Clean Slate (Action Plan) If you want a stable stream, you need to pick one path and burn the other. Don't leave remnants. Step A: Identity the Bloat Run this command to see what is actually installed: pacman -Qs obs-studio && flatpak list | grep obs Step B: The Purge If you see both, delete the native version. It clearly isn't working for you because of the missing Browser Source dependencies. sudo pacman -Rns obs-studio Note: This removes the app and its unused dependencies. Your scenes (stored in ~/.config/obs-studio) should stay safe, but back them up if you're paranoid. Step C: The Fix Now, install the Flatpak version properly. It is the only version on Linux that consistently bundles the Browser Source (CEF) without making you hunt for Arch headers. flatpak install flathub com.obsproject.Studio 3. The "CachyOS" Performance Trap You’re likely using CachyOS for those "gaming gains" and optimized kernels. You might worry that a Flatpak is "slower." The Truth: For OBS, the performance difference is negligible. The Opportunity Cost: Spending three hours debugging libcef.so dependencies on a native Arch build is time you aren't streaming. Use the Flatpak. It works. Do this now: Run that pacman -Rns command. Don't "keep the old one just in case"—it’s dead weight. Once you launch the Flatpak version, look at the Sources (+) menu. Is Browser there now?
