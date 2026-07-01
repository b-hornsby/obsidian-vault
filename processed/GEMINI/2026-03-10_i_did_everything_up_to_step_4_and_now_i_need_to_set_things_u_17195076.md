---
id: 175493
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'vpn-setup', 'gaming', 'lutris']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan has followed a NordVPN setup guide and now wants to configure it to launch from the Steam Deck's gaming mode, avoiding the desktop environment.
---
# i did everything up to step 4 and now i need to set things up on my steam deck before we continue. i would like the ability to launch it from the game side of things rather than running desktop each time 

### USER
i did everything up to step 4 and now i need to set things up on my steam deck before we continue. i would like the ability to launch it from the game side of things rather than running desktop each time 

### GEMINI
To get Moonlight running directly from your Steam Deck's Gaming Mode (the "game side"), you still have to take one quick trip into Desktop Mode to install it and tell Steam it exists. Here is the most direct path to setting up the Deck: 1. Install Moonlight (Desktop Mode) Press the Steam Button > Power > Switch to Desktop. Open the Discover Software Center (the blue shopping bag icon on your taskbar). Search for Moonlight and click Install. 2. Add it to Gaming Mode This is the critical step to ensure you never have to go back to Desktop Mode again: While still in Desktop Mode, open the Steam desktop app. Click Add a Game in the bottom-left corner. Select Add a Non-Steam Game... Find Moonlight in the list, check the box, and click Add Selected Programs. Double-click the Return to Gaming Mode icon on your desktop. 3. Final Pairing (Gaming Mode) Now in Gaming Mode, go to your Library > Non-Steam tab. Open Moonlight and click Play. Your CachyOS PC should appear in the list. Click it. A 4-digit PIN will appear on your Steam Deck screen. 4. Authorize on your PC Go to your PC. Open your browser to https://localhost:47990. Click the PIN tab at the top. Enter the 4-digit code shown on your Steam Deck and click Send. Optimize the Settings (Inside Moonlight) Before you launch a game, click the Settings (gear icon) in the top right of the Moonlight app on your Deck: Resolution: Set to 1280x800 (this matches your Deck perfectly). Frame Rate: Set to 60 FPS (or 90 FPS if you have the OLED Deck). Video Bitrate: Start at 30 Mbps. If your Wi-Fi is solid, you can bump this to 50 Mbps for better clarity. Now that you're paired, would you like me to help you set up "Desktop" as an app in Sunshine so you can stream your entire CachyOS desktop to your Deck instead of just individual games?
