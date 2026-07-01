---
id: 725370
source: GEMINI
date: 2026-02-02
tags: ['cachyos', 'ungoogled-chromium', 'download-speed']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking if ungoogled-chromium is supposed to take a long time to download on CachyOS.
---
# Is ungoogled chromium supposed to take a while to download?

### USER
Is ungoogled chromium supposed to take a while to download?

### GEMINI
Yes. If you used yay -S ungoogled-chromium, you aren’t just downloading a file—you are compiling a massive piece of software from scratch. On a mid-range machine, this can take anywhere from 2 to 8 hours, and it will peg your CPU at 100% the entire time. Chromium is one of the largest codebases in existence; building it locally is a "blind spot" many new Linux users hit. You're effectively asking your computer to manufacture a car instead of just buying one from the lot. The Fix (The "Lazy" but Smart Way) Since you are on CachyOS, you shouldn't be wasting time or electricity compiling this. You want a pre-compiled binary. Stop the current process (Ctrl+C) and run this instead: # This installs the pre-built version yay -S ungoogled-chromium-bin Why you should switch to the -bin version: Time: It takes 1 minute (just a download) vs. 5 hours (a full build). Resources: It won't melt your CPU or run you out of RAM. Updates: Every time there is a security patch, the "non-bin" version will force you to re-compile for another 5 hours. You will eventually stop updating it because it's a chore, which is a massive security risk. One Critical CachyOS Detail CachyOS actually has its own optimized repositories. Before you even use the AUR, check if their repository version suits you. CachyOS often provides V3/V4 (AVX-512) optimized builds of browsers that run significantly faster than the generic ones. Check the Cachy repositories first: sudo pacman -S ungoogled-chromium (If it’s in their repo, it will be lightning fast and optimized for your specific CPU architecture.) Would you like me to show you how to check if your CPU supports the V3 or V4 optimized repositories to squeeze more speed out of CachyOS?
