---
category: general
date: 2026-02-05
id: 585084
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is describing when a warning message appears, specifically when clicking
  on an application.
tags:
- application-error
- software-execution
- warning-message
---
# its when i click the application that it gives that warning

### USER
its when i click the application that it gives that warning

### GEMINI
The reason you’re still getting that warning when you click the icon is that the shadps4-bin (or -git) package installs two things: the emulator engine (shadps4) and the GUI launcher (shadps4-qt). Right now, your desktop shortcut is pointing to the "engine" instead of the "launcher." It’s like trying to start a car by grabbing the spark plug instead of turning the key. The Fix Since you use paru, you likely have the launcher already, but it’s not what the icon is linked to. You need to install the dedicated launcher package to get the correct "clickable" entry: Install the official launcher: paru -S shadps4-qtlauncher-bin Open your application menu (press the Super/Windows key). Search for "shadPS4 Launcher" (it might have a slightly different name/icon than the one you clicked before). Why the other icon is broken The shadps4 package provides a .desktop file that executes the command shadps4. In recent versions, the developers decided that shadps4 should only be a Command Line Interface (CLI) tool. When you click that icon, the tool sees it has no instructions (no game file attached) and gives you that "Please use the QTlauncher" warning. Strategic Move: Clean up the confusion To stop yourself from clicking the wrong icon in the future, you should prioritize the launcher. If you want to be surgical about it, you can manually edit the broken shortcut: Run sudo nano /usr/share/applications/shadps4.desktop (or whichever .desktop file is causing the popup). Find the line starting with Exec=. Change it to Exec=shadps4-qt. Save and exit. The Reality: You’re dealing with an emulator that is moving so fast the packagers can barely keep the icons straight. Don't expect "out of the box" perfection on Arch for a project this experimental. Next Step: Once you get the GUI open, do you have your firmware and keys ready, or are you expecting the emulator to provide those for you? (Hint: It won't.)
