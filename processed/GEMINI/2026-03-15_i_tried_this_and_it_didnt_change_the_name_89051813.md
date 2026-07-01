---
category: coding
date: 2026-03-15
id: 546774
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because a customization attempt (likely in GRUB) didn't
  produce the expected result.
tags:
- grub-customization
- bootloader-problem
- configuration-issue
- troubleshooting
---
# i tried this and it didnt change the name?

### USER
i tried this and it didnt change the name?

### GEMINI
The reason it didn’t work is likely because grub-mkconfig builds the menu first, and your script needs to run after the file is already written to catch those names. Since you're on CachyOS, we can do this more cleanly by editing the theme's configuration directly. It’s more "brute force," but it’s guaranteed to work because it changes how the theme reads the system. The Direct Fix Instead of that script, let's edit the main GRUB configuration file directly. This is the "honest" way to see if the names even can be changed on your specific setup. 1. Open the GRUB config: sudo micro /boot/grub/grub.cfg 2. Find the "menuentry" lines: Press Ctrl+F and type menuentry. You are looking for lines that look like this: menuentry 'CachyOS' ... menuentry 'Windows Boot Manager' ... 3. Manually rename them: Change the text inside the quotes to exactly what you want: menuentry 'Survival Mode (Linux)' menuentry 'Hardcore Mode (Tiny11)' 4. Save and Exit: Ctrl+S, then Ctrl+Q. Why the previous script might have failed: If you ran grub-mkconfig and the names stayed the same, it means the "CachyOS" entry actually has a slightly different name in the code (like CachyOS Linux or CachyOS (on /dev/nvme...)). Check this now: When you look at the Minecraft menu, what is the exact, literal text written under the "World" icons? (e.g., Is it "CachyOS" or "CachyOS Linux"?) If you tell me the exact text, I can give you a sed command that won't miss. Would you like me to give you the command to change that yellow bouncing "Splash Text" while we're at it?
