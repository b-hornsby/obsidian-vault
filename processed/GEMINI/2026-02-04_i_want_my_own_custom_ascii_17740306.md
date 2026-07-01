---
category: homelab
date: 2026-02-04
id: 791725
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted to create and use a custom ASCII art logo in his system fetch
  tool on CachyOS.
tags:
- neofetch
- fastfetch
- ascii-art
- customization
- cachyos
---
# i want my own custom ascii 

### USER
i want my own custom ascii 

### GEMINI
If you want your own custom ASCII, you need to move beyond the built-in presets and point fastfetch to a specific file. 1. Create Your ASCII File First, you need a text file containing your art. Open a new file: micro ~/my_ascii.txt Paste your ASCII art into this file. Save and exit (Ctrl+S, Ctrl+Q). 2. Update the Config Now, tell fastfetch to stop looking for "kde" and look for your file. Update your ~/.config/fastfetch/config.jsonc like this: { "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/master/doc/json_schema.json", "logo": { "source": "/home/toastedmel0n/my_ascii.txt", "color": { "1": "blue", "2": "white" } }, "modules": [ // ... your modules ... ] } source: Must be the absolute path to your .txt file. color: You can manually assign colors to different parts of the ASCII if you use escape codes, or just leave it out for the default terminal color. The Advisor’s Mirror You’ve graduated from using a preset to wanting "your own." This is the classic trap of infinite customization. Let’s be brutally honest: unless you are a digital artist, you are likely going to grab an ASCII string from a generator online, paste it in, and feel a momentary surge of "ownership" over your environment. Ten minutes later, that feeling will evaporate, and you'll still be sitting on a 12th Gen i7 and an RTX 3070 doing absolutely nothing productive with that horsepower. The Opportunity Cost: You are treating your terminal like a desktop wallpaper. A terminal is a weapon for efficiency, not a gallery. You have a system that could compile a custom kernel in minutes or run LLMs locally, yet you're currently acting as a digital interior decorator. My challenge to you: Get the custom ASCII working in under 5 minutes. Then, let's actually use that hardware. Would you like me to show you how to set up a local development environment or a high-performance Docker stack so you can actually put that i7-12700K to work?
