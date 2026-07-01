---
category: coding
date: 2026-03-15
id: 101665
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if enabling Secure Boot will cause problems with his current
  system configuration, likely related to dual-booting.
tags:
- secure-boot
- dual-boot-compatibility
- system-configuration
---
# Will turning secure boot on ruin any of this?

### USER
Will turning secure boot on ruin any of this?

### GEMINI
Turning Secure Boot on is the final boss of Linux dual-booting. Whether it "ruins" things depends entirely on how CachyOS was set up, but on an ASUS board, it usually causes one of two things: The "Security Violation": You reboot, and instead of your Minecraft menu, you get a big red box saying "Secure Boot Violation." This means the BIOS refuses to run GRUB because it doesn't recognize the "signature." The Silent Boot: It completely ignores GRUB and boots straight into Windows because Windows is the only one with a "signed" certificate that the BIOS trusts by default. Why would you want it on? Usually, there’s only one reason: Valorant (Vanguard). If you plan on playing Valorant on your Tiny11 partition, it requires Secure Boot to be enabled on Windows 11. How to do it without "ruining" your work: If you need it on, don't just flip the switch and hope for the best. You have two main paths: Path A: The "Preboot" Way (Harder but cleaner) You have to use a tool called shim or sbctl in Linux to "sign" your CachyOS kernel and GRUB. This tells the BIOS, "Hey, I'm a legitimate OS, trust me." Path B: The ASUS "Key Management" Way (Easier) Go into BIOS -> Boot -> Secure Boot. Change "OS Type" to Windows UEFI mode. Go to Key Management. If you see an option to "Append Default Keys," do that first. If GRUB still won't boot, you may need to set Secure Boot to "Custom" and clear the keys, but that can sometimes make Windows unhappy. My Advice: If you don't need Secure Boot for a specific game like Valorant, leave it off. Most Linux users keep it disabled because it’s a proprietary gatekeeper that adds zero actual security for a home gaming PC but creates massive headaches for bootloaders. Are you trying to turn it on specifically for a game, or just because you feel like the system should have it on?
