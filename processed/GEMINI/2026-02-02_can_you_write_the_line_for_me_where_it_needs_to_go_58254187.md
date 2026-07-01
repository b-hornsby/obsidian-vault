---
category: coding
date: 2026-02-02
id: 322508
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is asking the AI to write a specific line of code and indicate where
  it should be placed.
tags:
- code-generation
- code-assistance
---
# can you write the line for me where it needs to go

### USER
can you write the line for me where it needs to go

### GEMINI
Here is the exact modification you need. Since you are using Limine on CachyOS, you must edit the source configuration file and then run the generation tool to "push" those changes into the actual boot menu. 1. Edit the file Open the configuration file: sudo nano /etc/default/limine 2. Add this specific line Find the section where the KERNEL_CMDLINE is defined. You can simply add a new line at the bottom of the file to ensure it overrides or appends correctly. Copy and paste this exactly: KERNEL_CMDLINE[default]+=" usbcore.autosuspend=-1" Note: Make sure there is a space before usbcore inside the quotes. This ensures it doesn't "glue" itself to the previous parameter (like splashusbcore). 3. Commit the changes Simply saving the file isn't enough. You have to tell CachyOS to rebuild your boot entries: sudo limine-mkinitcpio (If the system says command not found, try sudo limine-update. One of these two will trigger the rebuild on your specific Cachy version). Why this is the "Kill Shot" The Problem: Your power-profiles-daemon was fighting your udev rules. The Fix: By adding this to the kernel command line, you are disabling the power-saving feature at the kernel level. This is higher than any daemon or software. The kernel will now ignore all requests to "suspend" USB devices. Your Final Checklist Reboot. Verify the Kernel: Run cat /proc/cmdline. You should see usbcore.autosuspend=-1 at the end of the string. Check the Yeti: Run cat /sys/module/usbcore/parameters/autosuspend. It should return -1. The Physical Reality: If it still acts up, look at your lsusb again. If that Yeti is still on Bus 001 with your high-polling Razer mouse, the issue is signal noise, not power. Move the Yeti to a blue/red USB 3.0 port to force it onto Bus 002. Once you've rebooted, let me know if cat /proc/cmdline shows the new parameter.
