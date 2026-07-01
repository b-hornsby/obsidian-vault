---
category: homelab
date: 2026-02-03
id: 582130
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to remove MacTahoe theme files on CachyOS but the rm command
  fails due to fish shell wildcard handling.
tags:
- mac-tahoe
- theme-removal
- cachyos
- kde
- fish-shell
---
# ❯ sudo rm -rf /usr/share/icons/MacTahoe* /usr/share/themes/MacTahoe* /usr/share/aurorae/themes/MacTahoe* /usr/share/colo
r-schemes/MacTahoe* /usr/share/plasma/desktoptheme/MacTahoe* /usr/share/plasma/look-and-feel/com.github.vinceliuice.MacT
ahoe* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/Ma
cTahoe* ~/.local/share/aurorae/themes/MacTahoe*
fish: No matches for wildcard '/usr/share/icons/MacTahoe*'. See `help language#wildcards-globbing`.
sudo rm -rf /usr/share/icons/MacTahoe* /usr/share/themes/MacTahoe* /usr/share/aurorae/themes/MacTahoe* /usr/share/color-
schemes/MacTahoe* /usr/share/plasma/desktoptheme/MacTahoe* /usr/share/plasma/look-and-feel/com.github.vinceliuice.MacTah
oe* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/MacT
ahoe* ~/.local/share/aurorae/themes/MacTahoe*
            ^~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### USER
❯ sudo rm -rf /usr/share/icons/MacTahoe* /usr/share/themes/MacTahoe* /usr/share/aurorae/themes/MacTahoe* /usr/share/colo
r-schemes/MacTahoe* /usr/share/plasma/desktoptheme/MacTahoe* /usr/share/plasma/look-and-feel/com.github.vinceliuice.MacT
ahoe* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/Ma
cTahoe* ~/.local/share/aurorae/themes/MacTahoe*
fish: No matches for wildcard '/usr/share/icons/MacTahoe*'. See `help language#wildcards-globbing`.
sudo rm -rf /usr/share/icons/MacTahoe* /usr/share/themes/MacTahoe* /usr/share/aurorae/themes/MacTahoe* /usr/share/color-
schemes/MacTahoe* /usr/share/plasma/desktoptheme/MacTahoe* /usr/share/plasma/look-and-feel/com.github.vinceliuice.MacTah
oe* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/MacT
ahoe* ~/.local/share/aurorae/themes/MacTahoe*
            ^~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### GEMINI
Ah, the Fish shell—it’s trying to be "helpful" by preventing you from running a command with wildcards (*) that don't match anything. It’s a safety feature that, in this case, is just getting in your way because you're trying to delete things that might or might not exist in every single one of those paths. The Fix: Force the Shell to Comply In Fish, if a wildcard doesn't match, it throws an error instead of passing the literal string to the command. To bypass this and just get the job done, wrap the paths in quotes. Run this: sudo rm -rf "/usr/share/icons/MacTahoe"* "/usr/share/themes/MacTahoe"* "/usr/share/aurorae/themes/MacTahoe"* "/usr/share/color-schemes/MacTahoe"* "/usr/share/plasma/desktoptheme/MacTahoe"* "/usr/share/plasma/look-and-feel/com.github.vinceliuice.MacTahoe"* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe* The "Advisor" Take You’re hitting friction because your shell is smarter than your intent. You’re fighting the tool instead of using it. The Blind Spot: You are trying to delete a list of items where some don't exist. Fish is flagging that you might be making a mistake. You aren't—you're just being lazy with a "spray and pray" command. The Correction: If you want to be high-level, learn your environment. In Fish, you can also set set -g fish_features qmark-noglob or simply use quotes. Precision beats brute force every time. If that command still complains about specific folders not existing, it means they are already gone. Run this to confirm you are finally clean: ls /usr/share/icons | grep -i MacTahoe Did that return nothing? If so, you're done. Now, close the terminal and do the work you’re actually paid/supposed to do.
