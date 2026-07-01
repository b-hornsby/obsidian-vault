---
category: homelab
date: 2026-03-16
id: 700703
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if his current configuration will maintain his Minegrub menu,
  allow him to use both operating systems, and play Valorant with secure boot enabled.
tags:
- secure-boot
- minegrub
- dual-boot
- valorant
---
# And this still keeps the minegrub menu I have and allows me to use both os/play valorant with secure boot on?

### USER
And this still keeps the minegrub menu I have and allows me to use both os/play valorant with secure boot on?

### GEMINI
Yes, this is the only way to have your cake and eat it too. Here is the logic: Minegrub is just a visual skin for GRUB. By running grub-mkconfig, you are keeping the "skin" but fixing the "engine" underneath so it doesn't crash when it sees your custom Secure Boot keys. Valorant/Windows only cares that the BIOS says "Secure Boot: Enabled." It doesn't care how Linux boots, as long as the hardware security is locked. Dual Booting stays intact because grub-mkconfig will still see your Windows partition and keep it in the Minecraft menu. One Critical Detail When you run the grub-install command from the previous step, make sure the --bootloader-id matches whatever folder Minegrub is looking at. To be safe, let's use the standard ID: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --no-uefi-secure-boot The "Victory" Checklist: Edit /etc/default/grub (Add the blacklist flag). Run the grub-install command above. Sign the result: sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi Update the menu: sudo grub-mkconfig -o /boot/grub/grub.cfg Wait! Before you reboot, run ls /boot/EFI/CachyOS to make sure the file is actually there. If that folder doesn't exist, check ls /boot/EFI/GRUB instead and sign that one. Once you run those, flip Secure Boot back to ON in the BIOS. This is the configuration that finally reconciles the "Vanguard requirements" with your "Minegrub aesthetics." Ready to try?
