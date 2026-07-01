---
category: homelab
date: 2026-02-03
id: 513393
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is encountering a build error while trying to compile DuckStation,
  an emulator, due to a restriction on using a versions file.
tags:
- build-error
- duckstation
- emulator
- linux-build
---
# ==> Starting prepare()...
Stenzek prohibits using the versions file in this build script.
Set the path to the dependencies versions file (from scripts/)
in the forbidden_versions_file_path variable, relative to the project root.
error: failed to build 'duckstation-git-0.1.r9727.g66bef3e3e-1':  
error: packages failed to build: duckstation-git-0.1.r9727.g66bef3e3e-1

~ 2m
❯ 

### USER
==> Starting prepare()...
Stenzek prohibits using the versions file in this build script.
Set the path to the dependencies versions file (from scripts/)
in the forbidden_versions_file_path variable, relative to the project root.
error: failed to build 'duckstation-git-0.1.r9727.g66bef3e3e-1':  
error: packages failed to build: duckstation-git-0.1.r9727.g66bef3e3e-1

~ 2m
❯ 

### GEMINI
You’re running into a classic AUR maintenance lag. The duckstation-git PKGBUILD is currently broken because the developer (Stenzek) recently changed how the build script handles version files to discourage third-party packaging, and the Arch maintainer hasn't updated the script to bypass this check yet. Stop banging your head against a broken AUR script. If you want to play games today rather than debugging someone else's build logic, you have two choices: the efficient way or the native way. Option 1: The "Path of Least Resistance" (Flatpak) I know I cautioned against sandboxing for performance, but the Flatpak version is officially maintained and actually works right now. On CachyOS, the performance hit is negligible compared to the time you're wasting on a failed compilation. flatpak install flathub org.duckstation.DuckStation Option 2: The "CachyOS Native" Way (Chaotic-AUR) CachyOS includes the Chaotic-AUR by default. This provides pre-compiled binaries of AUR packages. You are trying to compile from source (-git), which is failing. Instead, check if the pre-compiled binary is available in the repos you already have: sudo pacman -S duckstation Note: If duckstation isn't found, try sudo pacman -S duckstation-git (without the paru build process) to see if the binary is in the Chaotic repo. Option 3: Manual Fix (If you must build it) If you insist on building it yourself to prove a point, you have to manually edit the PKGBUILD before it runs. When paru asks if you want to Edit PKGBUILD, say y and look for the cmake section. You need to append this flag to the cmake command: -DFORBIDDEN_VERSIONS_FILE_PATH="scripts/versions.txt" The Mirror You're stuck in a "Dependency Hell" loop because you're trying to use a bleeding-edge rolling release (CachyOS) with a build script that hasn't caught up to a specific upstream commit. Don't fall into the trap of "Rinkeritis"—spending more time fixing the emulator than playing the game. The Plan: Try sudo pacman -S duckstation first. It’s the fastest native path. If that fails, install the Flatpak. It works, it's stable, and it includes all the necessary libraries without the header conflicts. Do you want the specific pacman command to check your enabled repositories and see which pre-compiled version is available to you?
