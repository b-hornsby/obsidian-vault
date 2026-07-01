---
category: streaming
date: 2026-03-09
id: 390598
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if a specific terminal command for legacy X11 support needs
  to be run every time, even with the setting enabled.
tags:
- legacy-x11
- obs-studio
- cachyos
- compatibility
- streaming-setup
---
# i have the legacy x11 app support set to always allowed. do i need to run that terminal command each time? 

### USER
i have the legacy x11 app support set to always allowed. do i need to run that terminal command each time? 

### GEMINI
If you have "Always Allowed" checked in your System Settings, you technically shouldn't need the terminal command, but there’s a catch: CachyOS and other modern Arch-based distros often default to the Wayland native version of OBS. If OBS starts as a Wayland app, it ignores that "Legacy X11" setting entirely because it's not a "Legacy" app—it's trying to be modern, which is exactly why your hotkeys are failing. The "Permanent Fix" (No Terminal Needed) You don't want to type a command every time you want to game. You should modify the OBS Desktop Entry so it always launches in X11 mode when you click the icon. Copy the desktop file to your local folder: cp /usr/share/applications/com.obsproject.Studio.desktop ~/.local/share/applications/ Open that file for editing: Use your preferred editor (like Kate or Nano): nano ~/.local/share/applications/com.obsproject.Studio.desktop Modify the Exec line: Find the line that starts with Exec= and change it to: Exec=env QT_QPA_PLATFORM=xcb obs Save and Exit. Now, whenever you launch OBS from your app menu or dock, it will automatically run in X11 mode, allowing it to "see" your hotkeys globally while you're in Apex or Fortnite. A Brutal Reality Check While this fixes the hotkey, running OBS in X11 mode on a Wayland compositor (like KWin on CachyOS) can sometimes introduce micro-stutter or frame-pacing issues in your recordings. If you notice your clips look "choppy" even though your game feels smooth: The "Vibe" Solution: Just use the obs-cmd method I mentioned (Option 2 in the previous reply). It allows OBS to stay in native Wayland (smoother recording) while letting the System handle the hotkey. It’s a 5-minute setup that saves you from performance headaches later. Would you like the specific obs-cmd setup for your Fish shell so you can stop wrestling with X11 compatibility?
