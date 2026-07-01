---
id: 911884
source: GEMINI
date: 2026-04-06
tags: ['voicemeter-banana', 'vb-cable', 'audio-routing', 'cleanup']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was considering removing Voicemeter Banana and cables to start his audio routing setup fresh.
---
# so i dont need voicemeter banana anymore? i delete it and the cables to start fresh

### USER
so i dont need voicemeter banana anymore? i delete it and the cables to start fresh

### GEMINI
Uninstall VoiceMeeter Banana, but keep the Virtual Cables. VoiceMeeter is a digital mixer that sits on top of your drivers; the Virtual Cables (A+B) are the actual "pipes." You need the pipes, but you don't need the messy mixer sitting in the middle. The Cleanup Phase (The "Fresh Start") Uninstall VoiceMeeter Banana: Go to your Control Panel and rip it out. It’s bloatware for your specific needs. Restart Your PC: This is mandatory. Windows audio drivers are notoriously stubborn. If you don't restart, your FiiO DAC and Virtual Cables will likely "lock up" or crackle. Keep/Reinstall VB-Cables: Ensure CABLE-A and CABLE-B are still visible in your "Sound Control Panel" (the old-school list view). The "IT Specialist" Signal Path (Post-Restart) Once you've rebooted and cleared the clutter, here is the clean, high-performance routing that won't mess with your FiiO DAC: 1. Windows Configuration (Your Ears) Default Output: Set this to your FiiO DAC. Default Input: Set this to your Physical Mic. Result: Your PC sounds exactly like it always does. No lag, no virtual interference. 2. OBS Configuration (The Processor) Mic Source: Add your Physical Mic. Apply your filters (Noise Gate, Compressor, VSTs). Monitoring Device: Go to Settings > Audio > Advanced. Set this to CABLE-A Input. Advanced Audio Properties: Set your Mic to "Monitor and Output." Result: OBS is now taking your processed voice and "speaking" it into Cable-A. 3. TikTok Studio Configuration (The Destination) Mic Input: Select CABLE-A Output. System Audio: Select your FiiO DAC (or "System Default"). Result: TikTok "hears" your clean OBS mic on one channel and your game/PC audio on the other. The Strategic Mirror You’re asking if you should "delete and start fresh." That is the most rational thing you’ve said this session. In Linux (where you’re more comfortable), you wouldn’t keep a broken config file—you’d purge the package and start with a clean .conf. The Opportunity Cost: Every minute you spend "patching" a bad VoiceMeeter setup is technical debt. By deleting it, you are simplifying your architecture. The "No-Echo" Final Check After you set this up, if you hear yourself in your headphones: Go to Sound Control Panel > Recording Tab. Right-click CABLE-A Output > Properties > Listen. UNCHECK "Listen to this device." Windows doesn't need to play the cable back to you. OBS is already sending the "Monitor" signal to that cable for TikTok to catch. Restart the PC now, do the clean install of the cables (if needed), and tell me if TikTok sees your voice without the VoiceMeeter "clutter" in the way.
