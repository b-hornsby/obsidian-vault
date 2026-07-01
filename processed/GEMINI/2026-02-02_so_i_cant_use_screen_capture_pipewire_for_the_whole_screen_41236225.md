---
category: streaming
date: 2026-02-02
id: 506895
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is questioning whether he can use PipeWire to capture the entire screen
  in OBS.
tags:
- obs-studio
- pipewire
- screen-capture
- linux
- streaming-setup
---
# so i cant use screen capture pipewire for the whole screen?

### USER
so i cant use screen capture pipewire for the whole screen?

### GEMINI
You absolutely can use "Screen Capture (PipeWire)" for the whole screen, but you have to understand why it’s flickering now: GNOME 49 + NVIDIA + VRR is currently a "flicker triangle" on Wayland. When you capture the whole screen, the compositor (Mutter) is trying to sync the 144Hz+ game you're playing with the 30/60FPS video you're watching in Discord. If Variable Refresh Rate (VRR) is on, your monitor is constantly jumping its refresh rate to match the game, while the Discord window is trying to hold a steady, lower frame rate. This "sync war" results in the flickering or "old frames" popping up in the recording. The Direct Fixes for Full Screen Capture: 1. Kill the VRR Flicker (Most Likely) GNOME 49 enables VRR by default for many monitors. If it’s on "Automatic" or "Always," it will flicker during screen sharing if any window on that screen is running at a different frame rate than the others. Go to GNOME Settings > Displays. Select your monitor. Set Variable Refresh Rate to OFF. The Reality: You lose the smooth G-Sync/FreeSync feel in-game, but your full-screen capture will be rock solid. 2. The NVIDIA "Explicit Sync" Toggle Since you're on CachyOS with an NVIDIA card, you are likely using the 555+ series drivers. These support Explicit Sync, which should stop flickering, but Electron apps (Discord/Vesktop) still struggle with it. Try launching OBS with this environment variable to see if it stabilizes the PipeWire stream: OBS_USE_EGL=1 obs If that doesn't work, try the "Safety First" launch: __GL_GSYNC_ALLOWED=0 __GL_VRR_ALLOWED=0 obs 3. Discord's "Overlay" and "Hardware Acceleration" If you are watching a stream in Discord while capturing the screen, Discord is fighting for the same GPU "slots" as OBS. In Discord/Vesktop: Go to User Settings > Voice & Video. Turn OFF "Hardware Acceleration" at the very bottom. Why? This stops Discord from using the GPU to decode the video you're watching. It shifts that load to your CPU, which prevents the GPU from getting "confused" about which frame belongs to the game and which belongs to the stream during a full-screen capture. The Advisor's Verdict You're trying to do a high-bandwidth task (Full Screen Capture) while multitasking video (Discord Stream) and playing a heavy game (Arc Raiders). On Linux, Screen Capture (PipeWire) is a "brute force" method—it copies every single pixel on the screen. Window Capture is "surgical"—it only grabs the game's frames. If you insist on Full Screen Capture: Turn off VRR in GNOME settings. Disable Hardware Acceleration inside Discord's Video settings. Reboot. (Always reboot after changing VRR or major GPU settings on CachyOS). Would you like me to show you how to check your nvidia-smi output while gaming to see if you're actually hitting your GPU's limit?
