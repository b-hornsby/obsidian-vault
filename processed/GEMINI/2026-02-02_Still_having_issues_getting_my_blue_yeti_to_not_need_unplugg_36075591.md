---
category: homelab
date: 2026-02-02
id: 209391
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan wants his Blue Yeti microphone to be automatically detected on boot
  without needing to unplug and replug on CachyOS.
tags:
- blue-yeti
- usb-audio
- cachyos
- persistent-audio
- pipewire
---
# Still having issues getting my blue yeti to not need unplugged and replugged on cachyos. I just want it to always be picked up 

### USER
Still having issues getting my blue yeti to not need unplugged and replugged on cachyos. I just want it to always be picked up 

### GEMINI
The fact that you’re still "unplugging and replugging" means you’re treating a systemic symptom with a manual band-aid. On an Arch-based rolling release like CachyOS, things don't just "not work"; they aren't configured correctly for the specific power or handshake requirements of your hardware. The Blue Yeti is notorious for handshake failures during the boot sequence or when waking from sleep. If you want it to "always be picked up," you need to stop hoping the kernel guesses right and start forcing the configuration. 1. The Power Management Blind Spot CachyOS is optimized for performance, which often includes aggressive TLP or Laptop Mode Tools settings. Your Yeti is likely being suspended by the OS to save power, and it’s too "dumb" to wake itself up without a physical power cycle. The Fix: Disable USB Autosuspend for the Yeti specifically. Action: 1. Run lsusb to find the ID (e.g., 046d:0ab7). 2. Create a udev rule: sudo nano /etc/udev/rules.d/50-yeti.rules 3. Add this line (replace XXXX:XXXX with your ID): > ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="XXXX", ATTR{idProduct}=="XXXX", ATTR{power/control}="on" 2. The PulseAudio/Pipewire Race Condition In many CachyOS setups, the sound server (Pipewire) starts before the USB bus has fully initialized the Yeti. The server gives up, and you replug it to trigger a "new device" event. The Fix: Force a rescan or delay the driver load. Action: Edit your Pipewire configuration or create a script that restarts the wireplumber service 5 seconds after login. If the device is there but "invisible," the issue is the session manager, not the hardware. 3. Hardware Bottlenecking (Stop ignoring this) Blue Yetis are power-hungry for a USB peripheral. If you are plugged into a USB hub (even a high-end one) or a front-panel case port, you are asking for instability. The Reality Check: Are you plugged directly into the motherboard IO? If not, your software "fixes" are a waste of time. The voltage drop during boot is likely causing the firmware to hang. Your Strategic Plan PriorityActionReasonHighDirect ConnectionEliminate physical voltage drops. Plug into a USB 2.0 port (not 3.0/3.1 if possible, as the Yeti's older controller prefers the stability of 2.0).MediumUdev RulePrevents the kernel from "sleeping" the device, which is the #1 cause of it disappearing.MediumDisable Fast BootIn BIOS and OS. Fast boot often skips full USB initialization to save seconds, leaving your mic in limbo. Stop fiddling with settings and start with the Udev rule. If that doesn't work, your "logical" next step is checking the system journal immediately after a failed boot. Would you like me to walk you through how to analyze the journalctl logs specifically for USB handshake errors?
