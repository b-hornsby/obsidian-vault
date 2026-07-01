---
category: streaming
date: 2026-04-06
id: 360453
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan confirmed that his current audio routing approach was not working.
tags:
- troubleshooting
- streaming
- audio-routing
---
# yeah thats not workinh 

### USER
yeah thats not workinh 

### GEMINI
The reason it’s "not working" is that Windows handles virtual audio like a game of telephone, and one of your "players" is likely on the wrong channel. If you don't see a clear output in TikTok, it's usually because the Windows Sound Control Panel is hiding the device or it's disabled. Let’s bypass the guesswork and fix the "invisible" link. 1. The "Hidden" Windows Check TikTok can only see what Windows "Recording" tab allows it to see. Right-click the Speaker Icon in your taskbar > Select Sounds (or "Sound Settings" > "More sound settings"). Go to the Recording tab. Find VoiceMeeter Output (VB-Audio VoiceMeeter VAIO). Right-click it and ensure "Enable" is checked. Also, right-click it and select Set as Default Device. Note: This is the "B1" bus from your Banana screenshot. 2. The OBS "Monitoring" Force If Voicemeeter isn't dancing, OBS isn't sending the signal. In OBS Settings > Audio, verify Monitoring Device is set specifically to CABLE-A Input. In the OBS Mixer, click the gear/three dots on your Mic > Advanced Audio Properties. Make sure it says Monitor and Output. If it already does, toggle it to "Off" and then back to "Monitor and Output" to reset the driver hook. 3. The Voicemeeter "Input" Logic Look at the first column in your Voicemeeter Banana (where you set Hardware Input 1). If you see "Select Input Device," click it and choose WDM: CABLE-A Output. Make sure the B1 button is green. Look at the far right of Voicemeeter under MASTER SECTION. Is the B1 meter moving when you talk? If NO: The problem is between OBS and Voicemeeter. If YES: The problem is between Voicemeeter and TikTok. 4. The TikTok "Nuclear Option" If you still don't see "Voicemeeter Output" in the TikTok list after doing Step 1: Close TikTok LIVE Studio entirely. Restart Voicemeeter (Menu > Restart Audio Engine). Re-open TikTok LIVE Studio. In TikTok's Audio Settings, look for Voicemeeter Output or CABLE-A Output directly. Advisor's Shortcut: If TikTok is being stubborn and won't show Voicemeeter, just select CABLE-A Output as your Mic in TikTok. This skips the Voicemeeter middleman and pulls the audio straight from the OBS monitor. The Brutal Truth You are dealing with "Driver Drift." Windows 11 updates often break how virtual cables report themselves to apps. Is the B1 meter in Voicemeeter moving when you talk in OBS? * If yes, the bridge is working and we just need to find the right name in the TikTok list. If no, OBS isn't actually "speaking" to Cable A. Check that OBS hasn't defaulted your Monitoring Device back to "Default."
