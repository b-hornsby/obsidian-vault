---
id: 897996
source: GEMINI
date: 2025-09-24
tags: ['elden-ring', 'mod-loader', 'modding']
category: general
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is asking if the Elden Mod Loader is required for a specific task.
---
# do i need elden mod loader for this?

### USER
do i need elden mod loader for this?

### GEMINI
In almost all cases for general modding of Elden Ring, the answer is No, you do not need Elden Mod Loader. Here is the simple breakdown of the two tools and when you would need them: Mod LoaderPurposeWhen You Need ItMod Engine 2Loads replacement files (models, textures, sound, regulation.bin—like the Randomizer uses) from its own folder, keeping your game install clean.This is the primary tool you should be using. It handles cosmetic mods, randomizers, and most major overhaul mods.Elden Mod Loader (EML)Loads .dll mods (dynamic link library) from a specific folder inside your main game directory. These are mods that inject code or new functionality.Only if the mod specifically states it requires EML. Examples were historically mods like "Seamless Co-op" or "Pause the Game," but recent versions of Mod Engine 2 can now load .dll files directly, making EML largely redundant. Since you are already using Mod Engine 2 for the Randomizer and cosmetic mods are simple file replacements, Mod Engine 2 is all you need. Just place the cosmetic mod files into the correct subdirectory (like parts or chr) inside your Mod Engine 2's mod folder, and the randomizer's files (usually the regulation.bin it generates) should be set up according to its instructions, usually also within the Mod Engine 2 structure.
