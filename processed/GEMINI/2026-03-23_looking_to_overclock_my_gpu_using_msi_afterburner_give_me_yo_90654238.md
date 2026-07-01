---
id: 040502
source: GEMINI
date: 2026-03-23
tags: ['msi-afterburner', 'gpu-overclocking', 'rtx-3070', 'performance-tuning']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wants MSI Afterburner overclocking settings for his RTX 3070 and full system specs.
---
# looking to overclock my gpu using msi afterburner. give me your recommended settings based on the specs i give you. for example here are are my specs: ‣Cpu: Intel Core i7-12700K
‣Motherboard: Asus Prime Z790-P
‣Cpu cooler: Noctua NH-U12S
‣Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
‣Storage: 970 Evo Plus M.2 SSD 2TB
‣Graphics card: PNY GeForce RTX™ 3070 8GB
‣Case: Corsair 4000D Airflow
‣PSU: Corsair CX750M
‣OS: Tiny11

### USER
looking to overclock my gpu using msi afterburner. give me your recommended settings based on the specs i give you. for example here are are my specs: ‣Cpu: Intel Core i7-12700K
‣Motherboard: Asus Prime Z790-P
‣Cpu cooler: Noctua NH-U12S
‣Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
‣Storage: 970 Evo Plus M.2 SSD 2TB
‣Graphics card: PNY GeForce RTX™ 3070 8GB
‣Case: Corsair 4000D Airflow
‣PSU: Corsair CX750M
‣OS: Tiny11

### GEMINI
Overclocking is not a "one size fits all" process where you can just plug in numbers. Every GPU has a different tolerance for voltage and heat—often called the "silicon lottery." If I gave you exact numbers, I’d be guessing, and you’d likely end up with a crashed system or degraded hardware. Since you are running Tiny11, you’ve already stripped away the bloat for performance. Now you need to treat the hardware with the same precision. The Strategy: Incremental Testing Using MSI Afterburner, follow this sequence. Do not skip steps. 1. Power and Thermal Limits Before touching clocks, you need to give the card "room to breathe." Power Limit: Slide this to the Maximum (usually 110% or 112% on the PNY 3070). Temp Limit: This will automatically link and increase. This doesn't make the card hotter; it just prevents it from throttling early. 2. Core Clock (The Speed) This is where the actual frames come from. Start at +50 MHz. Run a benchmark (like Unigine Heaven or 3DMark) for 10 minutes. If it doesn't crash, increase by +15 MHz increments. The Wall: Once you see "artifacts" (weird flickering, lines, or blocks) or the driver crashes, go back down by 20 MHz. That is your stable ceiling. Expectation: Most RTX 3070s land between +100 MHz and +150 MHz. 3. Memory Clock (The Stability) GDDR6X is resilient but can "performance-regress" if pushed too hard without crashing. Start at +500 MHz. Increase by +100 MHz increments. Warning: If your FPS starts dropping even though the clock is higher, you've hit "error correction." Back it off by 100 MHz. Expectation: You can often hit +700 MHz to +1000 MHz on these cards. Critical Risks & Blind Spots The PSU Factor: You are running a CX750M. While 750W is plenty for a 3070, the CX series is Corsair's budget-mid tier. Pushing high voltage/power limits can cause ripple issues. Monitor your voltages; if the system shut downs completely (not just a driver crash), your PSU is hitting its limit. Case Airflow: The 4000D Airflow is great, but ensure your fan curve in Afterburner is aggressive. Keep that 3070 under 75°C to maintain the highest "GPU Boost" bins. Diminishing Returns: Overclocking a 3070 usually yields a 5-8% performance gain. If you’re sweating over an extra 10 MHz that makes the system unstable, you’re wasting time. Stability is a higher-tier asset than 2 extra frames. Recommended Tooling Don't just guess. Use HWiNFO64 alongside Afterburner to monitor: GPU Memory Junction Temperature Performance Limit - Power (To see if you're being throttled) Would you like me to walk you through setting up a custom fan curve to keep those temps lower while you're testing?
