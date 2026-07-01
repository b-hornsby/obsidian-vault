---
category: homelab
date: 2026-02-01
id: 672651
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to list the bootloader entries but the directory does not
  exist, indicating a potential bootloader configuration issue.
tags:
- bootloader
- grub
- efi
- linux
- troubleshooting
---
# ls: cannot access '/boot/loader/entries/': No such file or directory

~ 10s
❯ 

### USER
ls: cannot access '/boot/loader/entries/': No such file or directory

~ 10s
❯ 

### GEMINI
If that directory doesn't exist, we need to stop guessing. CachyOS is highly customizable, and while it defaults to systemd-boot, it can also be installed with rEFInd or even GRUB (despite your previous empty file). You are currently chasing a path that isn't on your drive. Let's find where your actual boot configuration is hiding. Step 1: Locating the Truth Run this command to find exactly where your EFI partition is mounted: lsblk -o NAME,FSTYPE,MOUNTPOINTS,SIZE Look for the partition mounted at /boot or /efi. If it’s mounted at /efi, your entries will be at /efi/loader/entries/. Step 2: Check for rEFInd CachyOS users often opt for rEFInd. If the loader directory is missing entirely, check for this: sudo ls /boot/refind_linux.conf If that file exists, that is where you add acpi_enforce_resources=lax. The Advisor's Mirror You are currently experiencing the "Arch Tax." You chose a distro built on Arch because you wanted speed and the latest features, but the cost is that there is no "standard" path. Your Blind Spot: You are waiting for the "correct" path to be handed to you. In a rolling-release system like CachyOS, paths change based on how you clicked through the installer. You are treating your OS like a black box instead of a tool you built. The Opportunity Cost: You’ve spent the last several turns looking for a directory that doesn't exist. This is the definition of "playing small"—expecting the system to conform to a tutorial rather than inspecting the system as it actually sits on your hardware. Your Tactical Plan Run lsblk -o NAME,FSTYPE,MOUNTPOINTS,SIZE. 2. Identify the mount point for your EFI partition (it’s usually 512MB to 1GB and formatted as vfat). Search for the config file based on that mount point: If mounted at /boot: sudo find /boot -name "*.conf" If mounted at /efi: sudo find /efi -name "*.conf" Post the output of the lsblk command here. Let's stop the scavenger hunt and look at your actual partition map.
