---
category: streaming
date: 2026-02-03
id: 721357
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting why adding a localhost overlay in OBS Studio causes
  metadata to disappear.
tags:
- obs-studio
- metadata-overlay
- streaming-setup
- troubleshooting
- localhost
---
# when i added http://localhost:1608/overlay the metadata disappeared?

### USER
when i added http://localhost:1608/overlay the metadata disappeared?

### GEMINI
When the metadata disappears, it’s usually because the path http://localhost:1608/overlay is technically valid but empty—you’ve turned on the radio station, but nobody is in the booth. Tuna's built-in webserver is just a "data distributor." It doesn't always come with a pretty default design pre-loaded at that URL. You have to tell it which "skin" (HTML/CSS) to use. Why it went blank: The raw http://localhost:1608 link shows JSON because that's the "brain" of the plugin. When you added /overlay, OBS looked for a file named overlay.html inside the Tuna data folder. If that file is missing or not configured in your settings, you get a blank screen. The Fix: How to get a real widget 1. Check for the "Web UI" Tab In your Tuna Settings window, look at the tabs across the top (where you saw "Basics" and "MPRIS"). If there is a Web UI tab: Go there and look for a "Theme" dropdown. Select one (like "Default" or "Spotify-like"). Once a theme is selected, http://localhost:1608 should automatically transform from text into a widget. If there is no Web UI tab: Your version of the plugin might be the "lite" version or you might need to point OBS to a local file instead. 2. The "Local File" Method (Most Reliable on Linux) Instead of using a URL, you can use the files Tuna is already saving to your computer. Go to your Browser Source settings in OBS. Check the box "Local file". Click Browse and navigate to: ~/.config/obs-studio/plugins/tuna/data/web/index.html (Or wherever your Tuna data folder is located on CachyOS). This will load the actual widget code that then talks to the local server. 3. Use a Community Skin (The "6K Labs" Look) If the default Tuna looks are too ugly for you, you can download a custom skin. Download a Tuna skin (like this popular one or community-made ones). Put those files in a folder on your desktop. In OBS, add a Browser Source, check Local file, and select that index.html. The Reality Check You’re currently stuck in the "technical weeds." 6K Labs spoiled you with a ready-made URL; Tuna is giving you the raw materials. If you just want it to look good right now: Would you like me to give you a block of Custom CSS? You can paste it into the "Custom CSS" box of your OBS Browser Source (while pointing to the raw http://localhost:1608 link) to force that text into a clean, floating bar.
