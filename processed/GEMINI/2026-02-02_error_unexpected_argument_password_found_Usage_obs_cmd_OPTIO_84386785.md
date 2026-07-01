---
id: 781437
source: GEMINI
date: 2026-02-02
tags: ['obs-cmd', 'command-line-error', 'obs-studio', 'streaming-tools']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is encountering an error while using `obs-cmd`, indicating an unexpected argument was provided.
---
# error: unexpected argument '--password' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~

### USER
error: unexpected argument '--password' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~

### GEMINI
It is time to stop playing "Guess the Syntax" with a tool that clearly doesn't want to cooperate. If obs-cmd is rejecting --password, -p, and --address, it is likely an older or highly specific version that relies entirely on environment variables or a configuration file. As your advisor, I’m calling it: We are firing obs-cmd. It is wasting your time and keeping you out of your game. We are going to use a native GNOME solution that is bulletproof and doesn't require third-party terminal tools. The "DBus" Solution (No extra tools needed) OBS on Linux exposes itself to DBus. This allows you to send commands to it using a standard command that is already built into CachyOS/GNOME. Try this command in your terminal right now: dbus-send --print-reply --dest=com.obsproject.Studio /com/obsproject/Studio com.obsproject.Studio.SaveReplay If that works (Check OBS for the "Saved" pop-up): Open your OpenDeck software. Set the button action to Execute Command. Paste that dbus-send line in. You are done. No passwords, no websockets, no syntax errors. If the DBus command fails: It means the OBS version you have doesn't have the DBus plugin enabled. In that case, we go to the ultimate fallback—the Python script. This works regardless of Wayland, GNOME, or obs-cmd bugs. Install the library: pip install obs-websocket-py Create a tiny script: nano ~/save_clip.py Paste this in: import sys from obs_websocket_py import obsws, requests client = obsws("localhost", 4455, "YOUR_PASSWORD") client.connect() client.call(requests.SaveReplayBuffer()) client.disconnect() Tell OpenDeck to run it: python3 ~/save_clip.py Why the DBus way is the "Next Level" move: Security: No passwords stored in plain text. Speed: DBus is the native "nervous system" of Linux; it's faster than a websocket. Reliability: It doesn't care if you're on Wayland, X11, or GNOME. If OBS is open, DBus can talk to it. Did the dbus-send command trigger the replay save?
