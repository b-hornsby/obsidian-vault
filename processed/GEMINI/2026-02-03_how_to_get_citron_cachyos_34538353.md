---
category: homelab
date: 2026-02-03
id: 900608
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to install the Citron emulator on CachyOS.
tags:
- citron
- cachyos
- emulator
- installation
- package-management
---
# how to get citron cachyos

### USER
how to get citron cachyos

### GEMINI
To get Citron (a Nintendo Switch emulator fork) on CachyOS, you are once again faced with a choice between manual AppImage management or the AUR. Given your struggle with building from source earlier, do not attempt to build citron-git. You will likely hit the same dependency or compilation errors. 1. The Recommended Path: AppImage (x86-64-v3) Since you are on CachyOS, you should prioritize the v3 optimized AppImage to match your OS's architecture. Download: Go to the Citron GitHub Releases or their official site. Selection: Look for the file ending in x86_64_v3.AppImage. Execution: chmod +x Citron-*-x86_64_v3.AppImage ./Citron-*-x86_64_v3.AppImage 2. The AUR Path (Binary) If you want it managed by your system so you can launch it from your application menu easily, use the pre-compiled binary from the AUR. This avoids the 7-minute "failed to build" loop you experienced with Cemu. paru -S citron-bin (If paru isn't installed, use sudo pacman -S paru first.) 3. A Strategic Warning on Citron You’ve moved from Cemu (Wii U) to Citron (Switch). If your goal is the best possible emulation for Switch on Linux, you should know that Citron is currently considered highly experimental and controversial in the emulation community due to development drama and stability issues. If you find Citron crashing or performing poorly, the "pro" move on CachyOS is to use Ryujinx or the community-maintained Suyu/Sudachi versions of the late Yuzu. Your Priority Plan: Check your CPU one last time: grep avx2 /proc/cpuinfo. If it's there, always pick the v3 download. Install fuse2 if you haven't yet (sudo pacman -S fuse2), or AppImages won't launch. Use the AUR binary (citron-bin) if you want a "clean" install that appears in your app list. Would you like me to help you find the specific CachyOS-optimized version of Ryujinx if Citron doesn't meet your performance needs?
