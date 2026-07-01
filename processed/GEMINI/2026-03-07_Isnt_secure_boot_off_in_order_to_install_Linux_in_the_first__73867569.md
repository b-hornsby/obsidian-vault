---
id: 259168
source: GEMINI
date: 2026-03-07
tags: ['secure-boot', 'linux-installation', 'dual-boot', 'bios-settings']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was questioning whether Secure Boot needs to be disabled to install Linux.
---
# Isn’t secure boot off in order to install Linux in the first place?

### USER
Isn’t secure boot off in order to install Linux in the first place?

### GEMINI
Yes, you are 100% correct—the standard procedure for installing most Linux distros, including CachyOS, is to disable Secure Boot because the installer media isn't signed by Microsoft's keys. However, you’re now in a "Catch-22": Windows 11/Tiny11 and modern games like Fortnite/COD effectively require Secure Boot to be ON to function correctly in 2026, but turning it on will break your CachyOS boot. Here is the "High-Level Advisor" solution to keep both systems happy without buying new hardware. 1. The Reality Check: You can't just flip a switch If you simply turn Secure Boot back on in your BIOS right now: Windows/Tiny11: Will work perfectly. CachyOS: Will fail to boot with a "Security Violation" or "Invalid Signature" error. 2. The Strategic Solution: sbctl Since you are on CachyOS (Arch-based), you have access to the best tool for this: sbctl. It allows you to create your own Secure Boot keys, sign your CachyOS kernel, and enroll them into your motherboard so that both Linux and Windows can boot with Secure Boot Enabled. The Workflow: Keep Secure Boot OFF for now. Install Tiny11 on your 120GB SSD (unplug your 2TB drive during this to be safe). Plug your 2TB drive back in and boot into CachyOS. In CachyOS, install sbctl: sudo pacman -S sbctl Use sbctl to create your keys and enroll them with Microsoft's keys included (so Windows still boots): sudo sbctl create-keys sudo sbctl enroll-keys -m Sign your CachyOS bootloader and kernel: sudo sbctl sign -s /boot/vmlinuz-linux-cachyos # (And your EFI bootloader file, e.g., /boot/EFI/cachyos/grubx64.efi) Reboot, go into your BIOS, and turn Secure Boot ON. 3. Why this is worth the effort Fortnite/COD Compatibility: These games' anti-cheats (BattlEye/Ricochet) check the Secure Boot status. If it's off, you might get kicked from matches or barred from competitive play. System Integrity: You get the security benefits of Secure Boot on both OSes without sacrificing your optimized CachyOS environment. The "Use What You Have" Summary 120GB SSD: Tiny11 + Fortnite (signed via BIOS). 1TB HDD: Call of Duty storage. 2TB NVMe: CachyOS (signed via sbctl). You have a top-tier i7-12700K and Z790 system. Don't settle for a "half-broken" dual boot where you're constantly flipping BIOS settings. Taking 15 minutes to set up sbctl is the "pro" move here. Would you like me to find the specific CachyOS Wiki commands for signing your exact bootloader (Limine or GRUB)?
