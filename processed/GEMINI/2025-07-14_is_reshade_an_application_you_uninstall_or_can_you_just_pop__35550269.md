---
category: general
date: 2025-07-14
id: 517918
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether ReShade can be uninstalled through a dedicated uninstaller
  or simply deleted, indicating uncertainty about the proper removal method.
tags:
- reshade
- uninstall
- windows
- graphics-modding
---
# is reshade an application you uninstall or can you just pop it in the recycle bin and empty it?

### USER
is reshade an application you uninstall or can you just pop it in the recycle bin and empty it?

### GEMINI
You generally cannot simply drag ReShade to the Recycle Bin and empty it for a complete and clean uninstall. Here's why and what you should do instead: ReShade isn't a traditional "application" in the Windows sense. It doesn't install itself as a program that appears in "Apps and Features" (or "Add or Remove Programs" in older Windows versions). Instead, it injects itself directly into the game's executable files and associated folders. Leaving behind files can cause issues. If you just delete some .dll files, you might leave behind configuration files (.ini), shader files, or even registry entries that can cause conflicts, crashes, or prevent the game from launching correctly. The recommended and most effective way to uninstall ReShade is to use the original ReShade setup file. This file acts as both an installer and an uninstaller. When you run it again and select the game where ReShade is installed, it will give you an "Uninstall" option that cleanly removes all associated files. If you absolutely cannot use the setup file (e.g., you lost it, or it's not working for some reason), then you can proceed with manual deletion. However, this requires you to know exactly which files ReShade placed in the game's folder (like dxgi.dll, d3d9.dll, ReShade.ini, the ReShade-Shaders folder, etc.) and delete them yourself. This is more prone to error and should be a last resort. In summary: Best method: Use the ReShade setup file and select the "Uninstall" option for each game. Last resort: Manually delete the ReShade-related files from the game's installation folder. Don't just drag and drop random files to the Recycle Bin, as this is unlikely to fully remove ReShade and could potentially cause problems with your games.
