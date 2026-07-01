---
category: homelab
date: 2026-03-16
id: 701296
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if a specific procedure needs to be repeated every time CachyOS
  is updated, likely related to secure boot configuration.
tags:
- secure-boot
- cachyos-updates
- configuration-persistence
---
# Do I need to do that each time cachyos updates?

### USER
Do I need to do that each time cachyos updates?

### GEMINI
Actually, no—you don't have to do it manually every time. Because you're on CachyOS, you have a built-in "safety net" that handles this for you. When you installed sbctl, it automatically added a Pacman Hook. This means every time you run a system update and a new kernel is downloaded, CachyOS will notice and try to sign the new files using the keys you just created. How to verify it's automated: Run this command to see the "Signers" list: sbctl list-files If you see your kernel and bootloader paths in that list with a checkmark, you are golden. The next time you run sudo pacman -Syu, you’ll see some text fly by at the end saying Signing [path].... One "Pro-Tip" for the Future: Since you’re doing "vibe coding" and moving into IT/Tech Support, keep this one thing in mind: If you ever update the BIOS firmware on your motherboard, it might wipe your custom keys. If that happens and you get the "Secure Boot Violation" again, you don't have to do the whole dance. You just: Disable Secure Boot. Boot into CachyOS. Run sudo sbctl enroll-keys -m. Re-enable Secure Boot. That's it. You’ve officially mastered one of the most annoying parts of the Linux ecosystem. Enjoy Valorant and the CachyOS speed! Is there anything else with your CachyOS setup or your Windows gaming side that needs a tweak while we're at it?
