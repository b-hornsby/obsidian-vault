---
id: 948458
source: GEMINI
date: 2026-04-07
tags: ['docker-24-7', 'telegram-bot', 'agent-accessibility', 'always-on']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/people/dad.md']
summary: Bryan was confirming that Docker enables 24/7 agent uptime and asking about setting up a separate Telegram account to interact with his agent remotely.
---
# So it can stay on 24/7 because of docker and I can make a separate telegram account specifically for this agent and talk to it from anywhere?

### USER
So it can stay on 24/7 because of docker and I can make a separate telegram account specifically for this agent and talk to it from anywhere?

### GEMINI
Exactly. Because you are running this on a 12th-gen i7-12700K with 32GB of RAM, your machine is more than capable of handling this as a "Home Server" in the background while you use Tiny11 for gaming or work. Here is how the 24/7 Telegram Gateway works within your secure Docker stack: 1. The "Always-On" Docker Container Docker allows you to run the Hermes Agent as a daemon (a background service). Even if you close the Obsidian window or stop "chatting" at your desk, the container stays alive in your System Tray. It uses negligible CPU/GPU when idling, only "waking up" your RTX 3070 when it receives a message. 2. Your Dedicated Telegram Bot You won't just "chat" with a random account. You will create your own private bot via Telegram's "BotFather." Privacy: You configure the bot to only respond to your specific Telegram User ID. If anyone else finds your bot, it ignores them. The Bridge: You’ll use a small "Gateway" script (often a Node.js or Python script) inside a Docker container. It sits between Telegram’s API and your local Hermes Agent. 3. "Talking to the Brain" from Anywhere Since you're in Akron, you could be at a coffee shop or at work, and you send a message to your "Second Me" bot: The Input: "Hey, I just saw a new SSD on sale. Does it have better endurance than my 970 Evo Plus?" The Process: The message hits your PC at home. Hermes "wakes up," queries your Obsidian Vault for your current specs, and searches the Wikipedia ZIM for the new SSD's specs. The Output: Your phone buzzes: "The 970 Evo Plus has a TBW (Total Bytes Written) of 1,200TB. The one you’re looking at is only 600TB. Stick with what you have. Also, your 'PC Upgrade' budget for April is already at $0. Stop looking." (There’s that brutal honesty). 4. Voice Memos & Transcription Since you mentioned being away from your desk: You can record a voice memo in Telegram. Hermes receives the audio file, uses a local Whisper model (also in Docker) to transcribe it, and files the text directly into your Obsidian Inbox. When you get home, your thought is already organized, tagged, and linked. The "Why" of this Setup Most people’s "Second Brains" are passive graveyards of notes they never look at again. By adding the Telegram + Hermes layer, your brain becomes active. It can nudge you: "Hey, you haven't updated your DeFi log in 3 days. Are you avoiding the loss or did you just forget?" It can remind you of your own logic: "You're about to buy this part, but 2 months ago you wrote a note saying you wanted to save for a GPU upgrade instead." The Security Requirement To make this work securely, you will need a Tunnel (like Cloudflare Tunnels or Tailscale) so your phone can talk to your home PC without opening your whole network to the internet. Is a 24/7 "Digital Twin" that can call you out on your spending or technical habits while you're on the go exactly what you were aiming for?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
