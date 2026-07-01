---
id: 571697
source: GEMINI
date: 2026-04-06
tags: ['windows', 'gpu-scheduling', 'performance', 'streaming-optimization']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was trying Windows GPU scheduling as a first step to resolve streaming performance issues.
---
# Let’s try the windows gpu scheduling thing first

### USER
Let’s try the windows gpu scheduling thing first

### GEMINI
Disabling Hardware-Accelerated GPU Scheduling (HAGS) is a classic "pro-streamer" fix. While it's designed to make games run faster, it often breaks the way OBS "steals" frames from the GPU to send them to TikTok or NDI. On an 8GB card like your RTX 3070, HAGS can also hog up to 1GB of VRAM, which is likely why your CS2 feels like it’s drowning when you add a second stream. Step 1: Disable HAGS (The "Resource War" Fix) Right-click your desktop and select Display settings. Scroll down and click Graphics. Click the blue text at the top: "Change default graphics settings". Switch Hardware-accelerated GPU scheduling to OFF. Restart your computer. (This is mandatory for the change to take effect). Step 2: Fix the "Permissions" (Admin Mode) While your PC is rebooting, you need to make sure Windows knows that OBS is just as important as CS2. If you don't run OBS as Admin, Windows will starve it of GPU power the second a smoke grenade pops in CS2. Do this for BOTH OBS and TikTok Live Studio: Right-click the desktop shortcut for OBS. Select Properties. Go to the Compatibility tab. Check the box: "Run this program as an administrator". Click Apply and OK. Repeat this for TikTok Live Studio. Step 3: The "Peace Treaty" (FPS Capping) If you do the two steps above but still let CS2 run at uncapped FPS, your GPU will stay at 100% load, and the lag will return. You must give the system "breathing room." Open CS2. Open the console (~). Type fps_max 165 (or whatever your monitor's refresh rate is). The Result: This stops the GPU from wasting energy on frames you can't even see, leaving that extra 5-10% of power for OBS to handle the NDI/Vertical feed smoothly. The Advisor's Checklist [ ] HAGS: Off? [ ] PC Restarted: Yes? [ ] OBS & TikTok: Run as Admin? [ ] CS2 FPS: Capped? Why this works: When HAGS is ON, the GPU handles its own scheduling and ignores Windows' priority settings. By turning it OFF, Windows regained control and—because you set OBS to Admin—it will now force the GPU to reserve enough power for your stream, even when CS2 is demanding everything. Try a test match in CS2 now. Does the mouse movement feel "heavier" or is the stutter gone?
