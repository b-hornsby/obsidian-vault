---
category: crypto-web3
date: 2026-02-24
id: 452053
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to set up or run the crypto agent project on his CachyOS
  machine.
tags:
- cachyos
- setup
- crypto-agent
- local-development
---
# How would I do this on cachyos?

### USER
How would I do this on cachyos?

### GEMINI
Operating on CachyOS (a high-performance Arch Linux derivative) is actually a massive advantage for this project. Because CachyOS uses the x86-64-v3/v4 instruction sets and the BORE scheduler, your agent’s local processing and "thinking" via the CLI will be snappier than on a standard Windows/Mac bloat-ware install. However, since Anthropic does not officially support a native Linux desktop app (yet), we have to use the CachyOS Repos or the AUR to bridge the gap. 1. The Installation (The CachyOS Way) You have two main paths. I recommend Path A for the most "Agentic" experience. Path A: The Native CLI (Recommended) CachyOS actually carries claude-code in its own repositories. This is a terminal-based agent that is faster and more powerful for automation than the desktop app. Install Claude Code: sudo pacman -S claude-code Authenticate: claude auth login Run the Agent: Just type claude in your terminal. It now has access to your shell and can run the MCP tools directly. Path B: The GUI (Unofficial) If you really want the Desktop window, use the AUR: Install via paru or yay: paru -S claude-desktop-appimage # OR paru -S claude-desktop-bin 2. The Phantom MCP Setup on Linux Phantom's MCP works perfectly on Linux via Node.js. Install Node/NPM: sudo pacman -S nodejs npm Configure the Config File: Your config file on CachyOS is located at: ~/.config/Claude/claude_desktop_config.json. If it doesn't exist, create it. Add the Phantom Server: (Same JSON as before, but ensure npx is in your path). { "mcpServers": { "phantom": { "command": "npx", "args": ["-y", "@phantom/mcp-server"], "env": { "PHANTOM_APP_ID": "YOUR_PHANTOM_PORTAL_ID" } } } } 3. The "CachyOS Edge" for your Showcase Since CachyOS is built for speed, use this as part of your "Grant Pitch" to Solana/Jupiter: The Pitch: "My agent runs on a high-performance CachyOS (Arch) kernel, reducing latency between signal detection and transaction signing via the Phantom MCP." The Setup: Use btop or htop in a split terminal window while your agent runs. It looks incredibly professional and "hardcore" for your video showcase. 4. The "Immortal Agent" Launch Script On Linux, you can automate the bot's "start-up" with a simple alias. Add this to your ~/.zshrc or ~/.bashrc: alias launch-agent='claude "Check my $300 balance on Solana. Are there any de-pegs >0.5% on JitoSOL? If so, propose a swap using the Opportunity Fund."' The Mirror: Why CachyOS is the "Honest" Choice By choosing CachyOS, you are removing the "OS lag" that could kill a trade. You are treating this $300 like a high-frequency operation. You aren't playing around with a consumer OS; you're building on a performance-tuned machine. The only risk: CachyOS is rolling release. Do not run a full system upgrade (pacman -Syu) right before a high-volatility market event. If your kernel breaks, your agent stays offline, and you miss the yield that pays for your subscription. Would you like me to help you write a systemd service script that keeps your agent running in the background of your CachyOS install so it never misses a "Harvest" window?
