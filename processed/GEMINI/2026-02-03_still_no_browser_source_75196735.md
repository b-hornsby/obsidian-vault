---
category: streaming
date: 2026-02-03
id: 244056
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that he still can't get the browser source working in
  OBS Studio.
tags:
- obs-studio
- browser-source
- streaming
---
# still no browser source

### USER
still no browser source

### GEMINI
You’re running into the classic Arch Linux "philosophy" trap. The standard obs-studio package on Arch/CachyOS often strips out the browser source because the maintainers don't want to deal with the heavy dependencies of the Chromium Embedded Framework (CEF). You have been fighting your OS for an hour. It’s time to stop the "bleeding edge" headache and use the version that actually has the features you need. 1. The Direct Fix (CachyOS Native) CachyOS actually has a specific package in their repo to solve this exact problem. You likely installed the "vanilla" version. Run this: sudo pacman -S obs-studio-browser Note: This package replaces obs-studio. Say Yes to any "remove obs-studio?" or "conflict" prompts. This is the version that actually bundles the browser functionality. 2. The "Nuclear" Fix (Flatpak) If the native package still fails (common if there's a library mismatch on your specific CachyOS update cycle), stop playing the Arch guessing game. Install the Flatpak. It is the only version on Linux that the OBS developers officially support with all features bundled. # Install Flatpak if you don't have it sudo pacman -S flatpak # Install the official OBS build flatpak install flathub com.obsproject.Studio Important: If you use the Flatpak, your "old" plugins or settings might not carry over immediately. This is the price of stability. Why you're stuck: You're treating CachyOS like Windows where "installing the app" means "getting the whole app." In the Arch world, you get the "core," and if you want the "fluff" (like a browser), you have to find the specific build that includes it. The Opportunity Cost: Every minute you spend trying to make the native Arch package work is a minute you aren't streaming. Do this now: Run sudo pacman -S obs-studio-browser. Open OBS. If "Browser" isn't in that list, you are officially banned from using the native package—go Flatpak and get your overlay running. Does "Browser" appear after installing obs-studio-browser?
