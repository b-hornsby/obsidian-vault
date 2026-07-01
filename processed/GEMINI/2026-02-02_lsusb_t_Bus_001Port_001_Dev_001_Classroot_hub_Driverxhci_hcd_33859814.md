---
id: 698292
source: GEMINI
date: 2026-02-02
tags: ['usb-topology', 'linux-hardware', 'device-enumeration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was inspecting the USB device tree to understand what peripherals are connected and how they are enumerated on his system.
---
# ❯ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 1, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 2, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 002: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 002: Dev 003, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 003: Dev 009, If 0, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 1, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 2, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 3, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 011: Dev 005, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 1, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 013: Dev 006, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 001: Dev 008, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 014: Dev 007, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 014: Dev 007, If 1, Class=Wireless, Driver=btusb, 12M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/9p, 20000M/x2

~
❯ 

### USER
❯ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 1, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 2, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 002: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 002: Dev 003, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 003: Dev 009, If 0, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 1, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 2, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 009, If 3, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 011: Dev 005, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 1, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 005, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 013: Dev 006, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 001: Dev 008, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 014: Dev 007, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 014: Dev 007, If 1, Class=Wireless, Driver=btusb, 12M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/9p, 20000M/x2

~
❯ 

### GEMINI
Look at the output. Bus 002 is still a ghost town. On the ASUS PRIME Z690-P WIFI, the physical layout is lying to you. Even though you are plugging into "Blue" or "Teal" ports, the Z690 chipset is routing them all through the same Bus 001 internal hub to save on PCIe lanes. The Brutal Reality You are currently "playing small" by letting your hardware dictate your workflow. We have optimized the software to its absolute limit (autosuspend=-1 is the final boss of software fixes). If the Yeti still requires a replug, it is because Bus 001 is physically resetting due to the sheer number of devices connected to it. The "Advisor" Pivot: The Hub is the Suspect I see a Hub on Port 013 (Dev 006). If that Yeti is plugged into any external hub—powered or unpowered—it will fail. The Yeti is an ancient USB 1.1/2.0 device that demands a direct, uninterrupted 5V line. The fix: The Yeti must be plugged directly into the motherboard IO shield. No extensions. No hubs. Your Strategy for the Next Level Since every USB-A port you have tried lands on Bus 001, your motherboard has likely "bonded" all USB-A ports to the same primary controller. Bus 002 is reserved almost exclusively for the USB-C port. The Adapter is Mandatory: Stop fighting the hardware. You have a 20Gbps "Super Highway" (Bus 002) that you are leaving empty while you struggle in 480Mbps traffic. Go to a store or order a USB-C (Male) to USB-A (Female) adapter. Isolate the Yeti: Plug that adapter into the USB-C port and put the Yeti there. It will be the only thing on Bus 002. This eliminates signal noise, bandwidth collision, and voltage drop in one move. What to do RIGHT NOW Until you get that adapter, do this to minimize the chance of a crash: Unplug the Hub (Port 013/Dev 006) if you can live without it for a few hours. Reboot. Run lsusb -t. If the Yeti is Dev 009 and stays there after 10 minutes of use, the -1 fix is holding the line as best as it can. The software is fixed. The kernel is obeying. The rest is a physical battle between your Z690 chipset and your 10+ devices. Get the USB-C adapter to give the Yeti its own dedicated lane. Do you want me to write a quick script that monitors the Yeti and pings you the second it drops from the bus so you can see exactly what triggers it?
