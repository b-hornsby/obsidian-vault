---
id: 032875
source: GEMINI
date: 2026-01-31
tags: ['cachyos', 'installation', 'erase-disk']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan selected 'erase disk' in the CachyOS installer and is asking what to do next.
---
# Picked erase disk. Now what?

### USER
Picked erase disk. Now what?

### GEMINI
You have officially committed. By selecting Erase disk, the "After" bar shows exactly what you want: the old Windows clutter is replaced by a massive 1.82 TiB Btrfs partition. Here is how you finish the job: 1. Finalize the Partition Settings Filesystem: You have btrfs selected in the dropdown—keep it there. It's the superior choice for your hardware. Swap: You don't see the swap option in the "After" bar yet. Look for a dropdown or checkbox for Swap to File (likely below the filesystem choice) and set it to at least 16GB. Bootloader: Click Next. When it asks about the bootloader, ensure systemd-boot is selected. It’s leaner and faster than the old-school GRUB. 2. Desktop & Package Selection (The Next Screens) After you click Next, you'll reach the "Desktop" and "Packages" tabs: The Desktop: Select KDE Plasma. It’s the most powerful, highly customizable, and will make the best use of your 32GB of RAM and high-frequency CPU. The Kernel: Choose the default CachyOS Kernel. It’s pre-tuned for the kind of low-latency performance Windows 11 couldn't give you. Extras: Check the box for CachyOS Gaming and NVIDIA drivers (if you have an NVIDIA card). 3. User Setup Pick a username and a strong password. Check the box to "Use the same password for the administrator account." It makes life easier when you're running sudo commands later. 4. The "Full Send" Warning When you hit the final Install button on the "Summary" page, the installer will format your Samsung 970 EVO Plus. Any data left on that drive will be vaporized. Ready to hit Next and pick your Desktop environment?
