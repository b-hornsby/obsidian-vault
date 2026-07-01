---
category: streaming
date: 2026-02-02
id: 386150
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to fix his OBS replay buffer PgUp hotkey not working while
  gaming due to CachyOS/GNOME 49 keypress handling per window.
tags:
- obs-replay-buffer
- keybind-interception
- gnome-49
- cachyos
- wayland-keypress
---
# trying to get around cachyos with how it handles keypresses per window. i have replay buffer on in obs and i have pgup as my keybind to clip the last 30 seconds but when i try to do that while im playing it wont work? i'm on gnome 49.3, Linux 6.18.8-3-cachyos

### USER
trying to get around cachyos with how it handles keypresses per window. i have replay buffer on in obs and i have pgup as my keybind to clip the last 30 seconds but when i try to do that while im playing it wont work? i'm on gnome 49.3, Linux 6.18.8-3-cachyos

### GEMINI
The issue isn't CachyOS; it’s your understanding of how modern Linux desktops handle security. You are likely running on Wayland, which by design prevents one application (OBS) from "spying" on your keypresses while another window (your game) has focus. This isn't a bug—it’s a feature that you haven't accounted for in your setup. Here is the cold reality of your situation and how to fix it. The Blind Spot: Wayland Security In the X11 days, any app could see every keystroke. In Wayland (Gnome’s default), applications are isolated. OBS cannot see that you pressed PgUp because the game window is "consuming" that input. If you want this to work, you have to stop expecting the OS to just "work like Windows" and instead interface with the desktop environment's global shortcut handling. The Strategy: How to Fix It 1. The Global Shortcut Portal (The Modern Way) Gnome 46+ and OBS support the Global Shortcuts portal. Open OBS. Go to Settings > Hotkeys. Look for a notification or a "Global" indicator. If Gnome asks for permission to allow OBS to monitor shortcuts, grant it. Note: This is still hit-or-miss depending on your specific version of xdg-desktop-portal-gnome. 2. The "Brute Force" Fix (Xwayland Video Bridge) If the portal isn't catching the input, you need a bridge. Install xwaylandvideobridge from the Arch/Cachy repositories. This tool helps bridge the gap between X11-based input expectations and Wayland's isolation. 3. The "Legacy" Fallback (Switch to X11) If you want to stop fighting the protocol and just play your game: Log out of Gnome. Click the gear icon on the login screen. Select GNOME on Xorg. In Xorg, OBS will have zero issues seeing your PgUp key. The Trade-off: You lose the smoothness and modern touch-handling of Wayland. Decide if your "clipping" is worth the older tech stack. Priority Action Plan Immediate Check: Run echo $XDG_SESSION_TYPE in your terminal. If it says wayland, you have found your culprit. The Fix: Go to OBS Hotkeys, clear the PgUp bind, and re-bind it. If a system popup appears asking to "Allow OBS to handle shortcuts," you must click Allow. The Alternative: Use a controller or a secondary input device that sends a specific command via a script, though this is likely overkill for you. The Nuclear Option: If you refuse to troubleshoot Wayland's permissions, switch to Xorg and be done with it. Stop blaming the distro and start configuring the environment. Would you like me to walk you through checking your xdg-desktop-portal logs to see exactly why the keypress is being blocked?
