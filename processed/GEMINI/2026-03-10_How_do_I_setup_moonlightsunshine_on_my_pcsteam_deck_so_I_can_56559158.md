---
id: 560034
source: GEMINI
date: 2026-03-10
tags: ['moonlight', 'sunshine', 'game-streaming', 'steam-deck', 'pc-streaming']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan was looking for the easiest way to set up Moonlight/Sunshine game streaming from his PC to his Steam Deck.
---
# How do I setup moonlight/sunshine on my pc/steam deck so I can stream games from my pc to my steam deck? Looking for the path of least resistance and the easiest way to set this up 

### USER
How do I setup moonlight/sunshine on my pc/steam deck so I can stream games from my pc to my steam deck? Looking for the path of least resistance and the easiest way to set this up 

### GEMINI
To set up Moonlight and Sunshine with the "path of least resistance," you need to ignore the complex terminal commands often found in enthusiast forums. Stick to the standard installers and the Discover store. Here is the most direct, streamlined path to getting this running in under 10 minutes. 1. Setup the Host (Your PC) Sunshine is the "server" that sends the game signal. Download: Go to the Sunshine GitHub Releases and download the file ending in windows-installer.exe. Install & Launch: Run the installer. Once finished, it will likely open a web page in your browser (usually https://localhost:47990). Note: If your browser warns you about a "Private Connection," click "Advanced" and then "Proceed" anyway. It’s a local security certificate. Set Credentials: You will be prompted to create a username and password. Do not lose these. You need them to manage the server and pair new devices. Keep it Running: Ensure Sunshine is running in your system tray. 2. Setup the Client (Steam Deck) Moonlight is the "player" that receives the stream. Switch to Desktop Mode: Press the Steam Button > Power > Switch to Desktop. Install Moonlight: Open the Discover Software Center (blue shopping bag icon), search for Moonlight, and click Install. Add to Steam: While still in Desktop Mode, open the Steam Desktop App. Click Add a Game (bottom left) > Add a Non-Steam Game. Find Moonlight in the list, check the box, and click Add Selected Programs. Return to Gaming Mode: Click the "Return to Gaming Mode" icon on your desktop. 3. Pairing the Devices Launch Moonlight: In your Steam Deck library, open Moonlight. Select your PC: Your PC should automatically appear as long as both devices are on the same Wi-Fi. Click it. Enter the PIN: Moonlight will display a 4-digit PIN. Authorize on PC: Go back to your PC. Open the Sunshine Web UI (https://localhost:47990), click the PIN tab at the top, enter the 4-digit code, and click Send. Pro-Tips for the Best Experience The Resolution Fix: By default, your PC might try to stream at its native resolution (e.g., 4K). In Moonlight’s settings on the Steam Deck, set the resolution to 1280x800 (the Deck’s native res) to save bandwidth and reduce lag. Controller Support: If your controller isn't recognized, download and install the ViGEmBus driver on your PC. This allows Sunshine to "virtually" plug in an Xbox controller for the stream. Sleep Mode: If you want to wake your PC from the Deck, ensure "Wake on LAN" is enabled in your PC's BIOS and Windows Network Adapter settings. Would you like me to walk you through how to configure specific bitrates or latency settings for your specific Wi-Fi setup?
