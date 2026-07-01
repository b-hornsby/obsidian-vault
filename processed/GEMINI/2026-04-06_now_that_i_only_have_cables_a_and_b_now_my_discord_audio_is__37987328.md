---
category: streaming
date: 2026-04-06
id: 198699
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's Discord audio quality became terrible after switching to only Cables
  A and B.
tags:
- discord
- vb-cable
- audio-quality
- voicemeter
---
# now that i only have cables a and b now my discord audio is wack. when i test my mic on there it sounds awful 

### USER
now that i only have cables a and b now my discord audio is wack. when i test my mic on there it sounds awful 

### GEMINI
Discord is "wack" because it’s trying to be a smart sound engineer while you’re already doing the work in OBS. You’re feeding a highly processed, filtered, and compressed signal into an app that is also trying to apply its own noise suppression and echo cancellation. It’s like running two different GPS apps at the same time—they’re fighting each other and getting you lost. The "Clean Signal" Discord Fix Since you've already perfected your mic in OBS, you need to tell Discord to back off and just play the audio you're giving it. 1. Disable Discord's Internal "Processing" Go to Discord Settings > Voice & Video and turn off these three things immediately: Noise Suppression (Krisp): Set to None. (OBS is already doing this). Echo Cancellation: OFF. (This is the #1 cause of "robotic" or "underwater" sounds when using virtual cables). Automatic Gain Control: OFF. (This will fight your OBS compressor and mess up your levels). 2. The "Subsystem" Handshake If it still sounds "tinny" or laggy, it’s a driver handshake issue. Scroll to the bottom of the Voice & Video page. Change Audio Subsystem from "Standard" to Legacy. Restart Discord. 3. The "Standardization" Check (Windows Level) If the sample rates don't match, you get digital "crackling" or "deep voice" effects. Go to Sound Control Panel > Recording. Right-click your Physical Mic > Properties > Advanced. Check the format (e.g., 24-bit, 48000Hz). Right-click CABLE-A Output > Properties > Advanced. Ensure it is set to the exact same rate (48000Hz). If they don't match, your CPU is trying to resample your voice in real-time, which sounds like garbage. The Reality Check You’re frustrated because you want a "one-click" setup, but you're building a customized professional routing system. IT isn't about avoiding the "wack" issues; it's about knowing which lever to pull when they happen. The Strategy: You are now the "Master" of your audio. Discord is just a client. By turning off Discord's processing, you are forcing it to respect the high-quality signal you spent time building in OBS. The Move: Turn off Krisp/Echo Cancellation/Gain Control. Set Discord Input to Cable A. Set Discord Output to your FiiO DAC. Does the "Let's Check" mic test in Discord sound like your OBS recording now, or is it still distorted?
