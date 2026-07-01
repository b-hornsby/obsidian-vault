---
id: 315874
source: GEMINI
date: 2026-01-31
tags: ['cachyos', 'installation', 'advanced-tab']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is looking at the advanced tab in the CachyOS installer and asking for guidance.
---
# This is what I see in the advance tab

### USER
This is what I see in the advance tab

### GEMINI
Based on your photos, you are in the exact right spot to finish the "hardware handshake." ASUS boards have a specific flow, so follow this precisely to unlock that 2TB drive for the full send. 1. Kill Secure Boot (Photo 1) As it stands in your photo, Secure Boot state is "User," meaning it's active and guarding the door. Change OS Type from "Windows UEFI mode" to Other OS. If "Secure Boot state" still doesn't say "Disabled" after that, click on Key Management. Inside Key Management, select Clear Secure Boot Keys. Why? This wipes the Microsoft keys from the BIOS memory, forcing the state to "Disabled." CachyOS will now be allowed to boot without a digital signature from Microsoft. 2. The Storage Unlock (Photo 2) In your second photo, you are in the Advanced tab. This is where you prevent the "Drive Not Found" error. Click on PCH Storage Configuration. Look for VMD Setup Menu or Enable VMD controller. Set it to Disabled. The Truth: Intel VMD is great for enterprise RAID, but for a single-drive Linux "full send," it’s a wall. Disabling it exposes the raw 2TB NVMe directly to the CachyOS installer. If you leave this on, the installer will likely see 0 drives. 3. The "Full Send" Launch Go to the Exit tab and select Save Changes & Reset. As it reboots, tap F8 (ASUS Boot Menu key). Select your CachyOS Thumb Drive (it should have "UEFI" in the name). 4. Post-Installation Strategy (The Mirror) You're about to have a 2TB blank slate. When the CachyOS installer asks about partitioning: Don't "Play Small": Use the whole drive. BTRFS is your safety net: Use it. If you mess up a terminal command later, you'll be glad you have snapshots. Are you seeing the VMD option inside "PCH Storage Configuration," or did disabling it cause any weird warnings?
