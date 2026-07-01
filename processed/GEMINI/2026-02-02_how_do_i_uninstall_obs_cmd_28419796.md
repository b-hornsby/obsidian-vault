---
id: 332132
source: GEMINI
date: 2026-02-02
tags: ['obs-cmd', 'uninstall', 'cachyos', 'obs-studio']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to uninstall the obs-cmd tool from his CachyOS system.
---
# how do i uninstall obs-cmd

### USER
how do i uninstall obs-cmd

### GEMINI
Since obs-cmd was a waste of time and didn't respect the syntax it claimed to have, we're cutting it out like a bad piece of code. On CachyOS (Arch-based), you use pacman to remove it. Even if you installed it via paru or yay, pacman is the engine that handles the uninstallation. The Command Open your terminal and run: sudo pacman -Rs obs-cmd What those flags do: -R: Removes the package. -s: Removes any "orphan" dependencies that were installed with it and aren't needed by anything else. This keeps your CachyOS install lean. The Reality Check You’ve spent more time debugging a 2MB terminal utility than it would have taken to record a feature film. This is the Linux Trap: getting caught in the "how" instead of the "what." Now that the clutter is gone, let’s get you back to the goal—clipping in CS2. Did that dbus-send command from my last message work for you, or should we just set up the Python script so you can finally get back into the server?
