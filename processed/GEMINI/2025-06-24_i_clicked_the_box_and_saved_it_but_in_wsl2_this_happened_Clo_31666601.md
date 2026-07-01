---
category: homelab
date: 2025-06-24
id: 724912
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an error loading the 'superboogav2' extension in text-generation-webui
  on WSL2, which failed due to a Python import error.
tags:
- WSL2
- text-generation-webui
- superboogav2
- extension-error
- port-7860
---
# i clicked the box and saved it but in wsl2 this happened: Closing server running on port: 7860
13:04:55-115670 INFO     Loading the extension "superboogav2"
13:05:00-233187 ERROR    Failed to load the extension "superboogav2".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1976, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/modeling_utils.py", line 54, in <module>
    from .integrations.flash_attention import flash_attention_forward
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/integrations/flash_attention.py", line 5, in <module>
    from ..modeling_flash_attention_utils import _flash_attention_forward
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/modeling_flash_attention_utils.py", line 29, in <module>
    from flash_attn.bert_padding import index_first_axis, pad_input, unpad_input  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/__init__.py", line 3, in <module>
    from flash_attn.flash_attn_interface import (
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/flash_attn_interface.py", line 15, in <module>
    import flash_attn_2_cuda as flash_attn_gpu
ImportError: /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1976, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/integrations/integration_utils.py", line 36, in <module>
    from .. import PreTrainedModel, TFPreTrainedModel
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1964, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1978, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.modeling_utils because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/extensions.py", line 46, in load_extensions
    extension.setup()
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/script.py", line 43, in setup
    collector = make_collector()
                ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py", line 357, in make_collector
    return ChromaCollector()
           ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py", line 81, in __init__
    self.embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py", line 32, in __init__
    from sentence_transformers import SentenceTransformer
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/__init__.py", line 14, in <module>
    from sentence_transformers.cross_encoder.CrossEncoder import CrossEncoder
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/cross_encoder/__init__.py", line 3, in <module>
    from .CrossEncoder import CrossEncoder
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/cross_encoder/CrossEncoder.py", line 18, in <module>
    from sentence_transformers.evaluation.SentenceEvaluator import SentenceEvaluator
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/evaluation/__init__.py", line 9, in <module>
    from .NanoBEIREvaluator import NanoBEIREvaluator
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py", line 11, in <module>
    from sentence_transformers import SentenceTransformer
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 33, in <module>
    from sentence_transformers.model_card import SentenceTransformerModelCardData, generate_model_card
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/model_card.py", line 25, in <module>
    from transformers.integrations import CodeCarbonCallback
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1964, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1978, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.integrations.integration_utils because of the following error (look up to see its traceback):
Failed to import transformers.modeling_utils because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

Running on local URL:  http://127.0.0.1:7860

### USER
i clicked the box and saved it but in wsl2 this happened: Closing server running on port: 7860
13:04:55-115670 INFO     Loading the extension "superboogav2"
13:05:00-233187 ERROR    Failed to load the extension "superboogav2".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1976, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/modeling_utils.py", line 54, in <module>
    from .integrations.flash_attention import flash_attention_forward
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/integrations/flash_attention.py", line 5, in <module>
    from ..modeling_flash_attention_utils import _flash_attention_forward
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/modeling_flash_attention_utils.py", line 29, in <module>
    from flash_attn.bert_padding import index_first_axis, pad_input, unpad_input  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/__init__.py", line 3, in <module>
    from flash_attn.flash_attn_interface import (
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn/flash_attn_interface.py", line 15, in <module>
    import flash_attn_2_cuda as flash_attn_gpu
ImportError: /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1976, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/integrations/integration_utils.py", line 36, in <module>
    from .. import PreTrainedModel, TFPreTrainedModel
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1964, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1978, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.modeling_utils because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/extensions.py", line 46, in load_extensions
    extension.setup()
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/script.py", line 43, in setup
    collector = make_collector()
                ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py", line 357, in make_collector
    return ChromaCollector()
           ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py", line 81, in __init__
    self.embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py", line 32, in __init__
    from sentence_transformers import SentenceTransformer
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/__init__.py", line 14, in <module>
    from sentence_transformers.cross_encoder.CrossEncoder import CrossEncoder
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/cross_encoder/__init__.py", line 3, in <module>
    from .CrossEncoder import CrossEncoder
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/cross_encoder/CrossEncoder.py", line 18, in <module>
    from sentence_transformers.evaluation.SentenceEvaluator import SentenceEvaluator
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/evaluation/__init__.py", line 9, in <module>
    from .NanoBEIREvaluator import NanoBEIREvaluator
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/evaluation/NanoBEIREvaluator.py", line 11, in <module>
    from sentence_transformers import SentenceTransformer
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 33, in <module>
    from sentence_transformers.model_card import SentenceTransformerModelCardData, generate_model_card
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/sentence_transformers/model_card.py", line 25, in <module>
    from transformers.integrations import CodeCarbonCallback
  File "<frozen importlib._bootstrap>", line 1229, in _handle_fromlist
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1964, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/transformers/utils/import_utils.py", line 1978, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.integrations.integration_utils because of the following error (look up to see its traceback):
Failed to import transformers.modeling_utils because of the following error (look up to see its traceback):
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Excellent! You've provided a very clear error message, and this is a common one when dealing with deep learning libraries and specific hardware optimizations like Flash Attention. The core of the problem is this line: ImportError: /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationESs This indicates an issue with flash_attn_2_cuda. flash_attn is a highly optimized attention mechanism (a core part of how LLMs work) that aims to make things much faster, especially on NVIDIA GPUs like your RTX 3070. The "undefined symbol" error usually means one of a few things: Mismatched CUDA/PyTorch versions: The flash_attn library was compiled with a specific version of CUDA (NVIDIA's platform for GPU computing) or PyTorch (the deep learning framework that Oobabooga and Flash Attention rely on), and your currently installed CUDA or PyTorch version in your .venv is incompatible. Missing system libraries: Less likely in WSL2 for this specific error, but sometimes underlying system libraries that flash_attn depends on aren't correctly linked. Compilation issue: flash_attn is often compiled from source, and if the compilation environment wasn't perfect, it can lead to these errors. Given your goal of maximizing performance, flash_attn is something you do want to use eventually. However, to get superboogav2 working now and get your RAG capabilities online, we can temporarily disable flash_attn or address the underlying transformers library issue. The error path also shows: Failed to import transformers.integrations.integration_utils because of the following error (look up to see its traceback): Failed to import transformers.modeling_utils because of the following error (look up to see its traceback):. This means superboogav2 tries to import sentence_transformers, which in turn tries to import transformers, and that is where the flash_attn issue hits. Let's try to update your transformers and torch libraries first, as this often resolves such dependency conflicts. Step 5: Update transformers and torch for compatibility Sometimes, simply updating these core libraries can pull in compatible versions of dependencies or resolve compilation issues. Action: Stop Oobabooga again. (If it's still running from the previous step). Press Ctrl + C in the terminal until you see your prompt. Ensure your virtual environment is active. You should see (.venv) at the beginning of your prompt. If not, activate it: cd ~/text-generation-webui source .venv/bin/activate Upgrade transformers and torch: We'll use the --upgrade flag to ensure we get the latest compatible versions. pip install --upgrade transformers torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --index-url https://download.pytorch.org/whl/cu121: This is critical. It tells pip to specifically look for PyTorch packages compiled for CUDA 12.1. Given your 3070, this is a very common and recommended CUDA version. This helps ensure PyTorch (and by extension, libraries like flash_attn that integrate with it) are built for your GPU setup. This command might take a while as it downloads and installs potentially new versions of PyTorch and Transformers. Note: If you get a message about flash_attn not supporting CUDA 12.1, or other specific CUDA errors, or if it says it's already up to date, please paste the full output. Once this command finishes, we'll try restarting Oobabooga and enabling superboogav2 again.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]