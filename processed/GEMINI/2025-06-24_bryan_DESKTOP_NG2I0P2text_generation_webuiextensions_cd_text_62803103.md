---
category: coding
date: 2025-06-24
id: 888773
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- text-generation-webui
resolution: unresolved
sentiment: curious
source: GEMINI
summary: The user encountered an error while trying to install Python packages in
  a system-managed environment without using a virtual environment.
tags:
- python
- package-management
- virtual-environment
- text-generation-webui
- superboogav2
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ cd ~/text-generation-webui/extensions/superboogav2
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions/superboogav2$ pip install -r requirements.txt
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions/superboogav2$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ cd ~/text-generation-webui/extensions/superboogav2
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions/superboogav2$ pip install -r requirements.txt
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions/superboogav2$

### GEMINI
Ah, yes! This is a very common error in recent versions of Debian/Ubuntu (which WSL2 often uses) and Python. It's related to PEP 668 and the "externally managed environment" concept. Basically, your system is trying to prevent you from installing Python packages globally, which could break system tools that rely on specific Python versions or packages. The good news is, your Oobabooga installation already uses a virtual environment (that .venv folder you saw). We just need to tell pip to use that specific virtual environment's pip. You mentioned your usual start command: source .venv/bin/activate followed by python3 server.py. The source .venv/bin/activate part is what activates the virtual environment. When that's active, the pip command should automatically point to the one inside your .venv. Let's try this a slightly different way to ensure we're using the correct pip. Step 4b (Revised): Install superboogav2 requirements using the virtual environment's pip. Action: Ensure you are in the main text-generation-webui directory. This is where your .venv resides. cd ~/text-generation-webui Activate your virtual environment. This step is crucial. source .venv/bin/activate After running this, your terminal prompt might change slightly, often showing (.venv) at the beginning, like (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. This indicates your virtual environment is active. Now, navigate back to the superboogav2 extension directory: cd extensions/superboogav2 Run the pip install command again. Because the virtual environment is now active, the pip command should correctly target the pip within your .venv, avoiding the "externally-managed-environment" error. pip install -r requirements.txt Please execute these commands carefully, and if you encounter any errors this time, paste them here. This should resolve the externally-managed-environment issue.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]