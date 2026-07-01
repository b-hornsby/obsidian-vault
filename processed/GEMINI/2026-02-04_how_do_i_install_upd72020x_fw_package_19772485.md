---
category: homelab
date: 2026-02-04
id: 303074
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan needed help installing the upd72020x-fw package on CachyOS, likely
  for USB controller firmware.
tags:
- firmware
- upd72020x
- cachyos
- package-installation
- hardware
---
# how do i install upd72020x-fw package

### USER
how do i install upd72020x-fw package

### GEMINI
To install the upd72020x-fw package on CachyOS, you have it easy because CachyOS actually includes this package in its own optimized repositories. You don't even need the AUR for this one. Run this in your terminal: sudo pacman -S upd72020x-fw If you want to use paru (AUR version): If for some reason you prefer the AUR version or the main repo fails, you can use: paru -S upd72020x-fw Why do you need this? This package provides the firmware for Renesas uPD720201 / uPD720202 USB 3.0 chipsets. If you were seeing a warning like: ==> WARNING: Possibly missing firmware for module: xhci_pci ...then installing this will fix that warning during your mkinitcpio (kernel image) updates. Important Post-Install Step: Since this is firmware that needs to be loaded by the kernel at boot, you should regenerate your initramfs to make sure it's included: sudo mkinitcpio -P Wait for it to finish, then reboot. The Advisor's Check-in You’ve moved from OBS text outlines to hardware-level firmware. It looks like you're doing some system maintenance or trying to fix USB stability/warnings on your CachyOS install. One quick warning: This specific firmware is often hosted on web.archive.org in the PKGBUILD because the original Renesas source links are dead. If the download is slow or fails, just try the command again; it's a known quirk of this specific package. Did the installation go through, or did you hit a "404" or "Target not found" error?
