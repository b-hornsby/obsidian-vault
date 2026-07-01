---
id: 347959
source: GEMINI
date: 2026-03-23
tags: ['overclocking', 'performance-tuning', 'hardware-optimization']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wants optimal performance settings for his given hardware specs.
---
# just give me the best possible settings for my given specs

### USER
just give me the best possible settings for my given specs

### GEMINI
Since you want the "best possible" settings, I’m giving you the values that hit the statistical sweet spot for the PNY RTX 3070. These are the "aggressive-yet-likely-stable" numbers. If you put these in and your screen flickers or the driver resets, your specific chip lost the silicon lottery—back them off by 10%. The "Best Possible" Preset Input these exactly in MSI Afterburner: SettingValueWhy?Power LimitMax (110%–113%)Allows the card to draw more power to maintain high boost clocks.Temp LimitMax (90°C)Prevents the card from slowing down prematurely.Core Clock+120 MHzMost PNY 3070s hit +100 to +150; +120 is the sweet spot for stability in most games.Memory Clock+900 MHzGDDR6 is stable here. You can push +1000, but "error correction" often makes +900 faster in real-world FPS.Fan SpeedCustom CurveSet to hit 100% speed at 75°C. Heat is the enemy of high boost bins. The Strategy (Don't Ignore This) Check for Performance Regression: After applying +900 Memory, run a benchmark. Then drop it to +700. If your FPS stays the same or goes up at +700, keep it there. Memory can "silently fail" where it doesn't crash but slows down to correct errors. The CPU Bottle-neck: Your i7-12700K is a beast. At 1080p, the GPU is your primary limit, so these settings will be noticeable. At 1440p, you're going to hit the 8GB VRAM wall before the clock speed matters in modern titles (like Alan Wake 2 or Indiana Jones). PSU Safety: You have a 750W unit, which is enough, but with a maxed-out 12700K and a maxed-out Power Limit on the 3070, you are getting close to the efficiency peak. If your PC suddenly shuts off (no blue screen, just black), your PSU's Over Current Protection (OCP) is tripping. If that happens, drop the Power Limit back to 100%. Your Immediate Next Step Download Superposition Benchmark or 3DMark Time Spy. Run it once at stock settings, then run it with the values above. Would you like me to tell you what specific score you should be aiming for with these specs to see if your system is underperforming?
