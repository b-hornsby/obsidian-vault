---
category: homelab
date: 2025-12-07
id: 235177
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to completely remove Ubuntu/WSL from his computer.
tags:
- wsl
- ubuntu
- uninstall
- windows-11
---
# how do i fully make sure ubuntu/wsl is deleted from my computer?

### USER
how do i fully make sure ubuntu/wsl is deleted from my computer?

### GEMINI
That is a strategic desire for a clean slate—a decisive move, not just a casual deletion. Your goal is not just to uninstall the app but to erase the persistent data and disable the underlying Windows feature, which is the only way to "fully" remove it. You must follow a rigorous, multi-step process to ensure all traces of the Ubuntu distribution, its data, and the core Windows Subsystem for Linux (WSL) feature are removed. Skipping steps will leave behind large files or an incomplete environment, which is what you're trying to avoid. 🛑 Step 1: Unregister the Ubuntu Distribution (Data Deletion) This is the most critical step for fully deleting the Linux file system and all its data, which can take up significant disk space. Do this before uninstalling the app. Open PowerShell or Command Prompt as an administrator. List your distributions to confirm the exact name (case-sensitive): wsl --list --verbose (Note the name, which is likely just Ubuntu or Ubuntu-22.04, etc.) Unregister the distribution (this deletes all your Linux files and settings): wsl --unregister <DistroName> Replace <DistroName> with the exact name you found (e.g., wsl --unregister Ubuntu). Repeat this for any other Linux distributions listed. 🗑️ Step 2: Uninstall the Ubuntu Application (GUI/Store App) Once the data is gone, remove the application installer/launcher from Windows. Go to Settings > Apps > Installed apps (or Apps & features on older Windows versions). Search for Ubuntu (or the specific distribution name). Click the ellipsis (...) or the item itself, and select Uninstall. If you installed Ubuntu Pro for WSL, find and uninstall that application as well. ⚙️ Step 3: Disable the Windows Subsystem for Linux Feature This removes the core WSL platform from your operating system, ensuring no underlying components remain. Search the Windows Start Menu for "Turn Windows features on or off" and open the utility. In the list, uncheck the box for "Windows Subsystem for Linux." If present, also uncheck the box for "Virtual Machine Platform" (this is used by WSL 2). Click OK. You will be prompted to Restart your computer. You must restart to finalize the feature removal. 🧹 Step 4: Check for Residual Files (Paranoid Cleanup) For absolute completion, manually check the locations where leftover files might reside, especially if you had an older or custom installation. Open File Explorer and navigate to your user profile's local app data: %USERPROFILE%\AppData\Local\ Look for and delete the following folders if they still exist: Packages (look for folders named something like CanonicalGroupLimited.Ubuntu...) Lxss (This is an older WSL directory) Check the user profile root for configuration files: %USERPROFILE%\ Delete the file named .wslconfig (if it exists). Delete the directory named .ubuntupro (if it exists). Following this sequence—Unregister, Uninstall App, Disable Feature, Restart, Manual Check—is the only way to guarantee a truly full and clean removal of Ubuntu and the WSL environment. The video below covers the primary steps for removing a distribution and the WSL feature. Completely uninstall WSL on Windows 11 New Process This video provides a visual walkthrough of the final steps for completely uninstalling the WSL feature on Windows 11.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
