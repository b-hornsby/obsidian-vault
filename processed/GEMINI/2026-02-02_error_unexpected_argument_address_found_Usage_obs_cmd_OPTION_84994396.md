---
id: 997763
source: GEMINI
date: 2026-02-02
tags: ['obs-cmd', 'command-line-error', 'obs-studio', 'streaming-tools']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is encountering an error while using `obs-cmd`, indicating an unexpected argument was provided.
---
# error: unexpected argument '--address' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### USER
error: unexpected argument '--address' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### GEMINI
Ah, the classic open-source dilemma: the tool updated its syntax and didn't tell you. Based on that error, obs-cmd has moved to a more streamlined syntax where it expects the "connection" details as flags before the command, or it's looking for a different flag name entirely. Let's fix the syntax. Try this exact command in your terminal: obs-cmd -p YOUR_PASSWORD replay save If that also throws an error, try: The newer versions of obs-cmd sometimes use -s for server/address. Try: obs-cmd -s localhost:4455 -p YOUR_PASSWORD replay save How to verify the exact usage If you want to be 100% sure for your specific version, run: obs-cmd --help Look for the section under Options. It will show you exactly what letter it wants for the password and the address. It usually looks like this: -p, --password <PASSWORD> -w, --websocket <ADDRESS> (sometimes replaces --address) Once you find the one that works: Test it manually in the terminal one last time. Paste that working line into OpenDeck. The "Advisor" Advice: Don't hardcode the password every time If you don't want your password sitting in plain text in your OpenDeck config or terminal history, obs-cmd usually looks for environment variables. You can add this to your .zshrc or .bashrc: export OBS_PASSWORD=yourpassword Then your command becomes a very clean: obs-cmd replay save Which command ended up working when you ran --help? Let's get this finished so you can get back to CS2.
