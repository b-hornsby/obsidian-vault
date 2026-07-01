---
category: streaming
date: 2025-10-12
id: 786407
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was stuck on how to trigger the death counter automatically during
  his stream.
tags:
- death-counter
- trigger-mechanism
- tikfinity
- streaming-overlay
---
# i need to be able to trigger the counter though thats the part im stuck on 

### USER
i need to be able to trigger the counter though thats the part im stuck on 

### GEMINI
You are right! Getting the trigger set up is the most important part for a Death Counter. Since you've already created the goal (the screenshot confirms that), we now need to set up the method for increasing the count. Here are the three best ways to trigger your Death Counter, from simplest to most advanced: Method 1: The Manual Click (Simplest) This method only requires the main Goal Overlays page you are currently on. Set the Increment: Make sure the Change Value box (just above the Set button) is set to 1. To Trigger a Death: Whenever you die, click the Set button. The counter will instantly update on your stream. Pro Tip: Keep the Tikfinity Goal Overlays page open on a second monitor or on your phone for easy access. Method 2: The Chat Command (Best for Streamer/Mod Control) This is the most common and easiest method for live streaming. You, or a mod, just type a simple command in your TikTok chat. A. Create the Action (What happens when it's triggered) Go to the main Tikfinity menu and click Actions/Events. Go to the Actions tab. Click the Create New Action button. Name: Increase Death Counter Action Type: Choose Custom Goal Action. Custom Goal: Select Custom Goal 1 (or whatever you named your goal). Action: Select Increase by 1. Duration: Set this to 0. Click Save. B. Create the Event (How it gets triggered) Stay on the Actions/Events page and go to the Events tab. Click the Create New Event button. Event Type: Select Comment Command. Command: Type the command you want to use, like !death Tip: Use something short, like !d Action to Call: Select the action you just created: Increase Death Counter. Click Save. To Trigger a Death: Type !death (or your command) in your TikTok chat. Method 3: The Hotkey (Best for Gaming) If you have Tikfinity's Windows application installed, you can bind the counter to a key on your keyboard so you don't have to click anything on a second screen. Create the Action: Follow Step 2A above to create the Action called Increase Death Counter (Custom Goal, Increase by 1). Create the Event: Go to the Events tab. Click Create New Event. Event Type: Select Key Press. Key: Click the box and press the key you want to use (e.g., a key like F10 or a number pad key you don't use in your game). Action to Call: Select Increase Death Counter. Click Save. To Trigger a Death: Just press the assigned key (e.g., F10) while the Tikfinity desktop app is running.
