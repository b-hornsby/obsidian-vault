---
id: 924903
source: GEMINI
date: 2025-06-24
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'llama.cpp']
category: coding
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0 python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:12:07-645067 INFO     Starting Text generation web UI
13:12:07-647618 INFO     Loading settings from "user_data/settings.yaml"
13:12:07-649104 INFO     Loading the extension "superboogav2"
13:12:10-631279 ERROR    Failed to load the extension "superboogav2".
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
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0 python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:12:07-645067 INFO     Starting Text generation web UI
13:12:07-647618 INFO     Loading settings from "user_data/settings.yaml"
13:12:07-649104 INFO     Loading the extension "superboogav2"
13:12:10-631279 ERROR    Failed to load the extension "superboogav2".
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
Thank you for running that, and for the full output. This is a persistent and tricky error! It seems TRANSFORMERS_FLASH_ATTN_CUDA_HANDOFF=0 is not sufficient to prevent sentence-transformers from attempting to import components that rely on Flash Attention, or perhaps an underlying dependency is still trying to load it. The error undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv clearly indicates a deep-seated PyTorch/CUDA/Flash Attention incompatibility within your environment. Since we explicitly disabled it, and it's still trying to import it, this suggests that the flash_attn package itself is installed in your .venv and causing conflicts, even if transformers is told not to use it directly. The superboogav2 extension (specifically sentence_transformers) seems to have a strong dependency chain that gets tangled up by this flash_attn installation. To move forward, the most reliable way to bypass this specific error right now is to uninstall flash-attn from your virtual environment. This will remove the problematic module and force transformers and sentence-transformers to use their fallback, non-Flash Attention implementations, which should allow superboogav2 to load. We can always try to reinstall and reconfigure flash-attn later for maximum performance, but for now, getting the core RAG functionality working is the priority. Step 7: Uninstall flash-attn from the virtual environment. Action: Stop Oobabooga again. (If it's still running). Press Ctrl + C in the terminal until you see your prompt. Ensure your virtual environment is active. (You should see (.venv)). If not: cd ~/text-generation-webui source .venv/bin/activate Uninstall flash-attn: pip uninstall flash-attn When prompted, type y and press Enter to confirm the uninstallation. There might be some related packages. If pip suggests uninstalling other packages alongside flash-attn, for now, agree to it (y). We just want to get this core conflict resolved. Once flash-attn is uninstalled, we will try starting Oobabooga and loading superboogav2 again. Please paste the output of the pip uninstall command.