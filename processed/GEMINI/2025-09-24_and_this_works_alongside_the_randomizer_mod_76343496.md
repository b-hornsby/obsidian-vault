---
id: 450114
source: GEMINI
date: 2025-09-24
tags: ['elden-ring', 'mod-compatibility', 'randomizer-mod']
category: general
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is checking if a certain element works with the Elden Ring randomizer mod.
---
# and this works alongside the randomizer mod? 

### USER
and this works alongside the randomizer mod? 

### GEMINI
That's a very good question, as it involves two different types of mods! Yes, cosmetic mods generally work alongside the randomizer mod with Mod Engine 2. Here's a breakdown of why and what you need to be aware of: 1. Cosmetic Mods are "Replacement" Mods Cosmetic mods (like armor, weapon, or texture swaps) are typically file replacements. They usually consist of files placed in your Mod Engine 2's mod folder in directories like parts, chr, menu, etc. They simply replace the appearance of an existing item/asset in the game. They do not change the item's stats, where it's found, or what it drops. 2. The Randomizer is a "Data/Parameter" Mod The Randomizer mod works by modifying the game's core parameter file, usually regulation.bin. This file controls things like what enemy drops what, what item is in what location, and the stats of weapons/armor. The Randomizer generates a modified regulation.bin and then loads it through Mod Engine 2. The Harmony Since the cosmetic mod changes the look of an item, and the randomizer changes the data/location of an item, they generally don't conflict, assuming both are set up correctly with Mod Engine 2. If you find a randomized weapon, it will still use the custom cosmetic appearance if that appearance file is loaded by Mod Engine 2. If you're using a randomizer that adds new items (not just randomizing existing ones), the mod authors usually provide an option within the randomizer itself to "Merge other mods" which is necessary to combine the randomizer's regulation.bin changes with any other mod's regulation.bin changes. In summary, as long as you follow the Mod Engine 2 installation for your cosmetic mod (as described previously, dropping the folders into the ME2 mod folder), it should work with your already running randomizer.
