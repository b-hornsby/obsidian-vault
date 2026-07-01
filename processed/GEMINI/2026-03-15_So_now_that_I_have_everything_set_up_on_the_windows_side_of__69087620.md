---
category: coding
date: 2026-03-15
id: 860575
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking what the next steps are after setting up Windows, likely
  in preparation for dual-booting with Linux.
tags:
- dual-boot-setup
- windows-configuration
- linux-setup
- system-configuration
---
# So now that I have everything set up on the windows side of things, what do I need to do moving forward?

### USER
So now that I have everything set up on the windows side of things, what do I need to do moving forward?

### GEMINI
Now that Windows is settled, we need to perform "The Great Reconciliation"—getting your PC to recognize that CachyOS still exists and giving you that Minecraft-themed menu you want. Since you are currently in Windows, the very first step is to get back into Linux. Phase 1: The Temporary Return Restart your PC. As soon as the screen goes black, start mashing F2 or Delete to enter your ASUS BIOS. Go to the Boot tab. You should see two options: Windows Boot Manager and CachyOS. Move CachyOS to the top of the list (Priority #1). Save and Exit (F10). If this works, you'll boot straight back into your CachyOS desktop. If it doesn't work (or if the "CachyOS" option is missing), you'll need to boot into your CachyOS Live USB and run the cachy-chroot fix I mentioned earlier. Phase 2: The Minecraft Theme (Minegrub) CachyOS uses systemd-boot by default because it's fast, but the Minecraft theme only works with a bootloader called GRUB. To get the "Select World" screen, we need to switch you over to GRUB. Once you are inside your CachyOS install, open the Terminal and follow these exact steps: 1. Install GRUB and the Theme: # Install the GRUB bootloader and the tool to find Windows sudo pacman -S grub os-prober # Install GRUB to your drive (replaces systemd-boot) sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB # Download the Minecraft Theme git clone https://github.com/Lxtharia/minegrub-theme.git cd minegrub-theme sudo cp -ruv ./minegrub /boot/grub/themes/ 2. Enable the Theme and Windows Detection: Open the configuration file: sudo micro /etc/default/grub (If you don't have 'micro', use 'nano') Scroll to the bottom and add these two lines: GRUB_DISABLE_OS_PROBER=false GRUB_THEME="/boot/grub/themes/minegrub/theme.txt" Press Ctrl+S to save and Ctrl+Q to exit. 3. Update the Menu: sudo grub-mkconfig -o /boot/grub/grub.cfg Look at the output! It should say "Found Windows Boot Manager on..." If it does, you're golden. The Reality Check When you reboot, you should see the Minecraft "World Selection" screen. The Warning: Every time you update your BIOS, ASUS might try to put "Windows" back at the top. If that happens, you just have to go back into the BIOS and put "GRUB" or "CachyOS" back as #1. Valorant Note: If Valorant (Vanguard) gives you a "Secure Boot" error on the Windows side, we will need to re-enable Secure Boot in your BIOS. If that breaks the Linux boot, let me know—there is a specific way to sign the Linux kernel so both work together. Are you able to boot into CachyOS through the BIOS right now, or is the "CachyOS" option missing from your boot list?
