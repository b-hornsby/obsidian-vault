---
category: homelab
date: 2026-03-21
id: 876207
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is encountering a new issue after attempting a fix, related to secure
  boot on his Tiny11 installation, which he needs for Valorant.
tags:
- secure-boot
- tiny11
- valorant
- boot-issues
---
# Did that and now this? I had secure boot set up on my tiny 11 side for valorant

### USER
Did that and now this? I had secure boot set up on my tiny 11 side for valorant

### GEMINI
This is the classic "Secure Boot vs. Linux" collision. Because you just reinstalled GRUB, your BIOS sees it as an "unauthorized change" because the new GRUB bootloader isn't signed with a key the motherboard trusts. Since you need Secure Boot for Valorant, simply turning it off isn't a long-term solution. You have to make the motherboard trust your new GRUB. The Fix: Enroll the GRUB key (MOK) Most modern motherboards (especially if you're on a 12700K system) allow you to "Enroll" a trusted key from your EFI partition. Click OK on that red "Secure Boot Violation" screen to enter the BIOS. Navigate to the Security or Boot tab and look for Secure Boot settings. Look for an option called "Key Management" or "Enroll EFI Image". Navigate through your drive partitions (it usually looks like a file explorer). You are looking for: EFI -> GRUB -> grubx64.efi Select that file and choose "Trust" or "Enroll". Give it a name like "CachyGRUB" if it asks. Save and Exit. If your BIOS doesn't have an "Enroll" button: You have to do the "PreLoader" or "Shim" dance, but let's try the BIOS enrollment first as it's the cleanest way to keep Valorant happy. Brutally Honest Warning: Valorant's Vanguard is incredibly picky. If you can't get the BIOS to trust the GRUB file directly, you might have to temporarily Disable Secure Boot just to get back into Linux, then we can set up a "Signed Shim" that Valorant and Linux both agree on. Does your BIOS have an "Enroll EFI Image" or "Key Management" option available?
