---
source: GEMINI
date: 2025-06-24
category: ai-tools
id: 66742614
linked_nodes: ['nodes/people/bryan.md']
---
-
---
--
* 0            /usr/bin/python3.10   1         auto mode
  1            /usr/bin/python3.10   1         manual mode

Press <enter> to keep the current choice[*], or type selection number:
### USER
bryan_@DESKTOP-NG2I0P2:~$ which python3.12
/usr/bin/python3.12
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
bryan_@DESKTOP-NG2I0P2:~$ sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package python3.12-distutils
E: Couldn't find any package by glob 'python3.12-distutils'
bryan_@DESKTOP-NG2I0P2:~$ sudo apt install --reinstall python3.12 python3.12-minimal
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
0 upgraded, 0 newly installed, 2 reinstalled, 0 to remove and 0 not upgraded.
Need to get 2993 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 python3.12-minimal amd64 3.12.3-1ubuntu0.7 [2342 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 python3.12 amd64 3.12.3-1ubuntu0.7 [651 kB]
Fetched 2993 kB in 0s (6533 kB/s)
(Reading database ... 53075 files and directories currently installed.)
Preparing to unpack .../python3.12-minimal_3.12.3-1ubuntu0.7_amd64.deb ...
Unpacking python3.12-minimal (3.12.3-1ubuntu0.7) over (3.12.3-1ubuntu0.7) ...
Preparing to unpack .../python3.12_3.12.3-1ubuntu0.7_amd64.deb ...
Unpacking python3.12 (3.12.3-1ubuntu0.7) over (3.12.3-1ubuntu0.7) ...
Setting up python3.12-minimal (3.12.3-1ubuntu0.7) ...
Setting up python3.12 (3.12.3-1ubuntu0.7) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for systemd (255.4-1ubuntu8.8) ...
bryan_@DESKTOP-NG2I0P2:~$ sudo apt install --reinstall python3-apt
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 0 not upgraded.
Need to get 169 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 python3-apt amd64 2.7.7ubuntu4 [169 kB]
Fetched 169 kB in 1s (270 kB/s)
(Reading database ... 53075 files and directories currently installed.)
Preparing to unpack .../python3-apt_2.7.7ubuntu4_amd64.deb ...
Unpacking python3-apt (2.7.7ubuntu4) over (2.7.7ubuntu4) ...
Setting up python3-apt (2.7.7ubuntu4) ...
bryan_@DESKTOP-NG2I0P2:~$ sudo update-alternatives --config python3
There is 1 choice for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                 Priority   Status
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
---
-
---
* 0            /usr/bin/python3.10   1         auto mode
  1            /usr/bin/python3.10   1         manual mode

Press <enter> to keep the current choice[*], or type selection number:

### GEMINI
You've done all the reinstall commands correctly, and python3.12 is indeed confirmed as Python 3.12.3. However, the output of sudo update-alternatives --config python3 is still problematic: There is 1 choice for the alternative python3 (providing /usr/bin/python3). Selection Path Priority Status -
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
--- * 0 /usr/bin/python3.10 1 auto mode 1 /usr/bin/python3.10 1 manual mode Press <enter> to keep the current choice[*], or type selection number: This is the core issue. Even though python3.12 is installed on your system, it is not appearing as an option to be set as the default python3 using update-alternatives. Ubuntu Noble (24.04) natively uses Python 3.12, so it should absolutely be an option here. This is likely why apt's internal scripts, which expect to use Python 3.12 with its apt_pkg module, are failing because python3 is pointing to 3.10. We need to explicitly register /usr/bin/python3.12 with the update-alternatives system. Action: Manually Add and Select Python 3.12 as an Alternative Press Enter to keep the current choice (Python 3.10) for now, as there's no other option presented. Add python3.12 as an alternative for python3: sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2 --install: This flag adds a new alternative. /usr/bin/python3: This is the generic link that we want to provide. python3: This is the "name" of the alternative group. /usr/bin/python3.12: This is the actual executable we want to add. 2: This is the "priority." A higher number means higher priority. We're giving it a low priority initially to make sure update-alternatives gives you a choice. Now, try configuring python3 alternatives again: sudo update-alternatives --config python3 This time, you should see python3.12 as an option. Select the number corresponding to /usr/bin/python3.12. Finally, attempt sudo apt update again: sudo apt update This should hopefully resolve the apt_pkg error for good. Please provide the full output of each of these commands.