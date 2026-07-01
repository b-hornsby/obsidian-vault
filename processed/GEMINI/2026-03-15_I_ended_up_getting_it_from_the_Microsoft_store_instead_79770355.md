---
id: 214421
source: GEMINI
date: 2026-03-15
tags: ['software-installation', 'microsoft-store', 'windows-setup']
category: general
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan mentioned he got something from the Microsoft Store instead, likely during a software setup process.
---
# I ended up getting it from the Microsoft store instead

### USER
I ended up getting it from the Microsoft store instead

### GEMINI
Smart move. LibreWolf via the Store is much easier than fighting with a stripped-down PowerShell. Now that you're at the desktop and have your browser, you’re in the "Windows Phase." But as we discussed, your CachyOS entry has likely "vanished" from the boot process because Windows took over the priority. The "Dual-Boot" Recovery Plan Once you’ve finished installing your Nvidia drivers and Valorant, we need to get that menu back so you can actually choose between the two systems. Here is the objective truth of your current situation: CachyOS is safe: It's still sitting on that 1.5TB partition. The Bootloader is "Hidden": Windows set its own "Windows Boot Manager" as the #1 priority in your BIOS. How to Fix the Menu (The Professional Way) You don't need to reinstall anything. We are going to use the CachyOS Live USB (the one you used for GParted) to tell the system that CachyOS should be the boss of the boot menu again. When you are ready to fix the boot menu, follow these steps: Boot back into the CachyOS Live USB (Normal or GRUB2 mode). Open the terminal (Konsole). Type sudo cachy-chroot. It will ask you to select your root partition. Pick the Btrfs one (should be nvme0n1p2). If it asks to mount additional partitions, say No. Once you are "inside" your install (the prompt will change), run these two commands: sudo bootctl install (This reinstalls the bootloader files). sdboot-manage gen (This generates the menu entries for both Linux and Windows). A Warning for Valorant Since you are on Windows 11 (Tiny11), Vanguard requires Secure Boot to be enabled in your BIOS. If you find that CachyOS won't boot with Secure Boot on, we may need to enroll the CachyOS keys in your BIOS later. For now: Just focus on getting your Windows drivers and games ready. Are you all set with your Windows drivers, or do you want to jump back into the Live USB now to fix the boot menu?
