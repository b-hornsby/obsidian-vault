---
category: homelab
date: 2026-03-10
id: 889312
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to add individual games from Lutris as non-Steam games
  on his Steam Deck to enable controller support.
tags:
- steam-deck
- lutris
- non-steam-games
- controller-support
---
# okay so for example i have 4 games within lutris and in order to play them with a controller i had to add lutris as a nonsteam game. how do i add these individual games? 

### USER
okay so for example i have 4 games within lutris and in order to play them with a controller i had to add lutris as a nonsteam game. how do i add these individual games? 

### GEMINI
To add your Lutris games individually to Sunshine so they show up in Moonlight on your Steam Deck, you don't need to add Lutris itself. You can trigger each game directly using Lutris's command-line URI. Since you are on CachyOS, here is the most direct way to get this working without the headache of manual file paths. 1. Find the "Slug" (Game ID) for each Lutris Game Lutris uses a "slug" (a short name) to identify games. Open Lutris on your PC. Right-click the game you want to add. Select Configure. Look at the Game info tab. The field labeled Identifier (or the name at the very top of the window in brackets) is your slug (e.g., cyberpunk-2077 or fallout-4). 2. Add the Game to Sunshine Open the Sunshine Web UI (https://localhost:47990) on your PC. Go to the Applications tab and click Add New. Application Name: The name of the game (e.g., Cyberpunk 2077). Command: This is the magic string that launches the game through Lutris: lutris lutris:rungame/YOUR-GAME-SLUG (Replace YOUR-GAME-SLUG with the identifier you found in Step 1). Working Directory: You can leave this blank for Lutris games. Scroll down and click Save. 3. Fixing the Controller Issue You mentioned you originally added Lutris to Steam to get the controller to work. Since you are now bypassing Steam and going straight through Sunshine/Moonlight, you need to ensure the ViGEmBus equivalent on Linux is working so the Steam Deck's inputs are recognized as an Xbox controller. On CachyOS, verify that your user has permission to handle the virtual controller by running this in your terminal (if you haven't already): sudo usermod -a -G input $USER sudo udevadm control --reload-rules && sudo udevadm trigger Note: You may need to restart your PC once for the group permissions to fully "stick." 4. Optional: Add a "Stop" Command If you want the game to actually close when you quit the stream (so it doesn't stay running on your PC), you can add a Detached Command in the Sunshine app settings: Command: pkill -f lutris This ensures that when you're done, the Lutris runner is killed. Pro-Tip for Cover Art To make it look clean on your Steam Deck, go to SteamGridDB, search for your game, right-click a "Grid" image (600x900), and select Copy Image Address. Paste that URL into the Image Path field in Sunshine's Application settings. Repeat this for your other 3 games, then go to the "Troubleshooting" tab in Sunshine and click "Restart Sunshine." They will now appear as individual tiles on your Steam Deck. Do you want to try adding the first one now to see if the controller maps correctly?
