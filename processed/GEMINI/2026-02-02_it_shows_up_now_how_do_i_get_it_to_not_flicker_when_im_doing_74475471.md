---
category: homelab
date: 2026-02-02
id: 608589
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is experiencing display flickering and is seeking a solution to eliminate
  it.
tags:
- display-flickering
- graphics-issue
- linux
- troubleshooting
---
# it shows up now. how do i get it to not flicker when im doing things like that '

### USER
it shows up now. how do i get it to not flicker when im doing things like that '

### GEMINI
Since we’ve established that your hardware and portals are now talking to each other, the lingering flicker is a synchronization and resource war. When you play Arc Raiders while watching a Discord stream and capturing with OBS, your GPU is trying to juggle three different frame-timing demands at once. Here is your prioritized plan to stop the flicker for good. 1. Disable "Hardware Acceleration" inside Discord/Vesktop This is different from the app-level setting you changed earlier. This is for the video engine. Go to Vesktop Settings > Voice & Video. Scroll to the bottom and uncheck "Hardware Acceleration". Why: This stops the GPU from trying to decode the stream you are watching. Shifting this to the CPU prevents "frame collisions" on the GPU buffer, which is the primary cause of flickering during multitask video tasks on Wayland. 2. Kill the VRR Conflict Even if you didn't see the VRR toggle before, the experimental flag you enabled might be trying to "smooth out" the Discord stream's frame rate to match your game's refresh rate. This causes the compositor to "panic" and flicker. Go to Settings > Displays. Select your monitor. Ensure Variable Refresh Rate is set to OFF. The Brutal Truth: You might lose some in-game smoothness, but a steady refresh rate is the only way to get a clean, flicker-free capture on GNOME 49 with an NVIDIA/CachyOS setup. 3. Use "Window Capture" Correct-ly If you are using Screen Capture (PipeWire) for everything, OBS is grabbing the entire desktop. Any stutter in the Discord window or the GNOME shell will show up in your clip. In OBS, add a Window Capture (PipeWire) source. Click Open Selector and select only Arc Raiders. Pro Tip: If the game window is black, try switching the game to "Borderless Window" mode instead of "Exclusive Fullscreen." Wayland loves Borderless; it hates Exclusive. 4. The CachyOS Encode Check If you are encoding your OBS clips using your GPU (NVENC), and you're also watching a stream, you might be hitting the NVENC session limit. In OBS, go to Settings > Output. If you are using NVIDIA NVENC H.264, try switching to FFmpeg VA-API or x264 (CPU) just to see if the flicker stops. If it does, your GPU simply cannot handle the simultaneous render + decode + encode load you're throwing at it. Advisor's Final Priority You've made great progress, but you're pushing a lot of pixels. Your most effective move right now is Step 1 (Discord Video settings) and Step 2 (Turning off VRR). Next step: Turn off the Hardware Acceleration inside the Voice & Video menu specifically. Does that stop the flicker when you play Arc Raiders?
