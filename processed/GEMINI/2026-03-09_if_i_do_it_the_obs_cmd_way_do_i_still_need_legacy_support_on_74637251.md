---
category: streaming
date: 2026-03-09
id: 786366
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if legacy X11 support is still required when using obs-cmd
  for OBS Studio control.
tags:
- obs-cmd
- legacy-x11
- obs-studio
- cachyos
- streaming-setup
---
# if i do it the obs cmd way do i still need legacy support on?

### USER
if i do it the obs cmd way do i still need legacy support on?

### GEMINI
No. If you use the obs-cmd method, you can turn off Legacy X11 support entirely for OBS. In fact, that's the point of this setup. When you use a system shortcut to trigger a command, the operating system (CachyOS/KDE) handles the "listening" for your keys, and obs-cmd handles the "talking" to OBS via a network socket. This bypasses the Wayland security sandbox without needing to trick OBS into thinking it's an older X11 app. Why this is the "Pro" Move: Lower Latency: OBS stays in Native Wayland mode, which generally offers better frame pacing and less stutter on CachyOS. Privacy: You don't have to leave a "keylogger-shaped hole" in your security by allowing apps to read every keystroke. Reliability: It won't matter if your game is in Fullscreen, Borderless, or Windowed mode; the system shortcut will always fire. Quick Setup (Fish Shell) Since you're on CachyOS using Fish, here is the fastest way to verify it's working: Install the tool: sudo pacman -S obs-cmd In OBS: Go to Tools -> WebSocket Server Settings. Ensure Enable WebSocket Server is checked. Click Show Connect Info to see your password. Test it in your terminal: Run this command (replace your_password with yours): obs-cmd --password your_password replay save You should see a notification in OBS that the replay was saved. Final Step: Make it a Global Hotkey Now, instead of putting the hotkey inside OBS: Open System Settings -> Shortcuts -> Commands. Click Add New. Name: "Save OBS Clip" Command: obs-cmd --password your_password replay save Shortcut: Press the key combination you want to use. Strategic Tip: If you ever change your OBS password, you only have to update it in this one place in your System Settings, and it will work forever regardless of what game you are playing. Would you like me to show you how to add a "Replay Buffer Started" notification so you're never caught gaming without your recorder active?
