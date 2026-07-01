---
category: streaming
date: 2026-02-02
id: 009642
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing screen flickering in OBS when playing Arc Raiders while
  watching a stream in Discord.
tags:
- obs-studio
- screen-flickering
- discord
- game-streaming
- performance-issues
- arc-raiders
---
# so discord seems to work but when i tried to play arc raiders while watching a stream in discord it flickered in obs

### USER
so discord seems to work but when i tried to play arc raiders while watching a stream in discord it flickered in obs

### GEMINI
This isn't a "Discord" problem anymore; it's a Video Buffer Conflict. When you watch a Discord stream and play Arc Raiders while OBS is capturing, you are creating a "circular" demand on your GPU's video memory. Your GPU is trying to: Decode the incoming Discord stream. Render a heavy Unreal Engine 5 game (Arc Raiders). Encode your screen for OBS. On GNOME 49 Wayland, if these three tasks fight for the same memory buffer, you get flickering. Here is the direct fix for this scenario: 1. The "Observer Effect" Fix (Discord Hardware Acceleration) In your previous steps, you disabled hardware acceleration for rendering Discord, but it might still be using it for decoding incoming video. Go to Vesktop Settings > User Settings > Voice & Video. Scroll to the bottom and Disable "Hardware Acceleration" here as well. Why? This forces your CPU to handle the video you are watching, leaving the GPU entirely free to handle Arc Raiders and OBS. 2. The VRR / G-Sync Conflict Arc Raiders is a high-motion game. If you have a high-refresh monitor, GNOME 49’s Variable Refresh Rate (VRR) will try to match your monitor to your game’s FPS. But the Discord stream you’re watching is likely locked at 30 or 60 FPS. The Result: Your monitor refresh rate is rapidly jumping between 144Hz (game) and 60Hz (stream), causing the "flicker" you see in OBS. The Fix: Go to GNOME Settings > Displays and set Variable Refresh Rate to OFF while you are streaming. 3. OBS Capture Method If you are using "Screen Capture (PipeWire)," OBS is grabbing the entire desktop, including the flickering Discord window. The Fix: Switch your OBS source to Window Capture (PipeWire) and select only Arc Raiders. This isolates the game's frames from the Discord window's frames, preventing the flicker from appearing in your OBS recording/clip. 4. Direct CachyOS Optimization (Explicit Sync) CachyOS is fast, but it can be too fast for its own good. If you have an NVIDIA card, ensure you aren't hitting an "Explicit Sync" bug. Launch Arc Raiders with this launch option in Steam: __GL_GSYNC_ALLOWED=0 __GL_VRR_ALLOWED=0 %command% This forces the game to play nice with the compositor while other video windows are open. The Advisor's Verdict You're trying to do a "pro" multitasking setup on a bleeding-edge Linux build. The flicker is a sync mismatch. By forcing Discord to use your CPU for video decoding (Step 1) and isolating your game in OBS (Step 3), you stop the GPU from getting confused about which frame belongs to which app. Next step: Open Vesktop, disable Hardware Acceleration in Voice & Video, and try watching the stream again while Arc Raiders is in a Windowed/Borderless mode. Does the flicker stop?
