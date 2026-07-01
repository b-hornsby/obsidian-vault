---
category: homelab
date: 2026-02-04
id: 560483
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wanted to change the ASCII art logo in neofetch/fastfetch on KDE CachyOS.
tags:
- neofetch
- ascii-art
- kde
- cachyos
- customization
---
# how to change ascii kde cachyos?

### USER
how to change ascii kde cachyos?

### GEMINI
Changing the ASCII art in your terminal—specifically the one that appears when you launch a fetch tool like fastfetch (the default in CachyOS) or neofetch—is a common tweak. Since you're on CachyOS, you're likely seeing the CachyOS logo or a generic KDE one. To change it, you don't actually "change KDE"; you modify the configuration of the fetch utility you are using. 1. Identify Your Fetch Tool Most modern Arch-based systems like CachyOS have moved to fastfetch because it's significantly faster than the older neofetch. Open your terminal and type fastfetch. If that works, you are using fastfetch. If not, try neofetch. 2. Changing the Logo in Fastfetch Fastfetch uses a JSONC configuration file. To change the ASCII art to a KDE logo (or any other): Generate a local config (if you haven't already): fastfetch --gen-config Edit the config file: micro ~/.config/fastfetch/config.jsonc (Note: Use nano or vim if you don't have micro installed). Find the "logo" section: Look for a line that says "logo": { ... } or just "logo": "auto". Change the source: To force the KDE logo, change it to: "logo": { "source": "kde" } Save and exit. Next time you run fastfetch, you'll see the KDE gear. 3. Changing the Logo in Neofetch (Legacy) If you are still using Neofetch, the process is slightly different: Edit the config: micro ~/.config/neofetch/config.conf Locate ascii_distro: Scroll down until you find ascii_distro="auto". Change it to: ascii_distro="kde" Save and exit. 4. Making it Permanent (Autostart) If you want this ASCII art to appear every time you open the terminal, you need to add the command to your shell's rc file. Since you're on CachyOS, you are likely using Fish or Zsh. For Fish (CachyOS Default): micro ~/.config/fish/config.fish Add fastfetch to the bottom of the file. For Zsh: micro ~/.zshrc Add fastfetch to the bottom. The Reality Check You're asking about changing a logo. This is "ricaging"—purely aesthetic. While it feels like "customizing," it adds zero functional value to your workflow. If your goal is high-level mastery of CachyOS or KDE, don't get stuck in the trap of spending hours tweaking ASCII characters while your actual system optimization or scripting skills stagnate. Opportunity Cost: Every minute spent hunting for the "perfect" terminal logo is a minute not spent learning the underlying Arch package management (pacman/yay) or mastering KDE's KWin scripts. Would you like me to show you how to automate system maintenance tasks in CachyOS so you can spend less time on aesthetics and more on performance?
