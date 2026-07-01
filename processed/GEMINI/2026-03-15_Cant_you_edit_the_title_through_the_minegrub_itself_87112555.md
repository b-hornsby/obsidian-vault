---
category: homelab
date: 2026-03-15
id: 330390
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if he can edit the bootloader title directly through Minegrub,
  likely to customize the boot menu with a Minecraft theme.
tags:
- linux
- cachyos
- bootloader
- grub
- minecraft-theme
---
# Can’t you edit the title through the minegrub itself?

### USER
Can’t you edit the title through the minegrub itself?

### GEMINI
Actually, you’ve hit on the most logical point: the theme does have its own logic for that under-text, but it's a bit of a "smoke and mirrors" situation. The theme doesn't actually "know" what OS is there; it just takes the name GRUB gives it (like "Arch Linux") and then looks at its own internal list to decide what "Version" or "Mode" to display underneath it. Here is how to edit the "Minegrub" logic directly: Since you want the under-text to change, you need to edit the theme's main definition file. Open the theme's config: sudo micro /boot/grub/themes/minegrub-world-selection/theme.txt The "Under-text" Problem: If you scroll through that file, you'll see a lot of complex positioning code. You won't find a simple "Type Tiny11 here" line because the theme is designed to automatically assign "Survival Mode" to Windows and "Creative Mode" to Linux based on the icons it finds. The "Brutal Truth" Solution Because Minegrub is designed to be "dynamic," editing the theme.txt is actually much harder than the os-prober trick I gave you. The theme.txt uses variables like (item_text) which are filled by GRUB. To get exactly what you want (Tiny11 as the title and custom under-text), the 30_os-prober edit is the only way to make it "stick" for the title. Do you want to change the "Splash Text" instead? If you want to change that yellow bouncing text next to the Minecraft logo (e.g., make it say "CachyOS is better than Windows!"), that is super easy to do through the theme files: Open the splashes file: sudo micro /boot/grub/themes/minegrub-world-selection/splashes.txt Delete everything and just put your own lines there. Save and exit. Do you want to try the Splash Text, or are you satisfied with the "Tiny11" name for now?
