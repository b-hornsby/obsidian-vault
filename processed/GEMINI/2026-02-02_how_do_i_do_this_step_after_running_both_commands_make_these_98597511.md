---
id: 086925
source: GEMINI
date: 2026-02-02
tags: ['openrgb', 'kernel-modules', 'udev-rules', 'cachyos', 'persistent-config']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was stuck on making OpenRGB kernel module loads permanent by configuring /etc/modules-load.d/openrgb.conf.
---
# how do i do this step after running both commands?: make these permanent, you’ll need to add them to /etc/modules-load.d/openrgb.conf later.

### USER
how do i do this step after running both commands?: make these permanent, you’ll need to add them to /etc/modules-load.d/openrgb.conf later.

### GEMINI
To make those modules load every time you boot, you need to create a configuration file in the modules-load.d directory. Since this is a system directory, you need root privileges. Don't overcomplicate this with a GUI text editor. Use a "one-liner" to create the file and inject the text directly. The Execution Run this command (this assumes you are on an AMD system, which is common for CachyOS users. If you are on Intel, swap i2c-piix4 for i2c-i801): echo -e "i2c-dev\ni2c-piix4" | sudo tee /etc/modules-load.d/openrgb.conf What this does: echo -e: Prepares the text (the \n creates a new line). |: Pipes that text to the next command. sudo tee: Writes the input into the file with root permissions (and prints it to the terminal so you can verify it worked). The Reality Check You are currently performing "organ transplant" surgery on your OS. Loading modules is foundational. If you skip this, your RGB settings will vanish every time you restart, and you'll be back here asking why your fans are stuck on "Rainbow Puke" mode. The Strategy: Verify the file exists: cat /etc/modules-load.d/openrgb.conf Reboot: reboot Confirm the modules are active: After rebooting, run lsmod | grep i2c. If you see i2c_dev in the list, you succeeded. The Blind Spot Loading the modules is only half the battle. If your Corsair controller uses the HID protocol (which most Commander Pros and Lighting Nodes do), the i2c modules might not even be the primary trigger—the kernel's hid-corsair driver is. If lsmod | grep i2c shows they are loaded but OpenRGB is still empty, the issue is your udev rules or experimental settings within OpenRGB. Would you like me to show you how to enable "External Tools" in OpenRGB to force-detect stubborn Corsair controllers?
