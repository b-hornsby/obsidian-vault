---
category: homelab
date: 2025-06-24
id: 192101
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user attempted to manually download a specific version of the libtinfo5
  package for Ubuntu but received a 404 error, indicating the file is no longer available
  at the expected URL.
tags:
- linux
- package-management
- ubuntu
- ncurses
- dependency-resolution
---
# bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:44:26--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 185.125.190.83, 185.125.190.82, 91.189.91.82, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|185.125.190.83|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:44:26 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:44:26--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 185.125.190.83, 185.125.190.82, 91.189.91.82, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|185.125.190.83|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:44:26 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
You're persistently getting a 404 Not Found error for libtinfo5_6.3-2ubuntu0.1_amd64.deb, even from the security.ubuntu.com mirror. This is highly unusual for a standard package from a recent Ubuntu LTS release. This indicates that either: There's a temporary network issue or a specific firewall/DNS problem within your WSL2 environment that's preventing access to even basic Ubuntu package archives. The specific file might have been moved or renamed in a very recent update on the Ubuntu mirrors, which is less common but possible. Since nsight-systems-2022.4.2 is complaining about libtinfo5, and sometimes libncursesw5 is also a related dependency, we'll try to download both from the Jammy (Ubuntu 22.04) security archives. If these wget commands still fail, you'll need to troubleshoot your WSL2's network connectivity. Action: Try Both libtinfo5 and libncursesw5 .deb Packages Try downloading libtinfo5 again (confirming exact URL): wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb Also download libncursesw5 (it's often a companion or indirect dependency): wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libncursesw5_6.3-2ubuntu0.1_amd64.deb Check if both files downloaded. Then, attempt to install both .deb packages: sudo dpkg -i libtinfo5_6.3-2ubuntu0.1_amd64.deb libncursesw5_6.3-2ubuntu0.1_amd64.deb If dpkg complains about other dependencies or broken packages immediately after, run: sudo apt --fix-broken install Clean up apt's cache and try to install cuda-toolkit-11-8 again: sudo apt update --fix-missing sudo apt -y install cuda-toolkit-11-8 Crucial: If the wget commands for these standard Ubuntu archive URLs continue to result in 404 Not Found or any other network error, then the immediate problem is with your WSL2's network connectivity preventing it from reaching external repositories. In that scenario, you would need to: Check your internet connection on Windows. Restart WSL2 (wsl --shutdown in PowerShell/CMD, then restart your WSL terminal). Check your DNS settings within WSL2 (e.g., cat /etc/resolv.conf). Temporarily disable any VPNs or aggressive firewalls on your Windows host that might be interfering with WSL2's network access. Please provide the full output of each wget command and the subsequent dpkg and apt commands.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]