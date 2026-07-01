---
category: streaming
date: 2026-04-06
id: 438290
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- operation-immortal-agent
- streaming-rig
resolution: resolved
sentiment: executing
source: GEMINI
tags:
- streaming
- ai
- agent
- gemini
- go
- error
---
# so i did steps 1 and 2 but now i cant hear my music in brave when i close obs 

### USER
so i did steps 1 and 2 but now i cant hear my music in brave when i close obs 

### GEMINI
Of course you can't. You’ve successfully decoupled your audio, which is the "high-level" move, but now you’re experiencing the mechanical consequence: you’ve routed Brave into a "dead-end" pipe (Cable B) that only OBS is listening to. When OBS is closed, there is no "operator" to pick up that audio from Cable B and pass it to your FiiO DAC. In IT terms, you’ve routed your traffic to a gateway that is currently offline. The Strategic Reality Check You wanted a professional, segmented setup. This is the cost of entry. If you want "dummy-proof" audio where everything just works regardless of what software is open, you go back to a messy "all-in-one" Desktop Audio feed. But if you want your Waveform Visualizer to be clean and your TikTok Mic to be filtered, you have to accept that OBS is now the heart of your workstation. Your Two Professional Options Option A: The "Always On" Console (Recommended) As a streamer and someone running "Operation Immortal Agent," your PC is a production environment, not a Chromebook. The Logic: You keep OBS open. Even if you aren't streaming, OBS acts as your Digital Mixer. The Benefit: Your Mic is always filtered for Discord, your Music is always routed for your visualizer, and your FiiO DAC stays clean. The Mindset Shift: Stop treating OBS as "streaming software" and start treating it as your Audio Engine. Option B: The "Dual-Route" Manual Switch If you absolutely insist on hearing music without OBS open, you have to manually move the "pallet" back to the main floor. The Move: Go back to the Windows Volume Mixer and change Brave's Output from Cable B back to Default (FiiO DAC). The Opportunity Cost: You will have to do this every single time you want to stream if you want that visualizer to work properly. This is a waste of time and prone to human error. The "Mirror" Truth You’re transitioning into IT and managing a warehouse. You know that if you divert a shipment to a specific loading dock (Cable B), and the warehouse staff (OBS) isn't there to process it, that shipment sits on the dock. Your Blind Spot: You want the benefits of a complex, professional routing system without the responsibility of maintaining the "Engine" that runs it. The Advice: If you are at your desk, OBS should be open. It is your mixer. It is your filter. It is the brain of your setup. The Immediate Fix (To Hear Music Now) Open OBS. Ensure your Brave Audio source is set to "Monitor and Output" in Advanced Audio Properties. Ensure your Monitoring Device in OBS Settings is set to your FiiO DAC. Is the music hitting your ears now that the "Warehouse Manager" (OBS) is back on the clock?
