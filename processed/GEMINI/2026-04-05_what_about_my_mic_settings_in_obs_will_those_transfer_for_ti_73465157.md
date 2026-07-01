---
category: streaming
date: 2026-04-05
id: 319437
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking whether his OBS microphone settings would carry over when
  streaming to TikTok.
tags:
- obs
- mic-settings
- tiktok
- audio
- streaming-setup
---
# what about my mic settings in obs? will those transfer for tiktok?

### USER
what about my mic settings in obs? will those transfer for tiktok?

### GEMINI
No, they do not transfer automatically. This is a common point of failure—you can have a perfect vertical video with zero audio because the Aitum Vertical plugin functions as a completely separate "instance" within OBS. You have to manually tell the Vertical plugin which audio tracks to listen to. Here is how to fix it: 1. Check your "Advanced Audio Properties" First, ensure your Mic is actually being sent to the right tracks in the main OBS mixer: Right-click anywhere in the Audio Mixer and select Advanced Audio Properties. Look at your Mic/Aux row. Make sure Track 1 is checked (this is usually the default for your main stream). If you want a clean mix for TikTok (no music, just you and the game), check Track 2 for your Mic and Game, but leave it unchecked for your music source. 2. Configure the Aitum Vertical Plugin Now you have to tell the Vertical plugin to use that specific track: Go to the Aitum Vertical dock. Click the Settings (Gear icon) on that dock. Go to the Streaming tab. Look for the Audio Track dropdown. Select the track you just prepared (e.g., Track 1 for everything, or Track 2 for your "Clean" mix). 3. Check for "Use Main OBS Settings" In the Aitum Vertical Streaming or Recording tabs, you might see a checkbox that says "Use main OBS settings." Leave this UNCHECKED for TikTok. TikTok needs specific vertical settings (lower bitrate, specific audio track). If you check this box, it will try to copy your main (Twitter) settings, which might cause the audio to glitch or the bitrate to be too high for a mobile platform. Pro-Tip: The "Scene Linking" Trap When you use Aitum’s Scene Linking (where switching a scene on your main monitor also switches your vertical scene), make sure the Audio Sources (Mic/Game) are added as sources in both scenes. The Litmus Test: Look at the audio bars in your main OBS mixer while you are in your "Vertical" scene. If the bars aren't moving, TikTok is hearing silence. Quick question: Are you planning to stream with music, or just game audio and mic? If you're using music, we should set up a "VOD Track" style split so you don't get hit with copyright strikes on Twitter while keeping the TikTok vibes alive.
