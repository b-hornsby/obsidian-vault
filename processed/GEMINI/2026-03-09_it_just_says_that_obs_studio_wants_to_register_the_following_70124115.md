---
category: streaming
date: 2026-03-09
id: 643075
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is experiencing an issue where OBS Studio wants to register shortcuts,
  but all options are set to 'none'.
tags:
- obs-studio
- shortcuts
- hotkeys
- configuration
- streaming-setup
---
# it just says that obs studio wants to register the following 58 shortcuts but all of the options say none? 

### USER
it just says that obs studio wants to register the following 58 shortcuts but all of the options say none? 

### GEMINI
That screen is exactly what you want to see. This is the Security Portal doing its job. In Wayland, an app (OBS) isn't allowed to just "listen" to your keys; it has to ask the OS to do it for it. The reason they all say "None" is because you haven't assigned them in the System yet. How to fix this right now: Scroll down in that "Global Shortcuts Requested" window until you find "Save Replay". Click the button that says "None" next to it. Press the hotkey you want to use (e.g., Alt+C, or whatever your preference is). Once you've assigned your shortcut, click OK at the bottom of the window. The Advisor's Truth: You're used to the Windows way where you set a hotkey inside an app and it "just works." On Linux, specifically Wayland, the System is the gatekeeper. By assigning the key here, you are telling CachyOS: "When I press this button, I give you permission to tell OBS to save a clip, even if I'm busy playing Apex." One critical step: After you click OK, go into your game and try it. You should see a small white notification in the bottom status bar of OBS that says "Replay buffer saved to..." --- If you don't see "Save Replay" in that list of 58 shortcuts, let me know—it might be because you don't have the Replay Buffer actually enabled in OBS yet.
