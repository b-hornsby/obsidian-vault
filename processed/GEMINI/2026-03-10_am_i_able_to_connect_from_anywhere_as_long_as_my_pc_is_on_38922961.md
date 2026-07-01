---
id: 454016
source: GEMINI
date: 2026-03-10
tags: ['moonlight', 'remote-streaming', 'steam-deck', 'pc-always-on', 'game-streaming']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking if he can connect to his PC for game streaming from anywhere as long as the PC is powered on.
---
# am i able to connect from anywhere as long as my pc is on?

### USER
am i able to connect from anywhere as long as my pc is on?

### GEMINI
Technically, yes, but simply having your PC "on" isn't enough to connect from outside your house. Right now, your setup only works on your local Wi-Fi. To stream from "anywhere" (like a coffee shop or on mobile data), you have two main options. One is a security nightmare, and the other is the professional "CachyOS-friendly" way. Option 1: The "Lazy but Dangerous" Way (UPnP) Sunshine has a setting called UPnP that tells your router to open its doors to the entire internet so Moonlight can find it. Why it's bad: It exposes your PC to anyone with a port scanner. If there's ever a security bug in Sunshine, a random person on the internet could theoretically take over your machine. How to do it: In the Sunshine Web UI, go to Network > UPnP and set it to Enabled. Option 2: The "Path of Least Resistance" & Secure Way (Tailscale) This is what I recommend for you. Tailscale creates a private, encrypted tunnel (a "Mesh VPN") between your PC and your Steam Deck. They will think they are in the same room even if you’re 50 miles away. On your CachyOS PC: Install Tailscale: sudo pacman -S tailscale Enable and start the service: sudo systemctl enable --now tailscaled Log in: sudo tailscale up (It will give you a link; click it and sign in with Google/GitHub/etc.) On your Steam Deck: Go to Desktop Mode and open the Discover Store. Search for Tailscale and install it. Open the app and log in with the same account you used on your PC. How to connect: Open the Tailscale app on your Deck (or PC) to see your PC's new "Tailscale IP" (it usually starts with 100.x.y.z). Open Moonlight on your Deck. Click the "+" icon in the top right and manually type in that 100.x.y.z IP address. Done. You can now use this specific "PC entry" in Moonlight from any Wi-Fi in the world. One Reality Check: Your Upload Speed You mentioned you have 34.2 Mbps upload. This is your speed limit when you are away from home. Local (At home): You can use 50 Mbps bitrate. Remote (Away): You must go into Moonlight settings and drop your bitrate to around 15–20 Mbps. If you try to use 30+ Mbps, the stream will lag or freeze because your home internet can't "push" the data out fast enough. Would you like me to help you set up "Wake on LAN" next, so you can actually turn your PC on remotely from your Steam Deck if it's asleep?
