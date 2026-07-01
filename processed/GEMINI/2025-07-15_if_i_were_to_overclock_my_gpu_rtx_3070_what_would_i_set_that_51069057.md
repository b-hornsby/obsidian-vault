---
category: homelab
date: 2025-07-15
id: 903655
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to know optimal MSI Afterburner settings for overclocking his
  RTX 3070.
tags:
- overclocking
- rtx-3070
- msi-afterburner
- gpu-settings
---
# if i were to overclock my gpu (rtx 3070) what would i set that to in msi afterburner?

### USER
if i were to overclock my gpu (rtx 3070) what would i set that to in msi afterburner?

### GEMINI
Overclocking a GPU like the RTX 3070 involves increasing its clock speeds (Core Clock and Memory Clock) beyond factory settings to gain more performance. However, there's no single "best" setting that applies to all RTX 3070s, as performance can vary between individual cards (this is known as the "silicon lottery"). Instead of a fixed value, overclocking is a process of testing and gradual adjustment to find the stable limits of your specific card. Here's a general guide using MSI Afterburner, which is a popular and effective tool for this: Before You Start (Important!): Understand the Risks: While modern GPUs have safeguards, pushing them too far can lead to instability, crashes, and in rare cases, shorten the lifespan of your card. Always proceed with caution. Monitoring Software: MSI Afterburner itself has monitoring features. You'll want to keep an eye on: GPU Temperature: Aim to keep it below 80-85°C under load. Core Clock Speed: The actual speed your GPU is running at. Memory Clock Speed: The actual speed of your VRAM. Power Draw/Limit: How much power your card is consuming and if it's hitting its power limit. Stress Test/Benchmark Software: You'll need software to push your GPU and check for stability. Popular choices include: Unigine Heaven/Superposition: Good for general stability testing. 3DMark (Time Spy, Fire Strike): Comprehensive benchmarking with scores to track improvements. Your Favorite Games: Play demanding games to see how your overclock holds up in real-world scenarios. Steps to Overclock Your RTX 3070 in MSI Afterburner: Install MSI Afterburner: Download and install the latest version from the official MSI website. It usually comes bundled with RivaTuner Statistics Server (RTSS), which is useful for on-screen display monitoring. Update GPU Drivers: Ensure your NVIDIA drivers are up to date. Baseline Testing: Before making any changes, run a benchmark (e.g., Unigine Heaven, 3DMark) to get a baseline performance score and observe your stock temperatures and clock speeds. Increase Power Limit and Temperature Limit: In MSI Afterburner, find the Power Limit (%) slider and drag it to its maximum (usually 110-112%). Do the same for the Temp Limit (°C). Click the "Apply" checkmark. This allows your GPU to draw more power and run hotter, giving it more headroom for overclocking. Don't worry, the GPU has built-in thermal protection and will throttle if it gets too hot. Note: Some GPU models, like certain MSI Ventus cards, may have a hard-limited power limit in their BIOS. Overclock the Memory Clock (VRAM) First: The memory on RTX 3070s often has good overclocking potential. Start by increasing the Memory Clock (MHz) in steps of +100 MHz to +200 MHz. Click "Apply" after each step. Run a stability test (benchmark or demanding game) for at least 15-30 minutes. Look for artifacts (visual glitches like flickering, dots, or lines), crashes, or performance degradation (sometimes memory overclocking too high can actually lower performance). If stable and performance increases, continue increasing the Memory Clock by smaller increments (e.g., +50 MHz or +25 MHz) until you encounter instability. Once unstable, dial back the Memory Clock to the last stable setting. Common stable memory overclocks for the RTX 3070 are in the +800 MHz to +1200 MHz range, but again, this varies. Overclock the Core Clock (GPU Core): Once you've found your stable Memory Clock, it's time for the Core Clock. Reset the Core Clock to 0 in Afterburner (leave Memory Clock at your stable setting). Increase the Core Clock (MHz) in smaller steps, usually +15 MHz to +20 MHz at a time. NVIDIA's GPUs often increment in 15MHz steps. Click "Apply" after each step. Run a stability test for 15-30 minutes. Look for crashes or performance degradation. Continue increasing until you hit instability, then dial back to the last stable setting. Typical stable Core Clock overclocks for the RTX 3070 range from +75 MHz to +150 MHz, with some cards going a bit higher. Fine-Tuning and Validation: Once you have stable Core and Memory Clock settings, perform a more extended stability test (e.g., 1-2 hours of a demanding game or benchmark loop). You can try adjusting one or both values slightly up or down to find the absolute "sweet spot" where you get the best performance with no instability. Monitor your temperatures closely throughout this process. Save Your Profile: In MSI Afterburner, once you're happy with your stable overclock, click the "Save" icon (floppy disk). Choose one of the profile numbers (e.g., 1, 2, 3, 4, 5) and click it to save your settings. You can then click the "Windows startup" icon to apply this profile automatically when your PC boots. Example "Starting Points" (use with caution and always test!): While these are not guaranteed for your card, some users have reported stable overclocks in these ranges: Power Limit: Max (110-112%) Temp Limit: Max (84-90°C) Core Clock (MHz): Start around +75 MHz to +100 MHz, then go up in +15/+20MHz steps. Memory Clock (MHz): Start around +800 MHz to +1000 MHz, then go up in +25/+50MHz steps. Important Considerations: GPU Model Variation: Different RTX 3070 models (e.g., MSI Ventus, ASUS ROG Strix, EVGA FTW3) have different cooling solutions and power delivery, which can affect overclocking potential. Cooling: Good airflow in your PC case and efficient GPU cooling are crucial for stable overclocks. Higher temperatures can lead to throttling and instability. Undervolting: Some users prefer "undervolting" (reducing voltage while maintaining or even slightly increasing clock speed) which can improve efficiency, lower temperatures, and sometimes yield better sustained performance than a raw overclock due to reduced power limits. This is a more advanced technique but can be very beneficial for the 30-series cards. Remember, the key is to take it slow, test thoroughly, and prioritize stability over pushing for the absolute highest numbers. Good luck!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
