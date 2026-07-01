---
category: homelab
date: 2026-03-10
id: 157255
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for a complete guide on how to set up NordVPN on his CachyOS
  PC.
tags:
- nordvpn
- vpn-setup
- cachyos
- linux-vpn
---
# so from the start, what do i need to do on my pc to get this setup? currently running cachyos

### USER
so from the start, what do i need to do on my pc to get this setup? currently running cachyos

### GEMINI
Since you're on CachyOS, you have the "Arch advantage." Sunshine is in the official repositories, which makes this much cleaner than it is on Windows. Here is the exact, step-by-step sequence to get your PC ready. 1. Install Sunshine Open your terminal and run: sudo pacman -S sunshine 2. Set Up Essential Permissions On Linux, Sunshine needs specific hardware access to capture your screen and "virtually" plug in your Steam Deck's controller. Add your user to the input group: sudo usermod -a -G input $USER Set up the Virtual Input (udev) rule: This allows Sunshine to create the virtual controller for your Steam Deck. Run this whole block at once: echo 'KERNEL=="uinput", GROUP="input", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/85-sunshine-input.rules Give Sunshine permission for screen capture (KMS): sudo setcap cap_sys_admin+p $(readlink -f $(which sunshine)) Note: If you ever update Sunshine, you may need to run this command again. 3. Open the Firewall CachyOS usually has ufw active. If the ports are closed, your Steam Deck won't see the PC. sudo ufw allow 47984,47989,47990,48010/tcp sudo ufw allow 47998,47999,48000/udp 4. Enable and Start the Service You want Sunshine to start automatically every time you log in so you don't have to touch your PC. systemctl --user enable --now sunshine 5. First-Time Configuration On your PC, open your browser and go to: https://localhost:47990 Ignore the security warning: Click "Advanced" and "Proceed to localhost." Create a Username/Password: This is for the web interface only. Pairing: Open Moonlight on your Steam Deck. Your PC should appear. Click it, and it will give you a 4-digit PIN. On your PC's browser (in that Sunshine tab), click the PIN menu at the top, enter the code from the Deck, and click Send. Critical CachyOS/Wayland Note Since CachyOS defaults to KDE Plasma on Wayland, you might get a black screen initially. The Fix: In the Sunshine Web UI (https://localhost:47990), go to Configuration > Audio/Video. Change Video Tool to kms. Restart the service: systemctl --user restart sunshine. Would you like me to show you how to set up a desktop shortcut on your Steam Deck that launches a "Desktop Mode" stream so you can control your whole PC remotely?
