---
category: homelab
date: 2026-02-04
id: 625245
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan couldn't find the Clipboard & Input > Global Shortcuts section in KDE
  System Settings on CachyOS.
tags:
- kde
- system-settings
- global-shortcuts
- cachyos
- troubleshooting
---
# i dont see System Settings > Clipboard & Input > Global Shortcuts on kde

### USER
i dont see System Settings > Clipboard & Input > Global Shortcuts on kde

### GEMINI
If you don’t see that specific path, it’s because you are likely on KDE Plasma 6 (CachyOS moves fast). The menu layout changed, and more importantly, Wayland—the display engine CachyOS defaults to—has a "security" feature that specifically breaks background hotkeys for apps like OBS. In Wayland, a background app is technically a "keylogger" if it listens to your keys while you're in a game. Wayland blocks this by default. Here is the exact way to fix this on CachyOS/KDE: 1. The "Legacy" Fix (Most likely to work) KDE has a specific setting to allow X11 apps (like the version of OBS you might be running) to see global keys. Open System Settings. Go to Input Devices > Keyboard. Look for a tab or button labeled "Advanced" or "Configure Keyboard Options". Search for "Legacy X11 App Support". Set it to "Always" or "Allowed to read global keystrokes." 2. Force OBS to run in X11 Mode If the above doesn't work, you can force OBS to run using the older display protocol (Xwayland), which doesn't have these strict security blocks. Close OBS. Open your terminal and run this command to test: QT_QPA_PLATFORM=xcb obs If your hotkeys work now, you can edit your OBS shortcut (right-click application launcher > Edit Applications) and put QT_QPA_PLATFORM=xcb before the command. 3. The "Pure Wayland" Manual Bypass If you refuse to use X11, you have to tell KDE itself to trigger the save. Go to System Settings > Shortcuts > Shortcuts > Commands (or "Add New"). Create a new command called "OBS Save Replay". For the command, use: obs-cli replay save (This requires the obs-cli package from the AUR). Assign Page Down to this KDE command instead of inside OBS. The Reality Check You’re on CachyOS because you want performance, but you're hitting the "Bleeding Edge Tax." Wayland is the future, but for streamers and "clippers," it's currently a headache. My advice: If you just want it to work now without scripting, log out and change your session type from Plasma (Wayland) to Plasma (X11) at the bottom of the login screen. It will solve 100% of your hotkey issues instantly. Do you want to stick with Wayland and try the script method, or are you willing to switch to X11 for the stability?
