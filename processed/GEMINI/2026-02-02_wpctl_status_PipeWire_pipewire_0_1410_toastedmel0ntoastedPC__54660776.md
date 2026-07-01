---
id: 655253
source: GEMINI
date: 2026-02-02
tags: ['pipewire', 'audio-routing', 'wpctl', 'linux-audio', 'audio-configuration']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
summary: Bryan ran `wpctl status` to inspect his PipeWire audio configuration, likely troubleshooting an audio issue.
---
# ❯ wpctl status
PipeWire 'pipewire-0' [1.4.10, toastedmel0n@toastedPC, cookie:1768516141]
 └─ Clients:
        32. WirePlumber                         [1.4.10, toastedmel0n@toastedPC, pid:3758]
        33. pipewire                            [1.4.10, toastedmel0n@toastedPC, pid:3760]
        34. GNOME Volume Control Media Keys     [1.4.10, toastedmel0n@toastedPC, pid:3547]
        47. WirePlumber [export]                [1.4.10, toastedmel0n@toastedPC, pid:3758]
        48. gnome-shell                         [1.4.10, toastedmel0n@toastedPC, pid:3405]
        49. GNOME Shell Volume Control          [1.4.10, toastedmel0n@toastedPC, pid:3405]
        50. xdg-desktop-portal                  [1.4.10, toastedmel0n@toastedPC, pid:4776]
        88. Chromium input                      [1.4.10, toastedmel0n@toastedPC, pid:6168]
        97. Steam Voice Settings                [1.4.10, toastedmel0n@toastedPC, pid:5066]
        98. Steam                               [1.4.10, toastedmel0n@toastedPC, pid:5066]
        99. LibreWolf                           [1.4.10, toastedmel0n@toastedPC, pid:7310]
       105. Chromium                            [1.4.10, toastedmel0n@toastedPC, pid:6168]
       107. Mutter                              [1.4.10, toastedmel0n@toastedPC, pid:3405]
       108. wpctl                               [1.4.10, toastedmel0n@toastedPC, pid:10802]
       117. LibreWolf                           [1.4.10, toastedmel0n@toastedPC, pid:7310]

Audio
 ├─ Devices:
 │      51. GA104 High Definition Audio Controller [alsa]
 │      52. C922 Pro Stream Webcam              [alsa]
 │      53. Blue Microphones                    [alsa]
 │      54. FiiO USB DAC-E10                    [alsa]
 │      55. Built-in Audio                      [alsa]
 │  
 ├─ Sinks:
 │  *   43. FiiO USB DAC-E10 Analog Stereo      [vol: 0.44]
 │      44. Blue Microphones Analog Stereo      [vol: 0.40]
 │      62. GA104 High Definition Audio Controller Digital Stereo (HDMI) [vol: 0.40]
 │      64. Built-in Audio Analog Stereo        [vol: 0.40]
 │  
 ├─ Sources:
 │  *   45. Blue Microphones Analog Stereo      [vol: 1.00]
 │      63. C922 Pro Stream Webcam Analog Stereo [vol: 0.53]
 │      65. Built-in Audio Analog Stereo        [vol: 1.00]
 │  
 ├─ Filters:
 │  
 └─ Streams:
       116. Chromium                                                    
            114. output_FL       > FiiO USB DAC-E10:playback_FL    [active]
            115. output_FR       > FiiO USB DAC-E10:playback_FR    [active]

Video
 ├─ Devices:
 │      35. C922 Pro Stream Webcam              [v4l2]
 │      46. C922 Pro Stream Webcam              [v4l2]
 │  
 ├─ Sinks:
 │  
 ├─ Sources:
 │  *   95. C922 Pro Stream Webcam (V4L2)      
 │  
 ├─ Filters:
 │  
 └─ Streams:

Settings
 └─ Default Configured Devices:
         0. Audio/Sink    alsa_output.usb-GuangZhou_FiiO_Electronics_Co._Ltd_FiiO_USB_DAC-E10-00.analog-stereo
         1. Audio/Source  alsa_input.usb-Generic_Blue_Microphones_2110BAB0K638-00.analog-stereo

~
❯ 

