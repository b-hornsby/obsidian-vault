---
category: streaming
date: 2026-02-03
id: 170689
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is looking for a drop shadow option in OBS for styling text or overlay
  elements but can't find it.
tags:
- obs-studio
- drop-shadow
- filter
- streaming-overlay
---
# i dont see drop shadow as an option

### USER
i dont see drop shadow as an option

### GEMINI
If you don’t see Drop Shadow, it’s because you are running a "vanilla" version of OBS on Linux without the necessary plugin libraries. Unlike the Windows version, the Linux build of OBS is often stripped down to the bare essentials depending on how you installed it (Flatpak vs. Pacman). You are hitting the ceiling of what default OBS on Linux can do. You have two choices: stop fighting the software and use a workaround, or install the missing pieces. 1. The "Brute Force" Workaround (No Plugins Required) If you need it right now and don't want to install anything else, do this: Create your White text source (Call it "Text_Main"). Right-click "Text_Main" -> Duplicate (or Copy, then Paste Reference). Call this one "Text_Outline". Move "Text_Outline" below "Text_Main" in your Sources list. Right-click "Text_Outline" -> Filters -> Color Correction. Turn Brightness all the way down so the text is pure black. Select "Text_Outline" in the preview and use your Arrow Keys to nudge it 2 pixels up and 2 pixels left. Duplicate "Text_Outline" again and nudge it 2 pixels down and 2 pixels right. The Reality: This is "jank," but it works. It creates a manual shadow/outline. 2. The CachyOS/Arch Way (The "Correct" Fix) Since you are on an Arch-based distro, you have access to the AUR (Arch User Repository). You are missing the obs-filters or StreamFX plugins which provide the Drop Shadow and Stroke options. Open your terminal and check for filter packages. One of the most reliable for Linux is obs-multi-theme-skip or specific filter sets. Better yet: Install obs-gradient-source or obs-stroke if available in the AUR. 3. The "Stop Wasting Time" Alternative (Browser Source) I’m going to be brutally honest: You are spending more time troubleshooting a $0.05$ cent outline than it’s worth. If you want a perfect black outline on white text on Linux, use a Browser Source. Add a Browser Source to OBS. Set the URL to about:blank. Scroll down to the Custom CSS box and paste this: body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; } .outline-text { color: white; font-family: sans-serif; font-weight: bold; font-size: 70px; -webkit-text-stroke: 3px black; /* This is your outline */ text-shadow: 0px 0px 5px black; } In the HTML box (if available) or by using a local file, just put: <div class="outline-text">YOUR TEXT HERE</div> The Strategic Move You are on CachyOS because you want performance and control. Default OBS text sources on Linux are neither performant nor controllable. Which road do you want to take? The Quick & Dirty: I can explain the "Double Source" nudge method more clearly. The Pro: I can help you set up a local HTML file as a Browser source so you never have to deal with missing filters again.
