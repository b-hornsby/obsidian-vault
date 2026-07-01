---
category: ai-tools
date: 2025-09-07
id: 235943
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GPT
summary: Bryan was trying to download models from Hugging Face but couldn't find downloadable
  files in the Files and Versions tab, and was seeking help understanding why.
tags:
- huggingface
- model-download
- file-versions
- troubleshooting
---
# Hugging Face download issues

### ASSISTANT
Ah, I see exactly what you mean. This is a common situation with some Hugging Face repos, especially ones like Nous-Hermes-2-Mistral-7B-DPO. A few things to note from your screenshot:  

1. The **files are listed**, but there’s no explicit “Download” button for the whole model. Instead, each file has a small download arrow. You’d have to click each of these arrows individually to download them one by one.  

2. Some models on Hugging Face **require authentication** or accepting a license before downloading. Often for Nous-Hermes models, you need to be **logged in** and accept the model’s license before the download works. If you try downloading without accepting it, it may just show the files but not allow access.  

3. Hugging Face **doesn’t provide bulk download on the web UI** for large multi-file models like this. Instead, the recommended ways to download are:  
   - **Using `git-lfs`** (Git Large File Storage). You can clone the repo with:  
     ```bash
     git lfs install
     git clone https://huggingface.co/teknium/Nous-Hermes-2-Mistral-7B-DPO
     ```  
     This will automatically pull all the `.safetensors` and other large files.  
   - **Using the Hugging Face `transformers` library or `hf_hub_download`** if you want to pull individual files programmatically.  

If you want, I can write you the **exact commands to download the full Nous-Hermes-2-Mistral-7B-DPO model locally**, so you can load it in WSL2/oobabooga without having to click each file manually. Do you want me to do that?

### USER
{'asset_pointer': 'file-service://file-VHRHJjQeVyjjJCajgvxWkf', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1081, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 163307, 'width': 1217}it doesn't seem like the models are downloadable on hugging face? when i go to the files and versions tab it looks like this


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
