---
id: 526332
source: GEMINI
date: 2025-07-05
tags: ['coding', 'module', 'gemini', 'model', 'oobabooga', 'gguf', 'hermes', 'text-generation']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ # Try to install flash-attn for CUDA 12.x
./installer_files/env/bin/pip install flash-attn --upgrade --no-build-isolation --extra-index-url https://download.pytorch.org/whl/cu121
Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cu121
Collecting flash-attn
  Downloading flash_attn-2.8.0.post2.tar.gz (7.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 47.5 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: torch in ./installer_files/env/lib/python3.11/site-packages (from flash-attn) (2.7.1)
Requirement already satisfied: einops in ./installer_files/env/lib/python3.11/site-packages (from flash-attn) (0.8.1)
Requirement already satisfied: filelock in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.13.1)
Requirement already satisfied: typing-extensions>=4.10.0 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (4.14.1)
Requirement already satisfied: sympy>=1.13.3 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (1.14.0)
Requirement already satisfied: networkx in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.3)
Requirement already satisfied: jinja2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.1.6)
Requirement already satisfied: fsspec in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (2024.6.1)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.80)
Requirement already satisfied: nvidia-cudnn-cu12==9.5.1.17 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (9.5.1.17)
Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (11.3.0.4)
Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (10.3.7.77)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (11.7.1.2)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.5.4.2)
Requirement already satisfied: nvidia-cusparselt-cu12==0.6.3 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (0.6.3)
Requirement already satisfied: nvidia-nccl-cu12==2.26.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (2.26.2)
Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.85)
Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (1.11.1.6)
Requirement already satisfied: triton==3.3.1 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.3.1)
Requirement already satisfied: setuptools>=40.8.0 in ./installer_files/env/lib/python3.11/site-packages (from triton==3.3.1->torch->flash-attn) (78.1.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./installer_files/env/lib/python3.11/site-packages (from sympy>=1.13.3->torch->flash-attn) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in ./installer_files/env/lib/python3.11/site-packages (from jinja2->torch->flash-attn) (2.1.5)
Building wheels for collected packages: flash-attn
  DEPRECATION: Building 'flash-attn' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'flash-attn'. Discussion can be found at https://github.com/pypa/pip/issues/6334
  Building wheel for flash-attn (setup.py) ... done
  Created wheel for flash-attn: filename=flash_attn-2.8.0.post2-cp311-cp311-linux_x86_64.whl size=255941661 sha256=8ed71ac092f80b079d2e6043b769135904d6e834916cb6da7d372b394581447b
  Stored in directory: /home/bryan_/.cache/pip/wheels/a2/75/55/57ba1e272fd7fa1a01d9ba6b5334b7adaabf79900ede22c040
Successfully built flash-attn
Installing collected packages: flash-attn
Successfully installed flash-attn-2.8.0.post2
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ # Try to install flash-attn for CUDA 12.x
./installer_files/env/bin/pip install flash-attn --upgrade --no-build-isolation --extra-index-url https://download.pytorch.org/whl/cu121
Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cu121
Collecting flash-attn
  Downloading flash_attn-2.8.0.post2.tar.gz (7.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 47.5 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: torch in ./installer_files/env/lib/python3.11/site-packages (from flash-attn) (2.7.1)
Requirement already satisfied: einops in ./installer_files/env/lib/python3.11/site-packages (from flash-attn) (0.8.1)
Requirement already satisfied: filelock in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.13.1)
Requirement already satisfied: typing-extensions>=4.10.0 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (4.14.1)
Requirement already satisfied: sympy>=1.13.3 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (1.14.0)
Requirement already satisfied: networkx in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.3)
Requirement already satisfied: jinja2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.1.6)
Requirement already satisfied: fsspec in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (2024.6.1)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.80)
Requirement already satisfied: nvidia-cudnn-cu12==9.5.1.17 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (9.5.1.17)
Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (11.3.0.4)
Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (10.3.7.77)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (11.7.1.2)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.5.4.2)
Requirement already satisfied: nvidia-cusparselt-cu12==0.6.3 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (0.6.3)
Requirement already satisfied: nvidia-nccl-cu12==2.26.2 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (2.26.2)
Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.77)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (12.6.85)
Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (1.11.1.6)
Requirement already satisfied: triton==3.3.1 in ./installer_files/env/lib/python3.11/site-packages (from torch->flash-attn) (3.3.1)
Requirement already satisfied: setuptools>=40.8.0 in ./installer_files/env/lib/python3.11/site-packages (from triton==3.3.1->torch->flash-attn) (78.1.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./installer_files/env/lib/python3.11/site-packages (from sympy>=1.13.3->torch->flash-attn) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in ./installer_files/env/lib/python3.11/site-packages (from jinja2->torch->flash-attn) (2.1.5)
Building wheels for collected packages: flash-attn
  DEPRECATION: Building 'flash-attn' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'flash-attn'. Discussion can be found at https://github.com/pypa/pip/issues/6334
  Building wheel for flash-attn (setup.py) ... done
  Created wheel for flash-attn: filename=flash_attn-2.8.0.post2-cp311-cp311-linux_x86_64.whl size=255941661 sha256=8ed71ac092f80b079d2e6043b769135904d6e834916cb6da7d372b394581447b
  Stored in directory: /home/bryan_/.cache/pip/wheels/a2/75/55/57ba1e272fd7fa1a01d9ba6b5334b7adaabf79900ede22c040
Successfully built flash-attn
Installing collected packages: flash-attn
Successfully installed flash-attn-2.8.0.post2
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! That's fantastic news. The output shows that flash-attn-2.8.0.post2 was successfully built and installed. The "DEPRECATION" warning is normal and can be ignored; it's just about an older way of building packages that will be phased out in future pip versions, but it didn't prevent the installation. This means the tricky flash-attention dependency should now be correctly installed and compatible with your PyTorch/CUDA setup. Step 3: Reinstall coqui_tts Requirements Now that flash-attn is in place, let's reinstall coqui_tts's requirements to ensure everything is properly linked. Ensure you are in the Oobabooga root directory: cd ~/text-generation-webui Reinstall coqui_tts requirements: ./installer_files/env/bin/pip install -r extensions/coqui_tts/requirements.txt --upgrade This should now pass without the ModuleNotFoundError for TTS or the flash_attn error. Step 4: Restart Oobabooga After this second installation is complete, restart the Oobabooga server. ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Crucially, monitor the terminal for the loading messages for both whisper_stt and coqui_tts. We are looking for: INFO Loading the extension "whisper_stt" (without errors below it) INFO Loading the extension "coqui_tts" (without errors below it) Once it's running, you can proceed to the web UI to download Coqui TTS models and test. Let me know the output of Step 3 and the subsequent server restart.