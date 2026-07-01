---
category: streaming
date: 2025-10-12
id: 18834
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to add a death counter for a Dark Souls stream through TikTok
  Studio.
tags:
- death-counter
- dark-souls
- tiktok-studio
- streaming-overlay
- gaming-stream
---
# trying to add a death counter for a dark souls stream via tiktok studio but i'm not sure how? 

### USER
trying to add a death counter for a dark souls stream via tiktok studio but i'm not sure how? 

### GEMINI
That's a great idea for a Dark Souls stream! While TikTok Studio has its own features, the most common and flexible way to add a death counter involves using a separate counter application that outputs the number to a text file, and then having TikTok Studio read that file. Here is the general process: 1. Get a Death Counter Application You'll need a simple program that lets you press a hotkey to increase (or decrease/reset) a number and then saves that number to a text file. Popular options include: Dedicated Stream Counter Widgets: Many streaming services like StreamElements or Streamlabs offer free counter widgets that you can customize and control. You would set this up as a "Browser Source" (see step 3). AutoHotkey Script: More technical users can use a small script (like one written for AutoHotkey) that increases a number in a text file when you press a key (e.g., F12). OBS Plugins/Scripts: If you are using OBS Studio (and then capturing the OBS output or screen in TikTok Studio), OBS has built-in features and plugins for counters that can read/write to a file. 2. Set up the Counter to a Text File If you use a file-based method (like an AutoHotkey script or a dedicated program that saves to a file): The counter application will create a simple text file (e.g., deaths.txt) containing just the current number of deaths (e.g., 42). You will configure the counter to update this file every time you press your assigned hotkey. If you use a StreamElements/Streamlabs widget: The counter is usually hosted online and provides you with a unique Browser Source URL. This is what you'll add to TikTok Studio. 3. Add the Counter to TikTok Studio Now you need to get the counter to display on your stream in TikTok Studio. Method A: Using a Text File (for file-based counters) In TikTok Studio, go to your Sources. Click the + Add Source button. Look for a source type that can read from a local file, like a Text Source or a similar option for displaying static text. In the settings for the Text Source, there should be an option like "Read from file" or "Use local file". Check this box and browse to select the deaths.txt file you created/configured in Step 2. Position and style the text on your scene. Method B: Using a Browser Source (for widget-based counters like StreamElements) In TikTok Studio, go to your Sources. Click the + Add Source button. Select the Browser Source option. In the source settings, paste the Browser Source URL provided by your streaming widget service (StreamElements/Streamlabs, etc.). You may need to adjust the width and height of the source to fit the counter overlay. Position the counter overlay on your stream. 4. Test and Stream Start your game and your counter program/widget. In TikTok Studio, you should see the number appear on your screen. Press your hotkey and confirm that the number on the stream updates instantly!
