---
category: coding
date: 2026-03-15
id: 679336
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to customize the bootloader (likely GRUB) to display 'cachyos'
  instead of 'Arch Linux' and potentially modify the text underneath.
tags:
- grub-customization
- bootloader-configuration
- arch-linux
- cachyos
---
# This is what I see currently. I want arch Linux to say “cachyos” and to be able to change the under text if possible. That is the current objective

### USER
This is what I see currently. I want arch Linux to say “cachyos” and to be able to change the under text if possible. That is the current objective

### GEMINI
The image confirms the Minegrub theme is working, but it’s pulling the default "Arch Linux" and "Windows Boot Manager" strings. To change both the titles (the bold text) and the under-text (the descriptions), you need to modify the GRUB configuration directly. Since the script approach didn't work, we'll use a direct "Search and Replace" while you are booted into CachyOS. 1. The Direct Modification Open your terminal and run this command: sudo micro /boot/grub/grub.cfg 2. Change the Linux Entry Search (Ctrl+F) for the first occurrence of menuentry 'Arch Linux'. To change the Title: Change 'Arch Linux' to 'CachyOS'. To change the Under-text: Look a few lines down for a line starting with set subclass=. The theme uses metadata to generate that bottom text. However, to force a specific "Version" or "Mode" string, you usually have to look for the echo commands or the specific Minegrub theme logic further down in that file. 3. Change the Windows Entry Search (Ctrl+F) for Windows Boot Manager. Change the Title: Change it to 'Tiny11' (or whatever you prefer). The Under-text: Notice in your photo it says "Survival Mode, No Cheats." This is hardcoded into the theme's script. The "Minegrub" Way (Better for the Under-text) The Minegrub theme actually has its own configuration file that handles those "Survival Mode" and "Creative Mode" labels. Navigate to the theme folder: cd /boot/grub/themes/minegrub-world-selection/ Look for a file named theme.txt or a Python/Bash script in that folder. If you see a file called update_theme.py or similar, that is usually where the "Creative Mode" and "Date" strings are generated. Warning: The "Wipe" Factor Because you are editing /boot/grub/grub.cfg directly, running sudo grub-mkconfig in the future will reset these names to default. If you want it to be truly permanent, do this: sudo micro /etc/default/grub Change GRUB_DISTRIBUTOR="Arch" to GRUB_DISTRIBUTOR="CachyOS" Save and run sudo grub-mkconfig -o /boot/grub/grub.cfg. This will at least fix the Linux title permanently. Which specific "under-text" do you want to change? (e.g., Do you want to change the date "11/02/2002" or the "Creative Mode" text?)
