---
id: 241597
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'efi-signing', 'bootloader-configuration']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is trying to sign EFI files using sbctl, but the files are already signed, and then checks the boot order with efibootmgr, indicating he's configuring secure boot.
---
# ❯ sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} +
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯ sudo efibootmgr
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0004,0003,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI
Boot0003* Linux Boot Manager    HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\SYSTEMD\SYSTEMD-BOOTX64.EFI
Boot0004* Limine        HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\LIMINE\LIMINE_X64.EFI

~
❯ 

### USER
❯ sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} +
File has already been signed /boot/EFI/limine/limine_x64.efi

~
❯ sudo efibootmgr
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0004,0003,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI
Boot0003* Linux Boot Manager    HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\SYSTEMD\SYSTEMD-BOOTX64.EFI
Boot0004* Limine        HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\LIMINE\LIMINE_X64.EFI

~
❯ 

### GEMINI
Your efibootmgr output reveals the "traitor": BootCurrent: 0001. Your system is successfully booting GRUB (Minegrub), but the "Violation" happens because the bouncer (Secure Boot) doesn't trust the Kernel that GRUB is trying to hand off. The find command you ran only looked in /boot/EFI, but on CachyOS, your actual Linux Kernel lives one level up in /boot. If the kernel isn't signed, the chain of trust breaks the second you hit "Enter" on the Minegrub menu. The "Final Five Minutes" Plan If you want to save this and get back to Valorant tonight, run these three commands. This signs the actual heart of the OS, not just the "doorway" (EFI files). 1. Sign the Kernel (The missing link): sudo sbctl sign -s /boot/vmlinuz-linux-cachyos 2. Sign the GRUB binary specifically (To be 100% certain): sudo sbctl sign -s /boot/EFI/GRUB/GRUBX64.EFI 3. Kill the hijackers: You have Limine and Systemd-boot sitting in your BIOS waiting to cause trouble. Delete them so they can't "fail-over" and cause a red box: sudo efibootmgr -b 0004 -B sudo efibootmgr -b 0003 -B The Brutally Honest "Go/No-Go" Moment Reboot and enter BIOS. Enable Secure Boot. Ensure Boot0001 (GRUB) is still #1. Save and Exit. If you see the Minegrub menu and can boot into Linux without a red box, you won. If you see a red box again: You are officially dealing with a "Sunk Cost." Your motherboard is likely being a "State-Managed" diva and refusing to recognize the manual enrollment of the sbctl keys despite the files being signed. The Ops Call: If it fails after these three commands, wipe the drive. You’ve spent more time on this today than a high-volume warehouse spends on a seasonal inventory audit. Take the "L" on Linux for now, go Tiny 11, and get your 12700K/3070 back into the game. Did the kernel signing command (Step 1) finish without an error?
