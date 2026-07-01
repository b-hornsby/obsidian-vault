---
category: general
date: 2025-07-14
id: 553008
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to permanently remove ReShade from his Windows PC, suggesting
  he wants to completely uninstall it.
tags:
- reshade
- uninstall
- windows
- graphics-modding
---
# how do i permanently delete reshade off my windows pc 

### USER
how do i permanently delete reshade off my windows pc 

### GEMINI
ReShade is a bit unique in how it installs and uninstalls, as it typically injects itself into individual games rather than being a standalone program listed in "Apps and Features." Here's how to permanently delete it: Method 1: Using the ReShade Setup File (Recommended) This is the cleanest and most reliable way to uninstall ReShade from each game you've installed it on. Locate the ReShade setup file: Find the ReShade_Setup.exe file that you originally used to install ReShade. If you can't find it, download the latest version from the official ReShade website (reshade.me). Run the setup file: Double-click the ReShade_Setup.exe file to launch it. Select the game: The setup tool will show a list of games. Select the game from which you want to uninstall ReShade. If your game isn't listed, click "Browse..." and navigate to the game's installation folder to select its executable (.exe) file. Choose the rendering API: The setup tool will likely pre-select the rendering API (e.g., DirectX 10/11/12, OpenGL, Vulkan) that ReShade was installed with. Confirm it's correct. Select "Uninstall": Instead of "Install" or "Modify," you'll now see an "Uninstall" option. Select it. Complete the process: Click "Next" and follow any on-screen prompts to complete the uninstallation. Repeat for all games: You need to repeat this process for every single game where you installed ReShade. ReShade is installed per game, not globally. Method 2: Manual Deletion (If the setup file doesn't work or for specific cases) This method is more involved and should only be used if the setup file method fails. Be cautious, as deleting incorrect files can cause issues with your games. Navigate to the game's installation folder: Find the game where ReShade is still active. Right-click the game shortcut (if applicable) and select "Open file location" or "Properties" -> "Open File Location." Alternatively, go to your game library (Steam, Epic Games, etc.) and find the option to browse local files for the game. Delete ReShade files: In the game's root folder (where the main executable .exe file is located), look for and delete the following files and folders: dxgi.dll (Most common for DirectX 10, 11, 12) d3d9.dll (For DirectX 9 games) d3d10.dll (For DirectX 10 games) d3d11.dll (For DirectX 11 games) d3d12.dll (For DirectX 12 games) opengl32.dll (For OpenGL games) ReShade.ini (ReShade's configuration file) ReShade.log (ReShade's log file) ReShade-Shaders (The folder containing ReShade's shaders and textures) Tip: Make sure "File name extensions" are enabled in your Windows File Explorer view options to see .dll, .ini, etc. Check for global ReShade files (less common but possible): Sometimes, if you ticked a "globally enable ReShade on all Vulkan games" option during installation, you might find a ReShade folder in C:\Users\YourUserName\AppData\Local\ReShade\ or C:\ProgramData\ReShade\. If you find these and want to completely remove all traces, you can delete them. Be aware that AppData and ProgramData are hidden folders, so you'll need to enable "Show hidden files, folders, and drives" in File Explorer options. Empty Recycle Bin: After deleting the files, empty your Recycle Bin to permanently remove them. Restart your computer: This helps ensure all processes are terminated and changes take effect. Important Considerations: Game-specific installations: Remember that ReShade is often installed on a per-game basis. You need to uninstall it from each game individually. Third-party uninstallers: While some third-party uninstallers claim to remove ReShade, using the official setup tool or manual deletion is generally more effective and safer for this type of software. Reinstalling the game (last resort): If you've messed up the files or can't get ReShade to fully uninstall from a specific game, a clean reinstallation of that game will usually resolve the issue by replacing all game files.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
