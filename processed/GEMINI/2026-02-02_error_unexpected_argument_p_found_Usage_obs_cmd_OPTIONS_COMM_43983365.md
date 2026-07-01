---
id: 215114
source: GEMINI
date: 2026-02-02
tags: ['obs-cmd', 'command-line-error', 'obs-studio', 'streaming-tools']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is encountering an error while using `obs-cmd`, indicating an unexpected argument was provided.
---
# error: unexpected argument '-p' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### USER
error: unexpected argument '-p' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### GEMINI
This is becoming a textbook example of why the Linux "bleeding edge" can be a headache. The version of obs-cmd currently in the AUR has stripped away the old flags in favor of a cleaner, hierarchical structure. It likely wants the connection details passed via Global Options (at the start) or it's expecting you to use Environment Variables so you don't have to type the password every time. Try this exact structure, which is the current standard for the newer builds: 1. The "Correct" Modern Syntax obs-cmd --password YOUR_PASSWORD replay save (Notice the double dashes --password. If it rejected -p, it’s being strict about the full word.) 2. If that fails, it's the "Position" Error Some versions of this tool require the command (replay) to come before the flags. Try: obs-cmd replay save --password YOUR_PASSWORD 3. The "CachyOS / GNOME" Professional Way (Environment Variables) If the terminal is still being stubborn, we stop fighting the syntax and use environment variables. This is better because it keeps your password out of the "Process List" where other apps could see it. Open your .bashrc or .zshrc (CachyOS usually uses ZSH by default): nano ~/.zshrc Scroll to the bottom and add these lines: export OBS_CMD_PASSWORD="YOUR_PASSWORD_HERE" export OBS_CMD_ADDRESS="localhost:4455" Save and exit (Ctrl+O, Enter, Ctrl+X). Source the file to apply changes: source ~/.zshrc. Now, try the simplest command possible: obs-cmd replay save The "Brutal Truth" Mirror We have spent 10 minutes fighting a command-line tool's syntax. This is the opportunity cost of being a Linux gamer. If obs-cmd replay save doesn't work after you set the environment variables, then obs-cmd is fundamentally broken on your current build. If that happens, ditch it immediately. Plan B (The 10-second fix): Go to your OpenDeck and use this Python one-liner instead. It bypasses the obs-cmd tool entirely and uses the standard Python library: python3 -c "from obs_websocket_py import obsws, requests; client = obsws('localhost', 4455, 'YOUR_PASSWORD'); client.connect(); client.call(requests.SaveReplayBuffer()); client.disconnect()" (You may need pip install obs-websocket-py) Does obs-cmd replay save work now that we've cleared the clutter?
