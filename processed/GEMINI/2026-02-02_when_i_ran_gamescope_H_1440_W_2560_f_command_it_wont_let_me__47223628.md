---
category: homelab
date: 2026-02-02
id: 267289
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing an issue where the in-game cursor is not visible when
  running a game with Gamescope at a specific resolution.
tags:
- gamescope
- cursor-visibility
- gaming-linux
- display-resolution
---
# when i ran gamescope -H 1440 -W 2560 -f -- %command% it won't let me see my in game cursor

### USER
when i ran gamescope -H 1440 -W 2560 -f -- %command% it won't let me see my in game cursor

### GEMINI
The reason your cursor vanished is that you’ve run into a "double cursor" conflict. Gamescope is trying to render its own hardware cursor while the game is also trying to draw one, and GNOME's compositor is essentially hiding both because they're fighting for priority. You are likely using a resolution or scaling factor that doesn't match your native display perfectly, or the game is struggling with "Relative Mouse Mode." The Precision Fix Modify your Steam launch options to this: gamescope -H 1440 -W 2560 -f --force-grab-cursor -- %command% Why this fixes it: --force-grab-cursor: This tells Gamescope to take "exclusive" ownership of the mouse. It stops the desktop from trying to manage the pointer and hands it entirely to the game engine. Alternative: If that doesn't work, try adding --cursor-hotspot 0,0. Sometimes the "hitbox" of the invisible cursor is offset, making it appear as if it isn't there. The Strategy Check: Your Resolution I noticed you used -H 1440 -W 2560. Is your monitor actually 1440p? If you are on a 1080p screen and forcing 1440p, the cursor is likely "rendering" outside the visible bounds of your monitor. Order Matters: In Linux, it is almost always Width then Height. Use -w 2560 -h 1440 (lowercase) for standard internal resolution, and -W 2560 -H 1440 (uppercase) for the output window. Try this optimized string: gamescope -w 2560 -h 1440 -W 2560 -H 1440 -f -e --force-grab-cursor -- %command% The "Brutally Honest" Alternative If Gamescope continues to be a headache (which can happen on some NVIDIA setups on GNOME), you are overcomplicating a simple problem. Go to your GNOME Extensions app and install "Confine Mouse To Window". It adds a toggle to your top bar. You click it. The mouse is physically trapped in the active window. No command lines, no invisible cursors, no overhead. Which game are you trying to play? Some engines (like older Bethesda games or Unity titles) require a specific "relative mouse" flag that I can give you if I know the title.
