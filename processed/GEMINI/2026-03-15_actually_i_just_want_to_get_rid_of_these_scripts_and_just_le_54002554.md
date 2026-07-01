---
category: coding
date: 2026-03-15
id: 019359
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan wants to remove some scripts and revert his system to its previous
  state.
tags:
- script-removal
- system-cleanup
- configuration-reversal
---
# actually i just want to get rid of these scripts and just leave it as is 

### USER
actually i just want to get rid of these scripts and just leave it as is 

### GEMINI
Smart move. We’ve been over-engineering a solution for a cosmetic issue, and the more scripts we pile on, the more likely something breaks during a system update. In the Linux world, simple is almost always better for long-term stability. Let's clean up the "clutter" we created so your system is back to a stock, predictable state. 1. Remove the custom scripts Run these commands to delete the extra files we made: sudo rm /etc/grub.d/99_tiny11_rename sudo rm /etc/pacman.d/hooks/grub-rename.hook 2. Revert the system scripts You'll want to make sure there are no stray sed lines left in your main GRUB scripts: sudo micro /etc/grub.d/30_os-prober -> Scroll to the bottom and delete any sed lines you added. sudo micro /etc/grub.d/40_custom -> Do the same (delete any sed lines at the bottom). 3. Reset the Menu Now, run the generator one last time to make sure everything is "clean" and working: sudo grub-mkconfig -o /boot/grub/grub.cfg The Reality Check You've successfully moved to CachyOS, set up a custom Minegrub theme, and got your hardware running right. Having a slightly long name for the Windows partition is a tiny "imperfection" in an otherwise high-end, custom build. By leaving it as-is, you ensure that next time there’s a major GRUB or Kernel update, you won't be staring at a broken bootloader because a custom script got in the way. Is there anything else on your CachyOS setup or your AI dev environment you want to tweak before you call it a day?
