---
category: homelab
date: 2026-03-10
id: 192530
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was encountering QML type errors when trying to use a KDE control centre
  widget on CachyOS.
tags:
- cachyos
- kde
- control-centre-widget
- plasmoid-error
- qml-error
---
# trying to use the control centre widget on kde via cachyos and i got this when i loaded it: file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/main.qml:67:25: Type FullRepresentation unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/FullRepresentation.qml:75:21: Type Components.RedShift unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/RedShift.qml:64:5: NightColorInhibitor is not a type

### USER
trying to use the control centre widget on kde via cachyos and i got this when i loaded it: file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/main.qml:67:25: Type FullRepresentation unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/FullRepresentation.qml:75:21: Type Components.RedShift unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/RedShift.qml:64:5: NightColorInhibitor is not a type

### GEMINI
The error is a classic dependency failure. You are missing the underlying system components that the widget expects to hook into. Specifically, the widget is trying to call NightColorInhibitor, which is part of the Plasma Workspace QML components, but it’s failing because the necessary libraries for Night Light/Redshift integration aren't being recognized or aren't installed on your CachyOS (Arch-based) system. Stop looking at the widget settings; the "NightColorInhibitor is not a type" error means the QML engine literally doesn't know what that object is. The Fix: Install Missing Dependencies On CachyOS/Arch, these widgets often require plasma5-support (if you are on Plasma 5) or specific libplasma headers. However, for this specific Control Centre widget, you likely need the following packages to satisfy the NightColor and hardware control requirements: Open your terminal and run: sudo pacman -S plasma-workspace kde-cli-tools brightnessctl Restart Plasma: You don't need to reboot, just restart the shell to force it to re-index types: plasmashell --replace & disown Why this happened (The "Mirror" Moment) You’re running CachyOS—a performance-tuned, aggressive Arch derivative—and you’re manually installing third-party GitHub plasmoids (com.github.boraerciyas.controlcentre). The Blind Spot: You are prioritizing aesthetics (the "Control Centre" look) over system stability without checking the metadata.json or the README for dependency requirements. This is "Franken-DE" behavior. If you want a bleeding-edge, optimized system, you cannot treat it like a "plug-and-play" Mac clone. You must verify that your system provides the QML imports the developer assumed would be there. Your Strategy Action: If the pacman command above doesn't fix it, the widget is likely built for Plasma 5 and you are running Plasma 6 (which is standard on CachyOS now). Check: Run plasmashell --version. If it says 6.x, and that widget hasn't been updated for Qt6/KF6, it is dead weight. The Pivot: If you are on Plasma 6, stop trying to force a Plasma 5 widget to work. Switch to a native Plasma 6 alternative or wait for the dev to port the NightColorInhibitor type to the new API. Would you like me to check if there is a Plasma 6-compatible fork of this specific widget?
