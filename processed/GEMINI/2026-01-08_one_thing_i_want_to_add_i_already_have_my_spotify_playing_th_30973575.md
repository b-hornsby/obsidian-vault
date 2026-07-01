---
category: streaming
date: 2026-01-08
id: 494669
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan is trying to integrate his existing Spotify audio setup with Voicemeeter
  into his OBS configuration to exclude it from TikTok VODs.
tags:
- obs-studio
- voicemeeter
- audio-routing
- spotify
- vod-audio
- tiktok
---
# one thing i want to add i already have my spotify playing through voicemeter banana via cable a right now. i just need to know how to plug that isolated audio in so that it doesnt playing during a tiktok vod 

### USER
one thing i want to add i already have my spotify playing through voicemeter banana via cable a right now. i just need to know how to plug that isolated audio in so that it doesnt playing during a tiktok vod 

### GEMINI
Since you’re already using Voicemeeter Banana and a Virtual Cable, you’re halfway there. The "plugging it in" part happens entirely within the OBS Audio Mixer and your Multi-RTMP plugin settings. Because TikTok does not support a dedicated "VOD Track" (it just records whatever you send it live), you have to choose: do you want TikTok viewers to hear the music live, or do you want the TikTok VOD to be clean? You cannot have both. Here is how to route your Cable-A (Spotify) to achieve a clean TikTok VOD. 1. Add the "Isolated" Audio to OBS If you haven't already, you need Spotify as its own distinct source in OBS so you can toggle it on/off for specific tracks. In OBS, click + under Sources > Audio Input Capture. Name it "Spotify Music." Select CABLE-A Output (VB-Audio Cable A) as the device. 2. Configure the Advanced Audio Matrix This is the "brain" of your routing. Right-click your Audio Mixer in OBS > Advanced Audio Properties. Locate your Spotify Music source. Assign your tracks like this: Track 1 (Live Master): Check this box. (Music is ON for Twitch live). Track 2 (Clean Master): UNCHECK this box. (Music is OFF for VODs/TikTok). Note: Ensure your Mic and Game Audio are checked for BOTH Track 1 and Track 2. 3. Connect to TikTok (Multi-RTMP Plugin) Most streamers use the "Multiple RTMP Output" plugin to reach TikTok while streaming to Twitch via the main OBS settings. Open your Multiple Output dock. Click Modify on your TikTok target. In the Audio Settings section, change it from "Get from OBS" to Track 2. The Strategy & Outcome By doing this, you have created two simultaneous versions of your stream: FeatureTwitch LiveTwitch VODTikTok Live & VODSource TrackTrack 1Track 2Track 2Music StatusAudibleMutedMuted The Brutal Reality: Because you are sending Track 2 to TikTok, your live TikTok audience will not hear your music. This is the trade-off for having a clean VOD. If you send Track 1 to TikTok so they can hear the music, the music will be "baked into" the audio, and you will never be able to remove it from the VOD. Precise Next Step Go into your OBS Settings > Output > Streaming and ensure "Twitch VOD Track" is checked and set to Track 2. This ensures Twitch knows which track is the "clean" one. Would you like me to show you how to set up a secondary "Monitor" source so YOU can hear the music while keeping it off the TikTok track?
