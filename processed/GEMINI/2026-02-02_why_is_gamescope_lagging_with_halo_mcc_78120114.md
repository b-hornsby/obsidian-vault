---
category: homelab
date: 2026-02-02
id: 374728
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing lag when running Halo MCC with Gamescope and wants
  to know why.
tags:
- gamescope
- halo-mcc
- game-performance
- linux-gaming
---
# why is gamescope lagging with halo mcc?

### USER
why is gamescope lagging with halo mcc?

### GEMINI
Gamescope is lagging with Halo MCC because of a combination of Vsync fighting, NVIDIA driver overhead (if you're on NVIDIA), and GNOME's Mutter compositor adding a second layer of frame-timing logic. When you run Gamescope, you are essentially running a compositor inside a compositor. If their frame rates or sync settings don't match perfectly, you get "micro-stutter" or heavy input lag. 1. The "Clean" Gamescope Command for Halo MCC Halo MCC is sensitive to refresh rate mismatches. Try this exact string to bypass the most common lag causes: gamescope -w 2560 -h 1440 -r 144 --adaptive-sync --force-grab-cursor -- %command% -r 144: Replace 144 with your monitor's actual refresh rate. If Gamescope doesn't know your refresh rate, it defaults to 60Hz, which feels like 1995 if your monitor is 144Hz+. --adaptive-sync: This is critical. Without it, Gamescope forces its own Vsync, which conflicts with Halo’s internal Vsync, causing massive lag. In-Game Setting: Once the game starts, Disable Vsync inside the Halo MCC settings. Let Gamescope or your monitor handle the sync. 2. The "CachyOS Special" (Priority Fix) CachyOS includes a tool called setcap that allows Gamescope to take priority over other system processes. If Gamescope is "stuttering," it’s often because GNOME is stealing CPU cycles. Open your terminal and run: sudo setcap 'CAP_SYS_NICE=eip' $(which gamescope) This gives Gamescope "Real-time" priority. It’s one of the biggest performance boosters for Gamescope on Arch-based systems like Cachy. 3. The Brutal Truth: Halo MCC doesn't actually need Gamescope I’m going to challenge your assumption here. You’re using Gamescope to solve a mouse-lock problem, but Gamescope is introducing a performance penalty (the lag). The Better Way for Halo MCC on GNOME: Halo MCC has a known issue where it doesn't grab the mouse correctly in "Windowed" mode. Remove the Gamescope launch options. Use this instead: PROTON_ENABLE_WAYLAND=1 %command% Inside the game, set it to Exclusive Fullscreen. If the mouse still escapes, use the "Confine Mouse to Window" GNOME extension I mentioned earlier. Why? Gamescope is a wrapper. Wrappers add latency. For a fast-paced shooter like Halo, you want the shortest path between your mouse and the kernel. Native Wayland (via the Proton flag above) is that path. Your Next Step Are you on an NVIDIA or AMD card? If you are on NVIDIA, Gamescope is still considered "experimental" and is the direct cause of your lag. If so, I’ll give you the specific environment variables to bypass the compositor entirely.
