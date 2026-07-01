---
id: 553312
source: GEMINI
date: 2026-02-02
tags: ['vesktop', 'discord-client', 'configuration', 'json-settings']
category: general
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is inspecting the Vesktop settings file, likely to understand or modify its configuration.
---
# ❯ cat ~/.config/vesktop/settings.json
{
    "discordBranch": "stable",
    "minimizeToTray": false,
    "arRPC": true,
    "splashColor": "rgb(220, 220, 223)",
    "splashBackground": "rgb(44, 45, 50)",
    "hardwareAcceleration": false
}⏎                                                                                                                      
~
❯ 

### USER
❯ cat ~/.config/vesktop/settings.json
{
    "discordBranch": "stable",
    "minimizeToTray": false,
    "arRPC": true,
    "splashColor": "rgb(220, 220, 223)",
    "splashBackground": "rgb(44, 45, 50)",
    "hardwareAcceleration": false
}⏎                                                                                                                      
~
❯ 

### GEMINI
Your settings.json confirms you've already disabled Hardware Acceleration, yet you're still flickering. This means the problem isn't your GPU rendering the UI—it's the PipeWire stream itself or how the portals are negotiating the frame capture. Since the useElectronCapturer key is missing from your JSON, your Vesktop is likely defaulting to the internal Electron method, which is the "flicker king" on Wayland. 1. Manual Injection of the Fix We are going to force Vesktop to use the system's native portal by manually editing that config. Close Vesktop completely (ensure no background processes are running). Open the file: nano ~/.config/vesktop/settings.json Edit it to look exactly like this: { "discordBranch": "stable", "minimizeToTray": false, "arRPC": true, "splashColor": "rgb(220, 220, 223)", "splashBackground": "rgb(44, 45, 50)", "hardwareAcceleration": false, "useElectronCapturer": false } (Note the comma added after the hardwareAcceleration line). 4. Save and exit (Ctrl+O, Enter, Ctrl+X). 2. The "Portal" Conflict (The CachyOS Special) CachyOS often installs multiple desktop portals. If xdg-desktop-portal-wlr (for Hyprland/Sway) is installed alongside xdg-desktop-portal-gnome, GNOME 49 can get confused about which one should handle the screen buffer, leading to flicker. Run this: pacman -Qs xdg-desktop-portal If you see xdg-desktop-portal-wlr, remove it: sudo pacman -R xdg-desktop-portal-wlr (Don't worry, you only need this if you use Sway or Hyprland). 3. Clear the PipeWire State Sometimes the PipeWire stream gets "stuck" in a bad state after a flicker loop. Reset the audio/video session managers: systemctl --user restart pipewire wireplumber xdg-desktop-portal-gnome The Advisor's Verdict You are running a performance-tuned OS (CachyOS) but your configuration is currently "headless" regarding the screen capturer. By adding "useElectronCapturer": false, you stop Vesktop from trying to be "smart" and force it to let GNOME handle the video stream. If you do this and the flicker persists, the issue is your Kernel/Mesa version mismatching with GNOME 49's new frame-scheduling. Next step: Manually add that line to your JSON and restart. When you click "Share Screen," does a system popup (GNOME's native window) ask you which screen to share? (It should).
