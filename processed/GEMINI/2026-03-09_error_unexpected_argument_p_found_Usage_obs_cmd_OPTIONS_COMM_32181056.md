---
category: streaming
date: 2026-03-09
id: 624888
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered an error while using obs-cmd due to an unexpected argument
  and is likely trying to debug the command.
tags:
- obs-cmd
- command-line-tool
- syntax-error
- debugging
- streaming-tools
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
It looks like you’ve installed the modern version of obs-cmd (by grigio), which moved away from using the --password flag as a direct argument. It now uses subcommands or configuration files to keep things cleaner. Since you're on Fish, let's stop fighting the command line and set this up the right way. Step 1: Create the Config File The easiest way to get obs-cmd to work without argument errors is to give it a "home" for your credentials. Run this in your terminal to create the config directory: mkdir -p ~/.config/obs-cmd Create the config file: nano ~/.config/obs-cmd/obs-cmd.toml Paste this in (replace with your actual OBS WebSocket password): [default] host = "localhost" port = 4455 password = "your_password_here" Save and exit (Ctrl+O, Enter, Ctrl+X). Step 2: Test the "Naked" Command Now that the config exists, you don't need any flags. Try this: obs-cmd replay save If you see "Replay buffer saved" (or no error), it worked. Step 3: The "Advisor" Performance Audit You're playing Apex, Fortnite, and Valorant. These are high-movement games where frame-time consistency is everything. The Problem: Using the "Legacy X11" setting forces your GPU to handle a translation layer between Wayland and X11. It’s a minor hit, but on CachyOS (which is optimized for speed), it’s a waste of resources. The Solution: By using obs-cmd with a System Shortcut, you keep OBS in Native Wayland mode. This ensures your clips are recorded with the best possible smoothness and zero "X11 stutter." Step 4: Bind the Shortcut Now go back to System Settings → Shortcuts → Commands and change your command to simply: obs-cmd replay save One last check: If you get a "Connection Refused" error, it means OBS isn't actually running the WebSocket. Double-check Tools → WebSocket Server Settings and make sure the "Enable" box is checked. Would you like me to help you write a quick Fish function that automatically starts the Replay Buffer the moment you launch one of your games?
