---
category: streaming
date: 2026-03-09
id: 187995
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is confirming the correct password to use for obs-cmd authentication.
tags:
- obs-cmd
- password
- authentication
- obs-studio
- streaming-setup
---
# the password is the one in show connect info under server password right? 

### USER
the password is the one in show connect info under server password right? 

### GEMINI
Yes, that is exactly the one. In OBS → Tools → WebSocket Server Settings, when you click Show Connect Info, use the string found in the Server Password field. The Advisor's Quick Audit: If it’s still failing after you’ve copied that password, check for these three "silent killers" that happen during a copy-paste: The Invisible Space: Sometimes clicking the "Copy" button or highlighting the text adds a sneaky space at the end. In your .toml file, make sure it’s "password" and not "password ". Authentication Toggle: Ensure the checkbox for "Enable Authentication" is actually checked in OBS. If you're sending a password to a server that has authentication off, it will occasionally throw an error. The "Apply" Trap: If you just changed the password or enabled the server, make sure you hit Apply or OK at the bottom of the OBS window. OBS doesn't always commit those changes the instant you type them. The Final Test Run this one last time in your terminal to be 100% sure: obs-cmd --password PASTE_IT_HERE replay save If you see "Replay buffer saved", you're done. Stop fighting the configuration. Go map that key in your System Settings and get back to your stream. You've spent enough time on the plumbing; it’s time to actually use the sink. Once you've confirmed it works, would you like me to show you how to set up a notification that pops up on your screen saying "Clip Captured" so you have total peace of mind during a match?
