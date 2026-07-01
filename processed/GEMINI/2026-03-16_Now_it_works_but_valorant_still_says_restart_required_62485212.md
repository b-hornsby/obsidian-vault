---
category: homelab
date: 2026-03-16
id: 109871
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that while something is working, Valorant still requires
  a restart, suggesting a problem with secure boot or game compatibility.
tags:
- valorant
- secure-boot
- restart-required
- game-compatibility
---
# Now it works but valorant still says restart required?

### USER
Now it works but valorant still says restart required?

### GEMINI
That "Restart Required" message is the bane of every Linux/Windows dual-booter. If your BIOS says Secure Boot is Enabled and you’re actually inside Windows, the hardware side is fixed. The issue now is that Vanguard (Valorant's anti-cheat) is a "Type-0" driver. It has to be the very first thing that loads when Windows starts. If you've been hopping back and forth between Linux and Windows during this troubleshooting, Vanguard often "desyncs" or fails to initialize properly. 1. The "Cold Boot" Fix Vanguard hates "Fast Startup" and warm reboots. In Windows, click Start and type "Control Panel." Go to Hardware and Sound > Power Options > Choose what the power buttons do. Click "Change settings that are currently unavailable" and Uncheck "Turn on fast startup." Shut down the PC completely (not a restart). Wait 10 seconds. Turn it on, boot into Windows, and try the game. 2. Check the "VGC" Service Sometimes Vanguard’s service gets disabled during bootloader crashes. Press Win + R, type services.msc, and hit Enter. Find the vgc service. Right-click it, go to Properties, and ensure Startup type is set to Automatic. Click Start if it isn't running. 3. Verify the Status in Windows Let’s make sure Windows actually "sees" what the BIOS is doing. Press Win + R, type msinfo32, and hit Enter. Look for Secure Boot State. It must say On. If it says "Off" or "Unsupported," we need to check your BIOS "OS Type" setting again. 4. The Last Resort: Reinstall Vanguard If you've been messing with bootloaders, Vanguard might have flagged its own files as "corrupted" because the boot path changed. Uninstall Riot Vanguard from "Add or Remove Programs." Restart your PC. Open the Riot Client and it will prompt you to "Repair/Reinstall Vanguard." Restart one more time. Check msinfo32 first—does it show Secure Boot as "On"?
