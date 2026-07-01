---
category: homelab
date: 2026-02-03
id: 223068
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan encountered a build failure when trying to install cemu-git from the
  AUR on CachyOS.
tags:
- cemu
- build-error
- cachyos
- aur
- compilation-failure
---
# error: failed to build 'cemu-git-2.6.r85.g492116a-1':  
error: packages failed to build: cemu-git-2.6.r85.g492116a-1

~ 7m 7s
❯ 

### USER
error: failed to build 'cemu-git-2.6.r85.g492116a-1':  
error: packages failed to build: cemu-git-2.6.r85.g492116a-1

~ 7m 7s
❯ 

### GEMINI
Building from source (cemu-git) is failing because your environment is likely missing specific dependencies or hitting a compiler conflict. Stop wasting time on the AUR build. You spent 7 minutes waiting for a failure that doesn't give you a performance gain significant enough to justify the troubleshooting headache. If you want to play games instead of debugging build logs, pivot now. 1. The Immediate Fix (Binary) Install the pre-compiled version. It is stable, updated frequently, and eliminates the "build failure" variable entirely. sudo pacman -S cemu 2. Why your build likely failed If you are determined to use the Git version, the failure usually stems from one of three "blind spots": Missing Base-Devel: You're trying to compile without the core tools. sudo pacman -S --needed base-devel Submodule Issues: Cemu relies on several submodules (like glslang or vh). If the AUR helper didn't fetch them correctly, the build dies. Disk Space/Tmpfs: AUR helpers often build in /tmp. If you have a large amount of RAM but a small /tmp partition, the build will choke. 3. The "CachyOS" Way (Optimal Performance) Since you are on CachyOS, you should be using their specific repositories which often carry pre-optimized binaries. Check if it's in the Cachy repo first: sudo pacman -S cemu Check the output: If it says Repository: cachyos, you are getting the version optimized for your CPU (x86-64-v3/v4) anyway, making the -git build redundant. The Brutal Truth You're stuck in "dependency hell" because you chose the most complex installation path for a marginal gain. The Plan: Run sudo pacman -S cemu. If it installs, open it and play. If it fails, paste the last 20 lines of the error log here. The error you provided is just a "it didn't work" notification; it contains zero diagnostic value. Would you like me to show you how to check if your CPU supports the x86-64-v4 instructions so you can verify if you're actually using CachyOS's optimizations?
