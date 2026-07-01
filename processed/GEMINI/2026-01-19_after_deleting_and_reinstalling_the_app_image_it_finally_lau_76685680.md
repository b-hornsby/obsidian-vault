---
id: 101652
source: GEMINI
date: 2026-01-19
tags: ['citron-emulator', 'emulation-station', 'steam-rom-manager', 'steam-deck-gaming']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan got Citron AppImage working on Steam Deck and was now trying to integrate it with Steam ROM Manager for game mode.
---
# after deleting and reinstalling the app image it finally launches. the one thing im trying to do is to get citron to be picked up by emulation station since natively ryujinx/yuzu is the default and doesn't come with it natively 

### USER
after deleting and reinstalling the app image it finally launches. the one thing im trying to do is to get citron to be picked up by emulation station since natively ryujinx/yuzu is the default and doesn't come with it natively 

### GEMINI
To get EmulationStation-DE (ES-DE) to recognize Citron, you have to stop waiting for it to show up automatically. ES-DE only displays emulators it has pre-defined "rules" for. Since Citron is a newer fork, it isn't in the default config. You have two options: the Dirty Shortcut (easy but hacky) or the Professional Setup (clean but requires editing text files). Option 1: The "Dirty Shortcut" (Easiest) If you don't care about the icon saying "Yuzu" as long as the games launch in Citron, do this. Go to your Applications folder in Desktop Mode. Find your citron.AppImage. Rename it to exactly yuzu.AppImage. Open ES-DE, go to Other Settings > Alternative Emulators > Switch, and select Yuzu (Standalone). ES-DE will look for a file named yuzu.AppImage, find your Citron file instead, and launch it perfectly. Option 2: The "Professional" Setup (Proper Way) If you want Citron to actually show up as "Citron" in the menu, you need to create "Custom Systems" files. 1. Create the Custom Systems Folder Open the Dolphin file manager. Go to /home/deck/ES-DE/ (or wherever your ES-DE configuration is stored). Create a new folder named custom_systems (if it doesn't already exist). 2. Create es_systems.xml Inside that custom_systems folder, create a new text file named es_systems.xml and paste this in: <systemList> <system> <name>switch</name> <fullname>Nintendo Switch</fullname> <path>%ROMPATH%/switch</path> <extension>.nca .NCA .nro .NRO .nso .NSO .nsp .NSP .xci .XCI</extension> <command label="Citron (Standalone)">~/Applications/citron.AppImage %ROM%</command> <platform>switch</platform> <theme>switch</theme> </system> </systemList> (Note: Change ~/Applications/citron.AppImage if your file is named differently or stored elsewhere.) 3. Refresh ES-DE Restart EmulationStation-DE. Press Start > Other Settings > Alternative Emulators. Find Switch and you should now see Citron (Standalone) as an option. Select it. The Reality Check By using Option 2, you are essentially overriding ES-DE's default Switch settings. If ES-DE updates in the future with new official features for Switch, your custom file might hide them. However, for a power user, this is the only way to get a custom fork like Citron integrated properly without tricking the system. Do you want me to write a quick script you can run in the Konsole that handles the file creation for you automatically?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
