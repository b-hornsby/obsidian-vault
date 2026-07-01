---
category: homelab
date: 2026-02-03
id: 618236
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is confused about only seeing memorysearcher and mlc01 devices on his
  network and wants to understand what's happening.
tags:
- network-discovery
- homelab
- devices
- memorysearcher
- mlc01
---
# all i see is memorysearcher and mlc01

### USER
all i see is memorysearcher and mlc01

### GEMINI
If you only see memorysearcher and mlc01, you are looking at the internal data directory, not the application's configuration root. You’re likely playing "hide and seek" with your file system because Cemu creates directories in multiple places depending on how you're running it. Let’s cut through the confusion and put the file where it actually belongs. 1. The Correct Directory (The "Shadow" Root) On CachyOS, the keys.txt does not go inside mlc01. It goes in the parent directory or the config directory. Check this specific path: ~/.config/Cemu/ If you see a settings.xml in there, that is exactly where your keys.txt needs to live. 2. Why you're only seeing two folders If you are looking at a folder that only contains mlc01 and memorysearcher, you are likely inside a temporary path or a flatpak-style sandbox. Try this via Terminal to find the "real" home: find ~ -name "settings.xml" 2>/dev/null The directory containing settings.xml is the only directory Cemu cares about for its configuration and keys. 3. The "Manual Override" Strategy If you cannot find the path or it’s acting stubborn, Cemu allows you to define where the MLC (and by extension, the base files) live. Open Cemu. Go to Options > General Settings. Look at the MLC Path. Navigate to the folder one level above whatever is listed as your MLC path. Drop keys.txt there. The Brutal Truth on Your Workflow You are wasting time troubleshooting a legacy system. The fact that you are digging through file structures for a keys.txt means you are using outdated, encrypted ROM formats. Stop playing small with .wux or .wud files. * The Opportunity Cost: Every minute you spend hunting for a directory to paste a hex string is a minute you aren't playing. The Fix: Use UWUVCI or Cemu's own title manager (if you can get the game to show up) to convert your library to .wua. The Result: No keys, no decryption errors, one single file per game, and much better compression. Would you like the specific command-line instructions to convert your current files to .wua so you can delete that keys file forever?
