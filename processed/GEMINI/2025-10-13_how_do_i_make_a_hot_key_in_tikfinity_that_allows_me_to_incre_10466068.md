---
category: streaming
date: 2025-10-13
id: 478907
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to create a hotkey in Tikfinity to increase a goal during his
  TikTok streams, avoiding the need to type commands in chat.
tags:
- tikfinity
- hotkeys
- goal-increment
- tiktok-studio
- streaming-tools
---
# how do i make a hot key in tikfinity that allows me to increase a goal rather than having to type a command in chat? streaming via tiktok studio 

### USER
how do i make a hot key in tikfinity that allows me to increase a goal rather than having to type a command in chat? streaming via tiktok studio 

### GEMINI
While a direct "Hotkey" option to manually increase a goal's progress in TikFinity isn't a standard feature like it is in some other streaming software, you can achieve this effect by setting up a private, triggerable action that increments your goal. This method uses the TikFinity Desktop App and a feature designed for interactive games or commands, but you can repurpose it for your own use. Here's a general outline of the steps: 1. Install and Set Up the TikFinity Desktop App You will need the TikFinity Desktop App running on your streaming computer for local hotkeys to work. It handles the local commands like keystrokes. 2. Create a "Keystroke" Action in TikFinity Go to the 'Actions & Events' Tab on the TikFinity website. Create a New Action. Choose the Action Type as Keystroke. Specify a unique, non-used key on your keyboard (e.g., F12, a combination like Ctrl+Shift+Z, etc.). This is the "hotkey" that TikFinity will monitor for. Save this action. 3. Create a Custom Goal Increment Event TikFinity doesn't have a built-in "Hotkey Triggers Goal" option, but you can use an existing trigger (like a unique, high-value Gift) and then set up a Manual Trigger (like a webhook) to simulate it. The most common workaround for a manual trigger is a private command, which unfortunately brings you back to a chat command, or an external webhook. A More Direct Workaround Using the Goal's Admin Command: A much simpler approach, if you want to avoid complex setups, is to use the Goal Admin Command but only in a way that you can see it. Find your Goal's Admin Command: When you set up a goal in the 'Goal Overlays' section, TikFinity provides an Admin Command (e.g., !goal inc 50 or !followergoal add 1). This is what you've been trying to avoid. Use a Private Chat/Message: Instead of typing it into your public TikTok Live chat (which viewers would see), you can usually type this command into a private chat/DM with the TikFinity bot (if it supports this, check TikFinity documentation) or another private, administrative chat interface provided by the TikFinity platform. If a pure hotkey is an absolute must, here's the more complex approach that relies on the Desktop App's keystroke functionality, but it's not a direct goal increment: Set up an "External" Trigger (Webhook): You would need a third-party tool (like a local script or a service like StreamerBot, which integrates with TikFinity) that can recognize a keyboard hotkey press and then execute a Webhook URL. Create a Webhook Event in TikFinity: In the Actions & Events tab, create a new Event. Choose the Event Type as Webhook. This will give you a unique URL. Create an Action for the Webhook: Go to the Actions section. Create an action that, when the Webhook is triggered, executes the Goal: Increment action. Connect Your Hotkey to the Webhook: Use a program like AutoHotkey or your other streaming software's hotkey function (if it supports sending web requests) to run a script that sends a request to the TikFinity Webhook URL you created in step 2 whenever you press your desired hotkey. Recommendation: The Admin Command method (if you can use it privately, like in a bot's DM or a platform's admin panel) is the quickest and most reliable way to manually increment a goal without typing it into the public chat. If you must use a physical key, the External Webhook method is required, but it is much more technical.
