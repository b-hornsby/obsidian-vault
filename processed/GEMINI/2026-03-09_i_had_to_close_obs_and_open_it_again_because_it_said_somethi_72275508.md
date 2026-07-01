---
id: 821291
source: GEMINI
date: 2026-03-09
tags: ['obs-studio', 'configuration-issues', 'streaming-setup', 'troubleshooting', 'replay-buffer']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is experiencing issues with OBS Studio related to prior settings and is trying to resolve the problem.
---
# i had to close obs and open it again because it said something about prior settings and it wouldnt let me confirm. now it doesnt pop up with that menu

### USER
i had to close obs and open it again because it said something about prior settings and it wouldnt let me confirm. now it doesnt pop up with that menu

### GEMINI
That’s the Wayland security portal for you—it’s cautious. Once that window closes, it usually assumes you’ve made your choice. Since you didn't get to hit "OK," the system has essentially put those requests in "pending" or "ignored" status. Because you are on CachyOS (KDE Plasma), you don't need that pop-up to return. You can now go directly into the system's "control room" to finish the job. The Manual Fix Open your System Settings (the gear icon). Navigate to Keyboard → Shortcuts. Click on Global Shortcuts in the middle pane. On the left-hand side, look for OBS Studio in the list of applications. If you don't see it immediately, look for a "Commands" or "Web Portals" section, but it should have its own OBS entry now. Find "Save Replay" in that list. Click it, assign your hotkey, and hit Apply at the bottom. If it’s NOT in the list: If OBS Studio is missing from the Shortcuts menu, the portal "handshake" failed when you closed it. We need to force it to ask again. Close OBS. Run this in your terminal to clear the "denied" portal state: rm ~/.config/obs-studio/plugin_config/obs-wayland-hotkeys/state.json (If that file doesn't exist, don't worry, just proceed.) Open OBS. The "Global Shortcuts Requested" window should pop back up. The Advisor's Strategic Note You are currently fighting the "Security vs. Convenience" battle that defines the Linux experience. In Windows, apps just "steal" your keyboard focus. Here, you have to explicitly grant it. Once you map this in the System Settings, it is a permanent fix. You won't have to deal with passwords, firewalls, or X11 lag ever again. Go check the System Settings → Shortcuts menu now. Is "Save Replay" waiting for you there?
