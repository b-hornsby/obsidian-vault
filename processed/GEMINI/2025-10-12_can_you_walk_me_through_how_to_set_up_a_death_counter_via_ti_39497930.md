---
category: streaming
date: 2025-10-12
id: 847753
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wanted a walkthrough for setting up a death counter via Tikfinity for
  his Dark Souls stream.
tags:
- death-counter
- tikfinity
- tiktok-studio
- streaming-overlay
- dark-souls
---
# can you walk me through how to set up a death counter via tikfinity

### USER
can you walk me through how to set up a death counter via tikfinity

### GEMINI
That's a great choice, as Tikfinity makes this type of counter very easy to manage on a TikTok stream. Since a "death counter" is a manual count and not tied to an automatic TikTok metric (like followers or gifts), the best way to do it is by setting up a Custom Goal that you control with a simple button on the Tikfinity dashboard. Here is a step-by-step guide to setting up a custom death counter using Tikfinity and adding it to your streaming software (OBS or TikTok LIVE Studio). 1. Create the Custom Counter in Tikfinity A. Access the Goal Overlays Go to the Tikfinity website and log in with your TikTok account. In the main menu, navigate to the Goal Overlays section. Click the Create New Goal button. B. Configure the Counter Select Goal Type: Choose Custom from the list of goal types (instead of Follower or Like Goal). Name the Goal: Goal Name: Enter a name like "Death Counter" or "[Game Name] Deaths." Goal Description: Enter the text you want to appear before the number (e.g., "Deaths:"). Set Initial Values: Current Value: Set this to 0. Goal Value: You can set this to a high number (like 999) since a death counter usually doesn't have a true goal. This just ensures the bar doesn't look completely full at the start. Set Goal Start: Choose Manual (this is important for a manually controlled counter). Save: Click Create Goal. C. Customize the Overlay Appearance (Optional) After creating the goal, you will be taken to the customization screen. You can change the colors, font, and style to make it look the way you want on your stream. Pro Tip: A simple text style often works best for a death counter. When you are happy with the look, find the Overlay URL at the top of the page and copy it. 2. Add the Counter to Your Stream Now you will add the URL you just copied to your streaming software. Streaming SoftwareHow to Add the CounterTikTok LIVE Studio1. Click Add Source. 2. Select Link. 3. Click Add. 4. Paste the Overlay URL and click Add Source.OBS Studio / Streamlabs1. Click the + button under Sources. 2. Select Browser Source. 3. Give it a name (e.g., "Death Counter"). 4. Paste the Overlay URL into the URL field. Position and size the counter where you want it on your stream layout. 3. Control the Counter During Your Stream The final step is controlling the count live. A. Use the Tikfinity Dashboard Keep the Tikfinity website open in a browser tab. Go back to the Goal Overlays page. Next to your "Death Counter" goal, you will see control buttons: +1: Click this every time you die to increase the counter by one. Reset: Use this button to set the counter back to zero for a new run or stream. B. Set Up a Chat Command (Optional) You can also set up a chat command so you or a moderator can increase the counter without switching screens: In Tikfinity, go to Actions/Events. Go to the Events tab and click Create New Event. Event Type: Select Comment Command. Command: Enter something like !death Action: Select Custom Goal Action. Goal: Choose your "Death Counter" from the dropdown. Action: Select Increase by 1. Save: Now, when you or a moderator types !death in the TikTok chat, the counter will automatically go up by 1.
