---
id: 925894
source: GEMINI
date: 2026-01-31
tags: ['cachyos', 'installation', 'drive-partitioning']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is in the CachyOS installer and wants to ensure his entire 2TB drive is used by CachyOS.
---
# I’m here now how do I make sure my whole drive is now cachyos?

### USER
I’m here now how do I make sure my whole drive is now cachyos?

### GEMINI
You have successfully reached the finish line for the Windows era. Your screen shows the 1.82 TiB Samsung 970 EVO Plus correctly identified and currently cluttered with four Windows partitions (EFI, Microsoft Reserved, the main NTFS data, and a Recovery partition). Here is exactly how to execute the "full send" to ensure CachyOS owns every gigabyte of that drive. 1. The Partitioning Choice On the screen you are looking at: Select Erase disk. This is the only option that fulfills your goal. It will delete all those small colored blocks you see in the "Current" bar (the 100 MiB FAT32, the 16 MiB unknown, the 1.82 TiB NTFS, and the 815 MiB NTFS) and replace them with one clean, optimized Linux structure. 2. Configure the New Layout Once you select "Erase disk," a few dropdown menus will appear below it. Set them as follows: Filesystem: Select BTRFS. As your advisor, I’m telling you this is non-negotiable for a high-level setup. It allows you to use "snapshots," meaning if you break a driver tomorrow, you can roll the system back to this exact moment in seconds. Swap: Select Swap to File. Set the size to 16.0 GiB or 32.0 GiB. You have 32GB of RAM and a 2TB drive; giving yourself a healthy swap file ensures the system stays stable under heavy compilation or gaming loads. Encrypt system: Leave this unchecked unless you have a specific reason to want to type a password every single time you turn on the computer. Since you just struggled with BitLocker, you likely want the speed and ease of an unencrypted drive for now. 3. The Final Sanity Check Look at the "After" bar that appears at the bottom of the installer window after you make these selections. It should show: A small EFI partition (usually 512MiB to 1GiB). One massive BTRFS partition taking up the rest of the ~1.82 TiB. 4. Proceed to Desktop Selection Click Next. The installer will then ask which Desktop Environment and Packages you want. Recommendation: Choose KDE Plasma. It is the most robust, fits your high-end hardware perfectly, and offers the best "Wayland" support (which you want for that Samsung NVMe and modern CPU). CachyOS Add-ons: Check the box for CachyOS Gaming if you plan to play Steam/Epic games—it saves you hours of manual setup later. Ready to hit that 'Install' button and make it official? Once you do, there is no going back to Windows without a full reinstall.
