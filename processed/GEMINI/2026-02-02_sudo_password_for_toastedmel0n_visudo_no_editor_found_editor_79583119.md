---
id: 848087
source: GEMINI
date: 2026-02-02
tags: ['visudo', 'editor-config', 'sudoers']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan encountered an error when running visudo because no editor was configured on his system.
---
# [sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ 

### USER
[sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ 

### GEMINI
This is a classic Arch/CachyOS moment—the system is looking for the vi editor, but you likely only have nano installed (or the environment variable isn't set). Since we need to fix the sudo permissions so your Yeti can reset without you typing a password, we’ll force it to use nano. 1. Open Visudo with Nano Run this command: sudo EDITOR=nano visudo 2. Add the "Hall Pass" Scroll to the very bottom of the file and add this exact line: toastedmel0n ALL=(ALL) NOPASSWD: /usr/bin/usbreset Press Ctrl+O, then Enter to save. Press Ctrl+X to exit. 3. Test the "Electronic Replug" Now, let's see if the script actually works without asking for a password. Run: ~/reset_yeti.sh If you don't get a password prompt and you see a message about the device being reset (or just a clean return to the prompt), you’ve won. The software is now doing the physical labor of "unplugging" the mic for you. 4. The Final Strategic Move: The Autostart Since you are on CachyOS (likely using GNOME or KDE), you just need to make sure this script fires off 5 seconds after you log in. This gives the USB bus time to settle before we "kick" the Yeti into gear. Update the script one last time with a safety delay: echo -e '#!/bin/bash\nsleep 5\nsudo /usr/bin/usbreset 046d:0ab7' > ~/reset_yeti.sh The Brutal Truth You've essentially built a "software prosthetic" for a hardware defect. It’s not "elegant," but it’s the high-level advisor move: If you can't fix the antique hardware, automate the work-around. Would you like me to show you how to add this to your specific Desktop Environment's autostart list (GNOME or KDE)?
