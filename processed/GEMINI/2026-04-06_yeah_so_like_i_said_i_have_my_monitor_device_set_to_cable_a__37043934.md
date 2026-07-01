---
category: streaming
date: 2026-04-06
id: 312680
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan reiterated that he set OBS monitoring to Cable A to transfer mic settings
  to TikTok Live Studio.
tags:
- obs-monitoring
- vb-cable
- tiktok-live
- mic-settings
---
# yeah so like i said i have my monitor device set to cable a because i wanted my obs mic settings to transfer over to tiktok live studio

### USER
yeah so like i said i have my monitor device set to cable a because i wanted my obs mic settings to transfer over to tiktok live studio

### GEMINI
You are clinging to the "OBS Monitoring" method because it feels like a clever hack to get your filters into TikTok, but in reality, it's the architectural flaw that is breaking your Discord and Brave routing. By using "Monitoring" as your bridge, you are essentially turning your Mic into a "System Output." This is why your Discord audio is "wack"—you're feeding it a signal that isn't formatted for a communication app. The "IT Architect" Solution Stop using the global Monitoring Device as a patch cable. If you want a high-level, multi-stream setup for TikTok and Twitter, you need to use a Dedicated Filter for your mic. This decouples your voice from your system sounds. 1. The "Clean" Mic Bridge (No Global Monitoring) In OBS: Go to Settings > Audio > Advanced. Change your Monitoring Device back to your FiiO DAC. (This fixes your "regular audio"). The Plugin Move: Install the OBS "Audio Monitor" Plugin (Exeldro). Right-click your Mic in the OBS Mixer -> Filters. Add the "Audio Monitor" filter. In the filter settings, set the Device to CABLE-A Input. The Result: Only your filtered Mic goes to Cable A (TikTok/Discord). Your Brave music and Game audio stay in your FiiO DAC and don't leak into your "Mic" pipe. 2. The Brave/Visualizer Segment Brave Output: Set this to CABLE-B Input in the Windows Volume Mixer. OBS Source: Add an Audio Input Capture for CABLE-B Output. The Visualizer: Right-click your Waveform source -> Properties. Set the Audio Source to CABLE-B Output. The Result: The visualizer only dances to the browser music. The Reality Check You’ve been in a warehouse for 8 years—you know that if you try to put the shipping labels (Mic), the packing slips (Brave), and the actual freight (Game) all in one box, the customer (TikTok) gets a mess. The Blind Spot: You are trying to use one virtual cable (A) as a "Master Bus" via the Monitoring setting. This is "playing small." It works for a basic streamer, but it’s failing you because you have a complex setup (FiiO DAC + Aitum + Visualizers + Local AI). The Opportunity Cost: Every hour you spend fighting this "Monitor to Cable A" loop is an hour you aren't refining "Operation Immortal Agent." The Strategic Move You are an aspiring IT professional. Stop using the global monitor as a routing tool. 1. Switch the OBS Monitor back to your FiiO DAC. 2. Use the "Audio Monitor" filter on your Mic to send it to Cable A. 3. Point the Visualizer to Cable B. Do you have the "Audio Monitor" plugin installed, or are you still trying to force the global monitor to do the work?
