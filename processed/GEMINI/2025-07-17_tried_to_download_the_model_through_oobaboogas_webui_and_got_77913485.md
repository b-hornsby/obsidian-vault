---
id: 068148
source: GEMINI
date: 2025-07-17
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'gguf', 'lora']
category: coding
sentiment: frustrated
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# tried to download the model through oobaboogas webui and got this:   File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 198, in _new_conn

sock = connection.create_connection(

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/connection.py",
 line 60, in create_connection

for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/socket.py", line 974, in getaddrinfo

for res in _socket.getaddrinfo(host, port, family, type, proto, flags):

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 787, in urlopen

response = self._make_request(

           ^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 488, in _make_request

raise new_e

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 464, in _make_request

self._validate_conn(conn)

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 1093, in _validate_conn

conn.connect()

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 753, in connect

self.sock = sock = self._new_conn()

                   ^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 205, in _new_conn

raise NameResolutionError(self.host, self, e) from e

urllib3.exceptions.NameResolutionError: 
<urllib3.connection.HTTPSConnection object at 0x7d016db15dd0>: 
Failed to resolve 'huggingface.co' ([Errno -3] Temporary failure in name
 resolution)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py",
 line 667, in send

resp = conn.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  [Previous line repeated 4 more times]
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 841, in urlopen

retries = retries.increment(

          ^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/retry.py",
 line 519, in increment

raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: 
HTTPSConnectionPool(host='huggingface.co', port=443): Max retries 
exceeded with url: 
/api/models/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main (Caused 
by NameResolutionError("<urllib3.connection.HTTPSConnection object at
 0x7d016db15dd0>: Failed to resolve 'huggingface.co' ([Errno -3] 
Temporary failure in name resolution)"))
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 248, in download_model_wrapper

links, sha256, is_lora, is_llamacpp, file_sizes = downloader.get_download_links_from_huggingface(model, branch, text_only=False, specific_file=specific_file)

                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/download-model.py", line 94, in get_download_links_from_huggingface

r = session.get(url, timeout=10)

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 602, in get

return self.request("GET", url, **kwargs)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 589, in request

resp = self.send(prep, **send_kwargs)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 703, in send

r = adapter.send(request, **kwargs)

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py",
 line 700, in send

raise ConnectionError(e, request=request)

requests.exceptions.ConnectionError: 
HTTPSConnectionPool(host='huggingface.co', port=443): Max retries 
exceeded with url: 
/api/models/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main (Caused 
by NameResolutionError("<urllib3.connection.HTTPSConnection object at
 0x7d016db15dd0>: Failed to resolve 'huggingface.co' ([Errno -3] 
Temporary failure in name resolution)"))

### USER
tried to download the model through oobaboogas webui and got this:   File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 198, in _new_conn

sock = connection.create_connection(

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/connection.py",
 line 60, in create_connection

for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/socket.py", line 974, in getaddrinfo

for res in _socket.getaddrinfo(host, port, family, type, proto, flags):

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 787, in urlopen

response = self._make_request(

           ^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 488, in _make_request

raise new_e

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 464, in _make_request

self._validate_conn(conn)

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 1093, in _validate_conn

conn.connect()

  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 753, in connect

self.sock = sock = self._new_conn()

                   ^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connection.py",
 line 205, in _new_conn

raise NameResolutionError(self.host, self, e) from e

urllib3.exceptions.NameResolutionError: 
<urllib3.connection.HTTPSConnection object at 0x7d016db15dd0>: 
Failed to resolve 'huggingface.co' ([Errno -3] Temporary failure in name
 resolution)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py",
 line 667, in send

resp = conn.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 871, in urlopen

return self.urlopen(

       ^^^^^^^^^^^^^
  [Previous line repeated 4 more times]
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/connectionpool.py",
 line 841, in urlopen

retries = retries.increment(

          ^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/urllib3/util/retry.py",
 line 519, in increment

raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: 
HTTPSConnectionPool(host='huggingface.co', port=443): Max retries 
exceeded with url: 
/api/models/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main (Caused 
by NameResolutionError("<urllib3.connection.HTTPSConnection object at
 0x7d016db15dd0>: Failed to resolve 'huggingface.co' ([Errno -3] 
Temporary failure in name resolution)"))
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/modules/ui_model_menu.py", line 248, in download_model_wrapper

links, sha256, is_lora, is_llamacpp, file_sizes = downloader.get_download_links_from_huggingface(model, branch, text_only=False, specific_file=specific_file)

                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/download-model.py", line 94, in get_download_links_from_huggingface

r = session.get(url, timeout=10)

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 602, in get

return self.request("GET", url, **kwargs)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 589, in request

resp = self.send(prep, **send_kwargs)

       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/sessions.py",
 line 703, in send

r = adapter.send(request, **kwargs)

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File 
"/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/requests/adapters.py",
 line 700, in send

raise ConnectionError(e, request=request)

requests.exceptions.ConnectionError: 
HTTPSConnectionPool(host='huggingface.co', port=443): Max retries 
exceeded with url: 
/api/models/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main (Caused 
by NameResolutionError("<urllib3.connection.HTTPSConnection object at
 0x7d016db15dd0>: Failed to resolve 'huggingface.co' ([Errno -3] 
Temporary failure in name resolution)"))

### GEMINI
It looks like you're encountering a network connectivity error when Oobabooga tries to download the model from Hugging Face directly. The key part of the error message is: socket.gaierror: [Errno -3] Temporary failure in name resolution and urllib3.exceptions.NameResolutionError: Failed to resolve 'huggingface.co' This means that your Oobabooga environment (specifically, the Python script trying to reach huggingface.co) is unable to translate the domain name huggingface.co into an IP address. This is a DNS (Domain Name System) resolution issue or a general network problem on the system where Oobabooga is running, not an issue with Oobabooga itself or the model. Common causes for this error: No internet connection: The system running Oobabooga might not have active internet access. DNS server issues: Your computer's DNS servers might be misconfigured or temporarily unavailable. Firewall/Antivirus: A firewall or antivirus software might be blocking Oobabooga's outgoing connection to huggingface.co. VPN/Proxy: If you're using a VPN or proxy, it might be interfering with DNS resolution or the connection. Troubleshooting Steps: Check your internet connection: Can you browse other websites (like Google, YouTube) from the same computer where Oobabooga is running? Try opening https://huggingface.co/ directly in your web browser on that machine. Does it load? Test DNS resolution (from your command line/terminal): On Windows: Open Command Prompt and type ping huggingface.co On Linux/macOS: Open Terminal and type ping huggingface.co You should see replies with IP addresses. If you get "Temporary failure in name resolution" or "Host not found," then it confirms a DNS issue. Temporarily disable firewall/VPN: If you have a firewall, antivirus, or VPN active, try temporarily disabling them and then attempt the download through Oobabooga again. Remember to re-enable them afterward. Restart your router/modem: A simple network device restart can sometimes resolve temporary DNS caching issues. The Most Reliable Workaround (Recommended for now): Since you have the direct download link, the easiest way to proceed is to download the model manually using your web browser and then place it in the correct Oobabooga folder. Download the model manually: Use the direct link your chat provided: https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf Paste this link into your web browser and press Enter. The download should start. Place the downloaded file: Once the download is complete, move the file (it will be named something like Meta-Llama-3-8B-Instruct-Q4_K_M.gguf) into your Oobabooga models directory. Based on your previous output, your Oobabooga installation seems to be in /home/bryan_/text-generation-webui/. So the target folder is: /home/bryan_/text-generation-webui/models/ Load the model in Oobabooga: Go back to your Oobabooga web UI. Navigate to the "Model" tab. Click the refresh icon next to the model dropdown list. Select Meta-Llama-3-8B-Instruct-Q4_K_M.gguf from the list. Click the "Load" button. This manual download method will bypass the network resolution issue Oobabooga is facing and allow you to get the model loaded and ready for your CrewAI workflow.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]