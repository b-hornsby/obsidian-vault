---
id: 213841
source: GEMINI
date: 2026-02-03
tags: ['nvidia-settings', 'gpu-power', 'performance-tuning']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan ran a command to adjust GPU power settings using nvidia-settings and it seems to have fixed an issue.
---
# running nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" seemed to fix it 

### USER
running nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" seemed to fix it 

### GEMINI
Of course it did. Because while Linux developers want to save every milliwatt of power, NVIDIA’s "Adaptive" mode on Wayland is notoriously bad at realizing OBS needs a stable frame-sync. By forcing "Maximum Performance," you essentially told the GPU, "Stop sleeping on the job," and the flickering vanished. The problem? nvidia-settings commands like that do not persist after a reboot. You'll be back to Flicker-City the next time you turn on your PC. Make it Permanent (The "Autostart" Move) Since you are on GNOME, we can set a hidden "autostart" rule that runs this command every time you log in. This avoids editing scary system files that broke your boot last time. Create the autostart directory (if it doesn't exist): mkdir -p ~/.config/autostart Create a new "Desktop Entry" file: nano ~/.config/autostart/nvidia-performance.desktop Paste this exact block into the file: [Desktop Entry] Type=Application Exec=nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" Hidden=false NoDisplay=false X-GNOME-Autostart-enabled=true Name=NVIDIA Performance Mode Comment=Fixes OBS Flickering on Wayland Save and Exit: Press Ctrl + O, then Enter, then Ctrl + X. Why this is the "Adult" solution It's Safe: If it fails, it just doesn't run. It won't freeze your boot screen like our previous Xorg attempt. It's Specific: It only applies to your user login. It's Automated: You can finally stop typing commands into the terminal every time you want to stream. One Last "Pro" Tip Since you're on a 165Hz monitor, ensure OBS's Canvas Frame Rate (Settings > Video) is set to a divisor of 165 (like 60 or 55) or just keep it at 60. Mismatched refresh rates between your monitor and OBS can sometimes cause a "micro-stutter" that looks like a flicker. Go ahead and reboot your PC now. When you log back in, open OBS. If the flicker is still gone without you typing anything, you have officially conquered the NVIDIA-Wayland beast. Did the fix stick after the reboot?
