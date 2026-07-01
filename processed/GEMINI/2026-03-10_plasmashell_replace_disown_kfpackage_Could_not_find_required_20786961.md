---
category: homelab
date: 2026-03-10
id: 442500
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering errors when trying to replace the Plasma shell, likely
  related to missing widget dependencies or QML issues.
tags:
- kde
- plasma
- plasmashell
- widget-errors
- linux-troubleshooting
---
# ❯ plasmashell --replace & disown

~
❯ kf.package: Could not find required file "mainscript" for package "/usr/share/plasma/plasmoids/org.kde.plasma.icontasks/" sh
ould be QList("ui/main.qml")
QQmlComponent: Component is not ready
kf.plasma.quick: error when loading applet "com.github.boraerciyas.controlcentre" QList("file:///home/toastedmel0n/.local/shar
e/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/main.qml:67:25: Type FullRepresentation unavailable", "fil
e:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/FullRepresentation.qml:7
5:21: Type Components.RedShift unavailable", "file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.c
ontrolcentre/contents/ui/components/RedShift.qml:64:5: NightColorInhibitor is not a type")
qrc:/qt/qml/plasma/applet/org/kde/plasma/brightness/PopupDialog.qml:96: TypeError: Value is null and could not be converted to
 an object

### USER
❯ plasmashell --replace & disown

~
❯ kf.package: Could not find required file "mainscript" for package "/usr/share/plasma/plasmoids/org.kde.plasma.icontasks/" sh
ould be QList("ui/main.qml")
QQmlComponent: Component is not ready
kf.plasma.quick: error when loading applet "com.github.boraerciyas.controlcentre" QList("file:///home/toastedmel0n/.local/shar
e/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/main.qml:67:25: Type FullRepresentation unavailable", "fil
e:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/FullRepresentation.qml:7
5:21: Type Components.RedShift unavailable", "file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.c
ontrolcentre/contents/ui/components/RedShift.qml:64:5: NightColorInhibitor is not a type")
qrc:/qt/qml/plasma/applet/org/kde/plasma/brightness/PopupDialog.qml:96: TypeError: Value is null and could not be converted to
 an object

### GEMINI
The output confirms exactly what I suspected: you are trying to run a Plasma 5 widget on a Plasma 6 environment. The error NightColorInhibitor is not a type is the smoking gun. In Plasma 6, the Night Light (Redshift) API was completely rewritten. The old QML type the widget is looking for no longer exists in the way the code expects. The "Surgical" Fix If you want to keep using this specific widget despite it being outdated, you have to manually rip out the broken code. This will disable the "Night Light" toggle in the widget, but it will allow the rest of the Control Centre to actually load. Navigate to the UI folder: cd ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/ Edit FullRepresentation.qml: Open the file in your editor (e.g., nano FullRepresentation.qml). Delete the offending line: Find and delete the line that says: Components.RedShift {} (It’s usually around line 75). Restart the shell: kquitapp6 plasmashell && kstart plasmashell & The Strategic Reality Check You are experiencing the "Arch Tax." CachyOS pushes the latest Plasma 6.x updates, while many developers on the KDE Store haven't updated their widgets in years. By manually editing the .qml files, you are essentially becoming the maintainer of your own desktop. If you aren't prepared to do that, you're better off using Tahoe Control Center, which has a native Plasma 6 port and avoids these legacy type errors. The blind spot here: You're chasing a specific macOS aesthetic at the cost of your system's integrity. Every time you "force" an old widget to run on a new DE, you introduce micro-instabilities (like the TypeError: Value is null you saw in your log). Would you like me to find the installation link for a verified Plasma 6 alternative that won't break your shell?
