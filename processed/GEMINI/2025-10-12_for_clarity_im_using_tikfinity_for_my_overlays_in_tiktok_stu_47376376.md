---
id: 552233
source: GEMINI
date: 2025-10-12
tags: ['tikfinity', 'tiktok-studio', 'streaming-overlays', 'obs-alternative']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was clarifying that he uses Tikfinity for overlays in TikTok Studio for his streaming setup.
---
# for clarity i'm using tikfinity for my overlays in tiktok studio

### USER
for clarity i'm using tikfinity for my overlays in tiktok studio

### GEMINI
That's a great clarification! Since you are using TikFinity for your overlays in TikTok Studio, you can set up a keybind to trigger your death counter command by utilizing TikFinity's Keystroke Simulation feature. Here is the step-by-step process: 1. Set up a Local Counter (Outside of TikFinity) First, you need a way to increment a number on your PC that TikFinity can read and display. The simplest way is to use a local counter app that can be controlled by a hotkey and saves the count to a simple text file. A good option is a dedicated counter app (like "Death Counter and Soundboard"): Download and Install a simple counter application. Configure a Counter: Set it to save the count to a plain .txt file (e.g., C:\Counters\deaths.txt). Set a Hotkey: In the counter app's settings, assign a simple, unused keybind (like NumPad + or F11) to increment the counter. This is the key we will make TikFinity "press." 2. Set up the Keybind in TikFinity Now you need to tell TikFinity to "press" that key every time you want the count to go up. Download the TikFinity Desktop Client: The Keystroke Simulation feature requires the TikFinity Desktop Client (not just the web interface). Make sure this is running on your PC. Create a New Action in TikFinity: Go to the Actions tab in the TikFinity web interface. Click New Action. Give it a clear name like "Add Death." Add a Keystroke Sub-Action: In the new action, click Add Sub-Action. Find the Keystroke action. Configure: Set the key to the EXACT hotkey you set up in your local counter app from Step 1 (e.g., NumPad + or F11). Save the sub-action. Add a Manual Trigger: Go to the Triggers tab for the "Add Death" action. Click Add New Trigger. Look for a trigger related to Manual Input or OBS/Stream Deck. (While TikFinity is primarily gift/chat driven, if you have a Stream Deck or a similar controller, you'll select that. If not, the most reliable way is often to use an OBS Hotkey as a middle-man, see the Bonus Step below). 3. Display the Counter in TikTok Studio Add the Counter Text: In TikTok Studio, add a Text Source. Look for an option to "Read from File" or "Text File". Browse to and select the .txt file where your counter app is saving the number (e.g., C:\Counters\deaths.txt). Test: Click the hotkey (e.g., NumPad +) in your local counter app. The number in the text file and on your screen should go up. Now, activate the "Add Death" action in TikFinity (if you found a Manual Trigger) and the number should also go up. Alternative: Use a Simple Auto-Hotkey Script If you don't want to download a separate counter application, you can use a simple script that you run on your PC to manage the counter file and keybind directly. The concept is: Run a script (like an AutoHotkey script) that detects when you press a key (e.g., F10). When the key is pressed, the script reads the number in your deaths.txt file, adds one to it, and saves the new number back to the file. You then use a Text Source in TikTok Studio to display the contents of that deaths.txt file.
