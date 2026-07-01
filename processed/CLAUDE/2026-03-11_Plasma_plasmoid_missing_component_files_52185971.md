---
category: homelab
date: 2026-03-11
id: 617217
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: CLAUDE
summary: Bryan was troubleshooting a KDE Plasma plasmoid (controlcentre) that was
  failing to load due to missing QML component files.
tags:
- kde-plasma
- plasmoid
- qml
- controlcentre
- cachyos
- missing-files
---
# Plasma plasmoid missing component files

### HUMAN
file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/main.qml:67:25: Type FullRepresentation unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/FullRepresentation.qml:17:5: Type Components.ControlCentre unavailable

file:///home/toastedmel0n/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/ControlCentre.qml: No such file or directory

### ASSISTANT
This error means the plasmoid is missing a required file: `ControlCentre.qml` in the components directory.

Here are the steps to fix it:

**1. Check what's actually in the components directory:**
```bash
ls ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/
```

**2. Most likely causes & fixes:**

**Incomplete installation** — The most common cause. Try reinstalling:
```bash
# Remove the broken install
rm -rf ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre

# Reinstall from KDE Store via command line
kpackagetool6 --install /path/to/downloaded.plasmoid
# or
plasmapkg2 --install /path/to/downloaded.plasmoid
```

**If you installed from GitHub**, make sure you cloned/downloaded the full repo and not just a partial zip:
```bash
git clone https://github.com/boraerciyas/controlcentre
cd controlcentre
kpackagetool6 --install .
```

**3. Verify the file exists after reinstall:**
```bash
ls ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/
# Should show ControlCentre.qml among others
```

**4. Restart Plasma after fixing:**
```bash
plasmashell --replace &
```

If wget fails, go to `https://github.com/boraerciyas/controlcentre` in your browser, navigate to the components folder, find `ControlCentre.qml`, and manually save it to:
```
~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/
```

The file is simply missing from whatever archive you installed — this is a packaging bug on the plasmoid's end.

### HUMAN
its actually this one

### ASSISTANT
The widget is actually a **fork** from `https://github.com/Prayag2/kde_controlcentre` — so the GitHub URL I gave you earlier was wrong. Try:

```bash
wget https://raw.githubusercontent.com/Prayag2/kde_controlcentre/main/package/contents/ui/components/ControlCentre.qml \
  -O ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/ControlCentre.qml
```

Or try the `boraerciyas` fork directly (since that's what's installed):
```bash
wget https://raw.githubusercontent.com/boraerciyas/controlcentre/main/package/contents/ui/components/ControlCentre.qml \
  -O ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/ControlCentre.qml
```

If neither works, visit the homepage link from the widget page — **"Open the homepage for Control Centre 6"** — which should take you directly to the correct repo, then browse to `package/contents/ui/components/` and grab `ControlCentre.qml` manually.

After dropping the file in place:
```bash
plasmashell --replace &
```

### HUMAN
its not there

### ASSISTANT
`ControlCentre.qml` doesn't exist in this fork's repo at all — it's a genuine bug where the author forgot to include the file. The repo is also 13 commits behind the upstream (`Prayag2/kde_controlcentre`), so check if it exists there:

```bash
wget https://raw.githubusercontent.com/Prayag2/kde_controlcentre/main/package/contents/ui/components/ControlCentre.qml \
  -O ~/.local/share/plasma/plasmoids/com.github.boraerciyas.controlcentre/contents/ui/components/ControlCentre.qml
```

If that works, the upstream had the file that the fork dropped. Then just restart Plasma:
```bash
plasmashell --replace &
```

If it still 404s, this widget is simply broken and missing a core file with no fix available. Your options would be:
- **Leave a comment** on the KDE Store page (the reviews section) asking the author to fix it
- **Use the original** `Prayag2/kde_controlcentre` instead, installed directly from its store page at `https://store.kde.org/p/1916655`
- **Try a different** control centre widget entirely