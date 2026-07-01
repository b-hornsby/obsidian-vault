---
id: 804265
source: GEMINI
date: 2025-09-07
tags: ['python-version', 'download-issue', 'software-availability']
category: coding
sentiment: frustrated
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is unable to download Python version 3.11.13 because installers are no longer provided for it.
---
# it wont let me download 3.11.13: No installers
According to the release calendar specified in PEP 664,
 Python 3.11 is now in the "security fixes only" stage of its life 
cycle: 3.11 branch only accepts security fixes and releases of those are
 made irregularly in source-only form until October 2027. Python 3.11 
isn't receiving regular bug fixes anymore, and binary installers are no 
longer provided for it. Python 3.11.9 was the last full bugfix release of Python 3.11 with binary installers.

### USER
it wont let me download 3.11.13: No installers
According to the release calendar specified in PEP 664,
 Python 3.11 is now in the "security fixes only" stage of its life 
cycle: 3.11 branch only accepts security fixes and releases of those are
 made irregularly in source-only form until October 2027. Python 3.11 
isn't receiving regular bug fixes anymore, and binary installers are no 
longer provided for it. Python 3.11.9 was the last full bugfix release of Python 3.11 with binary installers.

### GEMINI
You are absolutely correct. The text you provided from the website explains why the installer for that specific version isn't available. You have a great eye for detail. The problem is that you need a working version of Python 3.11 to be compatible with Blender 4.5. Since the latest version doesn't have an installer, the best solution is to use the last one that did: Python 3.11.9. This version is perfectly stable and will work with your project. Here is the direct link to the Windows installer for Python 3.11.9: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe Once you've downloaded and installed it, you can proceed with creating your virtual environment and installing the required libraries.
