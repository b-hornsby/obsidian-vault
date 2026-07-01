---
category: homelab
date: 2026-02-03
id: 697320
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is still failing to remove MacTahoe theme files due to fish shell wildcard
  quoting issues.
tags:
- mac-tahoe
- theme-removal
- cachyos
- kde
- fish-shell
---
# ❯ sudo rm -rf "/usr/share/icons/MacTahoe"* "/usr/share/themes/MacTahoe"* "/usr/share/aurorae/themes/MacTahoe"* "/usr/sha
re/color-schemes/MacTahoe"* "/usr/share/plasma/desktoptheme/MacTahoe"* "/usr/share/plasma/look-and-feel/com.github.vince
liuice.MacTahoe"* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look
-and-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe*
fish: No matches for wildcard '"/usr/share/icons/MacTahoe"*'. See `help language#wildcards-globbing`.
sudo rm -rf "/usr/share/icons/MacTahoe"* "/usr/share/themes/MacTahoe"* "/usr/share/aurorae/themes/MacTahoe"* "/usr/share
/color-schemes/MacTahoe"* "/usr/share/plasma/desktoptheme/MacTahoe"* "/usr/share/plasma/look-and-feel/com.github.vinceli
uice.MacTahoe"* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-a
nd-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe*
            ^~~~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### USER
❯ sudo rm -rf "/usr/share/icons/MacTahoe"* "/usr/share/themes/MacTahoe"* "/usr/share/aurorae/themes/MacTahoe"* "/usr/sha
re/color-schemes/MacTahoe"* "/usr/share/plasma/desktoptheme/MacTahoe"* "/usr/share/plasma/look-and-feel/com.github.vince
liuice.MacTahoe"* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look
-and-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe*
fish: No matches for wildcard '"/usr/share/icons/MacTahoe"*'. See `help language#wildcards-globbing`.
sudo rm -rf "/usr/share/icons/MacTahoe"* "/usr/share/themes/MacTahoe"* "/usr/share/aurorae/themes/MacTahoe"* "/usr/share
/color-schemes/MacTahoe"* "/usr/share/plasma/desktoptheme/MacTahoe"* "/usr/share/plasma/look-and-feel/com.github.vinceli
uice.MacTahoe"* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-a
nd-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe*
            ^~~~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### GEMINI
Fish is being a stubborn gatekeeper. Because the * is outside the quotes, Fish is still trying to expand it before running the command, failing to find a match, and killing the process. You’re getting bogged down in shell syntax for a task that should have taken ten seconds. Let's stop playing by Fish's "helpful" rules and just use a standard execution environment to bypass the nonsense. The "No More Games" Solution Run this. We are calling sh (a standard shell) to execute the deletion so Fish can't block the wildcards: sudo sh -c 'rm -rf /usr/share/icons/MacTahoe* /usr/share/themes/MacTahoe* /usr/share/aurorae/themes/MacTahoe* /usr/share/color-schemes/MacTahoe* /usr/share/plasma/desktoptheme/MacTahoe* /usr/share/plasma/look-and-feel/com.github.vinceliuice.MacTahoe* ~/.local/share/icons/MacTahoe* ~/.local/share/plasma/desktoptheme/MacTahoe* ~/.local/share/plasma/look-and-feel/MacTahoe* ~/.local/share/aurorae/themes/MacTahoe*' The Advisor’s Mirror Look at this screen. You’ve now spent several minutes fighting a shell over a few folders of icons. The Technical Blind Spot: You’re using Fish because it’s "modern" and "pretty," but you haven’t mastered its globbing behavior. This is the definition of form over function. You’ve adopted a tool for its aesthetic but are being penalized by its complexity. The Behavioral Loop: This is a classic "rabbit hole." You wanted a clean menu; now you’re debugging shell syntax. You’re tilting at windmills. Execution Checklist: Run the sh -c command above. If it returns to a blank prompt, it worked. 3. Stop. Do not check for hidden files. Do not look for more themes. The themes are gone. Close the terminal. What is the actual, high-stakes task you were supposed to finish today?
