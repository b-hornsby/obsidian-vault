---
category: streaming
date: 2026-02-02
id: 357152
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is indicating that the OBS Studio interface doesn't show the 'start
  replay buffer' option, suggesting a configuration or installation issue.
tags:
- obs-studio
- replay-buffer
- streaming
- linux
---
# it doesnt say start replay buffer

### USER
it doesnt say start replay buffer

### GEMINI
If it doesn't say "Start Replay Buffer," it’s because you haven't enabled the feature in the settings yet. OBS hides the button until the "Buffer" is configured. Here is the direct fix to reveal the button: 1. Enable the Buffer Open Settings in OBS. Go to the Output tab. Look at the Output Mode at the top. If it says "Simple," change it to Advanced. Click the Replay Buffer tab (it’s the last one on the right in that row). Check the box: [X] Enable Replay Buffer. Set your Maximum Replay Time (e.g., 60 seconds). Click Apply and OK. Now look at your main OBS window. The button "Start Replay Buffer" will have appeared in the bottom right controls section, right under "Start Recording." 2. The "Encoder Busy" Trap If you enabled it but the button is greyed out or gives an error when you click it: Check your Recording settings: The Replay Buffer uses your Recording settings, not your Streaming settings. Go back to Settings > Output > Recording. Ensure the Video Encoder is actually set to NVIDIA NVENC H.264. If it's set to something your system doesn't support, the Replay Buffer will refuse to start. 3. Verification for CachyOS Since you are on CachyOS, if the encoder doesn't show up at all, run this to make sure the FFmpeg integration for NVENC is present: sudo pacman -S ffmpeg 4. The Logic Check You are setting this up to "clip." If you don't have a Hotkey set, the button is useless. Go to Settings > Hotkeys. Search for "Save Replay". Bind it (e.g., Ctrl + Shift + S). Crucial Warning: If you click "Start Recording" while the Replay Buffer is running, it’s fine. But if you only want clips, you only need the Replay Buffer running. It sits in your RAM and only writes to your SSD when you hit your hotkey. Would you like me to explain how to manage the RAM usage of the Replay Buffer so it doesn't choke your game's performance?
