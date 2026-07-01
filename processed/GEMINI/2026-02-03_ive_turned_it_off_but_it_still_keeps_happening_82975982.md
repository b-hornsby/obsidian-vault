---
category: general
date: 2026-02-03
id: 573456
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because something he turned off is still happening, but
  the context is missing.
tags:
- troubleshooting
- unspecified-issue
---
# ive turned it off but it still keeps happening 

### USER
ive turned it off but it still keeps happening 

### GEMINI
Turning off VRR was a logical step, but on your NVIDIA 3070 and GNOME 49 setup, the flickering is often a deep "sync" issue where the GPU driver and the Wayland compositor fail to communicate correctly when multiple refresh-heavy tasks are happening simultaneously. Since the GUI setting didn't cut it, you need to use these brutally direct technical workarounds. 1. Force the "Max Performance" Power State NVIDIA cards on Wayland often flicker because they aggressively try to save power, causing the clock speeds to fluctuate during a capture. This command forces the card to stay at full power. Run this in your terminal: nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" Why this helps: It prevents the card from "sleeping" while OBS is trying to grab frames, which is a leading cause of capture strobing. 2. The "Explicit Sync" Kill-Switch (Most Effective for GNOME 49) GNOME 49 uses "Explicit Sync" by default, which is currently causing major flickering issues for some NVIDIA users. You can bypass this by launching OBS with a specific instruction. Close OBS completely. Launch it using this exact command: __NV_DISABLE_EXPLICIT_SYNC=1 obs The Result: If the flickering stops, your driver’s new sync protocol is the culprit. You can make this permanent by adding that line to your ~/.config/fish/config.fish file. 3. Disable "Allow Flipping" This is an old-school Linux trick that still works for dual-monitor flickering on NVIDIA. Open NVIDIA Settings. Go to OpenGL Settings. Uncheck "Allow Flipping". Note: If you don't see this option in the GUI on Wayland, you may need to use the terminal command: nvidia-settings -a AllowOpenGLVideoFlipping=0. The "Strategic Pivot" If you have tried all of these and the Window Capture still flickers while you're gaming: Stop using Window Capture. * Use Screen Capture (PipeWire) instead. Capture your entire 27" monitor. Use the Alt-Crop method (hold Alt and drag the borders in OBS) to cut the capture down to just the game window. Did launching OBS with the __NV_DISABLE_EXPLICIT_SYNC=1 command change the flickering behavior at all?
