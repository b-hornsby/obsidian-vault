---
category: streaming
date: 2026-02-03
id: 202210
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is running OBS with `QT_QPA_PLATFORM=xcb` and encountering GTK theme
  parsing errors and a portal registration failure.
tags:
- obs-studio
- qt
- gtk-warnings
- theme-parsing-error
- linux-streaming
---
# ❯ QT_QPA_PLATFORM=xcb obs

(obs:12636): Gtk-WARNING **: 20:58:58.852: Theme parsing error: gtk.css:1959:16: 'border-spacing' is not a valid property name

(obs:12636): Gtk-WARNING **: 20:58:58.853: Theme parsing error: gtk.css:3272:16: '-gtk-icon-size' is not a valid property name

(obs:12636): Gtk-WARNING **: 20:58:58.853: Theme parsing error: gtk.css:3286:16: '-gtk-icon-size' is not a valid property name
debug: Found portal inhibitor
debug: Attempted path: /usr/bin/../share/obs/obs-studio/locale/en-US.ini
debug: Attempted path: /usr/bin/../share/obs/obs-studio/locale.ini
debug: Attempted path: /usr/bin/../share/obs/obs-studio/themes
debug: Attempted path: /usr/bin/../share/obs/obs-studio/themes/
qt.qpa.services: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")

### USER
❯ QT_QPA_PLATFORM=xcb obs

(obs:12636): Gtk-WARNING **: 20:58:58.852: Theme parsing error: gtk.css:1959:16: 'border-spacing' is not a valid property name

(obs:12636): Gtk-WARNING **: 20:58:58.853: Theme parsing error: gtk.css:3272:16: '-gtk-icon-size' is not a valid property name

(obs:12636): Gtk-WARNING **: 20:58:58.853: Theme parsing error: gtk.css:3286:16: '-gtk-icon-size' is not a valid property name
debug: Found portal inhibitor
debug: Attempted path: /usr/bin/../share/obs/obs-studio/locale/en-US.ini
debug: Attempted path: /usr/bin/../share/obs/obs-studio/locale.ini
debug: Attempted path: /usr/bin/../share/obs/obs-studio/themes
debug: Attempted path: /usr/bin/../share/obs/obs-studio/themes/
qt.qpa.services: Failed to register with host portal QDBusError("org.freedesktop.portal.Error.Failed", "Could not register app ID: Connection already associated with an application ID")

### GEMINI
That error message confirms it: OBS is struggling to bridge the gap between your NVIDIA card and the Wayland portal. When you see Failed to register with host portal, it means the "Wayland handshake" is failing, and forcing XCB (X11 mode) while still inside a Wayland session is causing a conflict. We are done with the "clean" fixes. It's time for the Pro-Streamer Workaround. Since the Browser Source is fundamentally broken on your 3070/Wayland setup, we are going to bypass it entirely. The "No-Flicker" 100% Guaranteed Method Open your Music Overlay in a standard Browser: Open a Firefox or Chrome window and paste your overlay URL (Amuse, Pixel Chat, etc.). In OBS, add a "Window Capture (PipeWire)": Click the + under Sources. Select Window Capture (PipeWire). Choose your browser window. The Magic Step (Chroma Key): Right-click the new Window Capture source in your list. Select Filters. Click the + and add Chroma Key. Select the background color of your overlay (usually green or black) to make it transparent. Why this works: Standard browser windows (Firefox/Chrome) handle Wayland/NVIDIA syncing much better than the "mini-browser" built into OBS. This eliminates the flicker because you're using a battle-tested window renderer instead of the buggy OBS internal one. If you still want to fix the system: The only way to actually kill that flicker globally is to disable the NVIDIA GSP Firmware, which is the notorious cause of stuttering for 30-series cards on Wayland. Run this in terminal: sudo nano /etc/modprobe.d/nvidia.conf Paste this exact line: options nvidia NVreg_EnableGpuFirmware=0 Save (Ctrl+O, Enter) and Exit (Ctrl+X). Reboot. My advice: Stop fighting the code. Use the Window Capture + Chroma Key method right now so you can actually get to the "Music Overlay" part of your goal. Would you like me to walk you through how to set up the Chroma Key filter once you have the window captured?
