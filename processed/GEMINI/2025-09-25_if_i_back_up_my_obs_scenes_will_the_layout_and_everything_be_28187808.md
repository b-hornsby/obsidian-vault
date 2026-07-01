---
id: 878803
source: GEMINI
date: 2025-09-25
tags: ['obs-studio', 'scene-backup', 'layout-preservation']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is asking if backing up OBS scenes will preserve the layout and settings.
---
# if i back up my obs scenes will the layout and everything be the same? 

### USER
if i back up my obs scenes will the layout and everything be the same? 

### GEMINI
Yes, if you properly back up your OBS Scene Collection, the layout, including the position and size of all your sources within each scene, will be the same when you restore it. What is included in an OBS Scene Collection backup? A Scene Collection in OBS Studio saves the configuration of your scenes and sources, which includes: Scene Layout: The arrangement, position, and size of all your sources (images, text, webcams, capture cards, etc.) on the canvas. Sources: Which sources exist within your scenes. Filters: Any filters applied to the scenes or sources (e.g., color correction, chroma key, audio filters). Important Considerations While the layout and all the settings are saved, there are two crucial points to keep in mind, especially if moving to a new computer: Media Files (Assets): The Scene Collection only saves the path to your media files (like images, video loops, sound effects, etc.). It does not include the files themselves. You must manually back up and place these assets in the exact same file path on the new computer, or you'll have to manually relink them in OBS. Profiles: Your Scene Collection does not save your general application settings like stream key, output settings (bitrate, encoder), and hotkeys. These are stored in a separate backup called your Profile. For a full backup, you should export both your Scene Collection and your Profile. You can export your Scene Collection and Profile from the OBS menu: Scene Collection > Export and Profile > Export. This video shows one method for backing up your entire OBS Studio setup, which would include your scenes and their layouts. Quick Tips: Backup your OBS scenes, overlays, settings, everything !
