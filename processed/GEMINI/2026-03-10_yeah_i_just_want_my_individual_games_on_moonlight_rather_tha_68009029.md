---
id: 129359
source: GEMINI
date: 2026-03-10
tags: ['moonlight', 'individual-games', 'game-streaming', 'steam-deck', 'desktop-streaming']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified he wants to stream individual games via Moonlight rather than his entire desktop to the Steam Deck.
---
# yeah i just want my individual games on moonlight rather than my whole desktop atm

### USER
yeah i just want my individual games on moonlight rather than my whole desktop atm

### GEMINI
Since you want to see your specific games in the Moonlight menu rather than a full desktop stream, you need to add them as "Applications" in the Sunshine web interface on your PC. Here is the most efficient way to do that for Steam games and others on CachyOS. 1. The Easy Way: Adding Steam Games To launch a Steam game directly, you don't need to find the specific .exe or Linux binary path. You can use Steam’s built-in URI system. Open the Sunshine Web UI on your PC: https://localhost:47990 Click the Applications tab at the top. Click Add New. Application Name: Type the name of the game (e.g., Elden Ring). Command: Use the following format: setsid steam steam://rungameid/[GAME_ID] How to find the ID: Go to the game's store page in Steam; the number in the URL (e.g., store.steampowered.com/app/1245620/) is the ID. Working Directory: You can leave this blank for Steam games. Scroll down and click Save. 2. The Manual Way (For Lutris, Heroic, or Non-Steam) If you have a game installed via Lutris or a standalone binary: Application Name: Game Name. Command: Enter the full path to the executable. Tip: In your file manager, right-click the game's launch file and select "Copy Location" to get the path. Working Directory: Paste the path to the folder containing that file. Click Save. 3. Adding Cover Art (Optional but recommended) If you want it to look "official" on your Steam Deck: In the same Applications edit screen, look for the Image Path field. You can paste a URL to a cover image (search Google Images for "[Game Name] Steam Grid") or a local path to a .jpg or .png. Important: Restart Sunshine Sunshine doesn't always refresh the list instantly. After you save your games: Go to the Troubleshooting tab in the Web UI. Click Restart Sunshine. Now, look at your Steam Deck—the new game icons should appear in Moonlight. Why use setsid? On Linux/CachyOS, using setsid before the steam command ensures that if you lose connection or close Moonlight, the game process is "detached" from Sunshine's session, preventing it from crashing or hanging your desktop environment. Would you like me to show you how to set up a "Global Prep Command" so that your PC's monitor automatically turns off or changes resolution only when you start a stream?
