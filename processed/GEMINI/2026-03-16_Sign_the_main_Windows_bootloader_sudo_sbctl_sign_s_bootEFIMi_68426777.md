---
id: 053468
source: GEMINI
date: 2026-03-16
tags: ['secure-boot', 'sbctl', 'efi-signing', 'dual-boot']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan signed Windows and systemd bootloaders with sbctl for secure boot but found many unsigned EFI files remaining.
---
# ❯ # Sign the main Windows bootloader
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgfw.efi

  # Sign the secondary Windows manager
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgr.efi

  # Sign the memory test (sometimes checked during boot)
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/memtest.efi
✓ Signed /boot/EFI/Microsoft/Boot/bootmgfw.efi
✓ Signed /boot/EFI/Microsoft/Boot/bootmgr.efi
✓ Signed /boot/EFI/Microsoft/Boot/memtest.efi

~
❯ sudo sbctl sign -s /boot/EFI/systemd/systemd-bootx64.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/core.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/grub.efi
✓ Signed /boot/EFI/systemd/systemd-bootx64.efi
✓ Signed /boot/grub/x86_64-efi/core.efi
✓ Signed /boot/grub/x86_64-efi/grub.efi

~
❯ sudo sbctl verify | grep "is not signed" | grep ".efi"
✗ /boot/EFI/GRUB/grubx64.efi is not signed
✗ /boot/EFI/Microsoft/Boot/SecureBootRecovery.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-GB/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-GB/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-MX/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-MX/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/et-EE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/et-EE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-CA/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-CA/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hr-HR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hr-HR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/qps-ploc/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/qps-plocm/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ro-RO/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ro-RO/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sk-SK/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sk-SK/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sl-SI/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sl-SI/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sr-Latn-RS/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sr-Latn-RS/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/uk-UA/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/uk-UA/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/memtest.efi.mui is not signed

~
❯ 

### USER
❯ # Sign the main Windows bootloader
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgfw.efi

  # Sign the secondary Windows manager
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgr.efi

  # Sign the memory test (sometimes checked during boot)
  sudo sbctl sign -s /boot/EFI/Microsoft/Boot/memtest.efi
✓ Signed /boot/EFI/Microsoft/Boot/bootmgfw.efi
✓ Signed /boot/EFI/Microsoft/Boot/bootmgr.efi
✓ Signed /boot/EFI/Microsoft/Boot/memtest.efi

~
❯ sudo sbctl sign -s /boot/EFI/systemd/systemd-bootx64.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/core.efi
  sudo sbctl sign -s /boot/grub/x86_64-efi/grub.efi
✓ Signed /boot/EFI/systemd/systemd-bootx64.efi
✓ Signed /boot/grub/x86_64-efi/core.efi
✓ Signed /boot/grub/x86_64-efi/grub.efi

~
❯ sudo sbctl verify | grep "is not signed" | grep ".efi"
✗ /boot/EFI/GRUB/grubx64.efi is not signed
✗ /boot/EFI/Microsoft/Boot/SecureBootRecovery.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/cs-CZ/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/da-DK/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/de-DE/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/el-GR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-GB/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-GB/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/en-US/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-ES/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-MX/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/es-MX/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/et-EE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/et-EE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fi-FI/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-CA/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-CA/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/fr-FR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hr-HR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hr-HR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/hu-HU/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/it-IT/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ja-JP/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nb-NO/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/nl-NL/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pl-PL/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-BR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/pt-PT/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/qps-ploc/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/qps-plocm/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ro-RO/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ro-RO/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ru-RU/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sk-SK/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sk-SK/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sl-SI/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sl-SI/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sr-Latn-RS/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sr-Latn-RS/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/sv-SE/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/tr-TR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/uk-UA/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/uk-UA/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-CN/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/zh-TW/memtest.efi.mui is not signed

~
❯ 

### GEMINI
That list is massive because it's flagging every language file and resource Windows has, but 99% of those are non-executable fluff that don't need signing. You’ve successfully signed the heavy hitters. The Final Culprit There is exactly one executable left in your list that could still trigger that red violation box: sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi Why you are ready now Linux Side: You’ve signed the CachyOS kernels, the Limine bootloader, and even the old GRUB/Systemd binaries just in case the BIOS probes them. Windows Side: You’ve signed the main bootmgfw.efi and bootmgr.efi. Even though your enrolled Microsoft keys should handle these, signing them with your own local key is the "nuclear option" that forces the BIOS to shut up and boot. The Moment of Truth Run the GRUB sign command above. Reboot and enter your BIOS. Enable Secure Boot (set to Windows UEFI Mode or Enabled). Save and Exit. If you see that Minecraft "Select World" screen, you’ve officially beaten the BIOS. You can then hop into Tiny11 and Valorant should finally be satisfied with your system's security status. Did that last GRUB file sign successfully? If so, it's time to flip the switch in the BIOS.
