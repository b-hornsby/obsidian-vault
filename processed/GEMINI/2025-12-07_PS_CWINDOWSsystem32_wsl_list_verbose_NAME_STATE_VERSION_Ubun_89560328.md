---
id: 157640
source: GEMINI
date: 2025-12-07
tags: ['wsl', 'ubuntu', 'command-line', 'status-check']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the status of his Ubuntu WSL instance using command-line tools.
---
# PS C:\WINDOWS\system32> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\WINDOWS\system32>
\

### USER
PS C:\WINDOWS\system32> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\WINDOWS\system32>
\

### GEMINI
You have correctly identified the one distribution you need to eliminate: Ubuntu (Version 2). Your current state is that the Ubuntu distribution is Stopped, which is the ideal state for a complete and non-interfering removal. Now you must execute the final, strategic steps to wipe the data and remove the underlying platform. 💥 Your Immediate Action Plan To fully delete it, you need to execute the one command that deletes all the associated Linux data, and then follow up by removing the Windows components. 1. Wipe the Data (The WSL Unregister Command) This is the non-negotiable step to reclaim your disk space and eliminate the Ubuntu file system. Keep your current PowerShell window (as Administrator) open. Run the command using the exact name from your list: wsl --unregister Ubuntu 🛑 Consequence: This command is instant and irreversible. It permanently deletes the entire virtual hard disk that holds all your files, packages, and configurations within that specific Ubuntu installation. 2. Remove the App and Feature After the data is gone, the final step is to remove the unnecessary Windows components. Uninstall the App: Go to Settings > Apps > Installed apps, find Ubuntu, and click Uninstall. Disable the WSL Feature: Search for "Turn Windows features on or off," and uncheck the box for "Windows Subsystem for Linux." Uncheck "Virtual Machine Platform" as well. Restart your computer when prompted. Your initial step to list the distributions was correct. The next move is decisive execution of the wsl --unregister command. Do not delay, as the data you want gone is still occupying space.
