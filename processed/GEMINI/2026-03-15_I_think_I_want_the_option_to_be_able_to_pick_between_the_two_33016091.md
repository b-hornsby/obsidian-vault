---
category: homelab
date: 2026-03-15
id: 048285
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted to set up a boot menu to choose between two OSes and asked about
  using a Minecraft-themed bootloader screen.
tags:
- dual-boot
- bootloader
- minecraft-grub-theme
- os-selection-menu
- custom-bootloader
---
# I think I want the option to be able to pick between the two os before I boot into either one. I seen there’s a Minecraft bootloader screen that’s custom you can add for something like that?

### USER
I think I want the option to be able to pick between the two os before I boot into either one. I seen there’s a Minecraft bootloader screen that’s custom you can add for something like that?

### GEMINI
That custom screen you’re thinking of is called "Minegrub." It makes your boot menu look exactly like the Minecraft "Select World" screen—CachyOS can be your "Hardcore Mode" world and Windows can be your "Survival" world. Since CachyOS uses systemd-boot by default, but the Minecraft theme is built for GRUB, we have two paths. If you want the Minecraft look specifically, the easiest way is to switch your bootloader to GRUB. How to get the "Minegrub" Menu You should do this from within CachyOS (not the Live USB, unless you can't boot into Cachy at all). 1. Install the Theme Open your terminal in CachyOS and run: git clone https://github.com/Lxtharia/minegrub-world-sel-theme.git cd minegrub-world-sel-theme sudo ./install_theme.sh 2. Make it see Windows For the menu to actually show Windows, you need a tool called os-prober: sudo pacman -S os-prober sudo grub-mkconfig -o /boot/grub/grub.cfg If it doesn't find Windows, we may need to edit /etc/default/grub and ensure GRUB_DISABLE_OS_PROBER=false is at the bottom. The "Mirror" Check: Efficiency vs. Aesthetics I need to be direct with you here: Aesthetics have an opportunity cost. The Risk: Swapping bootloaders (Systemd-boot to GRUB) while dual-booting with Windows is the #1 way people accidentally "break" their boot process. The Strategy: Right now, your priority is getting Valorant running to ensure Tiny11 is stable. Once you know the games work, then we can rice the bootloader. If we do it now and something breaks, you're stuck in a "no-boot" loop instead of gaming. My Recommendation: Finish Windows Drivers: Get the 3070 drivers and Valorant installed. The "Safety" Reboot: Restart your PC and mash F2/Delete to get to your ASUS BIOS. The Boot Order: Under the "Boot" tab, you should see "CachyOS" and "Windows Boot Manager." If you move CachyOS to the top, you'll boot into Linux. If you move Windows to the top, you'll boot into Tiny11. Do you want to stick with the BIOS switching for today to ensure your Windows install is solid, or are you ready to risk the "Minegrub" installation right now?
