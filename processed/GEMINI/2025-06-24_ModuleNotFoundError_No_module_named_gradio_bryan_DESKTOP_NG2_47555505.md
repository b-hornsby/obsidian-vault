---
category: coding
date: 2025-06-24
id: 184250
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- text-generation-webui
resolution: partial
sentiment: stuck
source: GEMINI
summary: The user encountered a dependency installation error when trying to install
  gradio for text-generation-webui due to an externally-managed Python environment,
  and received guidance on using virtual environments.
tags:
- python
- virtual-environment
- dependency-management
- gradio
- text-generation-webui
---
# ModuleNotFoundError: No module named 'gradio'
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install gradio
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
ModuleNotFoundError: No module named 'gradio'
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ pip install gradio
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
You've hit a very common road bump on newer Ubuntu/Debian systems! The error externally-managed-environment and the message about PEP 668 means that Ubuntu (specifically Python 3.12, which is likely what you have on 24.04) is trying to prevent you from installing Python packages directly into the system's core Python installation using pip. This is a good thing in principle, as it prevents accidentally breaking your operating system. However, for complex applications like text-generation-webui that have many Python dependencies, the recommended and best practice is to use a Python Virtual Environment. A virtual environment creates an isolated space for your Python project. When you install packages inside it, they don't affect your system's global Python installation. Action: Create and Use a Python Virtual Environment Here's how to create and activate a virtual environment, then install all the necessary dependencies for text-generation-webui (which includes gradio and many others): Make sure you are in your text-generation-webui directory: cd ~/text-generation-webui Create the Virtual Environment: We'll create a folder named venv (you can choose another name if you like) inside your text-generation-webui directory to hold the virtual environment. python3 -m venv venv (This command uses the venv module to create a new virtual environment.) Activate the Virtual Environment: You need to "activate" the virtual environment every time you open a new terminal or want to work on this project. You'll see (venv) appear at the beginning of your command prompt, indicating it's active. source venv/bin/activate Install all required packages into the Virtual Environment: text-generation-webui comes with a requirements.txt file that lists all its Python dependencies. This is the easiest way to install everything it needs. pip install -r requirements.txt This command will read the requirements.txt file and install all the necessary packages (including gradio, torch, transformers, etc.) into your newly created venv. This might take a few minutes as it downloads many packages. Run the text-generation-webui server (while the virtual environment is active!): python3 server.py --listen --model-menu Now, with gradio and all other dependencies installed within the isolated virtual environment, text-generation-webui should start up without the ModuleNotFoundError.