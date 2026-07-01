---
category: streaming
date: 2026-02-22
id: 911182
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: CLAUDE
summary: Bryan was troubleshooting OBS Studio not appearing in the KDE Plasma application
  launcher on CachyOS despite being installed.
tags:
- obs-studio
- kde-plasma
- app-tray
- cachyos
- desktop-entry
- kbuildsycoca6
---
# OBS not appearing in app tray

### HUMAN
tried installing obs on cachyos and it doesnt show up in my app tray but does pop up when i search for it?

### ASSISTANT
This is a pretty common issue on CachyOS (and Arch-based distros generally). The app is installed and working, it just isn't showing up in your app tray/launcher automatically. A few things to try:

**Update the desktop database**

Run this in a terminal:
```bash
sudo update-desktop-database
```
Then log out and back in, or restart your compositor/shell.

**Also refresh the icon cache:**
```bash
sudo gtk-update-icon-cache -f /usr/share/icons/hicolor
```

**Check if the .desktop file exists:**
```bash
ls /usr/share/applications/ | grep obs
```
You should see something like `com.obsproject.Studio.desktop`. If it's there, the database refresh above should fix it.

**If using a Wayland session**, sometimes the app grid/launcher needs a full logout or reboot to pick up new entries — worth trying if you haven't already.

**If the .desktop file is missing entirely**, you can try reinstalling:
```bash
sudo pacman -S obs-studio
```

Most likely it's just a stale desktop database and the `update-desktop-database` + logout will do the trick.

### HUMAN
none of those did anything but when i run the ls command it does show up: ❯ ls __/usr/share/applications/__ | grep obs .rw-r--r-- 9.4k root 18 Jan 05:52 com.obsproject.Studio.desktop ~ ❯

### ASSISTANT
Since the .desktop file is there and OBS launches fine from search, this is likely a launcher/category filtering issue. Which desktop environment or launcher are you using? (KDE, GNOME, something else?)

Some launchers hide apps that are categorized under "AudioVideo" or similar unless you're browsing that specific category. It might just be a matter of checking a different section of your app menu rather than it truly being missing.

### HUMAN
it literally doesnt pop up in the 'o' section of my apps

### ASSISTANT
Got it. Let's check what categories the desktop file has:

```bash
cat /usr/share/applications/com.obsproject.Studio.desktop
```

Paste the output here and we can see if something looks off with the categories or if `NoDisplay=true` snuck in there somehow.

### ASSISTANT
The .desktop file looks totally fine — no `NoDisplay=true`, categories are normal. Which launcher/DE are you using? KDE Plasma, GNOME, something custom like Rofi or Wofi?

On KDE for example, the app menu sorts alphabetically by **Name**, so "OBS Studio" would be under **O** but could be easy to miss if you're scrolling past it. Worth double-checking the **V** section too since some launchers group by the executable or generic name.

### HUMAN
im on kde but it literally isnt in my app tray at all

### ASSISTANT
Try rebuilding the KDE-specific menu cache:

```bash
kbuildsycoca6 --noincremental
```

Then log out and back in. KDE maintains its own service/menu cache separate from the general desktop database, and it can sometimes get out of sync with newly installed apps.

### HUMAN
still no

### ASSISTANT
That's pretty weird at this point. Let's check if it's maybe hidden in KDE's menu editor:

```bash
kmenuedit
```

