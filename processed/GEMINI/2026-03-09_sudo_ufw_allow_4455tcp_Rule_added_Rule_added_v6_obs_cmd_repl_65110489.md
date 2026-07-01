---
category: streaming
date: 2026-03-09
id: 387230
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is allowing traffic on port 4455 through the firewall, but still encountering
  authentication errors with obs-cmd.
tags:
- ufw
- firewall
- port-4455
- obs-cmd
- connection-error
- streaming-setup
---
# ❯ sudo ufw allow 4455/tcp
Rule added
Rule added (v6)

~
❯ obs-cmd replay save
Connection attempt 1 failed, retrying in 2 seconds...
Connection attempt 2 failed, retrying in 2 seconds...
Error: ConnectionError(Handshake(ConnectionClosed(Some(CloseDetails { code: Library(4009), reason: "Authentication failed." })
)))

~
❯ 

### USER
❯ sudo ufw allow 4455/tcp
Rule added
Rule added (v6)

~
❯ obs-cmd replay save
Connection attempt 1 failed, retrying in 2 seconds...
Connection attempt 2 failed, retrying in 2 seconds...
Error: ConnectionError(Handshake(ConnectionClosed(Some(CloseDetails { code: Library(4009), reason: "Authentication failed." })
)))

~
❯ 

### GEMINI
Success. The door is open (no more "Connection Refused"), but you’re being kicked out because your password is wrong or formatted incorrectly in your config file. The error Authentication failed means obs-cmd successfully reached OBS, but OBS rejected the credentials. The "Advisor" Fix: Stop Guessing, Start Executing You’re a "vibe coder"—you know that one character off in a string breaks the whole machine. Let's fix this once and for all. 1. Verify the Password (Manual Override) Run this command once. Replace YOUR_ACTUAL_PASSWORD with the one from OBS -> Tools -> WebSocket Server Settings. obs-cmd --password YOUR_ACTUAL_PASSWORD replay save If this works: Your obs-cmd.toml file is the problem. If this fails: You are either misreading the password in OBS (check for l vs 1 or O vs 0) or you have a trailing space in the OBS password field. 2. Repair the Config File If the manual command worked, your .toml file is likely broken. Open it again: micro ~/.config/obs-cmd/obs-cmd.toml Make sure it looks exactly like this (no extra spaces, no missing quotes): [default] host = "127.0.0.1" port = 4455 password = "your_password" The Brutal Advisor's Mirror You are spending significant cognitive load on a string mismatch. This is the exact kind of "wasted time" you told me to call out. The Opportunity Cost: You’ve spent the last 20 minutes on a login error. The Move: In OBS, Change the password to something dead simple (like clip123), update your config, and get back to the game. You don't need a 64-character hash for a local websocket on a machine you're already securing with a firewall. Final Check Once obs-cmd replay save returns a success message (or just doesn't error out), you are cleared for takeoff. Go to System Settings -> Shortcuts -> Commands and bind that command to your clipping key. Would you like me to help you create a "Clip Successful" desktop notification so you don't have to tab out to check if it worked?
