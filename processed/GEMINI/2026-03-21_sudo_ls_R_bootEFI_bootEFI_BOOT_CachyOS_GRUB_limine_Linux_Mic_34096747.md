---
id: 724469
source: GEMINI
date: 2026-03-21
tags: ['efi-directory', 'boot-configuration', 'file-listing', 'bootloader-files']
category: coding
sentiment: exploratory
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is listing the contents of the /boot/EFI directory recursively, likely to inspect bootloader files and troubleshoot boot issues.
---
# ❯ sudo ls -R /boot/EFI
/boot/EFI:
BOOT  CachyOS  GRUB  limine  Linux  Microsoft  systemd

/boot/EFI/BOOT:
BOOTX64.EFI

/boot/EFI/CachyOS:
grubx64.efi

/boot/EFI/GRUB:
grubx64.efi

/boot/EFI/limine:
limine_x64.bak  limine_x64.efi

/boot/EFI/Linux:

/boot/EFI/Microsoft:
Boot  Recovery

/boot/EFI/Microsoft/Boot:
BCD           boot.stl    es-MX  ja-JP           kd_02_19a2.dll       lt-LT        qps-plocm               tr-TR
BCD.LOG       CIPolicies  et-EE  kd_02_10df.dll  kd_02_1af4.dll       lv-LV        Resources               uk-UA
BCD.LOG1      cs-CZ       fi-FI  kd_02_10ec.dll  kd_02_1d0f.dll       memtest.efi  ro-RO                   winsipolicy.p7b
BCD.LOG2      da-DK       Fonts  kd_02_1137.dll  kd_02_8086.dll       nb-NO        ru-RU                   zh-CN
bg-BG         de-DE       fr-CA  kd_02_1414.dll  kd_07_1415.dll       nl-NL        SecureBootRecovery.efi  zh-TW
bootmgfw.efi  el-GR       fr-FR  kd_02_14e4.dll  kd_0C_8086.dll       pl-PL        sk-SK
bootmgr.efi   en-GB       hr-HR  kd_02_15ad.dll  kdnet_uart16550.dll  pt-BR        sl-SI
boot.pnd.stl  en-US       hu-HU  kd_02_15b3.dll  kdstub.dll           pt-PT        sr-Latn-RS
BOOTSTAT.DAT  es-ES       it-IT  kd_02_1969.dll  ko-KR                qps-ploc     sv-SE

/boot/EFI/Microsoft/Boot/bg-BG:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/CIPolicies:
Active

/boot/EFI/Microsoft/Boot/CIPolicies/Active:
{5DAC656C-21AD-4A02-AB49-649917162E70}.cip  {82443e1e-8a39-4b4a-96a8-f40ddc00b9f3}.cip  {CDD5CB55-DB68-4D71-AA38-3DF2B6473A52}.cip

/boot/EFI/Microsoft/Boot/cs-CZ:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/da-DK:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/de-DE:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/el-GR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/en-GB:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/en-US:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/es-ES:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/es-MX:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/et-EE:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/fi-FI:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/Fonts:
chs_boot.ttf  jpn_boot.ttf  malgun_boot.ttf   meiryo_boot.ttf   msjh_boot.ttf   msyh_boot.ttf   segmono_boot.ttf   segoe_slboot.ttf
cht_boot.ttf  kor_boot.ttf  malgunn_boot.ttf  meiryon_boot.ttf  msjhn_boot.ttf  msyhn_boot.ttf  segoen_slboot.ttf  wgl4_boot.ttf

/boot/EFI/Microsoft/Boot/fr-CA:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/fr-FR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/hr-HR:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/hu-HU:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/it-IT:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/ja-JP:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/ko-KR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/lt-LT:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/lv-LV:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/nb-NO:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/nl-NL:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pl-PL:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pt-BR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pt-PT:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/qps-ploc:
memtest.efi.mui

/boot/EFI/Microsoft/Boot/qps-plocm:
memtest.efi.mui

/boot/EFI/Microsoft/Boot/Resources:
bootres.dll  en-US

/boot/EFI/Microsoft/Boot/Resources/en-US:
bootres.dll.mui

/boot/EFI/Microsoft/Boot/ro-RO:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/ru-RU:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/sk-SK:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sl-SI:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sr-Latn-RS:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sv-SE:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/tr-TR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/uk-UA:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/zh-CN:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/zh-TW:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Recovery:
BCD  BCD.LOG  BCD.LOG1  BCD.LOG2

/boot/EFI/systemd:
systemd-bootx64.efi

~
❯ 

### USER
❯ sudo ls -R /boot/EFI
/boot/EFI:
BOOT  CachyOS  GRUB  limine  Linux  Microsoft  systemd

/boot/EFI/BOOT:
BOOTX64.EFI

/boot/EFI/CachyOS:
grubx64.efi

/boot/EFI/GRUB:
grubx64.efi

/boot/EFI/limine:
limine_x64.bak  limine_x64.efi

/boot/EFI/Linux:

/boot/EFI/Microsoft:
Boot  Recovery

