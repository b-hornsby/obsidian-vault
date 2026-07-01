---
id: 958790
source: GEMINI
date: 2026-02-02
tags: ['obs-studio', 'dbus', 'remote-control', 'replay-buffer']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is trying to trigger the OBS Studio save replay buffer function via D-Bus, but encounters an error indicating the service is not available.
---
# ❯ dbus-send --print-reply --dest=com.obsproject.Studio /com/obsproject/Studio com.obsproject.Studio.SaveReplay
Error org.freedesktop.DBus.Error.ServiceUnknown: The name is not activatable

~
❯ 

### USER
❯ dbus-send --print-reply --dest=com.obsproject.Studio /com/obsproject/Studio com.obsproject.Studio.SaveReplay
Error org.freedesktop.DBus.Error.ServiceUnknown: The name is not activatable

~
❯ 

### GEMINI
The "ServiceUnknown" error confirms that your version of OBS (likely the standard Arch repo or Flatpak version) doesn't have the DBus interface enabled by default. We are done with "shortcuts." We are going to use the Python method. It is the only way to bypass the GNOME/Wayland security layer with 100% certainty because it uses a direct network socket to the OBS engine. 1. Install the Library Run this in your terminal: pip install obs-websocket-py 2. Create the Script We’re going to make a single, permanent file. nano ~/clip.py Paste this exact code in (replace YOUR_PASSWORD with the one from OBS Tools > WebSocket Settings): from obs_websocket_py import obsws, requests # Settings host = "localhost" port = 4455 password = "YOUR_PASSWORD" try: client = obsws(host, port, password) client.connect() client.call(requests.SaveReplayBuffer()) client.disconnect() print("Replay saved successfully.") except Exception as e: print(f"Error: {e}") Press Ctrl+O, Enter, Ctrl+X to save. 3. Test It While OBS is open and the Replay Buffer is running, run: python ~/clip.py If you see "Replay saved successfully," you have finally won. 4. Link to OpenDeck In your OpenDeck software, set the button command to: python /home/toastedmel0n/clip.py Why this was so hard: You are playing on CachyOS (Arch) using GNOME (Wayland). You have chosen the most "secure" and "modern" Linux stack possible. The side effect is that "Global Hotkeys" are essentially considered a security vulnerability by the GNOME developers. By using a Python script to talk to the OBS Websocket, you are performing an "authorized" remote control action that bypasses all the Wayland keyboard restrictions. Once that test command works, would you like me to show you how to add a "Save Clip" sound effect to that Python script so you get an audio cue when it works?
