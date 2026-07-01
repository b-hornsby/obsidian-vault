---
category: homelab
date: 2026-02-03
id: 809510
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan tried to switch from GDM to a plasma login manager but the service
  name was incorrect.
tags:
- gdm
- sddm
- display-manager
- cachyos
- systemd
- kde
---
# ❯ sudo systemctl disable gdm
  sudo systemctl enable plasma-login-manager
Removed '/etc/systemd/system/display-manager.service'.
Failed to enable unit: Unit plasma-login-manager.service does not exist

~
❯ 

### USER
❯ sudo systemctl disable gdm
  sudo systemctl enable plasma-login-manager
Removed '/etc/systemd/system/display-manager.service'.
Failed to enable unit: Unit plasma-login-manager.service does not exist

~
❯ 

### GEMINI
That failed because CachyOS literally just made a massive change to their system 9 days ago (January 24, 2026). They have officially replaced the old login manager (sddm) with a new one called Plasma Login Manager. The package name and the service name are slightly different than what I gave you. Here is the corrected path to get into KDE. 1. Install the New Login Manager Run this to get the specific CachyOS package for the new manager: sudo pacman -S plasma-login-manager 2. Enable the New Service The service name isn't "plasma-login-manager," it's just plasmalogin. Run these commands in order: sudo systemctl disable gdm sudo systemctl enable plasmalogin 3. The "Wait, it's Empty" Check (One Last Time) Since you are switching desktops, CachyOS might try to default you back to Wayland. If you want X11 (The safest for NVIDIA): Once you reboot and see the new login screen, look for a "Desktop Session" or "Session Type" menu. Select Plasma (X11). OBS Fix: On X11, your flickering will almost certainly be gone without any further hacking. The "Clean" Cleanup Once you are inside KDE and everything is working, CachyOS recommends removing the old SDDM components to avoid conflicts with the new manager: sudo pacman -R sddm-kcm cachyos-themes-sddm sddm (Only do this after you have successfully logged into KDE). Go ahead and run sudo systemctl enable plasmalogin now. If that works, you are ready to reboot and finally leave the flickering behind. One final advisor note: If the login screen is black after rebooting, don't panic. Press Ctrl + Alt + F2 to get a terminal, log in, and we can fix it from there. But with the plasmalogin service, it should be smooth. Ready to reboot?
