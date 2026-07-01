---
category: streaming
date: 2025-09-25
id: 888966
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble deleting an OBS scene and is seeking help to resolve
  the issue.
tags:
- obs-studio
- scene-deletion
- troubleshooting
---
# how do i delete a stubborn obs scene that won't delete when i try to remove it? 

### USER
how do i delete a stubborn obs scene that won't delete when i try to remove it? 

### GEMINI
That sounds frustrating. A "stubborn" OBS scene that won't delete usually points to a configuration issue or a bug, possibly related to a specific source within the scene or a plugin. Here are a few troubleshooting steps, ranging from simple to more advanced manual deletion: 1. Basic Troubleshooting Steps Restart OBS Studio: Close OBS completely and open it again. Sometimes, a temporary glitch prevents the deletion. Run as Administrator (Windows): Right-click the OBS shortcut and select "Run as administrator." This can resolve permission issues that might be blocking the deletion. Check for Nested Scenes: If the scene you are trying to delete is being used as a Source within another scene (a "nested scene"), you won't be able to delete it until you remove it as a source from all other scenes. Check all your other scenes' Sources lists. Check for Third-Party Plugins: If you've recently installed a plugin (like StreamElements, Move Transition, etc.), it might be interfering with scene management. Try disabling or updating your plugins. Try a Different Collection: Switch to a different Scene Collection and then switch back. Sometimes this "resets" the current collection's state. 2. Force Deletion by Editing the Configuration File (Advanced) ⚠️ Important: This involves manually editing a configuration file. Make a backup of your entire OBS configuration folder before proceeding. Close OBS Studio completely. Locate your OBS configuration folder: Windows: Press Win + R, type %appdata%\obs-studio\basic\scenes, and press Enter. macOS: You'll typically find it in ~/Library/Application Support/obs-studio/basic/scenes. Identify your Scene Collection file: The files will be named like [Your Scene Collection Name].json. If you haven't renamed your collection, it might be Untitled.json. Make a Copy: Copy the .json file you are about to edit and save it somewhere safe (like your desktop) as a backup. Edit the .json file: Open the original .json file with a plain text editor like Notepad (Windows) or TextEdit (macOS). Do not use a word processor. Search within the file for the exact name of the stubborn scene. You are looking for a section of code (it's in a format called JSON) that starts and ends with curly braces {} and contains the scene's name and its sources. It will look something like this (but much longer): { "name": "Stubborn Scene Name", "id": "scene", "version": 2, "sources": [ // ... all the sources in the scene ... ] }, Carefully delete the entire section for that scene, making sure to remove the opening { and closing } and the comma , that follows the closing brace (unless it's the very last scene in the list). Removing the wrong punctuation will corrupt your entire scene collection. Save the file and close the text editor. Re-open OBS Studio. The stubborn scene should now be gone. If your collection is corrupted, you can revert by replacing the edited file with your backup.
