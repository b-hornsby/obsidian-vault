---
id: 211555
source: GEMINI
date: 2026-03-15
tags: ['ventoy', 'tiny11-iso', 'bootable-usb', 'dual-boot-install']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed he had Tiny11 on his Ventoy drive and asked what the next step was.
---
# okay tiny 11 on my ventoy drive. next?

### USER
okay tiny 11 on my ventoy drive. next?

### GEMINI
Next is the installation itself. Since you're using Ventoy, the heavy lifting of bypassing TPM and RAM checks is already handled by Ventoy's default settings. However, Windows 11 25H2 (the base for your Tiny11 ISO) has become much more aggressive about forcing a Microsoft Account. Even with Tiny11, you might hit a "Let's connect you to a network" wall that won't let you skip. The Game Plan Boot into Ventoy: Restart your PC, mash F12 (or your motherboard's boot menu key), and select your SanDisk drive. Pick the ISO: Select tiny11_25H2_Nov25.iso. The Partition Trap: When you get to "Where do you want to install Windows?", you'll see your CachyOS partitions. Be careful. If you intend to dual-boot, you need free space. If you're wiping CachyOS, delete all partitions until the drive shows as "Unallocated Space," then click Next. If it forces a Microsoft Account (The OOBE Bypass) If you get stuck at the "Connect to Internet" or "Sign in" screen: Press Shift + F10 to open the Command Prompt. Type: start ms-cxh:localonly and hit Enter. Note: If that doesn't work, the classic oobe\bypassnro command is often patched in 25H2, so use the ms-cxh one first. The setup should restart and give you the "I don't have internet" / "Continue with limited setup" option, allowing you to create a local username. Post-Install Checklist (Specific to your 3070 GPU) Once you're at the desktop, it's going to feel empty (that’s the point). But you need drivers: Nvidia Drivers: Tiny11 might not auto-pull drivers for your RTX 3070. Since it's a "stripped" OS, the standard Nvidia installer sometimes throws a "Windows version not compatible" error. Fix: Download the driver from Nvidia's site. If it fails, use NVCleanstall to strip the driver even further to match the stripped OS. Browser: Tiny11 usually doesn't have Edge. You'll need to use the curl command in Command Prompt to grab an installer, or have a Chrome/Firefox installer ready on another USB. curl -L "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US" -o firefox_setup.exe Would you like me to find the specific terminal command to install the Nvidia drivers once you're inside, or are you planning to dual-boot and need help with the GRUB/systemd-boot configuration?
