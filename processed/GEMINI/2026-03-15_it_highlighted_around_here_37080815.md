---
id: 001740
source: GEMINI
date: 2026-03-15
tags: ['visual-reference', 'highlighted-area', 'troubleshooting']
category: general
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared a visual reference of a highlighted area, likely pointing to something on screen for troubleshooting.
---
# it highlighted around here: 

### USER
it highlighted around here: 

### GEMINI
That screenshot shows you’ve scrolled way too far down. You are currently in the macOS/Darwin section of the script (you can see class osx and class darwin at the top). Windows isn't there. Let's get you to the right spot. It's much higher up in the file. Follow these steps exactly: Press Ctrl+F and type exactly this: on ${DEVICE} Hit Enter. It should jump you up to a section that looks like this: case ${OS} in windows) LONGNAME="${LABEL} (on ${DEVICE})" Change that specific line to: LONGNAME="Tiny11" Save & Exit: Ctrl+S, then Ctrl+Q. Apply the change: sudo grub-mkconfig -o /boot/grub/grub.cfg How to tell you're in the right place: When you run that grub-mkconfig command at the end, look at the text scrolling in your terminal. If it says "Found Tiny11 on /dev/nvme0n1p1", you nailed it. If it still says "Found Windows Boot Manager...", you edited the wrong line. Did the terminal confirm it found "Tiny11" after you ran the config command?
