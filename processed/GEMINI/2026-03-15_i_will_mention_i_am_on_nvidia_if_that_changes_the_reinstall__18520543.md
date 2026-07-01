---
category: homelab
date: 2026-03-15
id: 727994
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan mentioned he was on NVIDIA and asked if that changed the kernel reinstall
  steps.
tags:
- nvidia-drivers
- kernel-reinstall
- cachyos
- gpu-configuration
---
# i will mention i am on nvidia if that changes the reinstall kernel steps

### USER
i will mention i am on nvidia if that changes the reinstall kernel steps

### GEMINI
Since you're on an RTX 3070, we need to make sure the Nvidia modules are rebuilt for the new kernel. If we just install a generic kernel, you might boot into a black screen because the driver won't "snap" onto the new kernel automatically. Run these specific commands in your [root@CachyOS /]# prompt to get everything back in order: 1. Reinstall Kernel + Nvidia Drivers This command installs the kernel, the headers (needed for the driver to build), and the Nvidia modules. CachyOS prefers the open modules for your 30 series card. pacman -Sy linux-cachyos linux-cachyos-headers linux-cachyos-nvidia-open nvidia-utils 2. Build the "Initramfs" (The Startup Image) This command takes the kernel we just installed and packages it with your Nvidia drivers so they load immediately at boot. mkinitcpio -P Look for a line that says "Successfully generated" for linux-cachyos. 3. Final Update to the Minecraft Menu Now that the kernel and drivers are physically in the /boot folder, we tell GRUB to update the menu list. grub-mkconfig -o /boot/grub/grub.cfg Check the text output: It should finally say Found linux image: /boot/vmlinuz-linux-cachyos. Why this is the "Right" way for you: The RTX 3070: By installing linux-cachyos-nvidia-open, you ensure that the driver and the kernel are always in sync. The "Black Screen" Fear: Running mkinitcpio -P is what prevents the dreaded black screen. It bakes the video drivers into the boot process. Your Data: Again, notice we aren't touching anything in /home. This is strictly "under the hood" maintenance. Once those three steps are done, type exit and reboot. Does CachyOS finally appear in the "World Selection" list?
