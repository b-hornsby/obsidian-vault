---
category: streaming
date: 2026-02-25
id: 524321
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to convert game clips to be compatible with his iPhone 15
  using Handbrake, indicating a problem with video encoding.
tags:
- video-encoding
- iphone-compatibility
- handbrake
- mp4-conversion
---
# i was trying to send some game clips over to my phone via local send and the mp4 would have audio but no video. i looked it up and it said it had something to do with the encoder so i downloaded handbrake. how do i convert these mp4 so they are iphone 15 compatible 

### USER
i was trying to send some game clips over to my phone via local send and the mp4 would have audio but no video. i looked it up and it said it had something to do with the encoder so i downloaded handbrake. how do i convert these mp4 so they are iphone 15 compatible 

### GEMINI
The reason your video isn't showing up is likely due to the High Profile or Level of the original encoder (common with PC game captures like OBS or Shadowplay), which exceeds what the iPhone’s native Photos app can decode, even if it's an MP4. Since you've already downloaded Handbrake, here is the direct, no-fluff way to fix this for an iPhone 15. 1. The "Set and Forget" Method (Presets) Handbrake has built-in presets that handle the math for you. Open Handbrake and drop your video file in. Click the Presets button (top right or top menu). Navigate to Devices > Apple 1080p60 Surround (or Apple 2160p60 4K HEVC if you want to keep 4K quality). Ensure the Summary tab shows the Format as MP4. Click Start Encode. 2. Manual "Perfect Compatibility" Settings If you want to ensure it works every single time without losing quality or ending up with a massive file: Summary Tab: * Format: MP4 Check Web Optimized (this helps with local transfers and playback start times). Video Tab: Video Encoder: H.264 (x264) — Most compatible OR H.265 (x265) — Best for iPhone 15 to save space. Framerate: Same as source (and check Constant Framerate; iPhones hate Variable Framerate game clips). Quality: Set the slider to RF 20-22. (Lower number = higher quality). Encoder Profile: Main or High. Encoder Level: 4.1 or 4.2 (This is usually why your original didn't work). Audio Tab: Codec: AAC (CoreAudio) or AAC (avcodec). Bitrate: 160 or 192. 3. Why it failed (The "Blind Spot") You are likely recording game clips in a high-bitrate format intended for editing or YouTube, not mobile playback. If you use OBS to record, change your output settings to "Rec. 709" color space and "Main" profile next time to avoid having to run Handbrake every single time. Pro Tip: If you have a lot of clips, you can click "Add to Queue" for each one and then "Start Queue" to process them all at once while you do something else. Would you like me to show you the specific OBS/recording settings to use so you don't have to convert them in the future?
