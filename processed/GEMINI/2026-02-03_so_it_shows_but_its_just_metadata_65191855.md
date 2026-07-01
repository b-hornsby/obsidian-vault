---
category: general
date: 2026-02-03
id: 587880
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan is confused because something is showing up as metadata only, but the
  context is missing.
tags:
- metadata
- unspecified-issue
---
# so it shows but its just metadata? 

### USER
so it shows but its just metadata? 

### GEMINI
What you are seeing in that second screenshot is the raw JSON data. This is the "brain" of the plugin talking, and while it’s proof that Tuna is successfully grabbing your music info from SoundCloud (via MPRIS), it’s not exactly "stream-ready." To turn that wall of text into a clean widget like 6K Labs, you need to use one of the two following methods: Method 1: The "Ready-Made" Widget (Easiest) Tuna has a dedicated overlay page built into its webserver that is designed to look good, not just show code. Correct the URL: In your OBS Browser Source, don't just use the base IP. Try adding /overlay or /lyrics to the end of your URL (e.g., http://localhost:1608/overlay). Check Themes: Look for a Web UI tab in your Tuna settings. There is often a dropdown there to select a "Theme." If you select one, the URL will serve a styled widget instead of raw metadata. Method 2: Use a Community Preset Because the default Tuna output is "ugly," the community has built high-quality HTML/CSS templates that "read" that metadata and make it look professional. Download a Template: Search for "Tuna OBS Presets" or "ZeAntwan Now Playing Widget". These are usually small folders with an index.html file. Add to OBS: 1. Add a Browser Source. 2. Check the "Local File" box. 3. Select the index.html file you downloaded. 4. The widget will automatically "pull" the data from your running Tuna server. Method 3: The "DIY" OBS Method (Most Stable) If you don't want to mess with web servers, you can build the widget inside OBS using the files Tuna is already creating for you. Album Art: Add an Image Source and point it to /home/toastedmel0n/cover.png. Song Title: Add a Text Source, check "Read from file," and point it to the text file you configured in the "Song info outputs" section of your first screenshot. Style It: Use OBS filters like "Scroll" on the text or "Mask" on the image to make it look exactly how you want. The Brutal Advice: You have the data working (which is the hard part on Linux). Stop staring at the JSON metadata and decide: do you want a pre-made skin, or do you want to build your own layout in OBS? Would you like me to find a specific minimalist CSS template you can just paste into your Browser Source to fix the look instantly?
