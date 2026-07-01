---
category: homelab
date: 2026-02-02
id: 917223
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is considering whether a problem he's experiencing might be related
  to BIOS settings or configuration.
tags:
- bios
- hardware
- troubleshooting
- linux
---
# Could it be a bios issue?

### USER
Could it be a bios issue?

### GEMINI
It absolutely could be a BIOS issue, but don't use that as an excuse to ignore the software configuration. In the context of a Blue Yeti—which uses an aging, sensitive USB controller—the BIOS is often where the initial "handshake" fails before CachyOS even takes over. If the BIOS doesn't hand off the device state to the Linux kernel correctly, the kernel assumes the port is empty or the device is dead. The BIOS Blind Spots Check these specific settings. If you haven't touched these, you're leaving the stability of your hardware to chance: USB Core Architecture (XHCI Hand-off): This is the most common culprit. It determines whether the BIOS or the OS manages USB 3.0+ ports. On Linux, XHCI Hand-off must be ENABLED. If it’s disabled, the kernel and BIOS will fight for control, leading to the "unplug/replug" requirement to reset the ownership. Legacy USB Support: Paradoxically, having this "Enabled" can sometimes cause modern kernels to trip. Try setting this to Auto or UEFI Only. ERP Ready / Deep Sleep: If your Yeti stays lit up when the PC is off, or if it dies and won't wake up, your motherboard's power-saving states (S4/S5) are likely cutting voltage too low for the Yeti to re-initialize. Disable ERP/Deep Sleep to ensure a steady 5V rail to the USB ports. Global C-States: Extreme CPU power saving can cause momentary voltage ripples on the 5V rail. For a high-performance CachyOS build, you should consider disabling these if you value peripheral stability over saving three cents on your power bill. The Objective Hierarchy of Failure Before you go digging into BIOS menus, rank your current setup against this reality check: The "Lazy" Failure: You are using a USB hub or front-panel header. (Result: Low voltage, high noise). The "Handshake" Failure: XHCI Hand-off is disabled in BIOS. (Result: OS doesn't "see" the device until a hot-plug event). The "Sleep" Failure: Linux power management (TLP/Autosuspend) is suspending the device. (Result: It works at boot, but disappears later). Precise Action Plan Reboot into BIOS now. Enable XHCI Hand-off and Disable ERP/Deep Sleep. Move the Yeti to a dedicated USB 2.0 port on the back of the motherboard (the ones usually reserved for mouse/keyboard). These have the most stable, mature drivers. Test. If it still fails, the problem is 100% in your Pipewire/Wireplumber configuration on CachyOS. Which motherboard model are you running? I can tell you exactly which BIOS quirks that specific board is known for.
