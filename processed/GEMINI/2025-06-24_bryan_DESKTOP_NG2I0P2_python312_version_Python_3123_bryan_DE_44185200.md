---
category: coding
date: 2025-06-24
id: 735676
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user encountered a traceback error while running sudo apt update on their
  Ubuntu system, indicating a problem with the package management database update
  process.
tags:
- python
- ubuntu
- apt-update
- error
- system-administration
---
# bryan_@DESKTOP-NG2I0P2:~$ python3.12 --version
Python 3.12.3
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Traceback (most recent call last):
  File "/usr/lib/cnf-update-db", line 3, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
Reading package lists... Done
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code
bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ python3.12 --version
Python 3.12.3
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Traceback (most recent call last):
  File "/usr/lib/cnf-update-db", line 3, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
Reading package lists... Done
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code
bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
You've confirmed that Python 3.12.3 is installed, which is excellent! However, it looks like you ran sudo apt update immediately after confirming the python3.12 version, but before running the sudo apt install --reinstall commands and reconfiguring update-alternatives. That's why you're still seeing the apt_pkg error. We haven't applied the fixes yet that would resolve it. Action: Continue with the remaining steps from the previous instruction set. Please execute these commands in the following order: Reinstall core Python 3.12 packages and python3-apt: sudo apt update # Ensure your package list is fresh sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils sudo apt install --reinstall python3-apt After the reinstallations, configure python3 alternatives: sudo update-alternatives --config python3 Crucially, this time, you should see python3.12 in the list. If you do, select its corresponding number. Finally, attempt sudo apt update again: sudo apt update This is the ultimate test to see if the apt_pkg error is resolved. Please provide the full output of each of these commands.