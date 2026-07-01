---
category: crypto-web3
date: 2026-02-26
id: 159592
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to ensure the Phantom MCP authentication flow opens
  in Brave (where his wallet is) instead of his default Librewolf browser.
tags:
- phantom-wallet
- browser-selection
- librewolf
- brave
- mcp-auth
---
# how do i make sure it uses the browser i have that wallet in? i use librewolf for default and brave specifically for this 

### USER
how do i make sure it uses the browser i have that wallet in? i use librewolf for default and brave specifically for this 

### GEMINI
Because you use Librewolf as your default, npx will automatically try to open the auth link there. Since your Phantom wallet and Google session are in Brave, the authentication will fail because Librewolf doesn't "know" who you are. In 2026, the cleanest way to force an npx script to use a specific browser without changing your entire OS default is to use the BROWSER environment variable. The "Brave Force" Command Run this exact command in your terminal. It tells the Node process to ignore Librewolf and launch the auth flow directly in Brave: If you are on macOS: BROWSER="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" PHANTOM_APP_ID=YOUR_APP_ID_HERE npx -y @phantom/mcp-server If you are on Windows (PowerShell): $env:BROWSER="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"; npx -y @phantom/mcp-server --env PHANTOM_APP_ID=YOUR_APP_ID_HERE If you are on Linux: BROWSER=brave PHANTOM_APP_ID=YOUR_APP_ID_HERE npx -y @phantom/mcp-server Why this is the "Advisor" choice: Zero Friction: You don't have to manually copy-paste long OAuth URLs (which often expire in seconds). Cookie Sync: Since Brave already has your Google/Phantom session, it should "Auto-Login" or just require a single click, rather than forcing you to re-type passwords. Security: This keeps your "Trading" activity inside the Brave sandbox and away from your "Hardened" Librewolf environment. One Last Check (The "Redirect" URL) Before you run that command, make sure you did the step from my last message: Go to your Phantom Developer Dashboard. Find your App. Add http://localhost:8080/callback to the Redirect URLs. If the Brave window opens and you click "Approve," your terminal should finally spit out: Session saved to ~/.phantom-mcp/session.json. Did Brave launch correctly? If so, we are ready for the final Test 2 execution.
