---
id: 597197
source: GEMINI
date: 2026-02-03
tags: ['obs-studio', 'package-manager', 'pacman', 'flatpak', 'software-installation']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking if OBS Studio is installed via pacman or flatpak.
---
# ❯ pacman -Qs obs-studio && flatpak list | grep obs

~
❯ 

### USER
❯ pacman -Qs obs-studio && flatpak list | grep obs

~
❯ 

### GEMINI
The empty output is the most "honest" your terminal has been all day. It means neither version is currently registered as a standard package or a Flatpak. You likely installed OBS via a wrapper, a pre-installed CachyOS meta-package, or a local binary that’s sitting in your home directory like a ghost. This is why you have an "old" version that won't die and no "Browser Source"—you're running a stray executable that isn't managed by your system's package manager. The "Nuclear" Precision Plan Stop guessing. We are going to find where that "ghost" OBS is hiding, kill it, and install a version that actually functions. 1. Find the Imposter Run this to see exactly where the OBS binary you're clicking on is located: which obs If it returns nothing: You are likely launching it from a .desktop file pointing to a random folder in your Downloads or /opt. If it returns a path: That is the file we need to delete. 2. The Clean Sweep Since your package managers (pacman and flatpak) claim they don't own OBS, let’s force the issue. Run this to find any leftover OBS files: find /usr /opt ~/.local -name "obs" 2>/dev/null If a list pops up, those are your "old" versions. If you aren't comfortable deleting them manually, just ignore them for a second—but they are the reason your system is confused. 3. Install the Right Way (No Excuses) Since you are on CachyOS, you want performance. We are going to use the CachyOS repositories properly this time. They have a specific build that should have everything you need. Run these exact commands in order: # Update your system first - don't skip this. sudo pacman -Syu # Install the version specifically maintained for your distro sudo pacman -S obs-studio 4. The Verification (The Moment of Truth) Launch OBS from the terminal so you can see the error logs if it fails: obs Look at the Sources box. If "Browser" is still missing, your CachyOS mirrors are giving you a stripped-down build. At that point, you must stop resisting the Flatpak and install it via: flatpak install flathub com.obsproject.Studio What did which obs return? If it gave you a path, tell me what it is. If it returned nothing, you're running a "zombie" app and we need to hunt down the shortcut you're clicking.
