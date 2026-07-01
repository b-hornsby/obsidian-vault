---
category: homelab
date: 2025-06-19
id: 383582
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: exploratory
source: GEMINI
summary: The user was exploring the requirements files in the text-generation-webui
  project to understand dependency configurations for different hardware setups (AMD,
  Apple Silicon, CPU-only).
tags:
- text-generation-webui
- requirements
- local-ai
- python-venv
- dependency-management
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/requirements/full$ ls -l
total 44
-rw-r--r-- 1 bryan_ bryan_ 2283 Jun 18 21:29 requirements.txt
-rw-r--r-- 1 bryan_ bryan_ 1170 Jun 18 21:29 requirements_amd.txt
-rw-r--r-- 1 bryan_ bryan_ 1176 Jun 18 21:29 requirements_amd_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 1137 Jun 18 21:29 requirements_apple_intel.txt
-rw-r--r-- 1 bryan_ bryan_ 1389 Jun 18 21:29 requirements_apple_silicon.txt
-rw-r--r-- 1 bryan_ bryan_  859 Jun 18 21:29 requirements_cpu_only.txt
-rw-r--r-- 1 bryan_ bryan_  860 Jun 18 21:29 requirements_cpu_only_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2292 Jun 18 21:29 requirements_cuda128.txt
-rw-r--r-- 1 bryan_ bryan_ 2298 Jun 18 21:29 requirements_cuda128_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2289 Jun 18 21:29 requirements_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_  415 Jun 18 21:29 requirements_nowheels.txt
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/requirements/full$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/requirements/full$ ls -l
total 44
-rw-r--r-- 1 bryan_ bryan_ 2283 Jun 18 21:29 requirements.txt
-rw-r--r-- 1 bryan_ bryan_ 1170 Jun 18 21:29 requirements_amd.txt
-rw-r--r-- 1 bryan_ bryan_ 1176 Jun 18 21:29 requirements_amd_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 1137 Jun 18 21:29 requirements_apple_intel.txt
-rw-r--r-- 1 bryan_ bryan_ 1389 Jun 18 21:29 requirements_apple_silicon.txt
-rw-r--r-- 1 bryan_ bryan_  859 Jun 18 21:29 requirements_cpu_only.txt
-rw-r--r-- 1 bryan_ bryan_  860 Jun 18 21:29 requirements_cpu_only_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2292 Jun 18 21:29 requirements_cuda128.txt
-rw-r--r-- 1 bryan_ bryan_ 2298 Jun 18 21:29 requirements_cuda128_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_ 2289 Jun 18 21:29 requirements_noavx2.txt
-rw-r--r-- 1 bryan_ bryan_  415 Jun 18 21:29 requirements_nowheels.txt
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/requirements/full$

### GEMINI
Eureka! We found them! Your ls -l output from /home/bryan/text-generation-webui/requirements/full clearly shows a variety of requirements_*.txt files. Since you're running on WSL2 (which is Linux-based), you typically want the CUDA-enabled requirements if your GPU is an NVIDIA card and you have CUDA set up in WSL2. If you don't have an NVIDIA GPU, or don't plan to use it for acceleration, you might opt for a CPU-only version. Given the options, the most common choices for WSL2 with NVIDIA GPU support are: requirements_cuda128.txt: This is for systems with NVIDIA GPUs and CUDA 12.1/12.2. This is usually the one you want if you have an NVIDIA GPU. requirements_cuda128_noavx2.txt: Same as above, but for CPUs that do not support AVX2 instructions (less common for modern CPUs, but good to know). requirements.txt: This is the default or most generic one, which might attempt to install a CPU-only version or a general GPU version. requirements_cpu_only.txt: If you only want to run on your CPU, choose this. To install the requirements, you have two options: Option 1: (Recommended for NVIDIA GPU users in WSL2) If you have an NVIDIA GPU and want to use it for accelerating the LLM, use the CUDA-specific requirements: pip install -r requirements_cuda128.txt Option 2: (General or if you prefer the default/CPU) If you just want the default setup or are focusing on CPU-only for now: pip install -r requirements.txt Important: You are currently in the /home/bryan/text-generation-webui/requirements/full directory. The commands above assume you are still in this directory. Choose the appropriate requirements_*.txt file based on your hardware and desired setup, and run the pip install command. This should finally get you past the file not found error!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]