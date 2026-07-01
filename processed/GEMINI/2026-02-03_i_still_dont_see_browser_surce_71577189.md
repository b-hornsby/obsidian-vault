---
category: streaming
date: 2026-02-03
id: 097569
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan still can't see the browser source option in OBS on CachyOS after attempting
  fixes.
tags:
- obs-studio
- browser-source
- cachyos
- obs-plugin-missing
---
# i still dont see browser surce

### USER
i still dont see browser surce

### GEMINI
Here is the blunt truth: you are running the official Arch package, and the official Arch package maintainers have a long-standing "purist" stance against including the Browser Source because of the complex dependencies it requires (specifically CEF/Chromium). You are trying to find a feature in a version of the software where it was intentionally left out. The Solution: The "CachyOS" Fix Because you are on CachyOS, you have access to their specific repository, which actually provides a version with the browser source included. You need to swap your current installation for the one that actually works. Run this exact command: sudo pacman -S obs-studio-browser What this does: It will ask to replace obs-studio. Say Yes. Why this works: The obs-studio-browser package in the CachyOS repo is pre-compiled with the browser integration you’re looking for. If that doesn't work (The "Nuclear" Option) If for some reason you still don't see it or the repo is acting up, the Flatpak version of OBS is the only one guaranteed to have the Browser Source working out of the box on every Linux distro without you having to compile code like it's 1995. Remove the old one: sudo pacman -Rns obs-studio Install Flatpak: sudo pacman -S flatpak Install OBS: flatpak install flathub com.obsproject.Studio Brutal Advisor Post-Mortem You wasted 20 minutes looking for a button that wasn't there because you assumed all "OBS" installs are created equal. They aren't. On Linux, the source of your package matters as much as the package itself. Your blind spot: You’re treating your OS like Windows where you just "download the exe." On Arch/Cachy, you have to know which specific maintainer included the features you need. Next Step: Run the obs-studio-browser command. Once it's installed, open OBS and look for "Browser" under the + menu in Sources. Shall I help you set up your first scene once you've confirmed the Browser source is finally visible?
