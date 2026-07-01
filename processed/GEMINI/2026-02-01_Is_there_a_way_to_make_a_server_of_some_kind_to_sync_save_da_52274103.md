---
category: homelab
date: 2026-02-01
id: 545870
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
linked_projects:
- homelab-stack
resolution: abandoned
sentiment: building
source: GEMINI
tags:
- homelab
- ai
- gemini
- rag
- go
- ide
---
# Is there a way to make a server of some kind to sync save data between my steam deck and my pc for emulators? 

### USER
Is there a way to make a server of some kind to sync save data between my steam deck and my pc for emulators? 

### GEMINI
Yes, there are several ways to do this, ranging from "set it and forget it" cloud services to running your own private synchronization server. Since you're asking for a "server of some kind," you likely want maximum control. Here are the most effective methods to achieve this. 1. The "Self-Hosted Server" Choice: Syncthing Syncthing is the gold standard for this. It isn't a "cloud" in the traditional sense; it’s a peer-to-peer sync tool that turns your devices into their own private server network. How it works: You install Syncthing on both your Steam Deck and your PC. You tell it which folder contains your saves (e.g., your Emulation/saves folder). Whenever both devices are on, they instantly sync changes to each other. The "Server" Twist: If you have an old laptop, a Raspberry Pi, or a NAS that stays on 24/7, you can install Syncthing there too. It acts as a "relay server." Your Steam Deck uploads the save to the server, and then your PC downloads it from the server later (even if the Deck is now off). Pros: Entirely private, free, and no storage limits other than your hard drive size. Setup Tip: Use Syncthingy (available in the Steam Deck's Desktop Mode "Discover" store) for a cleaner integration on the Deck. 2. The Integrated Choice: EmuDeck Cloud Sync If you used EmuDeck to set up your emulators, they have a built-in tool for this. How it works: Within the EmuDeck application, there is a "Cloud Sync" or "Cloud Services" section. It allows you to link a provider like OneDrive, Google Drive, Dropbox, or Nextcloud. The "Server" Twist: If you want to own the server, you can host a Nextcloud instance (a private Dropbox alternative). You then point EmuDeck to your Nextcloud server. Pros: Native integration with EmuDeck's folder structure; often handles the complex file paths for you. 3. The Power-User Choice: Decky Cloud Save If you use Decky Loader (the plugin architect for Steam Deck), there is a plugin called Decky Cloud Save. How it works: It uses rclone (a powerful command-line sync tool) to move files to a remote server. The "Server" Twist: It supports WebDAV, SFTP, and FTP. If you have a home server or a VPS, you can set up a simple SFTP share, and this plugin will "push" and "pull" saves automatically when you start or exit a game in Gaming Mode. Comparison Table FeatureSyncthingEmuDeck Cloud SyncDecky Cloud SaveServer RequirementNone (P2P) or 24/7 PC/NASCloud Provider (or Nextcloud)SFTP/WebDAV/CloudPrivacyHigh (Encrypted P2P)Depends on ProviderHigh (Direct to Server)Ease of UseModerate (Initial Pairing)EasyModerateReal-time SyncYes (Continuous)On Game Launch/ExitOn Game Launch/Exit Recommendation If you want a "Private Server" feel: Set up Syncthing on your PC, Steam Deck, and an "always-on" device (like a cheap Raspberry Pi or a mini-PC). It ensures your saves are always backed up to the "server" the moment you close a game. If you want simplicity: Use the EmuDeck Cloud Sync tool with a Google Drive or Dropbox account you already have. Would you like me to walk you through the specific folder paths you'll need to sync for the emulators you're using?
