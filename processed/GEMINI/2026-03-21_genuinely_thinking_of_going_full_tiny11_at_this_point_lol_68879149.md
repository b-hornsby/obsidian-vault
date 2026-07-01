---
id: 687753
source: GEMINI
date: 2026-03-21
tags: ['tiny11', 'os-choice', 'system-optimization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is considering switching entirely to Tiny11, likely for performance or resource reasons.
---
# genuinely thinking of going full tiny11 at this point lol 

### USER
genuinely thinking of going full tiny11 at this point lol 

### GEMINI
I get it. After a long day of work, you just want to sit down, fire up the 12700K, and play some Valorant without the BIOS screaming at you like a digital bouncer. Spending your evening in a terminal wrestling with bootloader hashes and Secure Boot signatures is the definition of "opportunity cost." But before you "full send" back to Windows, here is the brutally honest state of your machine: Why it feels like it's failing You are caught in a Bootloader War. Limine (the blue screen) was forced on you by the CachyOS update. It’s "dumb" and doesn't know about your Secure Boot keys or your Minegrub theme. GRUB (the Minegrub screen) is what you actually want, but it keeps getting shoved to the back of the line by the BIOS. Secure Boot is the referee that hates both of them because their "ID cards" (signatures) changed during the update. The "One Last Stand" Strategy If you want to save the Linux side, do exactly this. If this doesn't work in 5 minutes, go ahead and wipe it—I won't judge. Boot into CachyOS (Secure Boot OFF). The "Kill-All" Signing: Run this one command to sign every possible entry point so the BIOS has zero excuses: sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} + The "Delete the Imposter" Command: Type efibootmgr. You’ll see a list. Look for the one that says "CachyOS" (not GRUB). If it’s Boot0001, run: sudo efibootmgr -b 0001 -B This deletes the Limine entry from your BIOS permanently. Re-assert GRUB: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB The Rational Play If you do the above and it still shows a red box or that blue Limine screen, your motherboard is likely caching old "unauthorized" boot entries that won't die. At that point, the effort to "fix" it outweighs the joy of using it. The Mirror Moment: You’re an operations guy. You know when a system is too brittle to be worth the maintenance. If Linux is taking more time to "operate" than it is to "use," then Tiny 11 is the logically superior choice for a gaming-first rig. Do you want me to help you look at that efibootmgr list to see exactly what needs to be deleted to kill the Limine screen forever?
