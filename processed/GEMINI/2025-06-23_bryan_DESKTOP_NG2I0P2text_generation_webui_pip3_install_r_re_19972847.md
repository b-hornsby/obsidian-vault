---
category: coding
date: 2025-06-23
id: 608349
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was trying to install Python dependencies for text-generation-webui
  but encountered an externally-managed-environment error, indicating they need to
  use a virtual environment instead of system-wide installation.
tags:
- python
- virtual-environment
- pip
- text-generation-webui
- dependency-installation
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip3 install -r requirements.txt
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip3 install -r requirements.txt
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You've hit a very common and important error in modern Linux distributions, especially Ubuntu: error: externally-managed-environment. This message indicates that Ubuntu (and other recent Linux distributions) are trying to prevent you from using pip to install packages globally into the system's Python installation. This is a good thing for system stability, as installing packages directly with pip can sometimes conflict with packages the operating system itself relies on, potentially "breaking" parts of your system. The recommended and best practice solution is to use a Python virtual environment. A virtual environment creates an isolated space for your project where you can install its specific dependencies without affecting the rest of your system's Python installations. This is the professional way to manage Python projects. Step 5: Create and Activate a Python Virtual Environment Action: We will create a virtual environment within your text-generation-webui directory, activate it, and then install the dependencies into that isolated environment. What I need you to do now (in your Ubuntu WSL2 terminal, still in ~/text-generation-webui): Create the Virtual Environment: Command: python3 -m venv .venv Explanation: python3 -m venv: This uses Python's built-in venv module to create a virtual environment. .venv: This is the name of the directory where your virtual environment will be created. The . makes it a hidden directory by default, which is common practice. Activate the Virtual Environment: You need to "activate" the virtual environment every time you open a new terminal session or start working on the project. Activating it tells your shell to use the Python and pip within this specific environment. Command: source .venv/bin/activate Explanation: source: This command executes the activate script. .venv/bin/activate: This is the path to the activation script within your newly created virtual environment. How to know it worked: After you run this, your terminal prompt should change. You'll typically see (.venv) or (venv) prepended to your prompt, like (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. This indicates that your virtual environment is active. Install Dependencies into the Virtual Environment: Now that the virtual environment is active, any pip install commands will install packages into this environment only, keeping them isolated from your system Python. Command: pip install -r requirements.txt Explanation: Notice we can now just use pip instead of pip3. When the virtual environment is active, pip (and python) in your PATH will automatically point to the versions inside your virtual environment. This command will now install all the necessary dependencies for oobabooga, including gradio, torch, transformers, etc., into your isolated .venv environment. What I need from you: Execute the python3 -m venv .venv command and confirm if it finishes without errors. Execute the source .venv/bin/activate command and confirm that your terminal prompt changes (you should see (.venv) at the beginning). Execute the pip install -r requirements.txt command. Copy and paste the entire output of the pip install -r requirements.txt command here. This step will take some time as it downloads and installs many packages. This is a crucial step towards getting oobabooga running correctly. Let's get these dependencies installed!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]