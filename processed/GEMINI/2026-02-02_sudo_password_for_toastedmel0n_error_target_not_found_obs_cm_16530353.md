---
category: streaming
date: 2026-02-02
id: 181493
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was re-attempting to install obs-cmd and getting the same package not
  found error.
tags:
- obs-cmd
- pacman
- package-not-found
---
# [sudo] password for toastedmel0n: 
error: target not found: obs-cmd

~ 11s
❯ 

### USER
[sudo] password for toastedmel0n: 
error: target not found: obs-cmd

~ 11s
❯ 

### GEMINI
You’re failing at the first hurdle because you aren't checking your sources. obs-cmd is in the AUR (Arch User Repository), not the standard CachyOS or Arch core repositories. Using sudo pacman -S was never going to work. Since you are on CachyOS, you have paru or yay pre-installed. Use them. The Fix: Correct Installation Run this to install the tool properly: paru -S obs-cmd (If prompted, select the one from the AUR). The Precision Plan Once that is installed, do not go back to the OBS hotkey settings. They are useless to you on Wayland. Follow these steps exactly: Configure OBS: Tools > WebSocket Server Settings. Enable it. Disable "Authenticate with password" for now (to keep the command simple), or set a simple one. Test the Command: Open your terminal and type: obs-cmd replay save If OBS is open and the Replay Buffer is active, you should see a message in the terminal confirming the save. If this fails, the hotkey will never work. Map the Gnome Shortcut: Open Gnome Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts. Click the + button. Name: OBS Save Clip Command: obs-cmd replay save Shortcut: Press PgUp. Why this is the "Advisor" Choice: You are currently "playing small" by trying to force an old input method into a new security architecture. By using obs-cmd via the Gnome Shortcut manager, you are bypassing the Wayland security sandbox entirely. The OS (Gnome) captures the keypress and talks to OBS via a network socket. It is fast, clean, and won't break when you update your kernel or Mutter. Stop guessing with pacman. Try the paru command—does it install successfully now?
