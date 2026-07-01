---
category: homelab
date: 2026-02-03
id: 978793
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to install the Citron emulator on the CachyOS operating
  system.
tags:
- citron
- cachyos
- emulator
- installation
- package-management
---
# how do i get citron on cachyos?

### USER
how do i get citron on cachyos?

### GEMINI
To get Citron (a Nintendo Switch emulator) on CachyOS, you have a few options. Since CachyOS is Arch-based, you have the advantage of the AUR (Arch User Repository) and Cachy’s own optimized repositories. Here is the direct, no-nonsense path to getting it running. 1. The Recommended Way: AUR (Build from Source) The most reliable way to get Citron on an Arch-based system like CachyOS is via the AUR. This ensures the binary is compiled against your specific system libraries. Open your terminal and use paru (the default helper on CachyOS) or yay: paru -S citron-git Why this? It handles dependencies automatically and integrates the app into your system menu. The Reality Check: Citron is a fork (specifically of Yuzu/Suyu). If the AUR package is orphaned or fails to build, it's usually due to a dependency mismatch in the rapidly shifting Switch emulation scene. 2. The Portable Way: AppImage If you don't want to mess with build dependencies, search for the official Citron AppImage from their GitHub releases or community mirrors. Download the .AppImage file. Right-click the file -> Properties -> Permissions -> Allow executing file as program. Double-click to run. 3. The Flatpak Way Flatpak is the safest bet for stability because it bundles its own libraries, avoiding the "dependency hell" that sometimes hits rolling-release distros like Cachy. flatpak install flathub npi.citron.Citron (Note: Use flatpak search citron first to verify the exact ID, as names in the Flatpak space change frequently due to legal pressures on Switch emulators.) Critical Advice for CachyOS Users Kernel Choice: You are likely using the linux-cachyos kernel. This is great for latency, but ensure your GPU drivers (especially if NVIDIA) are up to date, as Citron relies heavily on Vulkan extensions. The "Switch" Problem: Remember that Citron, like its predecessors, requires prod.keys and Title.keys, plus the Switch Firmware. Without these, the software is a useless window. If you're "playing small" by trying to run this without properly dumped keys, you'll spend hours debugging "missing components" errors that aren't actually bugs. Your Strategic Blind Spot You are asking about Citron, a relatively niche fork in a volatile ecosystem. If your goal is simply "playing Switch games on Linux," you are likely overcomplicating it. Ryujinx remains the most stable, well-maintained, and feature-complete option for Linux. Unless Citron offers a specific hack for a game you're obsessed with, you're likely wasting time on a less mature tool. Would you like me to provide the commands to set up Ryujinx instead, or do you have a specific technical reason for sticking with Citron?
