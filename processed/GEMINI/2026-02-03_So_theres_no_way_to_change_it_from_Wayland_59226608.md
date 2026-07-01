---
category: homelab
date: 2026-02-03
id: 193683
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if it's possible to switch from the Wayland display server
  to another one, likely X11.
tags:
- wayland
- x11
- display-server
- linux-desktop
---
# So there’s no way to change it from Wayland?

### USER
So there’s no way to change it from Wayland?

### GEMINI
There is a way, but your current system configuration is rejecting the "hard switch" because of how CachyOS and NVIDIA interact during the boot process. When you edited that file, you essentially broke the "handshake" between your GPU and the display manager. If you are determined to leave Wayland, you have to do it through the Login Screen (GDM) rather than a permanent configuration file, but we have to get you back to a working desktop first. 1. Get Back to Your Desktop (Immediate Priority) You must undo the change that caused the freeze. Press Ctrl + Alt + F3 to open the TTY (text console). Log in with your username and password. Run sudo nano /etc/gdm/custom.conf and put the # back in front of WaylandEnable=false. Save (Ctrl+O, Enter) and exit (Ctrl+X), then type sudo reboot. 2. The Proper Way to Switch (Without Breaking the Boot) Once you are back at the normal login screen (the one with your profile picture), the "Gear Icon" is the only safe way to switch. If it's missing, it's usually because NVIDIA Modesetting isn't enabled, which makes GDM think your card can't handle Xorg properly. Instead of fighting the OS to switch to X11, you should address the reason you want to switch: the OBS flickering. 3. The "Wayland-Safe" OBS Strategy If you stay on Wayland (which is generally better for modern CachyOS performance), you can stop the flickering with one click: The Fix: Open OBS -> Settings -> Advanced. The Action: Uncheck "Enable Browser Source Hardware Acceleration". The Result: This stops the NVIDIA/Wayland sync conflict that causes the flickering in your "Now Playing" overlay. Are you back at the desktop yet? If you are, open OBS and let's try the "Hardware Acceleration" fix first—it's much safer than risking another system freeze by forcing X11.
