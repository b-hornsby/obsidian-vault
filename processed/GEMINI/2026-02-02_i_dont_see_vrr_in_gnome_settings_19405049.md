---
category: homelab
date: 2026-02-02
id: 096161
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to find VRR settings in GNOME and is stating that he cannot
  find them.
tags:
- gnome
- vrr
- display-settings
- linux
---
# i dont see vrr in gnome settings

### USER
i dont see vrr in gnome settings

### GEMINI
If you don’t see the VRR (Variable Refresh Rate) toggle in your settings, it’s because GNOME 49 still hides it behind an "experimental" flag unless your distro has pre-enabled it. Even though you're on the performance-focused CachyOS, you still have to tell the GNOME compositor (Mutter) to unlock that specific menu. 1. Enable the Hidden VRR Toggle Open your terminal and run this command: gsettings set org.gnome.mutter experimental-features "['variable-refresh-rate']" Crucial: You must Log Out and Log Back In (or reboot) for this to take effect. Once you log back in: Go to Settings > Displays. Select your primary monitor. Look for Refresh Rate. Underneath it, a new Variable Refresh Rate toggle should now appear. Turn it OFF. (As we discussed, this is the #1 way to stop the flickering when you multitask video and games on Wayland). 2. Why isn't it there already? If the command above doesn't make it appear, there are two likely reasons: The Cable: VRR on Linux is notoriously picky. If you are using HDMI, it often fails to register as VRR-capable on NVIDIA cards. Using a DisplayPort cable is almost mandatory for reliable VRR on Linux. Monitor Settings: Check your monitor's physical On-Screen Display (OSD) buttons. Ensure "FreeSync," "G-Sync," or "Adaptive Sync" is set to On at the hardware level. 3. The "Brutal Advisor" Check You said OBS flickered when you watched a stream in Discord while playing Arc Raiders. If you enable the VRR toggle and set it to "On," the flickering will likely get worse. The Strategy: Enable it using the command above just so you have the power to turn it off. By explicitly setting it to Off in the menu, you force the compositor to stay at a fixed refresh rate (e.g., 144Hz), which stops the "sync war" that causes the flicker in your recordings. Next step: Run that gsettings command and reboot. Does the "Variable Refresh Rate" toggle show up in your Display settings now?
