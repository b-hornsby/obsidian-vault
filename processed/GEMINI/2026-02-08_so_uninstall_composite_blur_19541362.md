---
category: streaming
date: 2026-02-08
id: 262389
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan asked whether to uninstall the composite blur OBS plugin, likely because
  it wasn't working correctly.
tags:
- obs
- composite-blur
- uninstall
- cachyos
- streaming
---
# so uninstall composite blur?

### USER
so uninstall composite blur?

### GEMINI
No. Do not uninstall it. You are falling into the trap of thinking one plugin is a "replacement" for the other. They are two different tools in a toolbox, and you need both to build the "NVIDIA Broadcast" effect. If you uninstall Composite Blur, you lose the ability to actually blur anything. If you don't have Background Removal, you’re just blurring your entire face. Here is the objective breakdown of why you need both: 1. The "Scissors" vs. The "Lens" obs-background-removal is your Scissors. Its only job is to look at the video feed, identify what is "human" and what is "chair/wall," and cut the background away. obs-composite-blur is your Lens. Its job is to take a image and make it look out-of-focus and professional. NVIDIA Broadcast does both at once. In OBS on Linux, you have to "pipe" the scissors into the lens. 2. The Professional Setup (The "Mask" Method) If you want that high-end look, you don't just "turn on" blur. You use Composite Blur in "Mask" mode. Here is the logic you’re currently missing: Install obs-backgroundremoval (via the AUR: yay -S obs-backgroundremoval). In your Camera filters, add Background Removal first. Set it to "Mask Only" (this turns your background black and you white). Add Composite Blur below it. In Composite Blur settings, change the Mask Source to the Background Removal filter you just created. This is the only way to get clean edges. If you use the crappy "built-in" blur inside most background removal plugins, it looks like a cheap 2020 Zoom call. Composite Blur allows for "Dual Filtering" or "Gaussian" blur which looks much closer to the NVIDIA Broadcast AI. 3. Your "New-to-Linux" Blind Spot You are looking for a single "NVIDIA Blur" button. It doesn't exist here. You are currently in the "Assembly Required" stage of Linux ownership. The Plan: Keep Composite Blur (but make sure you installed the AUR version obs-composite-blur, not that Ubuntu zip file, or it will eventually break). Install Background Removal via the AUR. Check your Drivers. If you don't have cuda and nvidia-utils installed on CachyOS, the AI will run on your CPU, your fans will scream, and your stream will lag. Do you want the specific terminal commands to verify your NVIDIA GPU is actually ready to handle this AI load, or are you going to wing it and hope your CPU doesn't melt?
