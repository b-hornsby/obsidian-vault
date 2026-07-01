---
category: homelab
date: 2025-07-27
id: 466384
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is troubleshooting a drive that shows full storage in file explorer
  but isn't appearing.
tags:
- drive-troubleshooting
- storage
- file-explorer
- windows-11
---
# that isn't it. the drive shows the full storage when looking in file explorer though?

### USER
that isn't it. the drive shows the full storage when looking in file explorer though?

### GEMINI
You are correct to point out the discrepancy. While the file explorer shows the full storage of Drive 1 (D:), and Steam does list "Drive 1 (D:)" under its storage settings, the crucial part is that Steam is reporting "0 B FREE OF 0 B" for it. This "0 B FREE OF 0 B" is the key. It means that while Steam recognizes the existence of a "D:" drive, it's not recognizing it as a valid Steam Library Folder, or it's encountering an issue accessing it as such. Here's a more detailed breakdown of why this might be happening and what you can do, given that "Add Drive" wasn't the solution: Possible Reasons for "0 B FREE OF 0 B" and Solutions: No Steam Library Folder Present or Corrupted: Reason: Even if the drive exists, Steam needs a specific folder designated as a "Steam Library Folder" to install games there. If one doesn't exist, or if an existing one is corrupted or its permissions are wrong, Steam will show 0 bytes. Solution: Try "Add Drive" again carefully: Click the "Add Drive" button in Steam's Storage settings. A window should pop up allowing you to browse and select the D: drive. When you select it, Steam should prompt you to create a new Steam Library Folder on that drive. If you've tried this, and it didn't work, proceed to the next steps. Manually Create a Folder (if "Add Drive" fails): Go to your D: drive in File Explorer. Create a new folder, for example, named "SteamLibrary" or "Steam Games." Then, go back to Steam, click "Add Drive," and try to select this newly created folder on your D: drive. Permissions Issues: Reason: Steam might not have the necessary permissions to read from or write to the D: drive or the existing Steam Library folder on it. Solution: Run Steam as Administrator: Close Steam completely. Right-click on your Steam shortcut and select "Run as administrator." Then, check your storage settings again. If this works, it's a strong indication of a permissions problem. You might need to adjust folder permissions permanently. Check Folder Permissions: In File Explorer, navigate to your D: drive. Right-click on the drive (or the Steam Library folder if one exists) and select "Properties." Go to the "Security" tab. Check the permissions for your user account and "Users" group. Ensure they have "Full control" or at least "Modify," "Read & execute," "List folder contents," "Read," and "Write" permissions. If not, click "Edit" to change them. Drive Formatting/Type Issues (Less Likely, but possible): Reason: While your drive shows up, in rare cases, a drive might be formatted in a way that Steam struggles with, or it might be a network drive that Steam doesn't fully support for library folders. Solution: Check the "File system" type in the Drive Properties (as shown in your first image, it's NTFS, which is correct). If it were something unusual, that could be a factor. Antivirus/Security Software Interference: Reason: Sometimes, aggressive antivirus or security software can block Steam from accessing certain drive locations, especially if it's a new or previously unused location for game installations. Solution: Temporarily disable your antivirus software (just for a few minutes) and then try adding the drive in Steam again. If it works, you'll need to add an exception for Steam or its library folders in your antivirus settings. Steam Client Glitch: Reason: Occasionally, the Steam client itself can have a temporary glitch. Solution: Restart Steam: Fully exit Steam and then restart it. Restart your computer: A full system restart can sometimes resolve underlying issues. Clear Steam Download Cache: Go to Steam > Settings > Downloads > Clear Download Cache. This often resolves various Steam-related issues without affecting your installed games. What to do next: Confirm "Add Drive" behavior: When you click "Add Drive," what exactly happens? Does it open a file browser? Does it give an error message? Does it simply do nothing? Knowing this will help narrow down the problem. Check for an existing steamapps folder: On your D: drive, do you see a folder named SteamLibrary or a folder that contains a steamapps folder? If so, try navigating to it within Steam's "Add Drive" option. Let me know what happens when you try to "Add Drive" and if you've already tried any of the above steps!
