---
category: coding
date: 2026-02-03
id: 438166
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble installing the 'windsurf-bin' package using both
  'yay' and 'paru' package managers on CachyOS, and is also using the Fish shell.
tags:
- cachyos
- package-management
- yay
- paru
- windsurf-bin
- fish-shell
---
# ❯ yay -S windsurf-bin
fish: Unknown command: yay

~
❯ paru -S windsurf-bin
:: Resolving dependencies...
error: could not find all required packages:
    windsurf-bin (target)

~
❯ 

### USER
❯ yay -S windsurf-bin
fish: Unknown command: yay

~
❯ paru -S windsurf-bin
:: Resolving dependencies...
error: could not find all required packages:
    windsurf-bin (target)

~
❯ 

### GEMINI
It looks like you’re trying to use tools you haven't installed, searching for a package name that doesn't exist in the AUR yet. Let’s stop guessing and fix this. The Reality Check You’re hitting "command not found" because you’re trying to use Arch-specific helpers (yay) on a fresh CachyOS install without verifying if they're there, and you're searching for a package (windsurf-bin) that isn't currently in the standard AUR. Stop looking for an automated script for an IDE that is this new. If it's not in the AUR, you stop waiting for someone else to package it and you do it yourself. The Precise Plan 1. Install a Helper First CachyOS usually ships with paru. If it says "command not found," install it properly: sudo pacman -S paru 2. Install Windsurf via the Correct AUR Package The package is currently named windsurf, not windsurf-bin. paru -S windsurf Note: If paru still fails to find it, the AUR index might be out of sync on your local machine. Use paru -Sy windsurf. 3. The Manual Fallback (The "Pro" Way) If the AUR package fails or is broken, don't sit there frustrated. Download the .tar.gz from the official Codeium/Windsurf site and link it manually. This takes 30 seconds: Download and Extract to /opt/: sudo tar -xvf windsurf.tar.gz -C /opt/ Create the Symlink (This is what makes the windsurf command work): sudo ln -s /opt/Windsurf/bin/windsurf /usr/local/bin/windsurf The Blind Spot You are currently in "Dependency Hell"—a common trap for developers who want the latest tools but haven't mastered the package manager of their own OS. The Opportunity Cost: You’ve spent more time trying to invoke the IDE than you have using it. The Fix: If a package isn't in the AUR, don't keep typing variations of the name. Check aur.archlinux.org directly. If it's not there, download the binary, link it to /usr/local/bin, and get back to work. Shall I give you a script that checks for a package's existence in the AUR before you waste time running commands that don't exist?
