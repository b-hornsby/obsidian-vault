---
id: 061493
source: GEMINI
date: 2026-02-02
tags: ['udev-rules', 'blue-yeti', 'usb-device', 'power-management']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is examining udev rules related to his Blue Yeti microphone, probably to manage its power settings.
---
# ❯ cat /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"

~
❯ 

### USER
❯ cat /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"

~
❯ 

### GEMINI
There is your conflict. You have two rules doing the exact same thing, but the first one is "naked"—it doesn't specify an ACTION. On some kernel versions, a rule without a specified action can trigger on every event (add, change, remove, bind), which can cause the device to "flutter" during the boot sequence and fail to initialize properly in PipeWire. Also, both of these are missing the most important part for CachyOS: disabling the autosuspend timer. Let's clean this mess up and do it properly so you never have to think about this again. 1. Wipe the redundant rules Get rid of both to ensure no legacy junk is interfering: sudo rm /etc/udev/rules.d/50-blue-yeti.rules /etc/udev/rules.d/50-yeti.rules 2. Create the "Final" Rule This version includes the autosuspend flag. This is the "magic" that usually stops the need for a physical replug because it prevents the kernel from putting the Yeti into a sleep state it can't wake up from. Run this: echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on", ATTR{power/autosuspend}="-1"' | sudo tee /etc/udev/rules.d/99-yeti-fix.rules 3. Apply and Verify Tell the kernel to look at the new rule immediately: sudo udevadm control --reload-rules && sudo udevadm trigger Now, check if the "Autosuspend" is actually disabled for that device: cat /sys/bus/usb/devices/$(lsusb -d 046d:0ab7 | awk '{print $2 "/" $4}' | sed 's/://' | sed 's/^0*//;s/\/0*/\//')/power/autosuspend 2>/dev/null || echo "Check failed, but rule is applied." (If it returns -1, you’ve won.) Why this was failing you: Without the ATTR{power/autosuspend}="-1", CachyOS was likely seeing the Yeti, turning the power "on" (your old rule), but then 2 seconds later, the kernel's default power management was saying "Hey, this device is idle" and suspending it. Because the Yeti firmware is ancient, it doesn't know how to respond to a "Wake up" signal from Linux, so it just sits there "dead" until you replug it. Does pavucontrol show the mic bars moving now without a replug? If not, your next step is to check if it's muted in alsamixer (hit F6, select Yeti, check "Capture").
