---
category: general
date: 2026-02-26
id: 605588
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was sharing the output of a command to diagnose what went wrong when
  running a previous instruction.
tags:
- troubleshooting
- command-output
- error-checking
---
# this is what happened when i ran that

### USER
this is what happened when i ran that

### GEMINI
This error means the Phantom "Security Guard" is doing its job—it's blocking the login because you haven't told the Phantom Portal where the "callback" from the login should land. In 2026, the Phantom MCP server uses a local loopback to receive your login credentials, and it expects a specific address to be whitelisted. The 2-Minute Fix Go back to the Phantom Portal: Open your app in the Phantom Dashboard. Navigate to Redirect URLs: Look for a section labeled Dashboard → View App → Redirect URLs (or similar "Authentication" settings). Add the Whitelist Entry: Click "Add URL" and paste this exact address: http://localhost:8080/callback Save Changes: Ensure the change is saved before leaving the portal. Why this is happening The MCP server starts a tiny, temporary web server on your computer (port 8080) to "catch" the login code after you sign in via Gmail/Apple. If you don't whitelist http://localhost:8080/callback in the portal, Phantom's servers think a hacker is trying to hijack your session and they refuse to send the data. Once whitelisted, run the command again: PHANTOM_APP_ID=YOUR_APP_ID_HERE npx -y @phantom/mcp-server Brutally Honest Warning: If port 8080 is already being used by another app on your computer, you will see a "Port in use" error. If that happens, let me know, and we'll switch the agent to a different port. Is the "Redirect URL" field updated? If so, run the auth again and tell me if you finally see "Session saved."
