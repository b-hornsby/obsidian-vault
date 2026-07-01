---
id: 089866
source: GEMINI
date: 2025-09-25
tags: ['obs-studio', 'crashing', 'version-32.0.0', 'troubleshooting']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is reporting that OBS is crashing frequently, but the original scene issue seems to be resolved.
---
# i also want to add that it crashes a lot now. currently on version 32.0.0. the scene i was talking about doesn't exist now though so i guess i fixed it? 

### USER
i also want to add that it crashes a lot now. currently on version 32.0.0. the scene i was talking about doesn't exist now though so i guess i fixed it? 

### GEMINI
That's excellent news that the stubborn scene is finally gone! That was likely the root cause of both the deletion issue and possibly some stability problems, as a corrupted scene configuration can lead to unpredictable behavior and crashes. However, since you mentioned OBS is still crashing a lot on version 32.0.0, here is a breakdown of the most common causes and how to troubleshoot them, especially for recent major OBS updates: Most Common Causes of OBS Crashes Common CauseTroubleshooting StepsOutdated/Incompatible PluginsThis is the #1 cause of crashes after a major OBS update (like 32.0.0). Plugins (like StreamElements, Move Transition, Stream Deck, etc.) are often not immediately updated for the new OBS version and cause conflicts.Outdated DriversOBS relies heavily on your GPU and other system drivers (webcam, capture card). Outdated or corrupt drivers can lead to crashes, especially when capturing content.Hardware AccelerationConflicts with Windows' Graphics Settings (like Hardware-accelerated GPU scheduling - HAGS) can cause issues.Corrupted Settings/ProfileThe cleanup of the scene might have fixed one part, but the overall profile or scene collection could still have a hidden issue. Crash Troubleshooting Steps (for OBS 32.0.0) 1. Analyze the Crash Log (The Best First Step) OBS records exactly what happened when it crashed. Restart OBS. Try to reproduce the crash (e.g., switch scenes, start recording, or just let it sit until it crashes). Re-open OBS (if it didn't restart automatically). Go to Help > Log Files > Upload Current Log File. Click Analyze (this will open a browser window) and follow the instructions it provides. The log analyzer is designed to flag common issues like incompatible plugins, old drivers, or incorrect settings. 2. Check and Update Everything Update Your GPU Drivers: Go directly to the NVIDIA, AMD, or Intel website and download the absolute latest driver package. This is critical. Update/Disable Plugins: Check for updates for all third-party plugins (e.g., StreamElements, Move Transition, AITrack, etc.). If a plugin update isn't available, temporarily uninstall it. This is often the fastest way to stop recurring crashes. If the crashes stop, you've found your culprit. 3. Test with a Clean Configuration To rule out an issue with your current settings, sources, or scene collection: Go to Scene Collection > New. Give it a name (e.g., "Test Collection"). In this new, empty collection, try to perform the action that usually causes the crash (e.g., add a simple Display Capture or start a quick recording). If the crash stops in the new collection, the issue is definitely in your old scene collection (likely a specific source or setting there). You should rebuild your setup in the new, clean collection. 4. Graphics Settings (Windows) If you are on Windows, try this: In OBS, go to Settings > Advanced. Under General, uncheck "Enable Browser Source Hardware Acceleration." Run OBS as Administrator every time. (Advanced) Search for "Graphics Settings" in the Windows search bar and ensure Hardware-accelerated GPU scheduling (HAGS) is turned off (you'll need to restart your PC after changing this).


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
