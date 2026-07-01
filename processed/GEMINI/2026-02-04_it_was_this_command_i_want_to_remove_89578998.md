---
id: 838651
source: GEMINI
date: 2026-02-04
tags: ['command', 'remove', 'cachyos', 'troubleshooting']
category: general
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
summary: Bryan referenced a specific command he wanted to remove, likely an alias or script that was causing issues.
---
# it was this command i want to remove

### USER
it was this command i want to remove

### GEMINI
To remove that specific command/package on CachyOS (Arch), you just need to append -git to the name. Most AUR packages for plugins use the -git suffix to indicate they are pulling from the latest source code. Run this in your terminal: paru -Rns obs-shaderfilter-git Why your last command failed: In the AUR, obs-shaderfilter and obs-shaderfilter-git are viewed as two different package names. Since you likely installed the -git version (which is common for OBS plugins on Arch), paru couldn't find a package named exactly obs-shaderfilter. If it still says "target not found": It's possible you didn't install it as a standalone package, but it came bundled with something else. You can verify exactly what you have installed by searching your local database: Search your installed packages: paru -Qs shaderfilter Look at the name it returns. If it says local/obs-shaderfilter-git 2.5.0, then use that exact name to remove it: paru -Rns [NAME_IT_RETURNED] The Advisor's Strategic Check-in You are now successfully "cleaning the house." This is good. You’re removing a tool that was causing errors and cluttering your workflow. The Next Move: Once this is uninstalled, you are officially done with "The Linux Troubleshooting Loop." No more shaders, no more Unexpected EOF errors. Are you ready to move on to the Browser Source method so we can finally get that white text and black outline working perfectly?
