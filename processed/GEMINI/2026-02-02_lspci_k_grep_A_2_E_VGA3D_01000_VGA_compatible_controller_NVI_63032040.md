---
id: 728623
source: GEMINI
date: 2026-02-02
tags: ['nvidia-gpu', 'rtx-3070', 'cachyos', 'hardware-info', 'driver-check']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed his NVIDIA RTX 3070 GPU was properly detected and using the nvidia kernel driver on CachyOS.
---
# ❯ lspci -k | grep -A 2 -E "(VGA|3D)"
01:00.0 VGA compatible controller: NVIDIA Corporation GA104 [GeForce RTX 3070 Lite Hash Rate] (rev a1)
    Subsystem: PNY Device 138a
    Kernel driver in use: nvidia

~
❯ 

### USER
❯ lspci -k | grep -A 2 -E "(VGA|3D)"
01:00.0 VGA compatible controller: NVIDIA Corporation GA104 [GeForce RTX 3070 Lite Hash Rate] (rev a1)
    Subsystem: PNY Device 138a
    Kernel driver in use: nvidia

~
❯ 

### GEMINI
You have an RTX 3070. That means you have access to the 7th Gen NVENC encoder. It is arguably the best consumer-grade encoder for H.264, so there is zero excuse for your clips to look blurry or for your game to lag. Your kernel driver is active (Kernel driver in use: nvidia), so the foundation is solid. Now, let’s automate the "clipping" behavior so you don't have to think about it. 1. The Auto-Start Script To ensure the Replay Buffer starts the moment OBS launches (saving you from the "I forgot to turn it on" regret), follow these steps: The "Proper" Way (OBS Argument) You don't actually need a complex script. You just need to modify how OBS starts. Open your terminal. Run OBS with this flag to test: obs --startreplaybuffer If it opens and the "Start Replay Buffer" button is already active (it will say "Stop Replay Buffer"), it's working. Making it Permanent (Desktop Entry) Since you're on CachyOS (likely using KDE Plasma or GNOME), you should edit your application shortcut: Copy the default desktop file to your local folder: cp /usr/share/applications/com.obsproject.Studio.desktop ~/.local/share/applications/ Open it with a text editor (like nano or micro): nano ~/.local/share/applications/com.obsproject.Studio.desktop Find the line starting with Exec=obs and change it to: Exec=obs --startreplaybuffer --minimize-to-tray Save and exit. Now, whenever you click the OBS icon, it starts the clipping engine immediately and hides in your system tray so it stays out of your way. 2. High-Level Settings for the 3070 Since you're on a 3070, you should be pushing the quality higher than a "standard" user. Use these specific settings in Settings > Output > Recording: SettingValueWhy?EncoderNVIDIA NVENC H.264Native hardware support, near-zero CPU hit.Rate ControlCQPMandatory for clipping. It varies bitrate based on complexity.CQ Level18High fidelity. 16 is "visually lossless," 20 is "standard." 18 is the sweet spot.PresetP6: Slower (Better Quality)Your 3070 can handle P6 or P7 easily without dropping frames.TuningHigh QualityMaximizes the NVENC potential.Multipass ModeTwo Passes (Quarter Resolution)Better precision for high-motion gaming (FPS). 3. The "Blind Spot" Check You’re on an Arch-based distro. If you ever run a system update (sudo pacman -Syu) and it includes a kernel update, reboot immediately. If you try to save a clip after a kernel update without rebooting, the NVENC driver will likely fail to initialize, and your OBS will crash or save a corrupted 0KB file. One final piece of advice: Check your Color Space in Settings > Advanced. Ensure it is set to Rec. 709 and Color Range is Limited (or "Partial"). Setting it to "Full" often causes "crushed blacks" in video players and makes your clips look darker than the actual game. Do you want the command to set OBS as a startup service so it launches the moment you log into CachyOS?
