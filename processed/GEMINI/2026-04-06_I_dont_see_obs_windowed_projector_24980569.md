---
category: streaming
date: 2026-04-06
id: 612084
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was unable to find the windowed projector option in OBS and needed
  help locating it.
tags:
- obs
- windowed-projector
- troubleshooting
- ui
---
# I don’t see obs windowed projector

### USER
I don’t see obs windowed projector

### GEMINI
The reason you don’t see it is that the Aitum Vertical plugin has its own separate canvas that behaves differently than the main OBS window. To find the projector for your vertical setup, you have to right-click in a very specific spot. 1. Where to find the Vertical Projector Don't right-click the main OBS preview. Instead: Go to the Vertical Sources or Vertical Scenes dock (the one Aitum added). Right-click on the specific Vertical Scene you want to send to TikTok. In that menu, you will see Windowed Projector (Scene). Click that, and a vertical window will pop out. This is your "clean" feed. 2. The "Lag-Free" Capture in TikTok Studio Now that you have that window open, here is how you capture it without the "Virtual Camera" stutter: Open TikTok Live Studio (as Administrator). Add a new source -> Window Capture. Select the window named "Windowed Projector (Scene) - [Your Scene Name]". Critical for CS2: Look for the Capture Method setting in TikTok Studio. Change it from "Auto" to Windows 10 (Graphics Capture). This is a much "thinner" way to grab video than the Virtual Camera and won't fight CS2 for GPU priority as hard. 3. The "Advisor" Performance Tweak Since you’re playing CS2, frame timing is everything. If you still feel "micro-stutters," do this: Limit your CS2 FPS: If your monitor is 144Hz, cap your game at 144 or 160. If you let CS2 run at 400+ FPS, it will starve OBS and TikTok of the GPU resources they need to process that "Windowed Projector," causing the lag you're seeing. Minimize OBS: Once the projector is open and TikTok is capturing it, minimize the main OBS window. This stops OBS from rendering the preview twice (once in the main window and once in the projector), saving your 3070 a significant amount of work. Why this is better than what you were doing: The Virtual Camera is a software driver that sits between OBS and Windows. It’s slow. A Windowed Projector is a direct "draw" from your GPU memory. By capturing that window in TikTok Studio using the "Graphics Capture" method, you are using the same high-speed tech that Discord uses to share screens, which is significantly more efficient for high-motion gaming. Try the Right-click on the Vertical Scene trick—it’s hidden in the plugin's sub-menus!
