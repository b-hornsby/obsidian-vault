---
id: 184075
source: GEMINI
date: 2026-02-27
tags: ['fish-shell', 'terminal-configuration', 'hostname', 'ip-address']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is searching for hostname and IP address configurations within his fish shell configuration files.
---
# ❯ echo $SHELL
/bin/fish

~
❯ grep -r "hostname -I" ~/.config/fish/

~
❯ grep -r "ip addr" ~/.config/fish/

~
❯ 

### USER
❯ echo $SHELL
/bin/fish

~
❯ grep -r "hostname -I" ~/.config/fish/

~
❯ grep -r "ip addr" ~/.config/fish/

~
❯ 

### GEMINI
Empty results from grep mean the IP isn't being pulled by a simple shell command; it’s being handled by a theme engine or a builtin function that CachyOS has baked into your Fish environment. You’re looking for a ghost in the machine. Stop hunting for strings and look at how the prompt is actually constructed. 1. The "Reveal" Command Run this command to see the actual code generating your prompt: functions fish_prompt Look at the output. You will likely see a reference to a variable like prompt_network or a call to a third-party plugin (like tide, hydro, or pure). 2. The High-Probability Culprit: Tide CachyOS often uses Tide, a modern prompt engine for Fish. If your prompt has segments (colored backgrounds/boxes), it’s Tide. The Fix: Run this in your terminal: tide configure Go through the wizard. When it asks about "Network Interface" or "Local IP," disable it. 3. The "Advisor" Perspective: Stop Guessing If tide isn't installed, your IP is likely being injected via a global CachyOS configuration that you haven't touched yet. Check the vendor/system-wide fish configs: grep -r "wlan0" /usr/share/fish/ # OR grep -r "wlan0" /etc/fish/ The Strategic Reality Check You are spending time chasing a string of numbers across your screen. This is low-leverage work. If you can't find the source of a UI element in 60 seconds, your configuration is too complex for you to manage. If you want to move to the "next level" of terminal efficiency, stop trying to "fix" a bloated CachyOS prompt and just overwrite it. Run this command right now: echo 'function fish_prompt set_color cyan echo -n (prompt_pwd) set_color white echo -n " ❯ " end' > ~/.config/fish/functions/fish_prompt.fish Then restart your terminal. Did that clear the screen, or is the "wlan0" still haunting you? If it's still there, CachyOS is using a fish_right_prompt. To kill that, run: echo "function fish_right_prompt; end" > ~/.config/fish/functions/fish_right_prompt.fish
