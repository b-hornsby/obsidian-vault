---
source: GEMINI
date: 2025-06-24
category: ai-tools
id: 29681923
linked_nodes: ['nodes/people/bryan.md']
---
-
---
--
* 0            /usr/bin/python3.10   1         auto mode
  1            /usr/bin/python3.10   1         manual mode

Press <enter> to keep the current choice[*], or type selection number:
### USER
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
You've encountered a critical piece of information here! The output of sudo update-alternatives --config python3 shows: There is 1 choice for the alternative python3 (providing /usr/bin/python3). Selection Path Priority Status -
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
--- * 0 /usr/bin/python3.10 1 auto mode 1 /usr/bin/python3.10 1 manual mode Press <enter> to keep the current choice[*], or type selection number: This is the problem: Your system only lists Python 3.10 as an option for python3 via update-alternatives! Ubuntu Noble Numbat (24.04), which you are using, natively ships with Python 3.12. The apt_pkg error is almost certainly happening because apt's internal scripts expect to run with the system's native Python 3.12, but your python3 symlink points to 3.10 (likely installed from the deadsnakes PPA). Action: Confirm and then Install/Reinstall System Python 3.12 For now, just press Enter to keep the current choice (Python 3.10). There's no better option presented right now. Confirm Python 3.12's status: Let's check if Python 3.12 is even installed or where its executable is. which python3.12 python3.12 --version If which or --version commands fail, it means it's not properly installed or in your PATH. Install/Reinstall Core Python 3.12 Packages: We need to ensure the native Python 3.12 and its essential components (which apt relies on) are correctly installed and registered. sudo apt update # Run update again just to be safe after previous failures sudo apt install --reinstall python3.12 python3.12-minimal python3.12-distutils sudo apt install --reinstall python3-apt # Reinstall apt_pkg source again The --reinstall flag forces apt to download and re-install these packages, ensuring they are not corrupted and register correctly. After the reinstallation, try to configure python3 alternatives again: sudo update-alternatives --config python3 Crucially, this time, look for python3.12 in the list. If python3.12 appears, select its corresponding number. If it still doesn't appear, we have a more severe problem with your apt or deadsnakes configuration. Finally, attempt sudo apt update again: sudo apt update Please provide the output of which python3.12, python3.12 --version, all the sudo apt install commands, the new sudo update-alternatives --config python3 output (and your selection), and finally, the new sudo apt update output. This is a crucial step to fix your system's Python environment.