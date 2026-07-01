---
category: coding
date: 2026-03-15
id: 748480
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble with his BIOS not recognizing both drives, preventing
  him from booting into the desired OS.
tags:
- bios-configuration
- boot-order
- dual-boot-issue
- drive-detection
---
# When I go into my bios I only see one drive and when I save and exit it goes right back to windows. I’m in bios right now. What do I do?

### USER
When I go into my bios I only see one drive and when I save and exit it goes right back to windows. I’m in bios right now. What do I do?

### GEMINI
This is exactly why I warned you about the "clash of egos" between Windows and Linux. When Tiny11 installed, it didn't just add itself to the drive—it likely rewrote the EFI variables in your motherboard's NVRAM, effectively telling your BIOS, "Ignore whatever CachyOS was doing; I'm the only OS here now." Since you can't see CachyOS in the BIOS, we have to "force" the motherboard to recognize it again. Phase 1: The Rescue Mission You need to boot back into your CachyOS Live USB (the one you used to resize the partitions). Boot from the USB. Open the Terminal (Konsole). Type this command: sudo cachy-chroot The Prompt: It will ask you to select your root partition. Pick the one that says Btrfs (this is your CachyOS install). Mount Partitions: When it asks if you want to mount additional partitions, say No. The Re-Entry: Now you are "inside" your actual CachyOS system through the terminal. Run these two commands to reclaim the bootloader: sudo bootctl install sudo sdboot-manage gen (If the second command fails or isn't found, don't worry—the first one is the most important for getting the BIOS entry back). Type exit and then Reboot. Phase 2: Back in the BIOS After running those commands and rebooting, go back into your BIOS (F2/Del). You should now see "CachyOS" back in the Boot Priority list. Move it to Position #1. Save and Exit. Phase 3: The Minecraft Theme (Minegrub) Once you are back in your actual CachyOS desktop, you can finally set up the "Minecraft" menu. As I mentioned before, this theme requires GRUB, not the default systemd-boot. Since you've had a rough time with the bootloader today, here is the "Safest Path" to the Minecraft theme once you're back in Linux: Install GRUB: sudo pacman -S grub os-prober Install to Drive: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB The Theme: ```bash git clone https://github.com/Lxtharia/minegrub-theme.git cd minegrub-theme sudo cp -ruv ./minegrub /boot/grub/themes/ Edit Config: sudo micro /etc/default/grub Find GRUB_DISABLE_OS_PROBER and set it to false. Add GRUB_THEME="/boot/grub/themes/minegrub/theme.txt" at the bottom. Update: sudo grub-mkconfig -o /boot/grub/grub.cfg Does the cachy-chroot trick work for you to get the entry back in the BIOS?
