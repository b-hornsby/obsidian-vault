---
id: 572553
source: GEMINI
date: 2026-02-02
tags: ['stream-deck', 'opendeck', 'keybind-mapping', 'hotkey', 'streaming-tools']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was trying to map an Alt+Shift keybind as a button on his Stream Deck using the OpenDeck software.
---
# how do i make my keybind a button via opendeck for stream deck? my keybind is alt + shift 

### USER
how do i make my keybind a button via opendeck for stream deck? my keybind is alt + shift 

### GEMINI
To make this work on a Stream Deck, you need to understand one thing: Stream Deck hotkeys usually require a "base" key (like a letter, number, or function key). You can't typically bind just modifiers like Alt + Shift alone because they don't actually trigger an action in most software—they just modify one. If you are committed to Alt + Shift, you'll likely run into "phantom" triggers or it simply won't fire. Here is the objectively better way to set this up. Option 1: The Proper "Hotkey" Method (Recommended) Don't use just modifiers. Go back to OBS and change your "Save Replay" keybind to something unique like Alt + Shift + S or a Function key you don't use (like F10). Then: Open the Stream Deck software. On the right-hand side, look for the System category. Drag the Hotkey action onto an empty button. Click the Hotkey field at the bottom. Press your combination (e.g., Alt + Shift + S) on your keyboard. Pro Tip: If you have trouble recording it, click the 'v' arrow next to the input box and manually check the boxes for Alt and Shift, then type 'S'. Option 2: The Direct OBS Integration (Fastest) The Elgato Stream Deck has a native OBS plugin that is far more reliable than "simulated" keypresses because it talks directly to OBS through a websocket. In Stream Deck, find the OBS Studio category. (If it's not there, click the "Keyboard" icon/Store button and install the OBS Studio by Elgato plugin). Drag the Replay Buffer action onto a button. In the "Action" dropdown at the bottom, select Save. The Result: You don't even need a keyboard keybind anymore. This button will trigger the internal OBS command directly, which is less likely to be blocked by "exclusive mode" games or admin-level permissions. Why Your Current Plan is Weak If you insist on just Alt + Shift, you're asking for trouble. Many games use Shift for sprinting and Alt for inventory or menus. If you hit that button, you might accidentally trigger an in-game action while trying to save a clip. Using a dedicated F-key or the Direct OBS Integration (Option 2) eliminates the risk of your hardware conflicting with your gameplay. Next Step: Once you have the button working, would you like me to show you how to set up a "Multi-Action" that saves the clip AND automatically posts a "Clip Saved!" message in your Twitch/Discord chat?
