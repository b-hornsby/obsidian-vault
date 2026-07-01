---
category: coding
date: 2026-03-15
id: 163609
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because a search query isn't returning the expected results,
  hindering his troubleshooting efforts.
tags:
- troubleshooting
- search-results
- linux-commands
---
# Yeah that doesn’t give me anything like that when I search for it

### USER
Yeah that doesn’t give me anything like that when I search for it

### GEMINI
If LONGNAME isn't showing up, it's because different versions of the os-prober script use slightly different variable names. Don't worry, we'll find the line that handles the label manually. It's usually near the bottom of the file. 1. Open the file again sudo micro /etc/grub.d/30_os-prober 2. Find the Labeling Section Scroll down (usually about 75% of the way down the file) until you see a block of code that looks like this: for OS in ${OSPROBED} ; do DEVICE=`echo ${OS} | cut -d ':' -f 1` LONGNAME=`echo ${OS} | cut -d ':' -f 2 | tr '^' ' '` LABEL=`echo ${OS} | cut -d ':' -f 3 | tr '^' ' '` 3. The "Brute Force" Permanent Fix Since the search failed, we are going to force the name right before the menu is created. Scroll a little further down in that same file until you see this line: menuentry '$(echo "$OS $onstr" | grub_quote)' Immediately above that line, paste this: OS="Tiny11" It should look like this: OS="Tiny11" menuentry '$(echo "$OS $onstr" | grub_quote)' 4. Save and Update Press Ctrl+S to save. Press Ctrl+Q to exit. Run the generator: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this works: By setting OS="Tiny11" right before the menuentry is written, you are intercepting the name-making process. No matter what the script "found" (Windows, Windows Boot Manager, etc.), it is forced to output "Tiny11" into the final Minecraft menu. Did that grub-mkconfig command run successfully this time?
