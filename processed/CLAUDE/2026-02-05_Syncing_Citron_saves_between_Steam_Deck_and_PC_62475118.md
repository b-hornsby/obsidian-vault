---
source: CLAUDE
date: 2026-02-05
category: coding
id: 62475118
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
---
# Syncing Citron saves between Steam Deck and PC

### HUMAN
ready to get syncthing working with my citron saves. i have a steam deck running the latest nightly image and citron 2026.02.1 on my cachyos pc. i want to not lose the current progress i have on my steam deck

### ASSISTANT
I'll help you set up Syncthing to sync your Citron saves between your Steam Deck and CachyOS PC without losing your current progress. Let me search for the most current information about Citron save locations and Syncthing setup.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Perfect! Based on my research, I can help you set up Syncthing to sync your Citron saves between your Steam Deck and CachyOS PC. Here's what you need to know:

## Citron Save Locations

**On your Steam Deck (Linux/SteamOS):**
- Default save location: `~/.local/share/citron/nand/user/save/`
- This is typically: `/home/deck/.local/share/citron/nand/user/save/`

**On your CachyOS PC (Linux):**
- Same default location: `~/.local/share/citron/nand/user/save/`
- Typically: `/home/[your-username]/.local/share/citron/nand/user/save/`

## Setup Plan (to preserve your Steam Deck progress)

Since you want to keep your Steam Deck progress, here's the safest approach:

### 1. **First, backup your Steam Deck saves** (safety first!)
```bash
# On Steam Deck, create a backup
cp -r ~/.local/share/citron/nand/user/save ~/citron_save_backup
```

### 2. **Install Syncthing on both devices**

**On Steam Deck:**
```bash
# Install via Flatpak (recommended for Steam Deck)
flatpak install flathub me.kozec.syncthingtk
```

**On CachyOS:**
```bash
# Install via pacman
sudo pacman -S syncthing
```

### 3. **Initial sync strategy (preserving Steam Deck saves)**

The safest approach is to:
1. Set up Syncthing on both devices
2. Configure the Steam Deck as the "source of truth" initially
3. Let it sync TO your CachyOS PC (overwriting any PC saves)
4. Then enable bidirectional sync

### 4. **Syncthing Configuration**

Would you like me to create a detailed step-by-step guide for:
- Setting up Syncthing on both devices
- Configuring the sync folder
- Initial one-way sync (Steam Deck → CachyOS)
- Then switching to bidirectional sync

**Important notes:**
- Citron 2026.02.1 has new "Global Custom Save Paths" and "Save Mirroring" features that might be useful
- Make sure both installations use the same Citron version for compatibility
- Close Citron on both devices before the initial sync

Should I walk you through the complete setup process?

### HUMAN
i just need to know where my saves are on each device for routing and how to set it up so i dont lose my current saves

### ASSISTANT
## Save Locations

**Steam Deck:**
```
/home/deck/.local/share/citron/nand/user/save/
```

**CachyOS PC:**
```
/home/[your-username]/.local/share/citron/nand/user/save/
```

## Setup Without Losing Steam Deck Saves

### Step 1: Before anything, backup Steam Deck saves
```bash
# On Steam Deck
cp -r ~/.local/share/citron/nand/user/save ~/citron_save_backup
```

### Step 2: Install Syncthing
- **Steam Deck:** `flatpak install flathub me.kozec.syncthingtk`
- **CachyOS:** `sudo pacman -S syncthing`

### Step 3: Initial Setup (preserving Steam Deck progress)

