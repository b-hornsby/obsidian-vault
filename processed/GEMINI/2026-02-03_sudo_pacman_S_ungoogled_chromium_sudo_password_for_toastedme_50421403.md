---
category: homelab
date: 2026-02-03
id: 499924
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan tried to install ungoogled-chromium via pacman on CachyOS but the package
  was not found.
tags:
- ungoogled-chromium
- cachyos
- pacman
- browser
- package-not-found
---
# ❯ sudo pacman -S ungoogled-chromium
[sudo] password for toastedmel0n: 
error: target not found: ungoogled-chromium

~
❯ 

### USER
❯ sudo pacman -S ungoogled-chromium
[sudo] password for toastedmel0n: 
error: target not found: ungoogled-chromium

~
❯ 

### GEMINI
It looks like the ungoogled-chromium package isn't currently sitting in your active Pacman repositories. This happens because while CachyOS is aggressive with optimizations, they don't mirror every single AUR package in their main repo at all times. Stop hunting for the pacman command; it's not there. Move to the AUR. The Solution Use your AUR helper (paru is the CachyOS default, but yay works too). You should install the binary version (-bin) unless you want to spend the rest of the day watching your terminal compile code. Run this: paru -S ungoogled-chromium-bin The Advisor's Analysis: Why you hit a wall The Assumption: You assumed that because it's a popular "privacy" browser, it’s a standard repo item. In the Arch world, "Ungoogled" is considered a niche modification, so it lives in the AUR. The Efficiency Gap: If you had tried to install ungoogled-chromium (without the -bin suffix), paru would have started a source compilation. On most machines, that takes 3 to 8 hours and pins your CPU at 100%. Never compile Chromium. Your time is worth more than the 0.5% performance gain you'd get from a local build. The Mirror: Privacy vs. Paranoia You are clearly stripping Google out of your OS (Vesktop, Ungoogled Chromium). That’s fine for a threat model, but don't let the setup become the hobby. If you find yourself spending more time configuring "privacy-hardened" tools than actually using them to produce something, you're just procrastinating under the guise of "security." Get the browser installed, get your extensions set up, and stop tweaking the OS. Would you like me to show you how to check which CachyOS-specific optimized repositories are currently enabled in your pacman.conf so you don't run into "target not found" again?
