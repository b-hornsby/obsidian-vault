---
id: 408203
source: GEMINI
date: 2026-02-17
tags: ['obs-studio', 'desktop-entry', 'linux-applications', 'application-removal']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is removing a desktop entry for OBS Studio, likely as part of troubleshooting or uninstalling the application.
---
# ❯ rm ~/.local/share/applications/com.obsproject.Studio.desktop

~
❯  

### USER
❯ rm ~/.local/share/applications/com.obsproject.Studio.desktop

~
❯  

### GEMINI
If that command finished without an error message, you've successfully deleted the link. Your application launcher (KDE, GNOME, etc.) might still show the "ghost" for a few seconds because it caches its search results. Don't sit there waiting for it to disappear. Force the system to realize the file is gone. The Cleanup If the icon is still visible in your menu, restart your desktop environment's shell or just log out and back in. If you want to be surgical, run this to update the database: update-desktop-database ~/.local/share/applications The Strategy You are currently dealing with the "debris" of a fragmented installation. If pacman didn't find the package, but a desktop entry existed, you likely ran an AppImage or a manual script at some point that "integrated" itself into your system. Check for the configuration bloat I mentioned earlier to ensure you aren't leaving 100MB+ of cache and settings behind: ls -d ~/.config/obs-studio 2>/dev/null || echo "Config folder already gone." Is the icon gone from your launcher now, or are we still chasing a phantom?
