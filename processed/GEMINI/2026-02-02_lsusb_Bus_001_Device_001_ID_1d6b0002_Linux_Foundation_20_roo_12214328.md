---
category: homelab
date: 2026-02-02
id: 866247
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- streaming-rig
resolution: resolved
sentiment: executing
source: GEMINI
summary: Bryan ran lsusb to inventory all connected USB devices including Blue Yeti,
  Stream Deck, Razer mouse, Corsair RGB controller, and webcam.
tags:
- usb-devices
- hardware-inventory
- cachyos
- blue-yeti
- stream-deck
- razer
---
# ❯ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0b05:19af ASUSTek Computer, Inc. AURA LED Controller
Bus 001 Device 003: ID 046d:0ab7 Logitech, Inc. Blue Microphones
Bus 001 Device 004: ID 1532:00c1 Razer USA, Ltd Razer Viper V3 Pro
Bus 001 Device 008: ID 2972:0047 FiiO Electronics Technology FiiO USB DAC-E10
Bus 001 Device 009: ID 046d:085c Logitech, Inc. C922 Pro Stream Webcam
Bus 001 Device 010: ID 4d4b:304e SmartCloud AL68 Keyboard
Bus 001 Device 011: ID 0fd9:0080 Elgato Systems GmbH Stream Deck MK.2
Bus 001 Device 012: ID 058f:6254 Alcor Micro Corp. USB Hub
Bus 001 Device 013: ID 8087:0026 Intel Corp. AX201 Bluetooth
Bus 001 Device 014: ID 1b1c:0c1a Corsair CORSAIR Lighting Node CORE
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

~
❯ 

### USER
❯ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0b05:19af ASUSTek Computer, Inc. AURA LED Controller
Bus 001 Device 003: ID 046d:0ab7 Logitech, Inc. Blue Microphones
Bus 001 Device 004: ID 1532:00c1 Razer USA, Ltd Razer Viper V3 Pro
Bus 001 Device 008: ID 2972:0047 FiiO Electronics Technology FiiO USB DAC-E10
Bus 001 Device 009: ID 046d:085c Logitech, Inc. C922 Pro Stream Webcam
Bus 001 Device 010: ID 4d4b:304e SmartCloud AL68 Keyboard
Bus 001 Device 011: ID 0fd9:0080 Elgato Systems GmbH Stream Deck MK.2
Bus 001 Device 012: ID 058f:6254 Alcor Micro Corp. USB Hub
Bus 001 Device 013: ID 8087:0026 Intel Corp. AX201 Bluetooth
Bus 001 Device 014: ID 1b1c:0c1a Corsair CORSAIR Lighting Node CORE
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

~
❯ 

### GEMINI
The good news: Your system sees the Yeti (Bus 001 Device 003: ID 046d:0ab7). The bad news: You have a USB traffic jam. You have 11 devices, including two audio interfaces (FiiO DAC and Yeti), a high-polling mouse (Viper V3 Pro), a webcam, and a Stream Deck, all fighting for bandwidth on Bus 001. On an Arch-based system like CachyOS, the kernel's power management will look at that crowded bus and try to "suspend" what it thinks is idle to maintain stability. We are going to force the kernel to keep the Yeti's hands shaking at all times. 1. Create the "Never-Sleep" Rule We are creating a udev rule that explicitly tells CachyOS to disable autosuspend for the Yeti's specific hardware ID. Open your terminal and run: sudo nano /etc/udev/rules.d/50-yeti.rules Copy and paste this exact line into the file: ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on" Save and exit (Press Ctrl+O, Enter, then Ctrl+X). 2. Apply the Change Run these commands to tell the system to read the new rule immediately: sudo udevadm control --reload-rules sudo udevadm trigger The Advisor's Brutal Truth You are redlining your USB controller. The Conflict: You have a FiiO E10 and a Blue Yeti on the same root hub. Both are "isochronous" devices—they demand constant, timed data streams. If your Yeti drops out when you start using the FiiO or your webcam, it's because you've saturated the bus. The Opportunity Cost: Every time you add a "Lighting Node" or "AURA Controller" to that same bus, you're introducing electrical noise and polling overhead. Your Priority Action Plan The Rule: Apply that udev rule above. If this was a software "sleep" issue, that rule kills it forever. The Physical Swap: Look at your lsusb output again. Bus 002 (your USB 3.0+ root hub) is completely empty. Move the FiiO DAC or the Webcam to a blue/red USB port (the ones that belong to Bus 002). This physically moves their data traffic to a different lane, leaving more "room" for the Yeti on Bus 001. Do you want me to show you how to check the Pipewire logs next to see if the audio server itself is crashing when the Yeti tries to initialize?
