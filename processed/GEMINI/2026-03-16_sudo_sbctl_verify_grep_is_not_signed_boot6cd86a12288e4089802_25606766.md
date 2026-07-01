---
id: 043312
source: GEMINI
date: 2026-03-16
tags: ['sbctl', 'secure-boot-audit', 'unsigned-files', 'microsoft-boot']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan filtered sbctl verify output to identify all unsigned EFI files that needed signing.
---
# ❯ sudo sbctl verify | grep "is not signed"
✗ /boot/6cd86a12288e4089802591bd1a9a39ce/limine_history/vmlinuz-linux-cachyos-lts_sha256_7dcde488be59236bd26287be25d40bcefc36269e524a00e0d1dc39d9563
e0075 is not signed
✗ /boot/6cd86a12288e4089802591bd1a9a39ce/limine_history/vmlinuz-linux-cachyos_sha256_3c2b8d41d6095ee6a7f19b18b4eee7fadb4973f7fe0294e5ba6c41a31ca1e7c
b is not signed
✗ /boot/EFI/GRUB/grubx64.efi is not signed
✗ /boot/EFI/Microsoft/Boot/Resources/bootres.dll is not signed
✗ /boot/EFI/Microsoft/Boot/Resources/en-US/bootres.dll.mui is not signed
✗ /boot/EFI/Microsoft/Boot/SecureBootRecovery.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bootmgfw.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bootmgr.efi is not signed
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
✗ /boot/EFI/Microsoft/Boot/kd_02_10df.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_10ec.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1137.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1414.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_14e4.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_15ad.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_15b3.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1969.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_19a2.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1af4.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1d0f.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_8086.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_07_1415.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_0C_8086.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kdnet_uart16550.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kdstub.dll is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/memtest.efi is not signed
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
✗ /boot/EFI/systemd/systemd-bootx64.efi is not signed
✗ /boot/grub/x86_64-efi/core.efi is not signed
✗ /boot/grub/x86_64-efi/grub.efi is not signed

~
❯ 

### USER
❯ sudo sbctl verify | grep "is not signed"
✗ /boot/6cd86a12288e4089802591bd1a9a39ce/limine_history/vmlinuz-linux-cachyos-lts_sha256_7dcde488be59236bd26287be25d40bcefc36269e524a00e0d1dc39d9563
e0075 is not signed
✗ /boot/6cd86a12288e4089802591bd1a9a39ce/limine_history/vmlinuz-linux-cachyos_sha256_3c2b8d41d6095ee6a7f19b18b4eee7fadb4973f7fe0294e5ba6c41a31ca1e7c
b is not signed
✗ /boot/EFI/GRUB/grubx64.efi is not signed
✗ /boot/EFI/Microsoft/Boot/Resources/bootres.dll is not signed
✗ /boot/EFI/Microsoft/Boot/Resources/en-US/bootres.dll.mui is not signed
✗ /boot/EFI/Microsoft/Boot/SecureBootRecovery.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bg-BG/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/bootmgfw.efi is not signed
✗ /boot/EFI/Microsoft/Boot/bootmgr.efi is not signed
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
✗ /boot/EFI/Microsoft/Boot/kd_02_10df.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_10ec.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1137.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1414.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_14e4.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_15ad.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_15b3.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1969.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_19a2.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1af4.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_1d0f.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_02_8086.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_07_1415.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kd_0C_8086.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kdnet_uart16550.dll is not signed
✗ /boot/EFI/Microsoft/Boot/kdstub.dll is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/ko-KR/memtest.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lt-LT/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgfw.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/lv-LV/bootmgr.efi.mui is not signed
✗ /boot/EFI/Microsoft/Boot/memtest.efi is not signed
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
✗ /boot/EFI/systemd/systemd-bootx64.efi is not signed
✗ /boot/grub/x86_64-efi/core.efi is not signed
✗ /boot/grub/x86_64-efi/grub.efi is not signed

~
❯ 

### GEMINI
The list is long, but most of it is noise. However, there are three specific files in that list that are absolutely triggering the "Secure Boot Violation." Even though you enrolled Microsoft's keys, your BIOS is likely in a strict mode where it wants every active EFI file in the boot chain signed by your local keys too. 1. The "Must-Sign" Fix Run these commands to sign the actual Windows bootloader and the remaining system binaries that the BIOS sees during startup: # Sign the main Windows bootloader sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgfw.efi # Sign the secondary Windows manager sudo sbctl sign -s /boot/EFI/Microsoft/Boot/bootmgr.efi # Sign the memory test (sometimes checked during boot) sudo sbctl sign -s /boot/EFI/Microsoft/Boot/memtest.efi 2. Clean up the "Ghost" files Your BIOS might be trying to "help" by looking at old GRUB or Systemd files. Let's sign them just to shut the BIOS up: sudo sbctl sign -s /boot/EFI/systemd/systemd-bootx64.efi sudo sbctl sign -s /boot/grub/x86_64-efi/core.efi sudo sbctl sign -s /boot/grub/x86_64-efi/grub.efi 3. Why this will work The red box you saw usually triggers because the BIOS checks bootmgfw.efi (Windows) or the EFI binaries in the systemd or grub folders if it can't find a clear path. By signing these, you are leaving the BIOS with zero excuses to throw a violation. Final Verification After running those, run: sudo sbctl verify | grep "is not signed" | grep ".efi" If those specific .efi files you just signed are gone from the list, you are ready. Reboot, Enable Secure Boot in BIOS, and let's get you into Valorant. Any more "Unrecognized PE" errors, or did they sign successfully?
