---
category: streaming
date: 2026-02-03
id: 414144
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's OBS window capture was working but reverted to flickering, suggesting
  an intermittent or driver-related issue.
tags:
- obs-studio
- flickering
- window-capture
- intermittent-issue
---
# it went back to flickering but it was just working 

### USER
it went back to flickering but it was just working 

### GEMINI
Of course it did. You just witnessed the "XWayland Desync" trap. It worked for a minute because your GPU was at a high power state, but as soon as things settled, the frame timing drifted again, and the flickering returned. Because you are on an NVIDIA 3070 on Wayland, you are dealing with a bug where the browser engine (Chromium) and your GPU can't agree on when to "flip" the frame. Since forcing X11 broke your boot earlier, and the env command is failing you now, we are going to use the Streamer's "Nuclear" Workaround. This is how you stop being a beta tester for Wayland and actually start streaming. 1. The "Zero-Flicker" Capture Method (Do This Now) Stop using the "Browser Source" plugin. It is currently the weakest link in your chain. Open your music overlay (Amuse/Spotify) in a regular browser window (Firefox or Chrome). In OBS, delete the "Browser" source. Add a "Window Capture (PipeWire)" source. Select your browser window. The Pro Trick: Right-click the source -> Filters -> Add "Chroma Key". Use the color picker to select the background of your overlay. Why: Window capture handles frames differently than the internal browser plugin. On Wayland, this is often 100% stable while the browser source flickers like a strobe light. 2. The "Refresh Rate" Sync Your Neofetch showed two monitors (144x2560 and 2560x1440) at 165Hz. The Problem: If one monitor is scaled (1.78x) and the other isn't, GNOME's "Mutter" compositor will flicker your OBS preview as it tries to calculate the math between the two. The Fix: Go to GNOME Settings -> Displays. Set both monitors to 100% scaling (no fractional scaling) just for the test. If the flicker stops, you found your culprit. 3. Disable "Allow Flipping" This is a deep NVIDIA setting that often causes flickering when OBS is trying to record. Open a terminal. Run: nvidia-settings Go to OpenGL Settings. Uncheck "Allow Flipping". Restart OBS. The Advisor's Truth You've spent the last two hours fighting a battle that Linux developers have been fighting for years: NVIDIA Wayland Sync. If you want to stream today, stop trying to make the "Browser Source" work. It is objectively broken for your specific driver/compositor combo. Use Method #1 (Window Capture). It takes 30 seconds to set up, and it doesn't flicker. Are you ready to try the Window Capture + Chroma Key method, or do you want to keep fighting the config files? Would you like me to walk you through the Chroma Key setup for a transparent background?
