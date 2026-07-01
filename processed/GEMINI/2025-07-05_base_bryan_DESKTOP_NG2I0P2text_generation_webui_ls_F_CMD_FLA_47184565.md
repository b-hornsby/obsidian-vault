---
id: 512645
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'module', 'docker', 'ai', 'gemini', 'model', 'oobabooga', 'gguf']
category: ai-tools
sentiment: building
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md', 'nodes/projects/homelab-stack.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -F
CMD_FLAGS.txt            cmd_macos.sh*      extensions/       server.py                update_wizard_macos.sh*
Colab-TextGen-GPU.ipynb  cmd_windows.bat*   installer_files/  setup.cfg                update_wizard_windows.bat*
LICENSE                  css/               js/               start_linux.sh*          user_data/
README.md                docker/            modules/          start_macos.sh*
__pycache__/             docs/              one_click.py      start_windows.bat*
cmd_linux.sh*            download-model.py  requirements/     update_wizard_linux.sh*

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls -F
CMD_FLAGS.txt            cmd_macos.sh*      extensions/       server.py                update_wizard_macos.sh*
Colab-TextGen-GPU.ipynb  cmd_windows.bat*   installer_files/  setup.cfg                update_wizard_windows.bat*
LICENSE                  css/               js/               start_linux.sh*          user_data/
README.md                docker/            modules/          start_macos.sh*
__pycache__/             docs/              one_click.py      start_windows.bat*
cmd_linux.sh*            download-model.py  requirements/     update_wizard_linux.sh*

### GEMINI
Okay, I see the issue! You're right, there's no models/ directory directly visible in that listing. However, I see user_data/. It's very common for Oobabooga to store downloaded models within the user_data/models/ subdirectory. Let's check there: Ensure you are still in ~/text-generation-webui$. List the contents of the user_data/models/ directory: ls user_data/models/ This command should show you the .gguf files (or model folders containing .gguf files) that you've downloaded. Once we find the exact filename, we can proceed.