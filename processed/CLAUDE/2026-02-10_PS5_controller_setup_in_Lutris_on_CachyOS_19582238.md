---
category: homelab
date: 2026-02-10
id: 772920
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: CLAUDE
summary: Bryan was trying to get his PS5 controller working in Lutris games on CachyOS
  through various methods including environment variables, Steam integration, and
  SDL2 configuration.
tags:
- ps5-controller
- lutris
- cachyos
- sdl2
- controller-support
- linux-gaming
---
# PS5 controller setup in Lutris on CachyOS

### HUMAN
how do i add the ability to use my ps5 controller in games via lutris on cachyos?

### ASSISTANT
To use your PS5 controller in games via Lutris on CachyOS, you'll need to set up proper controller support. Here's how:

**1. Install necessary packages:**
```bash
sudo pacman -S steam  # Installs Steam's controller drivers
```

**2. Connect your controller:**
- **Wired**: Just plug it in via USB-C
- **Wireless**: Hold the PS button + Create button (small button left of touchpad) until the light bar flashes, then pair via Bluetooth settings

**3. Configure Lutris:**
Open Lutris and go to your game's settings:
- Right-click game → Configure
- Under "System options" tab, enable:
  - **SDL2 gamepad support** 
- Under "Runner options" (if using Wine/Proton):
  - Set environment variable `SDL_GAMECONTROLLERCONFIG` if needed

**4. Use Steam Input (recommended):**
Even if you're not launching through Steam, you can leverage Steam's excellent controller support:
```bash
# Launch Lutris through Steam
steam steam://rungameid/[launch lutris]
```
Or add Lutris games as non-Steam games to use Steam Input.

**5. Alternative - Install SDL controller configs:**
```bash
yay -S sdl-gamecontrollerdb-git
```

**6. Test the controller:**
```bash
sudo pacman -S jstest-gtk
jstest-gtk
```

The PS5 controller should work out of the box on most modern kernels (CachyOS uses recent kernels), but Steam's drivers provide the best compatibility. If you run into issues with specific games, enabling Steam's compatibility layer or using Proton-GE can help.

### HUMAN
this is what i see

### ASSISTANT
Perfect! I can see you're in the Lutris game configuration. Here's what you need to do:

**In the "SDL2 gamepad mapping" field:**
Leave it empty for now - this uses the system default which should work fine.

**In the "Environment variables" section:**
Click the "Add" button and add these:

1. **Key:** `SDL_GAMECONTROLLERCONFIG`  
   **Value:** Leave empty initially (or you can add a specific config if needed)

2. **Key:** `SDL_JOYSTICK_DEVICE`  
   **Value:** `/dev/input/event*` (this ensures SDL detects your controller)

However, the most important thing is to **enable SDL2 gamepad support** which I don't see in your screenshot. Scroll up in this same configuration window - there should be a checkbox or toggle for "Enable SDL2 gamepad support" or similar in the System options section.

**Quick alternative approach:**
Instead of manual environment variables, try adding:
- **Key:** `SDL_GAMECONTROLLER_ALLOW_BACKGROUND_EVENTS`
- **Value:** `1`

This allows the controller to work even when the game window isn't focused.

After making these changes, click "Save" and try launching your game. If the controller still doesn't work, you might need to install `steam` (as mentioned earlier) since it provides the best controller drivers, or check that your PS5 controller is actually detected by running `jstest /dev/input/js0` in a terminal.

### HUMAN
this is the upper part of that menu after i put those environment variables in

### ASSISTANT
Good! I can see the System options tab now. I notice there's no explicit "Enable SDL2 gamepad" toggle visible here, which means it's likely handled through the environment variables you added.

However, I see you have **"Prefer system libraries"** enabled. This is important for controller support.

**Now scroll down further** to see if there are more options below the "Input" section. Sometimes there's a specific controller or gamepad section.

**But before that, let's verify your controller is actually detected:**

Open a terminal and run:
```bash
ls /dev/input/js*
```

This should show something like `/dev/input/js0` if your controller is connected.

Also try:
```bash
cat /proc/bus/input/devices | grep -A 5 "DualSense"
```

This will confirm if your PS5 controller is recognized by the system.

**If the controller IS detected**, your environment variables should work. Make sure you have:
- `SDL_GAMECONTROLLER_ALLOW_BACKGROUND_EVENTS` set to `1`
- Save the configuration
- Launch your game

