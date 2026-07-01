---
id: 594297
source: GEMINI
date: 2026-02-03
tags: ['obs-studio', 'qt-platform', 'xcb', 'wayland-fix']
category: streaming
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan fixed his OBS issue by running it with the QT_QPA_PLATFORM=xcb environment variable to force X11 instead of Wayland.
---
# When I ran QT_QPA_PLATFORM=xcb obs
It’s working now

### USER
When I ran QT_QPA_PLATFORM=xcb obs
It’s working now

### GEMINI
That command worked because it forced OBS to run via XWayland (the X11 compatibility layer) instead of natively on Wayland. Since NVIDIA’s drivers have decades of stability with X11, the "Browser Source" stopped arguing with your GPU about frame timing, and the flickering died. Now, don't just run that command every time you want to stream. Let's make it permanent so you can just click the OBS icon and go. Make the Fix Permanent (The "CachyOS" Way) Instead of editing the system file (which gets overwritten when you update), we’ll create a local "override" for your user. Open your terminal and copy-paste this command to copy the OBS launcher to your local folder: cp /usr/share/applications/com.obsproject.Studio.desktop ~/.local/share/applications/ Edit your local copy: nano ~/.local/share/applications/com.obsproject.Studio.desktop Find the line that starts with Exec=. It probably just says Exec=obs. Change it to exactly this: Exec=env QT_QPA_PLATFORM=xcb obs Save and Exit: Press Ctrl + O, then Enter, then Ctrl + X. Why this is the "Pro" Move: Update-Proof: When CachyOS updates OBS next week, your custom launcher won't be deleted. Clean: You aren't forcing your entire computer to use X11 (which we saw broke your boot earlier); you are only forcing OBS to use it. Stability: You get the performance of Wayland for your desktop and the stability of X11 for your stream. The Final Step for your Music Overlay Now that OBS is stable: Close your current OBS session. Launch OBS normally from your app menu. Add your Browser Source (Amuse, Pixel Chat, etc.). Important: Since you are now in "X11 mode" inside OBS, you can actually keep Hardware Acceleration ON for better performance unless it starts acting up again. Does the OBS icon in your menu now launch the flicker-free version automatically? Once that's confirmed, you're officially ready to set up your scenes and go live.
