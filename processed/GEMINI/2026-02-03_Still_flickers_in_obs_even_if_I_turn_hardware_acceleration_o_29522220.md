---
category: streaming
date: 2026-02-03
id: 662962
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was still experiencing flickering in OBS even after turning off hardware
  acceleration.
tags:
- obs-studio
- flickering
- hardware-acceleration
- wayland
---
# Still flickers in obs even if I turn hardware acceleration off

### USER
Still flickers in obs even if I turn hardware acceleration off

### GEMINI
If you’ve turned off hardware acceleration and it’s still flickering, you are hitting the "GSP Firmware" or "Implicit Sync" bug that plagues NVIDIA 30-series cards on Wayland. Basically, your GPU is downclocking or "sleeping" during light tasks (like a music overlay), which causes the browser frames to desync and flicker. Since forcing Xorg broke your boot, we have to fix this from inside Wayland. Here are the three remaining ways to kill the flicker for good: 1. The "Power Management" Fix (Highest Success Rate) NVIDIA's power-saving features often cause this flicker on Wayland. You can force the GPU to stay "awake" while OBS is open. Open a Terminal. Run this command: nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=1" Note: This sets your GPU to "Prefer Maximum Performance." It prevents the card from "stuttering" its clock speeds, which usually stops the Wayland flicker. 2. The "Window Capture" Workaround If the Browser Source is still broken, stop using it. Open your music player or a browser tab with your overlay in it. In OBS, delete the "Browser" source. Add a "Window Capture (PipeWire)" source instead. Select your browser window. The Trick: If it flickers, try running that browser in "Windowed" mode rather than maximized. 3. The "CachyOS Specific" Update CachyOS is rolling-release. If you haven't updated in a few days, you might be missing the 565+ or 570+ drivers that specifically address "Explicit Sync" flickering. Run: sudo pacman -Syu Reboot. Check your driver version with nvidia-smi. If it's 555 or higher, the flicker should be fixable; if it's lower, you're on a broken version for Wayland. The Reality Check You are currently fighting one of the hardest technical battles in Linux: NVIDIA + Wayland + OBS. If the nvidia-settings command above doesn't work, and you don't want to risk the "Xorg switch" again, your only remaining option is to switch to a different compositor (like KDE Plasma 6.2+, which handles NVIDIA sync better than GNOME 49) or use a second monitor that runs at the same refresh rate as your primary, as mismatched Hz can also trigger this. Try the nvidia-settings command now. Does the flicker stop when the GPU is forced into "Maximum Performance" mode?
