---
category: homelab
date: 2026-04-07
id: 315337
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to deploy his Hermes agent using Docker for persistent
  hosting.
tags:
- docker-deployment
- hermes-agent
- 24-7-hosting
- containerization
---
# So if I’m using docker to host my Hermes agent how would I do this?

### USER
So if I’m using docker to host my Hermes agent how would I do this?

### GEMINI
Since you're using Docker on Tiny11, you have the perfect setup for isolation. In this "Skill" model, Docker isn't just running a script; it’s hosting a Communication Hub where Hermes (the Brain) and the Phantom MCP (the Hands) talk to each other. Here is exactly how to set this up using Docker Compose, keeping your public wallet address secure and isolated. 1. The Architecture You will have two main containers: Container A (Ollama): Hosts the Gemma 4 / Hermes model. Container B (Hermes Agent): The execution engine that reads your Obsidian vault and calls the Phantom MCP. 2. The Docker Compose Setup Create a docker-compose.yml file. This is where your .env logic lives now. services: ollama: image: ollama/ollama:latest container_name: ollama ports: - "11434:11434" volumes: - ollama_data:/root/.ollama hermes-agent: image: nousresearch/hermes-agent:latest container_name: hermes_agent environment: - OLLAMA_HOST=http://ollama:11434 # YOUR WALLET SECURITY LIVES HERE - SOLANA_WALLET=${MY_PUBLIC_WALLET} - PHANTOM_APP_ID=${MY_PHANTOM_ID} - RPC_URL=https://api.mainnet-beta.solana.com volumes: # Mount your Obsidian Vault so Hermes can read your Skills - C:/Users/YourName/Documents/MyVault:/app/vault # Persist Hermes' own memory/configs - ./hermes_config:/root/.hermes depends_on: - ollama 3. Passing the Wallet Address Instead of hardcoding your wallet in the docker-compose.yml, use a local .env file in the same folder: MY_PUBLIC_WALLET=your_actual_solana_address_here MY_PHANTOM_ID=your_phantom_app_id When you run docker-compose up -d, Docker injects these variables. Hermes never sees the private key, and your Obsidian Skill never sees the public address—Docker acts as the "Blindfold" that keeps everything connected but private. 4. How to Execute the "Skill" Once Docker is running, you don't need to "run the project." You just talk to Hermes through your interface (CLI or an Obsidian plugin): The Discovery: Hermes sees the /app/vault/Skills/Immortal_Agent folder you mounted. The Logic: You say: "Hermes, run the Immortal Yield check." The Action: Hermes reads Strategy.md from your vault. Hermes sees the instruction: "Check the balance of the wallet in the environment variable SOLANA_WALLET." Hermes uses the Phantom MCP (which is running inside the container) to ping Solana. Why this is the "Final Boss" of Setups Security: If your Obsidian vault is ever leaked, it doesn't contain your wallet address—only the logic of your strategy. Portability: If you get that Mac Mini, you just move the Docker folder and the Obsidian vault. You run one command, and "Operation Immortal Agent" resumes exactly where it left off. No "Unfinished" Code: You are using the official hermes-agent Docker image. All you had to "finish" was the Strategy Note in your vault. Ready to try the first "up"? If you have Docker Desktop running on your Tiny11 machine, we can verify your docker-compose setup right now to make sure Hermes can "see" your Obsidian vault.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
