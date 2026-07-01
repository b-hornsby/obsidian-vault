---
category: crypto-web3
date: 2026-02-24
id: 15277
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking about the deployment strategy for the autonomous crypto
  agent.
tags:
- deployment
- crypto-agent
- vps
- infrastructure
---
# How will this be deployed?

### USER
How will this be deployed?

### GEMINI
Deployment is where most "paper traders" fail because they underestimate the technical friction. Since it's February 2026, you aren't just writing code; you're setting up a Model Context Protocol (MCP) bridge. Here is the exact, step-by-step deployment blueprint to get your $300 working. 1. The Infrastructure (The "Connection") You will use Claude Desktop on your computer as the "Command Center" and the Phantom MCP Server as the "Hand" that signs transactions. Step A: Get your App ID. Go to the Phantom Portal (phantom.com/portal) and register. You'll get a PHANTOM_APP_ID. This is mandatory for the agent to have permission to talk to your wallet. Step B: Install the MCP Server. Open your terminal and run: npx -y @phantom/mcp-server Step C: Configure Claude. You need to tell Claude how to find your wallet. Open your claude_desktop_config.json file: macOS: ~/Library/Application Support/Claude/claude_desktop_config.json Windows: %APPDATA%\Claude\claude_desktop_config.json Paste this inside the mcpServers object: "phantom": { "command": "npx", "args": ["-y", "@phantom/mcp-server"], "env": { "PHANTOM_APP_ID": "YOUR_APP_ID_HERE" } } 2. The Logic Deployment (The "Brain") Once you restart Claude, you’ll see a 🔌 icon. Now you "deploy" the Mission Statement we discussed. You don't "upload" this as a file; you set it as the System Instructions for a new project/chat. Paste the "Big 5" logic into the chat: "Active Phantom MCP. You are now the 'Immortal Agent.' Your mission is to manage $300 to net $20/month. Use Jupiter to swap $200 into JitoSOL. Use Kamino Multiply to set a 2.5x loop. Monitor Meteora Dynamic Vaults for any yield spikes >30% APY for the remaining $100. Report all 'Reasoning' before asking for transaction approval." 3. The "Self-Sustaining" Loop Because you are using the Phantom MCP, the agent cannot drain your wallet without you clicking "Approve" on your phone or browser extension. This is your safety net. Daily Check-in: Every morning, ask Claude: "Status report: What is the current projected monthly yield, and are there any LST de-pegs to snipe?" The Recoup: On the 28th of every month, tell the agent: "Calculate total profit. If >$20, send $20 in USDC to [Address] to pay for your Claude sub." 4. The "Showcase" Deployment To get that $1,299 Mac Mini faster through grants: Screen Record: Use OBS or QuickTime to record the screen while Claude explains why it is choosing a specific Meteora vault. Public Log: Create a public "Read-Only" portfolio link in Phantom so people can watch the $300 grow (or fight to survive). The Mirror: The Real Deployment Obstacle The hardest part isn't the JSON config; it's the $300. If you don't have that yet, your first "deployment" isn't code—it's saving. Do not try to run this with $10; the gas fees and the time you spend monitoring it will cost you more than you'll ever make. Would you like me to write the specific "Safety Guardrail" prompt that prevents the agent from making trades when the Solana network "Priority Fees" are too high?
