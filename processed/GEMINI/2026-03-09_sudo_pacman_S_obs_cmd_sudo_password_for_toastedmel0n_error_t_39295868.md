---
category: streaming
date: 2026-03-09
id: 279665
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering an error while trying to install obs-cmd using pacman
  because the package cannot be found.
tags:
- pacman
- package-manager
- obs-cmd
- package-not-found
- cachyos
---
# ❯ sudo pacman -S obs-cmd
[sudo] password for toastedmel0n:  
error: target not found: obs-cmd

~
❯ 

### USER
❯ sudo pacman -S obs-cmd
[sudo] password for toastedmel0n:  
error: target not found: obs-cmd

~
❯ 

### GEMINI
The error is because obs-cmd isn't in the official Arch or CachyOS repositories; it lives in the AUR (Arch User Repository). Since you are on CachyOS, you likely have paru or yay installed as your AUR helper. Use one of these instead: 1. Install from the AUR Try this command: paru -S obs-cmd-bin (If paru isn't found, try yay -S obs-cmd-bin. Using the -bin version is faster because it doesn't have to compile from source.) 2. The Brutal Truth on "Vibe Coding" Your Setup You’re trying to build a high-performance streaming and gaming environment on CachyOS, but you're hitting a wall because you're treating Linux like Windows. In Windows, "it just works." In Linux, permissions are the law. If you keep trying to force OBS to "see" your keys through the Legacy X11 hack, you are essentially weakening your system's security and risking frame-time stuttering for the sake of a shortcut. The Opportunity Cost: Every minute you spend troubleshooting why a hotkey won't fire is a minute you aren't streaming, gaming, or working on your trading bot. 3. Verification Step Once installed, verify it's working by running this in your Fish shell: obs-cmd --version If that returns a version number, move to the WebSocket step we discussed. If you get an error about "Connection Refused," it means you forgot to check the "Enable WebSocket Server" box in OBS under Tools -> WebSocket Server Settings. Would you like me to give you a single Fish function you can paste into your config so you can just type saveclip in any terminal to test it?
