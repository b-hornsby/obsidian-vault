---
id: 663915
source: GEMINI
date: 2025-07-06
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'embedding', 'text-generation']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# when i boot it up it says:20:25:27-554379 ERROR    Failed to load the extension "superboogav2".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/socket.py", line 974, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

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
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py", line 37, in __init__
    self.models[model_name] = SentenceTransformer(
                              ^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 308, in __init__
    modules, self.module_kwargs = self._load_sbert_model(
                                  ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 1728, in _load_sbert_model
    module = module_class(model_name_or_path, cache_dir=cache_folder, backend=self.backend, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/models/Transformer.py", line 77, in __init__
    config = self._load_config(model_name_or_path, cache_dir, backend, config_args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/models/Transformer.py", line 105, in _load_config
    find_adapter_config_file(
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/peft_utils.py", line 88, in find_adapter_config_file
    adapter_cached_filename = cached_file(
                              ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/hub.py", line 403, in cached_file
    resolved_file = hf_hub_download(
                    ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1008, in hf_hub_download
    return _hf_hub_download_to_cache_dir(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1071, in _hf_hub_download_to_cache_dir
    (url_to_download, etag, commit_hash, expected_size, xet_file_data, head_call_error) = _get_metadata_or_catch_error(
                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1533, in _get_metadata_or_catch_error
    metadata = get_hf_file_metadata(
               ^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1450, in get_hf_file_metadata
    r = _request_wrapper(
        ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 286, in _request_wrapper
    response = _request_wrapper(
               ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 309, in _request_wrapper
    response = http_backoff(method=method, url=url, **params, retry_on_exceptions=(), retry_on_status_codes=(429,))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_http.py", line 310, in http_backoff
    response = session.request(method=method, url=url, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_http.py", line 96, in send
    return super().send(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 205, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
                              ^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 163, in host
    @property

  File "/home/bryan_/text-generation-webui/server.py", line 82, in signal_handler
    sys.exit(0)
SystemExit: 0

Running on local URL:  http://127.0.0.1:7860

### USER
when i boot it up it says:20:25:27-554379 ERROR    Failed to load the extension "superboogav2".
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/socket.py", line 974, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

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
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/chromadb/utils/embedding_functions/sentence_transformer_embedding_function.py", line 37, in __init__
    self.models[model_name] = SentenceTransformer(
                              ^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 308, in __init__
    modules, self.module_kwargs = self._load_sbert_model(
                                  ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/SentenceTransformer.py", line 1728, in _load_sbert_model
    module = module_class(model_name_or_path, cache_dir=cache_folder, backend=self.backend, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/models/Transformer.py", line 77, in __init__
    config = self._load_config(model_name_or_path, cache_dir, backend, config_args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/sentence_transformers/models/Transformer.py", line 105, in _load_config
    find_adapter_config_file(
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/peft_utils.py", line 88, in find_adapter_config_file
    adapter_cached_filename = cached_file(
                              ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/utils/hub.py", line 403, in cached_file
    resolved_file = hf_hub_download(
                    ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1008, in hf_hub_download
    return _hf_hub_download_to_cache_dir(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1071, in _hf_hub_download_to_cache_dir
    (url_to_download, etag, commit_hash, expected_size, xet_file_data, head_call_error) = _get_metadata_or_catch_error(
                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1533, in _get_metadata_or_catch_error
    metadata = get_hf_file_metadata(
               ^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 1450, in get_hf_file_metadata
    r = _request_wrapper(
        ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 286, in _request_wrapper
    response = _request_wrapper(
               ^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/file_download.py", line 309, in _request_wrapper
    response = http_backoff(method=method, url=url, **params, retry_on_exceptions=(), retry_on_status_codes=(429,))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_http.py", line 310, in http_backoff
    response = session.request(method=method, url=url, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/huggingface_hub/utils/_http.py", line 96, in send
    return super().send(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 753, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 205, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
                              ^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py", line 163, in host
    @property

  File "/home/bryan_/text-generation-webui/server.py", line 82, in signal_handler
    sys.exit(0)
SystemExit: 0

Running on local URL:  http://127.0.0.1:7860

### GEMINI
You're getting a NameResolutionError when superboogav2 tries to load. This means your WSL2 environment, or the Python environment within it, is having trouble connecting to the internet to download a component needed by superboogav2. Specifically, the traceback shows: socket.gaierror: [Errno -3] Temporary failure in name resolution This is a DNS (Domain Name System) error. Your system can't convert a hostname (like huggingface.co where superboogav2 tries to download embedding models) into an IP address. Here's what's happening and how to fix it: superboogav2 uses sentence-transformers for embeddings. When it initializes, it tries to download the necessary embedding model from Hugging Face Hub (e.g., sentence-transformers/all-MiniLM-L6-v2). The NameResolutionError indicates that your WSL2 instance can't resolve the domain name (huggingface.co) needed to fetch this model. How to Fix NameResolutionError This is usually a network configuration issue within WSL2 or a temporary internet problem. 1. Check Your Internet Connection in WSL2 First, ensure your WSL2 instance has working internet access. Open your WSL2 terminal. Try to ping a well-known website: ping google.com If you get replies, your basic internet connection is likely fine. If you get "Temporary failure in name resolution" or similar, then it's a deeper DNS issue within WSL2. 2. Restart WSL2 (Most Common Fix) Sometimes, WSL2's network components can get into a bad state. A full restart often resolves this. Close your WSL2 terminal(s). Open PowerShell or Command Prompt (on Windows) as Administrator. Run this command to completely terminate WSL2: wsl --shutdown Wait a few seconds for it to complete. Restart your WSL2 terminal. Try booting Oobabooga again. 3. Flush DNS Cache (Windows) While less likely to be the primary cause if the issue is within WSL2, flushing your Windows DNS cache can sometimes help if the problem is propagating from the host. Open Command Prompt (on Windows) as Administrator. Run: ipconfig /flushdns 4. Manually Configure DNS in WSL2 (If the above fails) If the issue persists, you might need to force WSL2 to use a reliable DNS server, like Google's or Cloudflare's. Stop Oobabooga and close all WSL2 terminals. Open a new WSL2 terminal. Create or edit the resolv.conf file: sudo nano /etc/resolv.conf Delete all existing lines in this file. Add the following two lines (Google's DNS servers): nameserver 8.8.8.8 nameserver 8.8.4.4 Alternatively, you can use Cloudflare's DNS: nameserver 1.1.1.1 nameserver 1.0.0.1 Save the file (Ctrl+O, then Enter, then Ctrl+X). Prevent WSL2 from overwriting this file: sudo chattr +i /etc/resolv.conf This command makes the file immutable. If you ever need to change it again, you'll first run sudo chattr -i /etc/resolv.conf. Run wsl --shutdown from Windows PowerShell/CMD (as Administrator) again. Restart your WSL2 terminal and try Oobabooga. 5. Check Firewall/Antivirus (Less common, but possible) Ensure your Windows firewall or any antivirus software isn't blocking network connections specifically for your WSL2 virtual network adapter or Python processes trying to reach huggingface.co. The most likely solution is Step 2 (restarting WSL2). If that doesn't work, Step 4 (manual DNS configuration) is the next best bet.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]