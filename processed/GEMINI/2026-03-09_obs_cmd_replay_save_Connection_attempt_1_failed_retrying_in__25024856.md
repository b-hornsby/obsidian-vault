---
category: streaming
date: 2026-03-09
id: 101456
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering connection errors when trying to save a replay using
  obs-cmd.
tags:
- obs-cmd
- replay-buffer
- connection-error
- streaming-tools
- troubleshooting
---
# ❯ obs-cmd replay save
Connection attempt 1 failed, retrying in 2 seconds...
Connection attempt 2 failed, retrying in 2 seconds...
Error: ConnectionError(Connect(ConnectError(Io(Os { code: 111, kind: ConnectionRefused, message: "Connection refused" }))))

~
❯ 

### USER
❯ obs-cmd replay save
Connection attempt 1 failed, retrying in 2 seconds...
Connection attempt 2 failed, retrying in 2 seconds...
Error: ConnectionError(Connect(ConnectError(Io(Os { code: 111, kind: ConnectionRefused, message: "Connection refused" }))))

~
❯ 

### GEMINI
This error means obs-cmd is knocking on the door, but OBS isn't answering. Since you are on CachyOS, it's likely one of three specific things blocking the "handshake." 1. The "Listen" Check (Most Likely) In OBS, go to Tools → WebSocket Server Settings. Is "Enable WebSocket Server" actually checked? (Sometimes it stays unchecked after a restart). Server Port: Ensure it says 4455. If it’s something else, your obs-cmd config needs to match it. Alert: If you see a button that says "Plugin Settings" instead of the server settings, you might be looking at an old version of the plugin. OBS 28+ has this built-in natively. 2. The Config File Sync If you created the obs-cmd-toml file earlier, any typo in the password or port will cause a refusal. Let's verify the file is being read correctly. Run this to see exactly what obs-cmd is trying to do: cat ~/.config/obs-cmd/obs-cmd.toml Does the password match the one in OBS exactly? (Note: Passwords are case-sensitive). 3. The "localhost" Loophole Sometimes on Linux, localhost tries to resolve to an IPv6 address (::1) while OBS is only listening on IPv4 (127.0.0.1). Try forcing the IPv4 address in your command to see if it connects: obs-cmd -w 127.0.0.1:4455 --password YOUR_PASSWORD replay save The Advisor's Strategy: Eliminate the Friction You’re hitting "Connection Refused," which is the digital version of a door being locked. You are an enthusiast building "Operation Immortal Agent"—you cannot let a simple local network socket defeat you. The diagnostic test: Run this command in your terminal. It will tell us if OBS is even "listening" on that port: ss -tulpn | grep 4455 If nothing pops up: OBS WebSocket is OFF. Go turn it on in the OBS menu. If you see a line: OBS is listening, but your password or obs-cmd config is wrong. Which result did the ss command give you? If it's empty, we just need to flip a switch in the OBS UI.
