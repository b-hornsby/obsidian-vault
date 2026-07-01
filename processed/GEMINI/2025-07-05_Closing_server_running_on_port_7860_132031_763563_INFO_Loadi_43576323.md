---
id: 042064
source: GEMINI
date: 2025-07-05
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# Closing server running on port: 7860
13:20:31-763563 INFO     Loading the extension "superboogav2"
13:20:31-765660 INFO     Loading the extension "web_rag"
13:20:31-766121 INFO     Loading the extension "whisper_stt"
13:20:31-769896 ERROR    Could not import the requirements for 'whisper_stt'. Make sure to install the requirements for
                         the extension.

                         * To install requirements for all available extensions, launch the
                           update_wizard script for your OS and choose the B option.

                         * To install the requirements for this extension alone, launch the
                           cmd script for your OS and paste the following command in the
                           terminal window that appears:

                         Linux / Mac:

                         pip install -r extensions/whisper_stt/requirements.txt --upgrade

                         Windows:

                         pip install -r extensions\whisper_stt\requirements.txt --upgrade

13:20:31-771297 ERROR    Failed to load the extension "whisper_stt".
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
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 9, in <module>
    import whisper
ModuleNotFoundError: No module named 'whisper'
13:20:31-772248 INFO     Loading the extension "coqui_tts"
13:20:31-774554 ERROR    Could not import the requirements for 'coqui_tts'. Make sure to install the requirements for
                         the extension.

                         * To install requirements for all available extensions, launch the
                           update_wizard script for your OS and choose the B option.

                         * To install the requirements for this extension alone, launch the
                           cmd script for your OS and paste the following command in the
                           terminal window that appears:

                         Linux / Mac:

                         pip install -r extensions/coqui_tts/requirements.txt --upgrade

                         Windows:

                         pip install -r extensions\coqui_tts\requirements.txt --upgrade

13:20:31-775596 ERROR    Failed to load the extension "coqui_tts".
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
ModuleNotFoundError: No module named 'TTS'

Running on local URL:  http://127.0.0.1:7860

### USER
Closing server running on port: 7860
13:20:31-763563 INFO     Loading the extension "superboogav2"
13:20:31-765660 INFO     Loading the extension "web_rag"
13:20:31-766121 INFO     Loading the extension "whisper_stt"
13:20:31-769896 ERROR    Could not import the requirements for 'whisper_stt'. Make sure to install the requirements for
                         the extension.

                         * To install requirements for all available extensions, launch the
                           update_wizard script for your OS and choose the B option.

                         * To install the requirements for this extension alone, launch the
                           cmd script for your OS and paste the following command in the
                           terminal window that appears:

                         Linux / Mac:

                         pip install -r extensions/whisper_stt/requirements.txt --upgrade

                         Windows:

                         pip install -r extensions\whisper_stt\requirements.txt --upgrade

13:20:31-771297 ERROR    Failed to load the extension "whisper_stt".
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
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 9, in <module>
    import whisper
ModuleNotFoundError: No module named 'whisper'
13:20:31-772248 INFO     Loading the extension "coqui_tts"
13:20:31-774554 ERROR    Could not import the requirements for 'coqui_tts'. Make sure to install the requirements for
                         the extension.

                         * To install requirements for all available extensions, launch the
                           update_wizard script for your OS and choose the B option.

                         * To install the requirements for this extension alone, launch the
                           cmd script for your OS and paste the following command in the
                           terminal window that appears:

                         Linux / Mac:

                         pip install -r extensions/coqui_tts/requirements.txt --upgrade

                         Windows:

                         pip install -r extensions\coqui_tts\requirements.txt --upgrade

13:20:31-775596 ERROR    Failed to load the extension "coqui_tts".
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
ModuleNotFoundError: No module named 'TTS'

Running on local URL:  http://127.0.0.1:7860

### GEMINI
You're running into a very common issue when enabling new Oobabooga extensions: missing Python requirements. The error messages are clear and helpful: ERROR Could not import the requirements for 'whisper_stt'. Make sure to install the requirements for the extension. ModuleNotFoundError: No module named 'whisper' (for whisper_stt) ERROR Could not import the requirements for 'coqui_tts'. Make sure to install the requirements for the extension. ModuleNotFoundError: No module named 'TTS' (for coqui_tts) This means the Python libraries that whisper_stt and coqui_tts rely on (like the whisper library itself, and the TTS library from Coqui) are not installed in Oobabooga's virtual environment. Solution: Install the specific requirements for each extension. Step 1: Install whisper_stt Requirements Ensure you are in your Oobabooga root directory: cd ~/text-generation-webui Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Run the installation command for whisper_stt: ./installer_files/env/bin/pip install -r extensions/whisper_stt/requirements.txt --upgrade This command tells Oobabooga's Python environment to read the requirements.txt file specific to the whisper_stt extension and install all the listed packages. The --upgrade flag ensures you get the latest compatible versions. Step 2: Install coqui_tts Requirements While still in the Oobabooga root directory, run the installation command for coqui_tts: ./installer_files/env/bin/pip install -r extensions/coqui_tts/requirements.txt --upgrade This will do the same for the Coqui TTS library. Important: Both of these installations might take a little while as they download and compile various Python packages. Let each command complete fully before proceeding. You'll see a lot of installation messages scroll by. Step 3: Restart Oobabooga After both installations are complete, you need to restart the Oobabooga server again so it can properly load the newly installed libraries for the extensions. ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Monitor the terminal during this restart. If the installations were successful, you should no longer see the "Could not import the requirements" errors for whisper_stt and coqui_tts. Instead, you should see "Loading the extension" messages for them, without subsequent errors. Once Oobabooga fully loads, we can proceed to configure them in the web UI. Please execute these pip install commands and then restart, and let me know the new terminal output.