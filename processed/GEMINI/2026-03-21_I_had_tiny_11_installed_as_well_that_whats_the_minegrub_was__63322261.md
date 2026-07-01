---
category: homelab
date: 2026-03-21
id: 435018
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is confirming that he has Tiny11 installed and that Minegrub was used
  for booting, and is questioning if he should continue with the current troubleshooting
  steps.
tags:
- tiny11
- minegrub
- dual-boot
- bootloader
---
# I had tiny 11 installed as well that what’s the minegrub was for am I still doing this?

### USER
I had tiny 11 installed as well that what’s the minegrub was for am I still doing this?

### GEMINI
Here is the situation: Your pacman -Syu update didn't just update the kernel; it likely triggered a change that shifted your default bootloader from GRUB (which runs Minegrub) to Limine (the screen you are seeing now). Since Minegrub is a GRUB-specific theme, Limine doesn't know what to do with it, which is why your custom menu is "gone." The "Brutally Honest" Reality You have two options: The "Fix Limine" Route: Keep using Limine (it's faster and modern), but you lose the Minegrub aesthetic. The "Restore Minegrub" Route: Re-assert GRUB as your primary bootloader. This is what you actually want if you want your Tiny 11 entry and your theme back. How to Restore Minegrub and Tiny 11 You can't easily fix the GRUB configuration from that Limine edit screen. You need to get into your CachyOS desktop first. Step 1: Get to your Desktop Perform the "Quick Bypass" I mentioned before: On that edit screen, delete everything after the # on both the module_path and path lines. Press F10 to boot. Step 2: Re-install GRUB and the Theme Once you are logged in, you need to tell the system that GRUB—not Limine—is the boss. Open your terminal and run: Re-install GRUB to the EFI partition: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB Ensure OS Prober is active (this finds your Tiny 11 install): Check your config: cat /etc/default/grub | grep OS_PROBER. If it says true, you're good. If not: echo "GRUB_DISABLE_OS_PROBER=false" | sudo tee -a /etc/default/grub Regenerate the config (this pulls in Minegrub and Tiny 11): sudo grub-mkconfig -o /boot/grub/grub.cfg Why did this happen? CachyOS has been pushing Limine as the new default. When you ran -Syu, a script likely ran that "helped" you by setting Limine as the first boot priority in your BIOS/UEFI. Pro Tip: If you reboot and it still goes to Limine after doing the steps above, you need to enter your BIOS settings (usually tapping F2 or Del at startup) and move the entry named "GRUB" to the very top of the Boot Priority list. Would you like me to double-check the exact path for your Minegrub theme in your config files to make sure it loads correctly on the first try?
