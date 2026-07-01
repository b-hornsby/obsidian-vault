---
category: streaming
date: 2025-09-07
id: 990105
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to configure Aitum for multistreaming to broadcast to
  multiple platforms simultaneously.
tags:
- multistreaming
- aitum
- streaming-setup
- obs-alternative
---
# How do I set up Aitum Multistream?

### USER
How do I set up Aitum Multistream?

### GEMINI
Setting up Aitum Multistream is a great choice for your powerful PC, as it allows you to multistream directly from OBS without relying on a third-party service. Here's a step-by-step guide to get you up and running: Step 1: Download and Install the Aitum Multistream Plugin Go to the official Aitum website and navigate to their products page. Find and download the Aitum Multistream plugin. It is completely free. Run the installer you downloaded. The installation process is straightforward and will automatically add the necessary files to your OBS Studio directory. After the installation is complete, close and then reopen OBS Studio. This is crucial for the plugin to be recognized. Step 2: Configure Your Main Stream (Twitch) Before setting up Aitum Multistream, you should configure your primary stream in OBS, which will be Twitch. In OBS, go to Settings > Stream. Select Twitch as your service. Connect your Twitch account or paste your Twitch stream key. Go to the Output tab and configure your main stream settings. Use your RTX 3070's NVENC H.264 encoder. Set your desired resolution (e.g., 1080p) and bitrate (e.g., 6000 Kbps). These settings will serve as the default for your other streams. Step 3: Access and Configure the Aitum Multistream Dock Once OBS is restarted, you should see a new dock for Aitum Multistream. If you don't see it, go to View > Docks > Aitum Multistream to enable it. The Aitum Multistream dock will appear. It may be a floating window, but you can drag and dock it to a convenient location in your OBS layout. Step 4: Add Your TikTok Channel In the Aitum Multistream dock, you will see a list of your "Main Outputs." This is where you'll add additional streaming destinations. Click the "+" or "Add New Output" button. You will need your stream key and server URL for TikTok. To get these: Open the TikTok app on your mobile device. Start a LIVE stream. Look for an option to get your stream key and server URL (RTMP). TikTok's interface changes, so this may be a share or settings icon. Copy the stream key and server URL. Paste the RTMP Server URL into the "Server" field and the Stream Key into the "Stream Key" field in the Aitum Multistream dock. Give the output a name, like "TikTok." Step 5: (Optional but Recommended) Set Up Aitum Vertical for TikTok For the best possible TikTok experience, you'll want a vertical (9:16) stream. Aitum has a free plugin specifically for this. Download and install the Aitum Vertical plugin from the Aitum website. Restart OBS. You will now have a second canvas in OBS that is oriented vertically. You can go to View > Docks > Aitum Vertical to see it. Create new scenes for your vertical layout. You can even link them to your main horizontal scenes so they change automatically. Once your vertical scene is configured, you can add a separate stream output for it in the Aitum Multistream dock. Click "+" in the Aitum Multistream dock. Paste your TikTok stream key and server URL. In the settings for this specific output, check the box to use the Aitum Vertical canvas as the source. Step 6: Go Live With your outputs configured, you are ready to multistream. You can either click the "Start All" button in the Aitum Multistream dock to go live on all configured platforms at once. Alternatively, you can start each stream individually. You must start your main (Twitch) stream first if you've configured your outputs to "piggyback" on it. Aitum Multistream will now handle the encoding and uploading of your streams. Your PC's powerful hardware will make this a smooth and stable process. Monitor your performance and internet upload speed to ensure everything is running perfectly.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
