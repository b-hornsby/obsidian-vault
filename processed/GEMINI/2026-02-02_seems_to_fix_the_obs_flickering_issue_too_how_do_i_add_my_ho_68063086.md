---
category: streaming
date: 2026-02-02
id: 309945
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to add a hotkey to clip games in OBS, and it seems to be
  related to fixing a screen flickering issue.
tags:
- obs-studio
- replay-buffer
- keybinds
- game-clipping
- screen-flickering
---
# seems to fix the obs flickering issue too. how do i add my hotkey (its =) so i can press it to clip my games

### USER
seems to fix the obs flickering issue too. how do i add my hotkey (its =) so i can press it to clip my games

### GEMINI
Great that the reboot and portal cleanup fixed both the Vesktop and OBS flickering. That confirms the issue was indeed a hung PipeWire session manager. Regarding the hotkey for clipping: Vesktop (the Linux Discord app) does not support global hotkeys out of the box. Because it runs in an Electron container on Wayland, it cannot "listen" to your keyboard when you are focused on a game unless you specifically configure it. Here is how to set up your = key to clip: 1. Enable the Clipping Plugin First, make sure the feature is actually turned on in the app. Open Vesktop Settings. Go to Plugins. Search for "Clips". Enable it and click the Gear icon next to it. Note the default hotkey (usually Alt+C or Cmd+C). You can try changing it to = here, but it likely will not work while you are inside a game because of Wayland's security model. 2. The Wayland Workaround (The "Real" Fix) Since you are on GNOME, you need the system to tell Vesktop to take the clip. You have to map a global shortcut in GNOME that sends the keypress to Vesktop. Go to GNOME Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts. Create a new shortcut: Name: Discord Clip Command: vesktop -- --keybind 1 (Note: the ID for clipping is usually 1 or 2, you can verify this in the "Clips" plugin settings). Shortcut: Press your = key. 3. If you use OBS for Clipping (Recommended) Since you mentioned OBS flickering was also fixed, it is actually much more efficient to use OBS Replay Buffer for clipping on Linux than Discord's internal clipper. In OBS, go to Settings > Output > Replay Buffer and enable it. Go to Hotkeys, search for "Replay Buffer: Save Replay," and set it to =. In Settings > General, check "Automatically start replay buffer when streaming." The Advisor's Verdict Discord's clipping feature on Linux is notoriously resource-heavy and buggy. Since you're on CachyOS, you want efficiency. Using OBS's Replay Buffer will give you better quality, lower CPU usage, and your = hotkey will actually work every time because OBS handles global inputs much better on Wayland than Vesktop does. Would you like me to help you configure the OBS Replay Buffer so your clips save to a specific folder automatically?
