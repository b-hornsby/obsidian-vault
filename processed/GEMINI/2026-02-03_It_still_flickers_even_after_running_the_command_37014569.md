---
category: general
date: 2026-02-03
id: 367689
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is still experiencing screen flickering even after trying a suggested
  command.
tags:
- screen-flickering
- troubleshooting
- display-issues
---
# It still flickers even after running the command

### USER
It still flickers even after running the command

### GEMINI
Since the nvidia-settings command didn't kill the flicker and you're stuck on Wayland, we're down to the "ugly" fixes. The flicker is happening because of "Implicit Sync"—your NVIDIA 3070 and the GNOME compositor (Mutter) are trying to draw the browser frame at different times, causing that "stuttering" or flashing effect. Here is the precise, prioritized plan to solve this once and for all: 1. The "XWayland" Force (Highest Success) Often, OBS on Arch/CachyOS tries to run natively on Wayland, which is actually less stable for the Browser Source than running it through the X11 compatibility layer (XWayland). Close OBS. Open your terminal and run this command: QT_QPA_PLATFORM=xcb obs Why this works: This forces OBS to think it's on an X11 system. For many NVIDIA users, this completely eliminates the Browser Source flicker because it uses a more mature (though older) rendering path. 2. The "Window Capture" Pivot If the Browser Source is simply refused to behave, stop using it. You are wasting time on a broken plugin. Open your music overlay in a standalone browser window (like Firefox or Chrome). In OBS, add a "Window Capture (PipeWire)" source. The Key: Right-click the Source in OBS -> Filters -> Add a "Chroma Key" or "Color Key" to remove the background of the browser window. Note: This is how pros did it for years before Browser Sources were stable. It’s a 100% flicker-free method. 3. Disable the GSP Firmware (The "CachyOS" Special) NVIDIA's recent drivers (555+) use a new "GSP Firmware" that is known to cause micro-stutters and flickers on Wayland. Open Terminal. Run: sudo nano /etc/modprobe.d/nvidia.conf Add this line to the file: options nvidia NVreg_EnableGpuFirmware=0 Save (Ctrl+O, Enter), Exit (Ctrl+X), and Reboot. The Reality Check You’ve been troubleshooting for a while. If QT_QPA_PLATFORM=xcb obs doesn't fix the flicker in the next 60 seconds, stop trying to fix the Browser Source. It is a known bug in the interaction between Chromium, Wayland, and NVIDIA. Your fastest path to streaming right now: Use the Window Capture (PipeWire) method mentioned in Step 2. It bypasses the Chromium bug entirely. Does forcing OBS to run with QT_QPA_PLATFORM=xcb stop the flashing?
