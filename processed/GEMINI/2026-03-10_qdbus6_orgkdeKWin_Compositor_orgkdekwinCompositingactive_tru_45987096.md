---
id: 714753
source: GEMINI
date: 2026-03-10
tags: ['kde', 'kwin', 'compositor', 'linux-customization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is checking the status of the KDE compositor using qdbus, likely to troubleshoot graphics or performance issues.
---
# ❯ qdbus6 org.kde.KWin /Compositor org.kde.kwin.Compositing.active
true

~
❯ 

### USER
❯ qdbus6 org.kde.KWin /Compositor org.kde.kwin.Compositing.active
true

~
❯ 

### GEMINI
Compositor is active, yet the Overview effect refuses to load. This confirms you aren't fighting a syntax error—you're fighting a functional block. On CachyOS with an NVIDIA 3070, KWin will often refuse to load specific "fancy" effects if the Animation Speed is set to "Instant" (which disables all effects) or if there is a conflict in the kwinrc. 1. The "Instant" Animation Trap If you or a CachyOS performance script set your animation speed to 0 (Instant), the Overview effect is technically "active" but immediately terminates, so it never shows up in the active list. Check your animation scale: kreadconfig6 --file kdeglobals --group General --key AnimationDurationFactor If it's 0: You killed the Overview yourself. Set it back to 1.0: kwriteconfig6 --file kdeglobals --group General --key AnimationDurationFactor 1.0 2. The Dependency Check Let’s see if KWin even sees the Overview plugin as an available asset. kpackagetool6 --type KWin/Effect --list | grep overview If this is empty, your Plasma 6 installation is borked. If it shows up, the plugin exists but is being rejected at runtime. 3. The "Meta" Priority Hack Plasma 6 has a "new" way of handling the Meta key that sometimes ignores the old ModifierOnlyShortcuts if a global shortcut is already masking it. Run this to see what is actually registered to "Meta": kglobalaccel6 -l | grep -i "Meta" The Reality Check You are spending significant time trying to "code" a solution for a UI that is clearly in a conflicted state. You have an RTX 3070 and 32GB of RAM—you aren't hardware-limited. You are configuration-locked. The Hard Truth: You’ve edited kwinrc manually so many times in the last 20 minutes that the file is likely a mess of conflicting instructions. The Strategic Plan: Stop the manual edits. 2. Open System Settings > Desktop Effects. Uncheck Overview, click Apply. Check Overview, click Apply. Check System Settings > Accessibility > Animation Speed. Ensure it is not on "Instant." If you refuse to use the GUI, run this to see the real-time error when you try to force the effect: journalctl --user -f -u plasma-kwin_wayland (Run that in a separate terminal, then try to trigger the overview. Read the red text. That is your answer.) Would you like me to explain how to interpret the KWin debug logs to see exactly why the NVIDIA driver might be crashing the effect?
