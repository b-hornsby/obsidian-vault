---
id: 575911
source: GEMINI
date: 2026-02-02
tags: ['udev-rules', 'blue-yeti', 'usb-power-management', 'autosuspend-fix']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was removing old udev rules for his Blue Yeti and creating new ones to disable USB autosuspend and keep the microphone powered on.
---
# ❯ sudo rm /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules
[sudo] password for toastedmel0n: 

~
❯ echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"' | sudo tee /etc/udev/rules.d/99-yeti-fix.rules
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"

~
❯ sudo udevadm control --reload-rules && sudo udevadm trigger

~
❯ cat /sys/bus/usb/devices/$(lsusb -d 046d:0ab7 | awk '{print $2 "/" $4}' | sed 's/://' | sed 's/^0*//;s/\/0*/\//')/power/autosuspend 2>/dev/null || echo "Check failed, but rule is applied."
Check failed, but rule is applied.

~
❯ 

### USER
❯ sudo rm /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules
[sudo] password for toastedmel0n: 

~
❯ echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"' | sudo tee /etc/udev/rules.d/99-yeti-fix.rules
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"

~
❯ sudo udevadm control --reload-rules && sudo udevadm trigger

~
❯ cat /sys/bus/usb/devices/$(lsusb -d 046d:0ab7 | awk '{print $2 "/" $4}' | sed 's/://' | sed 's/^0*//;s/\/0*/\//')/power/autosuspend 2>/dev/null || echo "Check failed, but rule is applied."
Check failed, but rule is applied.

~
❯ 

### GEMINI
The "Check failed" message happened because my cat command was trying to be too clever with the file path and couldn't resolve the directory—ignore that for a second. The rule is now correctly placed, but we need to confirm the hardware actually woke up. Since you’ve applied the fix, do not touch the cable. Run this to see if the kernel is currently communicating with the Yeti: lsusb -v -d 046d:0ab7 | grep -i "iInterface" The "Logic" Check If it returns nothing: The device is disconnected or the kernel has truly dropped it. If it returns "Audio Control" or "Streaming": The kernel sees it. If you still have no sound, PipeWire is the one "ignoring" it. If it still isn't "picking up" (No Green Bars) CachyOS uses wpctl. Let’s see what the audio server thinks is happening: wpctl status Look under Sources. Is the Blue Yeti listed? Does it have a [MUTED] tag next to it? If it is there, try to force a volume reset on it: wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.8 wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0 The "Startup" Opportunity Cost If this fix requires a reboot to "settle," we should do it now. But before you do: Check your Mute Button on the physical mic. Is it solid red? (I know it's basic, but in all this terminal work, sometimes the simplest thing gets bumped). Open pavucontrol one last time. Under "Input Devices," make sure "Show" is set to "All Input Devices" at the bottom. Next Step: Reboot your machine. Don't unplug the mic. When you get back to the desktop, check if the mic is working immediately. If it works after reboot without a replug, your udev rule fixed the power-handshake issue. If it still requires a replug, it means your USB controller is failing to initialize the device during the BIOS/Grub handoff. Are you ready to reboot and test?
