---
id: 876345
source: GEMINI
date: 2026-02-02
tags: ['kernel-parameters', 'boot-configuration', 'limine', 'linux', 'command-output']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is providing the output of a grep command on his Limine boot configuration file, likely as part of troubleshooting a boot-related issue.
---
# it still says ❯ grep "KERNEL_CMDLINE" /etc/default/limine
KERNEL_CMDLINE[default]+="quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 usbcore.autosuspend=-1"

~
❯ 

### USER
it still says ❯ grep "KERNEL_CMDLINE" /etc/default/limine
KERNEL_CMDLINE[default]+="quiet nowatchdog splash rw rootflags=subvol=/@ root=UUID=dab63c75-0142-4154-abed-4915a693f699 usbcore.autosuspend=-1"

~
❯ 

### GEMINI
The reason my previous command didn't work is that your CachyOS setup uses the += operator in Limine. This means it appends new settings to the default ones. We just need to add our quirk to that existing list correctly. Run these two commands exactly as written: 1. Add the Quirk to your Limine file This command looks for that specific line in your file and adds the Yeti fix to the end of the list inside the quotes. sudo sed -i '/KERNEL_CMDLINE\[default\]+=/ s/"$/ usbcore.quirks=046d:0ab7:k"/' /etc/default/limine 2. Force the update to the bootloader You must run this to "bake" the change into your actual boot menu: sudo limine-mkinitcpio How to verify it worked (The "No Lies" check) After you run those, run this command: grep "KERNEL_CMDLINE" /etc/default/limine It should now look like this: KERNEL_CMDLINE[default]+="... usbcore.autosuspend=-1 usbcore.quirks=046d:0ab7:k" The Brutal Reality Check If you reboot and the mic still needs a replug, it is because your motherboard is keeping the Yeti "half-alive" in its crashed state while the PC is off. Your absolute final step: Go into BIOS. Go to Advanced -> Onboard Devices Configuration. Set USB power delivery in Soft Off state (S5) to DISABLED. This forces the Yeti to lose power completely when you shut down, which clears its tiny, stuck brain so it can start fresh when CachyOS boots up with the new "Quirk" we just added. Reboot and check cat /proc/cmdline. If you see the quirk there, but the mic is still dead, did you turn off that S5 power in BIOS?
