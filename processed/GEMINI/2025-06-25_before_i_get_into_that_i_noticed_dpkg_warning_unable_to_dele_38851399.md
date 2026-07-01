---
id: 286727
source: GEMINI
date: 2025-06-25
tags: ['dpkg-warning', 'systemd', 'wsl2', 'package-management']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan noticed dpkg warnings about being unable to delete old systemd directories and asked about them.
---
# before i get into that i noticed: dpkg: warning: unable to delete old directory '/lib/systemd/system-generators': Directory not empty
dpkg: warning: unable to delete old directory '/lib/systemd/system/sshd-keygen@.service.d': Directory not empty

### USER
before i get into that i noticed: dpkg: warning: unable to delete old directory '/lib/systemd/system-generators': Directory not empty
dpkg: warning: unable to delete old directory '/lib/systemd/system/sshd-keygen@.service.d': Directory not empty

### GEMINI
Thanks for pointing that out! That's a good observation, and it's completely normal to see warnings like that during a large upgrade process. Let's break down what those dpkg warnings mean: dpkg: This is the "Debian Package" tool, which is the underlying system that apt uses to install, remove, and manage software packages on Ubuntu. warning: unable to delete old directory: This means that when the upgrade command was trying to update some system components, it attempted to remove old versions of directories. However, those directories weren't completely empty. Why would they not be empty? Sometimes, other parts of the system or other installed software might have placed temporary or configuration files inside those directories after the initial installation but before the upgrade. When dpkg tries to delete the old directory, it finds these new files and, as a safety measure, it warns you and leaves the non-empty directory behind rather than deleting files it didn't create. Are these a problem? No, these specific warnings are not critical errors and will not prevent you from moving forward or impact your LLM project. Your sudo apt upgrade -y command did complete successfully, and all the necessary new files were installed. These are just minor "leftovers" that are very common in Linux environments after large system updates. You have a perfectly healthy, updated Ubuntu environment. You are good to proceed with installing the essential development tools and GPU support. Go ahead with that command when you're ready: sudo apt install build-essential git nvidia-cuda-toolkit -y
