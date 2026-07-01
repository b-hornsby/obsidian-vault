---
category: homelab
date: 2025-06-24
id: 679532
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user attempted to manually download a specific version of the libtinfo5
  package for Ubuntu but received a 404 error, indicating the package is no longer
  available at the expected URL.
tags:
- package-management
- ubuntu
- ncurses
- dependency-resolution
- wget
---
# bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:45:59--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 91.189.91.83, 185.125.190.82, 185.125.190.81, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|91.189.91.83|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:45:59 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:45:59--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 91.189.91.83, 185.125.190.82, 185.125.190.81, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|91.189.91.83|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:45:59 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
This is very unusual and points to a more fundamental issue with your WSL2 environment's network connectivity. Getting a 404 Not Found error consistently for a standard, widely available package (libtinfo5_6.3-2ubuntu0.1_amd64.deb) from official Ubuntu archives like security.ubuntu.com means your WSL2 instance is either: Not able to resolve DNS correctly. Being blocked by a firewall (on Windows or within WSL2). Experiencing general internet connectivity issues within WSL2. Behind a proxy that's not correctly configured. We cannot proceed with installing the CUDA Toolkit until this basic network access is fixed. Action: Troubleshoot WSL2 Network Connectivity Please follow these steps to diagnose and potentially fix your WSL2's internet access. Exit your WSL2 terminal entirely. Open PowerShell or Command Prompt (CMD) on your Windows host. Shut down WSL2 completely: wsl --shutdown Wait for a few seconds until it confirms all distributions are stopped. Restart your WSL2 Ubuntu terminal. Once back in WSL2, first test basic internet connectivity: ping google.com You should see replies. If not, it's a connectivity problem. Check your DNS configuration within WSL2: cat /etc/resolv.conf This file should typically point to a DNS server provided by Windows, or to Google's DNS (8.8.8.8) if you've configured it that way. Look for nameserver entries. If it's empty or points to something unreachable, that's an issue. Try to ping one of the Ubuntu archive IP addresses directly (if ping google.com fails): For example, from security.ubuntu.com resolve output: ping 91.189.91.83 If ping google.com fails or wget continues to give 404s after restarting WSL2: Windows Firewall/Antivirus: Temporarily disable your Windows Firewall or any third-party antivirus/security software to see if it's interfering with WSL2's outgoing connections. VPN: If you are using a VPN on Windows, try temporarily disconnecting from it. VPNs often re-route network traffic in ways that can conflict with WSL2's virtual network adapter. DNS Issues on Windows: Ensure your Windows DNS settings are working correctly (e.g., set to automatic or use public DNS like 8.8.8.8). Once you believe your WSL2 has proper internet access (e.g., ping google.com works and your cat /etc/resolv.conf looks reasonable): Try the wget commands for libtinfo5 and libncursesw5 again. wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libncursesw5_6.3-2ubuntu0.1_amd64.deb If successful, proceed with installation: sudo dpkg -i libtinfo5_6.3-2ubuntu0.1_amd64.deb libncursesw5_6.3-2ubuntu0.1_amd64.deb sudo apt --fix-broken install sudo apt update --fix-missing sudo apt -y install cuda-toolkit-11-8 Please let me know the results of your network troubleshooting steps first.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]