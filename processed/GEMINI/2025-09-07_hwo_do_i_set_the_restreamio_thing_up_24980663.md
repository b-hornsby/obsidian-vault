---
category: streaming
date: 2025-09-07
id: 968077
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- homelab-stack
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is seeking guidance on setting up Restream.io for multistreaming.
tags:
- restreamio
- multistreaming
- streaming-setup
---
# hwo do i set the restream.io thing up

### USER
hwo do i set the restream.io thing up

### GEMINI
Setting up Restream.io with OBS Studio is a straightforward process that will allow you to stream to Twitch and TikTok at the same time with minimal hassle. Here is a step-by-step guide to get you started: Step 1: Create Your Restream.io Account Go to the Restream.io website. Click on "Sign Up" and create a free account. As we discussed, the free plan allows you to stream to two platforms, which is perfect for Twitch and TikTok. Step 2: Connect Your Streaming Channels Once you're logged into your Restream dashboard, click on the "Add Channel" button. From the list of platforms, find and select Twitch. You will be prompted to log in to your Twitch account and authorize Restream to connect. Go back to the dashboard and repeat the process to add TikTok. You will need to log in to your TikTok account. Note that TikTok requires you to get a unique stream key from their app to connect it. Follow the on-screen instructions from Restream to get the key from the TikTok app on your mobile device. Once both channels are added, they should appear in your Restream dashboard as active channels. Step 3: Set Up OBS Studio Open OBS Studio on your PC. If you don't have it, you can download it for free from the official OBS Studio website. In OBS, go to Settings (File > Settings or the "Settings" button in the bottom right corner). Click on the "Stream" tab in the left-hand menu. In the "Service" dropdown menu, select "Restream.io - RTMP". Click on the "Connect Account (recommended)" button. A browser window will pop up asking you to log in to your Restream account. This is the easiest way to connect your accounts. Alternative (Manual Setup): If for some reason the account connection doesn't work, you can do it manually. Go back to your Restream dashboard, find your unique stream key, copy it, and paste it into the "Stream Key" field in OBS. Step 4: Configure Your Stream Settings in OBS OBS and Restream will work together to give you the best settings. However, you can check them to ensure everything is optimized. In OBS Settings, go to the "Output" tab. Set the Output Mode to "Advanced". Under the "Streaming" section: Encoder: Select "NVIDIA NVENC H.264". This will use your RTX 3070 to handle the encoding, leaving your CPU free for gaming. Rate Control: Set to "CBR" (Constant Bitrate). Bitrate: Restream recommends a bitrate based on your desired quality. For 1080p, you can use a bitrate between 4500-6000 Kbps. You'll need to check your internet's upload speed to ensure it's sufficient for this. A general rule of thumb is to use a bitrate that is no more than 75% of your total stable upload speed. Keyframe Interval: Set to "2" seconds. Preset: Set to "P5: Slow" or "P6: Medium" for a good balance of quality and performance. With your RTX 3070, you can likely go with a higher-quality preset. Go to the "Video" tab in OBS Settings. Base (Canvas) Resolution: Set this to your monitor's resolution (e.g., 1920x1080). Output (Scaled) Resolution: Set this to your desired stream resolution (e.g., 1920x1080 for 1080p). Common FPS Values: Set this to "60" for a smooth stream. Step 5: Start Streaming! Make sure you have your scenes and sources set up in OBS (e.g., game capture, webcam, microphone). Go back to your Restream.io dashboard. You'll see your channels listed, and you can toggle them on or off. Make sure Twitch and TikTok are both enabled. In OBS, click the "Start Streaming" button. Your stream will now be sent to Restream's servers, which will then broadcast it to both Twitch and TikTok simultaneously. You can manage your titles and stream information directly from the Restream dashboard for both platforms at once.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
