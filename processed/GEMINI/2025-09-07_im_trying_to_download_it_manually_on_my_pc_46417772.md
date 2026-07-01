---
id: 806556
source: GEMINI
date: 2025-09-07
tags: ['manual-download', 'software-installation']
category: general
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is attempting to manually download something onto his computer.
---
# i'm trying to download it manually on my pc 

### USER
i'm trying to download it manually on my pc 

### GEMINI
While git clone with git-lfs is the most common and recommended way to download large models, you can also download the files manually. This is a good option if you only need a few specific files or if you're having trouble with the command-line tools. Here's how to do it: Navigate to the Files and Versions Tab: From the model's main page on Hugging Face, click on the "Files and versions" tab. This is the tab you have a screenshot of. Click on the Download Arrow: For each file you want to download, you'll see a small download icon (a down arrow) to the right of the file size. Download Each File Manually: Click the download arrow for each of the files you need. This will trigger a download of the individual file to your computer. Important: You need to download all the files listed in the repository to have the complete model. This includes the .safetensors files, the .json configuration files (config.json, generation_config.json, etc.), and the tokenizer files (tokenizer.model, tokenizer_config.json, etc.). Save in a Single Folder: Create a new folder on your computer and save all the downloaded files into that folder. The model will not work unless all the necessary files are in the same directory. A note about large files: The .safetensors files are typically very large (as seen in your screenshot, they are 4.94 GB and 5 GB). Downloading these manually through your browser can be slow and may fail on an unstable connection. If you have any issues, the command-line approach with git-lfs or the Hugging Face CLI is generally more robust for handling large files. Alternative manual method using the Hugging Face CLI: If you don't want to use git-lfs, but are comfortable with the command line, you can install the huggingface_hub Python library and use its built-in download command. This is often faster and more reliable than a browser download. Install the library: pip install huggingface_hub Use the download command: huggingface-cli download Nous-Hermes-2-Mistral-7B-DPO This command will download all the files in the repository and place them in a local cache directory. You can specify a different directory with the --local-dir option.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
