---
category: homelab
date: 2026-03-16
id: 854738
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan used an incorrect -f flag with sbctl sign and got errors, needing the
  correct -s flag syntax.
tags:
- sbctl
- signing-error
- wrong-flag
- cli-troubleshooting
---
# ❯ sudo sbctl sign -f /boot/vmlinuz-linux-cachyos
  sudo sbctl sign -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl sign -f /boot/EFI/limine/limine_x64.efi
unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging

unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging

unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging


~
❯ 

### USER
❯ sudo sbctl sign -f /boot/vmlinuz-linux-cachyos
  sudo sbctl sign -f /boot/EFI/BOOT/BOOTX64.EFI
  sudo sbctl sign -f /boot/EFI/limine/limine_x64.efi
unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging

unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging

unknown shorthand flag: 'f' in -f
Usage:
  sbctl sign [flags]

Flags:
  -h, --help            help for sign
  -o, --output string   output filename. Default replaces the file
  -s, --save            save file to the database

Global Flags:
      --config string      Path to configuration file
      --debug              Enable verbose debug logging
      --disable-landlock   Disable landlock sandboxing
      --json               Output as json
      --quiet              Mute info from logging


~
❯ 

### GEMINI
My mistake—I mixed up the flags between the enrollment and signing commands. sbctl sign doesn't use -f; it just needs the -s (save) flag to ensure the file is tracked and signed in the database. Since they were already signed in a previous step, you are actually already good to go. The database already has the signatures locked in from your previous successful sbctl sign -s commands. The Final Move Skip the force-signing. You’ve already enrolled the keys and the files are already signed. Reboot and enter your BIOS. Go to Boot -> Secure Boot. Set it to Enabled (or Windows UEFI Mode). Save and Exit (F10). Why you’re ready: You successfully removed the immutable locks on your EFI variables and enrolled your specific file fingerprints directly into the motherboard. The BIOS now has the "Identity" of your CachyOS bootloader and Kernel saved in its hardware memory. Go enable Secure Boot now. If that shim_lock error appears again, it would be a miracle—you've officially cleared every logical hurdle. Is the Minecraft menu greeting you with Secure Boot ON?
