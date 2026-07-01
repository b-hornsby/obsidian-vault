---
id: 173805
source: GEMINI
date: 2026-02-02
tags: ['general', 'system-reboot', 'troubleshooting']
category: general
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is reporting that something seems to be working after a reboot, indicating a potential resolution or temporary fix.
---
# it seems to be working after a reboot

### USER
it seems to be working after a reboot

### GEMINI
That reboot likely cleared a hung PipeWire buffer or finalized the Mutter (GNOME's compositor) state after you poked at the hardware acceleration settings. In the world of CachyOS and GNOME 49, a "clean" session is often the only way to get the system portals to stop tripping over themselves. However, since you're running a performance-tuned Arch derivative, "it seems to be working" is usually the calm before the next update breaks it again. Why the reboot actually worked: Portal Reset: GNOME 49 uses xdg-desktop-portal-gnome to handle the screen buffer. If the app crashed or was force-closed during previous attempts, a "ghost" capture session might have been stuck in memory, causing the flickering as two sessions fought for the same screen. Kernel/Mesa Sync: CachyOS updates often push new Mesa (graphics) drivers. If you updated recently without rebooting, you were likely running a mismatched user-space driver and kernel module, which wreaks havoc on Wayland frame-scheduling. Explicit Sync Initialization: GNOME 49 has improved support for Explicit Sync. A fresh boot ensures the GPU and the compositor are starting their handshake from zero rather than trying to recover from a stuttering Electron process. One final "Brutal Truth" check: If you haven't already, run pacman -Qs xdg-desktop-portal one last time. If you see xdg-desktop-portal-wlr or xdg-desktop-portal-kde in that list, remove them. They are the #1 cause of "random" flickering returning after a few days because they occasionally try to hijack the PipeWire stream from the GNOME portal. Advisor's Priority Plan: Don't touch the settings now. If it’s stable, leave it. Monitor the "PipeWire" stream. If it flickers again, don't just reboot—restart the portal specifically: systemctl --user restart xdg-desktop-portal-gnome Check your FPS. If you have a high-refresh monitor, ensure Variable Refresh Rate (VRR) in GNOME settings is set to "Off" during streams, as Electron apps still struggle to sync with fluctuating refresh rates on Wayland. Would you like me to show you how to create a simple script to "reset" your screen-sharing portals if the flicker comes back without needing a full reboot?
