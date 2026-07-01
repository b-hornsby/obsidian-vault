---
id: 538483
source: GPT
date: 2025-05-10
tags: ['ubuntu', 'windows-11', 'bootable-usb', 'os-recovery']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan got stuck in Ubuntu from a bootable USB and needed help returning to Windows 11.
---
# Exit Ubuntu Return Windows

### USER
I made a bootable Ubuntu drive but I want to go back to my windows 11 how do I get out of Ubuntu?

### ASSISTANT
To exit Ubuntu and go back to Windows 11, follow these steps:

### Step 1: **Remove the Bootable USB Drive**
If you're running Ubuntu from a bootable USB:
1. **Shut down your computer**.
2. **Remove the USB drive**.
3. **Turn your computer back on**.
   - It should automatically boot back into Windows 11 if it's still installed on your internal drive.

### Step 3: **Windows Still Not Booting?**
If you accidentally installed Ubuntu over Windows, you’ll need to:
- **Reinstall Windows 11** from a bootable Windows USB drive.
- Or, if Windows is still there but the bootloader is broken, **repair it**:
   1. Boot from a Windows 11 USB.
   2. Select **Repair your computer > Troubleshoot > Startup Repair**.

Do you know whether you installed Ubuntu over Windows or just ran it from USB?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]