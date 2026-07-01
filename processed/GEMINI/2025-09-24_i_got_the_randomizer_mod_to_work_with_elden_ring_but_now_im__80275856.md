---
category: general
date: 2025-09-24
id: 419693
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan has the Elden Ring randomizer mod working and is now trying to get
  other cosmetic mods to work using Mod Engine 2.
tags:
- elden-ring
- modding
- randomizer-mod
- mod-engine-2
---
# i got the randomizer mod to work with elden ring but now i'm working on getting other cosmetic mods to work? currently using mod engine 2 

### USER
i got the randomizer mod to work with elden ring but now i'm working on getting other cosmetic mods to work? currently using mod engine 2 

### GEMINI
That's great you got the randomizer working! Mod Engine 2 is the right tool for most Elden Ring mods, including cosmetic ones. For most cosmetic mods that replace things like armor, weapons, or character textures (file-based mods, not DLLs), here is the general process: Locate your Mod Engine 2 folder. This is usually in your ELDEN RING\Game directory. Find the mod folder inside the Mod Engine 2 folder. This is where you put most mods. Check the mod's file structure. If the mod comes with folders named things like parts, chr, menu, etc., you want to copy the entire folder(s) into the mod folder. Mod Engine 2 will read the files within these folders to override the game's assets. For example, if a cosmetic mod has a folder called parts (which contains models for armor/weapons), you would drop that parts folder directly into your Mod Engine 2 mod folder. The path would look something like [Mod Engine 2 Folder]\mod\parts\... Launch the game using launchmod_eldenring.bat from your Mod Engine 2 folder, as you did for the randomizer. A few extra things to keep in mind: File Conflicts: Mod Engine 2 can only load one replacement file for any given original file. If two cosmetic mods try to replace the same piece of armor, only one will be loaded (usually the one in the folder Mod Engine 2 loads first, or simply the one that was loaded last). Reading the Mod Page: Always, always check the mod's page (usually on Nexus Mods) for specific installation instructions. Some complex mods might require extra steps or specific subfolders. DLL Mods: Some mods (like Transmogrification or more advanced function changes) are DLL files. These need to be placed in a separate folder (which you might need to create, like dllbasedmods or similar) and then referenced in the config_eldenring.toml file. This is generally not required for simple texture/model swaps. If a specific cosmetic mod isn't working, let me know which one it is, and I can look up its specific requirements!
