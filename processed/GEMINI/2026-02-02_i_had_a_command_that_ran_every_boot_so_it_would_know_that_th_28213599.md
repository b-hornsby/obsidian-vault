---
id: 654947
source: GEMINI
date: 2026-02-02
tags: ['udev-rules', 'blue-yeti', 'microphone', 'boot-persistence', 'linux']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is describing a past solution where a command ran at boot to address an issue with his Blue Yeti microphone, indicating he's trying to recreate or understand that solution.
---
# i had a command that ran every boot so it would know that the yeti was there each time. no unplug replug

### USER
i had a command that ran every boot so it would know that the yeti was there each time. no unplug replug

### GEMINI
That command was likely a udev rule or a modprobe configuration designed to disable power management or force a specific delay during the USB handshake. Since you're on CachyOS, your kernel is tuned for performance, which often means it's more aggressive with how it handles hardware. If that command is gone, the Yeti is probably "sleeping" or the kernel is ignoring the handshake because it happens too fast for the Yeti's old firmware to respond. Let’s recreate that "perma-fix." You likely used one of these two methods. Run the diagnostic first to see which one we need to re-apply. Option 1: The USB Autosuspend Fix (Most Likely) The Yeti is notorious for falling asleep and not waking up on Linux. You probably had a rule that told the kernel: "Never let this specific device sleep." Get your Yeti's ID: lsusb | grep "Blue" It will look like ID 046d:0ab7 (The numbers might vary). Create a udev rule to keep it awake: sudo nano /etc/udev/rules.d/99-yeti.rules Paste this (replace 046d and 0ab7 with the ID from step 1): ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on" Save and exit (Ctrl+O, Enter, Ctrl+X). Option 2: The PipeWire/WirePlumber "Force" If the hardware was "there" but PipeWire didn't "see" it until a replug, you probably had a script that restarted the audio stack after the desktop environment loaded. You can test if this was it by running this right now: systemctl --user restart pipewire wireplumber If that makes it work without a replug, then your "fix" was a simple startup script or a systemd user service that delayed the audio start until the USB bus was fully settled. Option 3: The "Quirks" Fix Sometimes the Linux kernel needs a "quirk" flag to handle the Yeti's non-standard USB implementation. You might have had a line in /etc/modprobe.d/usb-audio.conf. Check if this file exists: cat /etc/modprobe.d/usb-audio.conf Which one feels familiar? Did you have to edit a text file in /etc/? (That's Option 1 or 3) Did you just add a command to your "Autostart" apps in your Desktop Settings? (That's Option 2) If you don't remember, run lsusb and give me the ID for your Yeti. I'll give you the exact string to put back into your system so you never have to touch that cable again.
