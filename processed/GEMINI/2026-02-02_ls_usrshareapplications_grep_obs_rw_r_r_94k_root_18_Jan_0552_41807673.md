---
id: 476105
source: GEMINI
date: 2026-02-02
tags: ['obs-desktop-entry', 'cachyos', 'application-files', 'obs-studio']
category: streaming
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed the OBS Studio desktop entry file exists in /usr/share/applications/ on CachyOS.
---
# ❯ ls /usr/share/applications/ | grep obs
.rw-r--r-- 9.4k root 18 Jan 05:52 com.obsproject.Studio.desktop

~
❯ 

### USER
❯ ls /usr/share/applications/ | grep obs
.rw-r--r-- 9.4k root 18 Jan 05:52 com.obsproject.Studio.desktop

~
❯ 

### GEMINI
The filename is exactly what we expected. If the local override in ~/.local/share/applications/ isn't being prioritized, it’s usually because the desktop environment is caching the old path or the Exec line inside your local file has a slight syntax error. Let's fix this with a single, surgical command to ensure your local file is perfect and then force the system to recognize it. 1. Rewrite the Local Shortcut Run this entire block in your terminal to overwrite your local shortcut with the correct configuration: cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop [Desktop Entry] Version=1.0 Name=OBS Studio (Auto-Replay) Exec=obs --startreplaybuffer Icon=com.obsproject.Studio Terminal=false Type=Application Categories=Video;AudioVideo;Recorder; StartupWMClass=obs EOF Why this works: I changed the Name to "OBS Studio (Auto-Replay)". This is a diagnostic trick. If you open your application menu and see a shortcut named "Auto-Replay," you know the system is finally looking at your file. 2. Clear the Cache CachyOS (likely using KDE Plasma) caches its menu. Force a refresh: kbuildsycoca6 (If you get a "command not found," try kbuildsycoca5 or just log out and back in). 3. The "High-Level" Audit Now that you are forcing the Replay Buffer to be on, you need to be aware of the Opportunity Cost of your RAM and Disk I/O: RAM Usage: Since the Replay Buffer stores the last 60–120 seconds of gameplay in your memory before you hit "Save," ensure you aren't starving your game. If you have 16GB of RAM, keep the buffer under 200MB. If you have 32GB+, feel free to go higher. The "Double Capture" Performance Hit: Make sure you are using Game Capture (PipeWire) and not "Screen Capture." Screen capture on Linux is significantly heavier and will cause micro-stutters that ruin the "pro" feel of your clips. One Final Test Close all instances of OBS. Search your apps for "OBS Studio (Auto-Replay)". Launch it. Does it show the "Stop Replay Buffer" button immediately? If it does, you're done with the setup. Would you like me to give you the ffmpeg command to instantly trim or convert those clips if they end up being too large for Discord or social media?
