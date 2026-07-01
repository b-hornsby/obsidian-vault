---
id: 189814
source: GEMINI
date: 2026-03-11
tags: ['tailscale', 'steam-deck', 'remote-gaming', 'game-streaming', 'offline-play']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking if Tailscale would allow him to play games on his Steam Deck remotely as long as it's connected to his PC.
---
# So would tailscale allow me to play those games even if my steam deck is offline as long as it’s connected to the pc via tailscale

### USER
So would tailscale allow me to play those games even if my steam deck is offline as long as it’s connected to the pc via tailscale

### GEMINI
No, and this is a common point of confusion. Tailscale requires an internet connection on both devices to work. Here is the breakdown of why "Offline" won't work with Tailscale, and how it actually functions: 1. The "Handshake" Problem Tailscale is a Coordination VPN. Even though the game data travels directly from your PC to your Deck (Peer-to-Peer), both devices must first talk to Tailscale’s servers over the internet to: Verify your identity. Find each other's current location (IP address). Exchange the security keys needed to encrypt the stream. If your Steam Deck is offline, the "tunnel" cannot be built. 2. Tailscale vs. Local Wi-Fi At Home (Local): You don't need Tailscale. Moonlight will see your PC via your router. If your internet goes out but your router is still powered on, Moonlight will usually still work because it’s staying entirely inside your house. Away from Home (Remote): You need an internet connection (Mobile Hotspot, Hotel Wi-Fi, etc.). Tailscale uses that internet connection to trick your devices into thinking they are still at home together. 3. The "Steam Deck Offline Mode" Trap If you put your Steam Deck into "Offline Mode" (the software setting), it disables many network features. To use Moonlight/Tailscale, your Deck needs to be in Online Mode and connected to some form of internet (like your phone's hotspot). The Reality of Remote Play If you want to play your PC games while traveling: PC: Must be on and connected to your home internet + Tailscale. Steam Deck: Must be connected to any Wi-Fi/Hotspot + Tailscale. The Result: You can play your high-end PC games on the train, at a hotel, or at work. Your Next Step If your goal is to play in places where there is zero internet (like a plane or a remote cabin), you won't be able to stream. In those cases, you’ll need to install the games directly on the Steam Deck's SSD. Would you like me to show you how to set up your phone as a "bridge" so you can use your mobile data to stream from your PC when you're out?
