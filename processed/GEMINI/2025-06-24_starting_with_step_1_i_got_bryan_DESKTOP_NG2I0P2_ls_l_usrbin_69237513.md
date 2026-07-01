---
category: coding
date: 2025-06-24
id: 919761
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is troubleshooting a Python symlink issue on their Linux system,
  checking the symbolic link for /usr/bin/python3.
tags:
- linux
- python
- symlink
- troubleshooting
- command-line
---
# starting with step 1 i got: bryan_@DESKTOP-NG2I0P2:~$ ls -l /usr/bin/python3lrwxrwxrwx 1 root root 25 Jun 24 13:59 /usr/bin/python3 -> /etc/alternatives/python3bryan_@DESKTOP-NG2I0P2:~$

### USER
starting with step 1 i got: bryan_@DESKTOP-NG2I0P2:~$ ls -l /usr/bin/python3lrwxrwxrwx 1 root root 25 Jun 24 13:59 /usr/bin/python3 -> /etc/alternatives/python3bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Okay, that's the expected output for ls -l /usr/bin/python3. It confirms that python3 is managed by the update-alternatives system. Now, let's see what update-alternatives currently has configured for python3 and, more importantly, choose the correct system Python 3 version that apt expects. Action: Continue with Step 2 (List and Configure Python 3 Alternatives) Run the following command: sudo update-alternatives --config python3 This will show you a list of all Python 3 installations known to your system that can be set as the default python3. Carefully examine the output. You'll see a numbered list. Look for the entry that points to the native Ubuntu Python 3 for your Noble Numbat release, which is likely python3.12 (e.g., /usr/bin/python3.12). Choose the number corresponding to /usr/bin/python3.12 (or whatever the system-default non-deadsnakes version is). Type that number and press Enter. Please provide the entire output of the sudo update-alternatives --config python3 command, including the options presented and the number you choose. After you've made your selection, we'll proceed to re-run sudo apt update.