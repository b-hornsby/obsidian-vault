---
category: homelab
date: 2026-03-15
id: 980032
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether a specific configuration task needs to be done through
  the live USB or directly on CachyOS.
tags:
- linux
- cachyos
- live-usb
- configuration
---
# Do I need to do that thru the live usb or just on cachyos now?

### USER
Do I need to do that thru the live usb or just on cachyos now?

### GEMINI
Since you've successfully booted into CachyOS and everything is "back to normal," you can do this directly from your CachyOS desktop. No more Live USB needed. Open your terminal in CachyOS and run these steps to finalize the Minecraft "World" names: 1. Create the Rename Script We'll create a script that automatically renames the boring labels every time the menu updates. sudo micro /etc/grub.d/99_rename_entries 2. Paste the Logic Inside the editor, paste this. Double-check if your Linux entry currently says "Arch Linux" or "CachyOS" on the boot screen and adjust the script below to match: #!/bin/sh set -e # Replace "Arch Linux" with your preferred name sed -i 's/menuentry "Arch Linux"/menuentry "Survival Mode (Linux)"/g' /boot/grub/grub.cfg # Replace "Windows Boot Manager" with your preferred name sed -i 's/menuentry "Windows Boot Manager"/menuentry "Hardcore Mode (Tiny11)"/g' /boot/grub/grub.cfg 3. Permissions & Activation Save and exit (Ctrl+S, then Ctrl+Q), then run these two commands to finish: # Make the script executable sudo chmod +x /etc/grub.d/99_rename_entries # Rebuild the menu to apply the new names sudo grub-mkconfig -o /boot/grub/grub.cfg One Final Warning on Secure Boot Since you mentioned Fortnite: If you decide to turn Secure Boot on later, do not just flip the switch in BIOS. It will "break" your Minecraft menu immediately. If a game eventually forces your hand, you'll need to install a tool called sbctl in CachyOS to "sign" your files. Until then, keep it Disabled and enjoy your custom boot screen. You're all set! Would you like me to show you how to change that yellow "Splash Text" (the bouncing text) next to the Minecraft logo?
