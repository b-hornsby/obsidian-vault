---
id: 541809
source: GEMINI
date: 2026-02-02
tags: ['linux', 'desktop-entry', 'autostart', 'yeti-microphone', 'udev-rules']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating a desktop entry to automatically run a script to reset his Yeti microphone on boot, but encounters an error in the fish shell.
---
# ran that command and got this: ❯ mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
  [Desktop Entry]
  Type=Application
  Exec=/usr/local/bin/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Fix
  Comment=Resets the Blue Yeti USB bus
  EOF
fish: Expected a string, but found a redirection
mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
                                     ^
~
❯ mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
  [Desktop Entry]
  Type=Application
  Exec=/usr/local/bin/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Fix
  Comment=Resets the Blue Yeti USB bus
  EOF

### USER
ran that command and got this: ❯ mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
  [Desktop Entry]
  Type=Application
  Exec=/usr/local/bin/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Fix
  Comment=Resets the Blue Yeti USB bus
  EOF
fish: Expected a string, but found a redirection
mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
                                     ^
~
❯ mkdir -p ~/.config/autostart && cat <<EOF > ~/.config/autostart/yeti-fix.desktop
  [Desktop Entry]
  Type=Application
  Exec=/usr/local/bin/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Fix
  Comment=Resets the Blue Yeti USB bus
  EOF

### GEMINI
Ah, the Fish shell. It’s fast and pretty, but it hates "here-docs" (<<EOF). It's trying to be helpful by complaining about the redirection, but it's just blocking progress. Since Fish handles strings differently, let's use a standard printf command that works across all shells to create that autostart file. 1. Create the Autostart File (Fish-Compatible) Copy and paste this single line into your terminal: printf "[Desktop Entry]\nType=Application\nExec=/usr/local/bin/reset_yeti.sh\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName=Yeti Fix\nComment=Resets the Blue Yeti USB bus\n" > ~/.config/autostart/yeti-fix.desktop 2. Verify it’s there Run this to make sure the file was created and looks right: cat ~/.config/autostart/yeti-fix.desktop 3. The Advisor's Final Audit Before you pull the trigger on a reboot, let's look at your BIOS photos again. Image 1 (CPU Settings): You have Enhanced C-states set to Enabled. Change this to Disabled. These power states cause tiny voltage fluctuations on the 5V rail that can "stroke out" a Blue Yeti. Image 2 (Onboard Devices): You have USB power delivery in Soft Off state (S5) set to Enabled. Change this to Disabled. As I said before, the Yeti needs to lose power completely when you shut down so it can reset its own internal "brain." The Strategy Run the printf command above. Go into BIOS and fix those two settings (Disable C-states and Disable S5 USB Power). Reboot. Once you log in, count to 10. If the Yeti light is solid and it shows up in your sound settings, you have successfully automated a hardware bypass. Would you like me to show you how to check the systemd journal after you reboot to see if the script actually fired?
