---
category: general
date: 2026-03-09
id: 111870
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for the best way to mod games on CachyOS, as he previously
  used Vortex on Windows.
tags:
- game-modding
- cachyos
- vortex
- mod-manager
- linux-gaming
---
# what is the best way to mod games on cachyos? i used to use vortex on windows 11

### USER
what is the best way to mod games on cachyos? i used to use vortex on windows 11

### GEMINI
Switching from Vortex on Windows to modding on CachyOS is a bit like moving from an automatic to a manual transmission: it requires more "under-the-hood" knowledge, but it gives you significantly more control over performance. Since you are already on CachyOS and likely using proton-cachyos, here is the most effective way to handle modding in 2026. 1. The "Vortex" Replacement: SteamTinkerLaunch While a native Linux version of Vortex is finally in development (targeting SteamOS/Steam Deck), the current best way to use Vortex or Mod Organizer 2 (MO2) on CachyOS is via SteamTinkerLaunch (STL). STL acts as a wrapper for Steam games that can automatically install and launch Vortex or MO2 inside the game's specific Wine prefix. How to install: sudo pacman -S steamtinkerlaunch How to use: In Steam, set the game's Launch Options to: steamtinkerlaunch %command% Launch the game. A menu will appear; click Main Menu -> Game Menu. Find the Modding section and select Vortex or MO2. The tool will handle the installation of the manager and .NET dependencies for you. 2. The Native Alternative: Limo If you want to avoid the overhead of running a Windows mod manager through Wine, Limo is the community favorite native Linux mod manager in 2026. It supports the NexusMods API and LOOT (for load order optimization) without the stability issues of Wine. Pros: Much faster, native UI, handles NXM (Nexus) links correctly. Cons: Doesn't support every game Vortex does (best for Bethesda and Cyberpunk). 3. Critical Configuration: DLL Overrides On Windows, Vortex just drops a DLL (like d3d11.dll for Script Extenders) and it works. On Linux/Proton, you must tell the system to use your modded DLL instead of the built-in one. If your mod includes a custom .dll, you need to add this to your Steam Launch Options: WINEDLLOVERRIDES="winedllname=n,b" %command% (Replace winedllname with the actual name of the mod's DLL, e.g., version, dinput8, or dxgi). Comparison at a Glance MethodEase of UsePerformanceRecommendationSteamTinkerLaunch + MO2ModerateHighBest for heavy modlists (Skyrim, Fallout).Limo (Native)HighBestBest for stability and native integration.Manual ModdingLowHighBest for simple mods (single folder drops). [!IMPORTANT] Case Sensitivity: Windows doesn't care if a folder is named Data or data, but Linux does. If a mod doesn't seem to load, check if the folder names match the game's internal directory structure exactly. Strategy for Next Level Modding Since you're already "vibe coding" and tinkering with LLMs, you’ll appreciate this: don't get sentimental about Vortex. It’s notoriously buggy through Wine layers. If you’re doing heavy Bethesda modding, Mod Organizer 2 via STL is objectively superior on Linux because it uses a virtual file system that keeps your base game folder clean. Would you like me to walk you through the specific setup for a particular game you're trying to mod right now?
