---
id: 019676
source: GEMINI
date: 2026-04-06
tags: ['tiktok-live', 'audio-options', 'troubleshooting']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was showing the limited audio device options available in TikTok Live Studio.
---
# these are the only options i see for audio

### USER
these are the only options i see for audio

### GEMINI
The reason you don't see an "Output" option in your screenshots is that Windows and TikTok treat these virtual paths differently. Windows/OBS sees them as Inputs (where you send sound). TikTok sees them as Recording Devices/Microphones (where it receives sound). Looking at your specific list of options, you actually have exactly what you need. Here is the proper final connection: 1. The OBS Step (The Send) In OBS Settings > Audio > Advanced, set your Monitoring Device to: CABLE-A Input (VB-Audio Virtual Cable A). In the OBS Mixer, right-click your Mic/Game > Advanced Audio Properties > Set them to Monitor and Output. 2. The Voicemeeter Banana Step (The Bridge) On Hardware Input 1 (the first column): Select KS: CABLE-A Output (this is the other end of the OBS pipe). Click the B1 button on that column so it’s green. Make sure A1 is OFF (to avoid hearing yourself). 3. The TikTok LIVE Studio Step (The Receive) Looking at your uploaded image (the list of devices), select this exact option as your Microphone: Voicemeeter Input (VB-Audio Voicemeeter VAIO) Wait, why "Input"? I know it's confusing as hell, but in your specific driver list (image b7ea48.png), TikTok is mislabeling the virtual output of Voicemeeter as an input. It’s a common Windows naming quirk. How to Verify It's Working: Look at the B1 meter in Voicemeeter (far right, under Master Section). If it's moving when you talk, Voicemeeter has the sound. Look at the green bar in TikTok LIVE Studio. If you selected the one I told you above, it should now be moving in sync with Voicemeeter. The Advisor's Final Word You've built a professional-grade "Virtual Matrix." It’s overkill for a casual stream, but perfect for what you're doing—streaming on TikTok while running a vertical OBS layout via Aitum. The Strategic Advice: Now that the pipes are connected, lock the doors. * Do not change your Windows Default device. Keep that on your FiiO DAC so your system sounds don't accidentally leak into TikTok. Ignore the other "Voicemeeter In 1, 2, 3, 4" options. Those are for advanced "Potato" versions or complex multi-track recording that you don't need right now. Action: Is the green bar in TikTok finally moving when you speak into your OBS mic?
