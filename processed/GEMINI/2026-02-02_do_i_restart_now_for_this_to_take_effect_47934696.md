---
id: 464469
source: GEMINI
date: 2026-02-02
tags: ['system-configuration', 'restart-required', 'linux-administration']
category: general
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is asking if a system restart is required for recent configuration changes to take effect.
---
# do i restart now for this to take effect

### USER
do i restart now for this to take effect

### GEMINI
You don't need to restart the whole computer just to test the visudo change, but you should restart once to verify the whole "automated fix" actually works when you aren't there to hold its hand. The Final Verification Sequence Test the "No Password" fix first: Run ~/reset_yeti.sh in your terminal right now. If it runs and returns to the prompt without asking for your password, the visudo change is successful. If it asks for a password, we need to double-check the spelling in sudo EDITOR=nano visudo. Add to Autostart (Before you reboot): The script won't run itself on boot unless you tell your Desktop Environment to do it. If you are on GNOME: Search for "Startup Applications" in your app menu and add ~/reset_yeti.sh. If you are on KDE: Go to "System Settings" -> "Autostart" and add the script there. The "Moment of Truth" Reboot: Now, Restart. Don't touch the cable. Log in. Wait about 10 seconds (because of the sleep 5 we put in the script). Check your sound settings. If it works: Congratulations. You’ve successfully outsmarted 15-year-old hardware by building a digital ghost that "unplugs and replugs" the mic for you every time you turn on the PC. If it still fails: The only stone left unturned is the physical one. If an electronic usbreset can't wake it up, but a physical pull can, it means the Yeti is suffering from a capacitance issue—it's holding onto just enough electricity from the motherboard to stay "frozen" instead of resetting. In that case, the BIOS "S5 Power" setting being Disabled is your only remaining prayer. Reboot now. When you get back in, is the Yeti's red light solid and is it showing up in your volume mixer?
