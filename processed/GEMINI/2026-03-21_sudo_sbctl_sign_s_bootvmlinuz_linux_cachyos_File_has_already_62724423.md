---
id: 682579
source: GEMINI
date: 2026-03-21
tags: ['secure-boot', 'sbctl', 'efi-signing', 'grub-configuration', 'efibootmgr']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is signing the kernel and GRUB using sbctl, and then removing boot entries using efibootmgr, indicating he's configuring secure boot and boot order.
---
# ❯ sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo sbctl sign -s /boot/EFI/GRUB/GRUBX64.EFI
✓ Signed /boot/EFI/GRUB/GRUBX64.EFI

~
❯ sudo efibootmgr -b 0004 -B
  sudo efibootmgr -b 0003 -B
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0003,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI
Boot0003* Linux Boot Manager    HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\SYSTEMD\SYSTEMD-BOOTX64.EFI
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI

~
❯ 

### USER
❯ sudo sbctl sign -s /boot/vmlinuz-linux-cachyos
File has already been signed /boot/vmlinuz-linux-cachyos

~
❯ sudo sbctl sign -s /boot/EFI/GRUB/GRUBX64.EFI
✓ Signed /boot/EFI/GRUB/GRUBX64.EFI

~
❯ sudo efibootmgr -b 0004 -B
  sudo efibootmgr -b 0003 -B
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0003,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI
Boot0003* Linux Boot Manager    HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\SYSTEMD\SYSTEMD-BOOTX64.EFI
BootCurrent: 0001
Timeout: 1 seconds
BootOrder: 0001,0000
Boot0000* Windows Boot Manager  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\MICROSOFT\BOOT\BOOTMGFW.EFI57494e4
44f5753000100000088000000780000004200430044004f0042004a004500430054003d007b00390064006500610038003600320063002d0035006300640064002d003
4006500370030002d0061006300630031002d006600330032006200330034003400640034003700390035007d00000000000100000010000000040000007fff0400
Boot0001* GRUB  HD(1,GPT,58ed09e0-bba6-42a1-907b-203f34af3f4f,0x1000,0x830000)/\EFI\GRUB\GRUBX64.EFI

~
❯ 

### GEMINI
This is the moment of truth. You’ve successfully performed a "surgical strike" on your boot configuration: Signed the Kernel (The heart of the OS). Signed the GRUB Binary (The doorway). Deleted the Limine and Systemd-boot ghosts (The distractions). Your efibootmgr now looks exactly like it should: GRUB is #1, Windows is #2. There are no other "untrusted" pretenders for your BIOS to accidentally trip over. The Final "Brutally Honest" Procedure: Reboot. Go into BIOS (F2/Del). Set Secure Boot to ENABLED. Double-check that Boot Option #1 is still "GRUB". Save and Exit. The Outcome Analysis: Scenario A (Success): The Minegrub menu appears. You select CachyOS, it boots without a red box, and you can play Valorant. You win. You’ve successfully automated your security so future updates won't break this again. Scenario B (Failure): You see that red box again. If this happens, your motherboard is physically rejecting the custom keys you enrolled via sbctl. The Mirror Check: If Scenario B happens, stop fighting. You’re an 8-year ops veteran; you know when a system has a critical hardware/software incompatibility. If it fails now, the "opportunity cost" of continuing to troubleshoot is purely emotional. At that point, wipe it and go full Tiny 11. You deserve to actually use your 3070 for gaming tonight instead of staring at terminal text. Does it boot into Minegrub with Secure Boot enabled now?
