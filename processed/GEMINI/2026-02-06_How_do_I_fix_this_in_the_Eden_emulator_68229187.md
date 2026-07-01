---
category: general
date: 2026-02-06
id: 696409
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is seeking help to fix an issue he's encountering with the Eden emulator.
tags:
- eden-emulator
- emulator-issues
- software-troubleshooting
---
# How do I fix this in the Eden emulator? 

### USER
How do I fix this in the Eden emulator? 

### GEMINI
This error is a classic file management mess. It means your save directory contains folders that the emulator doesn't recognize as active profiles. In your case, the "culprit" is likely a hidden folder called .stversions, which is usually created by Syncthing (a file synchronization tool). The emulator is panicking because it sees a folder that isn't a valid profile ID. Here is the direct, objective path to fix this. The Problem Eden expects every folder in your save directory to be a specific hexadecimal string (like the one starting with D321...). The folder .stversions is metadata from your syncing software. The emulator is trying to "read" it as a save profile and failing. The Tactical Fix Click OK: This will open the file manager to the exact location of your saves. Identify the Bloat: Look for the folder named .stversions. The Solution: * Delete it: If you don't care about Syncthing's version history, just delete .stversions. The error will vanish immediately. Move it: If you want to keep those backups, move the .stversions folder out of the Eden save directory and into a different folder entirely. Restart Eden: Once the save directory only contains the valid profile folder (D321...), the error will stop appearing. The Reality Check You are likely using a sync tool to play across multiple devices (Steam Deck to PC, etc.). While syncing is smart, unmanaged syncing is a liability. * Your Blind Spot: You are letting your sync software dump its administrative trash (.stversions) into the active application path. The Risk: If you don't clean this up or configure your sync tool to ignore that folder, you risk data corruption or "UNEXPECTED BAD THINGS" (as the prompt warns) when the emulator tries to index a non-save folder as a save. Strategic Advice: Go into your Syncthing (or equivalent) settings and add .stversions to your Ignore Patterns. Stop letting your tools conflict with each other. Would you like me to walk you through how to set up an ignore pattern in Syncthing to prevent this from happening again?
