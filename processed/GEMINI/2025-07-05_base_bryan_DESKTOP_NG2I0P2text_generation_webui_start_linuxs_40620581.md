---
id: 214402
source: GEMINI
date: 2025-07-05
tags: ['coding', 'llm', 'ai', 'gemini', 'model', 'oobabooga', 'gguf', 'lora']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh --update-only
usage: server.py [-h] [--multi-user] [--model MODEL] [--lora LORA [LORA ...]] [--model-dir MODEL_DIR] [--lora-dir LORA_DIR] [--model-menu] [--settings SETTINGS]
                 [--extensions EXTENSIONS [EXTENSIONS ...]] [--verbose] [--idle-timeout IDLE_TIMEOUT] [--loader LOADER] [--cpu] [--cpu-memory CPU_MEMORY] [--disk] [--disk-cache-dir DISK_CACHE_DIR]
                 [--load-in-8bit] [--bf16] [--no-cache] [--trust-remote-code] [--force-safetensors] [--no_use_fast] [--use_flash_attention_2] [--use_eager_attention] [--torch-compile] [--load-in-4bit]
                 [--use_double_quant] [--compute_dtype COMPUTE_DTYPE] [--quant_type QUANT_TYPE] [--flash-attn] [--threads THREADS] [--threads-batch THREADS_BATCH] [--batch-size BATCH_SIZE] [--no-mmap]
                 [--mlock] [--gpu-layers N] [--tensor-split TENSOR_SPLIT] [--numa] [--no-kv-offload] [--row-split] [--extra-flags EXTRA_FLAGS] [--streaming-llm] [--ctx-size N] [--cache-type N]
                 [--model-draft MODEL_DRAFT] [--draft-max DRAFT_MAX] [--gpu-layers-draft GPU_LAYERS_DRAFT] [--device-draft DEVICE_DRAFT] [--ctx-size-draft CTX_SIZE_DRAFT] [--gpu-split GPU_SPLIT]
                 [--autosplit] [--cfg-cache] [--no_flash_attn] [--no_xformers] [--no_sdpa] [--num_experts_per_token N] [--enable_tp] [--cpp-runner] [--deepspeed] [--nvme-offload-dir NVME_OFFLOAD_DIR]
                 [--local_rank LOCAL_RANK] [--alpha_value ALPHA_VALUE] [--rope_freq_base ROPE_FREQ_BASE] [--compress_pos_emb COMPRESS_POS_EMB] [--listen] [--listen-port LISTEN_PORT]
                 [--listen-host LISTEN_HOST] [--share] [--auto-launch] [--gradio-auth GRADIO_AUTH] [--gradio-auth-path GRADIO_AUTH_PATH] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE]
                 [--subpath SUBPATH] [--old-colors] [--portable] [--api] [--public-api] [--public-api-id PUBLIC_API_ID] [--api-port API_PORT] [--api-key API_KEY] [--admin-key ADMIN_KEY]
                 [--api-enable-ipv6] [--api-disable-ipv4] [--nowebui]
