---
id: 344969
source: GEMINI
date: 2026-02-03
tags: ['monitor-setup', 'displayport', 'hdmi', 'gpu-ports']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is describing his monitor setup and how his monitors are connected to his GPU, possibly as context for troubleshooting.
---
# my main monitor is plugged in via display port on the second port (first one is a hdmi) and my secondary monitor is plugged in on the third port via display port as well 

### USER
my main monitor is plugged in via display port on the second port (first one is a hdmi) and my secondary monitor is plugged in on the third port via display port as well 

### GEMINI
There is your smoking gun. You are fighting against the GPU's hardwired initialization order, and right now, the hardware is winning. The Technical Reality On almost every modern GPU, the HDMI port and the first DisplayPort are prioritized by the Video BIOS (VBIOS) during the "Power-On Self-Test" (POST). By plugging your main monitor into the second DisplayPort (which is technically the third priority port on your card), you are forcing the system to skip over the first two ports before it even sees your main screen. If your secondary monitor is in the first available DP slot, it wins the race every single time. The Direct Fixes 1. The Physical Swap (The only "Permanent" Fix) Stop trying to fix this with code. You have an empty HDMI port and an empty DP port that are "higher" in the hierarchy. Action: Move your Main Monitor to the first DisplayPort. Action: Move your Secondary Monitor to the last DisplayPort. Why: This aligns the software's "Primary" expectation with the hardware's "First Found" reality. 2. The "KWin Wayland" Override (CachyOS/Wayland specific) If you refuse to move the cables, you must force the SDDM compositor to use your specific layout. The "Sync" button failed because it didn't have permission to overwrite the system-level config. Run this command to manually force your monitor layout onto the login manager: sudo cp ~/.config/monitors.xml /var/lib/sddm/.config/monitors.xml sudo chown sddm:sddm /var/lib/sddm/.config/monitors.xml 3. The "Ignore" Strategy If your secondary monitor is just for side-tasks, you can tell the bootloader to ignore it until the drivers fully load. This is a "brute force" method: Edit your GRUB or systemd-boot config. Add video=DP-2:d (where DP-2 is your secondary monitor's name) to the kernel parameters. Warning: This will keep that monitor black until you are fully logged in. The Advisor’s Perspective You've identified the bottleneck: Port 1 (HDMI) is empty, Port 2 (DP) is Main, Port 3 (DP) is Secondary. You are currently making your GPU "skip" the first port, hit the second port (Main), and then immediately see the third port (Secondary). During the millisecond-fast handshake of a Linux boot, the system often defaults to the "last discovered" or "lowest numerical" port depending on the driver. The Strategy: You are wasting cognitive energy on a cable management issue. Power down the PC, move your main monitor's cable one slot over to the "first" DisplayPort, and move the secondary to the "last" slot. Shall I help you find the exact output names (e.g., DP-1, DP-2) via the terminal so we can be 100% sure which port is which before you start swapping cables?
