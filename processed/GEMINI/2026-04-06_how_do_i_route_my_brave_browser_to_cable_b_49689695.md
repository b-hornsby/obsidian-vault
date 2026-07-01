---
id: 985437
source: GEMINI
date: 2026-04-06
tags: ['brave-browser', 'vb-cable', 'audio-routing', 'voicemeter']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan needed help routing Brave browser audio to VB-Cable B for streaming separation.
---
# how do i route my brave browser to cable b?

### USER
how do i route my brave browser to cable b?

### GEMINI
Since you’ve ditched the VoiceMeeter bloat, you’re going to use the Windows 11 Volume Mixer. It’s cleaner, it’s native, and it doesn't crash when your CPU gets busy running your trading bots. This is the "IT Pro" way to handle individual application routing without a messy GUI. 1. The "Traffic Control" Move (Windows Settings) Windows allows you to hard-code where an app sends its sound. Open Brave and play a YouTube video or some audio (it needs to be active for Windows to see it). Right-click the Speaker Icon in your Taskbar > Open Volume Mixer. Scroll down to Apps. Find Brave. Click the dropdown arrow. Change Output Device from "Default" to CABLE-B Input (VB-Audio). 2. The "Bridge" Move (OBS) Now Brave is "speaking" into Cable B, but you can’t hear it yet, and neither can your stream. In OBS, add a new Audio Input Capture source. Name it "Brave Audio." Set the Device to CABLE-B Output (VB-Audio). The Result: You now have a dedicated volume slider in OBS just for your browser. 3. The "Ear" Move (Monitoring) If you want to hear the music/audio from Brave in your FiiO DAC while you're streaming: In the OBS Mixer, click the three dots on "Brave Audio" > Advanced Audio Properties. Set "Brave Audio" to Monitor and Output. Wait: Ensure your OBS Monitoring Device (Settings > Audio > Advanced) is set to your FiiO DAC for this specific step. The Strategic Mirror You’re starting to build a modular setup. By using Cable B for Brave, you’ve decoupled your browser from your system sounds. The Benefit: You can now play copyrighted music in Brave for your own ears, but mute it in the Aitum Vertical/TikTok scene so you don't get banned, while still letting it play on your Twitch stream. This is high-level production. The Warning: If you set Brave to Cable B and don't set it to "Monitor" in OBS, you will be sitting in silence wondering why your browser has no sound. The audio must flow through OBS to reach your ears. The "IT Audit" for Your Transition You’re moving from "warehouse guy" to "technical specialist." A warehouse specialist knows that if you mislabel a pallet, it ends up in the wrong truck. Brave (The Pallet) -> Windows Mixer (The Forklift) -> Cable B (The Dock) -> OBS (The Truck). Does Brave show up in the Windows Volume Mixer now? (Make sure audio is playing in a tab, or it won't appear).
