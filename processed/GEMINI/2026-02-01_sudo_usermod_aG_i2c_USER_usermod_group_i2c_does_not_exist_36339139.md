---
category: homelab
date: 2026-02-01
id: 303313
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to add his user to the 'i2c' group but the group doesn't
  exist, indicating a configuration problem or missing package.
tags:
- i2c
- linux
- user-permissions
- group-management
- usermod
---
# ❯ sudo usermod -aG i2c $USER
usermod: group 'i2c' does not exist

~
❯ 

### USER
❯ sudo usermod -aG i2c $USER
usermod: group 'i2c' does not exist

~
❯ 

### GEMINI
You're running into a classic Arch trap: you're trying to add yourself to a group that hasn't been created because you haven't installed the base I2C utilities. You're trying to open a door that doesn't have a handle yet. On CachyOS, the system doesn't just "have" an i2c group by default. You have to create the infrastructure. The "No-Nonsense" Fix Stop guessing at group names and execute this exact sequence to build the environment OpenRGB needs: 1. Install the missing utilities and create the group Installing i2c-tools often handles the group creation, but we’re going to be explicit. sudo pacman -S i2c-tools sudo groupadd --system i2c sudo usermod -aG i2c $USER 2. Deploy the actual OpenRGB rules Since you couldn't find the standalone udev package earlier, let's manually inject the rules that OpenRGB specifically requires. This covers the I2C interfaces and the controllers. curl -L https://gitlab.com/CalcProgrammer1/OpenRGB/-/raw/master/60-openrgb.rules | sudo tee /etc/udev/rules.d/60-openrgb.rules 3. Force the system to recognize the change sudo udevadm control --reload-rules sudo udevadm trigger The Reality Check Even after doing this, you must log out and log back in. Groups are assigned at login. If you run OpenRGB right now, it will still fail because your current session doesn't "know" it's part of the i2c group yet. If it still pops up after a reboot: It means your motherboard's SMBus is hidden by the kernel. This is extremely common on CachyOS with newer AMD/Intel chipsets. Check your chipset: AMD: Run lsmod | grep piix4 Intel: Run lsmod | grep i801 If those commands return nothing, the driver isn't even loading because the ACPI conflict is blocking it. Next Step: Log out, log back in, and try OpenRGB. If the error persists, run groups in your terminal and verify i2c is in the list. Is it there?