**If the controller is NOT detected**, you may need to:
1. Install Steam for its controller drivers: `sudo pacman -S steam`
2. Or install the standalone SDL gamepad library: `sudo pacman -S sdl2`

Let me know what those terminal commands show and whether you see any additional controller-related options when you scroll down in the Lutris settings.

### HUMAN
still wont work even after the steam and sdk gamepad library?

### ASSISTANT
Let's troubleshoot this step by step. First, I need to verify some things:

**1. Check if your controller is actually detected:**

Open a terminal and run these commands:
```bash
ls /dev/input/js*
ls /dev/input/event*
lsusb | grep -i sony
```

**2. Test the controller directly:**
```bash
sudo pacman -S evtest
sudo evtest
```
Select your PS5 controller from the list and press some buttons to see if it responds.

**3. Check what Wine runner you're using:**

In Lutris, go back to your game configuration and check the "Runner options" tab. What Wine version are you using? (Wine-GE, Proton, regular Wine?)

**4. Try these additional environment variables:**

Remove what you added before and try this combination instead:

**Key:** `DXVK_HUD`  
**Value:** `1`

**Key:** `PROTON_ENABLE_NVAPI`  
**Value:** `1`

**Key:** `WINE_GAMEPAD`  
**Value:** `1`

**5. Alternative: Use Steam's Proton directly**

If your game supports it, try adding the game as a non-Steam game in Steam and run it through Steam's Proton - this has the best controller support.

Can you tell me:
- What game are you trying to play?
- What shows up when you run those detection commands?
- Is the controller connected via USB or Bluetooth?

### HUMAN
how would i add the lutris game to my steam for easy controller support?

### ASSISTANT
Here's how to add your Lutris game to Steam for better controller support:

**Method 1: Add Lutris as a Non-Steam Game**

1. Open Steam
2. Click "Games" in the top menu → "Add a Non-Steam Game to My Library"
3. Click "Browse" and navigate to where Lutris is installed (usually `/usr/bin/lutris` or `/usr/games/lutris`)
4. Select it and click "Add Selected Programs"

**Method 2: Add the game's executable directly (better option)**

1. Find your game's executable in Lutris:
   - Right-click your game in Lutris → "Configure"
   - Note the "Executable" path under "Game options"
   
2. In Steam:
   - Games → Add a Non-Steam Game → Browse
   - Navigate to that executable path
   - Add it to Steam

3. Configure launch options (if needed):
   - Right-click the game in Steam → Properties
   - In "Launch Options" you may need to add Wine prefix path:
   ```
   WINEPREFIX="/path/to/your/game/prefix" %command%
   ```

**Method 3: Use Lutris URI (easiest for launching)**

