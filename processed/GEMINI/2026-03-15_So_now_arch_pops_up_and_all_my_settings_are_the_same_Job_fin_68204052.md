---
id: 775366
source: GEMINI
date: 2026-03-15
tags: ['cachyos-boot', 'settings-persistence', 'dual-boot-verification', 'post-install-check']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed that CachyOS booted successfully with all settings intact after the dual-boot setup process.
---
# So now arch pops up and all my settings are the same. Job finished?

### USER
So now arch pops up and all my settings are the same. Job finished?

### GEMINI
Almost. If you can see Arch Linux (CachyOS) and Windows in that Minecraft menu and both actually boot when you select them, you are 95% of the way to the finish line. However, since you're a perfectionist about this setup, there are two "quality of life" things you should check before you call it a day: 1. The "World Names" (Optional) Right now, the menu probably says "Arch Linux" and "Windows Boot Manager." If you want it to look like a real Minecraft save list (e.g., "Survival Mode" for Linux and "Hardcore Mode" for Windows), you can edit the names. Would you like the instructions for that, or are you happy with the default labels? 2. The Boot Order Permanence Sometimes, Windows likes to be a "bad roommate." After a big Windows Update, it might try to shove itself back to the top of the boot list, making the Minecraft menu disappear. The Fix: If that happens, you don't need to do all this terminal stuff again. You just go into your BIOS and move GRUB back to #1. 3. Verification Before you close the case: Boot into CachyOS: Make sure your internet and GPU drivers are still behaving. Boot into Windows: Make sure Tiny11 didn't lose its activation or mess up its own boot files. If both are working and you love the look of the menu, then yes—job finished. You’ve successfully navigated one of the most annoying parts of PC ownership (Dual-Booting on a single drive). Is there anything else bugging you about the setup, or are you ready to go play?
