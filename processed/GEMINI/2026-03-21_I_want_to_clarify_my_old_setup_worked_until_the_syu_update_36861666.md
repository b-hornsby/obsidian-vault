---
category: homelab
date: 2026-03-21
id: 723403
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is emphasizing that his system was working correctly before a recent
  system update (syu) caused issues.
tags:
- system-stability
- syu-update
- regression
- software-update
---
# I want to clarify my old setup worked until the syu update

### USER
I want to clarify my old setup worked until the syu update

### GEMINI
I hear you, and that makes total sense. Here is the blunt reality of why it worked before and why it’s "broken" now: When you first set up Minegrub and Secure Boot, you enrolled the specific digital signatures (hashes) of your GRUB bootloader and your Linux kernel into your BIOS. Your BIOS basically had a "VIP list," and those specific files were on it. What the -Syu update actually did: It replaced the files: The update downloaded a new version of the CachyOS kernel and updated the GRUB binaries. The "VIP List" is now invalid: Even a 1KB change to the kernel changes its digital signature. To your BIOS, the "new" kernel looks like a completely different, untrusted file. It doesn't care that the filename is the same; the "fingerprint" is different. The Limine Invasion: CachyOS recently moved toward Limine. The update didn't just refresh your files; it tried to install a whole new bootloader (Limine) which took over the #1 boot priority, which is why you saw that blue screen first. How to get back to "Exactly how it was": You don't have to reinvent the wheel, but you do have to update the BIOS's "VIP list" because the old entries are now useless. Since you are back in Minegrub (with Secure Boot OFF), do this right now to fix it for Valorant: Re-sign the files using sbctl (as I laid out in the last step). This is the modern, automated way to keep that "VIP list" updated so you don't have to manually click through BIOS menus every time there’s a kernel update. Or, manually re-enroll in BIOS: If you prefer the manual way, you have to go back into the BIOS and Enroll EFI Image again, picking the new grubx64.efi and the new vmlinuz-linux-cachyos. The Opportunity Cost: If you don't use a tool like sbctl, every single time you run pacman -Syu and get a kernel update in the future, you are going to run into this exact same "Secure Boot Violation." sbctl includes a "hook" that automatically signs the new files every time you update, so you never have to deal with this red box again. Shall we run the sbctl commands now so this update-breakage stops happening for good?
