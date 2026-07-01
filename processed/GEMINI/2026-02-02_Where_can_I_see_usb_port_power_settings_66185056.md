---
id: 485707
source: GEMINI
date: 2026-02-02
tags: ['usb-power', 'cachyos', 'system-settings']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to locate USB port power management settings on CachyOS to troubleshoot his Yeti microphone.
---
# Where can I see usb port power settings?

### USER
Where can I see usb port power settings?

### GEMINI
On your ASUS motherboard, USB port power settings are not always in one place. They are spread across a few specific sub-menus in Advanced Mode. Look in these three specific locations to ensure your Blue Yeti never loses power: 1. The "Soft Off" State (Most Important) This setting controls if power is delivered to the ports when the computer is shut down or in sleep. Path: Advanced -> Onboard Devices Configuration Setting: Look for USB power delivery in Soft Off state (S5). Action: Set this to Enabled. Why: If this is disabled, the Yeti loses all power the moment you shut down, which can cause it to fail to initialize when the power suddenly returns during boot. 2. Battery Charging Support Some ASUS boards have a specific toggle for high-draw USB power (often labeled for phone charging), which provides a more stable current. Path: Advanced -> Onboard Devices Configuration Setting: Look for USB 3.1 battery charging support or ASmedia USB 3.1 battery charging support. Action: Set to Enabled. 3. APM Configuration (ErP Ready) As we discussed, the ErP setting is the master "kill switch" for power savings. Path: Advanced -> APM Configuration Setting: ErP Ready. Action: Ensure this is Disabled. Why: If ErP is Enabled (S4+S5), it strictly limits power consumption to under 1W, which effectively kills all USB power. The Final "Hardware" Reality Check If you have applied all these BIOS settings and the Yeti still doesn't "wake up" with the PC: Check the Port: On ASUS boards, avoid the "USB BIOS Flashback" port for your mic. It has extra circuitry for firmware flashing that can occasionally interfere with standard audio handshakes. Cable Quality: The Blue Yeti uses a Mini-USB connector (ancient by modern standards). If the cable is thin or very long, the voltage drop is enough to fail the handshake even if the BIOS is perfect. Are you back in CachyOS now? If so, run lsusb and give me the output. I'll give you the exact terminal command to create the udev rule that will prevent CachyOS from ever trying to put that mic to sleep.
