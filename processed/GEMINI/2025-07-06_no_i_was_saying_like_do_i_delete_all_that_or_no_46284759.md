---
category: homelab
date: 2025-07-06
id: 902010
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether he should delete certain files or data as part of
  a troubleshooting or cleanup process.
tags:
- cleanup
- file-management
- troubleshooting
- wsl2
---
# no i was saying like do i delete all that or no?

### USER
no i was saying like do i delete all that or no?

### GEMINI
Ah, my apologies for the confusion! When you ran sudo nano /etc/resolv.conf and it showed all that text (like # This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8)), you should delete all of that content before adding nameserver 8.8.8.8. That block of text tells you that the file you're looking at is actually controlled by another system (systemd-resolved) and is just a symlink. We need to replace that symlink with our own static file. So, yes, you should delete everything that was in /etc/resolv.conf after running sudo nano /etc/resolv.conf and before adding nameserver 8.8.8.8. Here's the critical part of the instruction again for editing /etc/resolv.conf in Step 3: Step 3 (Revised): Delete Existing Content and Add New DNS Edit the resolv.conf file: sudo nano /etc/resolv.conf Delete ALL existing lines in this file. When you're in the nano editor, you can use the arrow keys to navigate and Ctrl+K to cut/delete an entire line. Keep pressing Ctrl+K until the file is completely empty. Add the following lines: nameserver 8.8.8.8 nameserver 8.8.4.4 Save the file: Press Ctrl+O, then Enter, then Ctrl+X. After doing this, continue with the rest of the steps I provided previously (making it immutable, shutting down WSL2, restarting, verifying DNS, clearing Hugging Face cache, and finally running Oobabooga).


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
