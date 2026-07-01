---
category: streaming
date: 2026-04-06
id: 338102
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was sharing what options appeared when right-clicking an OBS scene,
  trying to troubleshoot a missing feature.
tags:
- obs
- right-click-menu
- scene
- ui
- troubleshooting
---
# This is all I see when I right click the scene

### USER
This is all I see when I right click the scene

### GEMINI
The Aitum plugin handles projectors differently than standard OBS scenes, which is why that menu looks sparse. Since the "Windowed Projector" option isn't appearing in that specific right-click menu, we’ll use the Vertical Canvas itself. The Fix: How to Project the Vertical Canvas Instead of right-clicking the text name "fps games," try this: Right-click anywhere on the actual Vertical Preview/Canvas (where you see your CS2 character). Look for "Windowed Projector (Canvas)". Once that window pops up, go to TikTok Live Studio and add it via Window Capture. The "Brutally Honest" Plan B (If Projector fails) If you still can't find that option or if it's still laggy, you are hitting a classic "software bottleneck." You have a powerful 3070, but you're asking it to run a heavy game (CS2), a high-end recording suite (OBS), and a bloated mobile-port app (TikTok Studio) all at once. Stop fighting the software and do this instead: Lower your CS2 Resolution: If you're playing at 1080p or 1440p, drop it slightly or use NVIDIA Image Scaling (NIS). This frees up the specific GPU "cycles" OBS needs to hand the video over to TikTok. The "Virtual Camera" Secret Fix: Go back to the Virtual Camera method (the orange button in your photo). DO NOT click it yet. Click the Gear Icon next to it. Make sure the output is set to "Vertical Canvas" and not "Internal OBS." The Life-Saver: Lower the Virtual Camera Resolution in those settings to 720p. TikTok mobile users physically cannot see the difference between 720p and 1080p on a phone screen. This will instantly drop the lag in CS2. The Advisor's Cold Truth You're playing a game where every millisecond of input lag matters. By "projecting" or "virtually camming" into TikTok Studio, you're creating a feedback loop. If 720p doesn't fix the lag: You need to stop using TikTok Live Studio. Since Restream "revoked" you, look into Starscape or Prism Live Studio. They are often much lighter on resources than TikTok's official (and very poorly optimized) software. Did lowering the Virtual Camera resolution to 720p change the "feel" of your CS2 movement?