/boot/EFI/Microsoft/Boot:
BCD           boot.stl    es-MX  ja-JP           kd_02_19a2.dll       lt-LT        qps-plocm               tr-TR
BCD.LOG       CIPolicies  et-EE  kd_02_10df.dll  kd_02_1af4.dll       lv-LV        Resources               uk-UA
BCD.LOG1      cs-CZ       fi-FI  kd_02_10ec.dll  kd_02_1d0f.dll       memtest.efi  ro-RO                   winsipolicy.p7b
BCD.LOG2      da-DK       Fonts  kd_02_1137.dll  kd_02_8086.dll       nb-NO        ru-RU                   zh-CN
bg-BG         de-DE       fr-CA  kd_02_1414.dll  kd_07_1415.dll       nl-NL        SecureBootRecovery.efi  zh-TW
bootmgfw.efi  el-GR       fr-FR  kd_02_14e4.dll  kd_0C_8086.dll       pl-PL        sk-SK
bootmgr.efi   en-GB       hr-HR  kd_02_15ad.dll  kdnet_uart16550.dll  pt-BR        sl-SI
boot.pnd.stl  en-US       hu-HU  kd_02_15b3.dll  kdstub.dll           pt-PT        sr-Latn-RS
BOOTSTAT.DAT  es-ES       it-IT  kd_02_1969.dll  ko-KR                qps-ploc     sv-SE

/boot/EFI/Microsoft/Boot/bg-BG:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/CIPolicies:
Active

/boot/EFI/Microsoft/Boot/CIPolicies/Active:
{5DAC656C-21AD-4A02-AB49-649917162E70}.cip  {82443e1e-8a39-4b4a-96a8-f40ddc00b9f3}.cip  {CDD5CB55-DB68-4D71-AA38-3DF2B6473A52}.cip

/boot/EFI/Microsoft/Boot/cs-CZ:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/da-DK:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/de-DE:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/el-GR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/en-GB:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/en-US:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/es-ES:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/es-MX:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/et-EE:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/fi-FI:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/Fonts:
chs_boot.ttf  jpn_boot.ttf  malgun_boot.ttf   meiryo_boot.ttf   msjh_boot.ttf   msyh_boot.ttf   segmono_boot.ttf   segoe_slboot.ttf
cht_boot.ttf  kor_boot.ttf  malgunn_boot.ttf  meiryon_boot.ttf  msjhn_boot.ttf  msyhn_boot.ttf  segoen_slboot.ttf  wgl4_boot.ttf

/boot/EFI/Microsoft/Boot/fr-CA:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/fr-FR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/hr-HR:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/hu-HU:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/it-IT:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/ja-JP:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/ko-KR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/lt-LT:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/lv-LV:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/nb-NO:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/nl-NL:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pl-PL:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pt-BR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/pt-PT:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/qps-ploc:
memtest.efi.mui

/boot/EFI/Microsoft/Boot/qps-plocm:
memtest.efi.mui

/boot/EFI/Microsoft/Boot/Resources:
bootres.dll  en-US

/boot/EFI/Microsoft/Boot/Resources/en-US:
bootres.dll.mui

/boot/EFI/Microsoft/Boot/ro-RO:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/ru-RU:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/sk-SK:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sl-SI:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sr-Latn-RS:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/sv-SE:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/tr-TR:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/uk-UA:
bootmgfw.efi.mui  bootmgr.efi.mui

/boot/EFI/Microsoft/Boot/zh-CN:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Boot/zh-TW:
bootmgfw.efi.mui  bootmgr.efi.mui  memtest.efi.mui

/boot/EFI/Microsoft/Recovery:
BCD  BCD.LOG  BCD.LOG1  BCD.LOG2

/boot/EFI/systemd:
systemd-bootx64.efi

~
❯ 

### GEMINI
Okay, the output explains exactly why you’re stuck in a "Violation" loop. Your EFI partition is a graveyard of every bootloader known to man—Limine, Systemd-boot, and two different versions of GRUB. The BIOS is likely trying to launch the CachyOS version of GRUB or the Limine one, but you only signed the GRUB one (or vice versa). The "Clean Sweep" Signing Command Since you have a 12700K and you're at the "Tiny 11" tipping point, let's do the only thing that will actually work. We are going to sign every single bootable file in that folder so the BIOS has no choice but to trust whatever it picks. Run this command exactly: sudo find /boot/EFI -name "*.efi" -exec sbctl sign -s {} + Wait for it to finish. It should scroll through and sign things in BOOT, CachyOS, GRUB, limine, and systemd. The "Kill the Imposters" Step Now, run this to see which one the BIOS is actually trying to boot first: sudo efibootmgr Look at the list. You probably see: Boot000X* CachyOS Boot000Y* GRUB Boot000Z* Windows Boot Manager The Operation: If you want Minegrub (the Minecraft theme), you must make sure the one named GRUB is at the very top. If you see an entry for CachyOS or Limine, delete them so they stop hijacking your boot: sudo efibootmgr -b [NUMBER] -B Ensure the GRUB entry is BootOrder number 1. The "Brutally Honest" Final Call If you run the find command above and sign every .efi file, and you still get a red box after turning Secure Boot on, then your BIOS is physically refusing to acknowledge the sbctl keys you enrolled. At that point, go Tiny 11. You've spent hours on a 60-second update bug. As a logistics/ops guy, you know when a process is "broken beyond repair." If the "Clean Sweep" signing doesn't fix it, your time is better spent nuking the drive and getting back to Valorant. Does sbctl list-files show everything as "Signed: ✓" after you run that find command?
