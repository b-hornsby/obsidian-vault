---
category: coding
date: 2026-03-15
id: 506404
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about installing or using the LibreWolf browser, likely on
  his Linux system.
tags:
- librewolf
- browser-installation
- linux-applications
---
# What if I want librewolf?

### USER
What if I want librewolf?

### GEMINI
If you want LibreWolf, you can get it just as easily with winget. The "Clean" Way (winget) Open PowerShell as Admin and run: winget install --id LibreWolf.LibreWolf -e The "Brute Force" Way If Tiny11 is missing the winget tool, copy and paste this into PowerShell to download and run the installer directly: $Path = $env:TEMP; $Installer = "librewolf_setup.exe"; Invoke-WebRequest "https://gitlab.com/api/v4/projects/24386000/packages/generic/librewolf/122.0.1-1/librewolf-122.0.1-1-windows-x86_64-setup.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Verb RunAs -Wait; Remove-Item $Path\$Installer A Word of Advice for Your Setup: Since you're planning on playing Valorant, keep in mind: Vanguard Drivers: Don't forget to install the official Nvidia drivers for that 3070. LibreWolf won't help with frame rates! The "Bootloader" Problem: Right now, your PC is booting straight into Windows. Once you're done setting up your browsers and games, we'll need to go back and fix the "CachyOS" entry so you can actually choose between Linux and Windows. Would you like me to guide you through getting your CachyOS boot menu back once your Windows drivers are finished?
