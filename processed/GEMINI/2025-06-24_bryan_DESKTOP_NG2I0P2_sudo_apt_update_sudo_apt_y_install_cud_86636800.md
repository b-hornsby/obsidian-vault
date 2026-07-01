---
category: homelab
date: 2025-06-24
id: 456819
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: executing
source: GEMINI
summary: The user is setting up a CUDA toolkit installation on WSL Ubuntu for their
  homelab environment, working through package manager configuration and NVIDIA repository
  setup.
tags:
- CUDA installation
- NVIDIA drivers
- WSL Ubuntu
- GPU setup
- package management
---
# bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
sudo apt -y install cuda-toolkit-11-8
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Get:2 https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64  InRelease [1581 B]
Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Get:7 https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64  Packages [640 kB]
Fetched 641 kB in 1s (741 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nsight-systems-2022.4.2 : Depends: libtinfo5 but it is not installable
E: Unable to correct problems, you have held broken packages.
bryan_@DESKTOP-NG2I0P2:~$

### USER
bryan_@DESKTOP-NG2I0P2:~$ sudo apt update
sudo apt -y install cuda-toolkit-11-8
Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
Get:2 https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64  InRelease [1581 B]
Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease
Get:7 https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64  Packages [640 kB]
Fetched 641 kB in 1s (741 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nsight-systems-2022.4.2 : Depends: libtinfo5 but it is not installable
E: Unable to correct problems, you have held broken packages.
bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
You've hit another common roadblock when installing specific versions of software on newer Linux distributions: unmet dependencies for older libraries. The error message: The following packages have unmet dependencies: nsight-systems-2022.4.2 : Depends: libtinfo5 but it is not installable E: Unable to correct problems, you have held broken packages. This means that nsight-systems-2022.4.2 (a profiling tool that is part of the CUDA Toolkit installation) requires libtinfo5, but libtinfo5 is not available in the repositories for your Ubuntu 24.04 (Noble Numbat). Newer Ubuntu versions often replace older libraries with updated versions (e.g., libtinfo6 or libncursesw6). To proceed with the CUDA Toolkit installation, we need to make libtinfo5 available. The most common workaround for this on newer Ubuntu versions is to manually download and install the libtinfo5 package from an older, compatible Ubuntu release (like Ubuntu 22.04 "Jammy Jellyfish"). Action: Manually Install libtinfo5 from Ubuntu 22.04 Navigate to your home directory: cd ~ Download the libtinfo5 .deb package for Ubuntu 22.04 (Jammy): wget http://archive.ubuntu.com/ubuntu/pool/main/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb Install the downloaded .deb package: sudo dpkg -i libtinfo5_6.3-2ubuntu0.1_amd64.deb If dpkg complains about other dependencies, you might need to run sudo apt --fix-broken install immediately after. Clean up apt's cache and try to install cuda-toolkit-11-8 again: sudo apt update --fix-missing sudo apt -y install cuda-toolkit-11-8 The --fix-missing might help if any packages are partially downloaded. Please provide the full output of each of these commands. If libtinfo5 installs successfully, the cuda-toolkit should then proceed.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]