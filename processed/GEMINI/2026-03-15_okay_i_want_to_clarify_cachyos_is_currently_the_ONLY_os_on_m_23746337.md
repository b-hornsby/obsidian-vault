---
id: 265986
source: GEMINI
date: 2026-03-15
tags: ['system-clarification', 'cachyos-only', '2tb-nvme', '120gb-sandisk', 'dual-boot-planning']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified that CachyOS was the only OS on his 2TB NVMe and the 120GB SanDisk SSD was not yet in use, establishing the starting state for the dual-boot project.
---
# okay i want to clarify, cachyos is currently the ONLY os on my 2tb nvme right now and i havent done anything with the 120gb sandisk. it is NOT plugged in or being used at this time 

### USER
okay i want to clarify, cachyos is currently the ONLY os on my 2tb nvme right now and i havent done anything with the 120gb sandisk. it is NOT plugged in or being used at this time 

### GEMINI
Understood. That simplifies things and removes a major variable. Since your 2TB NVMe is currently a "clean slate" with only CachyOS, you are in the best possible position to do this correctly without the 120GB drive causing complications. Here is the objective reality of your situation: Because you already have a Linux environment set up on that 2TB drive, the "dangerous" part isn't the hardware—it's the partition resize. The Execution Strategy 1. The "Safety First" Move Before you touch a single partition bit: Backup your home directory. resizing a partition from the "inside" is a high-risk maneuver. If the power blips or the filesystem has an underlying error, you lose the CachyOS install you've worked so hard to optimize. 2. The Partition Surgery Since CachyOS is the only thing on that drive, it likely occupies the entire 2TB. Do not attempt to shrink the partition while you are logged into CachyOS. It’s like trying to move a rug while you're standing on it. Action: Boot from your CachyOS Live USB (the one you used to install the OS). Tool: Open gparted. Step: Right-click your main 2TB partition and select Resize/Move. Shrink it by 300GB–500GB. This will leave "Unallocated Space" at the end of the NVMe. 3. The Windows "Neighbor" Action: Boot from your Windows/Tiny11 installer. Step: When it asks where to install, pick that Unallocated Space. Result: Windows will create its own NTFS partitions and, crucially, it will see your existing EFI (boot) partition. It will add its own boot files there. 4. The "Peace Treaty" (Bootloader) Once Windows is installed, your PC will likely boot straight into Windows every time. This is Windows being "brutally honest" about its ego—it thinks it's the only OS that matters. The Fix: Boot back into CachyOS (you may need to use your BIOS boot menu, usually F11 or F12 on startup, to manually select the CachyOS entry). The Command: Once inside CachyOS, you need to tell your bootloader to look for its new neighbor. If you're using systemd-boot (Cachy's default): It usually picks up Windows automatically on the next reboot. If you're using GRUB: Run sudo os-prober then sudo update-grub. The Advisor's Final Warning You have a 12700K and an RTX 3070. You are building a high-performance machine. The 120GB SanDisk is officially retired from this project. Do not plug it in. Do not try to "offset" the game installs to it. By keeping both OS environments on the 2TB NVMe, you ensure that Vanguard (Valorant) and Easy Anti-Cheat (Fortnite) are running on the fastest possible bus with the lowest latency. Are you ready to boot into the Live USB and start the gparted resize, or do you want me to double-check your current partition layout first via a terminal command?
