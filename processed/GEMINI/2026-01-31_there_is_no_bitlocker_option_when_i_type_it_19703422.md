---
id: 151169
source: GEMINI
date: 2026-01-31
tags: ['bitlocker', 'windows-11', 'troubleshooting']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan cannot find the BitLocker option in Windows 11 while preparing for Linux installation.
---
# there is no bitlocker option when i type it

### USER
there is no bitlocker option when i type it

### GEMINI
If you don’t see "BitLocker," you likely have Windows 11 Home. On Home editions, Microsoft hides it under a different name: Device Encryption. Even if you’re planning to wipe the drive, leaving this on can sometimes cause the Linux installer to throw a fit because it sees the drive partitions as "locked" or "read-only." 1. Disable "Device Encryption" (The Home Edition way) Open Settings. Go to Privacy & security > Device encryption. Toggle it to Off. Crucial: Wait for it to finish. It will show a decryption progress bar. If you reboot before it’s done, you risk a messy partition table. 2. If it's still missing, use the "Force" method If you can't find that setting either, Windows might have it "pre-provisioned" but not fully active. We'll check the status via the command line to be 100% sure. Right-click the Start button and select Terminal (Admin) or Command Prompt (Admin). Type this command and hit Enter: manage-bde -status Look at "Conversion Status." * If it says "Fully Decrypted," you are good to go. If it says "Used Space Only Encrypted" or "Fully Encrypted," run this command to kill it: manage-bde -off C: 3. The "Full Send" Sanity Check Since you are wiping the whole 2TB drive, here is the absolute truth: If you can't turn it off in Windows, the CachyOS installer can still nuked it, but you have to be aggressive. When you boot into the CachyOS USB: If the installer doesn't see your 2TB drive, it's likely because of RAID/RST mode in your BIOS (change it to AHCI). If the installer sees the drive but won't let you format it, open the terminal in the CachyOS Live environment and type: sudo wipefs -a /dev/nvme0n1 (Replacing nvme0n1 with your actual drive ID). This is the "nuclear option" that wipes all filesystem signatures, including BitLocker, so the installer sees a brand-new blank slate. Ready to jump into the BIOS and flip the Secure Boot/AHCI switches?