server.py: error: unrecognized arguments: --update-only
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh --update-only
usage: server.py [-h] [--multi-user] [--model MODEL] [--lora LORA [LORA ...]] [--model-dir MODEL_DIR] [--lora-dir LORA_DIR] [--model-menu] [--settings SETTINGS]
                 [--extensions EXTENSIONS [EXTENSIONS ...]] [--verbose] [--idle-timeout IDLE_TIMEOUT] [--loader LOADER] [--cpu] [--cpu-memory CPU_MEMORY] [--disk] [--disk-cache-dir DISK_CACHE_DIR]
                 [--load-in-8bit] [--bf16] [--no-cache] [--trust-remote-code] [--force-safetensors] [--no_use_fast] [--use_flash_attention_2] [--use_eager_attention] [--torch-compile] [--load-in-4bit]
                 [--use_double_quant] [--compute_dtype COMPUTE_DTYPE] [--quant_type QUANT_TYPE] [--flash-attn] [--threads THREADS] [--threads-batch THREADS_BATCH] [--batch-size BATCH_SIZE] [--no-mmap]
                 [--mlock] [--gpu-layers N] [--tensor-split TENSOR_SPLIT] [--numa] [--no-kv-offload] [--row-split] [--extra-flags EXTRA_FLAGS] [--streaming-llm] [--ctx-size N] [--cache-type N]
                 [--model-draft MODEL_DRAFT] [--draft-max DRAFT_MAX] [--gpu-layers-draft GPU_LAYERS_DRAFT] [--device-draft DEVICE_DRAFT] [--ctx-size-draft CTX_SIZE_DRAFT] [--gpu-split GPU_SPLIT]
                 [--autosplit] [--cfg-cache] [--no_flash_attn] [--no_xformers] [--no_sdpa] [--num_experts_per_token N] [--enable_tp] [--cpp-runner] [--deepspeed] [--nvme-offload-dir NVME_OFFLOAD_DIR]
                 [--local_rank LOCAL_RANK] [--alpha_value ALPHA_VALUE] [--rope_freq_base ROPE_FREQ_BASE] [--compress_pos_emb COMPRESS_POS_EMB] [--listen] [--listen-port LISTEN_PORT]
                 [--listen-host LISTEN_HOST] [--share] [--auto-launch] [--gradio-auth GRADIO_AUTH] [--gradio-auth-path GRADIO_AUTH_PATH] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE]
                 [--subpath SUBPATH] [--old-colors] [--portable] [--api] [--public-api] [--public-api-id PUBLIC_API_ID] [--api-port API_PORT] [--api-key API_KEY] [--admin-key ADMIN_KEY]
                 [--api-enable-ipv6] [--api-disable-ipv4] [--nowebui]
server.py: error: unrecognized arguments: --update-only
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
My apologies, Bryan! You are absolutely correct. I made a mistake in assuming start_linux.sh supported the --update-only flag directly for updating dependencies in all Oobabooga versions. It seems your version (or the standard one) doesn't recognize it. That flag is usually for the one_click.py installer, or a newer version of the start_linux.sh script than what you have. The traceback you got confirms that the argument --update-only is not recognized by server.py, which is what start_linux.sh effectively calls. Instead of start_linux.sh --update-only, we need to run the installation script itself to perform an update or dependency check. This is typically python install.py or similar, but given your structure, the easiest way to ensure dependencies are met within the installer_files/env is often to just re-run the main installation process. Let's try a different approach to ensure dependencies are installed. The start_linux.sh script itself is designed to set up the environment. Corrected Solution: Run start_linux.sh without arguments to ensure environment setup If you run start_linux.sh without any arguments, it generally performs checks and installs missing dependencies before launching the web UI. Ensure you are in your Oobabooga directory in the second WSL2 terminal: cd ~/text-generation-webui (Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$) Run the start_linux.sh script without any flags. ./start_linux.sh This script is designed to activate the correct environment and install any missing Python packages (like gradio). It will then launch the web UI. Let this script run completely. It might take some time if it needs to install dependencies. You'll see many lines of output related to package installation. Once it's done, it will launch the Oobabooga web UI and typically print addresses like http://127.0.0.1:7860 and http://127.0.0.1:5000 (for the API). After start_linux.sh has fully completed and the Oobabooga web UI is running, you'll then need to stop it (Ctrl+C) and restart it with the --model and --api flags as intended. Stop Oobabooga by pressing Ctrl + C (you might need to press it a couple of times). Restart Oobabooga with your model and API: python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api Wait for the model to load fully and for the Uvicorn running on http://127.0.0.1:5000 message. Please try these corrected steps. First, run ./start_linux.sh (without arguments) to ensure all dependencies are met. Then, stop it, and restart with python server.py --model ... --api. Paste the output after you run the final python server.py command. This should finally get Oobabooga running correctly with the model loaded and the API enabled.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]