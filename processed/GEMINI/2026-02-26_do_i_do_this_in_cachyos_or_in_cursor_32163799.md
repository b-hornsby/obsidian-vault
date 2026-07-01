---
id: 719747
source: GEMINI
date: 2026-02-26
tags: ['development-environment', 'cachyos', 'cursor-ide', 'tool-selection']
category: coding
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is deciding whether to perform a task in CachyOS (his operating system) or within the Cursor IDE, indicating a choice of development environment.
---
# do i do this in cachyos or in cursor?

### USER
do i do this in cachyos or in cursor?

### GEMINI
In 2026, the answer is CachyOS (the system terminal). Do not run the npx auth command inside the Cursor terminal. Cursor’s terminal is "sandboxed" to your project, but the Phantom MCP needs to write a global session file to your home directory (~/.phantom-mcp/session.json) so it can be used by any script later. The CachyOS Playbook Open your standard terminal (Konsole or Alacritty) and run the "Brave Force" command there. Since CachyOS is an Arch-based powerhouse, the paths are straightforward. Run this in CachyOS: BROWSER=brave PHANTOM_APP_ID=YOUR_APP_ID_HERE npx -y @phantom/mcp-server Why this is the right move: Permission Zenith: CachyOS terminal has the direct permissions needed to create the ~/.phantom-mcp/ folder. Cursor sometimes triggers a "Permission Denied" because it treats the command as a local project task. Env Variable Persistence: If you set the BROWSER variable in CachyOS, it won't mess with Cursor's internal settings. The "Bridge" Strategy: Once you run this in CachyOS and see "Session saved," you can close the terminal and go back to Cursor. Cursor will see the session file sitting in your home directory and will be able to sign transactions automatically. One Critical "CachyOS" Detail: If BROWSER=brave doesn't work (depending on how you installed Brave), use the full binary name: BROWSER=brave-browser PHANTOM_APP_ID=... The Goal: 1. Run the command in CachyOS. 2. Brave opens. 3. You click "Approve." 4. Terminal says "Session saved." Once you see that "Session saved" message in your CachyOS terminal, tell me. We will then go back into Cursor to run the Final Test 2 and start the Meteora engine.
