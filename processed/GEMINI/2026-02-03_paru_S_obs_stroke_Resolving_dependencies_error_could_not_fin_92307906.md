---
category: streaming
date: 2026-02-03
id: 448254
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble installing the obs-stroke plugin using paru due to
  a dependency error.
tags:
- obs-studio
- obs-stroke
- paru
- package-manager
- dependency-error
---
#  paru -S obs-stroke
:: Resolving dependencies...
error: could not find all required packages:
    obs-stroke (target)

~
❯ 

### USER
 paru -S obs-stroke
:: Resolving dependencies...
error: could not find all required packages:
    obs-stroke (target)

~
❯ 

### GEMINI
That failed because obs-stroke isn't a standalone package name in the AUR. On Arch/CachyOS, most of those high-end filters (including Stroke and Drop Shadow) are bundled into a massive plugin called StreamFX, or you have to use a specific collection. Let’s stop guessing at package names and get you the one that actually works on Linux. 1. The Real Package (The "Everything" Solution) The plugin you actually want for shadows, strokes, and outlines on Linux is obs-composite-blur or obs-streamfx. However, StreamFX has been a mess with version compatibility lately. Try this specific one; it’s lightweight and contains a "Stroke" filter: paru -S obs-shaderfilter Once installed and OBS is restarted: Right-click Text -> Filters. Add User-defined shader. Look for a "Stroke" or "Outline" preset. 2. The "I Just Want It to Work" Plan If you don't want to mess with shaders, the most stable way to get filters on Arch is the obs-plugins meta-package or individual reliable ones. Try searching for what's actually available on your mirrors right now: paru -Ss obs-filter Look for obs-multi-theme-skip—it’s a common bundle that includes shadow and outline utilities for Linux users. 3. Brutal Honest Mirror: You are Yak Shaving Yak Shaving: An activity that is seemingly unrelated to your actual goal but is required to solve a problem, which was required to solve a problem, which was... You wanted a white text with a black outline. You are now troubleshooting Arch Linux package dependencies and compiling C++ plugins. The Opportunity Cost: You’ve spent the last 15 minutes being a sysadmin instead of a creator. The Fix: If you aren't going to use the Browser Source (which requires zero installation and works on every OS), then do the "Duplicate and Nudge" method I mentioned earlier. It takes 10 seconds: Text Source A (White). Text Source B (Black, Filter -> Color Correction -> Brightness down). Put B under A. Use arrow keys to offset it. Group them (Ctrl+G). Decision Time: Do you want to continue the "Linux Package Hunt" to find the perfect filter, or do you want to just use the Browser Source CSS I gave you and be done with this in 60 seconds?
