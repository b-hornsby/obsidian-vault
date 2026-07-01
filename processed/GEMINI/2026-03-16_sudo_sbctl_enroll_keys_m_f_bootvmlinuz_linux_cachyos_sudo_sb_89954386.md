---
id: 293751
source: GEMINI
date: 2026-03-16
tags: ['homelab', 'llm', 'ai', 'gemini', 'error', 'ide', 'class', 'database']
category: homelab
sentiment: curious
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md', 'nodes/people/dad.md']
---
# ❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
‼ File is immutable: /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f
You need to chattr -i files in efivarfs
‼ File is immutable: /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f
You need to chattr -i files in efivarfs

~ 8s
❯ 

### USER
❯ sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos
  sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi
[sudo] password for toastedmel0n:  
Enrolling keys to EFI variables...
With vendor keys from microsoft...
With vendor certificates built into the firmware...✓  
Enrolled keys to the EFI variables!
‼ File is immutable: /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f
You need to chattr -i files in efivarfs
‼ File is immutable: /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c
‼ File is immutable: /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f
You need to chattr -i files in efivarfs

~ 8s
❯ 

### GEMINI
This is a classic Linux defense mechanism. Your system has "locked" the EFI variables to prevent accidental damage, but we need them unlocked so sbctl can write your keys to the motherboard. The error message even tells you the fix: chattr -i. 1. Unlock the EFI Variables Run these three commands to remove the "immutable" (lock) attribute: sudo chattr -i /sys/firmware/efi/efivars/PK-8be4df61-93ca-11d2-aa0d-00e098032b8c sudo chattr -i /sys/firmware/efi/efivars/KEK-8be4df61-93ca-11d2-aa0d-00e098032b8c sudo chattr -i /sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f 2. Try the Enrollment Again Now that the door is unlocked, run the enrollment for your files: sudo sbctl enroll-keys -m -f /boot/vmlinuz-linux-cachyos sudo sbctl enroll-keys -m -f /boot/EFI/BOOT/BOOTX64.EFI sudo sbctl enroll-keys -m -f /boot/EFI/limine/limine_x64.efi 3. Re-sign and Re-lock If Step 2 finishes with a green checkmark: Re-sign: sudo sbctl sign -f /boot/vmlinuz-linux-cachyos (and the other two paths). Reboot to BIOS: Turn Secure Boot back to Enabled. Why this is the final hurdle: By clearing the "immutable" attribute, you're allowing Linux to talk directly to the motherboard's security chip. Once those keys are saved into the PK (Platform Key) and db (Signature Database), the hardware itself will recognize your Linux installation as "Safe." Did the chattr commands allow the enroll-keys to finish without those "Immutable" errors?