---
category: homelab
date: 2026-03-15
id: 625994
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered errors where install commands and librewolf package weren't
  recognized on CachyOS.
tags:
- command-not-found
- package-installation
- librewolf
- cachyos
- troubleshooting
---
# It said both the install —id command wasn’t recognized and same with librewolf.librewolf

### USER
It said both the install —id command wasn’t recognized and same with librewolf.librewolf

### GEMINI
It looks like your Tiny11 build is "ultra-lite" and stripped out the winget tool entirely. No worries—this is typical for these debloated versions. Since we can't use winget, let's use a native PowerShell script to grab the installer directly from the source. The "Brute Force" Solution Right-click the Start button and select Terminal (Admin) or Windows PowerShell (Admin). Copy and paste this entire command and hit Enter: $url = "https://gitlab.com/api/v4/projects/24386000/packages/generic/librewolf/124.0.1-1/librewolf-124.0.1-1-windows-x86_64-setup.exe"; $out = "$env:TEMP\librewolf.exe"; (New-Object System.Net.WebClient).DownloadFile($url, $out); Start-Process $out -Wait; Remove-Item $out What if that fails? If the script throws an error about "DownloadFile," it’s likely a security policy. Try this even simpler method to just open the download link directly: Press Win + R, type control, and hit Enter. Go to Appearance and Personalization > File Explorer Options. Under the View tab, make sure "Hide extensions for known file types" is unchecked. Now, open PowerShell and type: start https://librewolf.net/installation/windows/ This should force Windows to open the link in whatever basic "wrapper" browser it has left (or even just launch the download). Strategy Check: While you wait for that download: The Drivers: You'll need the Nvidia Game Ready Driver for your 3070. Since you have no browser, you can use the same start command to get to the download page: start https://www.nvidia.com/en-us/geforce/drivers/ Vanguard: Remember, Valorant's anti-cheat is picky. If it complains about "TPM 2.0" or "Secure Boot," we'll need to check your ASUS BIOS settings again. Did the PowerShell script manage to pull the installer for you?
