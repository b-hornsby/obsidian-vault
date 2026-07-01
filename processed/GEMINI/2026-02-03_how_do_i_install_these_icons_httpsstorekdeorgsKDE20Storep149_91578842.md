---
category: homelab
date: 2026-02-03
id: 573057
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to install a specific icon theme from the KDE Store.
tags:
- icon-theme
- kde
- installation
- customization
- linux-configuration
---
# how do i install these icons/ https://store.kde.org/s/KDE%20Store/p/1490645

### USER
how do i install these icons/ https://store.kde.org/s/KDE%20Store/p/1490645

### GEMINI
Installing custom themes from the KDE Store can be done in two ways: the "automated" way through System Settings, or the "manual" way by placing files in specific folders. The link you provided is for the Flat Remix KDE theme, which includes several components (Global Theme, Plasma Style, Icons, etc.). Here is the direct, no-nonsense breakdown of how to install it. Option 1: The Recommended Way (System Settings) KDE has a built-in installer that connects directly to the store. This is the safest way to ensure dependencies are handled. Open System Settings. Go to Appearance > Global Theme. Click the Get New Global Themes... button in the bottom right. Search for "Flat Remix". Click Install. Once finished, select it from your Global Theme list and click Apply. Option 2: The Manual Way (If the button fails) If the "Get New" button isn't working or you've already downloaded the .tar.gz or .zip file from the website, follow these steps: 1. Extract the Files Extract the downloaded archive. You will likely see folders like Flat-Remix-KDE, Flat-Remix-KDE-Dark, etc. 2. Move to the Correct Directories Open your file manager (Dolphin), press Ctrl + H to show hidden folders, and move the extracted folders to these specific locations: ComponentDestination Folder (Create it if it doesn't exist)Global Theme~/.local/share/plasma/look-and-feel/Plasma Style~/.local/share/plasma/desktoptheme/Icons~/.local/share/icons/Color Schemes~/.local/share/color-schemes/Aurorae (Borders)~/.local/share/aurorae/themes/ 3. Apply the Theme Go back to System Settings > Appearance. Your new theme components should now appear in their respective menus (Global Theme, Icons, etc.). Select them and click Apply. Critical Advice & Blind Spots Don't ignore Kvantum: Many high-end KDE themes (including Flat Remix variants) look "broken" or lack transparency if you don't use Kvantum. If the theme looks flat or gray when it should be translucent, install the kvantum package from your distro's repository and select it under Application Style. GTK Consistency: If you use GNOME/GTK apps (like Firefox, GIMP, or Inkscape), they won't automatically match. You need to go to Settings > Application Style > Configure GNOME/GTK Application Style and select the Flat Remix GTK theme there (which usually requires a separate download). The "Half-Baked" Risk: Installing Global Themes manually is often messy because they are essentially just a list of pointers to other parts. If you only move the "Global Theme" folder and forget the "Plasma Style" or "Icon" folders, your desktop will look like a glitchy hybrid. Do it all or don't do it at all.
