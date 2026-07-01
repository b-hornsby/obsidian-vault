---
id: 729156
source: GPT
date: 2025-05-11
tags: ['rufus', 'uninstall', 'usb-creation-tool']
category: general
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan asked how to uninstall Rufus from his system.
---
# Uninstalling Rufus

### USER
How do I uninstall Rufus?

### ASSISTANT
Rufus is a portable application, which means **it doesn’t actually install on your system** like a traditional program. So, to "uninstall" Rufus, you just need to:

1. **Locate the Rufus executable** — usually named something like `rufus.exe`.
2. **Delete the file**.

That’s it! If you want to clean up further:

- Delete any **shortcuts** you created for Rufus.
- Optionally, you can clear any user settings stored in the registry at:
  ```
  HKEY_CURRENT_USER\Software\Akeo\Rufus
  ```
  (Use `regedit` carefully if you're comfortable with it.)

Would you like help checking for leftover files or settings?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
