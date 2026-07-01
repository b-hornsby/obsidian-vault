---
id: 848012
source: GEMINI
date: 2026-02-03
tags: ['obs-studio', 'command-line', 'path-resolution']
category: streaming
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the location of the OBS Studio executable using the 'which' command.
---
# ❯ which obs
/home/toastedmel0n/.local/bin/obs

~
❯ 

### USER
❯ which obs
/home/toastedmel0n/.local/bin/obs

~
❯ 

### GEMINI
There it is. You’re running a standalone binary tucked away in your local user folder. This is why pacman and flatpak couldn't find it—it’s a "ghost" installation. It’s likely missing the Browser Source because it doesn't have the necessary library links to the Chromium Embedded Framework (CEF) that a proper system package would have. You are playing "system admin" manually, and you're losing. Let's fix this with surgical precision. 1. Kill the Ghost You need to delete that local binary so it stops overriding the system commands. rm /home/toastedmel0n/.local/bin/obs Note: If there is an obs-studio folder in ~/.local/bin/ or ~/.local/share/, get rid of those too. Clean house. 2. Install the Managed Version Now that the path is clear, install the version that is actually built for your OS and includes the browser dependencies. sudo pacman -Syu obs-studio 3. The "CachyOS" Check CachyOS users often optimize their systems to death. If you install the native obs-studio and Browser Source still isn't there, it’s because the Arch/Cachy repositories sometimes split the browser functionality into a separate package to save space or because of licensing. Check if this package exists and install it: sudo pacman -S obs-browser (Note: On many Arch builds, this is already included in obs-studio, but checking ensures you aren't leaving it to chance.) 4. Verify the Path After installing, run which obs again. It should now say: /usr/bin/obs Why this matters By running that file in .local/bin, you were bypassing all the shared libraries the OS provides. You were essentially driving a car with no wheels and wondering why it wouldn't move. Moving to /usr/bin/obs (the system path) ensures OBS can actually see the browser plugins. Do this now: Delete that local file and install via pacman. Once you open OBS, look at the "+" icon in Sources. Is "Browser" there? If not, your distro's repo is broken, and I'm going to force you to use the Flatpak for your own sanity.
