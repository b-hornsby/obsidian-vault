---
category: streaming
date: 2026-03-09
id: 475967
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is asking for alternative solutions to a problem after a previous attempt
  failed.
tags:
- troubleshooting
- problem-solving
- alternative-solutions
- obs-studio
- streaming-setup
---
# so seeing as that didnt work what is the best solution to the issue i described at this point? 

### USER
so seeing as that didnt work what is the best solution to the issue i described at this point? 

### GEMINI
Since we’ve stripped away the "hacks" and cleaned up the firewall, we’re going to use the native Wayland solution. On CachyOS (and most modern Linux distros), the "Best" solution isn't a workaround—it’s using the XDG Desktop Portal. This allows the OS to handle the hotkey and "pass" it to OBS without needing a password, a port, or X11 legacy support. The "Gold Standard" Fix: obs-wayland-hotkeys This plugin bridges the gap between OBS and your System Settings. Instead of putting the hotkey inside OBS, you put it in your KDE System Settings. 1. Install the Plugin Since you're on CachyOS, use paru to grab the specific bridge for Wayland: paru -S obs-wayland-hotkeys-git 2. The Initial Handshake Open OBS. A system pop-up (from KDE) should appear asking for permission to "Add Keyboard Shortcuts" for OBS Studio. Accept it. If no pop-up appears, don't panic; it just means the portal is already active in the background. 3. Map the Global Hotkey This is the most important part: Stop looking in the OBS Settings menu. Open your System Settings (KDE Plasma). Navigate to Keyboard → Shortcuts. On the left-hand side, look for OBS Studio in the list of applications. Find the entry for "Save Replay" (or "Replay Buffer - Save"). Click it and press your desired key combination. Why this is the "Strategic" Winner: Performance: OBS stays in "Native Wayland" mode. Since you play Apex and Fortnite, this ensures you don't get the micro-stutters that X11 legacy mode can cause. Security: Your firewall stays active and closed. No passwords are sent over local ports. Consistency: Because the OS is handling the keypress, it doesn't matter if you're in a high-intensity firefight in Apex or browsing the web; the OS will always send that "Save" signal to OBS. One "Advisor" Warning: If you don't see "OBS Studio" in your System Settings → Shortcuts after installing the plugin and restarting OBS, it means the portal didn't register. If that happens, run this command to see if the plugin is actually loaded: ls /usr/lib/obs-plugins/ | grep wayland Once you map that key in the System Settings, go into a game and try it. Does the "Replay Saved" notification finally pop up in the corner of your OBS window?
