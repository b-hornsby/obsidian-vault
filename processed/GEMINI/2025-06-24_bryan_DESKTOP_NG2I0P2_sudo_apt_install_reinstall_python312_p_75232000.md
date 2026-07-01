---
category: homelab
date: 2025-06-24
id: 915712
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was trying to reinstall Python 3.12 and its components on their
  Ubuntu system but encountered an error where the package python3.12-distutils could
  not be located, indicating a missing or misconfigured package repository.
tags:
- python-installation
- package-management
- ubuntu-linux
- dependency-issues
- homelab-setup
---
# bryan_@DESKTOP-NG2I0P2:~$ sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package python3.12-distutils
E: Couldn't find any package by glob 'python3.12-distutils'
bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package python3.12-distutils
E: Couldn't find any package by glob 'python3.12-distutils'
bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
You're getting specific errors, which helps us narrow down the problem! The error E: Unable to locate package python3.12-distutils means that python3.12-distutils is not available as a separate package in your Ubuntu Noble (24.04) repositories. In newer Python versions and Ubuntu releases, the distutils module might have been integrated directly into the main python3.12 package or its standard library. This is okay; apt_pkg's issue is unlikely to be directly dependent on distutils. We can proceed with reinstalling the other crucial packages. Action: Proceed with Reinstalling Core Python 3.12 and python3-apt Reinstall python3.12 and python3.12-minimal: sudo apt install --reinstall python3.12 python3.12-minimal This ensures the foundational Python 3.12 environment is intact. After that, reinstall python3-apt: sudo apt install --reinstall python3-apt This is the package that provides apt_pkg. After these reinstallations, configure python3 alternatives: sudo update-alternatives --config python3 Crucially, look very carefully for python3.12 in the list. If you see it, select its corresponding number. Finally, attempt sudo apt update again: sudo apt update This is the ultimate test to see if the apt_pkg error is resolved. Please provide the full output of each of these commands.