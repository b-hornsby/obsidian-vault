---
category: homelab
date: 2026-03-15
id: 792960
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was on CachyOS without PowerShell and faced a 2-hour download estimate
  for the Tiny11 ISO, looking for alternatives.
tags:
- tiny11-download
- powershell-alternative
- cachyos
- iso-download
- slow-download
---
# im on cachyos so i dont have powershell but when i try to download from the premade iso it says 2 hour download?

### USER
im on cachyos so i dont have powershell but when i try to download from the premade iso it says 2 hour download?

### GEMINI
Archive.org's direct downloads are notoriously throttled. Since you're on CachyOS, you have the perfect toolkit to bypass the slowness and the lack of PowerShell. 1. Fast Download: Use aria2c (Recommended) Archive.org usually offers a Torrent option or allows for multi-threaded downloads. Standard browser downloads are capped, but aria2c can open multiple connections to saturate your bandwidth. Install it first if you haven't: sudo pacman -S aria2 Then, use this command to pull the ISO with 16 concurrent threads (replace the URL with the specific ISO link from the "Show All Files" section of the NTDEV page): aria2c -x 16 -s 16 [URL_OF_THE_ISO] The -x 16 flag tells it to use 16 connections per server, which usually drops that "2 hour" wait down to a few minutes. 2. Can't use the PowerShell Builder? You don't need PowerShell to get a clean result. Since you're already on Linux, you have a better tool for the job once you have the ISO: Ventoy. Install Ventoy from the AUR or official repos: sudo pacman -S ventoy. Flash your USB: Run ventoy-gui and install it to your thumb drive. The "Tiny" Bypass: Ventoy has a built-in plugin system. If you just want to bypass the RAM/TPM/Microsoft Account requirements on a standard Windows ISO (making it "tiny-ish" without the risk of community-modded bugs), you can just drop a small ventoy.json file on the drive. 3. If you must use the "Builder" on Linux If you are determined to run the tiny11maker.ps1 script: Don't use Wine. PowerShell for Windows scripts often rely on DISM (a Windows-specific system image tool) which will not work under Wine. Use a VM: Since you have 32GB of RAM and an i7, just spin up a quick Windows VM in VirtualBox or virt-manager, run the script there to "cook" your ISO, and then move the finished .iso back to your CachyOS host. Summary for right now: Grab the .torrent file from the Archive.org page and open it in Transmission or qBittorrent. Torrents on Archive.org are almost always faster than the direct "2 hour" browser download. Would you like me to find the exact direct-link for the 25H2 version for your aria2c command?