### USER
❯ wpctl status
PipeWire 'pipewire-0' [1.4.10, toastedmel0n@toastedPC, cookie:1768516141]
 └─ Clients:
        32. WirePlumber                         [1.4.10, toastedmel0n@toastedPC, pid:3758]
        33. pipewire                            [1.4.10, toastedmel0n@toastedPC, pid:3760]
        34. GNOME Volume Control Media Keys     [1.4.10, toastedmel0n@toastedPC, pid:3547]
        47. WirePlumber [export]                [1.4.10, toastedmel0n@toastedPC, pid:3758]
        48. gnome-shell                         [1.4.10, toastedmel0n@toastedPC, pid:3405]
        49. GNOME Shell Volume Control          [1.4.10, toastedmel0n@toastedPC, pid:3405]
        50. xdg-desktop-portal                  [1.4.10, toastedmel0n@toastedPC, pid:4776]
        88. Chromium input                      [1.4.10, toastedmel0n@toastedPC, pid:6168]
        97. Steam Voice Settings                [1.4.10, toastedmel0n@toastedPC, pid:5066]
        98. Steam                               [1.4.10, toastedmel0n@toastedPC, pid:5066]
        99. LibreWolf                           [1.4.10, toastedmel0n@toastedPC, pid:7310]
       105. Chromium                            [1.4.10, toastedmel0n@toastedPC, pid:6168]
       107. Mutter                              [1.4.10, toastedmel0n@toastedPC, pid:3405]
       108. wpctl                               [1.4.10, toastedmel0n@toastedPC, pid:10802]
       117. LibreWolf                           [1.4.10, toastedmel0n@toastedPC, pid:7310]

Audio
 ├─ Devices:
 │      51. GA104 High Definition Audio Controller [alsa]
 │      52. C922 Pro Stream Webcam              [alsa]
 │      53. Blue Microphones                    [alsa]
 │      54. FiiO USB DAC-E10                    [alsa]
 │      55. Built-in Audio                      [alsa]
 │  
 ├─ Sinks:
 │  *   43. FiiO USB DAC-E10 Analog Stereo      [vol: 0.44]
 │      44. Blue Microphones Analog Stereo      [vol: 0.40]
 │      62. GA104 High Definition Audio Controller Digital Stereo (HDMI) [vol: 0.40]
 │      64. Built-in Audio Analog Stereo        [vol: 0.40]
 │  
 ├─ Sources:
 │  *   45. Blue Microphones Analog Stereo      [vol: 1.00]
 │      63. C922 Pro Stream Webcam Analog Stereo [vol: 0.53]
 │      65. Built-in Audio Analog Stereo        [vol: 1.00]
 │  
 ├─ Filters:
 │  
 └─ Streams:
       116. Chromium                                                    
            114. output_FL       > FiiO USB DAC-E10:playback_FL    [active]
            115. output_FR       > FiiO USB DAC-E10:playback_FR    [active]

Video
 ├─ Devices:
 │      35. C922 Pro Stream Webcam              [v4l2]
 │      46. C922 Pro Stream Webcam              [v4l2]
 │  
 ├─ Sinks:
 │  
 ├─ Sources:
 │  *   95. C922 Pro Stream Webcam (V4L2)      
 │  
 ├─ Filters:
 │  
 └─ Streams:

Settings
 └─ Default Configured Devices:
         0. Audio/Sink    alsa_output.usb-GuangZhou_FiiO_Electronics_Co._Ltd_FiiO_USB_DAC-E10-00.analog-stereo
         1. Audio/Source  alsa_input.usb-Generic_Blue_Microphones_2110BAB0K638-00.analog-stereo

~
❯ 

### GEMINI
Look at your wpctl status output. Your Yeti is actually there and even set as the default source (indicated by the * next to ID 45). If you still have to unplug and replug it to get it to work, the hardware is "alive" but the software stream is deadlocked. This is almost always caused by PipeWire or WirePlumber putting the device into a "suspend" state from which the Yeti’s ancient firmware cannot wake up. We are going to kill that "suspend" feature for your Yeti specifically. 1. The WirePlumber "Never Sleep" Hack Since CachyOS uses WirePlumber 1.4+, we need to create a specific configuration file to prevent the mic from timing out. Create the directory: mkdir -p ~/.config/wireplumber/wireplumber.conf.d/ Create the config file: nano ~/.config/wireplumber/wireplumber.conf.d/51-yeti-fix.conf Paste this exact block into the file: monitor.alsa.rules = [ { matches = [ { node.name = "~alsa_input.usb-Generic_Blue_Microphones.*" } ] actions = { update-props = { session.suspend-timeout-seconds = 0 } } } ] Save and Exit: Ctrl+O, Enter, Ctrl+X. 2. Restart the Audio Services You don't need to reboot. Just run: systemctl --user restart wireplumber The Advisor's Cold Reality Look at your Streams section in the wpctl output. Your Chromium audio is routing through the FiiO DAC. Meanwhile, your Yeti is sitting as a Source but has no active stream. The Yeti is notorious for a "ghosting" bug where it reports as available to the OS, but the internal buffer is frozen because the USB bus was reset during boot. Your final homework to ensure this "always" works: The Physical Move: You have 11 devices on Bus 001. I cannot stress this enough—move the FiiO DAC and the Webcam to the Blue/Red ports. They are currently choking the bandwidth that the Yeti needs for its initial handshake. The Kernel Module Reset: If the Yeti ever fails again, don't reach for the cable. Run this command instead: sudo modprobe -r snd_usb_audio && sudo modprobe snd_usb_audio If that command fixes it, it proves the issue is the Linux driver handshake, not your physical port. Do you want me to write a small "Auto-Fix" script for you that runs that driver reset automatically every time you log in?
