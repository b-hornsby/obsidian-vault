---
category: homelab
date: 2025-06-23
id: 920103
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
- private-ai-consulting
resolution: resolved
sentiment: executing
source: GEMINI
summary: The user successfully loaded a quantized LLM model with GPU acceleration
  on their local homelab setup, confirming the infrastructure is operational.
tags:
- local-llm
- gpu-acceleration
- model-loading
- cuda-setup
- infrastructure
---
# 14:43:44-528490 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:43:44-532425 INFO     Using gpu_layers=21 | ctx_size=8192 | cache_type=fp16
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 3070, compute capability 8.6, VMM: yes
build: 1 (b548c7c) with cc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 for x86_64-linux-gnu
system info: n_threads = 10, n_threads_batch = 10, total_threads = 20

system_info: n_threads = 10 (n_threads_batch = 10) / 20 | CUDA : ARCHS = 500,520,530,600,610,620,700,720,750,800,860,870,890,900 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 |

Web UI is disabled
main: binding port with default address family
main: HTTP server is listening, hostname: 127.0.0.1, port: 53767, http threads: 19
main: loading model
llama_model_load_from_file_impl: using device CUDA0 (NVIDIA GeForce RTX 3070) - 7100 MiB free
llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = models
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 17
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  18:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  19:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% for message in messages %}{{'<|im_...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q5_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q5_K - Medium
print_info: file size   = 4.78 GiB (5.67 BPW)
load: control-looking token:  32000 '<|im_end|>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: ssm_d_conv       = 0
print_info: ssm_d_inner      = 0
print_info: ssm_d_state      = 0
print_info: ssm_dt_rank      = 0
print_info: ssm_dt_b_c_rms   = 0
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = models
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|im_end|>'
print_info: EOT token        = 32000 '<|im_end|>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|im_end|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors: offloading 21 repeating layers to GPU
load_tensors: offloaded 21/33 layers to GPU
load_tensors:        CUDA0 model buffer size =  3083.34 MiB
load_tensors:   CPU_Mapped model buffer size =  4893.00 MiB
...................................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 8192
llama_context: n_ctx_per_seq = 8192
llama_context: n_batch       = 256
llama_context: n_ubatch      = 256
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (8192) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.12 MiB
llama_kv_cache_unified:      CUDA0 KV buffer size =   672.00 MiB
llama_kv_cache_unified:        CPU KV buffer size =   352.00 MiB
llama_kv_cache_unified: size = 1024.00 MiB (  8192 cells,  32 layers,  1 seqs), K (f16):  512.00 MiB, V (f16):  512.00 MiB
llama_context:      CUDA0 compute buffer size =   315.00 MiB
llama_context:  CUDA_Host compute buffer size =    12.00 MiB
llama_context: graph nodes  = 1158
llama_context: graph splits = 125 (with bs=256), 3 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 8192
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: model loaded
main: chat template, chat_template: {% for message in messages %}{{'<|im_start|>' + message['role'] + '
' + message['content'] + '<|im_end|>' + '
'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant
' }}{% endif %}, example_format: '<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
'
main: server is listening on http://127.0.0.1:53767 - starting the main loop
14:43:49-605673 INFO     Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" in 5.08 seconds.
14:43:49-606543 INFO     LOADER: "llama.cpp"
14:43:49-607050 INFO     TRUNCATION LENGTH: 8192
14:43:49-607500 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"

### USER
14:43:44-528490 INFO     Loading "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf"
14:43:44-532425 INFO     Using gpu_layers=21 | ctx_size=8192 | cache_type=fp16
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 3070, compute capability 8.6, VMM: yes
build: 1 (b548c7c) with cc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 for x86_64-linux-gnu
system info: n_threads = 10, n_threads_batch = 10, total_threads = 20

system_info: n_threads = 10 (n_threads_batch = 10) / 20 | CUDA : ARCHS = 500,520,530,600,610,620,700,720,750,800,860,870,890,900 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 |

Web UI is disabled
main: binding port with default address family
main: HTTP server is listening, hostname: 127.0.0.1, port: 53767, http threads: 19
main: loading model
llama_model_load_from_file_impl: using device CUDA0 (NVIDIA GeForce RTX 3070) - 7100 MiB free
llama_model_loader: loaded meta data with 22 key-value pairs and 291 tensors from user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = models
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 17
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  18:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  19:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  20:                    tokenizer.chat_template str              = {% for message in messages %}{{'<|im_...
llama_model_loader: - kv  21:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q5_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q5_K - Medium
print_info: file size   = 4.78 GiB (5.67 BPW)
load: control-looking token:  32000 '<|im_end|>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: ssm_d_conv       = 0
print_info: ssm_d_inner      = 0
print_info: ssm_d_state      = 0
print_info: ssm_dt_rank      = 0
print_info: ssm_dt_b_c_rms   = 0
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = models
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|im_end|>'
print_info: EOT token        = 32000 '<|im_end|>'
print_info: UNK token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|im_end|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors: offloading 21 repeating layers to GPU
load_tensors: offloaded 21/33 layers to GPU
load_tensors:        CUDA0 model buffer size =  3083.34 MiB
load_tensors:   CPU_Mapped model buffer size =  4893.00 MiB
...................................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 8192
llama_context: n_ctx_per_seq = 8192
llama_context: n_batch       = 256
llama_context: n_ubatch      = 256
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (8192) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.12 MiB
llama_kv_cache_unified:      CUDA0 KV buffer size =   672.00 MiB
llama_kv_cache_unified:        CPU KV buffer size =   352.00 MiB
llama_kv_cache_unified: size = 1024.00 MiB (  8192 cells,  32 layers,  1 seqs), K (f16):  512.00 MiB, V (f16):  512.00 MiB
llama_context:      CUDA0 compute buffer size =   315.00 MiB
llama_context:  CUDA_Host compute buffer size =    12.00 MiB
llama_context: graph nodes  = 1158
llama_context: graph splits = 125 (with bs=256), 3 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 8192
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: model loaded
main: chat template, chat_template: {% for message in messages %}{{'<|im_start|>' + message['role'] + '
' + message['content'] + '<|im_end|>' + '
'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant
' }}{% endif %}, example_format: '<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
'
main: server is listening on http://127.0.0.1:53767 - starting the main loop
14:43:49-605673 INFO     Loaded "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" in 5.08 seconds.
14:43:49-606543 INFO     LOADER: "llama.cpp"
14:43:49-607050 INFO     TRUNCATION LENGTH: 8192
14:43:49-607500 INFO     INSTRUCTION TEMPLATE: "Custom (obtained from model metadata)"

### GEMINI
Excellent, Bryan! This is fantastic news! The output you've provided confirms that: Oobabooga has successfully started and is running. llama.cpp has correctly detected and is using your NVIDIA GeForce RTX 3070 GPU! The Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf model has loaded successfully and offloaded layers to your GPU. This is precisely what we wanted to achieve by downgrading Python and installing llama-cpp-binaries. This means the core issue has been resolved, and your setup is now working as intended for GPU inference! Step 23: Access the Web UI and Interact with the Model Action: Open your web browser and navigate to the address where Oobabooga is serving the UI. What you need to do now: Open a web browser on your Windows machine. Go to the following URL: http://127.0.0.1:53767 (Note: The port 53767 is shown in your terminal output: main: HTTP server is listening, hostname: 127.0.0.1, port: 53767). Once the Web UI loads, you should see the interface for text-generation-webui. On the left panel, click on the "Model" tab (or "Text Generation" tab, depending on the exact version/layout). You should see "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" listed and selected. Go to the "Chat" tab. This is where you can interact with your model. Type a message into the input box and press Enter or click the "Generate" button. What I need from you: Confirm that the web UI loads correctly in your browser. Let me know if you are able to interact with the model and get responses. Congratulations, you've overcome the biggest hurdle!