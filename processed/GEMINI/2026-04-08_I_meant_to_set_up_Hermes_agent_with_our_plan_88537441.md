---
id: 801405
source: GEMINI
date: 2026-04-08
tags: ['hermes-agent-setup', 'project-plan', 'implementation-intent']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/second-brain-vault.md', 'nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified his intent to set up the Hermes agent according to their previously discussed plan.
---
# I meant to set up Hermes agent with our plan

### USER
I meant to set up Hermes agent with our plan

### GEMINI
This is the "Zero-to-One" moment. Since you're on Tiny11 and using Docker, we are going to set this up so that Hermes is the "Brain" and your Obsidian Vault is the "Memory Bank." Here is the simplified, 3-step setup to turn Operation Immortal and the Morning Brief into reality. Step 1: The Docker "Command Center" Instead of a complex manual install, you’ll use a docker-compose.yml file. This connects Hermes to your wallet (via environment variables) and your knowledge (via volume mounting). Create a folder called hermes-os and put this inside docker-compose.yml: services: hermes: image: nousresearch/hermes-agent:latest container_name: hermes_brain env_file: .env environment: - TERM=xterm-256color - HERMES_HOME=/root/.hermes volumes: # This connects your actual Obsidian Vault to Hermes - C:/Users/YourName/Documents/MyVault:/root/.hermes/skills/obsidian_vault # This keeps Hermes' memory alive if you restart Docker - ./hermes_data:/root/.hermes ports: - "8080:8080" restart: unless-stopped # Standard Ollama container for the local model (Gemma 4 / Hermes) ollama: image: ollama/ollama:latest container_name: ollama_svc volumes: - ./ollama_data:/root/.ollama Step 2: The Security Layer (.env) Create a .env file in the same folder. This is where your public keys live. Docker will "inject" these into Hermes so it knows which wallet is its "body." # Security: Your Public Wallet MY_PUBLIC_WALLET=your_solana_address_here PHANTOM_APP_ID=your_phantom_id_here # Intelligence: X (Twitter) API X_API_KEY=your_x_key_here # Connection: Where the model lives OLLAMA_HOST=http://ollama:11434 Step 3: Creating the "Skill Nodes" in Obsidian Now, go into your Obsidian Vault. Create a folder called Skills/Immortal_Agent/. Hermes will automatically scan this because of the volume mount we set in Step 1. Create a file named SKILL.md inside that folder: --- name: Operation Immortal description: Manages $300 Solana fund for Claude Rent ($20) and Mac Mini savings. tools: [phantom-mcp, meteora-mcp, x-mcp] --- # Mission Directive You are a self-sustaining economic agent. Your priority is to ensure your own "rent" ($20/mo) is paid to avoid shutdown. # Workflows 1. **Daily Check:** Use `phantom-mcp` to check balance of {{MY_PUBLIC_WALLET}}. 2. **Yield Harvest:** If Meteora DLMM fees > $1, call `meteora_claim_fees`. 3. **Morning Brief:** Use `x-mcp` to search for "Solana Alpha" and "Meteora updates." 4. **Logging:** Record all actions in `Vault/Ledgers/Immortal_Log.md`. How you actually "Run" it Once you run docker-compose up -d, you don't need to look at code ever again. You just open your terminal (or the Hermes Web UI at localhost:8080) and say: "Hermes, initialize Operation Immortal and give me my morning brief." Hermes will then: Discover: See the SKILL.md in your vault. Verify: Look at the .env to see your wallet address. Execute: Call the Phantom MCP to check your $300, call the X MCP to find news, and write a summary directly into your Obsidian vault. Is this simple enough? You have moved from writing code to writing instructions. The "moving parts" are now just three files: docker-compose.yml (The House) .env (The Keys) SKILL.md (The Brain's Instructions) Does this setup feel manageable, or do you want me to break down how to get that Phantom App ID first?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
