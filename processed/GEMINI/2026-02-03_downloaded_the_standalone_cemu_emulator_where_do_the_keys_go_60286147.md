---
category: homelab
date: 2026-02-03
id: 559061
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan downloaded the standalone Cemu emulator on CachyOS and needs help placing
  the encryption keys in the correct location.
tags:
- cemu
- emulator
- cachyos
- configuration
- encryption-keys
---
# downloaded the standalone cemu emulator. where do the keys go? cachyos

### USER
downloaded the standalone cemu emulator. where do the keys go? cachyos

### GEMINI
On Linux (including CachyOS), the standalone native Cemu build expects your keys.txt file to be in its data directory. Since you are on a Linux distribution, you likely have it in the standard XDG path. The Primary Location For the standalone version (likely installed via the AUR or as an AppImage), look here: ~/.local/share/Cemu/keys.txt If the Cemu folder or the keys.txt file doesn't exist, create them manually. How to verify the path If the path above doesn't work, Cemu provides a built-in way to find exactly where it's looking: Open Cemu. Go to File → Open Cemu folder. Place your keys.txt in the folder that opens. Note: If it opens the "MLC" folder, go up one level to the main Cemu directory. A Critical Reality Check You are asking for the keys.txt location, which implies you are using encrypted files (like .wud or .wux). The Problem: Managing keys is a hassle and prone to failure if the key doesn't match the specific region/version of your dump. The Strategic Move: Stop using encrypted formats. Use .wua or Loadiine (folders). They are decrypted. They do not require a keys.txt file. .wua is a single-file format that is significantly smaller and easier to manage. If you insist on sticking with encrypted files, ensure your keys.txt contains the Wii U Common Key at the top, followed by the specific title keys for your games. Quick Setup Command If you want to create the file via terminal: mkdir -p ~/.local/share/Cemu && touch ~/.local/share/Cemu/keys.txt Would you like me to help you find a tool to convert your encrypted files to the superior .wua format so you can ignore keys entirely?
