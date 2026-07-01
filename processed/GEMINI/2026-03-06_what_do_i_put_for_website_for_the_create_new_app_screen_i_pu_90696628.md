---
id: 179801
source: GEMINI
date: 2026-03-06
tags: ['phantom-app', 'app-creation', 'website-field', 'configuration']
category: crypto-web3
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was unsure what to enter for the website field when creating a new Phantom app for his self-sustaining agent.
---
# what do i put for website for the create new app screen? i put self sustained agent as the name 

### USER
what do i put for website for the create new app screen? i put self sustained agent as the name 

### GEMINI
Since you are building a self-sustained agent, the "Website" field in the Phantom Developer Portal isn't just a formality—it serves as the security anchor for your project. If you don't have a public domain yet, you have two specific options depending on your current stage: 1. The Development Approach (Localhost) If you are currently testing the agent's logic on your own machine, use your local development address. This allows the Phantom SDK to recognize your local environment as a "safe" origin. What to enter: http://localhost:3000 (or whatever port your agent's dashboard/interface is running on). 2. The Professional Approach (GitHub Pages / Vercel) If this agent is intended to be a legitimate, "immortal" entity, it needs a home. Using a placeholder like google.com will cause your App ID to fail once you actually try to trigger a wallet signature, as the origin won't match. What to enter: Use your project's GitHub repository URL or a README page. Example: https://github.com/your-username/self-sustained-agent Critical Checkpoints for an "Agent" Project: Setting the name to "Self Sustained Agent" is a solid start, but keep these two technical requirements in mind for the "Website" field: App Icon Matching: Phantom often cross-references the website provided with the App Icon you upload. If you use a GitHub URL, make sure your App Icon is also hosted or referenced clearly to avoid being flagged as "unverified" in the user's wallet. Deep Link Schemes: If your agent is running as a background process (like a CLI or a Node.js bot) rather than a web app, the "Website" field is less about the UI and more about the Redirect URI. You will eventually need to set up a custom scheme (e.g., agent://auth) in the "Redirects" section of the portal so the wallet knows where to send the transaction confirmation. The Advisor's Cold Reality If this agent is truly meant to be "self-sustained," it cannot live on localhost forever. You are creating a dependency. If your local machine goes down, the "immortality" of the agent ends. Strategy: Get a cheap .io or .com domain or use a decentralized hosting service (like IPFS or Arweave) as soon as your MVP is stable. This ensures the "Website" field points to a permanent cryptographic home for the agent's identity. Do you need the specific steps to configure the Redirect URIs for a headless/CLI agent, or are you running this through a web-based dashboard?
