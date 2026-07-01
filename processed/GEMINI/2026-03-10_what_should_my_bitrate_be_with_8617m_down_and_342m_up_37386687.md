---
id: 176052
source: GEMINI
date: 2026-03-10
tags: ['moonlight', 'bitrate', 'streaming-quality', 'network-speed', 'streaming-settings']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking what bitrate to use for game streaming given his 861.7Mbps down and 34.2Mbps up network speeds.
---
# what should my bitrate be with 861.7m down and 34.2m up?

### USER
what should my bitrate be with 861.7m down and 34.2m up?

### GEMINI
Since you are streaming from your PC to your Steam Deck within your own home, your Download/Upload speeds from your ISP (861.7 Mbps / 34.2 Mbps) actually don't matter. Streaming over a local network (LAN/Wi-Fi) uses your Router's internal speed, not your internet plan. Your 34 Mbps upload speed is only a bottleneck if you try to stream to your Steam Deck while you're at a coffee shop or a friend's house. For a smooth, low-latency experience on the Steam Deck (which has a 1280x800 screen), here is the "sweet spot" configuration: The Recommended Bitrate: 30 Mbps to 50 Mbps 30 Mbps: This is the "Safe Zone." It provides excellent image quality with almost zero chance of stuttering on a standard 5GHz Wi-Fi connection. 50 Mbps: This is the "Visual Fidelity" zone. If you have a high-end Wi-Fi 6 router and you're in the same room, this will make the image look native, as if the game is running locally on the Deck. Avoid 80+ Mbps: Anything higher is overkill for an 800p screen. It will increase your "Network Latency" (the time it takes for the frame to travel from PC to Deck) without providing a noticeable improvement in how the game looks. How to set it: Open Moonlight on your Steam Deck. Go to the Settings (Gear Icon). Scroll to Video Bitrate. Slide it to 35 Mbps to start. Three "Hidden" Settings for Better Performance: Because you are on CachyOS (Linux), these three tweaks in the Moonlight settings will make a massive difference: Video Codec: Set this to H.265 (HEVC). It’s more efficient than H.264, meaning you get better image quality at lower bitrates. Frame Rate: Set this to 60 FPS (or 90 FPS if you have the Steam Deck OLED). V-Sync: Disable it in the Moonlight settings and the game settings. V-Sync adds "input lag." Sunshine/Moonlight has its own way of handling frame pacing that is much faster. The "Path of Least Resistance" Test: Start at 35 Mbps. If you see a "Slow Connection" warning or the screen freezes for a split second, drop it to 25 Mbps. If it feels perfect, try pushing it to 50 Mbps to see if you can spot the extra clarity. Would you like to know how to check your "Total Latency" on the Steam Deck while playing so you can see exactly how many milliseconds of lag you have?
