---
id: 253952
source: GEMINI
date: 2026-03-07
tags: ['cachyos', 'dual-boot', 'steam-deck', 'linux-gaming']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking about dual-booting implications given he's currently running CachyOS on his main 2TB drive.
---
# What if I’m using this to dual boot? I’m currently on cachyos on my main 2tb drive

### USER
What if I’m using this to dual boot? I’m currently on cachyos on my main 2tb drive

### GEMINI
This actually makes your situation easier and safer. Dual-booting from a separate physical drive (the 120GB SSD) is the gold standard for stability because it prevents Windows and Linux from fighting over the same EFI partition. Since you are on CachyOS, which uses the highly optimized Limine or GRUB bootloaders, here is the objective, low-friction plan to get this working without ruining your Linux setup. 1. The "Physical Isolation" Safety Rule Before you install Tiny11/Windows on that 120GB SSD: Unplug your 2TB CachyOS drive. * Why? Windows is notorious for seeing other bootloaders and "helping" by overwriting them or placing its own boot files on the wrong drive. By unplugging the Linux drive, you force Windows to keep its files strictly on the 120GB SSD. 2. The 2026 Anti-Cheat Reality Check In early 2026, Fortnite and COD (Black Ops 7/Warzone) have updated their requirements. To play competitive/tournaments, you must have: TPM 2.0 Enabled Secure Boot Enabled IOMMU Enabled (New for 2026) The Tiny11 Strategy: When you create your Tiny11 ISO using the Tiny11 Builder script, do not use the options to "Remove Requirement for TPM/Secure Boot." Your Z790 board supports these natively. If you bypass them, Fortnite will likely block you from entering matches. 3. Merging the Dual-Boot Once Windows is installed on the 120GB SSD, plug your 2TB CachyOS drive back in. Your BIOS will likely still boot straight into CachyOS. To add Windows to your boot menu: If you use Limine (CachyOS Default in 2026): Open your terminal in CachyOS and run: sudo limine-entry-tool --scan Limine will find the Windows Boot Manager on the 120GB drive and add it automatically. If you use GRUB: Install os-prober: sudo pacman -S os-prober Edit your config: sudo micro /etc/default/grub Ensure GRUB_DISABLE_OS_PROBER=false is at the bottom. Update GRUB: sudo grub-mkconfig -o /boot/grub/grub.cfg 4. Final Storage Triage 120GB SSD: Tiny11 OS + Fortnite (keep it here for the speed). 1TB HDD: Call of Duty (formatted as NTFS). The Benefit: CachyOS stays pristine on your NVMe. If Windows ever breaks itself, your Linux side remains untouched. The Opportunity Cost: You’re using a "surgical" setup now. It’s efficient, uses exactly what you have, and protects your main OS. Would you like the specific BIOS settings for your Asus Z790-P to ensure Secure Boot and IOMMU are ready for those 2026 anti-cheat checks?
