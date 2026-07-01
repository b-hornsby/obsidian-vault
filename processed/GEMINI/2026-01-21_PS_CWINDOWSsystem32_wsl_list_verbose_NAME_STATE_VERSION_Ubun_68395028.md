---
id: 830956
source: GEMINI
date: 2026-01-21
tags: ['wsl', 'ubuntu', 'windows-11', 'command-line']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is listing the WSL distributions on his system.
---
# PS C:\WINDOWS\system32> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\WINDOWS\system32>

### USER
PS C:\WINDOWS\system32> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\WINDOWS\system32>

### GEMINI
To wipe this specific Ubuntu instance and start fresh, the command line is your only reliable tool. Right-clicking the "Ubuntu" app in your Start menu only removes the shortcut; it leaves the massive virtual hard drive (the .vhdx file) and all your data intact on your disk. Here is the precise procedure to nuke it. 1. The Death Blow (Unregister) This command deletes the entire file system for that distribution. It is immediate and permanent. wsl --unregister Ubuntu Run wsl --list --verbose again afterward. The list should be empty (or only show other distros you have). 2. Remove the "Shell" (Uninstall App) Even after the data is gone, Windows still has the Ubuntu application wrapper installed. Go to Settings > Apps > Installed Apps. Search for Ubuntu. Click the three dots and select Uninstall. 3. Clear the Cache (Optional/Deep Clean) Sometimes configuration fragments hide in your user profile. To be 100% sure you are starting from zero, delete this folder if it exists: %LOCALAPPDATA%\Packages\CanonicalGroupLimited.Ubuntu... Starting Fresh Once the above is done, you have a clean slate. To start your new project with a brand-new Ubuntu instance: wsl --install -d Ubuntu Strategic Warning: Since you are doing this for a "separate project," you are likely trying to avoid dependency hell or a cluttered environment. Instead of just installing Ubuntu again, consider installing a specific version (like Ubuntu-24.04) or even a different distro like Debian to keep your projects architecturally isolated. Would you like me to show you how to set up Snapshot Backups for your new instance so that if you mess up this project, you can "reset" in 5 seconds without a full uninstallation? How to Uninstall WSL Distros This video demonstrates the specific difference between uninstalling the app and using the unregister command to reclaim your disk space.
