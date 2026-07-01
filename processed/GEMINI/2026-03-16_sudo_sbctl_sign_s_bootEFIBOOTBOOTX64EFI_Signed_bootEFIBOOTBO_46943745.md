---
id: 649099
source: GEMINI
date: 2026-03-16
tags: ['sbctl', 'efi-signing', 'secure-boot', 'boot-verification']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan signed the BOOTX64.EFI file and verified signatures, finding many Microsoft and GRUB files still unsigned.
---
# ❯ sudo sbctl sign -s /boot/EFI/BOOT/BOOTX64.EFI
✓ Signed /boot/EFI/BOOT/BOOTX64.EFI

~
❯ sudo sbctl verify
Verifying file database and EFI images in /boot...
✓ /boot/EFI/BOOT/BOOTX64.EFI is signed
✓ /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/vmlinuz-linux-cachyos-lts is signed
✓ /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos is signed
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
✗ /boot/EFI/limine/limine_x64.efi is not signed
✗ /boot/EFI/systemd/systemd-bootx64.efi is not signed
✗ /boot/grub/x86_64-efi/core.efi is not signed
✗ /boot/grub/x86_64-efi/grub.efi is not signed
✗ /boot/vmlinuz-linux-cachyos is not signed

~
❯ 

### USER
❯ sudo sbctl sign -s /boot/EFI/BOOT/BOOTX64.EFI
✓ Signed /boot/EFI/BOOT/BOOTX64.EFI

~
❯ sudo sbctl verify
Verifying file database and EFI images in /boot...
✓ /boot/EFI/BOOT/BOOTX64.EFI is signed
✓ /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/vmlinuz-linux-cachyos-lts is signed
✓ /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos is signed
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
✗ /boot/EFI/limine/limine_x64.efi is not signed
✗ /boot/EFI/systemd/systemd-bootx64.efi is not signed
✗ /boot/grub/x86_64-efi/core.efi is not signed
✗ /boot/grub/x86_64-efi/grub.efi is not signed
✗ /boot/vmlinuz-linux-cachyos is not signed

~
❯ 

### GEMINI
Ignore the massive list of red Xs for the Microsoft files. Those are already signed by Microsoft's factory key; because you used the -m flag during enrollment, your BIOS will trust them automatically. You do not need to sign them yourself. However, we need to clean up the CachyOS side. You are using Limine, but you have leftover GRUB files and some unsigned kernel links that might cause a "Security Violation" if the BIOS picks them up. 1. The "Must-Sign" List Run these commands to cover the files sbctl verify flagged as unsigned for CachyOS: # Sign the main kernel link sudo sbctl sign -s /boot/vmlinuz-linux-cachyos # Sign the Limine EFI binary sudo sbctl sign -s /boot/EFI/limine/limine_x64.efi 2. Why the others don't matter Limine History: You don't need to sign the files in limine_history; those are just backups. GRUB/Systemd-boot: Since you are using Limine to boot, these are "ghost" files left over from previous attempts. They aren't used, so you can ignore them. Microsoft: As mentioned, your BIOS already trusts these via the Vendor Keys. 3. Final Check Run sudo sbctl verify one last time. As long as these three are Green ✓, you are good to go: /boot/vmlinuz-linux-cachyos /boot/EFI/BOOT/BOOTX64.EFI /boot/EFI/limine/limine_x64.efi 4. The BIOS Moment Once those are signed, reboot into your BIOS: Secure Boot: Set to Enabled (or "Windows UEFI Mode"). Key Management: Ensure it says "User" mode or "Enrolled" (not Setup Mode). Save and Exit. If you see the Minecraft menu, you've won. You can then boot into Windows and Vanguard should be satisfied. Are those three files showing green now?
