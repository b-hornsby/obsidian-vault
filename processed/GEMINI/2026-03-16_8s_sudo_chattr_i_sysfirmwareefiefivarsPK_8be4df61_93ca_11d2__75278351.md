---
id: 883911
source: GEMINI
date: 2026-03-16
tags: ['homelab', 'ai', 'gemini', 'lora', 'long', 'go', 'error', 'cert']
category: homelab
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md', 'nodes/people/dad.md']
---
# ~ 8s
❯ sudo chattr -i /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
  sudo chattr -i /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
  sudo chattr -i /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f

~
❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!

~
❯ 

### USER
~ 8s
❯ sudo chattr -i /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
  sudo chattr -i /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
  sudo chattr -i /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f

~
❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!

~
❯ 

### GEMINI
That’s it. You just won the war. Those green checkmarks mean your custom signatures are now physically burned into the motherboard's "Allow List." The BIOS will no longer see CachyOS as an intruder, and because you used the -m flag, it still recognizes Microsoft’s keys for Windows and Valorant. The Final Finish To be absolutely, 100% certain there is no "Shim" error this time, force one final signature on the files you just enrolled: sudo sbctl sign -f /boot/vmlinuz-linux-cachyos sudo sbctl sign -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl sign -f /boot/EFI/limine/limine_x64.efi The BIOS Lock-In Reboot and enter your BIOS. Go to Boot -> Secure Boot. Set it to Enabled (or Windows UEFI Mode). Save and Exit (F10). What should happen now: The PC boots. No Red Box. No "Shim" error. The Minegrub menu appears. You boot into Tiny11, and Valorant finally launches without the "Secure Boot" requirement error. Go flip that BIOS setting. Are you finally looking at a working menu with Secure Boot ON?