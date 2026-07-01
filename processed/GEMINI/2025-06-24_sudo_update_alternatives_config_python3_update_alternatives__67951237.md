---
id: 046697
source: GEMINI
date: 2025-06-24
tags: ['python-alternatives', 'python-version-management', 'local-llm-setup']
category: coding
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is configuring Python alternatives, likely to ensure the correct Python version is used for his local LLM setup.
---
# sudo update-alternatives --config python3
update-alternatives: using /usr/bin/python3.10 to provide /usr/bin/python3 (python3) in auto mode
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

### USER
sudo update-alternatives --config python3
update-alternatives: using /usr/bin/python3.10 to provide /usr/bin/python3 (python3) in auto mode
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
Perfect! This is exactly what we want to see. The output update-alternatives: using /usr/bin/python3.10 to provide /usr/bin/python3 (python3) in auto mode means that Python 3.10 has already been automatically selected as the default for python3. You don't need to type a number; just press Enter to confirm the current choice. After you press Enter, please run: python3 --version And confirm it shows Python 3.10.x. Once that's confirmed, we'll proceed with deleting and recreating the virtual environment. This is going very well!
