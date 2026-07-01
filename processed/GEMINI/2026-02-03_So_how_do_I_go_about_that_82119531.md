---
category: general
date: 2026-02-03
id: 824381
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for instructions on how to do something, but the context
  is missing.
tags:
- context-dependent
- linux-troubleshooting
---
# So how do I go about that?

### USER
So how do I go about that?

### GEMINI
It appears CachyOS has specific quirks with how GNOME sessions are configured, and the standard gear icon isn't always available, as forum posts confirm your exact issue. We need to resolve the flickering caused by your RTX 3070 and Wayland (Mutter) configuration. Since we can't easily switch to Xorg via the GUI, we must resolve it within OBS or the underlying system. The Most Reliable Fix: Disable Hardware Acceleration This is the critical step for your specific setup. The flickering stops when the Browser Source stops fighting your NVIDIA drivers for rendering control. Open OBS. Navigate to Settings -> Advanced. In the Sources section, UNCHECK the option that says "Enable Browser Source Hardware Acceleration." Restart OBS completely. This offloads the simple rendering of the "now playing" overlay to your powerful i7 CPU, completely bypassing the Wayland/NVIDIA conflict that is causing the flickering. Alternative: Install a Specific Package If disabling acceleration doesn't work, you might be missing the specific package that enables a smooth X11 transition in GDM on CachyOS. You can try installing gnome-shell-x11 or similar session packages if they exist in the CachyOS repos, but that dives back into system configuration. Stick to the simplest path: Disable hardware acceleration in OBS. That is the quickest, most immediate fix for Wayland flickering on your hardware profile.
