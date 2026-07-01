---
id: 747181
source: GEMINI
date: 2026-02-03
tags: ['monitor-setup', 'refresh-rate', 'display-config', 'dual-monitor']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified his dual-monitor refresh rate configuration, likely in context of a display or gaming setup discussion.
---
# they are both 165hz just the 27 in has variable refresh rate 

### USER
they are both 165hz just the 27 in has variable refresh rate 

### GEMINI
That 27" monitor is the "traitor" in your setup. The flickering is happening because your Variable Refresh Rate (VRR/G-Sync) is enabled on the 27" monitor but not on the 32". When you play a game, the 27" monitor constantly shifts its refresh rate to match your FPS (e.g., jumping between 80Hz and 165Hz). Meanwhile, OBS is trying to capture at a static 60 FPS. On NVIDIA Wayland, this mismatch causes the "Implicit Sync" bug, which manifests as that strobe-light flickering in your capture. The "Surgical" Fix: Kill VRR on the Desktop You don't need VRR while you're just sitting on the desktop or managing OBS; you only need it for the game itself. GNOME 49 has a specific setting to fix this conflict. Open GNOME Settings. Go to Displays. Select your 27" monitor. Look for Variable Refresh Rate. Change it to "Off" or "Never." * Alternative: If you have an "Only for Fullscreen" option, select that. Restart OBS. The "Nuclear" Option (If Settings doesn't work) If the GUI doesn't let you disable it, you can force NVIDIA to stop using VRR via the terminal. This is safer than the Xorg switch that broke your boot. Open Terminal. Run this command: nvidia-settings -a AllowVRR=0 Test OBS. If the flickering stops, your VRR was definitely the culprit. Why this happens to you specifically You have an RTX 3070. This card uses "Implicit Sync" by default on older setups, but CachyOS is pushing "Explicit Sync." When you have two monitors at 165Hz but only one is varying its speed (VRR), the GPU driver gets "confused" about which timing clock to use for the OBS preview window. It's essentially trying to draw two different reality-speeds at the same time. The Strategy: Disable VRR in your GNOME Display settings for the 27" monitor. Launch OBS using the command I gave you earlier: __NV_DISABLE_EXPLICIT_SYNC=1 obs. Once you turn off Variable Refresh Rate in the Windows/Display settings, does the OBS window capture finally stabilize?
