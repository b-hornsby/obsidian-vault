---
category: coding
date: 2025-06-25
id: 703778
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
resolution: resolved
sentiment: frustrated
source: GEMINI
summary: N/A
tags:
- coding
- '''llm'''
- '''ai'''
- '''gemini'''
- '''python'''
- '''rust'''
- '''go'''
- '''error'''
---
# ran the  second conda command and got: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ conda install -c "nvidia/label/cuda-12.0" cublas -y\
>
Channels:
 - nvidia/label/cuda-12.0
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - cublas

Current channels:

  - https://conda.anaconda.org/nvidia/label/cuda-12.0
  - defaults

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


(llm-assist) bryan_@DESKTOP-NG2I0P2:~$ 

### USER
ran the  second conda command and got: (llm-assist) bryan_@DESKTOP-NG2I0P2:~$ conda install -c "nvidia/label/cuda-12.0" cublas -y\
>
Channels:
 - nvidia/label/cuda-12.0
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - cublas

Current channels:

  - https://conda.anaconda.org/nvidia/label/cuda-12.0
  - defaults

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


(llm-assist) bryan_@DESKTOP-NG2I0P2:~$ 

### GEMINI
You're absolutely right! My apologies. The nvidia/label/cuda-12.0 channel doesn't contain a package simply named cublas. Instead, the cuda-toolkit package from that channel typically includes cublas as part of its dependencies. Also, for cublas specifically, the package name is often libcublas and it's commonly found on the conda-forge channel or sometimes directly under the nvidia channel with more specific versioning like nvidia::libcublas. Let's adjust our strategy. Revised Action Plan: Confirm cuda-toolkit installation (from the first command): You ran conda install -c "nvidia/label/cuda-12.0" cuda-toolkit -y first. Did that command complete successfully? If it did, it should have brought in the necessary CUDA runtime libraries (like libcudart.so.12) and potentially libcublas as a dependency. Please confirm if that first conda install command finished without errors. If cuda-toolkit was successful, let's just try the pip install again. If the cuda-toolkit package from the nvidia channel successfully installed, it might have already resolved the libcudart and libcublas issues. export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib:$CUDA_HOME/lib64 CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir If the cuda-toolkit command also failed or if the pip install still fails with the same linking errors, then we'll need to try a different approach for cublas specifically: We can try installing libcublas from conda-forge. This is often a good fallback for many libraries. conda install -c conda-forge libcublas -y Then retry the pip install command. Please first confirm the success of your initial cuda-toolkit installation. Then, try the pip install again. If it fails, then proceed with the conda install -c conda-forge libcublas -y step.