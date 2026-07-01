---
category: streaming
date: 2026-02-04
id: 563420
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to uninstall a user-defined shader from OBS on CachyOS.
tags:
- obs
- shader
- uninstall
- cachyos
- streaming
---
# how do i uninstall user define shader?

### USER
how do i uninstall user define shader?

### GEMINI
To uninstall or remove the User-defined shader, you don't need to dive back into the terminal or paru. Since it is a Filter attached to your source, you remove it directly within the OBS interface. How to Remove It Right-click on the Text or Media source where you applied the shader. Select Filters. In the list of "Effect Filters" (usually the bottom half of the window), click on User-defined shader. Click the Trash Can icon (bottom left of the filters window) or right-click the filter and select Remove. Confirm the deletion. Clean Up (The "Power User" Step) If you want to completely remove the plugin from your CachyOS system (because it was causing more headaches than help), run this in your terminal: paru -Rns obs-shaderfilter -R: Remove the package. -n: Remove configuration files. -s: Remove unused dependencies that were only installed for this plugin. The Advisor's "Final Mirror" Moment You spent the last hour fighting a tool that wasn't built for your OS, writing code you didn't want to write, and troubleshooting errors that shouldn't exist—all for a 2-pixel outline. The Lesson: In the creator world, "Good enough and working" beats "Perfect but broken" every time. Shaders are for high-end visual effects; Browser Sources are for text. By removing this shader, you are removing a "failure point" from your stream. Would you like me to help you set up the Browser Source now so you can actually see your song titles with that white-on-black outline?
