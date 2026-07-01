---
category: coding
date: 2025-06-24
id: 538611
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: The user is setting up Python 3.12 on their WSL environment and verifying
  the installation by checking the Python path.
tags:
- python
- linux
- terminal
- environment-setup
- wsl
---
# got step 2 down, this is what i got: bryan_@DESKTOP-NG2I0P2:~$ which python3.12/usr/bin/python3.12bryan_@DESKTOP-NG2I0P2:~$

### USER
got step 2 down, this is what i got: bryan_@DESKTOP-NG2I0P2:~$ which python3.12/usr/bin/python3.12bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Great! The output /usr/bin/python3.12 for which python3.12 is fantastic news! This confirms that Python 3.12 is indeed installed on your system. The reason it wasn't showing up in update-alternatives --config python3 before is likely because it wasn't fully registered or the alternatives system needed a refresh. Let's confirm its version and then make sure it's the one apt uses. Action: Continue with Step 3 (Confirm Version, Reinstall Core Packages, and Set Alternative) Confirm Python 3.12 version: python3.12 --version Now, run the commands to reinstall core Python 3.12 packages and python3-apt: sudo apt update # Update again to ensure latest package info sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils sudo apt install --reinstall python3-apt This should ensure all necessary components are in place and properly registered. After the reinstallations, try to configure python3 alternatives again: sudo update-alternatives --config python3 Crucially, this time, you should see python3.12 in the list. If you do, select its corresponding number. Finally, attempt sudo apt update again: sudo apt update This is the ultimate test to see if the apt_pkg error is resolved. Please provide the full output of each of these commands.