---
category: homelab
date: 2026-02-03
id: 660900
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that his KDE CachyOS login screen flips between his two
  monitors instead of staying on the main monitor.
tags:
- kde
- cachyos
- login-screen
- multi-monitor
- display-settings
---
# why when i log into my kde cachyos the password screen flips between my two monitors sometimes?

### USER
why when i log into my kde cachyos the password screen flips between my two monitors sometimes?

### GEMINI
This behavior is a known quirk (and occasional bug) in the interaction between SDDM (the login manager) and KWin (the window manager), particularly on Wayland and CachyOS. Your login screen and your desktop session are two different environments. When you boot up, SDDM hasn't yet "synced" with your personal desktop preferences. It's essentially guessing which monitor you want to type on, or it's trying to display the password field on all active screens simultaneously. Here is the "advisor" take: you’re likely seeing this because of a configuration mismatch or a specific bug in KDE Plasma 6.x. Here is how to fix it. 1. The "Sync" Fix (Easiest) KDE has a built-in feature to "push" your desktop monitor settings to the login screen. Go to System Settings > Colors & Themes > Login Screen (SDDM). Click the Apply Plasma Settings... button at the bottom right. Enter your password when prompted. Restart. This tells SDDM to mirror your current monitor layout (which one is primary, etc.). 2. The Wayland "Greeter" Bug If you are on Wayland (which CachyOS defaults to), there is a reported bug where the password field "jumps" to the secondary monitor the second you start typing. The Cause: SDDM often runs on X11 by default even if your desktop is Wayland. When it detects input, it can get confused about focus priority between the two screens. The Fix: Force SDDM to run on Wayland. Edit (or create) /etc/sddm.conf.d/10-wayland.conf. Add the following: [General] DisplayServer=wayland GreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell [Wayland] CompositorCommand=kwin_wayland --no-lockscreen --no-global-shortcuts --locale1 3. Check for Refresh Rate Mismatch If your two monitors have different refresh rates (e.g., one is 144Hz and the other is 60Hz), the GPU driver can sometimes "flicker" the signal as it tries to initialize both during the handoff from the BIOS to the login manager. Test: Temporarily set both monitors to 60Hz in System Settings, apply them to SDDM (Step 1), and see if the flipping stops. If it does, your GPU is struggling with the initial mode-setting. 4. Direct X11 Workaround If you are using X11, you can explicitly define the primary monitor in your Xorg config so SDDM doesn't have to guess. Run xrandr to find your primary display name (e.g., DP-1). Create a file at /etc/X11/xorg.conf.d/10-monitor.conf and specify: Section "Monitor" Identifier "DP-1" Option "Primary" "true" EndSection Advisor's Bottom Line: You are likely dealing with a "race condition" where the login manager is trying to grab focus before the second monitor is fully initialized by the driver. If the "Apply Plasma Settings" trick doesn't work, switching SDDM to Wayland (Step 2) is your best bet for a modern CachyOS install. Would you like me to walk you through the terminal commands to create that Wayland config file safely?
