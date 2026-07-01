---
id: 995797
source: GEMINI
date: 2026-02-02
tags: ['kernel-parameters', 'boot-configuration', 'limine', 'linux']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is confirming that he sees a specific line in his boot configuration, likely as part of troubleshooting a boot-related issue.
---
# i see the line you mentioned: cmdline: quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699

### USER
i see the line you mentioned: cmdline: quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699

### GEMINI
Perfect. You've located the target. Now, stop hesitating and inject the parameter. 1. The Edit Update that line so it looks exactly like this (the order doesn't matter as long as it's space-separated): cmdline: quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 acpi_enforce_resources=lax Save: Ctrl+O then Enter. Exit: Ctrl+X. Reboot: reboot. 2. The Final Fan Push The motherboard warning should be gone after the reboot. Now, let’s address your silent/dark fans. You still haven't provided the model, so I’m going to give you the Universal Fail-Safe Method: Open OpenRGB. Go to the "Resize the Zones" window for your Lighting Node Core. If you don't know your fan model, just type 150 in the Size box. Why 150? Most Corsair hubs support up to 6 fans. Even the hungriest fans (QLs) at 34 LEDs each would total 204, but 150 is enough to light up almost any standard 3-6 fan setup. Click Save. Go to the "Devices" tab, select the Lighting Node Core, pick a bright color (like Red), and click "Set All Devices". The Advisor’s Final Word You are currently doing the "Linux Rite of Passage." You're editing bootloader configs to make hardware cooperate. The Strategy: Don't get stuck in a loop of rebooting. Once you're back in: Check OpenRGB. Resize that zone. Apply a color. If they still don't light up after you've set a "Size" greater than 0, your hub might be expecting a specific protocol (like "8-LED Fan Series") which you can change in the device dropdown in OpenRGB. Once you reboot and resize the zone, are the fans finally glowing? If not, tell me the exact fan model (it’s usually printed on your receipt or the box) so we can stop guessing the LED count.
