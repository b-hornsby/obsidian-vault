---
id: 072569
source: GEMINI
date: 2026-04-06
tags: ['voicemeter-banana', 'audio-routing', 'screenshot', 'troubleshooting']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan shared his Voicemeter Banana configuration to get help diagnosing audio routing issues.
---
# this is what my voicemeter banana looks like 

### USER
this is what my voicemeter banana looks like 

### GEMINI
That screenshot shows the standard Voicemeeter, not Banana. Banana has three hardware inputs and two virtual ones; you have two hardware and one virtual. No problem—the logic stays the same, we just have one less "lane" to play with. Here is your 3-Step "Proper" Routing Plan using exactly what is in your image: 1. The OBS "Send" In OBS, we’re going to use Cable A as the bridge so we don't clutter your main desktop audio. In OBS Settings > Audio > Advanced: Set Monitoring Device to CABLE-A Input (VB-Audio Cable A). In OBS Audio Mixer: Right-click your Mic and Desktop Audio > Advanced Audio Properties. Change Audio Monitoring for both to Monitor and Output. Result: OBS is now "broadcasting" its audio into Cable A. 2. The Voicemeeter "Bridge" (Looking at your image) Now we make Voicemeeter pick up that OBS broadcast. Stereo Input 1 (Left Side): Click the "Select Input Device" text at the top. Choose KS: CABLE-A Output (or WDM if KS isn't there). Routing Buttons: On that same column, click the 'A' button so it is OFF (dark) and click the 'B' button so it is ON (lit up green). Why? If 'A' is on, you'll hear yourself in your own headphones (annoying echo). If 'B' is on, the sound goes to the "Virtual Out" which TikTok will listen to. 3. The TikTok "Receive" Now we tell TikTok to listen to Voicemeeter's "B" output. In TikTok LIVE Studio: Go to Audio Settings. Add a Microphone source. Choose Voicemeeter Output (VB-Audio Voicemeeter VAIO). Important: Mute everything else in TikTok Studio. You only want this one source. The Advisor's Strategic Audit You're using the base version of Voicemeeter. It works, but it's "tight." The Limit: Since you only have two hardware inputs, once you use one for OBS (TikTok Bridge), you only have one left for a physical mic or another cable. The Opportunity Cost: If you find yourself needing more lanes later (to separate Discord or Spotify for your Twitch VODs), you'll need to upgrade to Voicemeeter Banana (the free three-input version). But for getting TikTok live right now, this setup is lean and efficient. Quick Check: Look at your image under "B VIRTUAL OUT" (the far right meter). When you talk in OBS or play a game, do you see the green bars moving there? If yes, TikTok is officially receiving your audio. How do the levels look on that 'B' meter? Are they hitting the -12 to -6 range?
