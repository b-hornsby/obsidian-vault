---
id: 801670
source: GEMINI
date: 2026-03-11
tags: ['cloudflare', 'networking', 'vpn', 'tailscale', 'security-tools']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether an additional Cloudflare layer is needed on top of his current networking/VPN setup.
---
# I don’t need any cloudflare thing on top?

### USER
I don’t need any cloudflare thing on top?

### GEMINI
No, you absolutely do not need Cloudflare (like Cloudflare Tunnels) on top of Tailscale. In fact, adding it would likely make your gaming experience worse. Here is the "brutally honest" breakdown of why Tailscale is enough and why Cloudflare is a bad fit for this specific goal. 1. Tailscale is "Peer-to-Peer" (Fast) Tailscale (built on WireGuard) connects your Steam Deck directly to your PC. The data travels the shortest possible path between the two. Cloudflare Tunnels, however, force your game data to travel from your house → to a Cloudflare data center → then to your Steam Deck. This adds latency (lag), which is the ultimate enemy of game streaming. 2. The Protocol Conflict (UDP vs. HTTP) Tailscale handles UDP traffic perfectly. Moonlight/Sunshine relies on UDP for high-speed, low-lag video. Cloudflare Tunnels (specifically the free tier) are primarily designed for web traffic (HTTP). While you can force other traffic through them, it’s not what they were built for, and you might run into bandwidth throttling or "Terms of Service" issues for streaming high-bitrate video. 3. Security: You're Already "Invisible" The reason people use Cloudflare is to hide their home IP address from the public. Tailscale already does this. * Your Sunshine ports are closed to the public internet. The only way to reach your PC is through the encrypted Tailscale "tunnel" that requires your specific login. Unless someone steals your Tailscale credentials, your PC is essentially a ghost on the internet. 4. Simplicity (The "Path of Least Resistance") Your setup is already complex enough with CachyOS, Lutris, and the Steam Deck. Adding a Cloudflare Tunnel requires managing DNS records, installing cloudflared, and configuring a reverse proxy. It’s an enterprise-grade solution for a problem Tailscale solves with a single "Login" button. The Only "Extra" Tool You Might Actually Want: If you want to be truly professional about this, the only other tool I’d recommend is SteamGridDB Manager (on your PC). Since you're adding Lutris games manually, they won't have icons in Moonlight by default. This tool can help you quickly grab the official "Grid" art so your Moonlight menu doesn't look like a wall of grey boxes. You're in the home stretch. Your PC is ready, your Deck is ready, and your "tunnel" is secure. Would you like to do a final test run to see if the Lutris controller mapping works through the stream?
