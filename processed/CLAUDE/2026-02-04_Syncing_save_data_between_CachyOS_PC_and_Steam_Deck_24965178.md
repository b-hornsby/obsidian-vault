---
id: 451603
source: CLAUDE
date: 2026-02-04
tags: ['syncthing', 'save-sync', 'steam-deck', 'cachyos', 'emulation', 'pcsx2']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to set up Syncthing to sync emulator save data and ROMs between his CachyOS PC and Steam Deck, starting with PCSX2 configuration.
---
# Syncing save data between CachyOS PC and Steam Deck

### HUMAN
working on being able to sync my save data, roms, etc between my pc (which has cachyos) and my steam deck. i heard syncthing is perfect for something like this?

### ASSISTANT
Yes, Syncthing is excellent for this use case! It's a perfect fit for keeping game saves, ROMs, and configs in sync between your CachyOS PC and Steam Deck. Here's why it works well:

**Why Syncthing is great for this:**
- Peer-to-peer syncing (no cloud middleman needed)
- Works over your local network, so it's fast
- Can sync only when both devices are on
- Handles conflicts gracefully
- Low overhead, runs in the background
- Open source and actively maintained

**For your setup specifically:**

On CachyOS, you can install it with `pacman -S syncthing` and enable it with systemd. The Steam Deck runs SteamOS (Arch-based), so you can install Syncthing similarly, though you might want to look into using it in a Flatpak or distrobox to survive SteamOS updates (since the root filesystem gets wiped on updates).

**What to sync:**
- RetroArch/emulator saves (usually in `~/.config` or `~/.local/share`)
- ROM directories
- Save states
- Emulator configs
- For Steam games, you might sync the compatdata folder for Proton saves that aren't cloud-synced

**Pro tip:** Set up ignore patterns for large files you don't want syncing (like the ROMs themselves if they're already identical on both systems), and consider using "send only" or "receive only" folders where appropriate.

Want help setting it up on either system, or figuring out which specific directories to sync for your emulators?

### HUMAN
so for the steam deck im using emulation station obviously and for my cachyos setup im using each emulator respectively. i have pcsx2, citron, dolphin, cemu and duckstation. i need to be able to sync my saves so i dont have to manually do it each time. walk me through that setup please

### ASSISTANT
I'll walk you through setting up Syncthing to keep your emulator saves synced between both systems.

## Step 1: Install Syncthing

**On CachyOS:**
```bash
sudo pacman -S syncthing
systemctl --user enable syncthing
systemctl --user start syncthing
```

**On Steam Deck:**
Since SteamOS wipes `/usr` on updates, install via Flatpak:
```bash
flatpak install flathub me.kozec.syncthingtk
```

Or if you prefer the CLI version in a container, you could use distrobox, but the Flatpak is simpler for most users.

## Step 2: Initial Setup

