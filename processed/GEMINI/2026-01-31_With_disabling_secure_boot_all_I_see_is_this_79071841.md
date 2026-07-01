---
id: 369984
source: GEMINI
date: 2026-01-31
tags: ['secure-boot', 'cachyos', 'installation', 'boot-issues']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan disabled secure boot for CachyOS installation but is only seeing an unclear screen.
---
# With disabling secure boot all I see is this

### USER
With disabling secure boot all I see is this

### GEMINI
You’re in the right place, but ASUS makes this unnecessarily cryptic. They don't give you a simple "On/Off" switch for Secure Boot. You have to change the OS Type to trick the motherboard into backing off. The ASUS "Disable" Maneuver Change "OS Type": Click on Windows UEFI mode and change it to Other OS. Why? This is ASUS-speak for "Turn off Secure Boot enforcement." It tells the motherboard to stop looking for Microsoft-signed keys. Verify: After you switch it to "Other OS," look at the Secure Boot state at the top. It should change to "Disabled" (though you might need to save and reboot back into BIOS once to see the status update). One More Stop Before You "Full Send" While you are in the Advanced Mode (which you are), you need to check your drive mode. This is the #1 reason Linux installs fail on ASUS boards: Navigate to the Advanced tab (top menu). Look for SATA Configuration or Storage Configuration. Find SATA Mode Selection or VMD Setup Menu. If VMD is enabled, Disable it. VMD is an Intel technology that hides your NVMe drive from Linux. Ensure the mode is set to AHCI, not RAID. Final Step: The Boot Order Go to the Boot tab. Scroll down to Boot Option Priorities. Set Boot Option #1 to your USB thumb drive (it usually says "UEFI: [Your Drive Name]"). Execution Press F10 to Save & Exit. The computer should reboot and load the CachyOS installer. If the screen stays black or loops back to BIOS, tell me. It usually means the "Other OS" setting didn't take and we need to clear the keys in the "Key Management" menu below it.
