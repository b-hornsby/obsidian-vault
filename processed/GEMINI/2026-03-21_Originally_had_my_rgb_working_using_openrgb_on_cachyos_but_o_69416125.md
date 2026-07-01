---
category: homelab
date: 2026-03-21
id: 583827
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is explaining that his RGB lighting was working with OpenRGB on CachyOS,
  but now it's not working on Tiny11 with iCue.
tags:
- rgb-control
- openrgb
- icue
- cachyos
- tiny11
- software-compatibility
---
# Originally had my rgb working using openrgb on cachyos but on tiny11 and I use icue. Its doesn’t work now tho 

### USER
Originally had my rgb working using openrgb on cachyos but on tiny11 and I use icue. Its doesn’t work now tho 

### GEMINI
Moving from CachyOS (where OpenRGB is king) to a stripped-down Windows like Tiny11 creates a specific problem: iCUE is a "heavy" suite that relies on several background services and dependencies that Tiny11 often trims out for performance. If iCUE isn't seeing your hardware, it's likely because the Corsair Service failed to start or a dependency is missing. 1. The "Tiny11" Service Check Tiny11 often disables non-essential services. iCUE cannot function without its background "drivers." Press Win + R, type services.msc, and hit Enter. Scroll down to everything starting with Corsair. Check the status of Corsair Service and Corsair Device Control Service. If they are "Disabled" or "Manual," right-click them -> Properties -> set Startup Type to Automatic. Click Start for each. If they fail to start, Tiny11 might be missing a specific .NET framework or C++ Redistributable. 2. Dependency Scan iCUE 5 (the modular version) is notorious for failing if the environment isn't "standard." Install Visual C++ Redistributables: Download the "All-in-One" pack from a reputable source (like TechPowerUp) to ensure every year from 2005-2022 is present. Tiny11 usually strips these. Check .NET Framework: Ensure .NET 3.5 and 4.8 are enabled in "Turn Windows features on or off." 3. The "Clean Slate" (Crucial after OpenRGB) If you didn't fully "reset" your hardware before leaving Linux, the controllers might still be in a state OpenRGB left them in. Cold Boot: Shut down the PC, flip the PSU switch to OFF, and hold the power button for 30 seconds to drain the capacitors. This resets the MCU on your RGB controllers. Clean Install iCUE: Use Revo Uninstaller (Portable version is fine) to wipe iCUE. Tiny11's registry can get messy with partial installs. After wiping, reinstall the latest iCUE 5. 4. The "Tiny" Alternative If iCUE continues to fight you (which it often does on debloated Windows), don't waste your time. You already know the better way: SignalRGB: It’s basically the Windows equivalent of the flexibility you had with OpenRGB but with better UI. It usually works on Tiny11 because it doesn't rely on the bloated Corsair service architecture. OpenRGB for Windows: Since you used it on CachyOS, you can use the Windows binary. It’s lightweight and won't trigger the "service failed" errors iCUE is throwing. Strategic Reality Check: You’re an operations guy with an i7-12700K/RTX 3070—you didn't build that rig to spend your Saturday fighting Corsair's bloatware on a stripped-down OS. If the services don't start after step 1, the "opportunity cost" of fixing iCUE is too high. Would you like me to find the specific .NET/C++ packages Tiny11 usually misses, or should we just get OpenRGB/SignalRGB set up so you can get back to your DeFi agent?
