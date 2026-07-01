---
id: 560184
source: GEMINI
date: 2026-02-02
tags: ['bootloader', 'systemd-boot', 'grub', 'cachyos', 'system-configuration']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to determine whether CachyOS uses GRUB or systemd-boot as its bootloader.
---
# i am on cachyos so i don't know if it uses grub or systemd-boot

### USER
i am on cachyos so i don't know if it uses grub or systemd-boot

### GEMINI
To figure out which bootloader you're using, run this command: ls /boot If you see a grub folder, you're using GRUB. If you see a loader folder, you're using systemd-boot. If you see a limine folder or file, you're using Limine (the new 2026 default for CachyOS). Here is how to apply the fix for each one: 1. If you have GRUB Open the config file: sudo nano /etc/default/grub Find the line: GRUB_CMDLINE_LINUX_DEFAULT="..." Add acpi_enforce_resources=lax inside the quotes. Save (Ctrl+O, Enter) and Exit (Ctrl+X). Update the bootloader: sudo grub-mkconfig -o /boot/grub/grub.cfg Reboot. 2. If you have systemd-boot CachyOS uses a tool called sdboot-manage to handle this. Open the manager config: sudo nano /etc/sdboot-manage.conf Find the line starting with LINUX_OPTIONS. Add acpi_enforce_resources=lax to the end of that line inside the quotes. Save and Exit. Apply changes: sudo sdboot-manage gen Reboot. 3. If you have Limine (2026 Default) Open the config file: sudo nano /etc/default/limine Find the line KERNEL_CMDLINE[default]="...". Add acpi_enforce_resources=lax to the end. Save and Exit. Update the config: sudo limine-mkinitcpio Reboot. The "Mirror" Reality Check You’re doing the work, which is good, but don't lose sight of the objective. The lax parameter is only for the motherboard RGB. If your fans aren't lighting up, it's likely because you haven't performed the "Resize the Zones" step I mentioned in the last message. OpenRGB needs to know exactly how many LEDs are in your fan chain (e.g., 3 fans x 16 LEDs = 48). Quick Strategy: Which fan model do you have? (LL120, QL120, etc.) How many are plugged in? Once you give me those two numbers, I can tell you the exact "Size" value to type into OpenRGB so you can stop staring at black fans. Would you like me to calculate that for you?
