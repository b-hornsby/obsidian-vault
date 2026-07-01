---
id: 365716
source: GEMINI
date: 2026-02-02
tags: ['ascii-art', 'terminal-customization', 'cachyos']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted step-by-step instructions to change the ASCII art displayed in his CachyOS terminal.
---
# give me a step by step guide on how to change the ascii art

### USER
give me a step by step guide on how to change the ascii art

### GEMINI
Stop treating your terminal like a coloring book and start treating it like a tool. If you’re going to change the branding, do it efficiently so you can get back to work. Here is the direct, technical path to swapping that logo. Step 1: Access the Configuration CachyOS uses Fastfetch. You need to move the config from the system protected area to your user space so you can actually manipulate it without permission errors. Run this command to ensure you have a local config to edit: mkdir -p ~/.config/fastfetch && cp /usr/share/fastfetch/presets/cachyos.jsonc ~/.config/fastfetch/config.jsonc Step 2: Open the File Use a terminal editor. If you don't know how to use vi, use micro or nano. micro ~/.config/fastfetch/config.jsonc Step 3: The Modification Look for the "logo" block at the top of the file. You have two ways to handle this: Option A: The Built-in Swap (The Lazy Way) Change the "source" value to any major distribution name (e.g., "arch", "ubuntu", "gentoo"). Fastfetch has these baked in. "logo": { "source": "arch", "padding": { "top": 1 } }, Option B: Your Own ASCII (The Custom Way) Create a text file at ~/.config/fastfetch/my_art.txt. Paste your ASCII art into that file and save it. Update the config.jsonc to point to that specific path: "logo": { "source": "/home/yourusername/.config/fastfetch/my_art.txt", "color": { "1": "blue", "2": "white" } }, (Note: Replace yourusername with your actual Linux username.) Step 4: Verify and Force Save the file (Ctrl+S then Ctrl+Q in micro). Now, run: fastfetch The Reality Check: If you run neofetch and the old logo still appears, it’s because CachyOS has aliased neofetch to use a different system preset. Stop using the neofetch command. Use fastfetch. If you want it to appear every time you open the terminal, add fastfetch to the bottom of your ~/.zshrc or ~/.bashrc. Why this matters You are currently focused on the visual wrapper. If your goal is to be a power user, the next logical step isn't more "ricing"—it's understanding why CachyOS uses jsonc (JSON with Comments) and how to parse system data. Would you like me to provide a script that randomly cycles through different ASCII logos every time you launch, or are you ready to look at your kernel boot parameters to actually speed up the machine?
