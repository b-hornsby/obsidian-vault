---
category: streaming
date: 2026-02-03
id: 931952
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is troubleshooting a flickering issue with window capture in OBS Studio,
  specifically stating it's not related to the music overlay.
tags:
- obs-studio
- streaming
- window-capture
- flickering-issue
---
# its not my music overlay that flickers its the window capture 

### USER
its not my music overlay that flickers its the window capture 

### GEMINI
That changes everything. If your Window Capture is flickering, you are hitting the "Implicit Sync" bug where NVIDIA’s drivers and the Wayland compositor (Mutter) are literally fighting over which frame to show first. It looks like the window is jumping back and forth in time. Since we already know forcing Xorg breaks your boot, we have to fix this within Wayland using one of these three specific maneuvers. 1. The "XWayland" Force (Highest Success Rate) Many windows flicker because they are running as X11 apps inside Wayland. The Fix: If the app you are trying to capture is a browser (like Chrome or Discord), you need to force it to run natively on Wayland. For Chrome/Edge/Brave: Launch it with these flags: --enable-features=UseOzonePlatform --ozone-platform=wayland Why: This stops the app from using the "Xwayland" bridge, which is where 90% of the flickering happens. 2. The "GSP Firmware" Kill (The Real Fix) On NVIDIA 30-series cards like yours, a new "GSP" firmware feature is often the culprit for capture stutters. Disabling it is a common fix for CachyOS users. Open Terminal: sudo nano /etc/modprobe.d/nvidia.conf Add this line: options nvidia NVreg_EnableGpuFirmware=0 Save/Exit: (Ctrl+O, Enter, Ctrl+X) and Reboot. This forces the driver to handle the frames manually rather than letting the buggy firmware do it. 3. The "Desktop Capture" Pivot If a specific window flickers but the whole screen doesn't, stop using Window Capture. The Fix: Add a Screen Capture (PipeWire) instead of a Window Capture. The Adjustment: Use the "Crop" filter in OBS (Hold Alt and drag the red corners) to trim the screen capture down so it only shows the window you want. Why: Full-screen PipeWire streams are often prioritized by the compositor and tend to flicker less than individual window streams. The Brutal Truth You are using a GNOME version (49) that is very new, and an NVIDIA driver that is still perfecting "Explicit Sync." My prioritized move for you: Try the Screen Capture (PipeWire) + Alt-Crop method. It's the "dumb" solution that almost always works when the "smart" window capture fails. If that still flickers, run the GSP Firmware terminal command in Step 2. Does capturing the entire screen and cropping it down stop the flickering for you?
