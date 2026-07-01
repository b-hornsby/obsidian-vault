---
category: streaming
date: 2025-10-12
id: 418861
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was asking what steps were needed to get his death counter streaming
  setup working as intended.
tags:
- streaming-setup
- death-counter
- tikfinity
- tiktok-studio
- configuration
---
# so what do i need to do so this works as intended? 

### USER
so what do i need to do so this works as intended? 

### GEMINI
You have done all the hard work! Based on your screenshot, you have successfully created the counter. The only remaining steps are to connect it to your streaming software and set up the easy controls. Here is the simple, three-step checklist to get your Death Counter working on your stream: The 3-Step Checklist to Finish the Setup 1. Finalize the Counter Design & Get the Link Customize (Optional): Click the Customize button on the right to change the font, color, and size. Since you're using it as a counter, you may want to change the style from a progress bar (Style 1/7) to a simple text counter. Copy the URL: Click the Copy URL button to get the unique web address for your counter. 2. Add the Counter to Your Stream This link is how your streaming software displays the counter. SoftwareHow to Add the SourceTikTok LIVE StudioGo to Add Source $\rightarrow$ Link $\rightarrow$ Paste the URL $\rightarrow$ Click Add Source.OBS Studio / StreamlabsGo to Sources $\rightarrow$ Click + $\rightarrow$ Select Browser Source $\rightarrow$ Paste the URL in the URL field. Place and resize the counter where you want it on your stream layout. 3. Control the Counter (The Easy Way) You have two main ways to control the counter: A. The Quick Manual Way (Using the Dashboard) Keep the Tikfinity Goal Overlays page open in a separate browser tab. Whenever you die, make sure the Change Value box is set to 1 (or simply click the up arrow next to the "Change Value" box). Click the Set button. Tip: The counter will immediately update on your stream. B. The Hands-Free Chat Command Way (Highly Recommended) This lets you, or a moderator, type a command in chat to increase the count, so you don't have to switch screens. In Tikfinity, go to Actions/Events in the main menu. Go to the Events tab and click Create New Event. Event Type: Select Comment Command. Command: Type !death (or !d or anything you want to use). Go to the Action tab and click Create New Action. Action Type: Select Custom Goal Action. Custom Goal: Choose Custom Goal 1 (or whatever you named your counter). Action: Select Increase by 1. Duration: Set this to 0 (or 1 second). Save both the Event and the Action. Result: Now, whenever you or your moderator types !death in the TikTok chat, the death counter on your stream will automatically increase.
