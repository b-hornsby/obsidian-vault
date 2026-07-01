---
id: 758823
source: GEMINI
date: 2026-02-03
tags: ['nvidia-smi', 'gsp-firmware', 'gpu-information']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the GSP Firmware version using nvidia-smi, and it's reporting N/A, likely indicating a problem.
---
# ❯ nvidia-smi -q | grep "GSP Firmware"
    GSP Firmware Version                               : N/A

~
❯ 

### USER
❯ nvidia-smi -q | grep "GSP Firmware"
    GSP Firmware Version                               : N/A

~
❯ 

### GEMINI
Getting GSP Firmware Version: N/A is a massive win. You have successfully bypassed the "black box" firmware that causes most of the stuttering on modern NVIDIA/Wayland setups. If you still see a flicker, you are no longer fighting a bug; you are fighting Sync Timing. Your RTX 3070 is currently trying to output frames to two 165Hz monitors while Wayland tries to calculate its own refresh rate. This "math" often misses by a millisecond, creating a flicker. The "Pro" Finish (3 Final Steps) 1. The "Power Lock" (Most Effective) Since the GPU isn't using GSP, it might be dropping its clock speed too low to save power, which causes "sync misses." Force it to stay awake: Run this command and leave the terminal open (or minimize it): nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" If that doesn't work, run this "Hard Lock" (sets clock to 1500MHz): sudo nvidia-smi -lgc 1500,2100 2. Kill "Allow Flipping" This is a legacy NVIDIA setting that often interferes with how OBS captures windows on Linux. Open NVIDIA Settings (the app). Go to OpenGL Settings. Uncheck "Allow Flipping". 3. The Monitor Alignment Dual 165Hz monitors on Wayland are notorious for flickering if they aren't perfectly matched. Go to Settings > Displays. Ensure Variable Refresh Rate (VRR) is OFF for both. The Test: Set both monitors to 144Hz instead of 165Hz. (144 is a more standard "division" for many Linux compositors and often fixes the strobe effect instantly). The Brutal Advisor's Truth You have done the hard part. You’ve reconfigured the kernel, swapped drivers, and disabled the firmware. You are now in the "fine-tuning" phase. If you do the Power Lock (Step 1) and the 144Hz Match (Step 3), and it still flickers, your specific GNOME version (Mutter) is failing to handle the RTX 3070's output correctly on Wayland. At that point, your only "brutally honest" option is to use KDE Plasma (which handles NVIDIA Wayland much better) or use the Window Capture (PipeWire) method I mentioned earlier, which is technically immune to the browser-source flicker. Try Step 3 (144Hz + VRR Off) right now. Does the flicker stop the moment you drop the refresh rate?
