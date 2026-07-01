---
id: 360149
source: GEMINI
date: 2026-03-15
tags: ['grub-configuration', 'dual-boot-repair', 'windows-boot-issue', 'bootloader-problem']
category: coding
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is frustrated because editing the GRUB configuration has made Windows unbootable, and he wants to restore the original functionality.
---
# When I edited the grub directly now the windows side doesn’t show? I just want it to be back to normal I don’t care if it says arch at this point

### USER
When I edited the grub directly now the windows side doesn’t show? I just want it to be back to normal I don’t care if it says arch at this point

### GEMINI
Don't panic—this happens because manual edits to grub.cfg are extremely fragile. If a single quote or bracket is misplaced, GRUB gets confused and just hides the entry entirely. Since you just want it back to "normal" and functional, the easiest fix is to let the system regenerate the file automatically. It will overwrite your manual edits with the working, default configuration. How to get Windows back: Open your terminal in CachyOS. Run the generator: sudo grub-mkconfig -o /boot/grub/grub.cfg Watch the output: Look for a line that says Found Windows Boot Manager on /dev/nvme0n1p1. If you see that, you're golden. If you still want "CachyOS" instead of "Arch" safely: If you want to change the Linux name without breaking the file again, do it the "official" way which only takes one line: Open the default config: sudo micro /etc/default/grub Change the Distributor line: Look for GRUB_DISTRIBUTOR="Arch" and change it to GRUB_DISTRIBUTOR="CachyOS". Save and Update: Press Ctrl+S, Ctrl+Q, then run: sudo grub-mkconfig -o /boot/grub/grub.cfg This method is "safe" because it doesn't touch the complicated boot code; it just tells the generator what label to use. Verification Reboot your PC. You should see both entries again. Did Windows reappear in the menu after running the grub-mkconfig command?
