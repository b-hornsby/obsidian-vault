---
source: GEMINI
date: 2025-06-24
category: ai-tools
id: 77138635
linked_nodes: ['nodes/people/bryan.md']
---
-
---
--
* 0            /usr/bin/python3.12   2         auto mode
  1            /usr/bin/python3.10   1         manual mode
  2            /usr/bin/python3.12   2         manual mode

Press <enter> to keep the current choice[*], or type selection number:
### USER
bryan_@DESKTOP-NG2I0P2:~$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
update-alternatives: using /usr/bin/python3.12 to provide /usr/bin/python3 (python3) in auto mode
bryan_@DESKTOP-NG2I0P2:~$ sudo update-alternatives --config python3
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

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
* 0            /usr/bin/python3.12   2         auto mode
  1            /usr/bin/python3.10   1         manual mode
  2            /usr/bin/python3.12   2         manual mode

Press <enter> to keep the current choice[*], or type selection number:

### GEMINI
Excellent! This is exactly what we wanted to see! The line * 0 /usr/bin/python3.12 2 auto mode confirms that /usr/bin/python3 is now correctly pointing to python3.12, and it's already selected as the active choice. Action: Simply press Enter to accept the current choice (which is 0 /usr/bin/python3.12). Finally, run sudo apt update one more time. This should now complete without the apt_pkg error. sudo apt update Please provide the full output of this sudo apt update command. This should resolve the system Python issue, and we can then proceed with installing the CUDA Toolkit.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]