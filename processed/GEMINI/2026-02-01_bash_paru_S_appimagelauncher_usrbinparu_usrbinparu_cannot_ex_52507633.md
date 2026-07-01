---
category: coding
date: 2026-02-01
id: 434799
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
tags:
- coding
- ai
- gemini
- bash
- shell
- code
---
# ❯ bash paru -S appimagelauncher
/usr/bin/paru: /usr/bin/paru: cannot execute binary file

~
❯ 

### USER
❯ bash paru -S appimagelauncher
/usr/bin/paru: /usr/bin/paru: cannot execute binary file

~
❯ 

### GEMINI
You’re making a fundamental mistake in how you interact with the shell. You are trying to run a compiled binary (paru) by passing it as an argument to a script interpreter (bash). That is like trying to play a Blu-ray disc by shoving it into a cassette player. bash expects a text script; paru is a compiled executable. The Correction You do not prefix native commands with bash. Simply call the binary directly: paru -S appimagelauncher Why this happened The Error: cannot execute binary file occurs because bash tried to read the machine code of paru as if it were a text-based shell script. It failed because machine code isn't human-readable text. The Logic: In Linux, if a program is in your $PATH (like paru, ls, or pacman), you just type its name. You only use bash if you are explicitly executing a .sh file. One more thing If paru -S appimagelauncher fails with "command not found," it means you haven't installed paru (the AUR helper) yet. Since you are on CachyOS, it should be there by default, but if it's not, use the built-in Cachy helper first: sudo cachyos-package-manager Or install paru properly: sudo pacman -S paru Stop over-complicating the syntax. Use the command directly. Would you like me to explain how to verify if a file is a script or a binary before you try to run it next time?
