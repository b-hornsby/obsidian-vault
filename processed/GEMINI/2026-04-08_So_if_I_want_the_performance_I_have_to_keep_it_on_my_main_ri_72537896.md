---
id: 728036
source: GEMINI
date: 2026-04-08
tags: ['24-7-performance', 'main-rig', 'hardware-tradeoffs', 'always-on-hosting']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether he needs to keep his main PC running 24/7 for true always-on agent assistance due to performance requirements.
---
# So if I want the performance I have to keep it on my main rig and have that on 24/7 if I wanted true 24/7 assistance?

### USER
So if I want the performance I have to keep it on my main rig and have that on 24/7 if I wanted true 24/7 assistance?

### GEMINI
As your advisor, I’m going to give you the objective breakdown. You have two paths: the "Always On" strategy and the "Smart Trigger" strategy. If you want the assistance to be instantaneous and local without compromising performance, yes, your main rig is the only machine currently capable of handling the weight of Hermes and an Obsidian-backed MCP setup. 1. The "Always On" Cost (Akron, OH) Leaving your i7-12700K and RTX 3070 rig on 24/7 isn't as expensive as most people fear, but it's not free. Idle Power Draw: Your setup likely pulls 80W–120W while idling (assuming the GPU isn't crunching tokens). The Math: At Akron’s average rate of ~$0.13$ per kWh, running that rig 24/7 will cost you roughly $8.00–$12.00 per month in electricity just to keep it awake. The Opportunity Cost: You’re putting 24/7 wear on your AIO/fans and PSU for a service you might only use 5% of the day. 2. The "Smart Trigger" Strategy (High Level) Since you’re already deep into agentic workflows and Docker, don't just leave it on—automate the wake cycle. * Wake-on-LAN (WoL): You can set up a "listener" (even a cheap Raspberry Pi or that "cheap laptop") that stays on and consumes almost zero power. When you need your agent, you send a command to the listener, which sends a "Magic Packet" to your main rig to boot it up. Docker Autostart: Set your containers to --restart always. As soon as your main rig hits the desktop (or tty), Hermes and the MCP bridge will fire up automatically. The Mirror Truth: If you are building an "Autonomous Digital Entity," it needs a body that stays alive. If you aren't willing to pay the $10/month "server tax" to keep your PC on, you aren't building a 24/7 assistant; you're just building a desktop app you have to manually launch. 3. The Performance Compromise (The Middle Ground) If you move it to a cheap laptop, you'll be forced to switch from Hermes (which needs the VRAM) to something much smaller like Phi-3 Mini or a heavily quantized Gemma 2B. The Result: You'll have an assistant that is always online but has the "IQ" of a much simpler model. It will struggle with the complex reasoning you've been working on. Advisor's Recommendation: Keep it on the main rig for now. You are in the development phase of "Operation Immortal Agent." Don't bottleneck your progress by worrying about $10 of electricity or fighting with underpowered hardware. Your Priority Plan: Optimize Idle: Use nvidia-smi or your Windows power settings to ensure the GPU downclocks properly when the agent isn't active. Remote Access: Set up Tailscale so you can talk to your Docker instance from your phone or the cheap laptop while your main rig does the heavy lifting in another room. The Scale-Up: Only move to dedicated hardware when you can afford a used RTX 3060/4060 workstation or a Mac Mini (M-series) which has unified memory for LLMs. Does the idea of a $10–$15 monthly "hosting fee" to your utility company change your perspective on keeping the rig active?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
