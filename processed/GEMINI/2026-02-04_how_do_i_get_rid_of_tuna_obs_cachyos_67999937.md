---
category: streaming
date: 2026-02-04
id: 027953
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to uninstall OBS Tuna from OBS Studio on CachyOS.
tags:
- obs-studio
- obs-tuna
- uninstall
- cachyos
- streaming-tools
---
# how do i get rid of tuna obs cachyos?

### USER
how do i get rid of tuna obs cachyos?

### GEMINI
To get rid of Tuna on CachyOS, you need to determine how you installed it. Since you're on an Arch-based system, it’s likely either a package manager install or a manual folder drop. 1. The Package Manager Way (Try this first) If you installed it via paru or pacman, this command will wipe it and its unused dependencies: paru -Rns obs-tuna If it says "target not found," it means you either didn't use the AUR or the package name is slightly different. Try paru -Rns obs-tuna-git just in case. 2. The Manual Way (If the command above failed) Many Linux users install OBS plugins by dropping files into their home configuration folder. If the command above didn't work, Tuna is living in your hidden config files. Open your terminal. Run this command to delete the Tuna plugin files: rm -rf ~/.config/obs-studio/plugins/obs-tuna Also check the global folder (just in case): sudo rm -rf /usr/lib/obs-plugins/obs-tuna.so sudo rm -rf /usr/share/obs/obs-plugins/obs-tuna 3. Verification Restart OBS. Go to the Tools menu at the top. If "Tuna Settings" is gone, you’ve successfully purged it. The Advisor's Brutal Reality Check You’ve spent the last hour and a half in a "Search and Destroy" mission—deleting Shaders, deleting Firmware warnings, and now deleting Tuna. You are deep in the "System Administration Trap." You're cleaning your tools instead of using them to build something. Every minute you spend in the terminal is a minute you aren't streaming or creating content. My Recommendation: Stop the cleanup now. You've cleared the clutter. The Browser Source method I gave you earlier is the only thing you need to get that white-and-black text working without any more crashes. Would you like me to give you the final, simple instructions to set up that Browser Source so we can finally close the terminal?
