---
category: streaming
date: 2026-02-02
id: 905265
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install the obs-websocket-py Python package using pip,
  but the command is not recognized in his fish shell.
tags:
- python
- package-management
- pip
- obs-websocket
- fish-shell
---
# ❯ pip install obs-websocket-py
fish: Unknown command: pip

~
❯ 

### USER
❯ pip install obs-websocket-py
fish: Unknown command: pip

~
❯ 

### GEMINI
Since you're on CachyOS, you're likely using Python 3.12+, which implements PEP 668. This means you can't just pip install things globally because it might break your system's package manager. CachyOS (rightfully) blocks it. We are going to use the official Arch Linux package for this library so pacman can manage it safely. 1. Install the library via Pacman Run this command: sudo pacman -S python-obs-websocket-py (If that isn't found, use paru -S python-obs-websocket-py). 2. Verify and Create the Script Now that the library is installed the "clean" way, create that script again: nano ~/clip.py Paste this in: import obs_websocket_py.obsws as obsws import obs_websocket_py.requests as requests # Change this to your actual OBS Websocket password password = "YOUR_PASSWORD" try: client = obsws("localhost", 4455, password) client.connect() client.call(requests.SaveReplayBuffer()) client.disconnect() print("Success: Clip Saved.") except Exception as e: print(f"Failed: {e}") 3. Test it in Fish Run: python ~/clip.py 4. The OpenDeck Step Once that terminal command works, put this into your OpenDeck button: python /home/toastedmel0n/clip.py Advisor’s Brutal Reality Check You’re experiencing the "Linux Desktop Tax." On Windows, this is a 2-second hotkey bind. On GNOME Wayland, it's a cross-layered engineering project involving Python libraries, websocket protocols, and environment security. You've spent this much time on it—don't quit now. You are one pacman command away from never having to worry about GNOME's hotkey restrictions again. Did the pacman -S command go through? Let's get this clip saved.
