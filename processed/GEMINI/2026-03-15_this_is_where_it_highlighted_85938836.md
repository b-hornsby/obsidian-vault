---
id: 715955
source: GEMINI
date: 2026-03-15
tags: ['error-analysis', 'system-debugging']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is indicating a specific section of output or a configuration file that is relevant to a problem he's experiencing.
---
# this is where it highlighted

### USER
this is where it highlighted

### GEMINI
In that newest screenshot, you are at line 179. You can see the case ${LONGNAME} in block. This is where the script starts categorizing the OS it found. If you want to stick with the system script edit, do this: Find line 202 (just a few lines down from your screenshot). It says: menuentry '$(echo "${LONGNAME} $onstr" | grub_quote)' ... Change that line to this exactly: menuentry 'Tiny11' $CLASS --class os ... BUT—There is a much easier way that won't break your system Editing 30_os-prober is like performing surgery with a sledgehammer. If you mess up a single quote, the whole menu disappears. The "Nuclear Option" I mentioned earlier is actually the "Pro" way because it's separate from the system files. Do this instead: Exit Micro (Ctrl+Q). Don't save changes to that complicated file. Create a new, simple script: sudo micro /etc/grub.d/99_tiny11_rename Paste this inside: #!/bin/sh sed -i 's/Windows Boot Manager (on \/dev\/nvme0n1p1)/Tiny11/g' /boot/grub/grub.cfg Save and Exit (Ctrl+S, Ctrl+Q). Give it permission to run: sudo chmod +x /etc/grub.d/99_tiny11_rename Apply it: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this is the winner: Every time you run that grub-mkconfig command, GRUB will build the menu normally (with the long name), and then this script will immediately "find and replace" it with Tiny11 before the file is finished. It’s permanent, it survives updates, and it’s way safer than editing line 202 of a system script. Does "Tiny11" show up in the menu now after running that last command?
