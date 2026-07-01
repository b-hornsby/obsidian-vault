---
category: homelab
date: 2025-06-24
id: 306561
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: resolved
sentiment: executing
source: GEMINI
summary: The user was performing routine system maintenance by updating package lists
  on their Ubuntu server, confirming all packages were already up to date.
tags:
- system-administration
- package-management
- linux-maintenance
- server-updates
- ubuntu
---
# bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:3 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:4 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Hit:5 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:3 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:4 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Hit:5 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Fantastic! Success! The sudo apt update command completed without any apt_pkg errors, and it reported "All packages are up to date." This means your system's Python environment for apt is now correctly configured. We've successfully resolved that stubborn system-level issue! Now that apt is working, we can finally proceed with installing the NVIDIA CUDA Toolkit within your WSL2 environment, which is necessary for building llama.cpp with GPU support. Action: Continue with Step 38 - Install NVIDIA CUDA Toolkit in WSL2 You should be in your home directory (bryan_@DESKTOP-NG2I0P2:~$). We will pick up from the beginning of Step 38, ensuring your system is ready for the CUDA Toolkit installation. Remove any previous NVIDIA keyrings and clean apt (start fresh for CUDA installation): sudo rm -f /etc/apt/sources.list.d/cuda.list sudo apt autoremove --purge 'cuda*' 'nvidia*' sudo apt clean sudo apt autoclean sudo apt update # Update again after cleaning Download and add the NVIDIA GPG key and repository: wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600 wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb sudo dpkg -i cuda-keyring_1.1-1_all.deb Update your package list and install CUDA Toolkit 11.8: sudo apt update sudo apt -y install cuda-toolkit-11-8 This command will download a significant amount of data (several GB) and will take a considerable amount of time. Be patient and let it complete fully. After the installation, add CUDA to your PATH environment variable: echo 'export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}' >> ~/.bashrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc source ~/.bashrc Verify the nvcc installation: nvcc --version This should output the CUDA compiler version, confirming the toolkit is found. Navigate back to your llama.cpp/build directory: cd ~/text-generation-webui/repositories/llama.cpp/build Clear the build directory again (important after installing new system dependencies): rm -rf * Re-run CMake to configure the build (this time it should find CUDA): cmake .. -DGGML_CUDA=ON Build the project: cmake --build . --config Release Please provide the full output of each of these commands as you go. This is a crucial sequence of steps to get llama.cpp compiled with GPU acceleration.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]