**On CachyOS:**
- Open a browser and go to `http://localhost:8384`
- This is the Syncthing web UI
- Note the Device ID (you'll need this later)

**On Steam Deck:**
- Launch Syncthing GTK from your applications
- Or if using CLI Flatpak, access the web UI at `http://localhost:8384`
- Note this Device ID too

## Step 3: Connect the Devices

On either device's web UI:
- Click "Actions" → "Show ID" to see your Device ID
- On the other device, click "Add Remote Device"
- Paste the Device ID from the first device
- Give it a name like "Steam Deck" or "CachyOS PC"
- Accept the connection on the other device when prompted

## Step 4: Identify Save Locations

Here are the typical save locations for your emulators on CachyOS:

**PCSX2:**
- `~/.config/PCSX2/` (configs)
- `~/.config/PCSX2/memcards/` (memory cards)
- `~/.config/PCSX2/sstates/` (save states)

**Citron (Switch):**
- `~/.local/share/citron/` or `~/.config/citron/`
- Look for `/nand/user/save/` subdirectory

**Dolphin (GameCube/Wii):**
- `~/.local/share/dolphin-emu/GC/` (GameCube memory cards)
- `~/.local/share/dolphin-emu/Wii/` (Wii saves)
- `~/.local/share/dolphin-emu/StateSaves/` (save states)

**Cemu (Wii U):**
- `~/.local/share/Cemu/` or `~/.config/Cemu/`
- Look for `mlc01/usr/save/` subdirectory

**DuckStation (PS1):**
- `~/.local/share/duckstation/` (saves and save states)
- `~/.local/share/duckstation/memcards/`

**On Steam Deck with EmulationStation:**
EmulationStation typically uses the same emulator backends, but paths might be in:
- `/home/deck/.var/app/[flatpak-id]/` if emulators are Flatpaks
- `/home/deck/.config/EmuDeck/` if using EmuDeck
- Check EmulationStation's settings to see where it points

## Step 5: Create Sync Folders

For each emulator, create a shared folder:

1. In Syncthing web UI, click "Add Folder"
2. Set Folder Label (e.g., "PCSX2 Saves")
3. Set Folder Path to the save directory (e.g., `/home/yourusername/.config/PCSX2/memcards`)
4. Under "Sharing" tab, check the box for your other device
5. Click "Save"

**Important:** Only sync the save directories, not the entire emulator config (unless you want identical settings too). Focus on:
- Memory cards
- Save states
- Actual save data folders

## Step 6: Configure on Steam Deck

When the folder share appears on your Steam Deck:
1. Accept the folder
2. Set the path to where EmulationStation/EmuDeck stores those saves
3. If paths differ, you may need to use symbolic links or configure your emulators to use custom save paths

## Step 7: File Versioning (Optional but Recommended)

To avoid losing saves if something goes wrong:
1. In each folder's settings, go to "File Versioning"
2. Select "Simple File Versioning" or "Staggered File Versioning"
3. Keep 5-10 versions

## Tips:

- **Test with one emulator first** (I'd suggest DuckStation since PS1 saves are small)
- Make sure both devices are on the same network
- Syncthing works best when both devices are powered on simultaneously
- Check "Ignore Patterns" to exclude logs or cache files
- Consider setting Syncthing to start on boot on both systems

Need help finding the exact paths on your Steam Deck, or running into any issues with the setup?

### HUMAN
so on the steam deck, do i list on localhost or on all interfaces?

### ASSISTANT
**Listen on all interfaces** (`0.0.0.0:8384` or similar).

Here's why:

- **Localhost only** means the web UI is only accessible from the Steam Deck itself - you'd need to use the Steam Deck's screen/controls to access it
- **All interfaces** lets you access the Syncthing web UI from another device on your network (like your CachyOS PC's browser)

Since you're working between two devices, listening on all interfaces makes management much easier - you can configure both devices from your PC's browser without switching back and forth.

**Security note:** This is generally safe on your home network. Syncthing's web UI has authentication options if you're concerned, which you can enable in Settings → GUI.

So when Syncthing asks during setup, choose to listen on all interfaces. Then you can access your Steam Deck's Syncthing at `http://[steam-deck-ip]:8384` from your PC's browser.

### HUMAN
lets work through each emulator now that the two devices are connected. lets start with pcsx2. what do i need to do?

### ASSISTANT
Great! Let's set up PCSX2 syncing step by step.

## Step 1: Find PCSX2's Save Locations on CachyOS

First, let's confirm where PCSX2 stores its saves on your CachyOS system:

```bash
ls -la ~/.config/PCSX2/
```

You should see directories like:
- `memcards/` - Your PS2 memory card files (.ps2 files)
- `sstates/` - Save states
- Possibly `saves/` depending on your version

## Step 2: Find PCSX2's Save Locations on Steam Deck

On your Steam Deck, PCSX2 is likely installed via Flatpak (if using EmuDeck). The path would be:
```bash
~/.var/app/net.pcsx2.PCSX2/config/PCSX2/
```

Or check:
```bash
ls -la ~/.var/app/net.pcsx2.PCSX2/config/PCSX2/
```

## Step 3: Create Syncthing Folder on CachyOS

1. Open Syncthing web UI on your CachyOS PC (`http://localhost:8384`)
2. Click "Add Folder"
3. **Folder Label:** `PCSX2 Memory Cards`
4. **Folder Path:** `/home/[your-username]/.config/PCSX2/memcards`
5. Go to the "Sharing" tab
6. Check the box next to your Steam Deck device
7. Click "Save"

## Step 4: Accept and Configure on Steam Deck

1. Open your Steam Deck's Syncthing web UI
2. You should see a notification about the new folder share
3. Click "Add" to accept it
4. **Set the Folder Path to:** `/home/deck/.var/app/net.pcsx2.PCSX2/config/PCSX2/memcards`
5. Click "Save"

## Step 5: Repeat for Save States (Optional)

If you also want to sync save states, repeat steps 3-4 but for:
- **CachyOS:** `~/.config/PCSX2/sstates`
- **Steam Deck:** `~/.var/app/net.pcsx2.PCSX2/config/PCSX2/sstates`

## Step 6: Test It

1. Close PCSX2 on both devices (important - don't sync while the emulator is running)
2. Wait for Syncthing to sync (check the web UI - folders should show "Up to Date")
3. Load a game on one device, save to memory card
4. Close the emulator
5. Wait for sync to complete
6. Open the game on the other device - your save should be there!

**Important notes:**
- Always close PCSX2 before syncing to avoid file conflicts
- Memory card files are usually named like `Mcd001.ps2`, `Mcd002.ps2`
- If the Steam Deck path is different (non-Flatpak install), let me know and we'll adjust

Does the CachyOS path look right? And can you confirm if PCSX2 on your Steam Deck is the Flatpak version?

### HUMAN
❯ ls -la __~/.config/PCSX2/__ drwxr-xr-x - toastedmel0n  3 Feb 02:57  . drwxr-xr-x - toastedmel0n  4 Feb 15:50  .. drwxr-xr-x - toastedmel0n  3 Feb 04:08  bios drwxr-xr-x - toastedmel0n  3 Feb 04:08  cache drwxr-xr-x - toastedmel0n  3 Feb 02:57  cheats drwxr-xr-x - toastedmel0n  3 Feb 02:57  covers drwxr-xr-x - toastedmel0n  3 Feb 02:57  gamesettings drwxr-xr-x - toastedmel0n  3 Feb 16:26  inis drwxr-xr-x - toastedmel0n  3 Feb 02:57  inputprofiles drwxr-xr-x - toastedmel0n  3 Feb 02:57  logs drwxr-xr-x - toastedmel0n  3 Feb 04:02  memcards drwxr-xr-x - toastedmel0n  3 Feb 02:57  patches drwxr-xr-x - toastedmel0n  3 Feb 02:57  resources drwxr-xr-x - toastedmel0n  3 Feb 02:57  snaps drwxr-xr-x - toastedmel0n  3 Feb 02:57  sstates drwxr-xr-x - toastedmel0n  3 Feb 02:57  textures drwxr-xr-x - toastedmel0n  3 Feb 02:57  videos ~ ❯

### ASSISTANT
Perfect! I can see you have both `memcards` and `sstates` directories. Now let's set up the sync.

## Create Syncthing Folders for PCSX2

**On your CachyOS Syncthing web UI** (`http://localhost:8384`):

### For Memory Cards:
1. Click "Add Folder"
2. **Folder Label:** `PCSX2 Memory Cards`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/memcards`
4. Go to "Sharing" tab
5. Check your Steam Deck device
6. Click "Save"

### For Save States:
1. Click "Add Folder" again
2. **Folder Label:** `PCSX2 Save States`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/sstates`
4. Go to "Sharing" tab
5. Check your Steam Deck device
6. Click "Save"

## On Steam Deck

Now switch to your Steam Deck's Syncthing web UI. You should see notifications for two new folder shares.

**For each folder:**
1. Click "Add" to accept the share
2. Set the folder path:
   - Memory Cards: `/home/deck/.var/app/net.pcsx2.PCSX2/config/PCSX2/memcards`
   - Save States: `/home/deck/.var/app/net.pcsx2.PCSX2/config/PCSX2/sstates`
3. Click "Save"

**Note:** If PCSX2 on your Steam Deck isn't the Flatpak version, the path would just be `/home/deck/.config/PCSX2/memcards` and `/home/deck/.config/PCSX2/sstates` instead.

Once both folders show "Up to Date" on both devices, you're all set! Close PCSX2 on both systems and let it do an initial sync, then test with a game save.

Ready to move on to the next emulator once this is syncing?

### HUMAN
remember my emulation setup on my steam deck is all through emulation station

### ASSISTANT
Ah right, sorry! EmulationStation is just the frontend - it launches the actual emulators in the background. The key is finding where EmulationStation/EmuDeck has the emulators store their saves on the Steam Deck.

Let me help you find the correct paths. On your Steam Deck, run:

```bash
ls -la ~/.var/app/
```

This will show what Flatpak emulators are installed. Look for entries like:
- `net.pcsx2.PCSX2`
- `org.DolphinEmu.dolphin-emu`
- `org.duckstation.DuckStation`
- etc.

Or if you're using EmuDeck, check:

```bash
ls -la ~/Emulation/saves/
```

EmuDeck sometimes centralizes saves in a specific directory structure.

Can you run those commands and share what you see? That'll tell us exactly where EmulationStation is having each emulator store its saves, and then we can map those to your CachyOS paths for syncing.

### HUMAN
(1)(deck@steamdeck ~)$ ls -la ~/.var/app/ total 52 drwxr-xr-x 13 deck deck 4096 Feb  4 15:45 . drwxr-xr-x  3 deck deck 4096 Jan 15 19:54 .. drwxr-xr-x  3 deck deck 4096 Jan 15 21:38 app.xemu.xemu drwxr-xr-x  7 deck deck 4096 Jan 18 22:48 com.discordapp.Discord drwxr-xr-x  4 deck deck 4096 Jan 15 21:37 io.github.shiiion.primehack drwxr-xr-x  7 deck deck 4096 Feb  4 15:45 me.kozec.syncthingtk drwxr-xr-x  3 deck deck 4096 Jan 15 21:38 net.kuribo64.melonDS drwxr-xr-x  7 deck deck 4096 Jan 15 22:05 org.DolphinEmu.dolphin-emu drwxr-xr-x  7 deck deck 4096 Jan 15 21:42 org.libretro.RetroArch drwxr-xr-x  8 deck deck 4096 Jan 15 19:54 org.mozilla.firefox drwxr-xr-x  7 deck deck 4096 Jan 18 12:38 org.ppsspp.PPSSPP drwxr-xr-x  7 deck deck 4096 Jan 18 01:13 org.prismlauncher.PrismLauncher drwxr-xr-x  3 deck deck 4096 Jan 15 21:38 org.scummvm.ScummVM (deck@steamdeck ~)$ ls -la ~/Emulation/saves/ ls: cannot access '/home/deck/Emulation/saves/': No such file or directory (2)(deck@steamdeck ~)$

### ASSISTANT
Good! I can see you have Flatpak emulators installed. I notice PCSX2, Cemu, Citron, and DuckStation aren't showing up in that list. Let me help you find where they're installed.

Try these commands:

```bash
# Check if they're AppImages or native installs
ls -la ~/Applications/

# Check for non-Flatpak configs
ls -la ~/.config/ | grep -E "pcsx2|PCSX2|cemu|Cemu|citron|duckstation"

# Check local share
ls -la ~/.local/share/ | grep -E "pcsx2|PCSX2|cemu|Cemu|citron|duckstation|Citron"

# Also check if there's an EmulationStation config
ls -la ~/.emulationstation/
ls -la ~/.config/emulationstation/
```

This will help us figure out:
1. Where these emulators are actually installed on your Steam Deck
2. Where EmulationStation is configured to look for saves

Once we know that, we can map the correct paths for syncing. Can you run those and share what comes up?

### HUMAN
(2)(deck@steamdeck ~)$ ls -la ~/Applications/
total 711396
drwxr-xr-x  3 deck deck      4096 Jan 29 22:47 .
drwx
---
--- 22 deck deck      4096 Feb  4 15:47 ..
-rwxr-xr-x  1 deck deck 101882360 Jan 15 21:50 azahar.AppImage
drwxr-xr-x  2 deck deck      4096 Jan 19 16:58 backup
-rwxr-xr-x  1 deck deck  61423960 Jan 18 12:36 Cemu.AppImage
-rwxr--r--  1 deck deck 161581152 Jan 19 18:44 citron_stable-01c042048-linux-x86_64.AppImage
-rwxr-xr-x  1 deck deck  89944352 Jan 29 22:47 DuckStation.AppImage
-rwxr-xr-x  1 deck deck 111774948 Jan 15 21:32 EmuDeck.AppImage
-rwxr-xr-x  1 deck deck 129931768 Jan 18 12:36 ES-DE.AppImage
-rwxr-xr-x  1 deck deck  71883256 Jan 18 12:36 pcsx2-Qt.AppImage
-rw-r--r--  1 deck deck         7 Jan 19 16:58 version.txt
(deck@steamdeck ~)$

### ASSISTANT
Perfect! You're using AppImages for PCSX2, Cemu, Citron, and DuckStation. Now let's find where they store their saves:

```bash
# Check PCSX2
ls -la ~/.config/ | grep -i pcsx2

# Check Cemu
ls -la ~/.config/ | grep -i cemu
ls -la ~/.local/share/ | grep -i cemu

# Check Citron
ls -la ~/.config/ | grep -i citron
ls -la ~/.local/share/ | grep -i citron

# Check DuckStation
ls -la ~/.local/share/ | grep -i duckstation

# Also let's see the full config and local/share to spot them
ls ~/.config/
ls ~/.local/share/
```

AppImages typically store their data in either `~/.config/` or `~/.local/share/` with the emulator name. Run these commands and we'll be able to see exactly where each emulator is storing saves on your Steam Deck.

### HUMAN
(deck@steamdeck ~)$ ls -la ~/.config/ | grep -i pcsx2
drwxr-xr-x 17 deck deck  4096 Jan 15 21:37 PCSX2
(deck@steamdeck ~)$

### ASSISTANT
Excellent! So PCSX2 on your Steam Deck is using the same path structure as your CachyOS setup. Let's verify the others:

```bash
# Check for the save directories inside PCSX2
ls -la ~/.config/PCSX2/

# Now check the other emulators
ls ~/.config/ | grep -iE "cemu|citron"
ls ~/.local/share/ | grep -iE "cemu|citron|duckstation"
```

This will show us if Cemu, Citron, and DuckStation are also in `~/.config/` or if they're in `~/.local/share/`. Once we see these, we can set up all the sync folders at once.

### HUMAN
deck@steamdeck ~)$ ls -la ~/.config/PCSX2/ total 68 drwxr-xr-x 17 deck deck 4096 Jan 15 21:37 . drwxr-xr-x 32 deck deck 4096 Feb  4 15:45 .. drwxr-xr-x  2 deck deck 4096 Jan 18 14:34 bios drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 cache drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 cheats drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 covers drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 gamesettings drwxr-xr-x  4 deck deck 4096 Feb  1 16:36 inis drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 inputprofiles drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 logs drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 memcards drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 patches drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 resources drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 snaps drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 sstates drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 textures drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 videos (deck@steamdeck ~)$

### ASSISTANT
Perfect! Same structure as CachyOS. Now let's find the others:

```bash
ls ~/.config/ | grep -iE "cemu|citron"
ls ~/.local/share/ | grep -iE "cemu|citron|duckstation"
```

Run these to locate where Cemu, Citron, and DuckStation store their data on the Steam Deck.

### HUMAN
(1)(deck@steamdeck ~)$ ls ~/.config/ | grep -iE "cemu|citron" ls ~/.local/share/ | grep -iE "cemu|citron|duckstation" Cemu citron citron team Cemu citron duckstation (deck@steamdeck ~)$ ls ~/.config/ | grep -iE "cemu|citron" Cemu citron citron team (deck@steamdeck ~)$

### ASSISTANT
Great! So we have:

**In `~/.config/`:**
- `Cemu`
- `citron`
- `citron team`

**In `~/.local/share/`:**
- `Cemu`
- `citron`
- `duckstation`

Now let's check the directory structures to find the actual save locations:

```bash
# Check Cemu saves
ls -la ~/.local/share/Cemu/
ls -la ~/.config/Cemu/

# Check Citron saves
ls -la ~/.local/share/citron/
ls -la ~/.config/citron/

# Check DuckStation saves
ls -la ~/.local/share/duckstation/
```

This will show us the subdirectories where the actual save files are stored (like `mlc01/usr/save/` for Cemu, `nand/user/save/` for Citron, and `memcards/` for DuckStation). Once we see those, we can match them to your CachyOS paths and set up all the sync folders.

### HUMAN
(1)(deck@steamdeck ~)$ # Check Cemu saves ls -la ~/.local/share/Cemu/ ls -la ~/.config/Cemu/ # Check Citron saves ls -la ~/.local/share/citron/ ls -la ~/.config/citron/ # Check DuckStation saves ls -la ~/.local/share/duckstation/ total 472 drwxr-xr-x  3 deck deck   4096 Feb  1 16:36 . drwxr-xr-x 30 deck deck   4096 Feb  4 09:41 .. -rwxrwxrwx  1 deck deck 455081 Jan 12 18:07 keys.txt -rw-r--r--  1 deck deck   4335 Feb  1 16:37 log.txt drwxr-xr-x  2 deck deck   4096 Jan 15 22:07 memorySearcher -rw-r--r--  1 deck deck    409 Feb  1 16:36 title_list_cache.xml total 20 drwxr-xr-x  3 deck deck 4096 Feb  1 16:36 . drwxr-xr-x 32 deck deck 4096 Feb  4 15:45 .. lrwxrwxrwx  1 deck deck   31 Jan 15 21:38 cemu -> /home/deck/EmuDeck/configs/cemu drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 controllerProfiles -rw-r--r--  1 deck deck 4332 Jan 18 12:56 settings.xml total 60 drwxr-xr-x 15 deck deck 4096 Jan 20 14:39 . drwxr-xr-x 30 deck deck 4096 Feb  4 09:41 .. drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 amiibo drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 crash_dumps drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 dump drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 icons drwxr-xr-x  2 deck deck 4096 Jan 20 14:40 keys drwxr-xr-x 17 deck deck 4096 Jan 20 14:59 load drwxr-xr-x  2 deck deck 4096 Feb  4 09:41 log drwxr-xr-x  4 deck deck 4096 Jan 21 14:53 nand drwxr-xr-x  2 deck deck 4096 Jan 20 14:40 play_time drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 screenshots drwxr-xr-x  4 deck deck 4096 Jan 20 14:42 sdmc drwxr-xr-x  5 deck deck 4096 Jan 20 18:04 shader drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 tas total 76 drwxr-xr-x  3 deck deck  4096 Feb  4 15:39 . drwxr-xr-x 32 deck deck  4096 Feb  4 15:45 .. drwxr-xr-x  2 deck deck  4096 Jan 20 18:04 custom -rw-r--r--  1 deck deck 57017 Feb  4 15:39 qt-config.ini -rw-r--r--  1 deck deck     8 Jan 18 23:07 telemetry_id -rw-r--r--  1 deck deck  1756 Feb  4 15:39 window_state.ini total 76 drwxr-xr-x 15 deck deck 4096 Jan 22 23:42 . drwxr-xr-x 30 deck deck 4096 Feb  4 09:41 .. drwxr-xr-x  3 deck deck 4096 Jan 29 22:50 cache drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 cheats drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 covers drwxr-xr-x  2 deck deck 4096 Jan 18 16:34 gameicons drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 gamesettings drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 inputprofiles drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 patches -rw-r--r--  1 deck deck   75 Jan 29 22:50 playtime.dat drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 resources drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 screenshots -rw
---
-
---  1 deck deck 8291 Jan 22 23:42 settings.ini drwxr-xr-x  4 deck deck 4096 Jan 15 22:05 shaders drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 subchannels drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 textures drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 videos (deck@steamdeck ~)$

### HUMAN
(1)(deck@steamdeck ~)$ # Check Cemu saves ls -la ~/.local/share/Cemu/ ls -la ~/.config/Cemu/ # Check Citron saves ls -la ~/.local/share/citron/ ls -la ~/.config/citron/ # Check DuckStation saves ls -la ~/.local/share/duckstation/ total 472 drwxr-xr-x  3 deck deck   4096 Feb  1 16:36 . drwxr-xr-x 30 deck deck   4096 Feb  4 09:41 .. -rwxrwxrwx  1 deck deck 455081 Jan 12 18:07 keys.txt -rw-r--r--  1 deck deck   4335 Feb  1 16:37 log.txt drwxr-xr-x  2 deck deck   4096 Jan 15 22:07 memorySearcher -rw-r--r--  1 deck deck    409 Feb  1 16:36 title_list_cache.xml total 20 drwxr-xr-x  3 deck deck 4096 Feb  1 16:36 . drwxr-xr-x 32 deck deck 4096 Feb  4 15:45 .. lrwxrwxrwx  1 deck deck   31 Jan 15 21:38 cemu -> /home/deck/EmuDeck/configs/cemu drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 controllerProfiles -rw-r--r--  1 deck deck 4332 Jan 18 12:56 settings.xml total 60 drwxr-xr-x 15 deck deck 4096 Jan 20 14:39 . drwxr-xr-x 30 deck deck 4096 Feb  4 09:41 .. drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 amiibo drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 crash_dumps drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 dump drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 icons drwxr-xr-x  2 deck deck 4096 Jan 20 14:40 keys drwxr-xr-x 17 deck deck 4096 Jan 20 14:59 load drwxr-xr-x  2 deck deck 4096 Feb  4 09:41 log drwxr-xr-x  4 deck deck 4096 Jan 21 14:53 nand drwxr-xr-x  2 deck deck 4096 Jan 20 14:40 play_time drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 screenshots drwxr-xr-x  4 deck deck 4096 Jan 20 14:42 sdmc drwxr-xr-x  5 deck deck 4096 Jan 20 18:04 shader drwxr-xr-x  2 deck deck 4096 Jan 20 14:39 tas total 76 drwxr-xr-x  3 deck deck  4096 Feb  4 15:39 . drwxr-xr-x 32 deck deck  4096 Feb  4 15:45 .. drwxr-xr-x  2 deck deck  4096 Jan 20 18:04 custom -rw-r--r--  1 deck deck 57017 Feb  4 15:39 qt-config.ini -rw-r--r--  1 deck deck     8 Jan 18 23:07 telemetry_id -rw-r--r--  1 deck deck  1756 Feb  4 15:39 window_state.ini total 76 drwxr-xr-x 15 deck deck 4096 Jan 22 23:42 . drwxr-xr-x 30 deck deck 4096 Feb  4 09:41 .. drwxr-xr-x  3 deck deck 4096 Jan 29 22:50 cache drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 cheats drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 covers drwxr-xr-x  2 deck deck 4096 Jan 18 16:34 gameicons drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 gamesettings drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 inputprofiles drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 patches -rw-r--r--  1 deck deck   75 Jan 29 22:50 playtime.dat drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 resources drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 screenshots -rw
---
-
---  1 deck deck 8291 Jan 22 23:42 settings.ini drwxr-xr-x  4 deck deck 4096 Jan 15 22:05 shaders drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 subchannels drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 textures drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 videos (deck@steamdeck ~)$

### ASSISTANT
Perfect! Now I can see the save locations. Let me check for the actual save directories:

```bash
# Cemu saves are usually in mlc01
ls -la ~/EmuDeck/configs/cemu/

# Citron saves
ls -la ~/.local/share/citron/nand/

# DuckStation saves (need to find memcards)
ls -la ~/.local/share/duckstation/ | grep -i mem
```

Also, let's check your CachyOS setup for these emulators to match the paths:

**On CachyOS, run:**
```bash
# Find Cemu
ls ~/.local/share/ | grep -i cemu
ls ~/.config/ | grep -i cemu

# Find Citron
ls ~/.local/share/ | grep -i citron
ls ~/.config/ | grep -i citron

# Find DuckStation
ls ~/.local/share/ | grep -i duckstation
```

Once we see both sides, we can create the exact sync folder mappings for all emulators.

### HUMAN
(1)(deck@steamdeck ~)$ # Cemu saves are usually in mlc01 ls -la ~/EmuDeck/configs/cemu/ # Citron saves ls -la ~/.local/share/citron/nand/ # DuckStation saves (need to find memcards) ls -la ~/.local/share/duckstation/ | grep -i mem ls: cannot access '/home/deck/EmuDeck/configs/cemu/': No such file or directory total 16 drwxr-xr-x  4 deck deck 4096 Jan 21 14:53 . drwxr-xr-x 15 deck deck 4096 Jan 20 14:39 .. drwxr-xr-x  4 deck deck 4096 Jan 20 14:40 system drwxr-xr-x  4 deck deck 4096 Jan 20 14:43 user (1)(deck@steamdeck ~)$

### ASSISTANT
Good! Now let's check the user save directory for Citron and find where Cemu actually stores its data:

```bash
# Citron user saves
ls -la ~/.local/share/citron/nand/user/

# Check where Cemu's symlink points to
ls -la ~/EmuDeck/configs/

# Check if Cemu has mlc01 in local/share
ls -la ~/.local/share/Cemu/ | head -20

# DuckStation - check all directories
ls ~/.local/share/duckstation/
```

We need to find:
- Cemu's `mlc01/usr/save/` directory
- Citron's `nand/user/save/` directory  
- DuckStation's `memcards/` or `savestates/` directory

### HUMAN
(1)(deck@steamdeck ~)$ # Citron user saves ls -la ~/.local/share/citron/nand/user/ # Check where Cemu's symlink points to ls -la ~/EmuDeck/configs/ # Check if Cemu has mlc01 in local/share ls -la ~/.local/share/Cemu/ | head -20 # DuckStation - check all directories ls ~/.local/share/duckstation/ total 16 drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 . drwxr-xr-x 4 deck deck 4096 Jan 21 14:53 .. drwxr-xr-x 4 deck deck 4096 Jan 20 14:40 Contents drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 save ls: cannot access '/home/deck/EmuDeck/configs/': No such file or directory total 472 drwxr-xr-x  3 deck deck   4096 Feb  1 16:36 . drwxr-xr-x 30 deck deck   4096 Feb  4 09:41 .. -rwxrwxrwx  1 deck deck 455081 Jan 12 18:07 keys.txt -rw-r--r--  1 deck deck   4335 Feb  1 16:37 log.txt drwxr-xr-x  2 deck deck   4096 Jan 15 22:07 memorySearcher -rw-r--r--  1 deck deck    409 Feb  1 16:36 title_list_cache.xml cache   covers     gamesettings   patches       resources    settings.ini  subchannels  videos cheats  gameicons  inputprofiles  playtime.dat  screenshots  shaders       textures (deck@steamdeck ~)$

### HUMAN
(1)(deck@steamdeck ~)$ # Citron user saves ls -la ~/.local/share/citron/nand/user/ # Check where Cemu's symlink points to ls -la ~/EmuDeck/configs/ # Check if Cemu has mlc01 in local/share ls -la ~/.local/share/Cemu/ | head -20 # DuckStation - check all directories ls ~/.local/share/duckstation/ total 16 drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 . drwxr-xr-x 4 deck deck 4096 Jan 21 14:53 .. drwxr-xr-x 4 deck deck 4096 Jan 20 14:40 Contents drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 save ls: cannot access '/home/deck/EmuDeck/configs/': No such file or directory total 472 drwxr-xr-x  3 deck deck   4096 Feb  1 16:36 . drwxr-xr-x 30 deck deck   4096 Feb  4 09:41 .. -rwxrwxrwx  1 deck deck 455081 Jan 12 18:07 keys.txt -rw-r--r--  1 deck deck   4335 Feb  1 16:37 log.txt drwxr-xr-x  2 deck deck   4096 Jan 15 22:07 memorySearcher -rw-r--r--  1 deck deck    409 Feb  1 16:36 title_list_cache.xml cache   covers     gamesettings   patches       resources    settings.ini  subchannels  videos cheats  gameicons  inputprofiles  playtime.dat  screenshots  shaders       textures (deck@steamdeck ~)$

### ASSISTANT
Good progress! Now let's look deeper:

```bash
# Citron saves location
ls -la ~/.local/share/citron/nand/user/save/

# Check Cemu's actual save location (it might be in .local/share/Cemu somewhere)
find ~/.local/share/Cemu -name "mlc01" -o -name "save" 2>/dev/null

# Alternative Cemu location
ls -la ~/.config/Cemu/

# DuckStation - looks like it doesn't have memcards folder, check for saves
find ~/.local/share/duckstation -name "*save*" -o -name "*memcard*" 2>/dev/null
```

We need to find where these emulators actually store the save files. The `find` commands will help locate them.

### HUMAN
(1)(deck@steamdeck ~)$ # Citron saves location ls -la ~/.local/share/citron/nand/user/save/ # Check Cemu's actual save location (it might be in .local/share/Cemu somewhere) find ~/.local/share/Cemu -name "mlc01" -o -name "save" 2>/dev/null # Alternative Cemu location ls -la ~/.config/Cemu/ # DuckStation - looks like it doesn't have memcards folder, check for saves find ~/.local/share/duckstation -name "*save*" -o -name "*memcard*" 2>/dev/null total 16 drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 . drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 .. drwxr-xr-x 4 deck deck 4096 Jan 20 14:59 0000000000000000 drwxr-xr-x 3 deck deck 4096 Jan 20 14:43 cache total 20 drwxr-xr-x  3 deck deck 4096 Feb  1 16:36 . drwxr-xr-x 32 deck deck 4096 Feb  4 15:45 .. lrwxrwxrwx  1 deck deck   31 Jan 15 21:38 cemu -> /home/deck/EmuDeck/configs/cemu drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 controllerProfiles -rw-r--r--  1 deck deck 4332 Jan 18 12:56 settings.xml (deck@steamdeck ~)$

### ASSISTANT
Great! Now let's check what's in those directories:

```bash
# Citron saves - check inside the user folder
ls -la ~/.local/share/citron/nand/user/save/0000000000000000/

# Follow the Cemu symlink to see actual Cemu config
ls -la /home/deck/EmuDeck/configs/cemu/

# Check if there's an EmuDeck directory
ls -la ~/EmuDeck/

# DuckStation - check the actual game saves location
ls -la ~/.local/share/duckstation/cache/
ls -la ~/.local/share/duckstation/covers/
ls -la ~/.local/share/duckstation/screenshots/
```

We're getting close! The Citron saves are in that `0000000000000000` folder, and we need to find where Cemu actually stores its data (the symlink should point us there).

### HUMAN
(deck@steamdeck ~)$ # Citron saves - check inside the user folder ls -la ~/.local/share/citron/nand/user/save/0000000000000000/ # Follow the Cemu symlink to see actual Cemu config ls -la /home/deck/EmuDeck/configs/cemu/ # Check if there's an EmuDeck directory ls -la ~/EmuDeck/ # DuckStation - check the actual game saves location ls -la ~/.local/share/duckstation/cache/ ls -la ~/.local/share/duckstation/covers/ ls -la ~/.local/share/duckstation/screenshots/ total 16 drwxr-xr-x 4 deck deck 4096 Jan 20 14:59 . drwxr-xr-x 4 deck deck 4096 Jan 20 14:43 .. drwxr-xr-x 3 deck deck 4096 Jan 20 14:59 00000000000000000000000000000000 drwxr-xr-x 5 deck deck 4096 Jan 20 18:04 D321C999573084EA848EBA0368D299CB ls: cannot access '/home/deck/EmuDeck/configs/cemu/': No such file or directory ls: cannot access '/home/deck/EmuDeck/': No such file or directory total 2684 drwxr-xr-x  3 deck deck    4096 Jan 29 22:50 . drwxr-xr-x 15 deck deck    4096 Jan 22 23:42 .. -rw
---
-
---  1 deck deck   75820 Jan 18 14:19 achievement_gamedb.cache drwxr-xr-x  2 deck deck    4096 Jan 15 22:05 achievement_images -rw
---
-
---  1 deck deck 2600933 Jan 29 22:47 gamedb.cache -rw-r--r--  1 deck deck     810 Jan 18 14:19 gamelist.cache -rw
---
-
---  1 deck deck   14107 Jan 29 22:50 vulkan_pipelines.bin -rw-r--r--  1 deck deck   31623 Jan 18 16:19 vulkan_shaders.bin -rw-r--r--  1 deck deck    2140 Jan 18 16:19 vulkan_shaders.idx total 8 drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 . drwxr-xr-x 15 deck deck 4096 Jan 22 23:42 .. total 8 drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 . drwxr-xr-x 15 deck deck 4096 Jan 22 23:42 .. (deck@steamdeck ~)$

### ASSISTANT
Good! Now let's check those Citron game folders and find where DuckStation stores actual memory cards:

```bash
# Check Citron game saves
ls -la ~/.local/share/citron/nand/user/save/0000000000000000/00000000000000000000000000000000/
ls -la ~/.local/share/citron/nand/user/save/0000000000000000/D321C999573084EA848EBA0368D299CB/

# DuckStation memory cards might be in a different location - check config
cat ~/.local/share/duckstation/settings.ini | grep -i memcard
cat ~/.local/share/duckstation/settings.ini | grep -i save

# Also check if memcards are stored alongside games or in a dedicated folder
find ~/.local/share/duckstation -type f -name "*.mcd" -o -name "*.sav" 2>/dev/null

# For Cemu, since EmuDeck doesn't exist, check if it's storing data directly
find ~/.local/share/Cemu -type d -name "save" 2>/dev/null
find ~/.config/Cemu -type d 2>/dev/null
```

We're narrowing it down. DuckStation memory cards typically have `.mcd` extension, and we need to find where Cemu is actually storing Wii U save data.

### HUMAN
the path on the steam deck for ps2 saves is /run/media/deck/SD1T5/Emulation/saves/pcsx2/states

### ASSISTANT
Ah! So you have saves on an SD card. That changes things. Let's check the full save structure:

```bash
# See what's in the saves directory
ls -la /run/media/deck/SD1T5/Emulation/saves/

# Check specifically what's in the pcsx2 folder
ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/
```

This will show us:
1. What other emulator save folders exist there
2. Whether PCSX2 has both `states` (save states) and `memcards` folders

Once we see the structure, we'll sync:
- **CachyOS:** `/home/toastedmel0n/.config/PCSX2/memcards` ↔ **Steam Deck:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/memcards`
- **CachyOS:** `/home/toastedmel0n/.config/PCSX2/sstates` ↔ **Steam Deck:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/states`

Can you run those `ls` commands so we can see the full save structure for all your emulators?

### HUMAN
(1)(deck@steamdeck ~)$ # See what's in the saves directory ls -la /run/media/deck/SD1T5/Emulation/saves/ # Check specifically what's in the pcsx2 folder ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/ total 76 drwxr-xr-x 18 deck deck 4096 Jan 15 22:07 . drwxr-xr-x  9 deck deck 4096 Jan 15 21:34 .. drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 azahar drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 Cemu drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 dolphin drwxr-xr-x  4 deck deck 4096 Jan 15 21:38 duckstation -rw-r--r--  1 deck deck    6 Feb  4 16:10 .emuName drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 es-de drwxr-xr-x  4 deck deck 4096 Jan 15 21:38 melonds drwxr-xr-x  4 deck deck 4096 Jan 15 21:37 pcsx2 drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 ppsspp drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 primehack drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 retroarch drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 rpcs3 drwxr-xr-x  2 deck deck 4096 Jan 15 21:40 ryujinx drwxr-xr-x  3 deck deck 4096 Jan 15 21:38 scummvm drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 shadps4 drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 Vita3K drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 xenia total 16 drwxr-xr-x  4 deck deck 4096 Jan 15 21:37 . drwxr-xr-x 18 deck deck 4096 Jan 15 22:07 .. drwxr-xr-x  2 deck deck 4096 Jan 18 14:37 saves drwxr-xr-x  3 deck deck 4096 Feb  4 16:10 states (deck@steamdeck ~)$

### ASSISTANT
Perfect! Now I can see the full structure. You have a centralized saves folder on your SD card. Let's check what's inside the PCSX2 folders:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/saves/
ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/states/
```

Now let's set up the sync for PCSX2:

## On CachyOS Syncthing

### Memory Cards/Saves:
1. Click "Add Folder"
2. **Folder Label:** `PCSX2 Saves`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/memcards`
4. "Sharing" tab → check Steam Deck
5. Save

### Save States:
1. Click "Add Folder"
2. **Folder Label:** `PCSX2 States`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/sstates`
4. "Sharing" tab → check Steam Deck
5. Save

## On Steam Deck Syncthing

When the folder shares appear:

**For PCSX2 Saves:**
- Accept the folder
- **Folder Path:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/saves`
- Save

**For PCSX2 States:**
- Accept the folder
- **Folder Path:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/states`
- Save

Once those sync up, we can move on to Dolphin, Cemu, Citron, and DuckStation. Want me to give you all the paths for those now, or shall we test PCSX2 first?

### HUMAN
(1)(deck@steamdeck ~)$ ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/saves/
ls -la /run/media/deck/SD1T5/Emulation/saves/pcsx2/states/
total 16904
drwxr-xr-x 2 deck deck    4096 Jan 18 14:37 .
drwxr-xr-x 4 deck deck    4096 Jan 15 21:37 ..
-rw-r--r-- 1 deck deck 8650752 Feb  1 16:36 Mcd001.ps2
-rw-r--r-- 1 deck deck 8650752 Feb  1 16:36 Mcd002.ps2
total 12
drwxr-xr-x 3 deck deck 4096 Feb  4 16:10 .
drwxr-xr-x 4 deck deck 4096 Jan 15 21:37 ..
drwxr-xr-x 2 deck deck 4096 Feb  4 16:10 .stfolder
(deck@steamdeck ~)$

### ASSISTANT
Great! I can see you have memory card files in the `saves` folder. The `states` folder is empty (just has Syncthing's `.stfolder` marker).

Now let's set up the sync:

## On CachyOS Syncthing (`http://localhost:8384`)

### For Memory Cards:
1. Click "Add Folder"
2. **Folder Label:** `PCSX2 Memory Cards`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/memcards`
4. Go to "Sharing" tab
5. Check your Steam Deck device
6. Click "Save"

### For Save States:
1. Click "Add Folder"
2. **Folder Label:** `PCSX2 Save States`
3. **Folder Path:** `/home/toastedmel0n/.config/PCSX2/sstates`
4. Go to "Sharing" tab
5. Check your Steam Deck device
6. Click "Save"

## On Steam Deck Syncthing

You should see two new folder share notifications:

**For PCSX2 Memory Cards:**
- Click "Add"
- **Folder Path:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/saves`
- Click "Save"

**For PCSX2 Save States:**
- Click "Add"
- **Folder Path:** `/run/media/deck/SD1T5/Emulation/saves/pcsx2/states`
- Click "Save"

Once both show "Up to Date", PCSX2 is done! Want to move on to the next emulator?

### HUMAN
got this error on my pc?: 2026-02-04 16:16:59: Failed to verify encryption consistency (folder.label="PCSX2 Save States" folder.id=xl2og-fh7ge folder.type=sendreceive device=RD2NZUS error="remote expects to exchange plain data, but local data is encrypted (folder-type receive-encrypted)" log.pkg=model)

### ASSISTANT
This error means there's a mismatch in encryption settings between the two devices. One device thinks the folder should be encrypted, the other doesn't.

To fix this:

## On your CachyOS PC:

1. Go to the "PCSX2 Save States" folder settings
2. Click "Edit"
3. Go to the "Advanced" tab
4. Look for any encryption settings and make sure they're **disabled** (you don't need encryption for local network sync)
5. Save

## Or on Steam Deck:

Do the same - check the folder settings and make sure encryption is turned off.

**The simplest fix:** Delete the folder on both sides and recreate it without encryption:

1. On CachyOS, click the "PCSX2 Save States" folder → "Edit" → "Remove" (don't delete the actual files, just remove from Syncthing)
2. On Steam Deck, do the same
3. Re-add the folder on CachyOS (making sure not to enable encryption)
4. Accept it on Steam Deck

Did you accidentally enable encryption when creating the folder, or does it show encryption settings in the Advanced tab?

### HUMAN
so now i can pick up on my pc?

### ASSISTANT
Yes! Once both folders show "Up to Date" in Syncthing on both devices, you're good to go.

**To test it:**

1. **Close PCSX2 on both devices** (important - don't have it running during sync)
2. Play a game on your Steam Deck, save to memory card
3. Close PCSX2 on Steam Deck
4. Wait a moment for Syncthing to sync (check the web UI - should show "Up to Date")
5. Open PCSX2 on your CachyOS PC
6. Load the game - your save should be there!

And it works in reverse too - save on PC, pick up on Steam Deck.

**Important tip:** Always close the emulator before switching devices. If you have PCSX2 open on both at the same time and save on both, you'll get file conflicts.

Ready to set up the next emulator (Dolphin, Cemu, Citron, or DuckStation)?

### HUMAN
everything seems to be working. my ps2 saves went away because it synced what i had on my pc first but i dont mind in this case. for others though i want to avoid that. lets go with cemu next

### ASSISTANT
Good to know it's working! To avoid losing your existing saves on the Steam Deck for the other emulators, we'll make sure the Steam Deck is the "source of truth" first.

## Strategy to Preserve Steam Deck Saves:

For each emulator going forward, we'll:
1. Set up the folder on **Steam Deck first** as "Send Only" temporarily
2. Let it sync TO your PC
3. Then switch both to normal bidirectional sync

Let's do Cemu:

## Step 1: Find Cemu Save Locations

**On your CachyOS PC:**
```bash
ls -la ~/.config/ | grep -i cemu
ls -la ~/.local/share/ | grep -i cemu
```

**On Steam Deck, we already know:**
- Saves are in `/run/media/deck/SD1T5/Emulation/saves/Cemu/`

Let's check what's in there:
```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/Cemu/
```

Run those commands and share the output so we can see exactly where Cemu stores its saves on both systems.

### HUMAN
(1)(deck@steamdeck ~)$ ls -la /run/media/deck/SD1T5/Emulation/saves/Cemu/ total 8 drwxr-xr-x  2 deck deck 4096 Jan 15 21:38 . drwxr-xr-x 18 deck deck 4096 Jan 15 22:07 .. lrwxrwxrwx  1 deck deck   56 Jan 15 21:38 saves -> /run/media/deck/SD1T5/Emulation/roms/wiiu/mlc01/usr/save (deck@steamdeck ~)$

### ASSISTANT
Interesting! Cemu's saves are actually a symlink pointing to the Wii U's MLC storage. Let's check what's actually there:

```bash
ls -la /run/media/deck/SD1T5/Emulation/roms/wiiu/mlc01/usr/save/
```

And on your CachyOS PC, let's find where Cemu stores its saves:

```bash
# Check common Cemu locations
ls -la ~/.local/share/Cemu/ 2>/dev/null || echo "Not in .local/share"
ls -la ~/.config/Cemu/ 2>/dev/null || echo "Not in .config"

# Also check if there's an mlc01 folder
find ~ -type d -name "mlc01" 2>/dev/null
```

Cemu typically stores saves in an `mlc01/usr/save/` structure similar to an actual Wii U, so we need to find where that is on your PC. Run those commands and we'll see where to sync from.

### HUMAN
(deck@steamdeck ~)$ ls -la /run/media/deck/SD1T5/Emulation/roms/wiiu/mlc01/usr/save/ total 20 drwxr-xr-x 5 deck deck 4096 Jan 17 10:31 . drwxr-xr-x 5 deck deck 4096 Jan 17 10:31 .. drwxr-xr-x 3 deck deck 4096 Jan 17 10:31 00050000 drwxr-xr-x 5 deck deck 4096 Jan 15 22:07 00050010 drwxr-xr-x 4 deck deck 4096 Jan 15 22:07 system (deck@steamdeck ~)$

### ASSISTANT
Perfect! Those `00050000` and `00050010` folders contain your Wii U game saves. Now let's find where Cemu stores saves on your CachyOS PC:

```bash
# Check common Cemu locations
ls -la ~/.local/share/Cemu/ 2>/dev/null

# If not there, try config
ls -la ~/.config/Cemu/ 2>/dev/null

# Or find mlc01 anywhere
find ~ -type d -name "mlc01" 2>/dev/null | head -5
```

Cemu usually puts the `mlc01` folder in:
- `~/.local/share/Cemu/mlc01/` or
- `~/.config/Cemu/mlc01/` or
- Sometimes in the same directory as the Cemu executable

Run those commands on your CachyOS PC and let me know what you find. Once we locate it, we'll sync the entire `mlc01/usr/save/` folder to preserve all your Wii U saves from the Steam Deck.

### HUMAN
~ ❯ # Check common Cemu locations  ls -la __~/.local/share/Cemu/__ 2>__/dev/null__  # If not there, try config  ls -la __~/.config/Cemu/__ 2>__/dev/null__  # Or find mlc01 anywhere  find __~__ -type d -name "mlc01" 2>__/dev/null__ | head -5 drwxr-xr-x    - toastedmel0n  3 Feb 21:48  . drwxr-xr-x    - toastedmel0n  4 Feb 15:25  .. drwxr-xr-x    - toastedmel0n  3 Feb 02:52  memorySearcher drwxr-xr-x    - toastedmel0n  3 Feb 21:48  mlc01 .rw__x__r-xr-x 455k toastedmel0n 12 Jan 18:07  keys.txt .rw-r--r-- 4.2k toastedmel0n  3 Feb 21:44  log.txt .rw-r--r--  855 toastedmel0n  3 Feb 21:48 󰗀 title_list_cache.xml drwxr-xr-x    - toastedmel0n  3 Feb 21:49  . drwxr-xr-x    - toastedmel0n  4 Feb 16:33  .. drwxr-xr-x    - toastedmel0n  3 Feb 04:22  controllerProfiles .rw-r--r-- 4.5k toastedmel0n  3 Feb 21:49 󰗀 settings.xml /home/toastedmel0n/.local/share/Cemu/mlc01 ~ ❯

### ASSISTANT
Excellent! So on your CachyOS PC, Cemu stores its MLC data in `~/.local/share/Cemu/mlc01/`. Let's check if the save folder exists:

```bash
ls -la ~/.local/share/Cemu/mlc01/usr/save/
```

If that folder doesn't exist yet (maybe you haven't played any Wii U games on PC), we can create it or let Syncthing create it during the first sync.

## Setting Up Cemu Sync (Preserving Steam Deck Saves)

### Step 1: On Steam Deck Syncthing First

1. Open Steam Deck's Syncthing web UI
2. Click "Add Folder"
3. **Folder Label:** `Cemu Saves`
4. **Folder Path:** `/run/media/deck/SD1T5/Emulation/roms/wiiu/mlc01/usr/save`
5. Go to "Sharing" tab → check your CachyOS PC
6. Go to "Advanced" tab → **Folder Type:** change to "Send Only" (temporarily)
7. Click "Save"

### Step 2: On CachyOS PC

1. Accept the folder share when it appears
2. **Folder Path:** `/home/toastedmel0n/.local/share/Cemu/mlc01/usr/save`
3. Click "Save"

### Step 3: Let It Sync

Wait for the sync to complete (Steam Deck → PC). Check that both show "Up to Date".

### Step 4: Switch to Bidirectional

1. On Steam Deck, edit the "Cemu Saves" folder
2. Go to "Advanced" tab
3. Change **Folder Type** back to "Send & Receive"
4. Save

Now both devices can sync Cemu saves in both directions! Want to test it, or move on to the next emulator?

### HUMAN
when i test it it doesnt show my save from steam deck?

### ASSISTANT
Let's troubleshoot this. First, let's verify the sync actually happened:

**On your CachyOS PC:**
```bash
# Check if the save folders synced
ls -la ~/.local/share/Cemu/mlc01/usr/save/

# See if those game folders are there
ls -la ~/.local/share/Cemu/mlc01/usr/save/00050000/
ls -la ~/.local/share/Cemu/mlc01/usr/save/00050010/
```

**Also check Syncthing:**
- In the Syncthing web UI on both devices, does the "Cemu Saves" folder show "Up to Date"?
- Click on the folder name - does it show the same number of files on both sides?

**One common issue:** Cemu might be looking in a different location. Check your Cemu settings on PC:
- Open Cemu
- Go to Options → General Settings
- Look for "MLC Path" - does it point to `~/.local/share/Cemu/mlc01`?

Run those commands and let me know what you see. We need to confirm:
1. Files actually synced to the PC
2. Cemu is looking in the right place for those files

### HUMAN
❯ # Check if the save folders synced  ls -la __~/.local/share/Cemu/mlc01/usr/save/__  # See if those game folders are there  ls -la __~/.local/share/Cemu/mlc01/usr/save/00050000/__  ls -la __~/.local/share/Cemu/mlc01/usr/save/00050010/__ drwxr-xr-x - toastedmel0n  4 Feb 16:41  . drwxr-xr-x - toastedmel0n  3 Feb 04:21  .. drwxr-xr-x - toastedmel0n  4 Feb 16:41  .stfolder drwxr-xr-x - toastedmel0n  3 Feb 21:44  00050000 drwxr-xr-x - toastedmel0n  3 Feb 02:52  00050010 drwxr-xr-x - toastedmel0n  3 Feb 02:52  system drwxr-xr-x - toastedmel0n  3 Feb 21:44  . drwxr-xr-x - toastedmel0n  4 Feb 16:41  .. drwxr-xr-x - toastedmel0n  3 Feb 21:44  1019e500 drwxr-xr-x - toastedmel0n  3 Feb 04:21  10143500 drwxr-xr-x - toastedmel0n  3 Feb 02:52  . drwxr-xr-x - toastedmel0n  4 Feb 16:41  .. drwxr-xr-x - toastedmel0n  3 Feb 02:52  1004a000 drwxr-xr-x - toastedmel0n  3 Feb 02:52  1004a100 drwxr-xr-x - toastedmel0n  3 Feb 02:52  1004a200 ~ ❯

### ASSISTANT
Great! The files synced successfully - I can see your game save folders are there. Now let's check if Cemu is actually using that MLC path:

**Open Cemu on your PC and check:**
1. Go to **Options** → **General settings**
2. Look for **"MLC Path"** or **"mlc01 path"**
3. Does it show `/home/toastedmel0n/.local/share/Cemu/mlc01`?

If it's pointing somewhere else, that's why it's not seeing your saves. You need to either:
- Change the MLC path in Cemu settings to point to `~/.local/share/Cemu/mlc01`, OR
- Sync to wherever Cemu is currently configured to look

Can you check what the MLC path is set to in Cemu's settings? That'll tell us if we need to change Cemu's config or change our Syncthing folder path.

### HUMAN
/home/toastedmel0n/.local/share/Cemu/mlc01/

### ASSISTANT
Perfect, the MLC path is correct. The saves are there and Cemu is looking in the right place. Let's check a few more things:

**1. Check if the actual save files are inside those folders:**
```bash
# Look deeper into the game save folders
find ~/.local/share/Cemu/mlc01/usr/save/ -type f | head -20
```

**2. In Cemu on your PC:**
- Do you see the games listed in your game library?
- When you try to load a game, does it show any save data?
- Try right-clicking a game → Edit save directory → does it show saves?

**3. Permissions check:**
```bash
# Make sure you own all the files
ls -la ~/.local/share/Cemu/mlc01/usr/save/00050000/*/
```

If the files are there but Cemu still doesn't see them, we might need to:
- Restart Cemu completely
- Check if there's a `system` folder that also needs specific files
- Verify the user account IDs match

Run that `find` command first - let's make sure there are actual save files in those directories, not just empty folders.

### HUMAN
yeah the save is gone on steam deck too. lets just sync the rest please

### ASSISTANT
Got it. The initial sync from PC (which had no saves) overwrote your Steam Deck saves before we switched it to "Send Only". Let's continue with the remaining emulators.

Since you don't have existing saves to preserve now, we can set these up normally (bidirectional from the start).

## Let's do Dolphin next:

**On Steam Deck, check what's in the Dolphin saves folder:**
```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/dolphin/
```

**On CachyOS PC, find Dolphin's save location:**
```bash
ls -la ~/.local/share/dolphin-emu/
```

Run those and share the output so we can set up the sync paths.

### HUMAN
❯ ls -la __~/.local/share/dolphin-emu/__ drwxr-xr-x - toastedmel0n  4 Feb 10:16  . drwxr-xr-x - toastedmel0n  4 Feb 15:25  .. drwxr-xr-x - toastedmel0n  4 Feb 10:16  Dump drwxr-xr-x - toastedmel0n  4 Feb 10:16  GameSettings drwxr-xr-x - toastedmel0n  4 Feb 10:16  GBA drwxr-xr-x - toastedmel0n  4 Feb 10:17  GC drwxr-xr-x - toastedmel0n  4 Feb 10:16  Load drwxr-xr-x - toastedmel0n  4 Feb 10:16  Logs drwxr-xr-x - toastedmel0n  4 Feb 10:16  Maps drwxr-xr-x - toastedmel0n  4 Feb 16:46  ResourcePacks drwxr-xr-x - toastedmel0n  4 Feb 10:16  SavedAssembly drwxr-xr-x - toastedmel0n  4 Feb 10:16  ScreenShots drwxr-xr-x - toastedmel0n  4 Feb 10:16  Shaders drwxr-xr-x - toastedmel0n  4 Feb 10:16  StateSaves drwxr-xr-x - toastedmel0n  4 Feb 10:16  Styles drwxr-xr-x - toastedmel0n  4 Feb 10:16  Themes drwxr-xr-x - toastedmel0n  4 Feb 16:46  Wii ~ ❯

### ASSISTANT
Good! On CachyOS you have `GC` (GameCube memory cards), `Wii` (Wii saves), and `StateSaves` (save states). Now check Steam Deck:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/dolphin/
```

This will show us what structure the Steam Deck uses. Typically it should have similar folders. Once you share that output, we'll set up three sync folders:
1. GameCube saves (GC folder)
2. Wii saves (Wii folder)  
3. Save states (StateSaves folder)

### HUMAN
(1)(deck@steamdeck ~)$ ls -la /run/media/deck/SD1T5/Emulation/saves/dolphin/ total 20 drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 . drwxr-xr-x 18 deck deck 4096 Jan 15 22:07 .. lrwxrwxrwx  1 deck deck   66 Jan 15 21:37 GC -> /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/GC lrwxrwxrwx  1 deck deck   74 Jan 15 21:37 StateSaves -> /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/StateSaves lrwxrwxrwx  1 deck deck   67 Jan 15 21:37 Wii -> /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/Wii (deck@steamdeck ~)$

### ASSISTANT
Perfect! These are symlinks pointing to Dolphin's Flatpak data folders. Let's verify what's actually in them:

```bash
ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/GC/
ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/Wii/
ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/StateSaves/
```

Once I see what's there, we'll set up three bidirectional syncs:

**CachyOS → Steam Deck:**
- `~/.local/share/dolphin-emu/GC` ↔ `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/GC`
- `~/.local/share/dolphin-emu/Wii` ↔ `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/Wii`
- `~/.local/share/dolphin-emu/StateSaves` ↔ `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/StateSaves`

### HUMAN
(deck@steamdeck ~)$ ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/GC/ ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/Wii/ ls -la /home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/StateSaves/ total 24 drwxr-xr-x  5 deck deck 4096 Jan 15 22:06 . drwxr-xr-x 17 deck deck 4096 Jan 15 22:05 .. drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 EUR drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 JAP -rw-r--r--  1 deck deck   68 Jan 29 00:01 SRAM.raw drwxr-xr-x  3 deck deck 4096 Jan 15 22:05 USA total 48 drwxr-xr-x 11 deck deck 4096 Jan 29 00:01 . drwxr-xr-x 17 deck deck 4096 Jan 15 22:05 .. -rw-r--r--  1 deck deck  384 Jan 29 00:01 fst.bin drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 import drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 meta drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 shared1 drwxr-xr-x  3 deck deck 4096 Jan 15 22:05 shared2 drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 sys drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 ticket drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 title drwxr-xr-x  2 deck deck 4096 Jan 29 00:01 tmp drwxr-xr-x  2 deck deck 4096 Jan 15 22:05 wfs total 8 drwxr-xr-x  2 deck deck 4096 Jan 15 21:37 . drwxr-xr-x 17 deck deck 4096 Jan 15 22:05 .. (deck@steamdeck ~)$

### ASSISTANT
Perfect! Now let's set up the three Dolphin sync folders:

## On CachyOS Syncthing

### 1. GameCube Saves:
- Click "Add Folder"
- **Folder Label:** `Dolphin GC`
- **Folder Path:** `/home/toastedmel0n/.local/share/dolphin-emu/GC`
- Sharing tab → check Steam Deck
- Save

### 2. Wii Saves:
- Click "Add Folder"
- **Folder Label:** `Dolphin Wii`
- **Folder Path:** `/home/toastedmel0n/.local/share/dolphin-emu/Wii`
- Sharing tab → check Steam Deck
- Save

### 3. Save States:
- Click "Add Folder"
- **Folder Label:** `Dolphin States`
- **Folder Path:** `/home/toastedmel0n/.local/share/dolphin-emu/StateSaves`
- Sharing tab → check Steam Deck
- Save

## On Steam Deck Syncthing

Accept each folder share and set paths:

**Dolphin GC:**
- Path: `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/GC`

**Dolphin Wii:**
- Path: `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/Wii`

**Dolphin States:**
- Path: `/home/deck/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/StateSaves`

Once those are syncing, we'll move on to DuckStation and Citron!

### HUMAN
lets go citron

### ASSISTANT
Great! Let's set up Citron (Switch emulator).

**On Steam Deck, check the Citron saves structure:**
```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ | grep -i citron
```

Then let's look inside:
```bash
# Check if there's a citron folder
ls -la /run/media/deck/SD1T5/Emulation/saves/citron/ 2>/dev/null || ls -la /run/media/deck/SD1T5/Emulation/saves/ryujinx/ 2>/dev/null
```

**On CachyOS, find where Citron stores saves:**
```bash
# Check common locations
ls -la ~/.local/share/ | grep -i citron
ls -la ~/.config/ | grep -i citron
```

Citron is a fork of Yuzu/Ryujinx, so it might use similar paths. Run those commands and share the output so we can find the save locations on both systems.

### HUMAN
❯ # Check common locations  ls -la __~/.local/share/__ | grep -i citron  ls -la __~/.config/__ | grep -i citron drwxr-xr-x    - toastedmel0n  3 Feb 16:38 citron drwxr-xr-x    - toastedmel0n  4 Feb 15:24 citron drwxr-xr-x    - toastedmel0n  4 Feb 14:45 'citron team' ~ ❯

### ASSISTANT
Good! Citron has folders in both locations. Let's see what's inside:

```bash
ls -la ~/.local/share/citron/
ls -la ~/.config/citron/
ls -la ~/.local/share/citron/nand/user/save/ 2>/dev/null
```

Switch emulators typically store saves in a `nand/user/save/` structure. Now check Steam Deck:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ | grep -E "citron|ryujinx|yuzu"
```

Then look inside whichever folder exists:
```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ryujinx/ 2>/dev/null
```

(I'm guessing it might be under "ryujinx" since Citron is based on it, but let me know what you find!)

### HUMAN
❯ ls -la __~/.local/share/citron/__  ls -la __~/.config/citron/__  ls -la __~/.local/share/citron/nand/user/save/__ 2>__/dev/null__ drwxr-xr-x - toastedmel0n  3 Feb 16:38  . drwxr-xr-x - toastedmel0n  4 Feb 15:25  .. drwxr-xr-x - toastedmel0n  3 Feb 16:38  amiibo drwxr-xr-x - toastedmel0n  3 Feb 16:38  crash_dumps drwxr-xr-x - toastedmel0n  3 Feb 16:38  dump drwxr-xr-x - toastedmel0n  3 Feb 16:38  icons drwxr-xr-x - toastedmel0n  4 Feb 09:43  keys drwxr-xr-x - toastedmel0n  4 Feb 14:40  load drwxr-xr-x - toastedmel0n  4 Feb 15:22  log drwxr-xr-x - toastedmel0n  4 Feb 15:17  nand drwxr-xr-x - toastedmel0n  3 Feb 17:00  play_time drwxr-xr-x - toastedmel0n  3 Feb 16:38  screenshots drwxr-xr-x - toastedmel0n  4 Feb 15:01  sdmc drwxr-xr-x - toastedmel0n  4 Feb 14:40  shader drwxr-xr-x - toastedmel0n  3 Feb 16:38  tas drwxr-xr-x    - toastedmel0n  4 Feb 15:24  . drwxr-xr-x    - toastedmel0n  4 Feb 16:48  .. drwxr-xr-x    - toastedmel0n  4 Feb 15:10  custom drwxr-xr-x    - toastedmel0n  4 Feb 10:06  input .rw-r--r--  59k toastedmel0n  4 Feb 15:24 󱁻 qt-config.ini .rw-r--r--    8 toastedmel0n  3 Feb 16:59 󰡯 telemetry_id .rw-r--r-- 1.7k toastedmel0n  4 Feb 15:24 󱁻 window_state.ini drwxr-xr-x - toastedmel0n  4 Feb 10:05  . drwxr-xr-x - toastedmel0n  3 Feb 17:01  .. drwxr-xr-x - toastedmel0n  4 Feb 10:05  0000000000000000 drwxr-xr-x - toastedmel0n  4 Feb 15:24  cache ~ ❯

### ASSISTANT
Perfect! Now check Steam Deck:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ryujinx/
```

Citron uses the `nand/user/save/` structure for game saves. We'll need to sync that folder. Let me see what's on the Steam Deck side.

### HUMAN
why does it say ryujinx?

### ASSISTANT
Good question! Citron is a fork of Ryujinx (after Ryujinx was taken down by Nintendo). When you're using EmulationStation/EmuDeck on the Steam Deck, it might still be using the "ryujinx" folder name for save organization even though it's launching Citron.

It's similar to how many Yuzu forks still use "yuzu" in their paths. The save structure is compatible, so the folder naming doesn't really matter - what matters is that we sync the right folders.

Let's check what's actually there on Steam Deck:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ryujinx/
```

If there's no "ryujinx" folder, it might be under a different name. Let's also check:

```bash
ls -la /run/media/deck/SD1T5/Emulation/saves/ | grep -E "switch|citron|yuzu"
```

This will show us what Switch emulator save folder actually exists on your Steam Deck.
