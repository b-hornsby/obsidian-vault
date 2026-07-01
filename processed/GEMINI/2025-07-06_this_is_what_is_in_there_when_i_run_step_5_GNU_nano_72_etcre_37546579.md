---
category: homelab
date: 2025-07-06
id: 982891
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting DNS resolution in WSL2 by examining the /etc/resolv.conf
  file managed by systemd-resolved.
tags:
- dns
- resolv.conf
- wsl2
- networking
- systemd-resolved
---
# this is what is in there when i run step 5:    GNU nano 7.2                                        /etc/resolv.conf                                                  # This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search . 

### USER
this is what is in there when i run step 5:    GNU nano 7.2                                        /etc/resolv.conf                                                  # This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search . 

### GEMINI
You've hit a common and tricky point with WSL2 and Ubuntu! The output you're seeing for /etc/resolv.conf means: Your Ubuntu instance within WSL2 is using systemd-resolved to manage its DNS settings. /etc/resolv.conf is actually a symlink (a shortcut) to a file that systemd-resolved dynamically generates (usually /run/systemd/resolve/stub-resolv.conf). This is why your previous edits to /etc/resolv.conf (Step 2 in the last instruction) are not sticking – systemd-resolved just overwrites or ignores them because it's managing the file. The nameserver 127.0.0.53 means it's trying to use a local DNS stub resolver, which then forwards requests. If that stub resolver can't reach an external DNS, you get your NameResolutionError. We need to tell systemd-resolved to step aside so we can manually set the DNS. The Corrected Method: Disable systemd-resolved and Manually Set DNS This is the most robust way to force WSL2 to use a specific DNS server like 8.8.8.8. Step 1: Ensure wsl.conf is Set to Prevent Auto-Generation You've already done this, but let's confirm it's correct. This file tells WSL2 not to automatically manage /etc/resolv.conf. Close all WSL2 terminals. Open PowerShell or Command Prompt (on Windows) as Administrator. Run: wsl --shutdown Open a new WSL2 terminal. Edit wsl.conf again to confirm: sudo nano /etc/wsl.conf Make sure it contains: [network] generateResolvConf = false Save and exit Nano (Ctrl+O, Enter, Ctrl+X). Step 2: Disable and Stop systemd-resolved Service This stops the service that is constantly overwriting your resolv.conf. In your WSL2 terminal, disable the service: sudo systemctl disable systemd-resolved (You might see a message like "Removed /etc/systemd/system/multi-user.target.wants/systemd-resolved.service.") Stop the currently running service: sudo systemctl stop systemd-resolved Step 3: Delete the Existing Symlink and Create a New resolv.conf Now that systemd-resolved is out of the way, we can make our own static resolv.conf. Delete the existing symlink for resolv.conf: sudo rm /etc/resolv.conf Create a new, static resolv.conf file with your desired DNS: sudo nano /etc/resolv.conf Add the following lines: nameserver 8.8.8.8 nameserver 8.8.4.4 Save and exit Nano (Ctrl+O, Enter, Ctrl+X). Make the file immutable (prevent changes): sudo chattr +i /etc/resolv.conf This is important! It stops anything, even root, from modifying this file unless you explicitly remove the immutable flag (sudo chattr -i /etc/resolv.conf). Step 4: Final WSL2 Restart and Verification Close all WSL2 terminals. Open PowerShell or Command Prompt (on Windows) as Administrator. Run: wsl --shutdown Open a new WSL2 terminal. Verify DNS: cat /etc/resolv.conf It must now show nameserver 8.8.8.8 and nameserver 8.8.4.4. If it doesn't, something is still interfering, and you should re-check all previous steps very carefully. Test internet connectivity: ping google.com You should see successful replies. Step 5: Clear Hugging Face Cache and Run Oobabooga Since DNS was previously broken, ensure a clean slate for superboogav2. Ensure you have an active internet connection on your Windows host. In your WSL2 terminal, navigate to the Hugging Face cache directory: cd ~/.cache/huggingface/hub Delete the specific model cache again: rm -rf models--sentence-transformers--all-MiniLM-L6-v2 Go back to your Oobabooga directory: cd ~/text-generation-webui/ Run Oobabooga: ./installer_files/env/bin/python server.py This should finally resolve the persistent DNS and loading issues for superboogav2. It will download the embedding model once, and then it should load successfully offline in future runs (assuming web_rag is disabled for offline use).


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
