---
id: 551334
source: GEMINI
date: 2026-03-21
tags: ['grub-configuration', 'dual-boot', 'os-prober', 'linux']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is running a command to enable GRUB OS prober for dual-boot detection.
---
# ❯ # This adds the line to the end of the file if it isn't already there
  echo "GRUB_DISABLE_OS_PROBER=false" | sudo tee -a /etc/default/grub
GRUB_DISABLE_OS_PROBER=false

~ 6s
❯ 

### USER
❯ # This adds the line to the end of the file if it isn't already there
  echo "GRUB_DISABLE_OS_PROBER=false" | sudo tee -a /etc/default/grub
GRUB_DISABLE_OS_PROBER=false

~ 6s
❯ 

### GEMINI
Step 1 is done. Now, you need to actually re-install the GRUB binaries and then generate the config that pulls in the Tiny 11 entry and your Minegrub theme. Since you've already set the OS_PROBER flag, run these two commands in order: 1. Re-install GRUB to the Drive This tells your motherboard's UEFI to prioritize the GRUB bootloader again. sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 2. Generate the Config (The "Big One") This is where the magic happens. Watch the terminal output closely—you want to see it say it found both CachyOS and Windows Boot Manager. sudo grub-mkconfig -o /boot/grub/grub.cfg The "Brutally Honest" Reality Check: If the output of that last command doesn't mention your Tiny 11 install, it means the partition isn't mounted or os-prober is being stubborn. Quick tip: If you want to be 100% sure it finds Tiny 11, mount the Windows partition first: Open your file manager (Dolphin). Click on your Windows/Tiny 11 drive to "mount" it. Then run the sudo grub-mkconfig command again. Did the output show "Found Windows Boot Manager" after you ran the second command?
