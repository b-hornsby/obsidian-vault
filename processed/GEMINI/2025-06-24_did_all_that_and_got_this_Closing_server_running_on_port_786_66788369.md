---
category: coding
date: 2025-06-24
id: 109679
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an error loading the 'superboogav2' extension in text-generation-webui,
  with a Python import failure traceback, and is seeking help to resolve the issue.
tags:
- text-generation-webui
- extension-loading-error
- superboogav2
- Python-import-error
- debugging
---
# did all that and got this: Closing server running on port: 7860
13:09:51-207989 INFO     Loading the extension "superboogav2"
13:09:54-449901 ERROR    Failed to load the extension "superboogav2".
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
ImportError: /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

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
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

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
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

Running on local URL:  http://127.0.0.1:7860

### USER
did all that and got this: Closing server running on port: 7860
13:09:51-207989 INFO     Loading the extension "superboogav2"
13:09:54-449901 ERROR    Failed to load the extension "superboogav2".
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
ImportError: /home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

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
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

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
/home/bryan_/text-generation-webui/.venv/lib/python3.11/site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Thank you for the update. It's good that you provided the full output, as the error message is almost identical, but the specific "undefined symbol" has subtly changed from _ZN3c105ErrorC2ENS_14SourceLocationESs to _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv. Both still point to a core incompatibility with flash_attn_2_cuda and your PyTorch/CUDA setup, likely stemming from how flash_attn expects to interact with the underlying PyTorch c10 (core tensor library) components. This typically happens when flash_attn (or a component that relies on it, like parts of transformers) was built for a slightly different CUDA/PyTorch ABI (Application Binary Interface) than what's currently installed. Your RTX 3070 should certainly support Flash Attention, but getting the versions to align can be tricky. Since the error explicitly states it's within flash_attn_2_cuda, and that's preventing superboogav2 from loading, we have two main paths: Option A (Recommended for immediate progress): Disable Flash Attention integration. This will allow superboogav2 to load, and you can start using the RAG functionality. Your model will still use its default (but slightly less optimized) attention mechanism. We can revisit optimizing with Flash Attention later, once the core RAG is working. Option B (More complex, for deeper optimization): Manually install/recompile Flash Attention. This involves more advanced steps, potentially uninstalling existing flash_attn packages, and trying to install a specific version that matches your torch and CUDA. This is generally more involved and can lead to more troubleshooting. Given your goal to get the Helpdesk AI assistant up and running, let's go with Option A for now. We can tell Oobabooga's transformers integration to avoid using flash_attn. Step 6: Disable Flash Attention for superboogav2 compatibility. We can achieve this by setting an environment variable before launching Oobabooga, which tells transformers not to try and load flash_attn. Action: Stop Oobabooga again. (If it's still running). Press Ctrl + C in the terminal until you see your prompt. Ensure your virtual environment is active. (You should see (.venv)). If not: cd ~/text-generation-webui source .venv/bin/activate Launch Oobabooga with the TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF environment variable set to 0. This tells the transformers library to explicitly disable Flash Attention. TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0 python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Explanation of changes: TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0: This is the new part. It's an environment variable that prevents transformers from trying to use the flash_attn_cuda module, which is causing your ImportError. --extensions superboogav2: I've also added this to your start command. While you can enable extensions in the UI, adding them to the start command ensures they are loaded from the beginning and helps confirm they're being picked up. Important: You do not need to "Save" the extension in the Oobabooga UI if you specify it with --extensions in the command line. However, if you enabled it in the UI and clicked save, it's already written to your config.json and will attempt to load on its own. Adding it to the command line will ensure it's explicitly loaded if it's somehow not saved or if you want to bypass the UI setting for troubleshooting. If it loads via the command line, you should see the SuperBooga tab. Please try starting Oobabooga with this modified command. Pay close attention to the output in the terminal. We're looking for the Failed to load the extension "superboogav2" error to disappear and for Oobabooga to start normally, indicating superboogav2 loaded successfully. If you still get an error, please paste it. If it starts successfully, check for the "SuperBooga" tab in the web UI.