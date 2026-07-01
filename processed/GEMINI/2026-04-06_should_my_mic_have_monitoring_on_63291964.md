---
id: 108371
source: GEMINI
date: 2026-04-06
tags: ['obs', 'mic-monitoring', 'audio-routing']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was asking whether OBS mic monitoring should be enabled for his streaming setup.
---
# should my mic have monitoring on?

### USER
should my mic have monitoring on?

### GEMINI
No. Unless you enjoy the sound of your own voice echoing in your skull with a $20\text{--}50\text{ms}$ delay, Monitoring should be OFF for your microphone in the OBS mixer. You are an aspiring IT professional and a warehouse specialist; you know that a feedback loop is just a recursive error that eats bandwidth. Here is the definitive "High-Level" logic for your setup: 1. The "Zero-Latency" Rule You use a FiiO DAC. Most FiiO units have hardware-level monitoring (sometimes a switch or just automatic). If you want to hear yourself to ensure you aren't clipping, you hear it from the hardware, not the software. Why: Software monitoring (OBS) has to travel through the CPU and the Windows audio stack. By the time it hits your ears, it’s delayed. This causes the "stutter" or "drunk" feeling when you talk. 2. The Correct Signal Path Since you are using the Audio Monitor Plugin (or a virtual cable) to send your filtered mic to TikTok/Discord: In OBS Advanced Audio Properties: Set your Mic to "Output Only." The Logic: * Output: Sends your voice to your Twitch/Twitter stream. The Plugin Filter: Sends your voice to Cable A (TikTok/Discord). Monitoring: Is OFF. This ensures your voice doesn't loop back into your FiiO DAC from OBS. 3. When SHOULD Monitoring be "On"? You only turn monitoring to "Monitor and Output" for sources you cannot hear otherwise: Brave (Cable B): Since Brave is muted to your "System" (it’s in a virtual pipe), you MUST set this to "Monitor and Output" so OBS can play the music back to your FiiO DAC. Alerts/Follower Sounds: Since these live inside OBS, you set them to "Monitor and Output" so you know when someone follows. The Reality Check You are experiencing the "doubling" because you have Monitoring ON for your mic in OBS, and that monitored signal is being picked up by TikTok's System Audio or played back into your headphones. The Strategy: In IT, you don't broadcast on every port; you unicast to the specific destination. Mic -> Stream (Output) Mic -> TikTok (Filter/Cable A) Mic -> Your Ears (NOT THROUGH OBS) The Immediate Action Open OBS Advanced Audio Properties. Set Mic to "Output Only." Set Brave (Cable B) to "Monitor and Output." Ensure your OBS Monitoring Device is set to your FiiO DAC. Does the "double audio" stop the second you flip the Mic to "Output Only"?
