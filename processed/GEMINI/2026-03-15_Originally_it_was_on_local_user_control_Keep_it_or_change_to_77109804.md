---
category: homelab
date: 2026-03-15
id: 009012
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked whether to keep local user control settings or switch to auto
  during Tiny11 setup.
tags:
- user-account-control
- windows-settings
- tiny11-configuration
- local-user-control
---
# Originally it was on local user control? Keep it or change to auto?

### USER
Originally it was on local user control? Keep it or change to auto?

### GEMINI
"Local User Control" means the BIOS will stop and ask you every time it sees a change. Given that we are deliberately modifying the partition table to dual-boot, change it to "Auto Recovery" for now. This allows the motherboard to accept the new GPT header that Windows just wrote without halting the boot process with that "corruption" warning. The Plan: Set to "Auto Recovery." Save and Exit (F10). Observe the boot: Scenario A: It boots into Tiny11 setup (Great, let it finish). Scenario B: It boots into your Ventoy USB (If so, unplug the USB and restart so it finds the NVMe). Scenario C: It boots back to that Error or BIOS (We'll have to use the CachyOS Live USB to fix the GPT header manually). Go ahead and set it to Auto, hit F10, and tell me which "Scenario" you land in.
