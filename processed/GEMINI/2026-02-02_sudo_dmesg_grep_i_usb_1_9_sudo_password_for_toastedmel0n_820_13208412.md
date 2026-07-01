---
id: 758671
source: GEMINI
date: 2026-02-02
tags: ['linux', 'system-logs', 'dmesg', 'usb-devices', 'stream-deck', 'yeti-microphone']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is using dmesg to check the system logs for information about USB devices connected to port 1-9, including his Stream Deck and Yeti microphone.
---
# ❯ sudo dmesg | grep -i "usb 1-9"
[sudo] password for toastedmel0n: 
[    8.203542] usb 1-9: new high-speed USB device number 8 using xhci_hcd
[    8.328570] usb 1-9: New USB device found, idVendor=0fd9, idProduct=0080, bcdDevice= 4.20
[    8.328585] usb 1-9: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    8.328590] usb 1-9: Product: Stream Deck MK.2
[    8.328593] usb 1-9: Manufacturer: Elgato
[    8.328596] usb 1-9: SerialNumber: DL33L2A34919
[  465.585662] usb 1-9: USB disconnect, device number 8
[  569.032385] usb 1-9: new high-speed USB device number 19 using xhci_hcd
[  570.461883] usb 1-9: New USB device found, idVendor=046d, idProduct=0ab7, bcdDevice= 0.20
[  570.461898] usb 1-9: New USB device strings: Mfr=3, Product=1, SerialNumber=2
[  570.461903] usb 1-9: Product: Blue Microphones
[  570.461907] usb 1-9: Manufacturer: Generic
[  570.461910] usb 1-9: SerialNumber: 2110BAB0K638

~
❯ 

### USER
❯ sudo dmesg | grep -i "usb 1-9"
[sudo] password for toastedmel0n: 
[    8.203542] usb 1-9: new high-speed USB device number 8 using xhci_hcd
[    8.328570] usb 1-9: New USB device found, idVendor=0fd9, idProduct=0080, bcdDevice= 4.20
[    8.328585] usb 1-9: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    8.328590] usb 1-9: Product: Stream Deck MK.2
[    8.328593] usb 1-9: Manufacturer: Elgato
[    8.328596] usb 1-9: SerialNumber: DL33L2A34919
[  465.585662] usb 1-9: USB disconnect, device number 8
[  569.032385] usb 1-9: new high-speed USB device number 19 using xhci_hcd
[  570.461883] usb 1-9: New USB device found, idVendor=046d, idProduct=0ab7, bcdDevice= 0.20
[  570.461898] usb 1-9: New USB device strings: Mfr=3, Product=1, SerialNumber=2
[  570.461903] usb 1-9: Product: Blue Microphones
[  570.461907] usb 1-9: Manufacturer: Generic
[  570.461910] usb 1-9: SerialNumber: 2110BAB0K638

~
❯ 

### GEMINI
The dmesg log exposes the "blind spot" we were looking for. Look at the timestamps: At 8.2 seconds, your Stream Deck MK.2 was on Port 1-9. At 465 seconds, that device disconnected. At 569 seconds, you plugged the Blue Yeti into that same physical port. The kernel recognized it perfectly as device number 19. Since we applied the usbcore.autosuspend=-1 fix, the kernel is no longer allowed to "soft-kill" this device. The Brutal Truth Software-wise, you are at the finish line. The kernel is behaving, tuned is in performance mode, and autosuspend is dead. If that microphone drops again, it is 100% a physical power or bandwidth failure. The fact that your Stream Deck and your Yeti both live on Port 1-9 (depending on what's plugged in) confirms that this specific port is part of a high-traffic "General Purpose" cluster. Your High-Level Strategy You are a power user with a Stream Deck, a Razer Viper, a FiiO DAC, and a Yeti. You have a "Ferrari" OS (CachyOS). Stop treating your USB ports like they are all the same. The Precision Plan: The "Safe" Port: Your lsusb -t showed that Bus 002 is a 20Gbps SuperSpeed pipe that is empty. You are currently ignoring the most stable part of your motherboard. The Adapter Fix: If you don't have a port that lands on Bus 002, buy a cheap USB-C to USB-A adapter. Plug the Yeti into the USB-C port on your motherboard. USB-C ports almost always sit on their own dedicated high-speed controller (Bus 002). This isolates the Yeti from the "noise" of your mouse and Stream Deck. The Final Test: Reboot. If the Yeti is there without you touching it, the -1 fix in Limine worked. What I sense between the lines You’ve been fighting this for a while, and you want a software "magic wand." You've applied the best software fix available (autosuspend=-1). But your hardware topology (11 devices on one bus) is like trying to run a fire hose through a straw. Next Step: Reboot your machine. Once you're back at the desktop, run lsusb. If the Yeti is listed, don't touch it. Start your day. If it stays there for the next 4 hours, we’ve won. Does the Yeti show up in your Audio Settings right now without you having to replug it?