1. **Start Syncthing on Steam Deck first**
   - Open the Syncthing GUI (usually http://127.0.0.1:8384)
   - Add a new folder pointing to `/home/deck/.local/share/citron/nand/user/save/`
   - Set folder type to **"Send Only"** temporarily

2. **Start Syncthing on CachyOS**
   - Open GUI (http://127.0.0.1:8384)
   - Pair with Steam Deck (you'll see device IDs in each GUI)
   - Accept the shared folder from Steam Deck
   - Point it to your local path: `/home/[your-username]/.local/share/citron/nand/user/save/`

3. **Let the initial sync complete** (Steam Deck → CachyOS)

4. **After initial sync, change both to "Send & Receive"** for bidirectional sync

This way your Steam Deck saves are preserved and copied to your PC first, then both devices stay in sync going forward.

### HUMAN
why does my dolphin saves one say stopped on my steam deck but not my pc?

### ASSISTANT
The "Stopped" status in Syncthing usually means one of these things:

## Common Causes

1. **The folder path doesn't exist on that device**
   - On your Steam Deck, check if the Dolphin save path actually exists:
   ```bash
   ls -la ~/.local/share/dolphin-emu/GC/
   # or wherever your Dolphin saves are
   ```

2. **Syncthing paused/stopped the folder manually**
   - In the Syncthing GUI on Steam Deck, click on the folder
   - Look for a "Resume" button - if it's there, the folder was paused

3. **Permission issues**
   - Syncthing doesn't have read/write access to that folder path

4. **Different save locations between devices**
   - Dolphin saves might be in different paths on Steam Deck vs PC
   - Steam Deck (Flatpak): `~/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/`
   - Steam Deck (native): `~/.local/share/dolphin-emu/`
   - CachyOS: `~/.local/share/dolphin-emu/` or `~/.config/dolphin-emu/`

## Quick Fix

In the Syncthing GUI on your Steam Deck:
- Click on the stopped folder
- Check the error message (should tell you exactly why it's stopped)
- Either fix the path or click "Resume" if it was just paused

What error/message do you see when you click on the stopped folder?

### HUMAN
now that thats all set up do i need to manually enable sharething each boot or how does that work?

### ASSISTANT
## Auto-start Setup

Syncthing won't start automatically by default - you need to enable it.

### On CachyOS (systemd)
```bash
# Enable and start for your user
systemctl --user enable syncthing.service
systemctl --user start syncthing.service
```

### On Steam Deck (Flatpak version)

The Flatpak version doesn't come with auto-start by default. You have a couple options:

**Option 1: Add to Steam as a non-game application** (starts when you open it)

**Option 2: Create a systemd user service**
```bash
# Create the service file
mkdir -p ~/.config/systemd/user/
nano ~/.config/systemd/user/syncthing.service
```

Add this content:
```ini
[Unit]
Description=Syncthing
After=network.target

[Service]
ExecStart=/usr/bin/flatpak run me.kozec.syncthingtk

[Install]
WantedBy=default.target
```

Then enable it:
```bash
systemctl --user enable syncthing.service
systemctl --user start syncthing.service
```

**Option 3: Simple autostart** (easiest for Steam Deck)
```bash
# Add to autostart
mkdir -p ~/.config/autostart/
cp /var/lib/flatpak/exports/share/applications/me.kozec.syncthingtk.desktop ~/.config/autostart/
```

After setting this up, Syncthing will start automatically on boot. You can verify it's running by checking http://127.0.0.1:8384 in a browser.

### HUMAN
what is the recommended way of using this tool moving forward?

### ASSISTANT
## Recommended Workflow with Syncthing

### Daily Usage
**Just play normally** - Syncthing handles everything in the background. You don't need to do anything special.

**Golden rule:** Close Citron/Dolphin on one device before opening on the other
- This prevents save conflicts from both devices writing at the same time
- Syncthing syncs within seconds when files change

### Best Practices

1. **Let sync complete before switching devices**
   - Check Syncthing GUI shows "Up to Date" before moving to the other device
   - Usually takes just a few seconds after closing the emulator

2. **If you forget and play on both devices simultaneously:**
   - Syncthing will create conflict files (`.sync-conflict` extensions)
   - You'll need to manually decide which save to keep
   - Avoid this by following the golden rule above

3. **Monitor occasionally**
   - Glance at http://127.0.0.1:8384 if something seems off
   - Check that both devices show "Up to Date"

4. **Keep that backup**
   - Keep your initial backup (`~/citron_save_backup`) for a while
   - Delete it once you're confident everything works smoothly

### When Things Go Wrong

If you accidentally create conflicts or something seems off:
- Stop Citron on both devices
- Check Syncthing GUI for conflict files
- Keep the save with the latest timestamp/most progress
- Delete the conflict file
- Let Syncthing sync again

**TL;DR:** Play on one device, close the emulator, switch devices. Syncthing does the rest automatically.

### HUMAN
so when i play next, do i need to boot up syncthing on my steam deck? do  need to on my cachyos?

### ASSISTANT
## No, you don't need to manually start Syncthing

Since you set up auto-start on both devices:

**CachyOS:** Syncthing starts automatically on boot (you enabled the systemd service)

**Steam Deck:** Syncthing starts automatically on boot (depending which method you chose - systemd service or autostart)

### When You Play Next

Just boot up the device and play. Syncthing is already running in the background.

**You can verify it's running:**
- Open a browser and go to http://127.0.0.1:8384
- If you see the Syncthing GUI, it's running
- If not, you need to start it (or fix the auto-start setup)

### Typical Session

1. Boot Steam Deck (Syncthing auto-starts)
2. Open Citron and play
3. Close Citron when done
4. Wait ~10 seconds for sync to complete (optional: check GUI shows "Up to Date")
5. Boot CachyOS PC (Syncthing auto-starts and pulls the latest saves)
6. Open Citron and continue where you left off

The only time you'd manually interact with Syncthing is if you want to check sync status or troubleshoot issues. Otherwise, it's completely hands-off.

### HUMAN
so i NEED to make these both work on auto start?

### ASSISTANT
No, you don't **NEED** to set up auto-start, but it makes life much easier.

## Without Auto-start

You'd have to manually start Syncthing every time:
- **CachyOS:** `systemctl --user start syncthing` or launch it from app menu
- **Steam Deck:** Open the Syncthing app from your library

Then wait for it to sync before playing.

## With Auto-start (Recommended)

Syncthing just runs in the background always. You never think about it. Boot device → play → done.

## Middle Ground Option

Set up auto-start on **just one device** (like your CachyOS PC that's always on), and manually start it on Steam Deck only when you need it.

But honestly, auto-start on both is the "set it and forget it" approach. Uses minimal resources (Syncthing is lightweight), and you never have to remember to start it.

**Your choice** - but if you want the smoothest experience where you just play and don't think about syncing, set up auto-start on both.

### HUMAN
how do i set it up so i dont have to manually boot up syncthing each time?

### ASSISTANT
## Auto-start Setup

You already did CachyOS. Now for Steam Deck:

### Steam Deck (Easiest Method)

```bash
# Create autostart directory if it doesn't exist
mkdir -p ~/.config/autostart/

# Copy the Syncthing desktop file to autostart
cp /var/lib/flatpak/exports/share/applications/me.kozec.syncthingtk.desktop ~/.config/autostart/
```

That's it! Syncthing will now start automatically when you boot your Steam Deck.

### Verify It Works

1. Reboot your Steam Deck
2. After it boots, open a browser and go to http://127.0.0.1:8384
3. If you see the Syncthing GUI, auto-start is working

### Alternative Method (systemd - more reliable)

If the above doesn't work for some reason:

```bash
# Create systemd user directory
mkdir -p ~/.config/systemd/user/

# Create service file
nano ~/.config/systemd/user/syncthing.service
```

Paste this:
```ini
[Unit]
Description=Syncthing
After=network.target

[Service]
ExecStart=/usr/bin/flatpak run me.kozec.syncthingtk

[Install]
WantedBy=default.target
```

Save (Ctrl+O, Enter, Ctrl+X), then:
```bash
systemctl --user enable syncthing.service
systemctl --user start syncthing.service
```

Try the first method - it's simpler and should work fine for Steam Deck.

### HUMAN
i never did either device

### ASSISTANT
Ah, my mistake! Let's set up auto-start on both devices now.

## CachyOS PC

```bash
# Enable and start Syncthing service
systemctl --user enable syncthing.service
systemctl --user start syncthing.service
```

## Steam Deck

```bash
# Create autostart directory
mkdir -p ~/.config/autostart/

# Copy Syncthing to autostart
cp /var/lib/flatpak/exports/share/applications/me.kozec.syncthingtk.desktop ~/.config/autostart/
```

## Verify Both Work

**CachyOS:**
```bash
# Check if it's running
systemctl --user status syncthing.service
```

**Steam Deck:**
- Reboot the Steam Deck
- After boot, open browser and go to http://127.0.0.1:8384
- Should see Syncthing GUI

**Both devices:**
- Open http://127.0.0.1:8384 in a browser
- If you see the Syncthing interface, auto-start is working

Now both will start Syncthing automatically on boot and you won't have to think about it again.

### HUMAN
how does the cachyos command make it work automatically?

### ASSISTANT
## How the systemd Commands Work

### `systemctl --user enable syncthing.service`
This creates a **symbolic link** that tells systemd to start Syncthing when you log in.

Specifically, it links the service file to your user's auto-start directory so systemd knows "hey, when this user logs in, start this service."

### `systemctl --user start syncthing.service`
This starts Syncthing **right now** (without waiting for a reboot).

So you get it running immediately AND it will auto-start on future boots.
---
## What's systemd?

**systemd** is the system and service manager on most Linux distros (including CachyOS). It handles:
- Starting services on boot
- Managing background processes
- Restarting crashed services
- etc.

The `--user` flag means it runs under your user account (not as root/system-wide).

## Why This vs Steam Deck's Method?

- **CachyOS:** Has native Syncthing package with systemd service file built-in, so you just enable it
- **Steam Deck:** Uses Flatpak version, which doesn't include systemd integration, so you use the autostart directory method instead

Both achieve the same result: Syncthing starts automatically when you boot/login.
