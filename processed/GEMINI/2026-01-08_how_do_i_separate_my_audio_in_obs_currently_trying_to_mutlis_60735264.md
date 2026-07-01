---
category: streaming
date: 2026-01-08
id: 778248
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is trying to separate audio tracks in OBS for multistreaming to Twitch
  and TikTok, specifically to avoid music in TikTok VODs.
tags:
- obs-studio
- audio-separation
- multistreaming
- vod-audio
- twitch
- tiktok
---
# how do i separate my audio in obs? currently trying to mutlistream to tiktok and twitch. i want to be able to play music during my streams but when it comes to the vod afterward i don't want the music to be playing. twitch i know has the vod track feature in obs, but not sure how to tackle this issue for tiktok 

### USER
how do i separate my audio in obs? currently trying to mutlistream to tiktok and twitch. i want to be able to play music during my streams but when it comes to the vod afterward i don't want the music to be playing. twitch i know has the vod track feature in obs, but not sure how to tackle this issue for tiktok 

### GEMINI
To solve this, you need to stop thinking about "streaming" as one big bucket. You are running three distinct outputs: Twitch (Live), TikTok (Live), and your VODs (Recording). The reason you’re struggling is that Twitch has a dedicated "VOD Track" setting that ignores certain audio, while TikTok and standard recordings do not. To fix this, you must explicitly separate your music source and tell OBS exactly which "track" it’s allowed to travel on. 1. Isolate the Music You cannot separate audio if everything is bunched into "Desktop Audio." In OBS, go to Settings > Audio and set Desktop Audio to Disabled. Add a new source to your scene: Application Audio Capture (BETA). Select your music app (Spotify, etc.). Name it "Music." Add another Application Audio Capture for your game audio. 2. Configure the Audio Matrix This is where you decide who hears what. Right-click anywhere in the Audio Mixer and select Advanced Audio Properties. Look at the grid of 6 tracks on the right. Set them up like this: Track 1 (The "Master" Live Track): Check EVERYTHING (Mic, Game, Music). This is what people hear live. Track 2 (The "No Music" Track): Check Mic and Game. Uncheck Music. The Logic: Track 1 is for the live audience. Track 2 is your "Clean" version for VODs and TikTok. 3. Assign Tracks to Destinations Now you have to point your stream/recording outputs to the right tracks. DestinationSetting LocationTrack SelectionTwitch LiveSettings > Output > StreamingAudio Track: 1Twitch VODSettings > Output > StreamingTwitch VOD Track: 2TikTok (Restream/Plugin)Multi-RTMP Plugin SettingsAudio Track: 2Local RecordingSettings > Output > RecordingAudio Track: 2 4. The "TikTok Problem" TikTok doesn't have a "VOD Track" feature. If you stream to TikTok using Track 1, the music will be in the TikTok replay. The Brutal Truth: If you want your TikTok replays to be music-free, you must send Track 2 (the clean track) to TikTok. The Trade-off: This means your TikTok live audience will not hear your music while you are live. They only hear your voice and the game. If you are using the OBS Multi-RTMP plugin to send to TikTok, go into the plugin settings for the TikTok target and change the "Audio Track" to 2. Priority Action Plan Stop using Desktop Audio. It’s a lazy habit that prevents fine-tuned control. Use Application Audio Capture for every sound source. Remap your matrix. Spend 5 minutes in Advanced Audio Properties. Ensure Track 2 is your "Safety Track" (No Music). Sacrifice TikTok Live Music. If the goal is a clean VOD for content creation, TikTok must receive Track 2. You cannot have it both ways on TikTok because they do not support multi-track ingestion like Twitch does. Would you like me to walk you through how to set up the Multi-RTMP plugin specifically for this audio routing? How To Separate Audio Tracks in OBS Studio This video provides a visual guide on isolating individual applications and routing them to specific tracks, which is the foundational step for keeping music out of your VODs.
