---
id: 634815
source: GEMINI
date: 2026-03-15
tags: ['system-installation', 'language-selection', 'boot-process']
category: coding
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is providing context about what he sees after selecting a language during a system installation process.
---
# This is what I see when it loaded after it asked what language

### USER
This is what I see when it loaded after it asked what language

### GEMINI
Look at that list very carefully. You see Disk 0 Unallocated Space (297.4 GB)? That is the target. The Objective Select "Disk 0 Unallocated Space" (the third item in the list). Click "Next" at the bottom right. What NOT to do: Do NOT touch Partition 1 (4.1 GB System). That is your CachyOS bootloader. Do NOT touch Partition 2 (1.5 TB Unknown). That is your entire CachyOS install. Windows says "Unknown" because it doesn't speak "Linux/Btrfs," but that doesn't mean it's empty. Once you click Next on that Unallocated Space, Windows will automatically format it to NTFS and begin the installation. One final piece of advice: During the installation, your PC will reboot several times. It might automatically boot back into the Ventoy USB—if it does, just unplug the USB or change the boot order in the BIOS to the "Windows Boot Manager" to let it finish. Ready to select that 297.4 GB space and hit Next?
