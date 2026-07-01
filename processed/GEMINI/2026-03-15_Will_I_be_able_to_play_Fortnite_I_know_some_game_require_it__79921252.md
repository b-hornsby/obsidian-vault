---
category: coding
date: 2026-03-15
id: 653186
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is concerned about whether he'll be able to play Fortnite, knowing
  its anti-cheat requirements, and is looking for the best solution (likely dual-booting).
tags:
- gaming-on-linux
- fortnite
- anti-cheat
- dual-boot-requirement
- proton-compatibility
---
# Will I be able to play Fortnite? I know some game require it so I need the best solution here

### USER
Will I be able to play Fortnite? I know some game require it so I need the best solution here

### GEMINI
Turning Secure Boot on is the ultimate "it depends" situation. Here is the direct truth for your specific setup in 2026: 1. The Fortnite Reality Check On Linux (CachyOS): You cannot play Fortnite. Epic Games still explicitly blocks Linux. No amount of Secure Boot tinkering will change this because their anti-cheat (EAC) simply refuses to run on Linux. On Windows (Tiny11): You can play Fortnite. Casual Play: Currently, you do not need Secure Boot enabled for regular Battle Royale or Creative modes. Competitive/Tournaments: As of February 2026, Epic now requires Secure Boot, TPM 2.0, and IOMMU for all competitive tournaments. 2. Will turning it on "ruin" your setup? Yes, it likely will. If you simply flip the "Secure Boot" switch in your ASUS BIOS right now, the Minecraft menu (GRUB) will almost certainly fail to load with a "Security Violation" error. This is because you haven't "signed" the Linux bootloader to tell the BIOS it’s safe. The Best Solution (The "Middle Ground") Since you are dual-booting Tiny11 and CachyOS on one drive, here is the most stable path: Step 1: Keep Secure Boot OFF for now. Test Fortnite in Windows. If it launches and lets you into a match, leave everything exactly as it is. You don't need Secure Boot, and your Minecraft menu stays safe. Step 2: If Fortnite (or Valorant) refuses to launch: If you get an error saying "Secure Boot is required," you have to decide if the game is worth the extra work. To make them coexist, you’ll need to use a tool called sbctl inside CachyOS to "enroll" your own keys. If you ever reach that point, here is the "Quick Save" to get back to Linux: Go into BIOS. Set Secure Boot to "Other OS" or "Disabled." Your Minecraft menu will immediately start working again. My Recommendation Don't touch the Secure Boot setting yet. Boot into your Windows "World," install Fortnite, and try to play. Most casual players are currently unaffected by the new 2026 security mandates. Would you like me to help you test if Windows sees your TPM and IOMMU correctly so you're ready just in case?
