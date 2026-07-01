---
category: streaming
date: 2026-02-03
id: 722480
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's OBS window capture still flickers even after removing the browser
  source, indicating a deeper issue.
tags:
- obs-studio
- window-capture
- flickering
- gaming
- troubleshooting
---
# it still flickers even without the browser source '

### USER
it still flickers even without the browser source '

### GEMINI
If it is still flickering after you deleted the Browser Source, you aren't just fighting a plugin—you’re fighting GNOME’s Adaptive Sync (VRR) and your dual-monitor setup. Your Neofetch shows two monitors at 165Hz, one with scaling and one without. On NVIDIA Wayland, if your GPU doesn't have a "heavy" enough task, it tries to save power by lowering its clock speed. This causes the entire OBS preview window to "strobe" or flicker as it fails to sync with your high refresh rate monitors. The 3-Step "Final" Fix 1. Kill Adaptive Sync (VRR) — The Likely Culprit This is the #1 cause of "whole window" flickering on NVIDIA/Wayland. Open GNOME Settings. Go to Displays. Select your main monitor. Look for Variable Refresh Rate or Adaptive Sync. Set it to Off. (Do this for both monitors). 2. The "NVIDIA GSP" Nuclear Option CachyOS uses the "Open" NVIDIA modules by default, which use a new firmware (GSP) that is notoriously buggy with 30-series cards and high-refresh monitors. Open your terminal. Run: sudo nano /etc/modprobe.d/nvidia.conf Add this line: options nvidia NVreg_EnableGpuFirmware=0 Save (Ctrl+O, Enter) and Exit (Ctrl+X). Reboot. 3. Match Your Refresh Rates If one monitor is even slightly different (e.g., 165Hz vs 144Hz or 60Hz), the Wayland compositor will flicker the OBS window as it tries to reconcile the two. Go back to Displays. Force both monitors to a static 60Hz just to test. If the flickering stops, you know it's a "Refresh Rate Mismatch" bug. You can then try raising them both to 120Hz or 144Hz together. The Advisor's Brutal Truth You are being punished for having a high-end setup (RTX 3070 + dual 165Hz monitors) on a desktop environment (GNOME Wayland) that is still "learning" how to talk to NVIDIA cards properly. If you turn off Adaptive Sync in your GNOME settings and it still flickers, your hardware is literally too fast for the current Wayland drivers to handle stably while OBS is open. Go to Settings -> Displays right now. Is "Variable Refresh Rate" turned on? If so, turn it off and tell me if the strobe effect stops.
