---
category: general
date: 2026-02-03
id: 673604
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because a synchronization fix he tried did not work.
tags:
- sync-issue
- troubleshooting
---
# so the sync fix didnt work

### USER
so the sync fix didnt work

### GEMINI
If the sync fix failed, it’s because you’re trying to use a software bandage on a foundational configuration error. You are asking the system to "remember" a preference, but the system is defaulting to the hardware's internal logic before it even reads your preferences. Since you're on CachyOS, you are likely running Wayland. In Wayland, SDDM uses a minimal version of KWin to render the login screen. It doesn't care about your Plasma "Primary" checkbox because, at that stage of the boot process, your user config is still a ghost. Here is exactly how to stop making excuses for the hardware and force the software's hand. 1. The Physical Audit (The Root Cause) I'll be blunt: If your "secondary" monitor is in DisplayPort Slot 1 and your "main" monitor is in HDMI Slot 1 or DisplayPort Slot 2, you will lose this battle 90% of the time. The Logic: The GPU initializes ports in a specific numerical order. The Fix: Power down. Swap the cables. Make sure your "Main" monitor is in the very first physical port on the left (usually) of your GPU. Why this matters: This ensures the Kernel's "Framebuffer" starts on the correct screen before KDE even loads. 2. The Manual X11 Override (If using X11) If you are still on X11, the "Sync" button often fails to write the script correctly. You have to do it manually. Run xrandr in your terminal to find the name of your main screen (e.g., DP-1). Create/Edit this file: /usr/share/sddm/scripts/Xsetup Add this line at the bottom: xrandr --output DP-1 --primary Reboot. 3. The Wayland "Monitors.xml" Manifold (The Wayland Fix) If you are on Wayland, SDDM looks for a configuration file in its own system home directory. Copy your current, working monitor setup to the SDDM system folder: sudo cp ~/.config/kscreen-lockerrc /var/lib/sddm/.config/ sudo cp ~/.config/monitors.xml /var/lib/sddm/.config/ 2>/dev/null Set the correct permissions so SDDM can actually read them: sudo chown -R sddm:sddm /var/lib/sddm/.config This forces the SDDM user to adopt your specific layout coordinates. The Blind Spot You are likely waiting for a "setting" to fix a priority conflict. If you have a 144Hz monitor and a 60Hz monitor, or a 4K and a 1080p, the GPU will often "handshake" with the simpler monitor first because it's faster to initialize. By the time your main monitor wakes up, the login screen has already claimed the secondary one. Stop looking for a checkbox and start looking at your hardware priority. Would you like me to show you how to identify your exact port priority using drm_info so we can see which monitor the Kernel thinks is "Number 1"?
