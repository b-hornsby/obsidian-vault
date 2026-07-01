---
category: streaming
date: 2026-02-02
id: 819289
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was reporting that OBS replay buffer was not starting automatically
  when he launched the application.
tags:
- obs-studio
- replay-buffer
- streaming-software
---
# mine didnt start replay buffer when i launced

### USER
mine didnt start replay buffer when i launced

### GEMINI
If you followed the "Desktop Entry" steps and the Replay Buffer isn't active on launch, there are three likely culprits. Let’s stop guessing and fix it. 1. The "Simple Mode" Block If OBS is still set to Simple output mode, it sometimes ignores the --startreplaybuffer flag because it hasn't initialized the buffer settings properly. The Fix: Ensure Settings > Output > Output Mode is set to Advanced and that the Enable Replay Buffer box is checked. If it’s not checked in the settings, the command line flag is trying to start a feature that is technically "turned off." 2. The Command Line Audit Let’s see if the flag actually works on your specific build of OBS. Close OBS completely. Open your terminal. Type: obs --startreplaybuffer Watch the terminal output. * If OBS opens and the button says "Stop Replay Buffer," the flag is fine, but your shortcut is wrong. If it says Unknown option 'startreplaybuffer', then the version of OBS in the CachyOS repo has changed its flag syntax (unlikely, but possible). If you see Encoder Errors in the terminal, it means it tried to start but your GPU rejected the settings. 3. The Desktop Entry Mistake If it worked in the terminal (Step 2) but doesn't work when you click the icon, you likely edited the wrong .desktop file or have a duplicate. Run this to see which file is actually being used: which obs (should be /usr/bin/obs) In your terminal, run: nano ~/.local/share/applications/com.obsproject.Studio.desktop Ensure the Exec line looks exactly like this: Exec=obs --startreplaybuffer Note: If there are multiple Exec lines in the file (one for "Window" etc.), change the first one under the [Desktop Entry] header. 4. The "Path" Trap (CachyOS specific) CachyOS sometimes uses a wrapper or a specific binary name. Try changing the Exec line to the absolute path: Exec=/usr/bin/obs --startreplaybuffer Strategy Check: Is it actually worth the effort? If you can't get the shortcut to work, don't waste an hour on it. Alternative: Open OBS, go to Settings > General, and look for the Output section. There is a checkbox that says: "Automatically start replay buffer when streaming" The Blind Spot: If you aren't a streamer and just want it for clips while gaming, this built-in setting won't help you. You must use the command line flag or click it manually. Does the terminal output show any errors when you run obs --startreplaybuffer? If it mentions "NVENC" or "Device failed," your settings are too high for the driver to initialize.
