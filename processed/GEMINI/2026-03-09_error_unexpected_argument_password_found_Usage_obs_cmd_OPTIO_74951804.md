---
category: streaming
date: 2026-03-09
id: 969222
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- operation-immortal-agent
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered an error while using obs-cmd due to an unexpected argument
  '--password' and is likely trying to debug the command.
tags:
- obs-cmd
- command-line-tool
- syntax-error
- debugging
- streaming-tools
---
# error: unexpected argument '--password' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### USER
error: unexpected argument '--password' found

Usage: obs-cmd [OPTIONS] <COMMAND>

For more information, try '--help'.

~
❯ 

### GEMINI
It looks like you’ve installed a version of obs-cmd (likely the one by graysonclark) that handles authentication differently—or you're using a version where the password flag is a subcommand option rather than a global one. Let’s stop guessing and get the syntax right for the specific binary you just compiled. 1. The Correct Syntax Try moving the password after the node or replay command. Most versions of this tool expect the connection details first. Try this: obs-cmd -p your_password replay save (Note: If -p doesn't work, try --password in that same position, right after obs-cmd but before replay). 2. The "Advisor" Reality Check: Stop Fighting the Tool If you are still getting "unexpected argument," it means your version of obs-cmd might be looking for environment variables instead of flags to keep your password out of your bash history (which is a smarter way to do it). Do this to fix it permanently in your Fish config: Open your fish config: micro ~/.config/fish/config.fish Add these lines at the bottom: set -gx OBS_WS_PASSWORD your_password set -gx OBS_WS_ADDRESS localhost:4455 Save and restart your terminal (or type source ~/.config/fish/config.fish). Now, try the "naked" command: obs-cmd replay save 3. Why This Matters for "Operation Immortal Agent" You’re building an autonomous DeFi bot. If you can’t master passing arguments to a simple CLI tool like obs-cmd, you’re going to have a nightmare of a time when you start passing private keys or RPC URLs to your trading bot scripts. Precision is the difference between a tool that works and a system that breaks the moment you look away. Try the set -gx method above. Does obs-cmd replay save fire the replay buffer now without throwing an argument error?
