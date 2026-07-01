---
category: streaming
date: 2026-02-08
id: 113495
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wanted to create a folder for his Stream Deck profile in OpenDeck on
  CachyOS.
tags:
- opendeck
- stream-deck
- folder
- cachyos
- streaming
---
# how do i make a folder for my stream deck  in opendeck 

### USER
how do i make a folder for my stream deck  in opendeck 

### GEMINI
You are moving from software filters to hardware workflow. In the open-source world—specifically with OpenDeck (or similar tools like Boatswain or Streamdeck UI)—the concept of a "Folder" isn't a magical container like it is on Windows. In Linux Stream Deck utilities, a folder is simply a Page Link. You aren't "opening a folder"; you are "switching the layout." The Brutal Reality of Open-Source Hardware Control The Elgato software on Windows spoils you with "Create Folder." On Linux, you have to build the navigation logic yourself. If you don't set a "Back" button, you will trap yourself on a page with no way home. How to Build a "Folder" (The Page Method) Identify the Page System: Look at the top or side of the OpenDeck interface. You will see "Page 1," "Page 2," etc. Think of Page 1 as your Home, and Page 2 as your Folder. Create the "Enter" Button (On Page 1): Select an empty button on Page 1. In the action/command list, look for "Switch Page" or "Change Deck". Set the target to Page 2. Upload your "Folder" icon here. Create the "Back" Button (On Page 2): Crucial Step: Switch the UI view to Page 2. Pick a button (usually the top-left or bottom-left). Set the action to "Switch Page" and target Page 1. Use a "Back" or "Up" arrow icon. If you forget this, you'll have to reach for your mouse to reset the deck manually—defeating the purpose of the hardware. Fill the "Folder": Now stay on Page 2 and map your specific "Folder" actions (like your Blur toggles, scene switches, or media keys). Strategic Advice: Don't Play "Folder Inception" One of the biggest mistakes people make when setting up a Stream Deck is burying actions three or four folders deep. The Opportunity Cost: Every click to open a folder is a half-second of "dead air" or distracted eyes during a stream. The Pro-Level Setup: Use "Folders" (Pages) only for things you do infrequently (e.g., changing lighting scenes, launching apps). The "Mirror" Test: If you find yourself clicking into a folder more than three times an hour, that button shouldn't be in a folder. It belongs on Page 1. Your Next Step Since you are on CachyOS, are you using the Flatpak version of OpenDeck or the AUR version? If you are using the Flatpak, you might run into permission issues where the app can't execute your Linux scripts or talk to OBS. You’ll need to use Flatseal to give it access, or better yet, switch to the native AUR package for direct system access. Do you want the command to fix those permissions, or are your buttons already working?
