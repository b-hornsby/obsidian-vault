---
category: homelab
date: 2026-03-21
id: 449755
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is indicating that certain KWin settings related to compositing and
  priority are missing, suggesting he's trying to configure window behavior.
tags:
- kwin-settings
- compositing
- window-management
- desktop-environment
---
# these two are not there: Lowered priority: Set to Force -> No.
Allow compositing: Set to Force -> Yes.

### USER
these two are not there: Lowered priority: Set to Force -> No.
Allow compositing: Set to Force -> Yes.

### GEMINI
The reason you don't see them is that KDE Plasma 6 (which you are running on CachyOS) renamed several properties and automated others. KDE's menus change faster than most online guides can keep up with. Since you're on a high-performance i7-12700K, we need to use the modern equivalents to stop the OS from "parking" your CPU cores or "throttling" the Vesktop window while you're gaming. The Modern KDE 6 "Pro" Setup Go back into System Settings > Window Management > Window Rules and edit your Vesktop Fix rule. Look for these specific names instead: 1. The "Lag" Fix (Replaces Lowered Priority) Click Add Property. Search for Inhibition. Select Block compositing (or "Inhibit shortcuts"). Set it to Force -> No. Why: This ensures the window manager doesn't try to "pause" the window's rendering when it's in the background. 2. The "Flicker" Fix (The "Explicit Sync" Bridge) Search for Accept focus. Set it to Force -> Yes. Search for Focus stealing prevention. Set it to Force -> None. Why: This forces the desktop to keep "talking" to Vesktop even when your game is the active window. The "Brutally Honest" Logistics Check If you still feel like the stream is a "slideshow," the bottleneck isn't the window rule—it's the PipeWire buffer. On CachyOS, you have a specialized tool called the CachyOS Hello or the CachyOS Kernel Manager. Because you have an NVIDIA 3070, your "Logistics" chain for video data looks like this: Game -> GPU -> Wayland -> PipeWire -> Vesktop -> Internet. If you have already: Saved the Nano file with the Wayland flags. Applied the Window Rules above. Turned OFF Adaptive Sync (VRR). ...and it still flickers? The "Nuclear Option" is to switch to X11 for your streaming sessions. The Truth: Wayland is the future, but for an NVIDIA 3070 user in 2026 who wants to stream high-end games right now without a headache, clicking the "Session" button on your login screen and picking Plasma (X11) will solve 100% of these issues instantly. It’s the "stable warehouse" vs. the "under-construction automated facility." Would you like me to show you how to check if your PipeWire service is actually hitting errors during your stream?
