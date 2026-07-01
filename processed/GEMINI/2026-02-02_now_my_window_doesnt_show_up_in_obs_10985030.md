---
category: streaming
date: 2026-02-02
id: 277118
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting a window capture source not appearing in OBS.
tags:
- obs-studio
- window-capture
- source-not-showing
---
# now my window doesnt show up in obs?

### USER
now my window doesnt show up in obs?

### GEMINI
When you switched to "Window Capture (PipeWire)," you effectively changed the way OBS requests video from the OS. On GNOME 49 (Wayland), this often results in a black screen because the Permissions Portal is waiting for your approval, but the popup might be hidden, or the session is blocked by the "experimental" VRR flag we just messed with. Here is how to get the window back without re-enabling the flicker: 1. The "Open Selector" Ritual Unlike Windows, you can't just pick a window from a list in OBS. Wayland forces a system-level popup for security. In OBS, double-click your Window Capture (PipeWire) source. Click the "Open Selector" button. Wait. A GNOME system window should appear asking you to "Share a Window." If it doesn't appear, press Alt + Tab. Sometimes GNOME spawns this window behind OBS or your game. 2. The VRR Mismatch (The "Experimental" Side Effect) Since you just enabled the experimental VRR feature, the compositor (Mutter) might be having a stroke trying to virtualize a single window buffer while the rest of the screen is at a different state. If the selector is blank or the window is black, try disabling VRR in your Display settings now that the menu is visible. Reboot again. (I know, it’s annoying, but changing gsettings for Mutter requires a fresh compositor session to actually sync the PipeWire streams). 3. Check the "Window" vs "Screen" Source If Window Capture is failing, it's often because the game (Arc Raiders) is running in "Exclusive Fullscreen" mode, which Wayland treats as a "Screen" rather than a "Window." Try changing the source to Screen Capture (PipeWire) again. BUT, in the popup that GNOME shows, click the "Windows" tab instead of the "Entire Screen" tab. This uses the "Screen" portal logic but only pipes the specific window, which is often more stable on GNOME 49. 4. Direct Terminal Kick (The "CachyOS" Way) If the portal is still being stubborn and showing nothing: Close OBS. Run this to clear the portal's memory: systemctl --user restart xdg-desktop-portal-gnome xdg-desktop-portal Launch OBS with this specific flag to force it to use the Wayland pipe: QT_QPA_PLATFORM=wayland obs The Advisor's Verdict You're seeing a black screen because the handshake between OBS and GNOME was interrupted by the VRR change. Linux Wayland capture is a "request-response" system; if the request (OBS) and the response (GNOME Portal) aren't on the same page regarding the monitor's refresh state, the video buffer stays empty. Next step: Go back to Screen Capture (PipeWire), click Open Selector, and look for the "Windows" tab in the popup that appears. Does Arc Raiders show up in that list?
