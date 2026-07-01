---
category: streaming
date: 2026-02-03
id: 203521
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting flickering issues in his game capture when using
  OBS Studio with a specific Nvidia setting, even though it fixes OBS flickering.
tags:
- obs-studio
- nvidia
- explicit-sync
- game-capture
- streaming-setup
- troubleshooting
---
# when i launch obs with __NV_DISABLE_EXPLICIT_SYNC=1 obs, obs doesnt flicker but my character in game does and his had is completely black'

### USER
when i launch obs with __NV_DISABLE_EXPLICIT_SYNC=1 obs, obs doesnt flicker but my character in game does and his had is completely black'

### GEMINI
The black head/texture glitch combined with the flickering tells us exactly what's happening: you've moved the "sync" problem from OBS to the game engine itself. By disabling explicit sync, you're preventing OBS from flickering, but now the game (which expects explicit sync on GNOME 49) is delivering "empty" or "late" frames for specific textures, like your character's head. This is a classic "pick your poison" scenario on NVIDIA Wayland. To reach the next level, we need to stop the flickering without breaking the game's rendering. The Precision Fixes 1. The "Native Wayland" Game Launch (Highest Priority) If your game is flickering or showing black textures, it’s likely running through XWayland (the compatibility layer). We need to force it to use native Wayland to match how GNOME 49 wants to handle frames. If it's a Steam/Proton game: Right-click the game in Steam -> Properties -> Launch Options and add: PROTON_ENABLE_WAYLAND=1 %command% Why: This bypasses the X11 bridge where the "Explicit Sync" conflict is happening. Native Wayland apps on the newest NVIDIA drivers rarely flicker. 2. Kill the GSP Firmware (The "Magic Bullet" for 30-series) The RTX 3070 is notorious for flickering on Wayland due to the "GSP Firmware" which tries to manage power and sync on its own. Disabling it forces the driver to handle frames manually, which often fixes the "black texture" and "flickering character" glitch. Open Terminal: sudo nano /etc/modprobe.d/nvidia.conf Add this line: options nvidia NVreg_EnableGpuFirmware=0 Save (Ctrl+O, Enter), Exit (Ctrl+X), and Reboot. 3. Use Screen Capture + Alt-Crop (The OBS Workaround) If Window Capture causes flickering and the DISABLE_EXPLICIT_SYNC command breaks your character, go back to the most stable capture method in Linux: Delete the "Window Capture" source. Add a "Screen Capture (PipeWire)" source. Select your gaming monitor. Hold the Alt key and drag the edges of the box in OBS to crop it down to just your game. Why: Full screen PipeWire captures are prioritized by the compositor and are far less likely to cause the "out of order" frame flickering you're seeing. Strategy & Mindset You are fighting the "bleeding edge." CachyOS and GNOME 49 are pushing features that NVIDIA's drivers haven't 100% stabilized for dual-monitor setups yet. Stop doing this: Launching OBS with __NV_DISABLE_EXPLICIT_SYNC=1. It fixes the preview but breaks the game's rendering, which is a net loss. Do this instead: Disable that GSP Firmware (Step 2 above). Launch your game with PROTON_ENABLE_WAYLAND=1. Use Screen Capture instead of Window Capture. Try the PROTON_ENABLE_WAYLAND=1 launch option first. Does that fix the black character head while you stream?
