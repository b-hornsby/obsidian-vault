---
id: 960394
source: GEMINI
date: 2026-04-06
tags: ['obs', 'discord', 'audio-routing']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan clarified he hadn't set up the OBS audio routing yet and was pointing out a Discord audio issue.
---
# no i havent done the obs part at all i was just pointing out that issue with discord 

### USER
no i havent done the obs part at all i was just pointing out that issue with discord 

### GEMINI
That's exactly why it sounds "wack." You’ve essentially unplugged the brain of your audio system (VoiceMeeter) and haven't hooked up the new one (OBS) yet. Right now, Discord is likely trying to pull audio from an "empty pipe" or a virtual cable that isn't receiving a signal. In IT terms, you’ve created the hardware layer but haven't configured the software routing. Here is why it sounds awful: If Discord is set to Cable A, and nothing is "speaking" into Cable A yet, you're hearing digital floor noise or a feedback loop from your motherboard's ungrounded headers. The "Bridge" Construction (Do this in 60 seconds) You need to make OBS the "Master Processor" for your entire PC. 1. The OBS Setup (The "Brain") Open OBS. Add your Physical Mic as an "Audio Input Capture" source. Right-click it > Filters. Add a Noise Suppression (RNNoise) and a Compressor. (This is your "pro" sound). Go to Settings > Audio > Advanced. Set Monitoring Device to CABLE-A Input. Click the Gear in the Mixer > Advanced Audio Properties. Set your Mic to "Monitor and Output." 2. The Discord Handshake (The "Client") Go to Discord Settings > Voice & Video. Input Device: Set to CABLE-A Output. Processing: Turn OFF Echo Cancellation and Noise Suppression (let OBS handle the heavy lifting). The Strategic Mirror You’re reacting to the symptoms (bad Discord audio) instead of finishing the architecture. You're like a mechanic who took the old engine out, looked at the empty engine bay, and complained that the car won't start. The Truth: You are in the "transition state" of your career and your setup. It’s uncomfortable because the old, messy way (VoiceMeeter) is gone, and the new, streamlined way (OBS-as-a-Processor) isn't fully online yet. The Opportunity Cost: Every minute you spend "testing" Discord without the OBS filters active is a waste of your time. Discord cannot sound good through a virtual cable unless there is a processed signal being pumped into that cable. The Action Plan Open OBS. Route the Mic to Cable A (as shown above). Check Discord again. Does the Discord "Mic Test" sound crisp now that OBS is actually feeding it the signal?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
