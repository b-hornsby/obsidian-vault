---
id: 109614
source: GEMINI
date: 2026-02-03
tags: ['homelab', 'ai', 'gemini', 'go', 'terminal', 'at', 'cachyos', 'hardware']
category: homelab
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
---
# Deleted the # part and rebooted and got this

### USER
Deleted the # part and rebooted and got this

### GEMINI
This is the "Hold until boot process finishes up" freeze, a common issue on CachyOS when GDM (Gnome Display Manager) conflicts with NVIDIA drivers during the transition to Xorg. By disabling Wayland, you forced the system to use a display path it's currently failing to initialize. Don't panic. We can fix this through a Virtual Terminal (TTY) and revert the change to get your desktop back. Step 1: Access the Terminal (TTY) On the frozen screen (the one in your second photo), press Ctrl + Alt + F3 (or F4/F5). A black screen with a login prompt should appear. Type your username (Bryan) and your password. Step 2: Revert the Configuration Change Now, we need to add that # back to the file so Wayland can start again: Type: sudo nano /etc/gdm/custom.conf Find the line: WaylandEnable=false Change it back to: #WaylandEnable=false Press Ctrl + O, then Enter to save. Press Ctrl + X to exit. Step 3: Reboot and Return to Desktop Type: sudo reboot. Your system should now boot back into the GNOME login screen you saw originally. Why the "Fix" failed CachyOS uses a specific "Btrfs-overlayfs" or "Limine" boot setup that can occasionally break if GDM is forced away from its default Wayland configuration, especially on NVIDIA cards. The Strategy for your Music Overlay: Once you are back in GNOME, do not try to force Xorg again. Instead, we will fix the flickering within Wayland as previously discussed: Open OBS. Go to Settings > Advanced. Uncheck "Enable Browser Source Hardware Acceleration". Can you get into the TTY screen by pressing Ctrl + Alt + F3? If not, you may need to use your bootloader (Limine/GRUB) to select an earlier "Snapshot" to restore your system.