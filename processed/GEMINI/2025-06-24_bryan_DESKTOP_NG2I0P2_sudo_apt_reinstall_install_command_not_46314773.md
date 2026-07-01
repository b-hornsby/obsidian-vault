---
category: homelab
date: 2025-06-24
id: 918685
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: The user is attempting to reinstall the command-not-found package on their
  Ubuntu system, likely as part of troubleshooting or restoring functionality in their
  homelab environment.
tags:
- linux-troubleshooting
- package-management
- ubuntu
- system-recovery
- command-not-found
---
# bryan_@DESKTOP-NG2I0P2:~$ sudo apt --reinstall install command-not-found
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 0 not upgraded.
Need to get 5124 B of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 command-not-found all 23.04.0 [5124 B]
Fetched 5124 B in 0s (17.9 kB/s)
(Reading database ... 53075 files and directories currently installed.)
Preparing to unpack .../command-not-found_23.04.0_all.deb ...
Unpacking command-not-found (23.04.0) over (23.04.0) ...
Setting up command-not-found (23.04.0) ...
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://security.ubuntu.com/ubuntu noble-security InRelease
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
bryan_@DESKTOP-NG2I0P2:~$ sudo apt --reinstall install command-not-found
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 0 not upgraded.
Need to get 5124 B of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 command-not-found all 23.04.0 [5124 B]
Fetched 5124 B in 0s (17.9 kB/s)
(Reading database ... 53075 files and directories currently installed.)
Preparing to unpack .../command-not-found_23.04.0_all.deb ...
Unpacking command-not-found (23.04.0) over (23.04.0) ...
Setting up command-not-found (23.04.0) ...
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://security.ubuntu.com/ubuntu noble-security InRelease
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
You're right to be persistent, this apt_pkg error is very stubborn! The fact that reinstalling both python3-apt and command-not-found hasn't fixed it strongly points to an issue with which Python interpreter your apt system is trying to use for its internal scripts. Often, this happens when the system's default python3 symbolic link (/usr/bin/python3) gets modified or points to a Python version (like one from the deadsnakes PPA, which is visible in your apt update output) that isn't compatible with the apt_pkg module from your standard Ubuntu repositories. The apt system needs to use its own tightly integrated Python for these operations. Let's investigate and try to correct the python3 symlink to ensure apt can find what it needs. Action: Resetting System Python 3 Alternative Check where /usr/bin/python3 currently points: ls -l /usr/bin/python3 This will show you which actual Python executable your system considers to be python3. List available Python 3 alternatives: sudo update-alternatives --config python3 This command will show you all Python 3 installations that update-alternatives knows about and allows you to choose which one /usr/bin/python3 should point to. You'll likely see a list with numbers next to each option. Choose the system's default Python 3. Look for an entry that points to something like /usr/bin/python3.10 or /usr/bin/python3.12 (whatever is the native Ubuntu version for your Noble Numbat release, probably 3.12) and select its corresponding number. If prompted, confirm your choice. Avoid selecting any version explicitly from deadsnakes PPA here for apt's sake. The system's default Python will usually have the highest "priority" if you were to let it auto-configure, or it will be clearly labeled as the system version. Example output you might see: There are 2 choices for the alternative python3 (providing /usr/bin/python3). Selection Path Priority Status -
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
--- * 0 /usr/bin/python3.10 2 auto mode 1 /usr/bin/python3.10 2 manual mode 2 /usr/bin/python3.12 1 manual mode <-- You want to select this if 3.12 is default for Noble In this example, you'd type 2 and press Enter to select /usr/bin/python3.12. After setting the alternative, try sudo apt update again: sudo apt update Please provide the full output of ls -l /usr/bin/python3, the sudo update-alternatives --config python3 command (including the choice you make), and finally, the output of sudo apt update. This should hopefully resolve the apt_pkg issue.