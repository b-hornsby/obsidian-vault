---
category: general
date: 2026-02-27
id: 517175
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble finding the adaptive power setting on his system.
tags:
- adaptive-power
- windows-settings
- troubleshooting
---
# I don’t see the adaptive power setting

### USER
I don’t see the adaptive power setting

### GEMINI
My mistake—I assumed you were on the latest hardware. Since you're on a standard iPhone 15 Plus, you actually won't see the Adaptive Power setting. In iOS 26, Apple locked Adaptive Power behind Apple Intelligence requirements. It’s available for the 15 Pro, 15 Pro Max, and the 16/17 series. On your base 15 Plus, the system doesn't have the specific on-device processing "permission" to run that AI-driven power management. Since you can't use that feature, you need to be even more aggressive with the manual "levers" available to you. 1. The "Liquid Glass" Tax iOS 26 introduced the Liquid Glass UI design (those translucent, oozing blur effects). These are GPU intensive. On a 15 Plus with a 90% battery, this is likely your "hidden" drain. Go to Settings > Accessibility > Display & Text Size. Turn ON "Reduce Transparency." This stops the phone from constantly calculating blur layers behind your menus. 2. The New "Weather Wallpaper" Drain iOS 26.3 added more dynamic Weather wallpapers. If you are using a wallpaper that reflects live conditions (rain, clouds, sun), your phone is pinging GPS and the GPU every time you wake the screen. Action: Switch to a Static Wallpaper. Avoid the "Astronomy" or "Weather" sets if you want to claw back that battery life. 3. Lockdown Background Indexing Since 26.3 is a recent update, your phone is likely still re-indexing your Photos library and Spotlight database. The Test: Go to Settings > Battery. Scroll down to the list of apps. If you see "Home & Lock Screen" or "Siri" taking up more than 15-20% of your usage, your phone is stuck in a background loop. The Fix: Plug it into a charger overnight on Wi-Fi and leave it alone. This allows the indexing to finish so it stops burning juice while in your pocket. 4. Limit "Precise Location" iOS 26.3 expanded how apps use location. Most apps (Instagram, DoorDash, even Weather) don't need to know exactly which room you're in. Go to Settings > Privacy & Security > Location Services. Tap into your most-used apps and toggle OFF "Precise Location." This forces the phone to use lower-power cell tower triangulation rather than the high-power GPS chip. The Reality Check: You've lost 10% of your total capacity. In the world of tech, 90% is "used." If you do all of this and still see a 10-15% drop while the phone is idle for an hour, your battery's voltage may be sagging under the load of the new OS. Would you like me to walk you through how to check which specific background process is the "Top Offender" in your battery logs?
