---
category: streaming
date: 2026-04-06
id: 803379
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan confirmed his mic worked in OBS but Cable A output wasn't being picked
  up by TikTok Live.
tags:
- vb-cable
- obs
- tiktok-live
- mic-audio
- troubleshooting
---
# yeah i did the cable a output and it doesnt work my mic works on obs tho

### USER
yeah i did the cable a output and it doesnt work my mic works on obs tho

### GEMINI
It "doesn't work" because you haven't connected the output of the OBS "brain" to the input of the Cable A "pipe." In IT terms, you have the server running (OBS) and the cable plugged in (Virtual Cable), but you haven't configured the routing table. If your mic is moving in OBS but Discord/TikTok hears nothing, it’s a Monitoring issue. The 30-Second "Hard" Fix 1. Point the OBS "Speaker" at the Cable In OBS, go to Settings > Audio. Look at Advanced > Monitoring Device. Set this to CABLE Input (VB-Audio Virtual Cable). Note: If you have Cable A and B, make sure you pick CABLE-A Input. 2. Open the Valve (The Mixer) In the OBS main window, look at your Audio Mixer. Click the three dots (or gear icon) next to your Microphone. Select Advanced Audio Properties. Find your Mic in the list. Change Audio Monitoring from "Monitor Off" to Monitor and Output. Why This Works (The IT Logic) Output: This sends your mic to your Twitch/Twitter stream. Monitor: This sends your mic to the "Monitoring Device" you chose in Step 1 (Cable A). The Result: Discord and TikTok are "listening" to Cable A. Now that OBS is "monitoring" (speaking) into that cable, they finally have something to hear. The "Echo" Warning If you suddenly hear your own voice in your FiiO DAC (your headphones) after doing this: Go to your Windows Sound Control Panel (the list of devices). Go to the Recording tab. Right-click CABLE-A Output > Properties > Listen. UNCHECK "Listen to this device." Why? You want the audio to go into the cable for TikTok, but you don't want Windows to pull it out of the cable and back into your ears. The Reality Check You’re frustrated because you're treating this like a "setting" you toggle, but it's a flow. Mic -> OBS (Filters) -> Monitor Out -> Virtual Cable -> TikTok/Discord. If you skip the "Monitor and Output" step in the Advanced Audio Properties, the signal stops inside OBS and never reaches the virtual cable. It's like having a high-end water filtration system but forgetting to open the main valve to the rest of the house. Open the "Advanced Audio Properties" now and set that Mic to "Monitor and Output." Does the bar in Discord/TikTok finally start jumping?
