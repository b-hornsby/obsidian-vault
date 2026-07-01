---
category: streaming
date: 2025-09-25
id: 733686
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- homelab-stack
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about the best TikTok encoder settings for OBS using Aitum.
tags:
- tiktok-streaming
- encoder-settings
- obs-studio
- aitum
---
# what are the best tiktok encoder settings when trying to setup in obs via aitum? 

### USER
what are the best tiktok encoder settings when trying to setup in obs via aitum? 

### GEMINI
The specific "best" encoder settings for streaming to TikTok through OBS with Aitum (likely using the Aitum Vertical or Multistream plugins) can depend on your PC's hardware and internet connection, but here are the general recommendations for a high-quality, stable stream: General Encoder Settings (OBS Output Settings) Since TikTok streaming is typically a vertical format (9:16), you'll often be using the Aitum Vertical plugin to manage a separate vertical canvas and output. If you are using Aitum Multistream, the TikTok output might be configured as a secondary stream with its own settings. SettingRecommended ValueNotesEncoderNVIDIA NVENC (New) or AMD VCE/AMFHardware encoding (GPU) is highly recommended to offload work from your CPU and is generally required for multistreaming. Use x264 only if you have a very powerful CPU and no dedicated GPU encoder, but this is less common for modern streamers.Rate ControlCBR (Constant Bitrate)Provides a consistent stream quality and is the standard for most platforms.Bitrate2,500 - 4,500 KbpsTikTok often favors a lower bitrate than platforms like Twitch or YouTube. Start around 3,000 Kbps for 720p 30fps and go up to 4,500 Kbps for 1080p 30/60fps, but stay within TikTok's recommended limits and what your internet can handle consistently.Keyframe Interval2 secondsThis is the standard for most streaming platforms, including TikTok.PresetQuality or Max QualityBalances quality with performance. Use Max Quality if your GPU has headroom; otherwise, stick to Quality.ProfileHighProvides the best encoding features for visual quality.Look-AheadChecked (for NVENC)Improves quality by adapting the bitrate more intelligently.Psycho Visual TuningChecked (for NVENC)Improves the visual quality of complex scenes like fast-paced gameplay.Max B-Frames2A common standard for streaming. Video Settings (OBS Video Settings) You will likely set your Base (Canvas) Resolution to your monitor's resolution (e.g., $1920\times1080$), but the important setting is the Output (Scaled) Resolution for the TikTok stream. SettingRecommended ValueNotesOutput (Scaled) Resolution1080x1920 or 720x1280Vertical resolutions are critical for TikTok. Use $1080\times1920$ if your internet and hardware can handle the higher bitrate; otherwise, $720\times1280$ is a great, stable choice.Common FPS Values30 or 6030 FPS is easier to stream and common on mobile platforms. Use 60 FPS for smooth motion, but it requires a higher bitrate and more processing power. Audio Settings SettingRecommended ValueNotesSample Rate48 kHzThe standard professional audio sample rate.ChannelsStereoStandard for most content. Aitum Specific Considerations Aitum Multistream: If you are using this plugin to stream to multiple platforms (e.g., Twitch/YouTube and TikTok), you can often override the default OBS Output settings for the TikTok destination within the Aitum Multistream dock to use a lower resolution/bitrate for the vertical stream, saving resources on the main stream. Aitum Vertical: This plugin creates a second canvas in OBS for your vertical content, allowing you to design your layout specifically for $9:16$. You would then configure a second stream output (either via Aitum Multistream or a virtual camera) using the settings above. Virtual Camera: If you are using the Aitum Vertical output as a Virtual Camera to feed into the TikTok Live Studio app, the encoding is often handled by the TikTok app, so your OBS output settings won't apply directly. However, ensuring your Aitum Vertical canvas is set to $1080\times1920$ or $720\times1280$ at $30$ or $60$ FPS is still important. Pro-Tip: Always run a test stream to check for dropped frames and visual quality before going live. If you see high CPU or GPU usage, try lowering the bitrate or switching your encoder preset to a faster option (e.g., from "Quality" to "Performance").


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
