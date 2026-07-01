---
id: 074363
source: GEMINI
date: 2026-01-21
tags: ['wsl', 'ubuntu', 'uninstall', 'clean-slate', 'windows-11']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wants to completely uninstall Ubuntu WSL to start a new project from scratch.
---
# looking to uninstall ubuntu wsl on my machine to start completely fresh on a separate project. no extra fluff just tell me how to completely delete it so i can start fresh please 

### USER
looking to uninstall ubuntu wsl on my machine to start completely fresh on a separate project. no extra fluff just tell me how to completely delete it so i can start fresh please 

### GEMINI
To wipe Ubuntu from your WSL setup and start fresh, you need to do more than just right-click "Uninstall" in the Start menu. If you don't unregister the distribution, the virtual hard drive file (your data and system changes) stays on your disk. Here is the precise, two-step purge to ensure total removal. Step 1: Kill the Distribution (The "Clean Slate" Command) This is the most critical step. It deletes the entire Linux root file system associated with that name. Open PowerShell or Command Prompt (standard user is fine, Admin is better). Run this to see your exact distribution name: wsl --list --verbose Unregister the Ubuntu instance (Replace Ubuntu with the exact name from the list above): wsl --unregister Ubuntu Warning: This is instantaneous and irreversible. Every file, config, and package inside that Ubuntu instance is now gone. Step 2: Remove the Application Wrapper Now that the data is gone, you need to remove the "app" that launches it. Open Settings > Apps > Installed Apps (or "Apps & Features"). Search for Ubuntu. Click the three dots (or the app) and select Uninstall. Verify Total Removal If you want to be certain nothing is "haunting" your system: Run wsl --list again. It should either show no distributions or only the others you intend to keep. Check C:\Users\<YourUsername>\AppData\Local\Packages. If you see a folder named CanonicalGroupLimited.Ubuntu..., and it’s not empty, delete it manually. The New Start To start your fresh project with a clean Ubuntu install: wsl --install -d Ubuntu Next Step: Would you like me to provide a hardened configuration for your new instance (like setting up a non-root user or optimizing memory limits) so you don't end up needing another "fresh start" in a month? Completely Uninstall WSL on Windows 11 This video provides a visual walkthrough of removing both the Linux distributions and the underlying WSL components if you want to clear the entire environment.
