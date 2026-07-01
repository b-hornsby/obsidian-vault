---
category: general
date: 2026-03-09
id: 183136
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is stating that he cannot find the global shortcuts option in the KDE
  settings panel.
tags:
- kde
- global-shortcuts
- configuration
- customization
- cachyos
---
# there is no global shortcuts in the middle pane

### USER
there is no global shortcuts in the middle pane

### GEMINI
In KDE Plasma 6 (which CachyOS uses), the "Global Shortcuts" section was redesigned and simplified. It’s no longer its own separate tab; instead, everything is now integrated into a single list under Shortcuts. Since the pop-up disappeared, follow these exact steps to find where those 58 OBS shortcuts are hiding: 1. Find the OBS Shortcuts Open System Settings. Go to Keyboard → Shortcuts. Click on the Shortcuts button in the middle (if it’s not already selected). You should see a list of "Components" (like KWin, Plasma, etc.). Look for a button that says "Add New" or a "+" icon, or simply scroll through the list to see if "OBS Studio" has appeared as its own category. The Shortcut Search: If you don't see it, use the Search bar at the top of the Shortcuts window and type: Replay. 2. If OBS Studio is still missing from the list If searching for "Replay" shows nothing, it means the system "forgot" the request when the window was closed. We need to force OBS to ask the system for those shortcuts again. Close OBS. Open your terminal and run this command to reset the portal's "memory" for OBS: rm ~/.config/obs-studio/plugin_config/obs-wayland-hotkeys/state.json Open OBS. The "wants to register 58 shortcuts" window will pop up again. This time, do not close it. Scroll down to "Save Replay", click the "None" button, and press your hotkey. Crucial: Click OK at the bottom of that pop-up window before doing anything else. The Advisor's Observation You're hitting the "Plasma 6 transition" friction. Plasma 6 moved custom commands and app-specific global shortcuts into a unified backend to make them more reliable, but the migration from the old "pop-up" style can be clunky. One quick tip: If you find the "Save Replay" shortcut in that big list of 58, you can also map "Start/Stop Replay Buffer" there. This ensures your recording is actually running before you try to save a clip. Did the Search bar trick find "Save Replay" in your System Settings, or do we need to run that rm command to force the pop-up back?