Open that, then look under **Sound & Video** (that's where AudioVideo category apps go in KDE). See if OBS is listed there but has "hidden" checked on it.

### HUMAN
i dont even see a sound and video category

### ASSISTANT
That's odd. Can you check if you have any menu hiding rules set up?

```bash
cat ~/.config/menus/applications.menu
```

And also check if there's anything in:
```bash
ls ~/.local/share/applications/ | grep obs
```

A local override in `~/.local/share/applications/` could be shadowing or hiding the system one.

### HUMAN
❯ cat ~/.config/menus/applications.menu cat: /home/toastedmel0n/.config/menus/applications.menu: No such file or directory ~ ❯ ls __~/.local/share/applications/__ | grep obs .rw
---
-
---  149 toastedmel0n  3 Feb 20:40 net.local.obs-cli.desktop ~ ❯

### ASSISTANT
There's your culprit. That `net.local.obs-cli.desktop` file might be interfering. Let's see what's in it:

```bash
cat ~/.local/share/applications/net.local.obs-cli.desktop
```

### HUMAN
❯ cat __~/.local/share/applications/net.local.obs-cli.desktop__ [Desktop Entry] Exec=obs-cli replay save Name=replay save NoDisplay=true StartupNotify=false Type=Application X-KDE-GlobalAccel-CommandShortcut=true ~ ❯

### ASSISTANT
That's not the culprit — it's just a keyboard shortcut entry for obs-cli, unrelated to OBS Studio itself.

This is genuinely strange at this point. Can you check what version of OBS you have installed and how you installed it — pacman, flatpak, or AUR?

```bash
pacman -Qs obs
flatpak list | grep obs
```

### HUMAN
❯ pacman -Qs obs  flatpak list | grep obs local/libxmlb 0.3.25-1.1    Library to help create and query binary XML blobs local/obs-studio 32.0.4-1.1    Free, open source software for live streaming and recording local/parallel 20260122-1    A shell tool for executing jobs in parallel local/vlc-plugin-luajit 3.0.21-22    Multi-platform MPEG, VCD/DVD, and DivX player built with luajit for OBS Studio compatibility - LuaJIT scripting plugins ~ ❯

### ASSISTANT
So it's installed via pacman, no flatpak. At this point let's just check if KDE is actually reading that desktop file correctly:

```bash
kreadconfig6 --file /usr/share/applications/com.obsproject.Studio.desktop --group "Desktop Entry" --key "Name"
```

Also, what does your KDE app launcher look like — is it the default Kickoff (the grid/list menu), or something else like Krunner, Application Dashboard, etc.? And just to triple check, you've looked through every category in the menu and OBS genuinely isn't listed anywhere, not just missing from the alphabetical list?

### HUMAN
❯ kreadconfig6 --file __/usr/share/applications/____com.obsproject.Studio____.desktop__ --group "Desktop Entry" --key "Name" OBS Studio ~

### ASSISTANT
KDE can read it fine. Let's try one more thing — force KDE to re-index everything:

```bash
rm -rf ~/.cache/ksycoca6*
kbuildsycoca6
```

Then log out and back in. The ksycoca cache is what actually powers the app menu and sometimes just nuking it entirely works when rebuilding doesn't.

### HUMAN
literally still isnt there

### ASSISTANT
Let's try manually placing a local copy and see if that forces it to show up:

```bash
cp /usr/share/applications/com.obsproject.Studio.desktop ~/.local/share/applications/
```

Log out and back in. If it shows up now, it means something system-wide is suppressing the original — possibly a CachyOS-specific menu customization.

### HUMAN
still no \

### ASSISTANT
Let's see if CachyOS has any custom menu configuration that might be filtering things out:

```bash
ls /etc/xdg/menus/
cat /etc/xdg/menus/applications.menu
```

### HUMAN
❯ ls __/etc/xdg/menus/__ drwxr-xr-x    - root  3 Feb 01:56  applications-merged .rw-r--r--  702 root 17 Feb 13:37  DaVinciResolve.menu .rw-r--r-- 9.9k root 18 Feb 03:01  plasma-applications.menu ~ ❯ cat /etc/xdg/menus/applications.menu cat: /etc/xdg/menus/applications.menu: No such file or directory ~ ❯

### ASSISTANT
Let's check that plasma-applications.menu since that's what KDE actually uses:

```bash
cat /etc/xdg/menus/plasma-applications.menu
```

### ASSISTANT
The menu config looks fine — OBS has `AudioVideo;Recorder;` categories and there's a Multimedia section that includes `AudioVideo`. It should be showing up there.

Let me ask something basic I should have asked earlier — which app launcher widget are you using exactly? Like if you right-click the launcher button in your taskbar, what does it say? "Kickoff", "Application Menu", "Application Dashboard"? And is your Kickoff set to show apps as a list or a grid? Sometimes the grid view doesn't show category browsing the same way.

### HUMAN
application launcher

### ASSISTANT
Application Launcher (the grid one) can sometimes be weird about this. Try right-clicking the launcher > Configure > and check if there's any category filtering going on.

Also, when you open the launcher and browse categories, do you see a "Multimedia" category at all? OBS should be sitting in there since it's `AudioVideo`.

### HUMAN
yeah i dont have a filter on and when i open the launcher i do see multi media but no obs

### ASSISTANT
That's really bizarre. Let's see if KDE's menu system even knows OBS exists:

```bash
kbuildsycoca6 --noincremental 2>&1 | grep -i obs
```

### HUMAN
❯ kbuildsycoca6 --noincremental 2>&1 | grep -i obs ~ ❯

### ASSISTANT
Nothing at all — KDE isn't picking it up. Let's check if the desktop file is being read:

```bash
kbuildsycoca6 --noincremental --debug 2>&1 | grep -i obs
```

### HUMAN
❯ kbuildsycoca6 --noincremental --debug 2>&1 | grep -i obs ~ ❯

### ASSISTANT
Completely invisible to KDE. That's very strange given the file is there and readable. Let's check the file permissions:

```bash
ls -la /usr/share/applications/com.obsproject.Studio.desktop
```

### HUMAN
❯ ls -la __/usr/share/applications/____com.obsproject.Studio____.desktop__ .rw-r--r-- 9.4k root 18 Jan 05:52  /usr/share/applications/com.obsproject.Studio.desktop ~

### ASSISTANT
Permissions are fine. Let's check if there's something weird with the file itself — specifically if it has any hidden characters or a `Hidden=true` line that wasn't visible when we catted it:

```bash
grep -i "hidden\|nodisplay\|onlyshowin\|notshowin" /usr/share/applications/com.obsproject.Studio.desktop
```

### HUMAN
❯ grep -i "hidden\|nodisplay\|onlyshowin\|notshowin" __/usr/share/applications/____com.obsproject.Studio____.desktop__ ~ ❯

### ASSISTANT
Nothing. At this point I'm stumped by the system file. Let's try something different — edit the local copy we put in `~/.local/share/applications/` and add an explicit `OnlyShowIn=KDE;` line to force KDE to claim it:

```bash
echo "OnlyShowIn=KDE;" >> ~/.local/share/applications/com.obsproject.Studio.desktop
kbuildsycoca6
```

Then check if it shows up. If not, let's see if the local copy is being picked up at all:

```bash
kbuildsycoca6 --noincremental --debug 2>&1 | grep -i "local/share/applications"
```

### HUMAN
❯ kbuildsycoca6 --noincremental --debug 2>&1 | grep -i "local/share/applications" ~ ❯

### ASSISTANT
KDE isn't reading your local applications directory at all either, which is very abnormal. Let's check what directories KDE thinks it should be scanning:

```bash
kbuildsycoca6 --noincremental --debug 2>&1 | head -50
```

### HUMAN
❯ kbuildsycoca6 --noincremental --debug 2>&1 | head -50 kbuildsycoca6: Unknown option 'debug'. ~ ❯

### ASSISTANT
```bash
kbuildsycoca6 --noincremental 2>&1 | head -50
```

### HUMAN
❯ kbuildsycoca6 --noincremental --debug 2>&1 | head -50 kbuildsycoca6: Unknown option 'debug'. ~ ❯

### ASSISTANT
Without the debug flag, let's just check what XDG data dirs KDE is actually looking at:

```bash
echo $XDG_DATA_DIRS
echo $XDG_DATA_HOME
```

### HUMAN
❯ echo $XDG_DATA_DIRS
  echo $XDG_DATA_HOME
/home/toastedmel0n/.local/share/flatpak/exports/share /var/lib/flatpak/exports/share /usr/local/share /usr/share
~
❯

### ASSISTANT
There's your problem. `XDG_DATA_HOME` is empty — it should be `~/.local/share` by default, but it's not set. And `XDG_DATA_DIRS` is missing `/usr/share/applications` isn't the issue, but the empty `XDG_DATA_HOME` means KDE isn't scanning `~/.local/share/applications/` at all.

More importantly though, `/usr/share` is in `XDG_DATA_DIRS` so the system OBS desktop file should still be found... 

Let's check if this is a session issue — is `XDG_DATA_HOME` unset only in the terminal, or system-wide:

```bash
systemctl --user show-environment | grep XDG
```

### HUMAN
❯ systemctl --user show-environment | grep XDG XDG_DATA_DIRS=/home/toastedmel0n/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share XDG_RUNTIME_DIR=/run/user/1000 XDG_CONFIG_DIRS=/home/toastedmel0n/.config/kdedefaults:/etc/xdg XDG_CURRENT_DESKTOP=KDE XDG_MENU_PREFIX=plasma- XDG_SEAT=seat0 XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0 XDG_SESSION_CLASS=user XDG_SESSION_DESKTOP=KDE XDG_SESSION_ID=13 XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session11 XDG_SESSION_TYPE=wayland XDG_VTNR=7 ~ ❯

### ASSISTANT
`XDG_DATA_HOME` is missing from the systemd user environment too. That's abnormal but shouldn't prevent `/usr/share` apps from showing since that's in `XDG_DATA_DIRS`.

I'm now suspicious this might just be a Wayland/compositor rendering glitch where the app is actually there but not visible in the grid. Can you try scrolling through the Multimedia category really carefully, or try resizing the launcher window? Sometimes on Wayland the grid doesn't render all items.

Also try this — open the launcher, go to Multimedia, and see how many apps are listed there. Does the number seem right or suspiciously low?

### HUMAN
❯ sudo pacman -Rns obs-studio [sudo] password for toastedmel0n:  error: target not found: obs-studio ~ ❯

### ASSISTANT
Interesting — pacman can't find it to remove it either, yet it showed up in `pacman -Qs`. How did you actually install OBS originally? It might have been installed as part of a bundle or meta-package by CachyOS rather than as a standalone package.

```bash
pacman -Qi obs-studio
```

### HUMAN
nothing shows but the icon does when i search. im trying to delete it

### ASSISTANT
Try:

```bash
which obs
pacman -Qo $(which obs)
```

That'll tell us which package actually owns the obs binary so we can remove the right thing.

### HUMAN
~ ❯ which obs  pacman -Qo $(which obs) which: no obs in (/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/var/lib/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl) which: no obs in (/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/var/lib/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl) error: no targets specified (use -h for help) ~ ❯

### ASSISTANT
So there's no `obs` binary in your PATH either. When you search for OBS and launch it, what actually happens — does it open properly? And what did the search show exactly, was it "OBS Studio" or something else?

Also try:

```bash
find / -name "obs" -type f 2>/dev/null
```

### HUMAN
it fails when i click it

### ASSISTANT
That explains everything! It's a broken/phantom desktop file. The `.desktop` file exists but the actual OBS binary was never properly installed or was removed. Just delete the desktop file:

```bash
sudo rm /usr/share/applications/com.obsproject.Studio.desktop
rm ~/.local/share/applications/com.obsproject.Studio.desktop
kbuildsycoca6
```

Then reinstall OBS properly:

```bash
sudo pacman -S obs-studio
```

### HUMAN
❯ sudo rm /usr/share/applications/com.obsproject.Studio.desktop  rm __~/.local/share/applications/____com.obsproject.Studio____.desktop__  kbuildsycoca6 [sudo] password for toastedmel0n:  rm: cannot remove '/usr/share/applications/com.obsproject.Studio.desktop': No such file or directory kbuildsycoca6 running... ~ 7s ❯

### ASSISTANT
The system file is already gone, good. Now reinstall:

```bash
sudo pacman -S obs-studio
```

### HUMAN
❯ sudo pacman -S obs-studio [sudo] password for toastedmel0n:  resolving dependencies... looking for conflicting packages... Packages (6) libdatachannel-0.24.1-1.1  libjuice-1.7.0-1.1  qrcodegencpp-cmake-1:1.8.0-4  simde-0.8.2-1  uthash-2.3.0-2             obs-studio-32.0.4-1.1 Total Installed Size:  34.89 MiB :: Proceed with installation? [Y/n] y (6/6) checking keys in keyring                                                    [##############################################] 100% (6/6) checking package integrity                                                  [##############################################] 100% (6/6) loading package files                                                       [##############################################] 100% (6/6) checking for file conflicts                                                 [##############################################] 100% (6/6) checking available disk space                                               [##############################################] 100% :: Running pre-transaction hooks... (1/2) Performing snapper pre snapshots for the following configurations... ==> root: 198 (2/2) Waiting for limine-snapper-sync to finish... :: Processing package changes... (1/6) installing libjuice                                                         [##############################################] 100% (2/6) installing libdatachannel                                                   [##############################################] 100% (3/6) installing uthash                                                           [##############################################] 100% (4/6) installing simde                                                            [##############################################] 100% (5/6) installing qrcodegencpp-cmake                                               [##############################################] 100% (6/6) installing obs-studio                                                       [##############################################] 100% Optional dependencies for obs-studio    libfdk-aac: FDK AAC codec support [installed]    libva-intel-driver: hardware encoding    libva-mesa-driver: hardware encoding [installed]    luajit: scripting support [installed]    python: scripting support [installed]    sndio: Sndio input client [installed]    v4l2loopback-dkms: virtual camera support :: Running post-transaction hooks... (1/4) Arming ConditionNeedsUpdate... (2/4) Updating icon theme caches... (3/4) Updating the desktop file MIME type cache... (4/4) Performing snapper post snapshots for the following configurations... ==> root: 199 ~ 18s ❯

### ASSISTANT
Now run:

```bash
kbuildsycoca6
```

Then open your launcher and check Multimedia — OBS should be there now.

### HUMAN
still no but when i search it is shows up. still not in apptray

### ASSISTANT
At least it launches now when you click it from search. Let's verify the desktop file is back:

```bash
ls /usr/share/applications/com.obsproject.Studio.desktop
```

### HUMAN
❯ ls __/usr/share/applications/____com.obsproject.Studio____.desktop__ .rw-r--r-- 9.4k root 18 Jan 05:52  /usr/share/applications/com.obsproject.Studio.desktop ~ ❯

### ASSISTANT
File is there. At this point I strongly suspect this is just a quirk of the Application Launcher widget on your setup — it may simply not be showing the Multimedia category entries properly.

Try switching to Kickoff launcher temporarily to see if OBS shows up there. Right-click your taskbar > Add Widgets, search for "Kickoff" and add it. If OBS appears in Kickoff under Multimedia, then it's just an Application Launcher rendering bug and you can either stick with Kickoff or live with finding OBS via search.

### HUMAN
cant i add obs into my app tray?

### ASSISTANT
Yes! Right-click the launcher > Edit Applications (or open kmenuedit from search). Find OBS Studio under Multimedia, then you can pin it to your taskbar by right-clicking it in search results and selecting "Pin to Task Manager", or just add it as a favorite so it appears in the launcher's favorites section.

The quickest way: search for OBS in your launcher, then right-click it and select "Add to Favorites" — it'll show up in the favorites/pinned section of your launcher permanently.

### HUMAN
no i mean like manually add it back into the app tray

### ASSISTANT
Right-click the OBS icon in your taskbar while it's running, then select "Pin to Taskbar" — that'll keep it there permanently.

If you want to add it without launching it first, right-click an empty spot on your taskbar > Add Widgets > search for "Application name" or just drag it from the launcher search results onto the taskbar.

### HUMAN
i want it to be under the multimedia section is what i mean. i want to manually add it since it only shows up in search

### ASSISTANT
Open kmenuedit:

```bash
kmenuedit
```

Navigate to Multimedia, then click "New Item", and fill in:
- **Name:** OBS Studio
- **Command:** obs
- **Icon:** com.obsproject.Studio

Save and it should appear under Multimedia in your launcher.

### HUMAN
how do i point the exe to it so it launches when i choose to launch it that way ?

### ASSISTANT
In the Command field just put `obs` — that's the binary name and it's in your PATH now that it's properly installed. So just:

- **Command:** `obs`

That's it, no full path needed.