1. In Steam: Games → Add a Non-Steam Game → Browse
2. Navigate to `/usr/bin/lutris`
3. Add it, then right-click → Properties
4. Change the launch options to:
   ```
   lutris:rungame/[game-slug]
   ```
   (To find your game's slug, right-click the game in Lutris → "Copy game identifier")

**After adding to Steam:**
- Launch the game through Steam
- Steam's controller support should automatically work
- You can configure the controller by pressing the Steam button and going to "Controller Configuration"

Which method would you prefer? The direct executable method usually works best if you know where the game files are.

### HUMAN
which is the most straight forward way to get my controller working?

### ASSISTANT
**The most straightforward way: Install Steam and launch Lutris games through it.**

Here's the simplest approach:

**1. Make sure Steam is installed and running:**
```bash
sudo pacman -S steam
```
Launch Steam once to set up the controller drivers.

**2. Add Lutris to Steam:**
- Open Steam
- Games → Add a Non-Steam Game to My Library
- Click "Browse" → navigate to `/usr/bin/lutris` and select it
- Click "Add Selected Programs"

**3. Launch your game:**
- Close Lutris if it's open
- In Steam, launch "Lutris" from your library
- This opens Lutris with Steam's controller layer active
- Now launch your game from within Lutris

That's it. Your PS5 controller should just work because Steam's Input system handles everything automatically.

**Why this works:**
When you launch Lutris through Steam, Steam's controller drivers wrap around everything Lutris launches, giving you full controller support without any configuration needed.

**Alternative if that doesn't work:**
Just launch Steam first, then launch Lutris normally (not through Steam). As long as Steam is running in the background, its controller drivers are active system-wide and should help.

Try the first method - it's the most reliable and requires zero configuration in Lutris itself.

### HUMAN
how do i remove sdl2?

### ASSISTANT
To remove SDL2:

```bash
sudo pacman -R sdl2
```

If you want to also remove any dependencies that were installed with it and are no longer needed:

```bash
sudo pacman -Rs sdl2
```

**However**, be careful - SDL2 might be a dependency for other programs. Before removing it, check what depends on it:

```bash
pactree -r sdl2
```

This will show you what packages require SDL2. If you see important packages listed (like Steam, games, or other applications), removing SDL2 will break them.

**Why do you want to remove it?** If it's causing conflicts with controller detection, you don't need to remove it - just launching through Steam should override any SDL2 issues. The Steam approach I mentioned should work regardless of whether SDL2 is installed or not.

### HUMAN
do i need sdl2 from when you told me to install earlier?

### ASSISTANT
**No, you don't need it** for the Steam method I just recommended.

I originally suggested installing `sdl2` thinking you'd configure Lutris manually with environment variables. But since we're now using the **much simpler Steam approach**, Steam has its own controller drivers built-in and handles everything for you.

**You can safely remove it:**
```bash
sudo pacman -R sdl2
```

Just check first to make sure nothing else depends on it:
```bash
pactree -r sdl2
```

If it only shows sdl2-related packages or nothing critical, go ahead and remove it.

**Keep Steam installed though** - that's what's actually providing the controller support now. The workflow is just:
1. Steam installed ✓
2. Launch Lutris through Steam (or have Steam running in background)
3. Controller works automatically

Sorry for the confusion with the earlier SDL2 suggestion - the Steam method is way more straightforward and doesn't need all that manual configuration.

### HUMAN
it was this command sudo pacman -S sdl2

### ASSISTANT
Yes, that's the command I told you to use earlier. You can remove what it installed with:

```bash
sudo pacman -R sdl2
```

However, **before removing it**, run this to see if anything else needs it:

```bash
pactree -r sdl2
```

If you see important packages in that list (like Steam, Lutris, or other games/programs), then those programs depend on SDL2 and you should **keep it installed**.

But if nothing critical shows up, or if it's only showing optional dependencies, you can safely remove it.

The key point: **Steam has its own controller handling**, so for the Steam method, you don't need the standalone SDL2 package. But some programs (possibly including Steam itself or Lutris) might require SDL2 as a dependency anyway, in which case it needs to stay.

Check that `pactree` output first before deciding.

### HUMAN
❯ sudo pacman -R sdl2 error: target not found: sdl2 ~ ❯

### ASSISTANT
That means `sdl2` isn't actually installed on your system. 

When you ran `sudo pacman -S sdl2` earlier, either:
1. It was already installed as a dependency of something else (so pacman said "already installed")
2. The installation failed
3. The package name might be slightly different on CachyOS

You can verify what SDL-related packages you have:
```bash
pacman -Qs sdl
```

But honestly, **don't worry about it**. Since it's not installed as a standalone package, there's nothing to remove. 

**Just focus on the Steam method:**
1. Make sure Steam is installed: `sudo pacman -S steam`
2. Launch Lutris through Steam (or keep Steam running in the background)
3. Your controller should work

The SDL2 stuff was a red herring - you don't need to mess with it at all for the Steam approach.

### HUMAN
❯ pacman -Qs sdl local/sdl12-compat 1.2.68-2.1    SDL 1.2 runtime compatibility library using SDL 2.0 local/sdl2-compat 2.32.64-1.1    An SDL2 compatibility layer that uses SDL3 behind the scenes local/sdl3 3.4.0-3.2    A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard (Version 3) local/sdl_image 1.2.12-9.1    A simple library to load images of various formats as SDL surfaces local/vlc-plugin-sdl 3.0.21-32.1    Free and open source cross-platform multimedia player and framework - SDL plugin ~ ❯

### ASSISTANT
Perfect! You already have SDL packages installed (they're dependencies of other software), but not the standalone `sdl2` package I mentioned earlier. So there's nothing to remove.

**You're good to go with the Steam method now:**

1. **Make sure Steam is installed:**
   ```bash
   sudo pacman -S steam
   ```

2. **Launch Steam**, then either:
   - **Option A:** Add Lutris to Steam (Games → Add Non-Steam Game → Browse to `/usr/bin/lutris`), then launch Lutris from Steam library
   - **Option B:** Just keep Steam running in the background, then launch Lutris normally

3. **Launch your game from Lutris** - your PS5 controller should now work automatically thanks to Steam's controller support running in the background.

The SDL packages you have installed are fine and needed by other programs like VLC. Just focus on getting Steam running before you launch your games.

Does Steam launch correctly for you?
