---
category: streaming
date: 2026-02-02
id: 877226
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to install obs-cmd via pacman but the package was not found
  in the repositories.
tags:
- obs-cmd
- pacman
- package-installation
---
# ❯ sudo pacman -S obs-cmd
[sudo] password for toastedmel0n: 
error: target not found: obs-cmd

~ 6s
❯ 

### USER
❯ sudo pacman -S obs-cmd
[sudo] password for toastedmel0n: 
error: target not found: obs-cmd

~ 6s
❯ 

### GEMINI
Ah, the classic Arch-user moment: searching for a specialized tool that hasn't hit the official repos yet. On CachyOS (and Arch), obs-cmd lives in the AUR (Arch User Repository), not the standard Pacman repositories. Since you're on CachyOS, you likely have paru or yay installed as your AUR helper. Use one of those instead. 1. Install via AUR Try this command: paru -S obs-cmd (If you don't have paru, try yay -S obs-cmd. If you have neither, run sudo pacman -S paru first). 2. If you don't want to mess with the AUR If you want to avoid installing more packages, you can use Python (which is definitely already on your system) to talk to OBS. Enable the OBS Websocket (Tools > WebSocket Server Settings). Use this one-liner in your OpenDeck command field (replace PORT and PASSWORD): python -c "import obsws_python as obs; cl = obs.ReqClient(host='localhost', port=4455, password='yourpassword'); cl.save_replay_buffer()" Note: You might need to run pip install obsws-python first for this specific method. 3. The "Pure GNOME" Hotkey Workaround If you want to keep using the PgUp key on your keyboard instead of the Stream Deck, GNOME will only let it work if you register it as a System Shortcut: Go to Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts. Click Add Shortcut. Name: Save OBS Clip Command: obs-cmd --password yourpassword replay save (once installed). Shortcut: Press PgUp. Why this works: When you register a "Custom Shortcut" in GNOME, the Desktop Environment intercepts the PgUp key before it gets to the game, runs the command, and sends the signal to OBS. Which route are we taking? If paru worked and you got obs-cmd installed, stop here—you're ready to go. Should I help you troubleshoot the paru install or are we moving on to testing the button?
