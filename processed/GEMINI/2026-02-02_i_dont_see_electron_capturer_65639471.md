---
id: 310882
source: GEMINI
date: 2026-02-02
tags: ['electron-capturer', 'obs-studio', 'window-capture', 'cachyos', 'streaming']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/personal/streaming.md']
summary: Bryan was looking for the Electron Capturer option in OBS Studio for window capture on CachyOS.
---
# i dont see electron capturer

### USER
i dont see electron capturer

### GEMINI
If you don’t see the "Use Electron Capturer" toggle, it’s because it’s tucked away in a specific submenu that isn't under the main "Vencord" plugins list. Since you're on GNOME 49 (Wayland) on CachyOS, the flickering is almost certainly a conflict between Electron's internal capture method and the system's PipeWire portal. 1. The Real Location of the Toggle In the Vesktop app: Open User Settings (the gear icon at the bottom left). Scroll down the left sidebar until you see the Vencord section. Look for Vesktop Settings (this is usually separate from the "Plugins" tab). Inside Vesktop Settings, look for the "Use Electron Capturer" toggle. Turn it OFF. > Why? Disabling this forces the app to use the xdg-desktop-portal-gnome, which is the "correct" Wayland way to share your screen. If this is missing, you may be on an older version of Vesktop—update it via pacman -Syu. 2. The Hard Reset (If you still can't find it) If the UI is flickering too much to navigate, or the setting is missing, force it via the configuration file. This is the "brutally direct" way to bypass a buggy UI. Close Vesktop completely. Open your terminal and run: nano ~/.config/vesktop/settings.json Look for the line: "hardwareAcceleration": true and change it to false. Look for "useElectronCapturer": true (if it exists) and change it to false. Press Ctrl+O, Enter, then Ctrl+X to save and exit. Wipe the GPU Cache (Crucial for CachyOS/NVIDIA/GNOME 49 updates): rm -rf ~/.config/vesktop/GPUCache ~/.config/vesktop/Cache 3. Check for "Variable Refresh Rate" (VRR) On GNOME 49, if you have a high-refresh-rate monitor, flickering often occurs when the frame rate of the screen share doesn't match your monitor's sync. Go to GNOME Settings > Displays. Select your monitor and turn Variable Refresh Rate to Off. Test the screen share again. The Advisor's Verdict You're likely looking for a plugin that doesn't exist. "Use Electron Capturer" is an app-level setting, not a Vencord plugin. If you still don't see it, your Vesktop version is either ancient or your config file is borked. Next step: Run cat ~/.config/vesktop/settings.json in your terminal and paste the output here. I'll tell you exactly which line to strike out to kill the flicker.
