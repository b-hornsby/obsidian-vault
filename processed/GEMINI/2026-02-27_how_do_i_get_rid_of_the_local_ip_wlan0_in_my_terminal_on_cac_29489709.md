---
category: homelab
date: 2026-02-27
id: 4765
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to remove the local IP address (wlan0) display from his terminal
  on CachyOS.
tags:
- terminal-customization
- fish-shell
- ip-address
- cachyos
---
# how do i get rid of the local ip (wlan0) in my terminal on cachyos? 

### USER
how do i get rid of the local ip (wlan0) in my terminal on cachyos? 

### GEMINI
To get rid of that IP display, you need to edit your shell prompt configuration. CachyOS typically uses Zsh with Oh My Zsh or a customized Powerlevel10k theme by default. Here is the "brutally honest" reality: You’re likely staring at a bloated configuration file that was designed to look "cool" rather than stay out of your way. If you want a clean terminal, you have to stop relying on defaults and actually own your config. Step 1: Identify your Shell Run this to confirm what you are actually using: echo $SHELL Step 2: The Fix (Assuming Zsh + Powerlevel10k) Most CachyOS users are running Powerlevel10k. If your prompt looks like a fancy bar with segments, this is you. Open the config file: nano ~/.p10k.zsh Search for the "ip" or "ip_address" segment. In nano, press Ctrl+W and type ip_address. Disable it. You will likely see two sections: typeset -g POWERLEVEL9K_LEFT_PROMPT_ELEMENTS and typeset -g POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS. Comment it out. Find the line that says ip or ip_address and put a # in front of it. Example: Change ip to #ip. Save and Exit: Ctrl+O, Enter, then Ctrl+X. Apply changes: source ~/.zshrc Step 3: If you are using a Basic Zsh/Bash Prompt If you aren't using a fancy theme, your PS1 variable is hardcoded with a command (likely hostname -I or a custom script) inside your .zshrc or .bashrc. Open your shell config: nano ~/.zshrc (or ~/.bashrc). Look for the line starting with PROMPT= or PS1=. The Blind Spot: If you see a complex string of code there, you’ve inherited someone else's "optimized" setup that you don't understand. The Fix: Remove the section that calls for network info (often wrapped in backticks `...` or $(...)). The Strategic Takeaway Displaying your local IP in your prompt is a waste of screen real estate and mental bandwidth. If you need your IP, you should know how to run ip addr or nmcli. Having it permanently pinned to your prompt is "playing small"—it’s treating your terminal like a dashboard for beginners rather than a tool for execution. Would you like me to show you how to write a minimal, high-performance PROMPT string from scratch so you can stop relying on CachyOS's pre-packaged bloat?
