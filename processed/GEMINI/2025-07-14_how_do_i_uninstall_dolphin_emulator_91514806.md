---
category: general
date: 2025-07-14
id: 615296
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to uninstall the Dolphin emulator, indicating he wants
  to remove it from his system.
tags:
- dolphin-emulator
- uninstall
- windows
- game-emulation
---
# how do i uninstall dolphin emulator?

### USER
how do i uninstall dolphin emulator?

### GEMINI
Uninstalling Dolphin Emulator is generally straightforward, as it often doesn't install itself like traditional programs. For most users, especially if you downloaded it directly from the official Dolphin website, it's considered a "portable" application. Here's how to uninstall Dolphin Emulator depending on your operating system: For Windows 🪟 Method 1: Delete the Dolphin Folder (Most Common) If you downloaded Dolphin as a ZIP file and extracted it, it likely doesn't have an uninstaller. In this case, simply deleting the folder where you extracted Dolphin will remove the emulator itself. Close Dolphin: Make sure Dolphin Emulator is completely closed before proceeding. Locate the Dolphin Folder: Navigate to the directory where you unzipped or installed Dolphin. This is often in your "Downloads," "Program Files," or a custom folder you created. Delete the Folder: Right-click on the entire "Dolphin" folder and select "Delete." Method 2: Via Apps & Features (If installed traditionally) If you installed Dolphin through an installer that added it to your system's programs, you can uninstall it like any other application. Open Settings: Windows 10/11: Right-click the Start button and select "Apps and Features" or go to Settings > Apps > Apps & features. Windows 7/8: Go to Control Panel > Programs > Programs and Features. Find Dolphin: Scroll through the list of installed programs and look for "Dolphin" or "Dolphin Emulator." Uninstall: Click on "Dolphin" and then select "Uninstall." Follow any on-screen prompts. Method 3: Using the Uninstaller.exe (Less Common) Some installations might include an uninstaller executable within the Dolphin folder. Locate Installation Folder: Go to the folder where Dolphin is installed (e.g., C:\Program Files\Dolphin). Run Uninstaller: Look for a file named uninstall.exe or uninst000.exe and double-click it to start the uninstallation process. Removing User Data and Settings (Optional) Even after uninstalling the main program, Dolphin often leaves behind user data like configuration files, save states, and save games. If you want a complete removal, you'll need to delete these too. Open Dolphin User Folder: Launch Dolphin Emulator (if you haven't deleted the main program yet). Go to File > Open User Folder at the top left of the Dolphin window. Delete Contents: This will open a folder containing Dolphin's user data. You can delete everything in this folder. Caution: If you plan to reinstall Dolphin later and want to keep your saves, do NOT delete the GC (GameCube saves), StateSaves, and Wii (Wii saves) subfolders within the User Folder. For macOS 🍎 Quit Dolphin: Ensure Dolphin Emulator is not running. You can use Force Quit (from the Apple menu) if necessary. Open Applications Folder: Go to your Applications folder. Drag to Trash: Drag the "Dolphin" application icon to the Trash. Empty Trash: Right-click on the Trash icon in your Dock and select "Empty Trash." Removing Residual Files on macOS (Optional) To remove all related files, you'll need to delete files from your Library folder. Open Finder: Click on your desktop to make Finder active. Go to Folder: In the menu bar, click Go > Go to Folder... Enter Path: Type ~/Library/Application Support/Dolphin and press Enter. Delete this folder. Check Caches: Repeat step 3 with ~/Library/Caches/org.dolphin-emu.dolphin and ~/Library/Caches/c0b20623.org.dolphin-emu.dolphin if they exist, and delete them. You might also find preference files in ~/Library/Preferences/ that start with org.dolphin-emu.dolphin. For Linux 🐧 How you uninstall Dolphin on Linux depends on how you installed it (e.g., through a package manager like apt or dnf, or by compiling it from source, or using a portable version). If installed via a package manager (e.g., Ubuntu/Debian): Open Terminal: Open your terminal application. Remove Package: Use the appropriate command for your package manager: For Debian/Ubuntu-based systems: sudo apt-get remove dolphin sudo apt-get autoremove sudo apt-get remove dolphin removes the main Dolphin package. sudo apt-get autoremove removes any automatically installed dependencies that are no longer needed. If using a portable version (extracted from a tar.gz): Delete the Folder: Simply navigate to the directory where you extracted the Dolphin files and delete the entire folder. Removing User Data and Configuration Files on Linux (Optional) Dolphin's user data and configuration files are typically located in your home directory. Open Terminal: Open your terminal application. Delete Configuration Directory: rm -rf ~/.config/dolphin-emu Delete Data Directory: rm -rf ~/.local/share/dolphin-emu Important Notes: Backup Saves: Always back up your save files before completely uninstalling any emulator if you want to keep your game progress! Third-Party Uninstallers: While some third-party uninstallers claim to remove all traces of a program, for Dolphin, manually deleting the folders is usually sufficient and often the only method if it was a portable installation. Running Processes: Ensure Dolphin is not running in the background before attempting to delete its files. You can check your Task Manager (Windows) or Activity Monitor (macOS) or use htop/ps aux | grep dolphin (Linux) to verify.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
