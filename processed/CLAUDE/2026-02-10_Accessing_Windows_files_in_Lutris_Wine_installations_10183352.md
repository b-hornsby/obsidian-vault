---
category: homelab
date: 2026-02-10
id: 727209
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: CLAUDE
summary: Bryan wanted to know how to access the Windows-side files of a Wine installation
  for games managed through Lutris.
tags:
- lutris
- wine
- windows-files
- linux-gaming
- cachyos
---
# Accessing Windows files in Lutris Wine installations

### HUMAN
how to see windows side of wine installation for games via lutris

### ASSISTANT
I'll help you access the Windows-side files of a Wine prefix created by Lutris for your games.

When Lutris installs a game using Wine, it creates a Wine prefix (a virtual Windows environment) in a specific location. Here's how to navigate to it:

## Finding the Wine Prefix

1. **Open Lutris** and right-click on the game you want to examine
2. Select **"Configure"** from the menu
3. Go to the **"System options"** tab
4. Look for the **"Wine prefix"** field - this shows the path to your Wine installation

The default location is usually:
```
~/.local/share/lutris/runners/wine/
```

Or for specific games:
```
~/Games/[game-name]/
```

## Browsing the Windows Files

Once you have the prefix path, you can browse it in several ways:

**Via File Manager:**
- Open your file manager and navigate to the prefix path
- The Windows C: drive is in the `drive_c` folder
- Program Files will be at `drive_c/Program Files` or `drive_c/Program Files (x86)`

**Via Terminal:**
```bash
cd ~/.local/share/lutris/runners/wine/[prefix-name]/drive_c
```

**Using Lutris's Built-in File Browser:**
- Right-click the game in Lutris
- Select **"Browse files"** - this opens the game's installation directory directly

## Using Wine File Manager

You can also launch Wine's file explorer to see files as they appear in the Windows environment:

```bash
WINEPREFIX=~/.local/share/lutris/runners/wine/[prefix-name] wine winefile
```

Or use `winetricks` to open the file browser through Lutris's Wine configuration.

Does this help you find what you're looking for?
