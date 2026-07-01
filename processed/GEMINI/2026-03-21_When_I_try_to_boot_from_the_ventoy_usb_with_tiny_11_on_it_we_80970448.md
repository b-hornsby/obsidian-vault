---
id: 374378
source: GEMINI
date: 2026-03-21
tags: ['ventoy', 'tiny11', 'usb-boot', 'windows-installation']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is trying to boot Tiny11 from a Ventoy USB and encountering an error.
---
# When I try to boot from the ventoy usb with tiny 11 on it we get this:

### USER
When I try to boot from the ventoy usb with tiny 11 on it we get this:

### GEMINI
This is the final hurdle: Ventoy itself isn't signed by Microsoft, so the BIOS bouncer is blocking the USB stick because Secure Boot is still on. Since you're doing a "Nuclear" fresh start, we can temporarily lower the gate to let the installer in. The "Bypass" Sequence Enter BIOS (F2/Del). Disable Secure Boot. (Just for this 15-minute installation process). Boot from the Ventoy USB. It will work perfectly now. Perform the "Purge": Delete all partitions until you have that beautiful 1863 GB Unallocated Space and click Next. Let Windows Install. It will reboot a few times. The "Ops" Post-Game (Critical for Valorant) Once you reach the Tiny 11 desktop and everything is set up: Reboot back into BIOS. Enable Secure Boot. 3. Restore/Reset Factory Keys. (Since we're done with Linux, you want the standard Microsoft keys to be active so Valorant's Vanguard doesn't flag your system as "untrusted"). Save and Exit. Why this works Windows (Tiny 11) is officially signed by Microsoft. Unlike Linux or Ventoy, it has a "VIP Pass" that the BIOS recognizes by default. Once it's installed, you can turn Secure Boot back on and it will boot flawlessly while keeping the Valorant anti-cheat happy. Go ahead and kill those partitions—let me know when you're sitting on a clean 2TB "C:" drive.
