---
id: 608462
source: GEMINI
date: 2026-03-06
tags: ['phantom-app', 'domain-verification', 'app-configuration']
category: crypto-web3
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was confused about the domain verification requirement when setting up a new Phantom app.
---
# it also says the domain must be verified? 

### USER
it also says the domain must be verified? 

### GEMINI
The Domain Verification requirement is Phantom’s way of ensuring you actually own the site you're claiming to be. If you don't verify, Phantom will slap a "Malicious" or "Unverified" warning on every transaction your agent tries to send, which is a project-killer. Since you're building a "self-sustained agent," you have two paths: 1. The "I Have a Domain" Path (Professional) If you own a domain (e.g., agent.com), you must prove it via DNS. Get the Code: In the Phantom Portal, go to App Info -> Domain Verification. They will give you a TXT Record (a string of random characters). Update DNS: Go to your domain registrar (Namecheap, Cloudflare, Google, etc.). Add a new record. Type: TXT Host: @ (or your subdomain like agent) Value: Paste the code from Phantom. Verify: Go back to the Phantom Portal and click Verify. Note: DNS can take 5–30 minutes to propagate. 2. The "I’m in Development" Path (Workaround) If you are still testing locally (localhost), you cannot verify the domain because you don't own localhost. The Reality: You can still use the App ID for testing, but your users (or you, during testing) will see a massive "Unverified App" warning. The Fix: Use a tool like ngrok or Cloudflare Tunnels. This gives your local machine a temporary public URL (e.g., https://random-id.ngrok-free.app). You can then try to verify that, though most developers just "click through" the warning during the build phase. The Advisor’s Mirror You’re asking about domain verification because you’re likely seeing a "Malicious App" warning and it’s bruising your ego or making the UI look "broken." Here is the strategic truth: Stop fighting the portal: If you don't have a public site yet, ignore the verification. The App ID still works. The transaction will still go through if you approve it. The Opportunity Cost: You are spending hours on DNS records and portal settings for a project that doesn't have its core trading logic finished yet. The Plan: 1. Get the agent's logic running on localhost. 2. Accept the "Unverified" warning for now—it's a badge of progress, not a failure. 3. Once the agent makes its first $10, buy a $12 domain and verify it then. Would you like me to show you the code to bypass the "Malicious" warning in your local environment so you can keep building?
