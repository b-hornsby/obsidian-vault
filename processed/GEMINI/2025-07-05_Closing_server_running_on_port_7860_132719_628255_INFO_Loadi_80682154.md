---
id: 247258
source: GEMINI
date: 2025-07-05
tags: ['coding', 'module', 'ai', 'gpt', 'gemini', 'model', 'oobabooga', 'rag']
category: coding
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# Closing server running on port: 7860
13:27:19-628255 INFO     Loading the extension "superboogav2"
13:27:19-629055 INFO     Loading the extension "web_rag"
13:27:19-629535 INFO     Loading the extension "whisper_stt"
13:27:22-800723 INFO     Loading the extension "coqui_tts"
13:28:25-828616 ERROR    Failed to load the extension "coqui_tts".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1778, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/models/gpt2/modeling_gpt2.py", line 58, in <module>
    from ...modeling_flash_attention_utils import _flash_attention_forward
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/modeling_flash_attention_utils.py", line 27, in <module>
    from flash_attn.bert_padding import index_first_axis, pad_input, unpad_input  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn/__init__.py", line 3, in <module>
    from flash_attn.flash_attn_interface import (
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn/flash_attn_interface.py", line 15, in <module>
    import flash_attn_2_cuda as flash_attn_gpu
ImportError: /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/extensions.py", line 37, in load_extensions
    extension = importlib.import_module(f"extensions.{name}.script")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/extensions/coqui_tts/script.py", line 10, in <module>
    from TTS.api import TTS
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/__init__.py", line 16, in <module>
    from TTS.tts.configs.xtts_config import XttsConfig
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/configs/xtts_config.py", line 5, in <module>
    from TTS.tts.models.xtts import XttsArgs, XttsAudioConfig
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/models/xtts.py", line 14, in <module>
    from TTS.tts.layers.xtts.gpt import GPT
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/layers/xtts/gpt.py", line 10, in <module>
    from TTS.tts.layers.tortoise.autoregressive import (
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/layers/tortoise/autoregressive.py", line 11, in <module>
    from transformers import GPT2Config, GPT2PreTrainedModel, LogitsProcessorList
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1767, in __getattr__
    value = getattr(module, name)
            ^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1766, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1780, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.models.gpt2.modeling_gpt2 because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

Running on local URL:  http://127.0.0.1:7860

### USER
Closing server running on port: 7860
13:27:19-628255 INFO     Loading the extension "superboogav2"
13:27:19-629055 INFO     Loading the extension "web_rag"
13:27:19-629535 INFO     Loading the extension "whisper_stt"
13:27:22-800723 INFO     Loading the extension "coqui_tts"
13:28:25-828616 ERROR    Failed to load the extension "coqui_tts".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1778, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/models/gpt2/modeling_gpt2.py", line 58, in <module>
    from ...modeling_flash_attention_utils import _flash_attention_forward
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/modeling_flash_attention_utils.py", line 27, in <module>
    from flash_attn.bert_padding import index_first_axis, pad_input, unpad_input  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn/__init__.py", line 3, in <module>
    from flash_attn.flash_attn_interface import (
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn/flash_attn_interface.py", line 15, in <module>
    import flash_attn_2_cuda as flash_attn_gpu
ImportError: /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/extensions.py", line 37, in load_extensions
    extension = importlib.import_module(f"extensions.{name}.script")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/extensions/coqui_tts/script.py", line 10, in <module>
    from TTS.api import TTS
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/__init__.py", line 16, in <module>
    from TTS.tts.configs.xtts_config import XttsConfig
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/configs/xtts_config.py", line 5, in <module>
    from TTS.tts.models.xtts import XttsArgs, XttsAudioConfig
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/models/xtts.py", line 14, in <module>
    from TTS.tts.layers.xtts.gpt import GPT
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/layers/xtts/gpt.py", line 10, in <module>
    from TTS.tts.layers.tortoise.autoregressive import (
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/TTS/tts/layers/tortoise/autoregressive.py", line 11, in <module>
    from transformers import GPT2Config, GPT2PreTrainedModel, LogitsProcessorList
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1767, in __getattr__
    value = getattr(module, name)
            ^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1766, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1780, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.models.gpt2.modeling_gpt2 because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Okay, this is a more complex error, and it's specifically affecting coqui_tts (whisper_stt seems to be loading fine now, which is good!). The core of the problem for coqui_tts is this: ImportError: /home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs And the RuntimeError: Failed to import transformers.models.gpt2.modeling_gpt2 because of the following error... This error indicates an incompatibility or a broken installation related to flash_attn_2_cuda. flash-attention is a highly optimized library often used with Transformers to speed up attention mechanisms, especially on GPUs. The "undefined symbol" error typically means that a compiled component (like flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so) expects a symbol or function from a specific version of a CUDA or PyTorch library, and it's not finding it, or it's finding an incompatible version. This often happens due to: Incompatible CUDA toolkit versions. Incompatible PyTorch versions with flash-attention. Issues with the transformers library trying to use flash-attention when it's not correctly set up for your specific environment. What to do: The coqui_tts library, especially when it pulls in transformers components like GPT2 models (which use attention mechanisms), can have very specific dependency requirements, particularly around CUDA and PyTorch. Given this complex error, we have a few paths: Attempt a focused reinstallation/fix for Coqui TTS and its dependencies. Try silero_tts instead (as it might have simpler dependencies). Troubleshoot the flash_attn issue directly (most complex). Let's try a targeted fix for coqui_tts first. This error often comes from flash-attention being built against a slightly different CUDA/PyTorch version than what's currently active. Attempted Fix for coqui_tts (flash_attn issue) We will try to force a reinstallation of flash-attention and then reinstall coqui_tts's requirements. Stop Oobabooga: If Oobabooga is still running, press Ctrl+C in your WSL2 terminal to stop it. Uninstall flash-attention related packages: ./installer_files/env/bin/pip uninstall -y flash-attn flash-attn-2-cuda This removes any potentially problematic existing installations. Reinstall flash-attention (specifically for your setup if possible, or a general version): # This command tries to install flash-attention based on your PyTorch and CUDA version # If it fails, we might need a more specific wheel or to skip it. ./installer_files/env/bin/pip install --no-index flash-attn --find-links https://download.pytorch.org/whl/cu121/torch_stable.html Note: The cu121 in the URL implies CUDA 12.1. Your system uses CUDA 12.6. If this command fails, it's likely due to a mismatch. We might need to adjust this URL or try a CPU-only version first for flash-attention. Reinstall coqui_tts requirements (which will pull in its specific transformers and other dependencies): ./installer_files/env/bin/pip install -r extensions/coqui_tts/requirements.txt --upgrade Restart Oobabooga: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Important: This flash-attention error can be tricky. If the above steps don't work, we might consider switching to silero_tts as it often has fewer complex GPU-specific dependencies. Please share the full output of each step.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]