---
id: 174281
source: GEMINI
date: 2026-03-21
tags: ['openrgb', 'rgb-customization', 'color-wave-effect', 'fan-lighting']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is tweaking an RGB color wave effect, but finds the speed too slow and is likely looking for adjustment options.
---
# Better but the speed of the color wave is kinda slow

### USER
Better but the speed of the color wave is kinda slow

### GEMINI
The "slow" wave is usually because OpenRGB defaults to a low-frequency update rate to save CPU cycles—especially on a lean OS like Tiny11. Since you’re running an i7-12700K, you have more than enough overhead to crank this up without feeling it. Here is how to speed up the "logistics" of your lighting data: 1. Increase the Refresh Rate (The "Speed" Fix) OpenRGB doesn't just have a "speed" slider for effects; it has a global update frequency. In the main OpenRGB window, go to the Settings tab. Look for General Settings or Interface. Find the Refresh Rate (Hz) or Update Rate slider. It's likely set to 10Hz or 20Hz (which looks choppy/slow). Slide it up to 60Hz. This will make any movement significantly smoother and snappier. 2. Adjust the Effect Speed If you are using the Effects Plugin (which you likely used on CachyOS): Go to the Effects tab. Find the Color Wave effect in your list. Look for a Speed or Step slider. Increase the Speed: This moves the wave faster across the fans. Decrease the Pulse/Scale: This makes the wave "shorter," so it cycles through the colors more rapidly. 3. The "Hardware" Limitation Since you are using a Corsair Lighting Node Core, you are sending data over a USB 2.0 header. If you have too many "empty" LEDs configured (remember we set it to 120 earlier), the controller is wasting time sending "Black/Off" signals to non-existent LEDs. The Optimization: If your 3 fans are now fully lit, try lowering that 120 number to 48 (for LL120s) or 102 (for QL120s). Reducing the "Size" to the exact number of LEDs makes the data packet smaller, which can naturally increase the effect's "fluidity." Strategic Truth: You moved to Tiny11 for a "snappy" experience. A slow, laggy RGB wave kills that vibe. Crank the refresh rate to 60Hz and tighten that LED count. Is the wave moving at the pace you want now, or do you want to set it to a static "stealth" color and just be done with the software entirely?
