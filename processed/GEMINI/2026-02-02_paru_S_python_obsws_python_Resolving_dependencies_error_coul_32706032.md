---
category: streaming
date: 2026-02-02
id: 225211
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to install python-obsws-python using paru but encountering
  a dependency error, likely for OBS automation.
tags:
- arch-linux
- package-management
- paru
- python-obsws-python
- obs-websocket
- streaming-automation
---
# ❯ paru -S python-obsws-python
:: Resolving dependencies...
error: could not find all required packages:
    python-obsws-python (target)

~
❯ 

### USER
❯ paru -S python-obsws-python
:: Resolving dependencies...
error: could not find all required packages:
    python-obsws-python (target)

~
❯ 

### GEMINI
This is the final straw for the AUR. We are officially abandoning the Arch repositories for this specific task. They are out of sync with your Python version, and it's wasting your time. We are going with the Emergency Exit (venv) method. This is the "professional" way to handle Python on Linux—it creates a private, isolated container for this one script so it doesn't care about CachyOS's global packages or paru errors. 1. Create the Environment Run this in your terminal: python -m venv ~/obs_env 2. Install the Library (Inside the Container) This bypasses the pip block and the AUR entirely: ~/obs_env/bin/pip install obsws-python 3. Create the Final Script nano ~/clip.py Paste this in: import obsws_python as obs # Change this to your actual OBS Websocket password password = "YOUR_PASSWORD" try: cl = obs.ReqClient(host='localhost', port=4455, password=password) cl.save_replay_buffer() print("Clip Saved!") except Exception as e: print(f"Error: {e}") 4. The "God-Tier" Test Run this exact command: ~/obs_env/bin/python ~/clip.py If OBS shows "Replay Saved," we have finally killed the dragon. 5. Finalize the OpenDeck Button Don't use python or pgup. Set your OpenDeck button to run this exact path: /home/toastedmel0n/obs_env/bin/python /home/toastedmel0n/clip.py The Advisor's Post-Mortem Look at what we just did. We built a custom remote-control bridge because GNOME Wayland refused to let you press a button. This is why people call Linux "the hard mode" of gaming. But now? Your clipping is un-killable. It doesn't rely on hotkeys, it doesn't rely on focus, and it doesn't rely on Arch maintainers updating a package. Does that test command finally give you the "Clip Saved" success in OBS?
