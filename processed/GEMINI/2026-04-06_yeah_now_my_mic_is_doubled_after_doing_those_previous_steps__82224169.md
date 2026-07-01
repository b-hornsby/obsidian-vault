---
category: streaming
date: 2026-04-06
id: 347940
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's mic audio became doubled on TikTok Live Studio after following previous
  audio routing steps.
tags:
- tiktok-live
- mic-doubling
- audio-routing
- echo
---
# yeah now my mic is doubled after doing those previous steps on tiktok live studio

### USER
yeah now my mic is doubled after doing those previous steps on tiktok live studio

### GEMINI
The "double audio" is the classic sign that you’ve created a redundant loop. You are sending your voice to TikTok through two different doors at the same time. In IT terms, you have a broadcast storm. You're sending the same packet twice, and TikTok is playing them both with a slight delay between them. The Source of the "Double" Door 1: You are sending your filtered Mic to Cable A via that OBS filter/monitor. Door 2: You likely still have TikTok's "System Audio" or "Desktop Audio" source active, which is picking up your OBS "Monitoring" signal from your FiiO DAC. The "Surgical" Kill (Do this now) 1. The TikTok Mixer Cleanup Open TikTok Live Studio. Look at your audio sources. The Goal: TikTok should only be "listening" to one thing from you. The Move: MUTE the "System Audio" or "Desktop Audio" source inside TikTok. Why: Since you are already piping your Mic (and presumably your game/music) through OBS, TikTok doesn't need to capture your Windows sound separately. If it does, it hears your "Monitor" signal from OBS and your "System" signal from Windows. Double audio. 2. The Windows "Listen" Check (The Repeat Offender) If muting TikTok's system audio didn't fix it, Windows is looping you. Go to Sound Control Panel > Recording. Right-click CABLE-A Output > Properties > Listen. UNCHECK "Listen to this device." Why: If this is checked, Windows is playing your processed Mic back into your headphones. You hear yourself twice: once naturally (or via FiiO) and once through the $20ms$ Windows delay. 3. The OBS "Advanced" Audit Go to Advanced Audio Properties in OBS. Look at your Mic. If you are using the "Audio Monitor" Filter to send your voice to Cable A, set your Mic in the OBS Mixer to "Output Only." Why: If you have it set to "Monitor and Output" in the mixer and you have a filter sending it to a cable, you are essentially "double-monitoring." The Reality Check You’re frustrated because you keep adding "fixes" without removing the "old" settings. You’re building a professional IT rig, but you’re leaving the old cables plugged in. The Strategy: In any high-level routing, you want One Path. The Logic: Your Mic goes to OBS -> Cable A -> TikTok. The Failure: You currently have Mic going to OBS -> Cable A -> TikTok AND OBS -> FiiO -> TikTok System Audio. The Action Plan Mute "System Audio" in TikTok Live Studio. 2. Keep your "Mic" in TikTok set to Cable A. Check your Windows Sound Panel for any "Listen to this device" boxes that are checked. Is the "doubling" gone now that you’ve closed one of the doors?
