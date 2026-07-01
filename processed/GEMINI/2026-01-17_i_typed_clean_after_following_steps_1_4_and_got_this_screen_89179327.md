---
category: homelab
date: 2026-01-17
id: 597854
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was following diskpart steps to clean a USB drive and encountered an
  unexpected screen after typing 'clean'.
tags:
- diskpart
- clean-command
- usb-reformat
- windows-cli
---
# i typed "clean" after following steps 1-4 and got this screen 

### USER
i typed "clean" after following steps 1-4 and got this screen 

### GEMINI
That "Unknown capacity" message is actually a good sign—it means the clean command worked perfectly. By cleaning the drive, you've wiped the Linux partition table entirely, leaving the drive as a "blank slate" with no active partitions for Windows to measure. Because there is no partition yet, the standard "Format" window doesn't know what to do. You need to finish the process in the command prompt to tell Windows to treat that blank space as a single, usable 128 GB chunk. How to finish the job Go back to your Command Prompt (which should still be open as Administrator) and type these commands in order: Create the container: create partition primary This tells Windows to take all that "unknown" space and turn it into one big partition. Format the container: format fs=exfat quick This officially sets the file system. Use exfat for a 128 GB drive to ensure it works on both Windows and Mac. Give it a name (Optional): assign This gives the drive a letter (like E: or F:) so it shows up in your file explorer. Exit: exit Why the screen you saw happened The "Lies" are gone: The Linux flash created multiple hidden "zones" on your drive that Windows couldn't read. Empty State: clean deleted those zones. Right now, your computer sees the hardware but doesn't see a "volume" inside it to format. The Fix: create partition primary is the missing link that turns that raw hardware back into a storage volume. Would you like me to show you how to verify the drive is showing the correct 128 GB once you've finished these steps?
