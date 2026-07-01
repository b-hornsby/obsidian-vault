---
id: 351753
source: GEMINI
date: 2026-03-10
tags: ['cachyos', 'pc-os', 'streaming-setup', 'moonlight-sunshine']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan mentioned his PC is running CachyOS while setting up game streaming to his Steam Deck.
---
# Should also mention my pc is on cachyos at the moment

### USER
Should also mention my pc is on cachyos at the moment

### GEMINI
Since you're on CachyOS, the process is actually more efficient than Windows because Sunshine is available directly in the optimized Cachy repositories. You don't need to hunt for AppImages or GitHub releases. Here is the path of least resistance for your specific Linux setup. 1. Install Sunshine (Host PC) CachyOS includes Sunshine in its own repository, so you can skip the AUR and use the optimized version. Open your terminal and run: sudo pacman -S sunshine Permissions: For the Steam Deck to control your PC, Sunshine needs permission to access the "uinput" interface. Run this command: sudo usermod -a -G input $USER (You will need to log out and log back in for this to take effect.) 2. Configure the CachyOS Firewall CachyOS usually comes with ufw (Uncomplicated Firewall) enabled by default, which will block the Steam Deck from seeing your PC. Run this single command to open the necessary ports: sudo ufw allow 47984,47989,47990,48010/tcp && sudo ufw allow 47998,47999,48000/udp 3. Launch & Pair Start Sunshine: Type sunshine in your terminal or find it in your App Launcher. Set Password: It will likely prompt you to open https://localhost:47990 to create your login. Steam Deck Setup: Install Moonlight via the Discover Store in Desktop Mode (as outlined previously). Pairing: Open Moonlight on the Deck, click your PC's name, and enter the PIN in the Sunshine Web UI under the PIN tab. 4. Enable Auto-Start (The "Set and Forget" step) To make sure you don't have to manually start Sunshine every time you reboot your PC: Run this command: systemctl --user enable --now sunshine The "CachyOS" Advantage Since you are on a Wayland-based system (likely KDE Plasma on Cachy), you might run into an issue where the screen is black but audio works. The Fix: In the Sunshine Web UI (https://localhost:47990), go to Configuration > Audio/Video and ensure the Video Tool is set to kms. This is the most stable method for Linux desktop capture. Would you like me to show you how to set up a script that automatically matches your PC's resolution to the Steam Deck's 1280x800 whenever you start a stream?
