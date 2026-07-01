---
category: homelab
date: 2025-06-24
id: 038308
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user attempted to manually download a specific version of the libtinfo5
  package for Ubuntu but encountered a 404 error, indicating the file is no longer
  available at the expected URL.
tags:
- linux
- package-management
- ubuntu
- dependency-resolution
- system-administration
---
# bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:48:08--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 91.189.91.82, 91.189.91.81, 185.125.190.81, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|91.189.91.82|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:48:08 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ wget http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
--2025-06-24 14:48:08--  http://security.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
Resolving security.ubuntu.com (security.ubuntu.com)... 91.189.91.82, 91.189.91.81, 185.125.190.81, ...
Connecting to security.ubuntu.com (security.ubuntu.com)|91.189.91.82|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-06-24 14:48:08 ERROR 404: Not Found.

bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
The persistent 404 Not Found error for libtinfo5_6.3-2ubuntu0.1_amd64.deb, despite your network working, points to a deeper compatibility issue: You are running Ubuntu 24.04 (Noble Numbat). However, cuda-toolkit-11-8 is primarily designed for Ubuntu 22.04 (Jammy Jellyfish). The dependency on libtinfo5 is a classic symptom of trying to install older software onto a newer Ubuntu release that uses updated libraries (like libtinfo6 or libncursesw6). The nsight-systems-2022.4.2 component in CUDA 11.8 specifically needs that older libtinfo5, which is causing the installation failure. The most robust and recommended solution is to install a version of the NVIDIA CUDA Toolkit that is officially supported for Ubuntu 24.04 (Noble Numbat). NVIDIA has released newer CUDA Toolkit versions that are compatible with your operating system. For Ubuntu 24.04, CUDA 12.5 (or the latest 12.x series) is the recommended choice. Action: Switch to CUDA Toolkit 12.x for Ubuntu 24.04 We need to: Remove the existing CUDA 11.8 repository configuration. Add the repository for the newer CUDA 12.x toolkit (e.g., 12.5) that supports Ubuntu 24.04. Install the correct CUDA toolkit. Step 1: Clean Up Old CUDA Repository and Cache sudo rm -f /etc/apt/sources.list.d/cuda.list # Remove old CUDA repo sudo rm -f /etc/apt/preferences.d/cuda-repository-pin-600 # Remove old pinning sudo rm -f cuda-keyring_1.1-1_all.deb # Remove downloaded keyring sudo apt autoremove --purge 'cuda*' 'nvidia*' # Clean up any partially installed CUDA/NVIDIA packages sudo apt update sudo apt clean sudo apt autoclean Step 2: Install CUDA Toolkit 12.5 for Ubuntu 24.04 (Noble) These instructions are directly from NVIDIA's official CUDA Toolkit download page for Linux -> x86_64 -> Ubuntu -> 24.04 -> deb (network). # Download and install the new CUDA GPG key and repository for Noble (24.04) wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600 wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb sudo dpkg -i cuda-keyring_1.1-1_all.deb # Update your package list to include the new repository sudo apt update # Install the CUDA Toolkit 12.5 (this will be a large download) sudo apt -y install cuda-toolkit-12-5 This sudo apt -y install cuda-toolkit-12-5 command will download several gigabytes and will take a long time. Please be patient and let it complete. Step 3: Update PATH and Verify CUDA Installation # Add CUDA 12.5 to your PATH environment variable echo 'export PATH=/usr/local/cuda-12.5/bin${PATH:+:${PATH}}' >> ~/.bashrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.5/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc source ~/.bashrc # Verify the nvcc installation (should show CUDA 12.5) nvcc --version Step 4: Re-compile llama.cpp # Navigate back to your llama.cpp build directory cd ~/text-generation-webui/repositories/llama.cpp/build # Clear the build directory rm -rf * # Re-run CMake to configure the build (it should now find CUDA 12.5) cmake .. -DGGML_CUDA=ON # Build the project cmake --build . --config Release This is a comprehensive set of commands. Please execute them one by one, and provide the full output for each, especially for the large sudo apt -y install cuda-toolkit-12-5 command. This should finally get CUDA working correctly for llama.cpp.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]