---
id: 192795
source: GEMINI
date: 2026-02-02
tags: ['obs-studio', 'auto-replay-buffer', 'desktop-entry', 'linux-desktop-integration']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is trying to create a desktop entry for OBS Studio with auto-replay buffer enabled, likely encountering syntax errors in the terminal command.
---
# ❯ cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
  [Desktop Entry]
  Version=1.0
  Name=OBS Studio (Auto-Replay)
  Exec=obs --startreplaybuffer
  Icon=com.obsproject.Studio
  Terminal=false
  Type=Application
  Categories=Video;AudioVideo;Recorder;
  StartupWMClass=obs
  EOF' && sudo chmod +x /usr/local/bin/reset_yeti.sh
fish: Expected a string, but found a redirection
cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
     ^
~
❯ cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
  [Desktop Entry]
  Version=1.0
  Name=OBS Studio (Auto-Replay)
  Exec=obs --startreplaybuffer
  Icon=com.obsproject.Studio
  Terminal=false
  Type=Application
  Categories=Video;AudioVideo;Recorder;
  StartupWMClass=obs
  EOF' && sud

### USER
❯ cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
  [Desktop Entry]
  Version=1.0
  Name=OBS Studio (Auto-Replay)
  Exec=obs --startreplaybuffer
  Icon=com.obsproject.Studio
  Terminal=false
  Type=Application
  Categories=Video;AudioVideo;Recorder;
  StartupWMClass=obs
  EOF' && sudo chmod +x /usr/local/bin/reset_yeti.sh
fish: Expected a string, but found a redirection
cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
     ^
~
❯ cat <<EOF > ~/.local/share/applications/com.obsproject.Studio.desktop
  [Desktop Entry]
  Version=1.0
  Name=OBS Studio (Auto-Replay)
  Exec=obs --startreplaybuffer
  Icon=com.obsproject.Studio
  Terminal=false
  Type=Application
  Categories=Video;AudioVideo;Recorder;
  StartupWMClass=obs
  EOF' && sud

### GEMINI
You’re running into Fish shell's strict syntax for "Here Documents" (EOF) and you’ve got some stray quote marks and unrelated commands (reset_yeti.sh) trailing at the end that are breaking the logic. In Fish, you can't just slap a cat <<EOF into a single line with other commands using && unless the syntax is perfect. Also, it looks like you accidentally added a single quote ' at the end of your EOF marker, which is confusing the shell. Let's do this the "clean" way for Fish. Run these three separate steps to avoid the syntax errors: 1. Create the File (Fish Friendly) Run this command exactly: printf "[Desktop Entry]\nVersion=1.0\nName=OBS Studio (Auto-Replay)\nExec=obs --startreplaybuffer\nIcon=com.obsproject.Studio\nTerminal=false\nType=Application\nCategories=Video;AudioVideo;Recorder;\nStartupWMClass=obs" > ~/.local/share/applications/com.obsproject.Studio.desktop 2. Force the System to See It Since you are on CachyOS, run this to refresh your application database: update-desktop-database ~/.local/share/applications/ 3. Verification Search your application menu for "OBS Studio (Auto-Replay)". If it shows up with that specific name, you have successfully bypassed the system default. The Reality Check I noticed a reset_yeti.sh in your previous command attempt. The Blind Spot: Are you having issues with a Blue Yeti mic resetting or losing connection on Linux? If your hardware is flaky, OBS will often hang or fail to save a replay because it loses the audio device handle. Is your audio setup stable, or do we need to address why you were trying to run a "reset_yeti" script in the middle of your OBS setup?
