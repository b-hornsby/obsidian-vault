---
id: 142318
source: GEMINI
date: 2026-02-02
tags: ['obs-studio', 'replay-buffer', 'autostart', 'cachyos', 'streaming-config']
category: streaming
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was frustrated that OBS Studio's replay buffer still wasn't starting automatically when launching via the desktop icon.
---
# it still doesn't start with replay buffer when i launch obs via the icon

### USER
it still doesn't start with replay buffer when i launch obs via the icon

### GEMINI
If you’re clicking the icon and it’s still not starting the buffer, it means your system is still ignoring your custom file and launching the global one at /usr/share/applications/com.obsproject.Studio.desktop. On some modern Linux desktops (especially with Fish and certain launchers), the system-level shortcut is "sticky." We need to be more aggressive. The "Surgical" Fix: Override the Exec Path Instead of fighting the shortcut, we will create a local binary override. This works regardless of which icon you click because it intercepts the obs command itself. Create a local 'bin' directory (if it doesn't exist): mkdir -p ~/.local/bin Create a wrapper script named obs: printf '#!/bin/bash\n/usr/bin/obs --startreplaybuffer "$@"' > ~/.local/bin/obs Make it executable: chmod +x ~/.local/bin/obs Ensure your local bin is prioritized: In Fish, your PATH usually includes ~/.local/bin at the front. Run this to check: echo $PATH | grep .local/bin If it shows up, proceed. If not, let me know. The Reality Check By doing this, every time you launch OBS (from the terminal, the icon, or a script), it will always add the --startreplaybuffer flag. This is the "brute force" way to win against the OS. Test it now: Close OBS completely. Click the normal OBS icon. The Result: The Replay Buffer should be running. Why the Shortcut Failed Most likely, your Desktop Environment (KDE/GNOME) is reading the ID from the flatpak or the system-wide desktop file and ignoring the local one because the Desktop ID matches. By creating the wrapper in ~/.local/bin/obs, we are essentially tricking the system into running our "version" of the program before it finds the real one. Is the button "Stop Replay Buffer" now visible when you click the icon? If yes, you're finally ready to play. If no, we need to check if your PATH is actually looking at your local bin first.
