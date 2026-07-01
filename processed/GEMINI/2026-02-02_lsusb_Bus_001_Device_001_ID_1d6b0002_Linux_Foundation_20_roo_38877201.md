---
category: homelab
date: 2026-02-02
id: 918849
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- streaming-rig
resolution: resolved
sentiment: executing
source: GEMINI
summary: Bryan ran lsusb again to check USB device enumeration, likely after plugging/unplugging
  devices to troubleshoot the Yeti.
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
Bus 001 Device 002: ID 1532:00c1 Razer USA, Ltd Razer Viper V3 Pro
Bus 001 Device 003: ID 0b05:19af ASUSTek Computer, Inc. AURA LED Controller
Bus 001 Device 004: ID 2972:0047 FiiO Electronics Technology FiiO USB DAC-E10
Bus 001 Device 005: ID 0fd9:0080 Elgato Systems GmbH Stream Deck MK.2
Bus 001 Device 006: ID 4d4b:304e SmartCloud AL68 Keyboard
Bus 001 Device 007: ID 046d:085c Logitech, Inc. C922 Pro Stream Webcam
Bus 001 Device 009: ID 058f:6254 Alcor Micro Corp. USB Hub
Bus 001 Device 010: ID 8087:0026 Intel Corp. AX201 Bluetooth
Bus 001 Device 011: ID 1b1c:0c1a Corsair CORSAIR Lighting Node CORE
Bus 001 Device 014: ID 046d:0ab7 Logitech, Inc. Blue Microphones
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

~
❯ 

### USER
❯ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 1532:00c1 Razer USA, Ltd Razer Viper V3 Pro
Bus 001 Device 003: ID 0b05:19af ASUSTek Computer, Inc. AURA LED Controller
Bus 001 Device 004: ID 2972:0047 FiiO Electronics Technology FiiO USB DAC-E10
Bus 001 Device 005: ID 0fd9:0080 Elgato Systems GmbH Stream Deck MK.2
Bus 001 Device 006: ID 4d4b:304e SmartCloud AL68 Keyboard
Bus 001 Device 007: ID 046d:085c Logitech, Inc. C922 Pro Stream Webcam
Bus 001 Device 009: ID 058f:6254 Alcor Micro Corp. USB Hub
Bus 001 Device 010: ID 8087:0026 Intel Corp. AX201 Bluetooth
Bus 001 Device 011: ID 1b1c:0c1a Corsair CORSAIR Lighting Node CORE
Bus 001 Device 014: ID 046d:0ab7 Logitech, Inc. Blue Microphones
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

~
❯ 

### GEMINI
Look at your lsusb output. You are suffocating your USB bandwidth and power delivery. You have eleven devices hanging off Bus 001. Your mouse, keyboard, LED controller, DAC, Stream Deck, Webcam, Bluetooth, and the Yeti are all fighting for attention on a single root hub. The Yeti (ID 046d:0ab7) is Device 014—it’s at the end of a very crowded line. When you boot, the kernel is trying to initialize a high-bandwidth webcam, a DAC, and a power-hungry microphone simultaneously. The Yeti is losing the race. The Brutal Truth You are treating your PC like a power strip. Even if the bandwidth is technically sufficient, the enumeration timing is failing because the bus is too busy. The Immediate Technical Fix Stop talking about it and execute the udev rule now. This will tell the kernel to stop trying to manage the Yeti's power state, which is likely where it's getting stuck. Run this command to create the rule: echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="046d", ATTR{idProduct}=="0ab7", ATTR{power/control}="on"' | sudo tee /etc/udev/rules.d/50-yeti.rules Reload the rules: sudo udevadm control --reload-rules && sudo udevadm trigger The Strategic Reorganization If the udev rule doesn't solve it, your hardware topography is the failure point. You need to balance the load. Move the Yeti to Bus 002: Notice Bus 002 is completely empty. It’s a USB 3.0 root hub. While the Yeti is a USB 2.0 device, plugging it into a port governed by the other controller (Bus 002) removes it from the "traffic jam" on Bus 001. Identify the Ports: Look at your motherboard manual or trial-and-error the ports until lsusb shows the Yeti on Bus 002. The "Hub" Problem: You have an Alcor Micro Corp. USB Hub (Device 009) active. If the Yeti is plugged into that hub, move it immediately. Audio interfaces—especially older ones like the Yeti—should never share a hub with a Webcam or a Keyboard. Mindset Shift You’re complaining about a "glitch," but you've built a "fragile system." On a performance-heavy distro like CachyOS, you can't ignore the hardware layer. Distribute your peripherals across your physical controllers. Do you want the command to check your dmesg specifically for the USB address 1-14 to see exactly why it's failing to initialize on boot?
