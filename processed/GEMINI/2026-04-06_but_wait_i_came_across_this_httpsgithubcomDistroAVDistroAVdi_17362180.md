---
id: 175791
source: GEMINI
date: 2026-04-06
tags: ['distroav', 'ndi', 'obs-plugin', 'github-research']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan found a DistroAV GitHub discussion that might help with his NDI/OBS streaming setup.
---
# but wait. i came across this: https://github.com/DistroAV/DistroAV/discussions/831

### USER
but wait. i came across this: https://github.com/DistroAV/DistroAV/discussions/831

### GEMINI
The GitHub discussion you found highlights a known limitation: Aitum Vertical and NDI (DistroAV) don't always talk to each other correctly by default. Because Aitum uses a "secondary canvas" rather than a standard OBS Scene, the NDI plugin often doesn't "see" it as a source it can broadcast. If you are stuck using TikTok Live Studio as your "receiver," here is the most efficient way to bridge that gap without the lag of the Virtual Camera. 1. The "Filter" Workaround (Most Reliable) Instead of trying to output your whole OBS through NDI, you can apply NDI to the Vertical canvas specifically. In OBS, go to your Vertical Scenes list. Right-click the Scene you want to send to TikTok. Select Filters. Click the + and look for Dedicated NDI™ output (this comes with DistroAV). Name it something like TikTok_Vertical. In TikTok Live Studio: Add a source, select NDI, and you should see TikTok_Vertical as an option. 2. The "Window Capture" Method (If NDI Filters Fail) If the NDI filter doesn't show up or causes a crash (which some users in that discussion mentioned), do not go back to Virtual Camera. Instead: In the Aitum Vertical panel, click the Settings (Gear icon). Find the option to "Open Vertical Projector" (usually Windowed). This opens a separate window on your desktop that is only the vertical feed. In TikTok Live Studio: Add a source -> Window Capture -> Select the Vertical Projector window. Crucial Optimization: In OBS, right-click the Projector window and ensure "Scale Filtering" is set to Point or Bicubic. This reduces the GPU load of rendering that extra window. 3. The Hardware Strategy (Brutally Honest Truth) You have an RTX 3070. The reason you're lagging in CS2 is that CS2 is trying to hog 99% of your GPU's "Compute" power, and the Virtual Camera/TikTok Live Studio is trying to steal some of that power to process the video frame. To stop the lag immediately: Cap your FPS in CS2: If you're running uncapped (e.g., 300+ FPS), your GPU is pinned at 100%. Cap it to something stable like 144 or 240 using fps_max in the console. This leaves "breathing room" for the NDI/Virtual Camera encoding. Enable "NVIDIA Reflex" in CS2: Set it to Enabled + Boost. This tells the driver to prioritize the game's latency even when the GPU is under load from streaming. HAGS (Hardware Accelerated GPU Scheduling): Go to Windows Settings -> System -> Display -> Graphics -> Change default graphics settings. Turn HAGS ON. In 2026, with an RTX card and OBS, this is essential for preventing stuttering when multi-tasking. Summary: What to do right now Try the Dedicated NDI Filter on the Vertical Scene first. If that doesn't work, use the Windowed Projector + Window Capture in TikTok Live Studio. Cap your FPS in CS2. This is the most common reason high-end PCs lag while streaming—the game is simply eating all the resources because it wasn't told to stop.
