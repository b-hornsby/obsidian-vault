---
category: homelab
date: 2026-03-15
id: 980282
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was stuck on a fresh OS install desktop without a browser and couldn't
  download drivers.
tags:
- fresh-install
- no-browser
- driver-download
- windows-setup
- networking-issues
---
# I’m in the desktop now but I can’t download a browser to get my drivers and things

### USER
I’m in the desktop now but I can’t download a browser to get my drivers and things

### GEMINI
Tiny11 is so stripped down that it even cuts the browser, but Windows has a "secret" terminal tool called winget that can bypass this. Since you have an internet connection, here is how to get Chrome or Firefox without a browser: 1. Open PowerShell as Admin Right-click the Start button and select Terminal (Admin) or Windows PowerShell (Admin). 2. Type the "Magic" Command Copy and paste one of these into the terminal and hit Enter: For Chrome: winget install Google.Chrome For Firefox: winget install Mozilla.Firefox Note: The first time you run this, it might ask you to agree to source agreements. Type Y and hit Enter. If "winget" is not found: Sometimes Tiny11 is so lean that even winget is missing. If that happens, we'll use a "brute force" PowerShell command: Copy this entire block: $Path = $env:TEMP; $Installer = "chrome_installer.exe"; Invoke-WebRequest "https://dl.google.com/chrome/install/latest/chrome_installer.exe" -OutFile $Path\$Installer; Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait; Remove-Item $Path\$Installer Paste it into PowerShell and hit Enter. Wait about 60 seconds. Chrome will silently install itself and appear on your desktop. What's Next? Once you have a browser, go straight to the Nvidia and Asus websites to get your drivers. Does the winget command work for you, or do we need to try the brute force script?
