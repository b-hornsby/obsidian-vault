---
id: 640776
source: GEMINI
date: 2025-07-05
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf', 'embedding']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# when i go to speak, it gives this in the terminal: 13:43:01-888257 INFO     Output generated in 7.52 seconds (5.32 tokens/s, 40 tokens, context 362, seed 722626693)
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/queueing.py", line 541, in process_events
    response = await route_utils.call_process_api(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/route_utils.py", line 276, in call_process_api
    output = await app.get_blocks().process_api(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1928, in process_api
    result = await self.call_function(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1514, in call_function
    prediction = await anyio.to_thread.run_sync(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/utils.py", line 833, in wrapper
    response = f(*args, **kwargs)
               ^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 62, in auto_transcribe
    transcription = do_stt(audio_bytes, whipser_language)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 41, in do_stt
    dubaudio = AudioSegment.from_file(io.BytesIO(audio))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/audio_segment.py", line 728, in from_file
    info = mediainfo_json(orig_file, read_ahead_limit=read_ahead_limit)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/utils.py", line 274, in mediainfo_json
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/subprocess.py", line 1955, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe'
13:43:35-605596 INFO     Successfully deleted 5 records from chromaDB.
13:43:35-713552 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 452, n_tokens = 145, progress = 0.320796
prompt eval time =    2546.41 ms /   145 tokens (   17.56 ms per token,    56.94 tokens per second)
       eval time =    1432.20 ms /    47 tokens (   30.47 ms per token,    32.82 tokens per second)
      total time =    3978.61 ms /   192 tokens
13:43:39-714371 INFO     Output generated in 3.98 seconds (12.07 tokens/s, 48 tokens, context 452, seed 828843966)

### USER
when i go to speak, it gives this in the terminal: 13:43:01-888257 INFO     Output generated in 7.52 seconds (5.32 tokens/s, 40 tokens, context 362, seed 722626693)
/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/queueing.py", line 541, in process_events
    response = await route_utils.call_process_api(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/route_utils.py", line 276, in call_process_api
    output = await app.get_blocks().process_api(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1928, in process_api
    result = await self.call_function(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/blocks.py", line 1514, in call_function
    prediction = await anyio.to_thread.run_sync(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/gradio/utils.py", line 833, in wrapper
    response = f(*args, **kwargs)
               ^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 62, in auto_transcribe
    transcription = do_stt(audio_bytes, whipser_language)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/extensions/whisper_stt/script.py", line 41, in do_stt
    dubaudio = AudioSegment.from_file(io.BytesIO(audio))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/audio_segment.py", line 728, in from_file
    info = mediainfo_json(orig_file, read_ahead_limit=read_ahead_limit)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/site-packages/pydub/utils.py", line 274, in mediainfo_json
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/home/bryan_/text-generation-webui/installer_files/env/lib/python3.11/subprocess.py", line 1955, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe'
13:43:35-605596 INFO     Successfully deleted 5 records from chromaDB.
13:43:35-713552 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 452, n_tokens = 145, progress = 0.320796
prompt eval time =    2546.41 ms /   145 tokens (   17.56 ms per token,    56.94 tokens per second)
       eval time =    1432.20 ms /    47 tokens (   30.47 ms per token,    32.82 tokens per second)
      total time =    3978.61 ms /   192 tokens
13:43:39-714371 INFO     Output generated in 3.98 seconds (12.07 tokens/s, 48 tokens, context 452, seed 828843966)

### GEMINI
You've identified the problem! The key error here is: FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe' And the preceding warning: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work This means that the pydub library, which whisper_stt uses to process audio, relies on external tools called ffmpeg and ffprobe. These are command-line utilities for handling multimedia files (audio and video). Your system doesn't have them installed in a location where pydub can find them. Solution: Install ffmpeg and ffprobe in your WSL2 Ubuntu environment. Step 1: Install ffmpeg in WSL2 ffprobe is part of the ffmpeg package. You can install it using your system's package manager, apt. Stop Oobabooga: If Oobabooga is still running, press Ctrl+C in your WSL2 terminal to stop it. Update your package lists: sudo apt update (You may be asked for your WSL2 password.) Install ffmpeg: sudo apt install ffmpeg When prompted, type Y and press Enter to confirm the installation. Step 2: Restart Oobabooga After ffmpeg is successfully installed, restart Oobabooga. ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Step 3: Test Voice Input Again Go back to the Oobabooga web UI (http://127.0.0.1:7860). Navigate to the "Chat" tab. Click the microphone icon to record your voice. This time, you should no longer see the FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe' error in the terminal, and your voice should be successfully transcribed by whisper_stt. The superboogav2 RuntimeWarning: invalid value encountered in scalar divide is a separate, minor warning related to the RAG component and is usually harmless; it won't prevent STT from working. Focus on resolving the ffprobe error first.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]