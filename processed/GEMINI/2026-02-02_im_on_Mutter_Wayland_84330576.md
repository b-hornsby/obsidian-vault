---
id: 947657
source: GEMINI
date: 2026-02-02
tags: ['mutter', 'wayland', 'display-server', 'linux']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is providing information about his display server (Mutter/Wayland), likely for troubleshooting a graphics-related issue.
---
# im on Mutter (Wayland)

### USER
im on Mutter (Wayland)

### GEMINI
Since you're on Mutter (Wayland), you are dealing with a protocol that treats "global hotkeys" as a security threat. In Mutter's eyes, an app listening for keypresses while it isn't focused is a keylogger. Even with recent updates in Gnome (48/49), the "Global Shortcuts" portal is still a mess and OBS doesn't always hook into it correctly on CachyOS. If you want your Replay Buffer to actually save when you hit PgUp, you have two real options: the Standard Workaround (running OBS in Xwayland) or the Advanced Automation (Websockets). Option 1: The Xwayland "Hack" (Easiest) By forcing OBS to run via Xwayland instead of Native Wayland, it regains the ability to see global keypresses (because Xwayland is less restrictive). Close OBS completely. Open your terminal and run it with this environment variable: QT_QPA_PLATFORM=xcb obs Test your PgUp key. If it works, you need to make this permanent. Make it Permanent: Edit your OBS desktop entry (usually in /usr/share/applications/com.obsproject.Studio.desktop or ~/.local/share/applications/). Find the Exec= line and change it to: Exec=env QT_QPA_PLATFORM=xcb obs Option 2: The "Clean" Way (Gnome Custom Shortcuts) If you hate the idea of running OBS in legacy mode, you have to tell Gnome itself to trigger the save. Since Gnome won't let OBS listen, you make Gnome send a command to OBS. Enable OBS Websocket: In OBS, go to Tools > WebSocket Server Settings. Check Enable WebSocket server. Note the port (default 4455) and password. Install a CLI Controller: Install obs-cmd (available in the AUR/Cachy repos): sudo pacman -S obs-cmd Create a Gnome Shortcut: Go to Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts. Add a new shortcut: Name: Save Replay Buffer Command: obs-cmd replay save (You may need to add --password YOURPASSWORD if you set one). Shortcut: Press PgUp. The Reality Check You are likely using Wayland for the performance/latency benefits in games. Option 2 is the superior "Wayland-native" solution because it doesn't degrade OBS's performance by forcing it through a translation layer (Xwayland). It also won't break when Gnome eventually removes X11 support entirely. Stop trying to bind the key inside the OBS settings menu; bind it in the Gnome Settings menu instead. Would you like the specific obs-cmd syntax to also trigger a notification so you actually know the clip saved?
