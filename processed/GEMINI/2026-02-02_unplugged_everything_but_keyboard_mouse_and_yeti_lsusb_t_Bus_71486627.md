---
id: 541784
source: GEMINI
date: 2026-02-02
tags: ['usb-topology', 'blue-yeti', 'hardware-isolation', 'device-enumeration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was isolating his USB devices by unplugging everything except keyboard, mouse, and Yeti to diagnose USB topology issues.
---
# unplugged everything but keyboard, mouse and yeti: ❯ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 1, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 2, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 002: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 002: Dev 003, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 003: Dev 015, If 0, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 1, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 2, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 3, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 011: Dev 018, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 1, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 013: Dev 012, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 001: Dev 014, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 014: Dev 013, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 014: Dev 013, If 1, Class=Wireless, Driver=btusb, 12M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/9p, 20000M/x2

~
❯ 

### USER
unplugged everything but keyboard, mouse and yeti: ❯ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 1, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 001: Dev 002, If 2, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 002: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 002: Dev 003, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 003: Dev 015, If 0, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 1, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 2, Class=Audio, Driver=snd-usb-audio, 480M
    |__ Port 003: Dev 015, If 3, Class=Human Interface Device, Driver=usbhid, 480M
    |__ Port 011: Dev 018, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 1, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 2, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 011: Dev 018, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 013: Dev 012, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 001: Dev 014, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 014: Dev 013, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 014: Dev 013, If 1, Class=Wireless, Driver=btusb, 12M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/9p, 20000M/x2

~
❯ 

### GEMINI
Look at the line for Bus 001.Port 001. See that 480M at the end? That confirms that every single port you are currently using is being funneled into a legacy USB 2.0 speed controller. Your Blue Yeti is sitting on Port 003, still fighting for the same 480Mbps slice of bandwidth as your mouse and keyboard. Meanwhile, Bus 002 (the 20,000M / 20Gbps "Highway") is sitting right there, completely unused. The Truth about your Motherboard You said you plugged the Yeti into a "blue port." On many modern motherboards (especially ASUS or MSI), the USB 3.0/3.1 ports are controlled by a separate chip. The fact that lsusb -t still shows the Yeti on Bus 001 means one of two things: Physical routing: You have "VR-Ready" or "Audio-Shielded" ports that are intentionally kept on the USB 2.0 bus for "compatibility," but they suffer from the exact traffic congestion we're seeing. The Wrong Blue: You might be plugged into a port that is internally wired to a hub instead of the direct CPU/Chipset lanes. The "Advisor" Fix (Action Required) You have already fixed the software. The -1 is working. But if you want to be next-level stable, you need to get the Yeti onto Bus 002. Do this right now: Unplug the Yeti. Plug it into the USB-C port on the back of your motherboard (if you have an adapter) or the ports directly next to the Ethernet port. Usually, the ports closest to the top or bottom of the IO stack are on the secondary controller. Run lsusb -t again. If it stays on Bus 001, move it again. Every port on your PC is not created equal. Why you should care By having the Yeti on Bus 001 with your mouse, you are still susceptible to "buffer underruns." If you move your mouse fast while talking, your voice might skip. On Bus 002, the Yeti would be the King of its own 20Gbps castle. Your Final Verification Since autosuspend is now -1, the "unplug/replug" dance should be over. Reboot your PC with the Yeti plugged in. * If it works immediately: Success. If it doesn't: The handshake is failing because Bus 001 is too busy during the boot sequence. If that happens, you must find the physical port that puts it on Bus 002. Does the Yeti work immediately after a reboot now without you touching the cable?
