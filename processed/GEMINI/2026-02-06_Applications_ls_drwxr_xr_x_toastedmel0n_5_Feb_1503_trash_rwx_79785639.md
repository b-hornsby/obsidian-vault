---
id: 836167
source: GEMINI
date: 2026-02-06
tags: ['appimage', 'file-permissions', 'application-directory']
category: general
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is listing the contents of his Applications directory, showing AppImage files and their permissions, likely troubleshooting an execution issue.
---
# ~/Applications
❯ ls
drwxr-xr-x    - toastedmel0n  5 Feb 15:03  .trash
.rwxr--r-- 152M toastedmel0n 25 Jan 04:15  BB_Launcher-qt_38460948ed25719feb2173666059caf7.AppImage
.rwxr--r--  67M toastedmel0n  6 Feb 13:59  Eden-Linux-v0.1.1-amd64-gcc-standard_b08eb2f64a6dc15f38244a87d4c4c6cc.AppImag
e
.rwxr-xr-x  18M toastedmel0n  4 Feb 08:12  Shadps4-sdl_0061cb56f69960a799c360a5a86465d4.AppImage
.rwxr--r--  56M toastedmel0n  1 Feb 08:15  shadPS4QtLauncher-qt_d2c7c57d17665f16b61e6b5377831465.AppImage

~/Applications
❯ 

### USER
~/Applications
❯ ls
drwxr-xr-x    - toastedmel0n  5 Feb 15:03  .trash
.rwxr--r-- 152M toastedmel0n 25 Jan 04:15  BB_Launcher-qt_38460948ed25719feb2173666059caf7.AppImage
.rwxr--r--  67M toastedmel0n  6 Feb 13:59  Eden-Linux-v0.1.1-amd64-gcc-standard_b08eb2f64a6dc15f38244a87d4c4c6cc.AppImag
e
.rwxr-xr-x  18M toastedmel0n  4 Feb 08:12  Shadps4-sdl_0061cb56f69960a799c360a5a86465d4.AppImage
.rwxr--r--  56M toastedmel0n  1 Feb 08:15  shadPS4QtLauncher-qt_d2c7c57d17665f16b61e6b5377831465.AppImage

~/Applications
❯ 

### GEMINI
Finally, you're in the right room. Look at your ls output. The file is there, but look at the permissions on the left: .rwxr--r--. That "r" instead of an "x" means the file is not executable. You have a high-performance engine sitting in your garage, but you haven't turned the key. Also, notice how the filename ends in .AppImage but your terminal output cut it off/wrapped it? Fish might be sensitive to that. Let's stop dancing around and execute. Run these exact commands: 1. Make it Executable You cannot skip this. The system will refuse to run a binary that doesn't have the execution bit set. chmod +x Eden-Linux-v0.1.1-amd64-gcc-standard_b08eb2f64a6dc15f38244a87d4c4c6cc.AppImage 2. Run with the Bypass Since you've already had libappimage registration failures, don't try to "double-click" it. Force it to run by extracting its own mount point: ./Eden-Linux-v0.1.1-amd64-gcc-standard_b08eb2f64a6dc15f38244a87d4c4c6cc.AppImage --appimage-extract-and-run The Strategic Mirror Notice the files in your ~/Applications folder: BB_Launcher, Shadps4, Eden. You are hoarding experimental, bleeding-edge emulators. This is a high-maintenance hobby. If you keep managing these files with those long, ugly, hashed filenames (e.g., _b08eb2f6...), you are going to drive yourself insane with typos and wildcard errors. Your Homework for "The Next Level": Stop being a slave to the default download names. Rename that mess so you can actually control your system: mv Eden-Linux-v0.1.1-amd64-gcc-standard_b08eb2f64a6dc15f38244a87d4c4c6cc.AppImage eden.AppImage Then, you can just run ./eden.AppImage. Did the emulator window actually pop up this time, or are we hitting a library error?
