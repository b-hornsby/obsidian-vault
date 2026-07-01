---
category: homelab
date: 2025-07-27
id: 746141
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is asking why his secondary drive is not showing up in Windows.
tags:
- drive-not-detected
- windows-11
- storage-troubleshooting
---
# why would my other drive not be popping up? 

### USER
why would my other drive not be popping up? 

### GEMINI
Based on the provided images, here's why your other drive (Drive 1 (D:)) might not be "popping up" in Steam's storage settings, even though it appears in your file explorer: Steam only recognizes Steam Library Folders: In the first image, under "Steam Settings > Storage," Steam is showing "Drive 1 (D:)" but indicates "0 B FREE OF 0 B". This typically means that there isn't a Steam Library Folder set up on that drive yet, or if there was, it's not being recognized correctly. The "Add Drive" option: In the first image, directly below "Local Drive (C:)", there's an "Add Drive" button. To make Steam recognize and utilize your D: drive for game installations, you need to click this "Add Drive" button and then select your D: drive. This will create a new Steam Library Folder on that drive. Your D: drive appears to be healthy and have plenty of space: The second image shows the "Properties" of Drive 1 (D:), indicating a "Free space" of 991 GB, which is ample. This confirms that the drive itself is present and has available storage. In summary, to make your D: drive "pop up" and be usable for Steam games, you need to manually add it as a Steam Library Folder within Steam's storage settings.
