---
category: streaming
date: 2026-02-08
id: 563140
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was trying to blur his webcam background in OBS for streaming on CachyOS.
tags:
- obs
- background-blur
- camera
- streaming
- cachyos
---
# im trying to blur my camera background

### USER
im trying to blur my camera background

### GEMINI
Installing the plugin is only 20% of the work. If you simply apply Composite Blur to your camera source right now, you will just look like a blurry smudge. It blurs the entire source, not just the background. You are underestimating the technical requirements. Unlike Zoom or Discord, OBS does not have a native "Portrait Mode" button. To blur a background while keeping yourself sharp, you need a way to separate your body from the room. Here is the objective reality of your situation and how to fix it. The Reality Check: You Need a Mask To achieve a background blur, you need two things working together: A Mask: Something to tell OBS, "This is a human, don't blur it" and "This is the wall, blur it." The Filter: The actual blur effect (which is what you just installed). If you don't have a green screen, you are forced to use AI Background Removal. The Precise Plan 1. Install the AI Engine You need a plugin that uses machine learning to detect your silhouette. Since you are on CachyOS, do not hunt for files. Use the AUR. Run this: yay -S obs-backgroundremoval Note: This plugin is heavy. If you don't have a decent GPU, your frame rate will tank. That is the "performance tax" of not using a physical green screen. 2. The Setup (The "Sandwich" Method) You cannot do this with one single source effectively. You need to layer it: Top Layer (You): Your Camera source. Add the Background Removal filter. Set it to "Selectable" or "Mask" mode so it only shows you. Bottom Layer (The Background): A duplicate of your Camera source (use "Source Mirror" or just add the camera again). The Blur: Apply the Composite Blur you just installed to the Bottom Layer. 3. Refine the Logic If you want to do it all on one source (the professional way), do this: Add the Background Removal filter to your camera. Set the "Calculation Mode" to Mask. Add the Composite Blur filter below it in the filter list. In the Composite Blur settings, change the Mask Source to use the output of the Background Removal filter. Why You’re Likely to Fail (and how to avoid it) Lighting: If your room is dark, the AI will "eat" your hair or ears. Turn on a light. CPU Usage: AI background removal is intensive. If your stream starts lagging, you are hitting a hardware bottleneck. CachyOS's kernel helps with latency, but it can't fix a weak GPU. Dependency Hell: If obs-backgroundremoval fails to compile, it’s because you’re missing ONNX Runtime or similar headers. Read the terminal output; don't just close it. Which route are you taking: the AI plugin route or do you actually have a green screen behind you?
