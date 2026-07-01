---
id: 236875
source: GEMINI
date: 2026-02-03
tags: ['nvidia', 'gpu-clocks', 'overclocking', 'nvidia-smi', 'cachyos']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan successfully set NVIDIA GPU clock speeds on CachyOS using nvidia-smi.
---
# [sudo] password for toastedmel0n: 
GPU clocks set to "(gpuClkMin 1500, gpuClkMax 2100)" for GPU 00000000:01:00.0

Warning: persistence mode is disabled on device 00000000:01:00.0. See the Known Issues section of the nvidia-smi(1) man page for more information. Run with [--help | -h] switch to get more information on how to enable persistence mode.
All done.

~ 12s
❯ 

### USER
[sudo] password for toastedmel0n: 
GPU clocks set to "(gpuClkMin 1500, gpuClkMax 2100)" for GPU 00000000:01:00.0

Warning: persistence mode is disabled on device 00000000:01:00.0. See the Known Issues section of the nvidia-smi(1) man page for more information. Run with [--help | -h] switch to get more information on how to enable persistence mode.
All done.

~ 12s
❯ 

### GEMINI
That warning is expected. Persistence Mode is the feature that keeps the NVIDIA driver "alive" and prevents it from resetting your clock speed every time an app closes. Because you have it disabled, your lgc 1500,2100 command (locking the clocks) might only last for a split second before the driver "naps" and resets them to zero, bringing the flickering back. The 2-Step "Permanent" Fix 1. Enable Persistence Mode (The Service) Don't just run a command; enable the system service so it stays on forever. Run this in your terminal: sudo systemctl enable --now nvidia-persistenced.service Verify it's on: nvidia-smi Look at the top right. It should now say Persistence-M: On. 2. Re-Lock the Clocks Now that the driver is "persistent," your clock lock will actually stick. Run the lock command again: sudo nvidia-smi -lgc 1500,2100 Why this works: By holding the clock at 1500MHz, you prevent the 3070 from dropping into its "P8" (ultra-low power) state. On Wayland, that P8 state is the #1 cause of frame-sync flickering in OBS. The Result With GSP: N/A (which you did earlier) and Persistence: On with Locked Clocks, you have effectively forced your NVIDIA card to behave like a standard, high-performance video device rather than a power-saving mobile chip. Open OBS now. If the "Now Playing" overlay still flickers, it is 100% a Refresh Rate Mismatch. Go to GNOME Settings > Displays. Set both monitors to 144Hz (or 120Hz). Turn OFF Variable Refresh Rate (VRR). Does nvidia-smi show "Persistence-M: On" now? If it does, and you've locked the clocks, your OBS preview should finally be as stable as a rock.
