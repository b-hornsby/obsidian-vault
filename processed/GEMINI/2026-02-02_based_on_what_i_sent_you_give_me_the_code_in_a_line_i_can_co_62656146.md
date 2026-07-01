---
id: 783572
source: GEMINI
date: 2026-02-02
tags: ['copy-paste-code', 'one-liner', 'scripting']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted a single copy-paste command line based on previously shared context to execute a task.
---
# based on what i sent you give me the code in a line i can copy/paste

### USER
based on what i sent you give me the code in a line i can copy/paste

### GEMINI
To get the Kernel Quirk into Limine so it survives updates, you need to run these three commands in order. This will append the fix to your existing configuration and then force Limine to rebuild the boot menu. 1. Add the Quirk Copy and paste this line. It uses sed to find your KERNEL_CMDLINE[default] and inject the Yeti fix right before the closing quote: sudo sed -i 's/KERNEL_CMDLINE\[default\]="\(.*\)"/KERNEL_CMDLINE[default]="\1 usbcore.quirks=046d:0ab7:k"/' /etc/default/limine 2. Update the Bootloader Now, you must tell CachyOS to take that change and write it into the actual boot files: sudo limine-mkinitcpio 3. Verify the Change Run this to make sure the file looks correct (the quirk should be at the end of the line): grep "KERNEL_CMDLINE" /etc/default/limine The "Why this works" (Advisor's Note) The Quirk (:k): This is the "LPM-disable" flag. Modern Linux kernels try to use Link Power Management to save tiny amounts of electricity. The Blue Yeti's controller is too old to understand these signals and essentially "shuts the door" and locks it, requiring a physical power pull to reset. The Command: By putting this in /etc/default/limine, you are hard-coding a rule into the kernel: "When you see this specific device ID, do not try to be smart with power management." Final Strategic Move If you reboot and it still requires a replug: Go to BIOS. DISABLE "USB power delivery in Soft Off state (S5)". Why? If the Yeti stays "half-powered" while the PC is off, it stays in its crashed state. Disabling S5 power kills the Yeti's "memory" so it has to start fresh when you hit the power button. Reboot now and let me know: Does the mic work immediately after the CachyOS logo disappears?
