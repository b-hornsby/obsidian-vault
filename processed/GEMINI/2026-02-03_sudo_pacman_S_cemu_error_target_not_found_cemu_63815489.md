---
category: general
date: 2026-02-03
id: 894184
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install cemu using pacman but the target is not found.
tags:
- pacman
- cemu
- package-installation
- target-not-found
---
# ❯ sudo pacman -S cemu
error: target not found: cemu

~
❯ 

### USER
❯ sudo pacman -S cemu
error: target not found: cemu

~
❯ 

### GEMINI
You are being throttled by the fact that Cemu isn't in the standard Arch repositories yet—it’s only in the AUR and third-party repos. Since you’re on CachyOS, you have a better option than manual compilation. Stop trying to build it from source; you’re missing dependencies and wasting CPU cycles. Use the pre-compiled binary from the AUR to bypass the build errors entirely. 1. The "Path of Least Resistance" (Recommended) Install the binary version. This downloads the official Cemu release and packages it for Arch without needing to compile a single line of code. paru -S cemu-bin (If you don't have paru, use yay -S cemu-bin. If you have neither, install them first with sudo pacman -S paru). 2. The "I Must Use Pacman" Way If you absolutely want to use pacman -S, you have to add a repository that hosts the binary. Since you are on CachyOS, you should check if the cachyos-extra repo is enabled in your /etc/pacman.conf. However, the most reliable way right now for Cemu on Arch-based systems is the Flatpak. It is sandboxed, includes all dependencies (like the specific fmt and wxwidgets versions that usually break AUR builds), and just works. flatpak install flathub info.cemu.Cemu Why pacman -S cemu failed You were operating on the assumption that "Cemu" is a standard package like "Firefox." It isn't. It’s a community-maintained project on Linux. When you typed that command, you were asking pacman to find something that doesn't exist in the default Arch core or extra databases. Your Priority Plan: Run paru -S cemu-bin. It will take 30 seconds instead of 7 minutes. Launch it by typing Cemu. Go to Settings > Graphics and ensure Vulkan is selected. Would you like me to show you how to enable the CachyOS-v3/v4 repositories so you can get optimized gaming packages directly through pacman in the future?
