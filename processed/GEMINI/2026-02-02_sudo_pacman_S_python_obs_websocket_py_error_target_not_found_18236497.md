---
category: streaming
date: 2026-02-02
id: 838809
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to install python-obs-websocket-py via pacman and paru but
  the package could not be found.
tags:
- obs-websocket
- python
- package-installation
- paru
---
# ❯ sudo pacman -S python-obs-websocket-py
error: target not found: python-obs-websocket-py

~
❯ paru -S python-obs-websocket-py
:: Resolving dependencies...
error: could not find all required packages:
    python-obs-websocket-py (target)

~
❯ 

### USER
❯ sudo pacman -S python-obs-websocket-py
error: target not found: python-obs-websocket-py

~
❯ paru -S python-obs-websocket-py
:: Resolving dependencies...
error: could not find all required packages:
    python-obs-websocket-py (target)

~
❯ 

### GEMINI
This is the "Linux Moment" where the universe tests your resolve. The package name has changed in the AUR/Repos because of Python versioning. Let's stop guessing the package names and use the modern, standard library that replaced the one we've been trying. It's called obsws-python. 1. Install the correct library Since you're on CachyOS, the most reliable way is through the AUR using this specific name: paru -S python-obsws-python 2. Update the Script The code for this library is much cleaner. Re-edit your ~/clip.py: nano ~/clip.py Paste this in: import obsws_python as obs # Setup password = "YOUR_PASSWORD" # Your OBS websocket password try: cl = obs.ReqClient(host='localhost', port=4455, password=password) cl.save_replay_buffer() print("Clip Saved!") except Exception as e: print(f"Error: {e}") 3. Test it Run this: python ~/clip.py If paru fails again (The "Emergency Exit" Method) If the AUR package is being stubborn, we are going to use a Virtual Environment (venv). This is the "correct" Python way that works on any Linux distro without needing paru or pacman to cooperate: Create the environment: python -m venv ~/obs_env Install the library inside it: ~/obs_env/bin/pip install obsws-python Run your script using that specific Python: ~/obs_env/bin/python ~/clip.py Strategy Check If the paru command worked, you're golden. If not, the venv method in Step 3 is 100% foolproof because it doesn't rely on the Arch repositories at all—it downloads the library directly from the Python source. Which one did you go with? If the venv worked, your OpenDeck command is simply: # /home/toastedmel0n/obs_env/bin/python /home/toastedmel0n/clip.py
