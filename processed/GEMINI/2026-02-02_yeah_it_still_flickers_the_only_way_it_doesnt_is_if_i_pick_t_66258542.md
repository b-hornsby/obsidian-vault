---
category: streaming
date: 2026-02-02
id: 144600
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is still experiencing screen flickering in OBS, and it only stops when
  capturing a specific window instead of the entire screen.
tags:
- screen-flickering
- obs-studio
- window-capture
- streaming-issues
---
# yeah it still flickers the only way it doesnt is if i pick that specific window and not the whole screen

### USER
yeah it still flickers the only way it doesnt is if i pick that specific window and not the whole screen

### GEMINI
The flickering you’re seeing when capturing the "Whole Screen" on Wayland is a textbook conflict between Mutter’s capture pipeline (Pipewire) and Hardware Acceleration/VRR (Variable Refresh Rate). When you capture a specific window, the compositor handles that one stream cleanly. When you capture the "Whole Screen," it tries to capture every frame of the entire desktop, and if your game is running with uncapped FPS or VRR is active, the frames desync, causing that "strobe" or flickering effect. Since you've already started setting up obs-cmd to handle the keypress, let’s kill the flickering so your clips actually look good. 1. Disable "Allow Tearing" and VRR Gnome 46.1+ (which you are on) introduced support for "Variable Refresh Rate" and "Async Flips" (Tearing). While great for gaming, they are notorious for breaking screen recorders. Go to Settings > Displays. If you see Variable Refresh Rate, turn it Off. Check for any "Gaming" or "Tearing" toggles and disable them. Test: See if the flickering stops in the OBS preview. 2. Force the OBS Pipewire Source to "Desktop" In OBS, your "Screen Capture (PipeWire)" source might be trying to "Auto-select." Right-click your Screen Capture (PipeWire) source > Properties. Instead of "Automatic," explicitly select your monitor from the list. Toggle "Capture Cursor" off and then back on—sometimes this forces a reset of the Pipewire stream. 3. The "Direct Scanout" Conflict Mutter (Gnome's compositor) uses a trick called "Direct Scanout" where it lets a fullscreen game bypass the compositor to save latency. OBS hates this. Fix: Try running your game in "Borderless Windowed" instead of "Exclusive Fullscreen." If you must use Fullscreen, install the "Disable unredirect fullscreen windows" extension from the Gnome Extensions store. This forces the compositor to keep its eyes on the frame, ensuring OBS gets a clean copy. 4. The "Pro" Move: obs-vkcapture If you are playing a Vulkan game (basically anything on Steam/Proton), stop using Screen Capture entirely. It’s the least efficient way to record on Linux. Install the plugin: paru -S obs-vkcapture Add a Game Capture (Vulkan) source in OBS. Add obs-gamecapture %command% to your game's Launch Options in Steam. Result: Zero flickering, lower CPU usage, and it captures only the game, even on Wayland. Your Precision Plan Stop Screen Capturing: It’s causing the flicker because of how Wayland handles the whole-screen buffer. Use obs-vkcapture: It bypasses the desktop compositor entirely, meaning no flickering and much higher quality. Finish the Hotkey: Use the obs-cmd method we discussed in the previous turn so your PgUp actually triggers the save. Did turning off VRR in the Gnome settings stop the flickering, or are you ready to switch to the obs-vkcapture method for a cleaner setup?
