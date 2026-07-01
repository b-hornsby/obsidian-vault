---
category: streaming
date: 2026-03-09
id: 985952
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is checking if a proposed solution will work with his existing OBS
  hotkey setup for creating clips.
tags:
- obs-studio
- hotkeys
- replay-buffer
- streaming-setup
- clip-creation
---
# and this will work with my key bind i have set up in obs for clipping? 

### USER
and this will work with my key bind i have set up in obs for clipping? 

### GEMINI
No. This replaces the keybind you set up in OBS. The whole reason your current OBS keybind isn't working is that Wayland is "deaf" to OBS when you're in another window. If you keep trying to use the hotkey inside the OBS settings, it will continue to fail the second you click over to Apex or Fortnite. How it works now: You are moving the "brain" of the hotkey from OBS to your Operating System (CachyOS/KDE). Remove the hotkey from OBS's internal settings (to avoid confusion). Go to System Settings → Shortcuts → Commands. Add the command: obs-cmd replay save Assign the exact same keybind there. Now, when you press that button, CachyOS hears it, runs the obs-cmd script, and tells OBS via the "back door" (WebSocket) to save the clip. It doesn't matter if OBS is minimized, on your second monitor, or "out of focus"—it will work every time. The Advisor's Cold Truth You’re looking for a way to keep your old workflow without changing your habits. In the Windows world, you can be lazy because the OS is less secure. On Linux/Wayland, logic is king. If you want the clip, you have to trigger it from the level of the system that actually has permission to hear your keyboard. The OBS internal hotkey menu is essentially useless to you now that you've migrated to CachyOS. Accept the new workflow: System Shortcut = Global power. App Shortcut = Local power (only works when the window is active). Do you want the command to send a desktop notification as well, so you get a visual "Clip Saved" confirmation over your game?
