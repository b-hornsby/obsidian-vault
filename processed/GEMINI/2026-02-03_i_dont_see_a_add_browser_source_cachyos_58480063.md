---
category: streaming
date: 2026-02-03
id: 618439
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan can't find the 'Add Browser Source' option in OBS on CachyOS, likely
  missing the browser plugin.
tags:
- obs-studio
- browser-source
- cachyos
- obs-plugin-missing
---
# i don't see a add browser source? cachyos

### USER
i don't see a add browser source? cachyos

### GEMINI
If you don’t see the Browser Source option in OBS on CachyOS (which is Arch-based), it’s because you are likely using the Flatpak version or a repository build that didn't include the CEF (Chromium Embedded Framework) dependencies. This is a common "blind spot" for Linux users—assuming everything is bundled. On Linux, the Browser Source is a separate beast. If it's missing, you aren't "streaming," you're just capturing a screen. You need to fix the environment. 1. The "Lazy" (But Effective) Fix: Flatpak If you want things to just work without hunting down dependencies, use the Flatpak version. It bundles the browser plugin correctly. Uninstall your current OBS. Run: flatpak install flathub com.obsproject.Studio Restart OBS. The Browser Source will be there. 2. The "Arch Way" (CachyOS Native) If you want to keep the native performance of CachyOS, you are likely missing the obs-studio-browser functionality or using the base package that doesn't include it. Check if obs-studio is installed via pacman. On CachyOS/Arch, the standard obs-studio package should include it, but if it's broken, you might need to switch to the AUR version which is often more robust for feature parity: Install obs-studio-tytan652 or obs-studio-git from the AUR. These versions are maintained specifically to ensure things like Browser Source and Wayland support are fully functional. 3. The Wayland Trap If you are running Wayland (likely on CachyOS), check your launch flags. If OBS is running through XWayland, the browser source can occasionally glitch out or fail to initialize. Try launching OBS with: QT_QPA_PLATFORM=wayland obs Or, if it's already on Wayland, try forcing X11 to see if the source appears: QT_QPA_PLATFORM=xcb obs The Reality Check You're trying to set up a high-end stream on a "bleeding edge" Linux distro. This is the Opportunity Cost of CachyOS: you get speed, but you spend your time troubleshooting basic plugin dependencies instead of actually creating content. Stop fighting the OS. If the Browser Source doesn't show up after a reinstall of the obs-studio package, move to the Flatpak. It is the only way to ensure the CEF environment is isolated and functional without you having to manually compile browser headers. Which version did you install? Run pacman -Qi obs-studio and tell me what the "Packager" or "Source" says so I can tell you exactly which command to run to fix the missing header.
