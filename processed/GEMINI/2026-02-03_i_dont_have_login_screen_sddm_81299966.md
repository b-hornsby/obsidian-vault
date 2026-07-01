---
category: homelab
date: 2026-02-03
id: 533367
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan doesn't have an SDDM login screen on CachyOS and needs help getting
  it working.
tags:
- sddm
- display-manager
- login-screen
- cachyos
- kde
---
# i dont have login screen sddm

### USER
i dont have login screen sddm

### GEMINI
If you don’t see Login Screen (SDDM) in that list, it’s usually because the sddm-kcm (KDE Control Module for SDDM) package is missing from your system. It’s a common oversight in "minimal" or custom CachyOS installs. You're trying to fix a problem with a tool you don't even have installed. Let's stop guessing and get the right tools on the field. 1. Install the Missing Module Open your terminal and run: sudo pacman -S sddm-kcm Once that's done, close and reopen System Settings. The Login Screen (SDDM) option will now appear in that sidebar between System Sounds and Splash Screen. 2. The Direct Root Fix (No GUI required) If you want to be efficient and skip the "Apply settings" button entirely, you can manually tell SDDM which monitor is primary. The flipping happens because SDDM doesn't know your layout. Run this command to see your monitor names: wlr-randr --list (If wlr-randr isn't found, use kscreen-doctor -o). Look for your main monitor name (like DP-1 or HDMI-A-1). Then, create the configuration file that forces the layout: sudo nano /etc/sddm.conf.d/monitors.conf Add this (replace DP-1 with your actual primary monitor name): [X11] DisplayCommand=/usr/bin/xrandr --output DP-1 --primary 3. The "Unfiltered" Strategy If you're on CachyOS, you're likely using Wayland. The reason it "flips" is often because the secondary monitor responds to the GPU initialization a fraction of a second faster than your primary. SDDM sees the first "live" screen and throws the password box there, then panics when the second one wakes up. If installing sddm-kcm and hitting "Apply" doesn't work, you are wasting time fighting a GUI that can't handle the hardware handshake. The only "high-level" fix is to force SDDM to run on Wayland specifically (as I detailed in the previous response). Which one do you want to do: install the missing GUI module first, or should we just go straight to the config files and force it manually?
