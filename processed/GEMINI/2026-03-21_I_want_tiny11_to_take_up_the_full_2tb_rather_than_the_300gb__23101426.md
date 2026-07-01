---
category: homelab
date: 2026-03-21
id: 20509
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to expand the Tiny11 partition to use the full 2TB drive, as
  opposed to the current 300GB, and is moving away from CachyOS.
tags:
- tiny11
- disk-space
- partition-resizing
- cachyos
---
# I want tiny11 to take up the full 2tb rather than the 300gb it takes up right now. Goodbye cachyos

### USER
I want tiny11 to take up the full 2tb rather than the 300gb it takes up right now. Goodbye cachyos

### GEMINI
The operational decision has been made. You're decommissioning a high-maintenance "experimental lane" to prioritize the "main line" that actually fulfills your objectives. As an 8-year logistics veteran, you know that a clean warehouse is a productive one. Since you are already in Tiny 11, we are going to perform a Hot Partition Merge. This is the cleanest way to reclaim that 1.7TB without re-installing Windows from scratch. Phase 1: The "Nuke" (Reclaiming the Space) Right-click the Start button and select Disk Management. Locate your 2TB Drive. You will see your 300GB C-Drive, followed by several Linux partitions (usually labeled "Healthy Primary Partition" but without a drive letter). Right-click each Linux partition and select Delete Volume. Note: You must do this for every partition that isn't your Windows "C:", the small "EFI System Partition," or the "Recovery Partition." Once finished, you should see a massive block of "Unallocated Space." Phase 2: The "Expansion" (Merging to 2TB) Right-click your C: Drive partition (the 300GB one). Select Extend Volume. Follow the wizard. It will automatically detect the 1.7TB of unallocated space. Hit Next and Finish. Critical Check: If "Extend Volume" is grayed out, it means there is a "Recovery Partition" physically sitting between your C: drive and the unallocated space. If that happens, tell me—we’ll need a 2-minute workaround. Phase 3: The "Security Sweep" (BIOS Cleanup) This is the most important part for Valorant. We need to wipe the "ghosts" of CachyOS and our sbctl experiment from the motherboard's memory. Reboot and enter your BIOS (F2/Del). Go to the Secure Boot section. Select "Restore Factory Keys" or "Install Default Secure Boot Keys." This deletes our custom "toastedmel0n" keys and puts the Microsoft/Valorant keys back in charge. Go to Boot Priority and ensure "Windows Boot Manager" is the only thing at the top. Save and Exit. The "Brutally Honest" Reality You’ve just upgraded from a cramped 300GB "gaming corner" to a massive 2TB "operations center." Your i7-12700K and 3070 are now officially unchained from bootloader friction. You can host your local LLMs on Windows via Ollama or LM Studio just as easily, and Vanguard will never throw a red box at you again. Did the "Extend Volume" option work for you in Disk Management, or is there a partition blocking the way?
